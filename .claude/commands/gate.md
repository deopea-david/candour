---
description: Run a Candour decision gate on a proposal
---

Run the gate for: $ARGUMENTS

1. Delegate to the skeptic subagent FIRST, with a NEUTRAL invocation: file paths and nothing else — no summary, no opinion, no expected outcome (it will report any steering it detects). It reads the artifacts from disk, verifies citations per `pipeline/evidence-standard.md` (all load-bearing sources retrieved and checked, rest sampled, independence tested, unverifiable flagged), and writes `proposals/[slug]/dissent-memo.md` including its verification report. Its text is never edited by anyone.
2. In parallel, collect: cto feasibility note, cfo cost model check, cgo compliance read (and ux-lead read if user-facing).
3. As the cgo subagent, compile the full gate pack: proposal + research brief + cost model + dissent memo + seat notes, plus a one-page summary that does NOT soften the dissent.
4. Present the pack to the CEO with the three options (kill / proceed / park + revisit date) and the anti-drift deadline status. The CEO decides — never decide for them, and require a written response to the dissent before recording PROCEED.
5. Record the outcome using `pipeline/templates/decision-record.md` into `decisions/`, dated, noting any overruled blocks.
