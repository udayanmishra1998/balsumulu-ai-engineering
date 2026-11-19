# Workflow: Requirements to PRD

## Overview
Takes approved requirements and produces a comprehensive, approved PRD with feature specifications and testable acceptance criteria.

**Phases covered:** Requirements → Specification
**Agents involved:** Requirements Analyst (handoff), PRD Agent
**Entry point:** Approved requirements document with MVP scope
**Exit point:** Approved PRD published in Notion/Confluence

## Flow

```
Approved Requirements + MVP Scope
              │
              ▼
     ┌──────────────────┐
     │ PRD Setup         │   Create document structure
     │ (PRD Agent)       │   in Notion/Confluence
     └────────┬─────────┘
              │
              ▼
     ┌──────────────────┐
     │ Feature Spec      │◄─── Loop: for each MVP feature
     │ (PRD Agent)       │
     │  - Problem        │
     │  - Interaction    │
     │  - Edge cases     │
     │  - Error handling │
     │  - ACs            │
     └────────┬─────────┘
              │
              ▼
     ╔══════════════════╗
     ║ FOUNDER REVIEW   ║   Per-feature approval
     ║ (per feature)    ║
     ╚════════╤═════════╝
              │
              ▼
     ┌──────────────────┐
     │ NFR Specification │   Performance, security,
     │ (PRD Agent)       │   scalability, accessibility
     └────────┬─────────┘
              │
              ▼
     ┌──────────────────┐
     │ Integration Spec  │   External system details
     │ (PRD Agent)       │
     └────────┬─────────┘
              │
              ▼
     ┌──────────────────┐
     │ Full PRD Review   │   End-to-end consistency check
     │ (PRD Agent)       │
     └────────┬─────────┘
              │
              ▼
     ╔══════════════════╗
     ║ FOUNDER APPROVAL ║ ← Specification Gate
     ╚══════════════════╝
```

## State Transitions

```yaml
states:
  - phase: specification
    activities:
      - prd_setup → feature_specification → nfr_specification → integration_specification → prd_review
    gate: founder_approval
    gate_artifacts: [prd_document]
    sub_gates:
      - per_feature_approval  # Each feature spec reviewed individually
      - nfr_approval
```

## Key Rules

1. **Feature specs are presented one at a time** — don't dump the entire PRD on the founder at once
2. **Acceptance criteria are non-negotiable** — every feature must have them
3. **The PRD must be self-sufficient** — a developer should be able to build from it without asking the founder
4. **Traceability is maintained** — every feature links back to requirements

## Error Recovery

| Error | Recovery |
|---|---|
| Feature spec rejected | Revise with founder feedback, re-present |
| Acceptance criteria too vague | Rewrite with specific measurements |
| NFR targets disputed | Research industry benchmarks, present options |
| PRD inconsistent with requirements | Reconcile — update PRD or flag requirement change |
