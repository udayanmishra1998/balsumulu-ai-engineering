# ADLC Phase: Specification

## Purpose

Transform approved requirements into a comprehensive Product Requirements Document (PRD) that serves as the single source of truth for what the product does, how it behaves, and what "done" looks like. The PRD is a living document that evolves as the product matures.

## When This Phase Runs

- After Requirements phase is complete and approved
- When requirements change significantly enough to warrant PRD updates
- When adding a new major feature area to an existing product

## Inputs

| Input | Source | Required |
|---|---|---|
| Approved user personas | Requirements phase (Confluence/Notion) | Yes |
| Approved requirements document | Requirements phase (Confluence/Notion) | Yes |
| MVP scope definition | Requirements phase (Confluence/Notion) | Yes |
| User journey maps | Requirements phase (Confluence/Notion) | Yes |
| Product vision | Discovery phase (Confluence/Notion) | For reference |
| Research findings | Discovery phase (Confluence/Notion) | For reference |

## Activities

### 1. PRD Structure Setup
**Agent:** PRD Agent
**Skill:** prd-management

- Create the PRD document in the project's Confluence or Notion workspace
- Set up the standard PRD structure (see PRD Template below)
- Link back to the requirements document and discovery artifacts
- Establish version history tracking

### 2. Feature Specification
**Agent:** PRD Agent
**Skill:** prd-management

For each feature in the MVP scope, write a detailed specification:

- **Feature name and ID** — linked to the requirement ID
- **Problem statement** — what user problem this solves
- **User stories** — high-level stories (detailed stories come in Planning)
- **Functional description** — what the feature does, step by step
- **User interaction flow** — how the user interacts with it
- **Edge cases** — what happens in unusual scenarios
- **Error handling** — what happens when things go wrong
- **Dependencies** — other features or systems this depends on
- **Out of scope** — what this feature explicitly does NOT do

**Questions the agent should ask per feature:**
- Walk me through how you imagine a user using this feature
- What should happen if [edge case]?
- Is there a specific behavior you've seen elsewhere that you want to replicate?
- What's the simplest version of this feature that still delivers value?

### 3. Acceptance Criteria Definition
**Agent:** PRD Agent
**Skill:** prd-management

For each feature, define testable acceptance criteria:
- Written in Given/When/Then format where applicable
- Cover the happy path, edge cases, and error scenarios
- Must be specific enough that a developer or test engineer knows exactly what to verify
- Must be agreed upon with the founder

**Structure per criterion:**
```
AC-{feature-id}-{number}:
  Given: [precondition]
  When: [action]
  Then: [expected result]
  Priority: [must-pass / should-pass]
```

**Questions the agent should ask:**
- For this feature, what would make you say "yes, that works correctly"?
- What's the most important thing to get right?
- Are there any edge cases that worry you?
- What would be a deal-breaker if it didn't work?

### 4. Non-Functional Specification
**Agent:** PRD Agent
**Skill:** prd-management

Specify non-functional requirements in measurable terms:
- **Performance** — response times, throughput, concurrent users
- **Security** — authentication, authorization, data protection
- **Scalability** — expected growth, scaling triggers
- **Availability** — uptime targets, disaster recovery
- **Accessibility** — WCAG level, screen reader support
- **Internationalization** — language support, locale handling
- **Data retention** — how long data is kept, deletion policies

### 5. Integration Specification
**Agent:** PRD Agent
**Skill:** prd-management

For each external integration:
- What system is being integrated
- What data flows between systems
- Direction of data flow (one-way, two-way)
- Authentication method
- Error handling and fallback behavior
- Rate limits and constraints

### 6. PRD Review and Refinement
**Agent:** PRD Agent
**Skill:** prd-management

- Present the complete PRD to the founder section by section
- Walk through each feature specification
- Review all acceptance criteria
- Identify and resolve any gaps or ambiguities
- Incorporate founder feedback
- Get final approval on the complete PRD

## PRD Template Structure

```
1. Overview
   1.1 Product Vision (from Discovery)
   1.2 Problem Statement
   1.3 Target Users (from Requirements)
   1.4 Success Metrics
   1.5 Scope (MVP boundary)

2. User Personas (linked from Requirements)

3. Feature Specifications
   3.1 Feature: [Name]
       - Problem it solves
       - User stories
       - Functional description
       - User interaction flow
       - Edge cases
       - Error handling
       - Acceptance criteria
       - Dependencies
       - Out of scope
   3.2 Feature: [Name]
       ...

4. Non-Functional Requirements
   4.1 Performance
   4.2 Security
   4.3 Scalability
   4.4 Availability
   4.5 Accessibility
   4.6 Data Requirements

5. Integration Requirements
   5.1 [System Name]
       ...

6. Constraints and Assumptions

7. Open Questions and Deferred Items

8. Appendix
   - Glossary
   - References to Discovery and Requirements documents
   - Version history
```

## Outputs

| Output | Format | Destination | Approval Required |
|---|---|---|---|
| PRD (first draft) | Document | Confluence/Notion | Yes |
| PRD (final, approved) | Document | Confluence/Notion | Yes |
| Acceptance criteria (all features) | Within PRD | Confluence/Notion | Yes |
| Integration specifications | Within PRD or linked | Confluence/Notion | Yes |

## Quality Gates

Before exiting Specification, all of the following must be true:

- [ ] Every MVP feature has a complete specification
- [ ] Every feature has at least 3 acceptance criteria (happy path, edge case, error)
- [ ] All acceptance criteria are testable — a developer can verify pass/fail
- [ ] Non-functional requirements are specified with measurable targets
- [ ] Integration requirements are fully defined
- [ ] No TBD or placeholder sections remain in the PRD
- [ ] The PRD is consistent with the approved requirements document
- [ ] The founder has reviewed and approved the final PRD
- [ ] The PRD is published in Confluence/Notion as the living document

## Failure Modes

| Failure | Detection | Resolution |
|---|---|---|
| Feature spec too vague | Can't derive clear acceptance criteria from it | Ask founder to walk through the feature step by step |
| Acceptance criteria not testable | Criteria use subjective language ("should be fast") | Rewrite with measurable targets ("page loads in < 2s") |
| PRD inconsistent with requirements | Feature in PRD not in requirements (or vice versa) | Reconcile — either update requirements or adjust PRD |
| Scope creep in specification | PRD includes features not in MVP scope | Flag to founder, re-confirm MVP boundary |
| Integration not feasible | API doesn't support required functionality | Research alternatives, present options to founder |

## Transition to Planning

Specification is complete when the founder approves the final PRD. The following artifacts are handed to the Planning phase:
- Approved PRD with all feature specifications
- Acceptance criteria for all features
- Integration specifications
- All upstream artifacts (for reference)

The handoff must be explicit — the agent confirms the PRD is published, all acceptance criteria are approved, and the founder is ready to move to roadmap and backlog creation.

## Living Document

The PRD is a **living document**. After initial approval:
- Changes go through a change request process (propose → review → approve → update)
- Every change is versioned with rationale
- Downstream artifacts (stories, tests) must be updated to match PRD changes
- The founder approves all material changes to the PRD
