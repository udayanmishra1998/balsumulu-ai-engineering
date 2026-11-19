"""
PRD Tools — MCP tools for the Specification phase.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import yaml
from mcp.server import Server
from mcp.types import Tool, TextContent


def register_prd_tools(server: Server, get_project_dir: Callable[[], Path]):

    tools = [
        Tool(
            name="prd_create",
            description="Create or update the PRD document for the project.",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "version": {"type": "string", "description": "e.g. 1.0.0"},
                    "overview": {"type": "string"},
                    "goals": {"type": "array", "items": {"type": "string"}},
                    "scope": {"type": "string"},
                },
                "required": ["title", "version", "overview"],
            },
        ),
        Tool(
            name="prd_add_feature",
            description="Add a feature specification to the PRD.",
            inputSchema={
                "type": "object",
                "properties": {
                    "feature_id": {"type": "string", "description": "e.g. FEAT-001"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "acceptance_criteria": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "ac_id": {"type": "string"},
                                "given": {"type": "string"},
                                "when": {"type": "string"},
                                "then": {"type": "string"},
                                "type": {"type": "string", "enum": ["happy_path", "edge_case", "error"]},
                                "priority": {"type": "string", "enum": ["must", "should", "could"]},
                            },
                            "required": ["ac_id", "given", "when", "then"],
                        },
                    },
                    "linked_requirements": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["feature_id", "title", "description", "acceptance_criteria"],
            },
        ),
        Tool(
            name="prd_add_nfr",
            description="Add a non-functional requirement to the PRD with measurable targets.",
            inputSchema={
                "type": "object",
                "properties": {
                    "nfr_id": {"type": "string"},
                    "category": {"type": "string", "enum": ["performance", "security", "scalability", "reliability", "usability", "accessibility"]},
                    "description": {"type": "string"},
                    "target": {"type": "string", "description": "Measurable target, e.g. p95 < 200ms"},
                },
                "required": ["nfr_id", "category", "description", "target"],
            },
        ),
        Tool(
            name="prd_get",
            description="Get the full PRD with all features, NFRs, and metadata.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if not name.startswith("prd_"):
            return []

        project_dir = get_project_dir()
        spec_dir = project_dir / "specification"
        spec_dir.mkdir(parents=True, exist_ok=True)

        if name == "prd_create":
            prd_file = spec_dir / "prd.yaml"
            existing = {}
            if prd_file.exists():
                existing = yaml.safe_load(prd_file.read_text()) or {}
            existing.update({
                "title": arguments["title"],
                "version": arguments["version"],
                "overview": arguments["overview"],
                "goals": arguments.get("goals", existing.get("goals", [])),
                "scope": arguments.get("scope", existing.get("scope", "")),
            })
            existing.setdefault("features", [])
            existing.setdefault("nfrs", [])
            prd_file.write_text(yaml.dump(existing, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "artifact": str(prd_file),
            }))]

        if name == "prd_add_feature":
            prd_file = spec_dir / "prd.yaml"
            prd = yaml.safe_load(prd_file.read_text()) if prd_file.exists() else {"features": [], "nfrs": []}
            features = prd.setdefault("features", [])
            features = [f for f in features if f.get("feature_id") != arguments["feature_id"]]
            features.append(arguments)
            prd["features"] = features
            prd_file.write_text(yaml.dump(prd, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved",
                "feature_id": arguments["feature_id"],
                "ac_count": len(arguments["acceptance_criteria"]),
            }))]

        if name == "prd_add_nfr":
            prd_file = spec_dir / "prd.yaml"
            prd = yaml.safe_load(prd_file.read_text()) if prd_file.exists() else {"features": [], "nfrs": []}
            nfrs = prd.setdefault("nfrs", [])
            nfrs = [n for n in nfrs if n.get("nfr_id") != arguments["nfr_id"]]
            nfrs.append(arguments)
            prd["nfrs"] = nfrs
            prd_file.write_text(yaml.dump(prd, default_flow_style=False))
            return [TextContent(type="text", text=json.dumps({
                "status": "saved", "nfr_id": arguments["nfr_id"],
            }))]

        if name == "prd_get":
            prd_file = spec_dir / "prd.yaml"
            if not prd_file.exists():
                return [TextContent(type="text", text=json.dumps({"error": "No PRD found. Create one first."}))]
            prd = yaml.safe_load(prd_file.read_text())
            return [TextContent(type="text", text=json.dumps(prd, default_flow_style=False))]

        return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]
