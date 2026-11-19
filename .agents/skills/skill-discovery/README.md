# Skill: Skill Discovery

## Purpose
Find and evaluate existing open-source skills, MCP servers, tools, and frameworks that can be leveraged by the harness instead of building from scratch.

## When to Use
- When a new capability is needed and before building it custom
- When evaluating if an existing tool covers a use case better
- During periodic harness improvement reviews

## Skill Steps

### Step 1: Define the Need
1. What capability is needed?
2. What inputs does it take?
3. What outputs must it produce?
4. What quality bar must it meet?

### Step 2: Search for Existing Solutions
Search for:
- MCP servers on GitHub: "mcp server [capability]"
- Claude Code skills: existing skill registries
- Open-source tools: "[capability] open source tool"
- NPM/PyPI packages: relevant libraries
- Awesome lists: "awesome [domain]" repositories

Prioritize:
1. Official/well-maintained MCP servers (for integrations)
2. Claude Code / Cursor compatible skills
3. Well-maintained open-source libraries
4. Community tools with active development

### Step 3: Evaluate Candidates
For each candidate, assess:

| Criteria | Weight | Assessment |
|---|---|---|
| Functionality match | High | Does it do what we need? |
| Maintenance status | High | Last commit, open issues, release frequency |
| Community adoption | Medium | Stars, forks, users |
| Documentation quality | Medium | Can we figure out how to use it? |
| Security | High | Any known vulnerabilities? Dependencies? |
| License compatibility | High | MIT/Apache/BSD preferred |
| Integration effort | Medium | How hard to plug in? |

### Step 4: Recommend to Founder
Present findings:
- What we need
- What exists (top 2-3 options)
- Recommendation with rationale
- Build vs. adopt trade-off

**HITL checkpoint:** Founder decides whether to adopt or build.

### Step 5: Register (if adopted)
Add to `skill-registry/catalog.yaml`:
```yaml
- name: "[skill-name]"
  type: external
  source: "[URL]"
  version: "[version]"
  purpose: "[what it does for us]"
  status: active
  evaluated: "[date]"
```

## Tips for the AI Editor
- Always check for existing solutions before building
- Prefer MCP servers for integrations — they're purpose-built for AI editors
- A 70% solution that exists now beats a 100% solution built from scratch
- But don't adopt abandoned or insecure tools — quality matters
