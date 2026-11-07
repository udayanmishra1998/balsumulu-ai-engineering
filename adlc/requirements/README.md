# ADLC Phase: Requirements

## Purpose

Transform the validated product concept from Discovery into structured, prioritized requirements. This phase bridges the "what problem are we solving" with "what exactly does the product need to do" — producing a requirements document that fully captures the founder's intent.

## When This Phase Runs

- After Discovery phase is complete and approved
- When a significant pivot requires re-examining requirements
- When expanding an existing product with a new capability area

## Inputs

| Input | Source | Required |
|---|---|---|
| Approved product vision | Discovery phase (Confluence/Notion) | Yes |
| Target user segments | Discovery phase (Confluence/Notion) | Yes |
| Validated pain points | Discovery phase (Confluence/Notion) | Yes |
| Value proposition | Discovery phase (Confluence/Notion) | Yes |
| Success metrics | Discovery phase (Confluence/Notion) | Yes |
| Research findings | Discovery phase (Confluence/Notion) | For reference |

## Activities

### 1. User Persona Development
**Agent:** Requirements Analyst
**Skill:** requirements-engineering

- Expand target user segments from Discovery into detailed personas
- For each persona, define:
  - Name (fictional), role, demographics
  - Goals and motivations
  - Pain points and frustrations
  - Current workflows and tools
  - Technical proficiency
  - What success looks like for them
- Validate personas with the founder — are these the right people?

**Questions the agent should ask:**
- Do these personas match the real users you have in mind?
- Is anyone missing? Any persona that shouldn't be here?
- Which persona is the most important — the one we build for first?
- Can you share any real examples (anonymized) of these users?

### 2. User Journey Mapping
**Agent:** Requirements Analyst
**Skill:** requirements-engineering

- For each primary persona, map their journey:
  - How they discover the product
  - First experience / onboarding
  - Core usage patterns
  - Pain points in the journey
  - Moments of delight / value realization
- Identify touchpoints, emotions, and decision points
- Surface gaps where the product must solve a problem

### 3. Feature Identification
**Agent:** Requirements Analyst
**Skill:** requirements-engineering

- Extract features from user journeys and pain points
- Group features by capability area
- For each feature, define:
  - What it does (one sentence)
  - Which persona(s) it serves
  - Which pain point(s) it addresses
  - Preliminary priority (must-have, should-have, nice-to-have)
- Cross-reference with competitor features from Discovery research

**Questions the agent should ask:**
- Are there features you already know you want that we haven't captured?
- Any features you've seen elsewhere that you want to include or explicitly exclude?
- Are there any regulatory or compliance features needed?
- What's the minimum set of features for the product to be useful?

### 4. Requirement Structuring
**Agent:** Requirements Analyst
**Skill:** requirements-engineering

- Organize features into a structured requirements document:
  - Functional requirements (what the system does)
  - Non-functional requirements (performance, security, scalability, accessibility)
  - Integration requirements (third-party systems, APIs)
  - Data requirements (what data is needed, stored, processed)
  - Constraint requirements (technical, business, regulatory)
- Each requirement gets:
  - Unique ID
  - Description
  - Priority (MoSCoW: Must, Should, Could, Won't)
  - Associated persona(s)
  - Acceptance criteria (high-level)
  - Dependencies

### 5. Prioritization Workshop
**Agent:** Requirements Analyst
**Skill:** requirements-engineering

- Present the full requirements list to the founder
- Walk through prioritization using MoSCoW or a similar framework
- Discuss trade-offs between features
- Identify the MVP boundary — what's in v1 vs. later
- Document the rationale for every priority decision

**Questions the agent should ask:**
- If you could launch with only 3 features, which would they be?
- Which features are table stakes (users expect them) vs. differentiators?
- Are there time-sensitive features (seasonal, regulatory deadline)?
- What's your risk tolerance — lean MVP or more complete first release?

### 6. Requirements Validation
**Agent:** Requirements Analyst
**Skill:** requirements-engineering

- Cross-check requirements against:
  - Product vision — does everything align?
  - User personas — is every persona served?
  - Pain points — is every critical pain point addressed?
  - Success metrics — will these features move the metrics?
  - Competitor analysis — are we differentiated?
- Surface any gaps or contradictions
- Get final founder approval on the requirements document

## Outputs

| Output | Format | Destination | Approval Required |
|---|---|---|---|
| User personas | Document | Confluence/Notion | Yes |
| User journey maps | Document/Diagram | Confluence/Notion | Yes |
| Feature list with priorities | Table/Document | Confluence/Notion | Yes |
| Requirements document | Document | Confluence/Notion | Yes |
| MVP scope definition | Document section | Confluence/Notion | Yes |
| Open questions and deferred items | List | Confluence/Notion | Reviewed |

## Quality Gates

Before exiting Requirements, all of the following must be true:

- [ ] At least one detailed persona exists for each primary user segment
- [ ] User journeys are mapped for primary personas
- [ ] All features are linked to at least one persona and pain point
- [ ] Every requirement has a unique ID, description, and priority
- [ ] MoSCoW prioritization is complete with founder agreement
- [ ] MVP boundary is clearly defined
- [ ] Non-functional requirements are captured (performance, security, etc.)
- [ ] No orphan requirements (requirements not linked to any feature)
- [ ] The founder has approved each milestone (per human-approval-policy)

## Failure Modes

| Failure | Detection | Resolution |
|---|---|---|
| Scope creep during requirements | Feature list grows beyond what's reasonable for v1 | Remind the founder of MVP principles, re-prioritize |
| Conflicting requirements | Two requirements contradict each other | Surface the conflict, ask founder to decide |
| Missing non-functional requirements | Only functional features captured | Explicitly walk through NFR categories with founder |
| Persona doesn't match real users | Founder says "that's not quite right" | Iterate on personas with more founder input |
| Requirements too vague to implement | Description doesn't suggest a clear implementation | Push for specificity — ask "how would a user do this?" |

## Transition to Specification

Requirements is complete when the founder approves the full requirements document and MVP scope. The following artifacts are handed to the Specification phase:
- Approved user personas
- Approved requirements document with priorities
- MVP scope definition
- User journey maps
- All Discovery artifacts (for reference)

The handoff must be explicit — the agent summarizes what's being passed, notes any deferred items, and confirms the founder is ready to move to PRD creation.
