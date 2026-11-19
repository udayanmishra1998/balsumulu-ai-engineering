# Skill: Sprint Planning

## Purpose
Create the product roadmap, define phases, prioritize epics, and organize the backlog for execution.

## When to Use
- During Planning phase after PRD is approved
- When re-planning after scope changes
- When starting a new roadmap phase

## Prerequisites
- Approved PRD with all feature specifications
- MVP scope definition
- Success metrics from Discovery

## Skill Steps

### Step 1: Feature-to-Epic Mapping
**Goal:** Group PRD features into epics.

1. List all MVP features from the PRD
2. Group related features into epics:
   - Features that form a complete user capability = one epic
   - Features with tight technical dependencies = consider one epic
   - Features serving different capability areas = separate epics
3. Name each epic: `[AREA] Epic Title`
4. Use `templates/engineering/epic.yaml` for each

**Naming examples:**
- `[Auth] User Registration and Login`
- `[Content] Document Upload and Management`
- `[Dashboard] User Dashboard and Analytics`

### Step 2: Roadmap Construction
**Goal:** Create a phased roadmap.

Using `templates/engineering/roadmap.md`:

**Phase 1 (MVP):**
- All "Must have" features
- Group into epics
- Identify dependencies between epics (what must come first?)
- Define milestones within Phase 1

**Phase 2 (Enhancement):**
- "Should have" features
- Features that enhance Phase 1 capabilities
- Define trigger to start (after launch? after N users?)

**Phase 3+ (Scale):**
- "Could have" features
- Expansion features
- Keep as candidates, not commitments

**Questions for the founder:**
- "Does this phasing align with your go-to-market strategy?"
- "Are there features that must ship together?"
- "Do you have a target launch date or timeline?"
- "Would you rather launch faster with less, or later with more?"

**HITL checkpoint:** Approve the roadmap before proceeding.

### Step 3: Epic Prioritization
**Goal:** Order epics within each phase.

Default framework: **RICE**
- **Reach:** How many users does this affect? (number)
- **Impact:** How much does this impact each user? (3=massive, 2=high, 1=medium, 0.5=low)
- **Confidence:** How sure are we about reach and impact? (100%=high, 80%=medium, 50%=low)
- **Effort:** How many person-months? (estimate)

RICE Score = (Reach × Impact × Confidence) / Effort

Present to founder:
1. Show the RICE scores and resulting priority
2. Explain the rationale for each
3. Ask: "Do you agree with this order? What would you change?"
4. Adjust based on founder input (business reasons may override RICE)
5. Document the final priority and rationale

**Alternative frameworks** (if founder prefers):
- **WSJF** (Weighted Shortest Job First) — value / effort
- **MoSCoW** — simpler, less quantitative
- **Custom** — the founder's own criteria

**HITL checkpoint:** Approve the epic priority order.

### Step 4: Dependency Analysis
**Goal:** Map epic and feature dependencies.

Create a dependency map:
- Which epics must come before others?
- Are there cross-epic dependencies?
- Any external dependencies (APIs, services, data)?
- Flag any critical path items

Visualize:
```
EPIC-001 (Auth) ──→ EPIC-003 (Dashboard)  [must have auth before dashboard]
EPIC-002 (Content) ──→ EPIC-003 (Dashboard)  [dashboard shows content]
EPIC-004 (Notifications) [independent]
```

### Step 5: Sprint/Phase Planning
**Goal:** Organize the first phase for execution.

For Phase 1:
1. Order epics by priority and dependencies
2. Identify what can be built in parallel vs. sequentially
3. Define sprint boundaries (if using sprints) or milestones (if continuous)
4. For each sprint/milestone:
   - Which epics/stories are targeted
   - What's the deliverable at the end
   - What's the demo or validation criteria

**HITL checkpoint:** "Here's the execution plan for Phase 1. Agreed?"

### Step 6: Backlog Organization
**Goal:** Set up the project management tool.

1. Create the project/board in Jira/Linear/Notion
2. Create epics in priority order
3. Hand off to `backlog-grooming` skill for story creation
4. After stories are created, organize the board:
   - Backlog column with priority order
   - Labels and filters set up
   - Dependencies visible

## Templates Used
- `templates/engineering/roadmap.md`
- `templates/engineering/epic.yaml`

## Quality Checklist
- [ ] Roadmap has at least MVP phase fully detailed
- [ ] All MVP features are assigned to epics
- [ ] Epics are prioritized with rationale documented
- [ ] Dependencies are mapped (no circular dependencies)
- [ ] Critical path is identified
- [ ] Founder has approved roadmap and priority order
- [ ] The backlog is organized and ready for story decomposition

## Tips for the AI Editor
- Roadmaps are communication tools — they should tell a story of the product evolution
- Don't over-plan future phases — they'll change based on what you learn from MVP
- Dependencies drive sequencing more than preferences — respect them
- If the founder can't prioritize, help by framing it as trade-offs: "If we do A first, users get X earlier but Y waits"
- Keep Phase 1 focused — the most common mistake is trying to do too much in MVP
- Document WHY each priority decision was made — this context is invaluable later
