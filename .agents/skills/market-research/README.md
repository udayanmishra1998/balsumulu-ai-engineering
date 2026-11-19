# Skill: Market Research

## Purpose
Conduct structured market research, competitive analysis, and industry intelligence using the AI editor's web search capabilities.

## When to Use
- During Discovery phase when research is needed
- When the founder asks about competitors or market landscape
- When validating assumptions about the market

## Prerequisites
- The AI editor must have web search capability (Claude Code, Cursor with web search)
- Research scope defined (from Product Analyst or founder)

## Skill Steps

### Step 1: Define Research Scope
Before searching, clarify:
1. **Problem domain:** What space are we researching?
2. **Known players:** Any competitors the founder already knows?
3. **Key questions:** What specific things do we need to find out?
4. **Boundaries:** Any areas to exclude?

### Step 2: Landscape Scan
**Goal:** Map the competitive landscape.

Search for:
- "[problem domain] software/tools/solutions"
- "[problem domain] competitors comparison"
- "best [category] tools [current year]"
- "[problem domain] market size"
- G2, Capterra, Product Hunt for the category

Identify:
- **Direct competitors:** Same problem, same audience, similar approach
- **Indirect competitors:** Different approach but same outcome
- **Alternatives:** What users do without a dedicated tool (Excel, manual, etc.)

**HITL checkpoint:** Present the landscape to the founder. "Here's what I found. Any of these you already know about? Any I missed?"

### Step 3: Deep Competitor Analysis
For each significant competitor (top 5-8):

**Product Analysis:**
- Core features (from their website, docs, demo videos)
- Unique selling points
- Limitations (from reviews)
- Tech stack (if discoverable)

**Business Analysis:**
- Pricing model and tiers
- Target audience (from their messaging)
- Funding/team size (Crunchbase, LinkedIn)
- Market position (leader, challenger, niche)

**User Sentiment:**
- Search: "[competitor name] reviews"
- Search: "[competitor name] reddit"
- Search: "[competitor name] alternatives"
- Look for: common complaints, praised features, deal-breakers

**Sources to check:**
- Company website and docs
- G2 / Capterra / TrustRadius reviews
- Product Hunt (launch and comments)
- Reddit threads
- App Store / Play Store reviews (if applicable)
- Crunchbase (funding, team)
- Blog posts and case studies

### Step 4: Market Sizing
**Goal:** Estimate market size (be honest about confidence).

Search for:
- "[domain] market size [year]"
- "[domain] market forecast"
- Industry reports (Gartner, Forrester, Statista — summaries often available)

Document:
- TAM (Total Addressable Market)
- SAM (Serviceable Addressable Market)
- Growth rate
- **Source and confidence level for each number**

If hard data isn't available, state that clearly rather than guessing.

### Step 5: Trend & Risk Analysis
**Goal:** Identify tailwinds and headwinds.

Search for:
- "[domain] trends [year]"
- "[domain] regulations"
- "[domain] challenges"
- Technology trends affecting the space

Document:
- Industry trends (tailwinds for the product)
- Regulatory landscape
- Technology shifts
- Market risks (saturation, timing, adoption barriers)

### Step 6: Synthesis
**Goal:** Produce the research findings document.

Using `templates/product/research-findings.md`:
1. Fill in the market overview
2. Complete the competitor matrix
3. Write the gap analysis — where do existing solutions fall short?
4. Document risks with likelihood and impact
5. Write the opportunity summary — why this product, why now

**Present to founder for review and approval.**

## Output Format
Use the `templates/product/research-findings.md` template.

## Quality Checklist
- [ ] At least 3-5 competitors analyzed in depth
- [ ] Competitor matrix is filled with real data (not assumptions)
- [ ] User sentiment includes actual review quotes/themes
- [ ] Market size has sources cited
- [ ] Gap analysis identifies at least 2 underserved needs
- [ ] Risks are honest and actionable
- [ ] Every data point has a source and confidence rating
- [ ] "I don't know" is used where data isn't available (never fabricate)

## Tips for the AI Editor
- **Cite your sources** — always note where data came from
- **State confidence levels** — "High confidence (multiple sources)" vs. "Low confidence (single blog post)"
- **Don't fabricate data** — if you can't find market size, say so
- **Look for negative signals too** — failed startups in the space tell a story
- **Check dates** — a 2020 market report may not reflect the current landscape
- **Be thorough but focused** — research serves Discovery, not an academic paper
