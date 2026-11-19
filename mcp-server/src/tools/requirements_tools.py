"""
Requirements Tools — MCP tools for the Requirements phase.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import yaml
from mcp.server import Server
from mcp.types import Tool, TextContent


def register_requirements_tools(server: Server, get_project_dir: Callable[[], Path]):

    tools = [
        Tool(
            name="requirements_save_persona",
            description="Save a user persona definition.",
            inputSchema={
                "type": "object",
                "properties": {
                    "persona_id": {"type": "string", "description": "e.g. P-001"},
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "goals": {"type": "array", "items": {"type": "string"}},
                    "pain_points": {"type": "array", "items": {"type": "string"}},
                    "tech_comfort": {"type": "string", "enum": ["low", "medium", "high"]},
                },
                "required": ["persona_id", "name", "role", "goals", "pain_points"],
            },
        ),
        Tool(
            name="requirements_save_journey",
            description="Save a user journey map for a persona.",
            inputSchema={
                "type": "object",
                "properties": {
                    "persona_id": {"type": "string"},
                    "journey_name": {"type": "string"},
                    "steps": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "step": {"type": "string"},
                                "action": {"type": "string"},
                                "emotion": {"type": "string"},
                                "pain_point": {"type": "string"},
                                "opportunity": {"type": "string"},
                            },
                        },
                    },
                },
                "required": ["persona_id", "journey_name", "steps"],
            },
        ),
        Tool(
            name="requirements_save_requirement",
            description="Save a structured requirement with ID, priority, and MoSCoW classification.",
            inputSchema={
                "type": "object",
                "properties": {
                    "requirement_id": {"type": "string", "description": "e.g. REQ-001"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "type": {"type": "string", "enum": ["functional", "non_functional", "integration"]},
                    "moscow": {"type": "string", "enum": ["must", "should", "could", "wont"]},
                    "linked_personas": {"type": "array", "items": {"type": "string"}},
                    "linked_features": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["requirement_id", "title", "description", "type", "moscow"],
            },
        ),
        Tool(
            name="requirements_list_all",
            description="List all requirements, optionally filtered by type or MoSCoW priority.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filter_type": {"type": "string", "enum": ["functional", "non_functional", "integration"]},
                    "filter_moscow": {"type": "string", "enum": ["must", "should", "could", "wont"]},
                },
            },
        ),
    ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if not name.startswith("requirements_"):
            return []

        project_dir = get_project_dir()
        req_dir = project_dir / "requirements"
        req_dir.mkdir(parents=True, exist_ok=True)

        if name == "requirements_save_persona":
            personas_dir = req_dir / "personas"
            personas_dir.mkdir(exist_ok=True)
            filepath = personas_dir / f"{arguments['persona_id']}.yaml"
            filepath.write_text(yaml.dump(arguments, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(filepath),
            }))]

        if name == "requirements_save_journey":
            journeys_dir = req_dir / "journeys"
            journeys_dir.mkdir(exist_ok=True)
            slug = arguments["journey_name"].lower().replace(" ", "-")
            filepath = journeys_dir / f"{arguments['persona_id']}-{slug}.yaml"
            filepath.write_text(yaml.dump(arguments, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(filepath),
            }))]

        if name == "requirements_save_requirement":
            reqs_dir = req_dir / "specs"
            reqs_dir.mkdir(exist_ok=True)
            filepath = reqs_dir / f"{arguments['requirement_id']}.yaml"
            filepath.write_text(yaml.dump(arguments, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(filepath),
            }))]

        if name == "requirements_list_all":
            reqs_dir = req_dir / "specs"
            results = []
            if reqs_dir.exists():
                for f in sorted(reqs_dir.glob("*.yaml")):
                    data = yaml.safe_load(f.read_text())
                    if arguments.get("filter_type") and data.get("type") != arguments["filter_type"]:
                        continue
                    if arguments.get("filter_moscow") and data.get("moscow") != arguments["filter_moscow"]:
                        continue
                    results.append(data)
            return [TextContent(type="text", text=json.dumps({"requirements": results, "count": len(results)}))]

        return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]
