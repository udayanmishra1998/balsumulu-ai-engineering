# Skill: PRD Management

## Purpose
Create, maintain, and version a comprehensive Product Requirements Document that serves as the single source of truth for what the product does.

## When to Use
- After Requirements phase is approved
- When updating the PRD with changes
- When reviewing PRD for consistency

## Prerequisites
- Approved requirements document (in Notion/Confluence)
- Approved user personas
- MVP scope definition

## Skill Steps

### Step 1: PRD Setup
**Goal:** Create the PRD document structure in the project's documentation tool.

1. Use `templates/product/prd.md` as the base
2. Create the document in Notion/Confluence (via MCP integration)
3. Fill in Section 1 (Overview) from approved Discovery and Requirements artifacts:
   - Link to product vision
   - Copy problem statement
   - Link to personas
   - Copy success metrics
   - Define scope (from MVP definition)
4. Set up version tracking

### Step 2: Feature Specification (per feature)
**Goal:** Write detailed specs for each MVP feature.

For each feature in the MVP scope, work through:

**2a. Problem Statement**
- What specific user problem does this feature solve?
- Pull from requirements — refine if needed

**2b. User Interaction Flow**
Walk through with the founder:
- "When a user wants to [do this thing], what's the first thing they see?"
- "Then what happens?"
- "What if they make a mistake here?"
- "What does success look like?"

Document as a step-by-step flow with decision points.

**2c. Edge Cases**
Proactively identify:
- What if the input is empty?
- What if there's a lot of data?
- What if two users do this simultaneously?
- What if the network drops?
- What if the user is on mobile vs. desktop?

Ask the founder: "Any edge cases that worry you for this feature?"

**2d. Error Handling**
For each error condition:
- What the user sees (message, behavior)
- What the system does (log, retry, fallback)
- How to recover

**2e. Acceptance Criteria**
Write at least 3 ACs per feature using Given/When/Then:
- 1+ happy path (the normal use case)
- 1+ edge case (unusual but valid)
- 1+ error scenario (something goes wrong)

Rules:
- Specific and measurable — no "should work correctly"
- Independent — each AC can be tested alone
- Complete — a developer knows exactly what to build and verify

**HITL checkpoint per feature:** Present the full spec. "Does this capture what you had in mind? Are the acceptance criteria right?"

### Step 3: Non-Functional Specification
**Goal:** Define measurable NFR targets.

For each NFR category, ask the founder for context and recommend targets:

**Performance:**
- "How many users do you expect at launch? In 6 months?"
- Recommend: page load < 2s, API response < 500ms p95

**Security:**
- "What authentication method? Social login? Email/password?"
- "Who can see what data? Any role-based access needed?"
- Recommend based on data sensitivity

**Scalability:**
- "What's your growth expectation?"
- Recommend based on expected trajectory

**Accessibility:**
- Recommend WCAG AA as default
- Ask if there are specific accessibility needs

**Data:**
- "What data do you collect? Any PII?"
- "Any data retention requirements? GDPR?"

**HITL checkpoint:** "Here are the NFR targets. These affect architecture decisions. Agreed?"

### Step 4: Integration Specification
**Goal:** Detail every external system integration.

For each integration:
- Purpose (why we integrate)
- Data flow (what data, which direction)
- Authentication (how we connect)
- Error handling (what if the integration is down)
- Rate limits (and how we handle them)

**HITL checkpoint:** "These are the integrations we need. Any missing?"

### Step 5: Review & Refinement
**Goal:** End-to-end PRD review.

1. Present the complete PRD to the founder
2. Walk through section by section
3. Check for:
   - Consistency (no contradictions between features)
   - Completeness (no TBD sections)
   - Traceability (every feature links to requirements)
   - Testability (every AC is verifiable)
4. Incorporate feedback
5. Get final approval

**HITL checkpoint:** "The PRD is complete. Ready to approve and move to Planning?"

### Step 6: Change Management (ongoing)
After approval, changes follow this process:
1. Identify the change and its trigger
2. Assess impact (what other features/stories are affected?)
3. Present change request to founder with impact analysis
4. If approved: update PRD, bump version, flag downstream artifacts
5. If rejected: document the decision and rationale

## Templates Used
- `templates/product/prd.md`

## Quality Checklist
- [ ] Every MVP feature has a complete specification
- [ ] Every feature has 3+ acceptance criteria (happy, edge, error)
- [ ] All ACs use Given/When/Then (or equivalent testable format)
- [ ] No subjective language in ACs
- [ ] NFRs have measurable targets
- [ ] Integration specs are complete
- [ ] No TBD or placeholder sections
- [ ] Consistent with approved requirements
- [ ] Version history is maintained
- [ ] Founder has approved the final version

## Tips for the AI Editor
- Write specs as if the developer has never talked to the founder — the PRD should be self-sufficient
- When the founder says "it should just work," push for specifics
- Edge cases are where products break — spend time here
- Acceptance criteria are the contract between product and engineering — make them precise
- If a feature is too complex to specify, it may need to be split
- Keep a running list of open questions — resolve them before approval
