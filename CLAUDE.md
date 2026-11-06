# CLAUDE.md — Instructions for Claude Code

## Project Overview

This is the Balsumulu AI Engineering harness — a framework for AI agents to build real software projects through a structured ADLC (Agent Development Life Cycle).

## Key Conventions

- All agent definitions live in `.agents/agents/`
- All skills live in `.agents/skills/<skill-name>/`
- All policies live in `.agents/policies/`
- Each project gets its own directory under `projects/<project-name>/`
- Workflows connect ADLC phases and live in `workflows/`
- MCP server code is in `mcp-server/src/`

## When Working on This Repo

- Follow the policies in `.agents/policies/` when they exist
- Keep agent definitions declarative (markdown with YAML frontmatter)
- Skills should be self-contained with their own README
- Workflows define inputs, outputs, and the agent/skill chain
- Always update `skill-registry/catalog.yaml` when adding or removing skills
- Write tests for MCP tools and workflows

## Python

- Use Python 3.11+
- Follow PEP 8
- Type hints required for all public functions
