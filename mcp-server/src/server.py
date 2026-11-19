"""
Balsumulu AI Engineering MCP Server

Exposes the ADLC harness pipeline as MCP tools that Claude Code,
Cursor, or any MCP-compatible AI editor can call.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .tools.project_tools import register_project_tools
from .tools.product_tools import register_product_tools
from .tools.requirements_tools import register_requirements_tools
from .tools.prd_tools import register_prd_tools
from .tools.backlog_tools import register_backlog_tools


server = Server("balsumulu-ai-engineering")


def get_project_dir() -> Path:
    """Get the active project directory from environment or default."""
    import os
    project_path = os.environ.get("BALSUMULU_PROJECT_DIR")
    if project_path:
        return Path(project_path)
    return Path.cwd() / "projects" / "default"


# Register all tool groups
register_project_tools(server, get_project_dir)
register_product_tools(server, get_project_dir)
register_requirements_tools(server, get_project_dir)
register_prd_tools(server, get_project_dir)
register_backlog_tools(server, get_project_dir)


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
