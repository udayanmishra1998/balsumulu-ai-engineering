# Skill: Backlog Grooming

## Purpose
Decompose epics into well-groomed user stories with testable acceptance criteria, following INVEST principles, ready for a technical architect to estimate and implement.

## When to Use
- During Planning phase after roadmap and epics are defined
- When new features are added to the backlog
- When stories need re-grooming after scope changes

## Prerequisites
- Approved PRD with feature specifications and acceptance criteria
- Epics defined and prioritized
- User personas available

## Skill Steps

### Step 1: Epic Decomposition
**Goal:** Break each epic into user stories.

For each epic:

1. Read the epic's linked PRD feature specification
2. Read the feature's acceptance criteria
3. Identify the distinct user actions/capabilities within the feature
4. Each distinct action becomes a candidate story

**Decomposition rules:**
- One story = one user action or system capability
- If you can't describe it in one "As a... I want... So that..." it's too big
- If it doesn't deliver user-visible value on its own, it might be a task (attach to a story)
- Technical setup (DB schema, API scaffolding) is a story if it's needed before other stories

**Use `templates/engineering/user-story.yaml` for each story.**

### Step 2: Story Writing
**Goal:** Write complete stories with narratives and ACs.

For each story:

**Narrative:**
```
As a [persona from the personas list],
I want to [specific action — what the user does],
So that [specific benefit — why it matters to them].
```

Bad: "As a user, I want to use the system, so that it works."
Good: "As a teacher, I want to upload a PDF worksheet, so that my students can access it from their dashboard."

**Description:**
- Context the developer needs
- Design hints (if any)
- Constraints specific to this story
- Keep it concise — the ACs are the contract

**Acceptance Criteria:**
Derive from the PRD feature ACs, broken down to story level:
- At least 1 happy-path AC
- At least 1 edge-case AC  
- At least 1 error-handling AC

Each AC:
```
Given [specific precondition],
When [specific action],
Then [specific, measurable outcome].
```

**Rules for ACs:**
- A developer reading this can write a test for it
- No ambiguous words: "appropriate," "correct," "properly" → replace with specifics
- Include data boundaries: "max 100 characters," "at least 1 item," "within 2 seconds"
- Error ACs specify the error message or behavior

**Edge Cases:**
- What happens at boundaries (empty, max, special characters)?
- What about concurrent access?
- What about slow network?

**Out of Scope:**
- Explicitly state what this story does NOT cover
- Prevents scope creep during implementation

### Step 3: INVEST Validation
**Goal:** Ensure every story meets quality criteria.

Check each story against INVEST:

| Criterion | Question | If No |
|---|---|---|
| **Independent** | Can this be built without another story in the same sprint? | Identify the dependency, consider reordering or merging |
| **Negotiable** | Can implementation details be discussed with the developer? | Loosen the spec — describe what, not how |
| **Valuable** | Does this deliver something the user or system needs? | If not, it might be a sub-task, not a story |
| **Estimable** | Can a developer roughly gauge effort? | Add more context or split into clearer pieces |
| **Small** | Can this be completed in one sprint? | Split along user action boundaries |
| **Testable** | Can you write a test from the ACs? | Rewrite ACs with specific, measurable criteria |

### Step 4: Dependency Mapping
**Goal:** Map relationships between stories.

For each story, identify:
- **Blocks:** This story must be done before story X can start
- **Soft dependency:** Helpful but not strictly required
- **No dependency:** Can be built in any order

Visualize as a simple dependency chain per epic:
```
STORY-001 → STORY-003 → STORY-005
STORY-002 → STORY-003
STORY-004 (independent)
```

Flag circular dependencies — they indicate a decomposition problem.

### Step 5: Grooming with Founder
**Goal:** Validate stories with the founder.

For each epic's stories:
1. Walk through each story narrative
2. Review acceptance criteria together
3. Ask per story:
   - "Does this capture what you had in mind?"
   - "Are the acceptance criteria right — anything missing?"
   - "What edge case would worry you most?"
   - "Is this the right size, or should we split/combine?"
4. Adjust based on feedback
5. Confirm priority within the epic

**HITL checkpoint:** "These stories are groomed and ready. Approved for the backlog?"

### Step 6: Backlog Push
**Goal:** Create all items in the project management tool.

Before pushing (per security policy):
1. Show the founder the complete data payload
2. Name the destination tool and workspace
3. Get explicit permission
4. Create epics first, then stories under them
5. Set priorities, labels, and dependencies
6. Confirm creation with the founder

## Templates Used
- `templates/engineering/epic.yaml`
- `templates/engineering/user-story.yaml`

## Quality Checklist
- [ ] Every story follows the "As a / I want / So that" format
- [ ] Every story has 3+ acceptance criteria (happy, edge, error)
- [ ] All ACs are specific and testable (no vague language)
- [ ] INVEST validated for every story
- [ ] Dependencies are mapped and no circular chains exist
- [ ] Out of scope is defined for each story
- [ ] Stories are small enough for one sprint
- [ ] Founder has reviewed and approved each epic's stories
- [ ] All items created in the project management tool

## Tips for the AI Editor
- Stories should read like user actions, not technical tasks
- If you're writing "implement the backend for..." it's a task, not a story — wrap it in user value
- Acceptance criteria are the most important part — spend time here
- The founder may not care about edge cases — push gently, they matter for quality
- When stories feel too big, split along the user's action sequence
- When stories feel too small, combine if they always ship together
- Keep the "So that" meaningful — it reminds everyone WHY this matters
