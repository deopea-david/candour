# Consistency sweep — after the Coordinator week

**CGO · sonnet (Sonnet 5.5) · effort high · 2026-10-04.** Commissioned by the main session on the CEO's instruction: *"we do not want anything to be out of date after this weeks changes … Check other areas for inconsistensies as well"*. Base: `origin/main` at `4862a9c`. Branch `governance/consistency-sweep-2026-10-04`, not pushed.

**Benchmark.** `decisions/2026-10-02-coordinator-seat.md` D0.1–D19 and `pipeline/agentic-agile.md`: the Coordinator runs only via `/coordinator` (D14); any seat but the Skeptic only in a fresh session on the CEO's explicit ask (D16); the CEO merges every PR (D8); full QA before merge, a wave integration check, then Done (D6, D9); controls trusted with limits and restart after any `.claude/` change (D10); no unattended work; credits confirmed by the CEO each session (D19); widgets stay (D18); agent teams off (D7); model selection unchanged.

**Read:** `CLAUDE.md`; every `roles/*.md`; all 11 `.claude/agents/*.md`; the commands `idea`, `gate`, `audit`, `scout`, `agile-sync` (`build.md` skipped, as commissioned); `pipeline/agentic-agile.md`, `model-selection.md`, `evidence-standard.md`, `omission-check-markers.md`; all nine `pipeline/templates/*.md`; `products/haunt/STATUS.md`, `standup-routine.md`, and by keyword search the rest of `products/haunt/*.md`; `README.md`; `project-instructions.md`; `constitution.md` (read only). **Not checked:** the `haunts` repository (`docs/conventions.md`, `.github/pull_request_template.md`, its `CLAUDE.md`); it is a separate repo.

**Evidence for "no unattended work":** a keyword search of the in-scope files for unattended, overnight, scheduled and cron found nothing stale. Two assumptions of a continuously running orchestrator are listed below (standup-routine.md lines 21, 104, 110).

---

## A. Fixed on this branch (19)

| # | File | What was stale | Fix |
|---|---|---|---|
| 1 | `CLAUDE.md` Who's who | Said nothing about the Coordinator, though its limits bullet refers to `/coordinator` | Added one bullet: not a subagent; the main session only after the CEO types `/coordinator` (D14); otherwise `CLAUDE.md` alone, no autonomy |
| 2 | `CLAUDE.md` pipeline list | `/coordinator` missing from the commands | Added |
| 3 | `CLAUDE.md` `/build` line | Old order ("QA/UX → review pack"), no review, merge or wave check | Now the D6 chain, pointing at `pipeline/agentic-agile.md`. *`build.md` itself is the main session's, on `docs/build-command-current`; the two should read alike when both land* |
| 4 | `roles/dormant-seats.md` | COO mandate ("run the machine so the CEO doesn't have to") overlapped the Coordinator with no boundary | Boundary added, quoting the Coordinator charter; overlap on activation goes to the CEO; v0.3 |
| 5 | `roles/cgo.md` Produces | The Coordinator charter gives the CGO its charter drafting, the M2/M8 script, the template markers and the phase-review audit; the CGO charter listed none | One sentence added |
| 6 | `roles/qa.md` Invoked | Silent on where QA sits in the chain (listed as owed in `pipeline/agentic-agile.md`) | Full QA before merge; integration check per wave; only QA moves to Done, after it |
| 7 | `pipeline/model-selection.md` | "The orchestrator" used 10 times, undefined; now ambiguous between the main session and the Coordinator | Dated terminology note under the header (it means the main session when it commissions; the Coordinator in a `/coordinator` session). No rule changed |
| 8 | `pipeline/model-selection.md` §4 CVO row | *"In practice the main session often acts as CVO"*; D16 allows it only in a fresh session on the CEO's ask | Reworded to D16 |
| 9 | `pipeline/model-selection.md` §7 | Fable option (c) written as live; credits have been off since D0.2, and the Coordinator charter cites §7 for "Fable unavailable" while §7 did not say it | Dated update added: Fable unavailable until the CEO turns credits on |
| 10 | `pipeline/model-selection.md` §5.5 | Provenance line did not record the role when the main session writes in a seat's role (the Coordinator charter relies on it) | One sentence added. (Also fixed "only only", §3 item 2) |
| 11 | `pipeline/templates/review-pack.md` QA line | Did not ask for pre-merge QA, wave checks or Done | Reworded |
| 12 | `pipeline/templates/review-pack.md` | The "Delivery measures and retrospective" section owed since 2026-09-26 (`pipeline/agentic-agile.md` item 8, "Follow-ups") | Section added: five measures, no self-scored ratings |
| 13 | `project-instructions.md` | *"twelve seats"*; the boardroom could be read as playing the Coordinator, whose charter says it is never invoked there | Reworded. **The CEO must re-paste the instructions into the claude.ai Project by hand** |
| 14 | `decisions/2026-09-16-haunt-gate.md` D30 | Column order read as QA-after-merge; D6 promised a cross-reference | Dated cross-reference added; text unchanged |
| 15 | same, D34 | *"reaches QA when all its stories are merged"*; D6 and D9 promised a cross-reference | Dated cross-reference added; text unchanged |
| 16–19 | `decisions/2026-10-02-coordinator-seat.md` | D19's time (13:41:51; the transcript gives 13:40:51 BST); conditions row 8 (broken strikethrough, "awaiting his merge" though PR #24 merged); line 597 ("not updated", done in `30b3b51`); the S3 row ("still owed") | Correction **C4**, original text quoted; stale lines marked by dated notes; row 8 split into the right cells |

