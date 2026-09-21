# Decision record — Scout round 2: Plot, Quizmaster, Postcard, Doorstep

**Date:** 2026-09-20 · **Decision:** PARK (revisit: **2027-03-01**) · **Decided by:** CEO
**Anti-drift (5.2):** deadline [none running once parked; had the clocks run, 2026-10-20] — measured from the research brief's delivery, or its due date if late, whichever is earlier. No brief was delivered; the committed due date was 2026-09-22.
**Published within 30 days (Constitution, Article 3) — due by 2026-10-20. Not yet published.**

## What was decided and why

The CEO parked all four ideas: *"put them on hold/defer them until a later date"*, because *"I am focusing on … the privacy focused location timeline app"* (Haunt). The CEO chose the revisit date of 2027-03-01 from three offered.

This decision does not rest on a commercial case, and none is constructed here. It is a decision about attention: Haunt is in build (a 2,090-hour, two-platform build per the CTO's figures in `decisions/2026-09-16-haunt-gate.md`, D1), and four parallel discovery clocks would compete with it.

**What state each idea is parked in** (none has a research brief or cost model; the six commissions issued on 2026-09-01 all failed on a rate limit before producing anything):

| Idea | Parked with these questions still open |
| ---- | -------------------------------------- |
| **Plot** | Is postcode-level frost variation large enough to change a sowing decision? (free test, HadUK-Grid, OGL v3). Is there any evidence people *pay* for UK sowing timing? |
| **Quizmaster** | Both scout kill reasons are **unanswered**: no evidence quiz buyers value cited answers, and verification cost may exceed a £2.00–£4.50 market. The CFO's cost of a verified 60-question pack was to be run first and is not done. |
| **Postcard** | Scout kill withdrawn on one ground only (CEO appetite for fulfilment work). Shape objections stand: no software leverage, cold start, recipient data under 6.1, unlimited liability on fulfilment failures. UK domestic only. |
| **Doorstep** | Re-aimed hypothesis (urban walking is underserved by Komoot/Strava) is **untested**; the original kill reason is not overturned. Which of three framings has a gap is undecided. |

## Written response to the dissent memo

No gate was run and no gate dissent memo exists. The pre-pipeline cull memo (`research/scouts/scout-2026-09-01-skeptic-cull.md`, on branch `scout/2026-09-candidates`) killed Quizmaster and Postcard; the CEO promoted both over it on 2026-09-01. **Parking does not answer that memo** — its objections carry forward unchanged to the revisit.

## Conditions attached to parking

| # | Condition | Owner | Due / gates what |
| - | --------- | ----- | ---------------- |
| 1 | Bring all four back for a decision, one at a time: revisit, re-park (with a fresh written reason and a new date), or kill. | CVO to surface; CEO decides | **2027-03-01** |
| 2 | Prices, competitor terms and data licences retrieved on 2026-09-01 are re-retrieved before any brief relies on them (evidence standard: they are dated claims). | Research Analyst | Gates any new commissioning |
| 3 | Any new commission for these four gets a fresh brief due date; the 2026-09-22 date lapses with this park. | CVO | Gates `/idea` on any of the four |

## Overrules exercised (if any)

None. No block was asserted or overruled.

## Corrections

**C1 — the same-day deferral note misdescribed the pipeline state.** `research/scouts/deferred-2026-09-20.md`, as first written, said *"no research brief has been commissioned"*, *"no anti-drift clock is running"* and *"no park record is required"*. The idea briefs committed on `scout/2026-09-candidates` (976a607) record each research brief as **"commissioned 2026-09-01, due 2026-09-22"** with decisions due 2026-10-20, and the commissions were issued that day. They failed to execute, so no brief exists. Whether a commission that never produced anything started a 5.2 clock is arguable; this park record makes the question moot. The note now carries a dated correction; its original text is preserved. The rules are unchanged, only the description of the pipeline state was wrong, so no weakening applies.
