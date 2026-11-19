"""
Backlog Tools — MCP tools for the Planning phase.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import yaml
from mcp.server import Server
from mcp.types import Tool, TextContent


def register_backlog_tools(server: Server, get_project_dir: Callable[[], Path]):

    tools = [
        Tool(
            name="backlog_save_epic",
            description="Save an epic definition with RICE scores.",
            inputSchema={
                "type": "object",
                "properties": {
                    "epic_id": {"type": "string", "description": "e.g. EPIC-001"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "linked_features": {"type": "array", "items": {"type": "string"}},
                    "rice": {
                        "type": "object",
                        "properties": {
                            "reach": {"type": "number"},
                            "impact": {"type": "number"},
                            "confidence": {"type": "number"},
                            "effort": {"type": "number"},
                        },
                    },
                    "dependencies": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["epic_id", "title", "description"],
            },
        ),
        Tool(
            name="backlog_save_story",
            description="Save a user story following INVEST principles.",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_id": {"type": "string", "description": "e.g. US-001"},
                    "epic_id": {"type": "string"},
                    "title": {"type": "string"},
                    "narrative": {
                        "type": "object",
                        "properties": {
                            "as_a": {"type": "string"},
                            "i_want": {"type": "string"},
                            "so_that": {"type": "string"},
                        },
                        "required": ["as_a", "i_want", "so_that"],
                    },
                    "acceptance_criteria": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "given": {"type": "string"},
                                "when": {"type": "string"},
                                "then": {"type": "string"},
                            },
                        },
                    },
                    "story_points": {"type": "number"},
                    "priority": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
                },
                "required": ["story_id", "epic_id", "title", "narrative", "acceptance_criteria"],
            },
        ),
        Tool(
            name="backlog_save_roadmap",
            description="Save or update the product roadmap.",
            inputSchema={
                "type": "object",
                "properties": {
                    "phases": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "goal": {"type": "string"},
                                "epics": {"type": "array", "items": {"type": "string"}},
                                "duration": {"type": "string"},
                            },
                        },
                    },
                },
                "required": ["phases"],
            },
        ),
        Tool(
            name="backlog_list_epics",
            description="List all epics, sorted by RICE score.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="backlog_list_stories",
            description="List stories, optionally filtered by epic.",
            inputSchema={
                "type": "object",
                "properties": {
                    "epic_id": {"type": "string"},
                },
            },
        ),
        Tool(
            name="backlog_get_summary",
            description="Get a summary of the full backlog — epics, stories, points, readiness.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if not name.startswith("backlog_"):
            return []

        project_dir = get_project_dir()
        planning_dir = project_dir / "planning"
        planning_dir.mkdir(parents=True, exist_ok=True)

        if name == "backlog_save_epic":
            epics_dir = planning_dir / "epics"
            epics_dir.mkdir(exist_ok=True)
            filepath = epics_dir / f"{arguments['epic_id']}.yaml"
            rice = arguments.get("rice", {})
            if rice:
                effort = rice.get("effort", 1)
                score = (rice.get("reach", 0) * rice.get("impact", 0) * rice.get("confidence", 0)) / max(effort, 1)
                arguments["rice_score"] = round(score, 2)
            filepath.write_text(yaml.dump(arguments, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(filepath),
                "rice_score": arguments.get("rice_score"),
            }))]

        if name == "backlog_save_story":
            stories_dir = planning_dir / "stories"
            stories_dir.mkdir(exist_ok=True)
            filepath = stories_dir / f"{arguments['story_id']}.yaml"
            filepath.write_text(yaml.dump(arguments, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(filepath),
            }))]

        if name == "backlog_save_roadmap":
            filepath = planning_dir / "roadmap.yaml"
            filepath.write_text(yaml.dump({"phases": arguments["phases"]}, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(filepath),
            }))]

        if name == "backlog_list_epics":
            epics_dir = planning_dir / "epics"
            epics = []
            if epics_dir.exists():
                for f in sorted(epics_dir.glob("*.yaml")):
                    epics.append(yaml.safe_load(f.read_text()))
            epics.sort(key=lambda e: e.get("rice_score", 0), reverse=True)
            return [TextContent(type="text", text=json.dumps({"epics": epics, "count": len(epics)}))]

        if name == "backlog_list_stories":
            stories_dir = planning_dir / "stories"
            stories = []
            if stories_dir.exists():
                for f in sorted(stories_dir.glob("*.yaml")):
                    data = yaml.safe_load(f.read_text())
                    if arguments.get("epic_id") and data.get("epic_id") != arguments["epic_id"]:
                        continue
                    stories.append(data)
            return [TextContent(type="text", text=json.dumps({"stories": stories, "count": len(stories)}))]

        if name == "backlog_get_summary":
            epics_dir = planning_dir / "epics"
            stories_dir = planning_dir / "stories"
            epic_count = len(list(epics_dir.glob("*.yaml"))) if epics_dir.exists() else 0
            story_count = len(list(stories_dir.glob("*.yaml"))) if stories_dir.exists() else 0
            total_points = 0
            if stories_dir.exists():
                for f in stories_dir.glob("*.yaml"):
                    data = yaml.safe_load(f.read_text())
                    total_points += data.get("story_points", 0)
            roadmap_exists = (planning_dir / "roadmap.yaml").exists()
            return [TextContent(type="text", text=json.dumps({
                "epics": epic_count,
                "stories": story_count,
                "total_story_points": total_points,
                "roadmap_defined": roadmap_exists,
                "ready_for_architect": epic_count > 0 and story_count > 0 and roadmap_exists,
            }))]

        return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]
