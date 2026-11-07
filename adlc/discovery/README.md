# ADLC Phase: Discovery

## Purpose

Transform a raw idea into a validated, well-understood product concept. This phase ensures the founder has clarity on what they're building, who it's for, why it matters, and whether the market supports it — before any requirements are written.

## When This Phase Runs

- At the very start of a new project (idea → validated concept)
- When pivoting or exploring a new product direction
- When expanding into a new market segment or user base

## Inputs

| Input | Source | Required |
|---|---|---|
| Raw idea or problem statement | Founder (conversation) | Yes |
| Domain context | Founder (conversation) | Yes |
| Existing research (if any) | Founder (documents, links) | No |
| Constraints or preferences | Founder (conversation) | No |

## Activities

### 1. Idea Intake & Clarification
**Agent:** Product Analyst
**Skill:** product-discovery

- Listen to the founder's idea and ask clarifying questions
- Identify what's clear vs. what's ambiguous
- Surface assumptions the founder may be making
- Document the raw idea as stated

**Questions the agent should ask:**
- What problem are you solving?
- Who has this problem? How do you know?
- Why does this problem matter? What happens if it's not solved?
- Have you seen other solutions? What's wrong with them?
- What's your unfair advantage or unique angle?
- What does success look like for this product?
- Are there any hard constraints (timeline, budget, technology, regulation)?

### 2. Market Research
**Agent:** Research Analyst
**Skill:** market-research

- Research the market landscape for the problem domain
- Identify existing solutions, competitors, and alternatives
- Analyze competitor strengths, weaknesses, pricing, and positioning
- Identify market size indicators and growth trends
- Find relevant industry reports, articles, and data
- Surface risks, regulatory considerations, and market barriers

**Output structure:**
- Market overview (size, trends, growth)
- Competitor analysis (matrix with feature comparison)
- Gap analysis (what's missing in current solutions)
- Risk assessment (market risks, regulatory risks)
- Opportunity summary

### 3. Pain Point Validation
**Agent:** Product Analyst
**Skill:** product-discovery

- Map the pain points identified from the founder's input and market research
- Categorize pain points by severity and frequency
- Identify which pain points are underserved by existing solutions
- Prioritize pain points based on impact and feasibility

### 4. Target User Identification
**Agent:** Product Analyst
**Skill:** product-discovery

- Define preliminary user segments
- Identify primary vs. secondary users
- Map user characteristics, behaviors, and needs
- Surface questions about users that need founder input

### 5. Value Proposition Formulation
**Agent:** Product Analyst
**Skill:** product-discovery

- Synthesize research and pain points into a clear value proposition
- Define what makes this product different
- Articulate the core promise to users
- Present to the founder for validation

### 6. Idea Refinement
**Agent:** Product Analyst
**Skill:** product-discovery

- Incorporate all research findings and founder feedback
- Refine the problem statement
- Define the product vision
- Set preliminary success metrics
- Document constraints and assumptions

## Outputs

| Output | Format | Destination | Approval Required |
|---|---|---|---|
| Research findings document | Document | Confluence/Notion | Yes |
| Competitor analysis matrix | Table/Document | Confluence/Notion | Yes |
| Refined problem statement | Document section | Confluence/Notion | Yes |
| Target user segments | Document section | Confluence/Notion | Yes |
| Value proposition | Document section | Confluence/Notion | Yes |
| Product vision statement | Document section | Confluence/Notion | Yes |
| Preliminary success metrics | Document section | Confluence/Notion | Yes |
| Open questions and assumptions | List | Confluence/Notion | Reviewed |

## Quality Gates

Before exiting Discovery, all of the following must be true:

- [ ] The founder can articulate the problem in one sentence
- [ ] Market research is complete with competitor analysis
- [ ] Target users are identified with their key pain points
- [ ] Value proposition is clear and differentiated
- [ ] Product vision is documented and approved
- [ ] Success metrics are defined (even if preliminary)
- [ ] All open questions are either answered or explicitly deferred
- [ ] The founder has approved each milestone (per human-approval-policy)

## Failure Modes

| Failure | Detection | Resolution |
|---|---|---|
| Idea too vague to research | Agent can't formulate search queries | Ask founder for more context, examples, or analogies |
| No clear target user | Research returns broad, unfocused results | Workshop with founder to narrow the audience |
| Market is saturated | Competitor analysis shows many strong players | Surface finding to founder — may need to pivot angle or niche down |
| Founder has conflicting goals | Inputs contradict each other | Surface contradictions explicitly and ask founder to resolve |

## Transition to Requirements

Discovery is complete when the founder approves the product vision and the quality gates above are met. The following artifacts are handed to the Requirements phase:
- Approved product vision
- Target user segments
- Validated pain points
- Value proposition
- Success metrics
- Research findings (for reference)

The handoff must be explicit — the agent summarizes what's being passed and confirms the founder is ready to move on.
