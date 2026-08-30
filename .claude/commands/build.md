---
description: Kick off or continue a Candour build phase after a PROCEED decision
---
Build phase for: $ARGUMENTS

Preconditions: a PROCEED decision record exists in `decisions/`. If not, stop and say so.

1. pm-ba subagent: produce/refresh `products/[slug]/requirements.md` with QA-verifiable acceptance criteria. No build starts without them.
2. cto subagent: architecture ADR + standards; cso subagent: threat model alongside it.
3. engineer subagent(s): build to the acceptance criteria, tests included; parallel instances only on separated workstreams.
4. qa subagent: test plan from the acceptance criteria; independent verification; release-readiness report with coverage gaps stated. ux-lead: Article 4 + accessibility check.
5. End every phase by having the cgo subagent compile `pipeline/templates/review-pack.md` and present it to the CEO with a demo. Work is not done until reviewed (Constitution 5.5).
Blocks by CGO/CSO/QA/UX halt release; only the CEO may overrule, recorded in the decision log.
