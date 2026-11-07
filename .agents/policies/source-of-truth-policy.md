# Source of Truth Policy

This policy defines where the canonical version of each artifact type lives. When there is a conflict between sources, the source of truth wins.

## Core Principle

Every artifact has **one canonical location**. Agents must read from and write to that location. Copies, summaries, or references in other locations are secondary and must never be treated as authoritative.

## Artifact Sources of Truth

### Product & Requirements Artifacts

| Artifact | Source of Truth | Notes |
|---|---|---|
| Product vision | Confluence or Notion | Founder chooses per project |
| Market research | Confluence or Notion | Research findings and analysis |
| User personas | Confluence or Notion | Persona definitions and details |
| Requirements document | Confluence or Notion | Full requirements with priorities |
| PRD | Confluence or Notion | The living product requirements document |
| Acceptance criteria | Confluence or Notion | Part of the PRD or linked from stories |
| Product roadmap | Confluence or Notion | Phased roadmap with milestones |
| Product decisions | Confluence or Notion | Decision log with rationale |

### Backlog & Project Management Artifacts

| Artifact | Source of Truth | Notes |
|---|---|---|
| Epics | Jira, Linear, or Notion | Founder chooses per project |
| User stories | Jira, Linear, or Notion | Groomed stories with acceptance criteria |
| Sprint/phase plans | Jira, Linear, or Notion | What's in each sprint/phase |
| Bug reports | Jira, Linear, or Notion | Tracked in the same tool as stories |
| Task tracking | Jira, Linear, or Notion | Day-to-day work items |

### Technical Artifacts

| Artifact | Source of Truth | Notes |
|---|---|---|
| Source code | Git (project repository) | Always the code in the repository |
| Architecture decisions (ADRs) | Git (project repository) | Committed alongside code |
| Database schemas | Git (project repository) | Migration files in the repo |
| API specifications | Git (project repository) | OpenAPI/Swagger specs in the repo |
| CI/CD configuration | Git (project repository) | Pipeline definitions in the repo |
| Infrastructure config | Git (project repository) | IaC files in the repo |

### Harness Artifacts

| Artifact | Source of Truth | Notes |
|---|---|---|
| Agent definitions | Git (this repository) | `.agents/agents/` |
| Policies | Git (this repository) | `.agents/policies/` |
| Skills | Git (this repository) | `.agents/skills/` |
| Workflows | Git (this repository) | `workflows/` |
| Templates | Git (this repository) | `templates/` |
| Skill registry | Git (this repository) | `skill-registry/` |

## The Role of `projects/` Directory

The `projects/<project-name>/` directory in this repository is **not the source of truth** for any artifact. It serves as:
- **Local context** — project configuration, pointers to external sources, and metadata that helps agents understand the project
- **Working space** — draft content being formulated before it's pushed to Confluence/Notion/Jira/Linear
- **Cross-reference** — links and references to where the real artifacts live

Think of `projects/` as the agent's notebook, not the published document.

## Project Configuration

Each project must define its tool choices in `projects/<project-name>/project.yaml`:

```yaml
project:
  name: "<project-name>"
  documentation:
    tool: "confluence"  # or "notion"
    workspace: "<workspace-id-or-url>"
  backlog:
    tool: "jira"  # or "linear" or "notion"
    project: "<project-key-or-id>"
  repository:
    url: "<git-repo-url>"
    branch_strategy: "gitflow"  # or "trunk-based"
```

## Conflict Resolution

When data conflicts between sources:
1. The source of truth (as defined above) wins
2. The secondary source must be updated to match
3. The conflict and resolution must be logged and reported to the founder
4. If the source of truth itself has conflicting versions (e.g., concurrent edits in Notion), escalate to the founder immediately

## Synchronization

- Agents must **always read from the source of truth** before starting work that depends on an artifact
- After creating or updating an artifact in the source of truth, update any references in `projects/` to stay current
- Stale references must be flagged, not silently used
