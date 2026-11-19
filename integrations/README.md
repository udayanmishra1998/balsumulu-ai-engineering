# Integrations

This directory holds configuration and adapters for external tool integrations.

## Supported Integrations

| Tool | Purpose | MCP Server |
|------|---------|------------|
| Notion | Documentation, Backlog | Use existing Notion MCP server |
| Confluence | Documentation | Use existing Confluence MCP server |
| Jira | Backlog management | Use existing Jira MCP server |
| Linear | Backlog management | Use existing Linear MCP server |
| GitHub | Code, PRs, Issues | Use existing GitHub MCP server |

## How It Works

The harness does **not** build custom API clients. Instead, it relies on existing open-source MCP servers for each integration. The AI editor connects to those MCP servers alongside the harness MCP server.

## Configuration

Each project specifies its integration preferences in `projects/<name>/project.yaml`:

```yaml
integrations:
  documentation: notion  # or confluence
  backlog: linear        # or jira, notion
  code: github
```

The harness agents and skills reference these preferences when deciding where to push artifacts (PRDs, epics, stories).

## Setup

1. Install the relevant MCP servers for your project's tools
2. Configure API keys in `.env` (see `.env.example`)
3. Add MCP server configs to your AI editor's MCP settings