---

## B. Not mine to fix: listed by owner

Line numbers are on `4862a9c`. "Edit" means the owner makes it by PR and the CEO merges.

### PM/BA (process files)

| File | Line | Issue |
|---|---|---|
| `pipeline/agentic-agile.md` | 31 | *"The orchestrator's commission"*: say "the main session's (the Coordinator's, in a `/coordinator` session)" |
| `pipeline/agentic-agile.md` | 30 | Item 5: *"The reviewer closes a story on merge"*. D8 left open that the reviewer closes it **after** the CEO's merge; `standup-routine.md` line 119 says so, this file does not |
| `pipeline/agentic-agile.md` | 74–91 | "Follow-ups not yet made" is itself stale. Done since: `STATUS.md` 127, `standup-routine.md` §8, the dated note in `agentic-agile-adoption.md`, `roles/qa.md` (item 6 above), the Haunts D34 cross-reference (item 15), `review-pack.md` (item 12). Still open: `build.md` (main session), the `haunts` repo files (CTO), `roles/cto.md` (CTO). Owners at lines 80, 83, 88 say "orchestrator" |
| `products/haunt/standup-routine.md` | 21, 33, 44, 85, 104, 108, 110 | "orchestrator" seven times; say "main session / the Coordinator" |
| `products/haunt/standup-routine.md` | 21 | A `standups` branch *"merged daily"*: the CEO merges every PR (D8), so this is a daily merge for him. Decide whether that is wanted |
| `products/haunt/standup-routine.md` | 104, 110 | *"The orchestrator commissions within one working day"* and a blocker that *"goes up one level automatically"*: both assume a main session running every day. It runs when the CEO opens one. Reword to "at the next session" |
| `products/haunt/backlog-plan.md` | 420 | Blocked view owner "PM/BA, orchestrator" (low; line 38 is a dated proposal, leave) |

### Main session

| File | Line | Issue |
|---|---|---|
| `products/haunt/STATUS.md` | 127 | *"The orchestrator pushes and opens the PR"*: fine as a fact, but "orchestrator" is now ambiguous. Say "the main session" |
| `products/haunt/STATUS.md` | 136 | *"The main session is the orchestrator … Where no seat owns a task, the main session has acted as the CVO."* Stale on both counts: since D14 it is the Coordinator only after `/coordinator`, and since D16 it acts as the CVO only in a fresh session on the CEO's ask |
| `products/haunt/STATUS.md` | 3, 120 | "As of 2026-10-02 … build starts at M1": the memory note says `haunts` is already at PR #351. State, not authority, but out of date |
| `.claude/commands/idea.md` | 6 | *"Act as the CVO"* |
| `.claude/commands/scout.md` | 8 | *"As the CVO"*. **One CEO decision**, see C below |
| `.claude/commands/build.md` | all | Skipped, as commissioned |
| **Memory** `main-session-is-orchestrator.md` | — | The body was already updated for D14/D16/D19 (modified 2026-10-04 14:23). **Still stale:** the file name and the `MEMORY.md` index line (*"commission seats, route work; CEO only guides and decides"*), which carry no `/coordinator` qualification. Rename or re-describe |
| **Memory** `chief-of-staff-seat-in-progress.md` | — | `MEMORY.md` description and file header: *"open: #23 omission check, credits-check method, D18, v1.4"*: #23 is merged, the credits method is settled (D19), D18 is decided. Body says *"D0.1–D17"* (now D19) and *"charter v0.7+"* (now v0.10). Its *"cosmetic fixes … owed for the CGO"* are all done (C4) |

