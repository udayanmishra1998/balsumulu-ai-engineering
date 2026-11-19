# Workflow: PRD to Architecture

## Overview
Takes the approved PRD and translates it into a product roadmap with epics. This is the bridge between "what to build" (PRD) and "in what order" (backlog).

**Phases covered:** Specification → Planning (first half)
**Agents involved:** PRD Agent (handoff), Engineering Planner
**Entry point:** Approved PRD
**Exit point:** Approved roadmap with prioritized epics

## Flow

```
Approved PRD
     │
     ▼
┌──────────────────┐
│ Feature-to-Epic   │   Group PRD features into epics
│ Mapping           │
│ (Eng. Planner)    │
└────────┬─────────┘
     │
     ▼
┌──────────────────┐
│ Roadmap           │   Phase features across releases
│ Construction      │
│ (Eng. Planner)    │
└────────┬─────────┘
     │
     ▼
╔══════════════════╗
║ FOUNDER APPROVAL ║   Approve roadmap
╚════════╤═════════╝
     │
     ▼
┌──────────────────┐
│ Epic              │   RICE scoring, priority order
│ Prioritization    │
│ (Eng. Planner)    │
└────────┬─────────┘
     │
     ▼
┌──────────────────┐
│ Dependency        │   Map epic dependencies
│ Analysis          │
│ (Eng. Planner)    │
└────────┬─────────┘
     │
     ▼
╔══════════════════╗
║ FOUNDER APPROVAL ║   Approve epic priorities
╚══════════════════╝
```

## State Transitions

```yaml
states:
  - phase: planning
    activities:
      - feature_epic_mapping → roadmap_construction → epic_prioritization → dependency_analysis
    gates:
      - roadmap_approval
      - epic_priority_approval
    gate_artifacts: [roadmap, epics, dependency_map]
```

## Handoff to Architecture-to-Backlog
Once the roadmap and epics are approved, the `architecture-to-backlog` workflow takes over for story decomposition and backlog creation.
