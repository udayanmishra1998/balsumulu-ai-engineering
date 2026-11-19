# Workflow: Architecture to Backlog

## Overview
Takes prioritized epics and decomposes them into groomed user stories, then pushes the complete backlog to the project management tool.

**Phases covered:** Planning (second half)
**Agents involved:** Engineering Planner
**Entry point:** Approved roadmap with prioritized epics
**Exit point:** Groomed backlog in Jira/Linear/Notion, ready for a technical architect

## Flow

```
Approved Epics (prioritized)
         │
         ▼
┌──────────────────┐
│ Story             │◄─── Loop: for each epic (in priority order)
│ Decomposition     │
│ (Eng. Planner)    │
│  - User stories   │
│  - ACs per story  │
│  - Edge cases     │
│  - Dependencies   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ INVEST            │   Validate each story meets criteria
│ Validation        │
└────────┬─────────┘
         │
         ▼
╔══════════════════╗
║ FOUNDER REVIEW   ║   Per-epic story review & grooming
║ (per epic)       ║
╚════════╤═════════╝
         │
         ▼
┌──────────────────┐
│ Dependency        │   Map story-level dependencies
│ Mapping           │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Backlog           │   Show payload → get permission → push
│ Push              │
│ (Eng. Planner)    │
└────────┬─────────┘
         │
         ▼
╔══════════════════╗
║ FOUNDER APPROVAL ║ ← Planning Gate (final)
║ Backlog complete ║
╚══════════════════╝
```

## State Transitions

```yaml
states:
  - phase: planning
    activities:
      - story_decomposition → invest_validation → founder_grooming → dependency_mapping → backlog_push
    gate: founder_approval
    gate_artifacts: [groomed_stories, backlog_in_tool]
    sub_gates:
      - per_epic_story_approval
      - backlog_push_permission  # Security policy: show payload before pushing
```

## Backlog Push Protocol

Per the security policy, before pushing to Jira/Linear/Notion:

1. **Show the data:** Present every epic and story that will be created
2. **Name the destination:** "I'll create these in [tool] in workspace [name]"
3. **Get permission:** Wait for explicit "go ahead"
4. **Allow edits:** Founder can modify anything before push
5. **Execute:** Create epics first, then stories under each
6. **Confirm:** Show what was created with links

## Final Output

The completed backlog contains:
- Product roadmap (in Notion/Confluence)
- Epics with priorities and dependencies (in Jira/Linear/Notion)
- Groomed user stories with acceptance criteria (in Jira/Linear/Notion)
- Full traceability: Story → Epic → Feature → Requirement → Pain Point → Persona

**This is the complete handoff to a technical architect.** They can review, estimate, and begin architecture and implementation.

## Completion State

```yaml
harness_state:
  phase: planning
  status: approved
  artifacts:
    roadmap: { location: "notion/confluence", status: approved }
    epics: { location: "jira/linear/notion", count: N, status: approved }
    stories: { location: "jira/linear/notion", count: N, status: groomed }
  traceability: complete
  ready_for: architecture
```
