---
description: Kick off or continue a Candour build phase after a PROCEED decision
---
Build phase for: $ARGUMENTS

Preconditions: a PROCEED decision record exists in `decisions/`. If not, stop and say so. Run this inside a `/coordinator` session if the CEO wants the Coordinator's autonomy; outside one, ask before each step (`roles/coordinator.md`, D14).

**Before any code:** the product repository's security baseline is in place and has been seen to block (`pipeline/agentic-agile.md` item 10), and so are its Claude Code agent controls (`pipeline/cso-advice-permission-mode.md` §5).

1. pm-ba subagent: produce/refresh `products/[slug]/requirements.md` with QA-verifiable acceptance criteria. No build starts without them. Tickets are generated from it (item 1).
2. cto subagent: architecture ADR, standards, and **wave plans with file ownership** (items 2–3); cso subagent: threat model alongside it.
3. **Build in waves, ticket by ticket, through "The per-ticket chain" in `pipeline/agentic-agile.md`.** That chain is the order, and this file does not restate it: engineer builds and opens the PR (`Refs #n`); CTO review (plus CSO where labelled); **full QA before merge**; **the CEO merges**; QA's integration check at each wave gate; QA marks Done only after it. Parallel engineers only on separated workstreams, within item 4's limit.
4. ux-lead: Article 4 and accessibility check during the build and before release; qa subagent: release-readiness report with coverage gaps stated.
5. End every phase by having the cgo subagent compile `pipeline/templates/review-pack.md` and present it to the CEO with a demo. Work is not done until reviewed (Constitution 5.5).

Blocks by CGO/CSO/QA/UX halt release; only the CEO may overrule, recorded in the decision log. Where this file and `pipeline/agentic-agile.md` differ, `pipeline/agentic-agile.md` governs; say so and ask.
