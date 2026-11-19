"""
Product Discovery Tools — MCP tools for the Discovery phase.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import yaml
from mcp.server import Server
from mcp.types import Tool, TextContent


def register_product_tools(server: Server, get_project_dir: Callable[[], Path]):

    tools = [
        Tool(
            name="product_start_discovery",
            description="Start the discovery phase — kicks off idea intake with the Product Analyst.",
            inputSchema={
                "type": "object",
                "properties": {
                    "idea_summary": {"type": "string", "description": "One-line idea summary"},
                },
                "required": ["idea_summary"],
            },
        ),
        Tool(
            name="product_save_research",
            description="Save market research findings for a project.",
            inputSchema={
                "type": "object",
                "properties": {
                    "research_type": {"type": "string", "enum": ["market", "competitor", "user", "trend"]},
                    "title": {"type": "string"},
                    "content": {"type": "string", "description": "Research content in markdown"},
                },
                "required": ["research_type", "title", "content"],
            },
        ),
        Tool(
            name="product_save_vision",
            description="Save or update the product vision document.",
            inputSchema={
                "type": "object",
                "properties": {
                    "problem_statement": {"type": "string"},
                    "value_proposition": {"type": "string"},
                    "target_users": {"type": "string"},
                    "success_metrics": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["problem_statement", "value_proposition", "target_users"],
            },
        ),
        Tool(
            name="product_list_artifacts",
            description="List all discovery artifacts for the current project.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if not name.startswith("product_"):
            return []

        project_dir = get_project_dir()
        discovery_dir = project_dir / "discovery"
        discovery_dir.mkdir(parents=True, exist_ok=True)

        if name == "product_start_discovery":
            intake_file = discovery_dir / "idea-intake.yaml"
            data = {
                "idea_summary": arguments["idea_summary"],
                "status": "in_progress",
                "activities": {
                    "idea_intake": "in_progress",
                    "market_research": "not_started",
                    "pain_point_validation": "not_started",
                    "target_user_identification": "not_started",
                    "value_proposition": "not_started",
                    "idea_refinement": "not_started",
                },
            }
            intake_file.write_text(yaml.dump(data, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "started",
                "next": "Begin idea intake — ask the founder the 9 intake questions from the product-discovery skill.",
                "artifact": str(intake_file),
            }))]

        if name == "product_save_research":
            research_dir = discovery_dir / "research"
            research_dir.mkdir(exist_ok=True)
            slug = arguments["title"].lower().replace(" ", "-")
            filepath = research_dir / f"{arguments['research_type']}-{slug}.md"
            filepath.write_text(f"# {arguments['title']}\n\n{arguments['content']}")
            return [TextContent(type="text", text=json.dumps({
                "status": "saved",
                "artifact": str(filepath),
            }))]

        if name == "product_save_vision":
            vision_file = discovery_dir / "product-vision.yaml"
            data = {
                "problem_statement": arguments["problem_statement"],
                "value_proposition": arguments["value_proposition"],
                "target_users": arguments["target_users"],
                "success_metrics": arguments.get("success_metrics", []),
            }
            vision_file.write_text(yaml.dump(data, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved",
                "artifact": str(vision_file),
            }))]

        if name == "product_list_artifacts":
            artifacts = []
            if discovery_dir.exists():
                for f in discovery_dir.rglob("*"):
                    if f.is_file():
                        artifacts.append(str(f.relative_to(project_dir)))
            return [TextContent(type="text", text=json.dumps({"artifacts": artifacts}))]

        return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]
