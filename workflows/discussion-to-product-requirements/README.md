# Workflow: Discussion to Product Requirements

## Overview
Takes a founder's raw idea through Discovery to produce validated product requirements.

**Phases covered:** Discovery → Requirements
**Agents involved:** Product Analyst, Research Analyst, Requirements Analyst
**Entry point:** Founder shares an idea
**Exit point:** Approved requirements document with MVP scope

## Flow

```
┌─────────────────────────────────────────────────────────┐
│ DISCOVERY PHASE                                         │
│                                                         │
│  ┌──────────────┐    ┌──────────────────┐              │
│  │ Idea Intake   │───→│ Research Handoff  │              │
│  │ (Product      │    │ (Product Analyst) │              │
│  │  Analyst)     │    └────────┬─────────┘              │
│  └──────────────┘             │                         │
│                               ▼                         │
│                    ┌──────────────────┐                  │
│                    │ Market Research   │                  │
│                    │ (Research Analyst)│                  │
│                    └────────┬─────────┘                  │
│                             │                           │
│       ┌─────────────────────┤                           │
│       ▼                     ▼                           │
│  ┌──────────┐    ┌──────────────────┐                   │
│  │ Pain Point│    │ Target User      │                   │
│  │ Mapping   │    │ Identification   │                   │
│  └────┬──────┘    └────────┬─────────┘                  │
│       │                    │                            │
│       └────────┬───────────┘                            │
│                ▼                                        │
│       ┌──────────────────┐                              │
│       │ Value Proposition │                              │
│       │ & Vision          │                              │
│       └────────┬─────────┘                              │
│                │                                        │
│                ▼                                        │
│       ╔══════════════════╗                              │
│       ║ FOUNDER APPROVAL ║ ← Discovery Gate             │
│       ╚════════╤═════════╝                              │
│                │                                        │
└────────────────┼────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ REQUIREMENTS PHASE                                      │
│                                                         │
│  ┌──────────────────┐                                   │
│  │ Persona           │                                   │
│  │ Development       │                                   │
│  │ (Req. Analyst)    │                                   │
│  └────────┬─────────┘                                   │
│           ▼                                             │
│  ┌──────────────────┐                                   │
│  │ User Journey      │                                   │
│  │ Mapping           │                                   │
│  └────────┬─────────┘                                   │
│           ▼                                             │
│  ┌──────────────────┐                                   │
│  │ Feature           │                                   │
│  │ Extraction        │                                   │
│  └────────┬─────────┘                                   │
│           ▼                                             │
│  ┌──────────────────┐                                   │
│  │ Requirement       │                                   │
│  │ Structuring       │                                   │
│  └────────┬─────────┘                                   │
│           ▼                                             │
│  ┌──────────────────┐                                   │
│  │ Prioritization    │                                   │
│  │ (MoSCoW)          │                                   │
│  └────────┬─────────┘                                   │
│           ▼                                             │
│  ┌──────────────────┐                                   │
│  │ MVP Scope         │                                   │
│  │ Definition        │                                   │
│  └────────┬─────────┘                                   │
│           ▼                                             │
│  ╔══════════════════╗                                   │
│  ║ FOUNDER APPROVAL ║ ← Requirements Gate               │
│  ╚══════════════════╝                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Step-by-Step Execution

### Step 1: Idea Intake
- **Agent:** Product Analyst
- **Skill:** product-discovery (Step 1)
- **State update:** `phase: discovery, activity: idea_intake, status: in_progress`
- **HITL:** Founder confirms understanding
- **Output:** Raw idea documented in `projects/<name>/context/idea-intake.yaml`

### Step 2: Market Research
- **Agent:** Research Analyst
- **Skill:** market-research
- **State update:** `activity: market_research, status: in_progress`
- **HITL:** Founder reviews landscape scan, then full research
- **Output:** Research findings → Notion/Confluence (via MCP)

### Step 3: Pain Points & Users
- **Agent:** Product Analyst
- **Skill:** product-discovery (Steps 3-4)
- **State update:** `activity: pain_point_analysis, status: in_progress`
- **HITL:** Founder validates pain points and user segments
- **Output:** Pain point map, target users → Notion/Confluence

### Step 4: Value Proposition & Vision
- **Agent:** Product Analyst
- **Skill:** product-discovery (Steps 5-6)
- **State update:** `activity: vision_formulation, status: in_progress`
- **HITL:** Founder approves vision — **DISCOVERY GATE**
- **Output:** Product vision document → Notion/Confluence
- **State update:** `phase: discovery, status: approved`

### Step 5: Persona Development
- **Agent:** Requirements Analyst
- **Skill:** requirements-engineering (Step 1)
- **State update:** `phase: requirements, activity: persona_development, status: in_progress`
- **HITL:** Founder validates personas
- **Output:** Personas → Notion/Confluence

### Step 6: Journey Mapping & Feature Extraction
- **Agent:** Requirements Analyst
- **Skill:** requirements-engineering (Steps 2-3)
- **State update:** `activity: feature_extraction, status: in_progress`
- **HITL:** Founder reviews journeys and feature list
- **Output:** Journey maps, feature list → Notion/Confluence

### Step 7: Requirement Structuring & Prioritization
- **Agent:** Requirements Analyst
- **Skill:** requirements-engineering (Steps 4-5)
- **State update:** `activity: prioritization, status: in_progress`
- **HITL:** Founder approves MoSCoW priorities
- **Output:** Structured requirements document → Notion/Confluence

### Step 8: MVP Scope & Approval
- **Agent:** Requirements Analyst
- **Skill:** requirements-engineering (Steps 6-7)
- **State update:** `activity: mvp_scope, status: in_progress`
- **HITL:** Founder approves MVP scope — **REQUIREMENTS GATE**
- **Output:** Requirements doc with MVP scope → Notion/Confluence
- **State update:** `phase: requirements, status: approved`

## State Transitions

```yaml
states:
  - phase: discovery
    activities:
      - idea_intake → market_research → pain_point_analysis → vision_formulation
    gate: founder_approval
    gate_artifacts: [product_vision, research_findings, pain_points, target_users]

  - phase: requirements
    activities:
      - persona_development → journey_mapping → feature_extraction → requirement_structuring → prioritization → mvp_scope
    gate: founder_approval
    gate_artifacts: [personas, requirements_document, mvp_scope]
```

## Error Recovery

| Error | Recovery |
|---|---|
| Founder rejects research | Research Analyst re-scopes and re-runs |
| Founder rejects vision | Product Analyst revises based on feedback |
| Founder rejects personas | Requirements Analyst iterates with more founder input |
| Founder rejects MVP scope | Re-prioritize with founder |
| Integration down (Notion/Confluence) | Save locally in `projects/`, push when available |
