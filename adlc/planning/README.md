# ADLC Phase: Planning

## Purpose

Transform the approved PRD into an actionable, prioritized backlog ready for a technical architect and development team. This phase produces the product roadmap, breaks it into epics, decomposes epics into groomed user stories with acceptance criteria, and ensures everything is organized in the project management tool.

## When This Phase Runs

- After Specification phase is complete and PRD is approved
- When re-planning after a significant scope change
- At the start of each new release cycle (for ongoing products)

## Inputs

| Input | Source | Required |
|---|---|---|
| Approved PRD | Specification phase (Confluence/Notion) | Yes |
| Acceptance criteria | Specification phase (within PRD) | Yes |
| MVP scope definition | Requirements phase (Confluence/Notion) | Yes |
| User personas | Requirements phase (Confluence/Notion) | For reference |
| Success metrics | Discovery phase (Confluence/Notion) | For reference |

## Activities

### 1. Product Roadmap Creation
**Agent:** Engineering Planner
**Skill:** sprint-planning

- Analyze the PRD features and their dependencies
- Propose a phased roadmap:
  - **Phase 1 (MVP):** Minimum viable product — the features that must exist for launch
  - **Phase 2:** Features that enhance the MVP based on priority
  - **Phase 3+:** Future features, nice-to-haves, and expansion
- For each phase, define:
  - Features included (with rationale for sequencing)
  - Dependencies between features
  - Estimated relative complexity (not time — that comes from the architect)
  - Key milestones and deliverables
  - Success criteria for the phase

