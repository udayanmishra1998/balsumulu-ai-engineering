# AGENTS.md — Agent Governance

## Agent Roster

| Agent | Role | Primary ADLC Phase |
|---|---|---|
| Product Analyst | Product discovery, market analysis | Discovery |
| Research Analyst | Market research, competitive intelligence | Discovery |
| Requirements Analyst | Requirements engineering, stakeholder alignment | Requirements |
| PRD Agent | PRD creation and management | Specification |
| Architect Agent | System, database, and API design | Architecture |
| Engineering Planner | Decomposition, backlog, sprint planning | Planning |
| Developer Agent | Code implementation, refactoring | Implementation |
| Code Review Agent | Code review, quality enforcement | Implementation |
| Test Engineer Agent | Test strategy, test creation, execution | Testing |
| Release Agent | CI/CD, deployment, release management | Release |
| Skill Engineer Agent | Skill discovery, creation, evaluation | Cross-cutting |

## Policies

All agents are governed by the policies in `.agents/policies/`:

- **Global Policy** — Universal rules all agents must follow
- **Human Approval Policy** — What requires human sign-off before proceeding
- **Security Policy** — Security boundaries and constraints
- **Coding Policy** — Code standards and practices
- **Source of Truth Policy** — Canonical sources for each artifact type

## Skill System

Agents use skills from `.agents/skills/` and `skill-registry/`. Skills are composable, testable, and versioned. The Skill Engineer Agent manages the skill lifecycle.
