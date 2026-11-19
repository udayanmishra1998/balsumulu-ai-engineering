"""
Project Management Tools — MCP tools for pipeline state and approvals.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Callable

from mcp.server import Server
from mcp.types import Tool, TextContent

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from orchestration.graphs.adlc_graph import ADLCOrchestrator


def register_project_tools(server: Server, get_project_dir: Callable[[], Path]):

    tools = [
        Tool(
            name="harness_init_project",
            description="Initialize a new project in the harness pipeline.",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_name": {"type": "string", "description": "Project name"},
                    "documentation_tool": {"type": "string", "enum": ["notion", "confluence"]},
                    "backlog_tool": {"type": "string", "enum": ["jira", "linear", "notion"]},
                },
                "required": ["project_name", "documentation_tool", "backlog_tool"],
            },
        ),
        Tool(
            name="harness_get_status",
            description="Get current project status — phase, activity, pending approvals.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="harness_get_next_action",
            description="Get what to do next — which agent, skill, and step.",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="harness_submit_milestone",
            description="Submit a milestone for founder approval.",
            inputSchema={
                "type": "object",
                "properties": {
                    "milestone": {"type": "string"},
                    "description": {"type": "string"},
                },
                "required": ["milestone", "description"],
            },
        ),
        Tool(
            name="harness_founder_approve",
            description="Founder approves a pending milestone.",
            inputSchema={
                "type": "object",
                "properties": {
                    "approval_id": {"type": "string"},
                    "notes": {"type": "string"},
                },
                "required": ["approval_id"],
            },
        ),
        Tool(
            name="harness_founder_reject",
            description="Founder rejects a milestone with feedback.",
            inputSchema={
                "type": "object",
                "properties": {
                    "approval_id": {"type": "string"},
                    "reason": {"type": "string"},
                },
                "required": ["approval_id", "reason"],
            },
        ),
        Tool(
            name="harness_advance_phase",
            description="Advance to the next ADLC phase.",
            inputSchema={
                "type": "object",
                "properties": {
                    "target_phase": {"type": "string"},
                },
                "required": ["target_phase"],
            },
        ),
        Tool(
            name="harness_check_quality_gate",
            description="Check quality gate criteria for a phase.",
            inputSchema={
                "type": "object",
                "properties": {"phase": {"type": "string"}},
                "required": ["phase"],
            },
        ),
    ]

    original_list = server.list_tools()
    @server.list_tools()
    async def list_tools():
        existing = await original_list() if original_list else []
        return existing + tools

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        if not name.startswith("harness_"):
            return []

        project_dir = get_project_dir()
        orchestrator = ADLCOrchestrator(project_dir)

        handlers = {
            "harness_init_project": lambda: orchestrator.initialize_project(
                arguments["project_name"],
                {"documentation_tool": arguments["documentation_tool"], "backlog_tool": arguments["backlog_tool"]},
            ),
            "harness_get_status": orchestrator.get_status,
            "harness_get_next_action": orchestrator.get_next_action,
            "harness_submit_milestone": lambda: orchestrator.submit_milestone(
                arguments["milestone"], arguments["description"],
            ),
            "harness_founder_approve": lambda: orchestrator.founder_approve(
                arguments["approval_id"], arguments.get("notes", ""),
            ),
            "harness_founder_reject": lambda: orchestrator.founder_reject(
                arguments["approval_id"], arguments.get("reason", ""),
            ),
            "harness_advance_phase": lambda: orchestrator.advance_to_phase(arguments["target_phase"]),
            "harness_check_quality_gate": lambda: orchestrator.check_quality_gate(arguments["phase"]),
        }

        handler = handlers.get(name)
        if handler:
            result = handler()
        else:
            result = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(result, indent=2))]