**Questions the agent should ask:**
- Does this phasing make sense for your go-to-market strategy?
- Are there features that must ship together (can't launch one without the other)?
- Do you have a target launch date or timeline constraint?
- Would you rather launch faster with less, or later with more?

### 2. Epic Definition
**Agent:** Engineering Planner
**Skill:** backlog-grooming

- Break each roadmap phase into epics
- An epic is a body of work that delivers a complete capability
- For each epic, define:
  - **Title** — clear, concise name
  - **Description** — what this epic delivers and why
  - **Linked PRD features** — which features this epic implements
  - **Acceptance criteria** — high-level criteria for the epic (pulled from PRD)
  - **Dependencies** — other epics that must complete first
  - **Priority** — within the phase
  - **Labels/Tags** — capability area, persona served

**Naming convention:** `[AREA] Epic Title` (e.g., `[Auth] User Registration and Login`)

### 3. Epic Prioritization
**Agent:** Engineering Planner
**Skill:** backlog-grooming

- Present epics to the founder with recommended priority order
- Prioritization criteria:
  - User value (which personas benefit, how critical the pain point is)
  - Dependencies (what must come first technically)
  - Risk (de-risk the hardest things early)
  - Business value (revenue impact, market timing)
- Use a prioritization framework (RICE, WSJF, or MoSCoW — recommend one and ask founder)
- Document the priority rationale for every epic

**Questions the agent should ask:**
- Do you agree with this priority order? What would you change?
- Are there business reasons to move any epic up or down?
- Is there a feature that would make or break early user feedback?
- Should we de-risk any technically uncertain feature by building it first?

### 4. User Story Decomposition
**Agent:** Engineering Planner
**Skill:** backlog-grooming

Break each epic into user stories. Each story must be:
- **Independent** — can be developed without depending on another story in the same sprint
- **Negotiable** — details can be discussed, it's not a contract
- **Valuable** — delivers something useful to the user or system
- **Estimable** — a developer can roughly estimate the effort
- **Small** — completable within a single sprint
- **Testable** — has clear acceptance criteria

**Story format:**
```
Title: [Concise action-oriented title]

As a [persona],
I want to [action/capability],
So that [benefit/value].

Description:
[Additional context, design notes, constraints]

Acceptance Criteria:
- AC1: Given [context], When [action], Then [result]
- AC2: Given [context], When [action], Then [result]
- AC3: Given [context], When [action], Then [result]

Edge Cases:
- [Edge case 1 and expected behavior]
- [Edge case 2 and expected behavior]

Out of Scope:
- [What this story does NOT include]

Dependencies:
- [Story IDs or epic references]

Labels: [epic, capability-area, persona]
```

### 5. Story Grooming
**Agent:** Engineering Planner
**Skill:** backlog-grooming

For each story, ensure grooming quality:
- Acceptance criteria are specific and testable
- Edge cases are identified
- Dependencies are mapped
- The story is small enough for one sprint
- The story is clear enough for a developer to start without further questions

**Grooming with the founder:**
- Walk through each story in the epic
- Confirm the acceptance criteria match the founder's intent
- Ask about edge cases the founder cares about
- Confirm priority within the epic
- Get approval on the groomed stories

**Questions the agent should ask per story:**
- Does this story capture what you had in mind?
- Are the acceptance criteria right — anything missing?
- What edge case would worry you most?
- Is this the right size, or should we split/combine?

### 6. Backlog Organization
**Agent:** Engineering Planner
**Skill:** sprint-planning

- Create all epics in the project management tool (Jira/Linear/Notion)
- Create all user stories under their respective epics
- Set priorities, labels, and dependencies
- Organize the backlog in priority order
- Create a board view for the first phase/sprint

**Before pushing to the tool:**
- Show the founder the complete backlog structure
- Confirm the data that will be sent (per security policy)
- Get explicit approval to create items in the external tool
- Execute and confirm creation

## Outputs

| Output | Format | Destination | Approval Required |
|---|---|---|---|
| Product roadmap | Document | Confluence/Notion | Yes |
| Epic definitions | Epics | Jira/Linear/Notion | Yes |
| Epic priority order | Backlog order | Jira/Linear/Notion | Yes |
| User stories (groomed) | Stories | Jira/Linear/Notion | Yes |
| Acceptance criteria (per story) | Within stories | Jira/Linear/Notion | Yes |
| Dependency map | Document/Diagram | Confluence/Notion | Reviewed |
| Sprint/phase plan | Board/Plan | Jira/Linear/Notion | Yes |

## Quality Gates

Before exiting Planning, all of the following must be true:

- [ ] Product roadmap is defined with at least MVP phase fully detailed
- [ ] All MVP features are decomposed into epics
- [ ] All epics are decomposed into user stories
- [ ] Every user story follows the INVEST criteria
- [ ] Every user story has at least 3 acceptance criteria
- [ ] Every acceptance criteria is testable (Given/When/Then or equivalent)
- [ ] Dependencies between stories and epics are mapped
- [ ] Priority order is founder-approved
- [ ] All items are created in the project management tool
- [ ] The backlog is ready for a technical architect to review and estimate
- [ ] The founder has approved each milestone (per human-approval-policy)

## Failure Modes

| Failure | Detection | Resolution |
|---|---|---|
| Stories too large | A story spans multiple capability areas | Split into smaller, focused stories |
| Stories too small | Dozens of trivial stories that could be one | Combine related micro-stories |
| Acceptance criteria vague | Criteria can't distinguish pass from fail | Rewrite with specific, measurable conditions |
| Missing dependencies | Story references capability not in the backlog | Add the dependency or note it as an assumption |
| Epic not decomposable | Can't break an epic into independent stories | Revisit the PRD feature — it may need restructuring |
| Prioritization deadlock | Founder can't decide between two options | Present data (user value, risk, dependencies) and recommend |

## Transition to Architecture

Planning is complete when the founder approves the full backlog. The output of this phase is the **complete input for a technical architect**:
- A groomed, prioritized backlog with acceptance criteria
- A product roadmap with phasing
- Full traceability from stories → epics → PRD features → requirements → vision

The handoff must be explicit — the agent confirms all items are in the project management tool, the roadmap is published, and the founder is ready for the technical architecture phase to begin.

## Ongoing Planning

Planning is not a one-time event. As the product evolves:
- New stories may be added (through the requirements → specification → planning pipeline)
- Priorities may shift (always with founder approval)
- Completed stories are closed and velocity is tracked
- The roadmap is updated to reflect progress and changes
- Sprint retrospectives feed back into process improvement