### CTO

| File | Line | Issue |
|---|---|---|
| `roles/cto.md` | 23 | Produces: no wave plans, file ownership or the review record on every PR (`pipeline/agentic-agile.md` items 2, 3, 7; `model-selection.md` §4). Also the standing task of reviewing the `/coordinator` generator (D14) |
| `haunts` `docs/conventions.md` 102; `.github/pull_request_template.md` 41–50 | — | Not in this repo, not checked. `pipeline/agentic-agile.md` says they still have the orchestrator merging and no QA step |

### CSO

| File | Line | Issue |
|---|---|---|
| `roles/cso.md` | 23 | Produces: no `needs:cso-review` PR reviews, and no re-verification of the Annex F controls at each phase review and each Claude Code release (`roles/coordinator.md` Annex F; `pipeline/cso-controls-results.md`) |
| `products/haunt/repo-security-baseline.md` | 566 | Agent rule 5: *"report … to the orchestrator"*. Wording only |
| `products/haunt/repo-security-baseline.md` | 517, 569 | *"Never merge on a red secret-scan"*: no agent merges (D8), so this reads as if one does. Safe as it stands; say "never ask for a merge on a red scan". This text is embedded verbatim in `haunts/CLAUDE.md`, and `repo-security-baseline.md` says changes to the guard rails need a CSO note and the CEO's approval |

### CGO (me, on the next charter pass; not done now because it needs the command regenerated and the CTO's review)

| File | Line | Issue |
|---|---|---|
| `roles/coordinator.md` | 217 | "About this page", Status: a stray `**` after *"Not yet listed in Article 6:"*. Cosmetic, outside the compaction window |
| `constitution.md` | Article 6 table | Does not list the Coordinator. **Known and deliberate** until Decision 9 (D13); listed so nobody reports it as new |

### CEO (decisions, one at a time if he wants them)

| Question | Why |
|---|---|
| **C. Does typing `/idea` or `/scout` count as "explicitly asking for the CVO seat" (D16)?** And what if it is typed inside a `/coordinator` session, which cannot switch roles? | `idea.md` and `scout.md` say "Act as the CVO". What a clause means is his. Options: yes it counts, in a fresh session; or the commands commission the `cvo` subagent instead. Both command files are on Annex D's allowlist, so a change there changes the Coordinator's authority |
| **Add "the CEO merges every PR, in every repo; no seat merges" to `CLAUDE.md`?** | It is decided (D8) and enforced by deny rules, but `CLAUDE.md`, which every seat reads, does not say it. It is a limit, so I did not add it without his yes |
| Re-paste `project-instructions.md` into the claude.ai Project | Item 13 changes the file, not the Project |

---

## C. Records: noted, not flagged

Left as written: `decisions/2026-09-16-haunt-gate.md` (text), `pipeline/dissent-chief-of-staff.md` (the Skeptic's memo), `pipeline/amendment-draft-coordinator.md` and `amendment-draft-amortisation.md`, the `pipeline/cso-*` files, `pipeline/governance-review-2026-09.md`, `pipeline/amortisation-proposal.md`, `products/haunt/agentic-agile-adoption.md` (dated proposal; it has a 2026-10-04 note, and says "orchestrator" throughout), `products/haunt/backlog-plan.md` line 38, the cost sheets, notes, block rulings and spikes, and `proposals/`.

## D. Found clean

`roles/ceo.md`, `cfo.md`, `cvo.md`, `engineer.md`, `pm-ba.md`, `research-analyst.md`, `skeptic.md`, `ux-lead.md`; all 11 `.claude/agents/*.md` (model and effort match `model-selection.md` §4; none says anything about merging or orchestrating); `.claude/commands/gate.md`, `audit.md`, `agile-sync.md`; `pipeline/evidence-standard.md`; the other eight templates; `README.md`; `roles/coordinator.md` against the decision record (v0.10 matches D14–D19).

## E. What would overturn this, and where I looked

A stale statement in a file I did not open. The in-scope list above is what I read; the rest of `products/haunt/` was searched by keyword (orchestrat, merge, unattended, scheduled, routine, coordinator, main session, bypass), so a stale statement that uses none of those words would be missed. The `haunts` repo was not read.
