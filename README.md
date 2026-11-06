# Balsumulu AI Engineering

An open-source harness pipeline for AI agents to build, manage, and ship real software projects through a structured **Agent Development Life Cycle (ADLC)**.

## Vision

Software engineering is evolving from human-only workflows to human-AI collaborative systems. This framework provides the structure, policies, skills, and orchestration needed for AI agents to participate as first-class contributors across the entire software development lifecycle — from product discovery to production operations.

## What This Is

- **A harness pipeline** — not a single tool, but a structured framework that coordinates AI agents across SDLC phases
- **Agent-native** — built around agent policies, skills, and workflows rather than retrofitting AI onto existing tools
- **Project-aware** — each real project gets its own context, objectives, and decision history within the shared harness
- **Incrementally adoptable** — start with one skill or workflow, expand as needed
- **Open source** — designed to be generic, extensible, and community-driven

## Structure

```
.agents/          — Agent definitions, skills, and governance policies
projects/         — Real project contexts (objectives, PRDs, architecture, backlog)
adlc/             — Agent Development Life Cycle phase definitions
workflows/        — End-to-end workflow pipelines connecting ADLC phases
skill-registry/   — Catalog and management of agent skills
mcp-server/       — MCP server exposing tools for Claude Code / MCP clients
platform/         — Core platform services (API, workflow engine, approvals, audit)
orchestration/    — Agent orchestration graphs, state, and routing
integrations/     — Connectors to GitHub, Notion, Linear, Codex, Claude Code
database/         — Schemas, migrations, and seed data
templates/        — Reusable templates for artifacts across phases
evaluations/      — Quality evaluation frameworks per phase
observability/    — Logging, tracing, metrics, and audit
tests/            — Unit, integration, workflow, and regression tests
scripts/          — Utility scripts
docs/             — Documentation
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/udayanmishra1998/balsumulu-ai-engineering.git
cd balsumulu-ai-engineering

# Copy environment config
cp .env.example .env

# Install dependencies
pip install -e .
```

## Agent Development Life Cycle (ADLC)

The ADLC defines how AI agents move a project from idea to production:

1. **Discovery** — Product discovery, market research, competitive analysis
2. **Requirements** — Requirements engineering, stakeholder alignment
3. **Specification** — PRD creation, acceptance criteria, constraints
4. **Architecture** — System design, database design, API design
5. **Planning** — Engineering decomposition, backlog grooming, sprint planning
6. **Implementation** — Code generation, code review, refactoring
7. **Testing** — Unit, integration, E2E, security, and performance testing
8. **Release** — CI/CD, deployment, release management
9. **Operations** — Observability, feedback loops, continuous improvement

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.
