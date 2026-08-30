---
description: Generate candidate ideas from scratch when the CEO has no initial spark
---
Scout for new Candour ideas. Optional focus/constraints from the CEO: $ARGUMENTS

This is PRE-pipeline work: nothing scouted enters the pipeline or starts an anti-drift clock until the CEO promotes it via /idea.

1. As the CVO (read `.claude/agents/cvo.md`), generate 6–10 candidate problem spaces. Hunt where Candour's constitution gives an edge: everyday people or small businesses being overcharged, locked in, or confused by incumbents; markets where transparent flat pricing is itself the differentiator; genuinely useful tools nobody builds because the margins look "too honest". Respect any CEO focus given above.
2. Delegate to the research-analyst subagent for a light validation pass on each candidate (existence of the problem, incumbents and their pricing, obvious blockers) — evidence-vs-inference labelled, an hour's rigour not a full brief.
3. Score each candidate against: constitution fit (Articles 1, 2, 4), cheapness to build and run, the CEO's actual reach (no industry contacts is a known constraint — favour ideas validatable without insider access), and honest niche size.
4. Delegate to the skeptic subagent for a one-paragraph cull: which candidates die immediately and why.
5. Write the shortlist to `research/scouts/scout-[date].md`: surviving candidates ranked, each with a two-line pitch, the strongest reason against, and what a full research brief would need to prove. Recommend at most 2 for promotion.
6. Present to the CEO. The CEO picks what (if anything) gets promoted to /idea — never promote automatically.
