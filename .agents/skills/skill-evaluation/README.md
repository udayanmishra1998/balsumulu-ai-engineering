# Skill: Skill Evaluation

## Purpose
Evaluate whether an external or internal skill meets the harness quality bar and should be adopted, improved, or replaced.

## When to Use
- After skill-discovery identifies a candidate
- During periodic review of adopted skills
- When a skill's output quality is questioned

## Evaluation Framework

### Functional Evaluation
1. Does it produce the expected output format?
2. Does it handle edge cases?
3. Does it integrate with the harness workflow?
4. Does it respect the policies (security, approval, source-of-truth)?

### Quality Evaluation
| Dimension | Criteria | Minimum Bar |
|---|---|---|
| Accuracy | Output is correct and reliable | > 90% accuracy on test cases |
| Completeness | Covers all required aspects | No critical gaps |
| Consistency | Same inputs produce consistent outputs | Deterministic where needed |
| Usability | Easy for the AI editor to invoke | Clear instructions, predictable behavior |

### Integration Evaluation
1. Can it be called from the MCP server?
2. Does it work with the orchestration state machine?
3. Does it respect HITL checkpoints?
4. Does it handle errors gracefully?

### Security Evaluation
1. Does it handle data per the security policy?
2. Does it expose credentials?
3. Does it send data to unauthorized endpoints?
4. Is the source code auditable?

## Evaluation Process

1. **Define test cases** — representative inputs with expected outputs
2. **Run the skill** against test cases
3. **Score** against the framework above
4. **Document findings** in `skill-registry/`
5. **Recommend** to founder: adopt / improve / reject

## Output
Evaluation report added to `skill-registry/` with:
- Skill name and source
- Evaluation date
- Scores per dimension
- Recommendation
- Conditions (if any — "adopt only if X is fixed")

## Tips for the AI Editor
- Test with real-world inputs, not just happy paths
- Check how the skill handles missing or malformed input
- Evaluate the skill in the context of the full workflow, not in isolation
- A skill that works great alone but doesn't integrate well isn't useful
