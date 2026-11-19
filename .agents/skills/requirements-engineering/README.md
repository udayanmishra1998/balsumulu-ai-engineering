# Skill: Requirements Engineering

## Purpose
Transform a validated product concept into structured, prioritized requirements with user personas, journey maps, and MVP scope definition.

## When to Use
- After Discovery phase is approved
- When requirements need to be re-examined after a pivot
- When expanding an existing product's scope

## Prerequisites
- Approved product vision (in Notion/Confluence)
- Target user segments identified
- Validated pain points
- Research findings available

## Skill Steps

### Step 1: Persona Development
**Goal:** Turn user segments into detailed personas.

For each target user segment from Discovery:

1. Ask the founder:
   - "Tell me more about this type of user. Can you describe a real person (anonymized) who fits this?"
   - "What's their typical day like when they encounter this problem?"
   - "What tools are they comfortable with?"

2. Build the persona using `templates/requirements/persona.md`:
   - Fictional name and profile
   - Goals (what they're trying to achieve)
   - Pain points (mapped from Discovery, refined)
   - Current workflow (how they solve it today)
   - Success definition (what would make them love this product)

3. **HITL checkpoint:** Present each persona. "Does this person feel real to you? Is anything off?"

4. Ask: "Which persona is the most important — the one we build for first?"

### Step 2: User Journey Mapping
**Goal:** Map how each primary persona interacts with the product.

For each primary persona, map:
1. **Awareness:** How do they discover the product?
2. **First use:** What's their first experience / onboarding?
3. **Core loop:** What do they do regularly?
4. **Value moment:** When do they first think "this is worth it"?
5. **Expansion:** How does their usage grow over time?

At each stage, note:
- Actions (what they do)
- Thoughts (what they're thinking)
- Emotions (frustrated, curious, satisfied)
- Pain points (where it could go wrong)
- Opportunities (where we can delight them)

**HITL checkpoint:** Walk through the journey with the founder. "Does this match how you see users interacting?"

### Step 3: Feature Extraction
**Goal:** Identify every feature the product needs.

Sources for features:
1. User journeys — what does each step require?
2. Pain points — what feature addresses each?
3. Competitor analysis — what do users expect as table stakes?
4. Founder input — features they already know they want

For each feature:
- One-sentence description
- Which persona(s) it serves
- Which pain point(s) it addresses
- Preliminary priority (must-have / should-have / nice-to-have)

**HITL checkpoint:** "Here's every feature we've identified. What's missing? What shouldn't be here?"

Also ask:
- "Are there features you've seen elsewhere you want to include?"
- "Any features you explicitly do NOT want?"
- "Any compliance or regulatory features needed?"

### Step 4: Requirement Structuring
**Goal:** Organize features into formal requirements.

Using `templates/requirements/requirements-document.md`:

**Functional Requirements:**
- Group by capability area
- Assign unique IDs (REQ-{area}-{number})
- Write clear descriptions
- Link to personas and pain points
- Add preliminary acceptance criteria

**Non-Functional Requirements (walk through each category):**
- **Performance:** "How fast should this be? What's acceptable response time?"
- **Security:** "What data are we handling? Who should access what?"
- **Scalability:** "How many users do you expect in 6 months? A year?"
- **Accessibility:** "Any accessibility requirements? WCAG level?"
- **Data:** "What data do we store? How long? Any regulations?"

**Integration Requirements:**
- "What other systems does this need to connect to?"
- "What data flows between systems?"

**Constraints:**
- Technical, business, regulatory, timeline constraints

### Step 5: Prioritization
**Goal:** MoSCoW prioritize all requirements with the founder.

Present the full list and walk through prioritization:

1. **Must have:** Without this, the product doesn't work. Essential for launch.
2. **Should have:** Important but launch is viable without it. Next after Must.
3. **Could have:** Nice to have. Only if time/resources allow.
4. **Won't have (this time):** Explicitly deferred. Not in this release.

**Key questions:**
- "If you could launch with only 3 features, which would they be?"
- "Which features are table stakes (users expect them)?"
- "Which features are differentiators (users choose you because of them)?"
- "Any time-sensitive features (seasonal, regulatory deadline)?"

**HITL checkpoint:** Confirm every priority. This directly shapes the MVP.

### Step 6: MVP Scope Definition
**Goal:** Draw the line between MVP and later.

1. Present all "Must have" requirements as the MVP candidate
2. Check if the MVP is viable — does it deliver enough value to launch?
3. If too thin, selectively promote "Should have" items
4. If too thick, challenge "Must have" items — "Could we launch without this?"
5. Document the MVP boundary explicitly

**HITL checkpoint:** "This is the MVP scope. Everything in it ships in Phase 1. Everything outside waits. Agreed?"

### Step 7: Validation & Approval
**Goal:** Ensure the requirements document is complete and consistent.

Cross-check:
- Every persona has features that serve them
- Every critical pain point has a requirement addressing it
- Requirements align with the product vision
- Success metrics can be measured with these features
- No orphan requirements (not linked to any feature)
- No conflicting requirements

**Present the full requirements document for final approval.** This is the Requirements gate.

## Templates Used
- `templates/requirements/persona.md`
- `templates/requirements/requirements-document.md`

## Quality Checklist
- [ ] At least one persona per primary user segment
- [ ] Personas feel real (not generic)
- [ ] User journeys cover awareness through expansion
- [ ] All features linked to personas and pain points
- [ ] Every requirement has an ID, description, and priority
- [ ] MoSCoW prioritization complete
- [ ] MVP boundary is explicit
- [ ] NFRs are covered (performance, security, scalability, accessibility)
- [ ] Integration requirements identified
- [ ] No orphan or conflicting requirements
- [ ] Founder approved at every checkpoint

## Tips for the AI Editor
- Personas should feel like real people, not marketing segments
- Push for specificity — "fast" is not a requirement, "< 2 seconds" is
- The founder will resist cutting features — that's normal, guide them gently
- NFRs are often forgotten — explicitly walk through the checklist
- Every "Won't have" should have a reason documented
- If the MVP scope feels too big, it probably is
