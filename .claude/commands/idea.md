---
description: Take a spark or full proposal from the CEO into the Candour pipeline
---
The CEO has an idea: $ARGUMENTS

1. Act as the CVO (read `.claude/agents/cvo.md` context). If this is a bare spark, draft `pipeline/templates/idea-brief.md` into `proposals/[slug]/idea-brief.md`, asking the CEO only what genuinely can't be inferred. If it's already a full proposal, move straight to step 2's commissions and then `/gate` prep.
2. Commission discovery: delegate to the research-analyst subagent (research brief → `research/[slug]-brief.md`) and the cfo subagent (cost model). Add a cto feasibility note if the idea is technically novel.
3. When discovery returns, synthesise a proposal from `pipeline/templates/proposal.md` into `proposals/[slug]/proposal.md`.
4. Record the anti-drift deadline (research brief date + 4 weeks) prominently in the proposal, and tell the CEO the date.
Do not proceed to a gate decision — that is `/gate`, and the decision is the CEO's.
