# Haunts — status and hand-off

**As of:** 2026-10-09 (`haunts` `origin/main` at `dc9a0a0`, 2026-10-04; no PR open since) · **Phase:** planning complete; **no M1 ticket has started** (SPK-21 and MAINT-4 are open with no branch or PR; every board item is Backlog or Done, none Ready). M0's 17 remaining spikes are open.

This file is state, not authority. Facts below come from `git log origin/main`, `gh pr list` / `gh issue list --repo deopea-david/haunts --state all`, and `gh project item-list 1 --owner deopea-david`, all run 2026-10-09 [E].

**Product name:** Haunts (D9, still a working name until PLAT-6's checks pass) · **Slug in `candour`:** `haunt` · **Code repo:** `deopea-david/haunts` (private; local clone `~/Documents/haunts`) · **Board:** https://github.com/users/deopea-david/projects/1

This note exists so a new session can pick up without the conversation that produced it. **It summarises; it does not decide.** Where it and the decision record disagree, the decision record wins.

---

## Read these, in this order

1. `decisions/2026-09-16-haunt-gate.md` — **the source of truth**: Conditions 1–10, Corrections C1–C6, and **CEO decisions D1–D66**.
2. `products/haunt/requirements.md` — **v1.4**, 221 requirement IDs with acceptance criteria. §22 holds the open questions, §24 the scope-change log.
3. `products/haunt/architecture/ADR-0001-code-architecture.md` — **the code architecture (B-strict, D64)**. Read it before writing any code.
4. `~/Documents/haunts/CLAUDE.md` and `docs/conventions.md` — how work is done in the code repo (traceability, commits, branches, merges, the security rules, TypeScript style).
5. `products/haunt/backlog-plan.md` and `standup-routine.md` — how tickets, the board and standups work. `agentic-agile-adoption.md` covers waves and the delivery measures.
6. `constitution.md` (v1.3) and `pipeline/model-selection.md` (which model each seat uses).

Design: `products/haunt/design/` (rounds 1–3; the final marks are in round 3). Costs: `cost-sheet-v3.md` plus `cost-sheet-v3-addendum-design.md`. Sizing: `design-feasibility-and-sizing.md`.

---

## What Haunts is

A private, on-device journal of places visited. The phone detects visits; the user confirms them, rates venues and adds notes. **Nothing leaves the device** except user-chosen backup to their own cloud, their own photos being fetched from their own cloud to display, and a one-time map download identical for every user. iOS **and** Android at launch, React Native with native capture.

## Decisions in one line each

| | Decision |
|---|---|
| D1 | iOS and Android at launch |
| D2 | *Superseded by D4* |
| D3 | Venue matching: nearest first, the user's own confirmations as a prior, uncertainty shown |
| D4 | Build cost amortised over a standard period; Haunts publishes **no guaranteed support date** |
| D5 | Sharing layer **gated**, not closed — reopens only through a fresh proposal and full gate |
| D6 | Standard amortisation period: **three years**, reviewed once at first launch + 12 months |
| D7 | Cumulative margin cap binds; **≥90 days' notice** before any price rise |
| D8 | Confirm interaction: nearest by default, options when unclear, search always reachable (20 rows, prefix match, never auto-select) |
| D9 | Named **Haunts** |
| D10 | Companions, competitor import, "what Haunts has worked out about you" screen, heatmap, recap |
| D11 | Photos by reference; recap saveable as image with hideable logo; icon owed (UX) |
| D12 | Photos fetched from the user's own cloud; thumbnail cached at attach; privacy wording reworded |
| D13 | Export is a right-of-access tool; rating trend in; ranked list + heatmap as two views |
| D14 | **Pay-once £28.99 leads**, yearly £9.89, monthly 99p, no quarterly; **90 days' notice**; thumbnails in backup |
| D15 | Pay-once steps down on **build-recovery milestones**, not dates |
| D16 | Shared company costs split equally; weighted if a product's price moves ≥10% |
| D17 | Candour absorbs pay-once buyers' support after year three |
| D18 | Every price recomputed at each annual review and cut when the numbers allow |
| D19 | Weighted rating order (true stars always shown); merge duplicates; search notes; self-portrait |
| D20 | Self-portrait headlines on the home screen — **celebrate memories, never volume** |
| D21 | **Product-wide: never encourage drinking or reward visit frequency** (requirements MEM-1) |
| D22 | Heatmap map: **offline OS Open Zoomstack** + MapLibre, optional ~0.8 GB store download |
| D23 | **Minimum iOS 26** |
| D24 | Health, religious, social-service places out of headlines by default; **protective defaults, user can change** (DFLT-1) |
| D25 | Uncategorised places: per-entry headline toggle; typed-in on, imported off, bulk switch on import |
| D26 | Strip clubs, casinos, off-licences also out of headlines by default |
| D27 | Code, tickets and board in a separate repo named **`haunts`**; backlog split into **epics → features → tasks**; tickets link to requirement IDs, never copy them (*copying superseded by D31*) |
| D28 | `haunts` repo **private now, public later** under a personal-use, non-commercial licence; licence text with the CGO; written reason owed (`LICENSE.md` presumes open source) |
| D29 | **Secret scanning (gitleaks and/or similar) on pre-commit before any code** in `haunts`; CSO specifies the baseline |
| D30 | Backlog mapping approved (17 epics, 67 features, 211 tasks); **Kanban** board; **QA** column; only QA moves a requirement ticket to **Done** |
| D31 | Tickets carry the requirement and acceptance criteria **in full**, stamped with the `requirements.md` commit; **the document wins** |
| D32 | CSO security baseline approved — **live on `haunts`**, CI green |
| D33 | Tickets have a files section, **TBD until the CTO designs the architecture** |
| D34 | Ticket format from the agentic-agile adoption plan; implementation stories only when needed, **closed on merge**; waves inside Kanban |
| D35 | **CEO logs his own hours** per phase, roughly, for the cost sheet |
| D36 | Phases are **GitHub milestones** M0–M5; a milestone closes only with the CGO review pack and demo |
| D37 | Every commit, branch and PR carries its **ticket key** (Conventional Commits, scope = key; `Refs: #n`, never closing keywords) — enforced |
| D38 | Design: clean, modern, distinctive; selectable themes; UX commissioned |
| D39 | **Merge commits only** (no squash, no rebase); full history kept |
| D40 | **commitlint** for message format, plus a small custom check |
| D41 | **`pre-commit`** is the only hook manager; **all `haunts` scripts in TypeScript** |
| D42 | Design feedback on round 1 |
| D43 | CSO baseline changes approved; **`MAINT-n`** ticket series for maintenance |
| D44 | Three selectable themes; default left to research |
| D45 | HEAD-8 amended: Mono's **typed headline** with a blinking cursor |
| D46 | **Mono is the default theme** (for now); store icon is Mono's h |
| D47 | Themes named **Warm, Mono, Retro** |
| D48 | Floating tab bar (amended by D53) |
| D49 | Warm's ticker is **Rotate** |
| D50 | More headline templates and phrasings, never generated freely |
| D51 | **User-chosen app icon at launch** |
| D52 | Theme-specific components allowed, kept to a minimum, in a register |
| D53 | Tab bar is **Expo Router Native Tabs**; build on the **SDK 58 beta** (CTO checks its bugs); contrast measured, not opacity floors |
| D54 | Contrast re-checked on bar-colour change and each **major iOS release**; **Retro has its own bevelled bar** |
| D55 | Android uses Material's docked bar |
| D56 | Recap credit is always the store mark |
| D57 | HEAD-8 reading: a chosen appearance's own motion is not an "entry animation" |
| D58 | Rotate capped at 3 facts per open |
| D59 | **Architecture decided before any product code** (SPK-20) |
| D60 | Design scope widened the cost gap (+£15,586 one-off, +18% cost base); **all prices hold** |
| D61 | Phone's own backups are the user's choice; the app says so (PRIV-9) |
| D62 | Dependabot never proposes `@types/node` majors |
| D63 | **Two SQLite files, one owner each** (`capture.db` native, `journal.db` app); proven corruption hazard otherwise |
| D64 | **Architecture: Option B-strict** (feature folders on a small core; 17 checks at commit and in CI); ADR-0001 |
| D65 | Export includes unconfirmed capture candidates, marked as such |
| D66 | Revised PRIV-1 privacy sentence approved (CGO to confirm before launch) |

## Blocks and gates

- **Block 4 (CTO, venue index): LIFTED** (SPK-01, `block-4-lift.md`).
- **Block 2 (CTO, Android device matrix): live.** It lifts with SPK-02.
- **CFO:** prices hold (D60). A launch cost sheet (v4) is due once SPK-08 sizing lands.
- **Launch bars, not build bars:** qualified human legal review (Constitution 6.1); CGO confirmation of PRIV-1 (D66); the PLAT-6 name checks for "Haunts"; the CGO's font-licence readings (SPK-18); the licence decisions before the repo goes public (D28, `code-licence-note.md`).

---

## What has landed in `haunts` since the security baseline (D32)

Merged PRs [E: `gh pr list --repo deopea-david/haunts --state all`, 2026-10-09]:

| PR | Ticket | Merged | What |
|---|---|---|---|
| #299 | SPK-15 | 2026-09-27 | Traceability standard and enforcement |
| #300 | SPK-16 | 2026-09-27 | Agent scaffolding, story and PR templates |
| #309 | SPK-15 | 2026-09-27 | Prefer arrow functions in TypeScript tools |
| #310 | MAINT-1 | 2026-09-27 | Deny force pushes by refspec |
| #311 | MAINT-2 | 2026-09-27 | Dependabot npm updates, 7-day cooldown |
| #349 | MAINT-3 | 2026-10-02 | Closing-keyword check scoped to this repository |
| #351 | MAINT-5 | 2026-10-02 | Dependabot holds `@types/node` to our Node major (D62) |
| #357 | MAINT-6 | 2026-10-04 | Agent controls: deny rules, guard hook, CEO merges |
| #358 | MAINT-6 | 2026-10-04 | Close guard bypasses; QA step in the PR template |

Closed PRs #304, #305, #306 were superseded by #309, #310, #311; Dependabot's #312 was closed unmerged (D62).

**Closed tickets (8, all Done on the board):** SPK-15 (#297), SPK-16 (#298), MAINT-1 (#302), MAINT-2 (#303), MAINT-3 (#307), SPK-17 (#346), SPK-20 (#348), MAINT-5 (#350). SPK-17 (design costing) and SPK-20 (architecture, ADR-0001) closed with no code PR in `haunts`.

**Not landed:**
- **SPK-21 (#355) and MAINT-4 (#308) have not landed**: both open, no PR. Both are M1 — Foundations. SPK-21 is owned by the CTO (the Engineer builds); MAINT-4 by the Engineer (issue label `seat:engineer`).
- **MAINT-6 (#356)** is merged but its issue is open (see findings).

**M0 spikes still open (17)** [E: board, all Backlog; owner seat from the board]:

| Issue | Spike | Owner seat |
|---|---|---|
| #279 | SPK-01 Block 4 limb (b) against 7.7.7 | CTO |
| #280 | SPK-02 Android device matrix (Block 2) | CTO |
| #282 | SPK-03 Android minimum version | CTO |
| #288 | SPK-04 Heatmap render test | CTO |
| #283 | SPK-05 RN reduce-motion on Android | Engineer |
| #289 | SPK-06 Backup KDF | CSO |
| #284 | SPK-07 Local notification authorisation | Engineer |
| #294 | SPK-08 Size scope outside the 2,090 h | CTO |
| #295 | SPK-09 Re-cost the build | CFO |
| #285 | SPK-10 Store trial mechanism | CTO |
| #290 | SPK-11 Photos C-1 durable reference | CTO |
| #291 | SPK-12 Backup architecture branch | CTO |
| #292 | SPK-13 Competitor export formats | CTO |
| #286 | SPK-14 Relinquish location authorisation | Engineer |
| #344 | SPK-18 Font licences | CGO |
| #345 | SPK-19 Area name from Places alone | CTO |
| #354 | SPK-22 Android build without INTERNET | CTO |

## Findings for the owning seats (flagged, not fixed here)

1. **MAINT-6 (#356), for the CTO and QA.** Merged in #357 and #358 (2026-10-04), but the issue is open, has **no milestone**, and is the **one board item with no Status** (no Level or Owner seat either). It is a hand-made `MAINT-n` ticket, the case the "always set a board Status" rule exists for. In the per-ticket chain it is past the CEO's merge: **QA's wave-gate integration check, and moving it to Done, are QA's** (D6). Setting its milestone and Status belongs to the CTO. Nothing records that either has happened [I].
2. **`Wave` field, for the CTO.** The field **exists** on the board (`gh project field-list`, text) but **no item carries a value** [E: `item-list` JSON has no wave key]. The CTO sets it at wave planning (`backlog-plan.md`); no wave has been planned yet [I]. (This corrects the Coordinator's reading that the field was absent.)
3. **SPK-01 (#279), for the CTO.** Block 4 is recorded as lifted (`block-4-lift.md`) but the ticket is open in Backlog with no comment. Close it, or say what remains [I].
4. **Spikes the previous list omitted:** SPK-01, SPK-05, SPK-08 and SPK-09 are open but were not named. SPK-08 and SPK-09 gate the v4 launch cost sheet (CFO).
5. **MAINT-4 (#308)** has no Owner seat or Level on the board; its issue label says `seat:engineer`. Board and issue disagree by omission.
6. **Counts:** 344 board items = 344 issues. Status: Backlog 335, Done 8, none 1. Milestones: M0 32, M1 55, M2 90, M3 45, M4 76, M5 45, none 1. M1–M5 remain provisional until the CTO confirms them.

---

## Still open

**CEO decisions, to bring one at a time:**
- EU storefront (PLAT-5, `requirements.md` §16.1)
- usability testing (never done; §22 item 1)
- the five licence decisions (`code-licence-note.md` §9; none urgent until go-public)
- the `SECURITY.md` contact address (before go-public)
- paying for final icon artwork (PLAT-7), after the CGO's ownership question

**For seats:** `requirements.md` §22. These include whether the venue index is left out of Android backups (it nearly fills the 25 MB limit), whether the app-switcher cover hides the whole app, the capture module's restore call, and the PM/BA's two import rules from D65 (CTO and CSO to review).

---

## Next step: the build (M1)

*State at 2026-10-09: none of the steps below has started. SPK-21 (#355) and MAINT-4 (#308) are open with no PR [E: `gh pr list --state all`, 2026-10-09].*

1. **CTO plans the first wave of M1.** Start with **SPK-21 (the B-strict scaffolding)** and **MAINT-4 (the arrow-function lint rule)** in the same set-up wave, then the two-file store (DATA-1/2, D63), the JS-free capture path (CAP-1), entitlement and sessions foundations. Fill each ticket's CTO-maintained files section, set the **Wave** field, and confirm or move the **provisional** milestones (M1–M5).
2. **CSO writes the threat model** alongside the first wave, and approves the B-strict dev tools (`dependency-cruiser`, `eslint-plugin-eslint-comments`).
3. **Remaining M0 spikes** (the 17 in the table under "What has landed") run as desk research in the background, two or three at a time.
4. **Standups start** (`standup-routine.md`). The CEO logs his hours per phase (D35).

**The PR flow in `haunts`:** the author seat opens a branch (`type/KEY-slug`) and writes commits with the key and `Refs: #n`. The main session pushes and opens the PR. **A seat other than the author reviews**, and the review is pinned to the head commit and posted on the PR. The CSO reviews anything labelled `needs:cso-review`. **QA verifies the PR in full before merge** (D6), checking a split requirement limb by limb on each PR (D9). The CEO merges every PR (D8) with **"Create a merge commit"**. If GitHub offers "Update branch", choose **merge, never rebase**. After merge, QA runs a light integration check once per wave, checks a split requirement as a whole (D9), and only then alone moves the ticket to Done (D6). Decisions D6, D8 and D9: `decisions/2026-10-02-coordinator-seat.md`; practice: `pipeline/agentic-agile.md`.

**Tickets:** generated from `requirements.md` by `backlog-tickets.py` and created by `backlog-create.py` (key → issue map in `backlog-issues.csv`). A changed requirement means regenerating the ticket body, never hand-editing it (D31). **Always set a board Status on any ticket created by hand** (the `MAINT-n` ones were once left without one).

---

## How this company works — things a new session should know

- **Replies to the CEO are short and plain; documents stay thorough.** One decision at a time. This is in `CLAUDE.md` and binds every seat's summary.
- **Seats are the agents in `.claude/agents/`**, each bound to its charter in `roles/`. **The main session is the Coordinator only after `/coordinator`** (D14): it commissions the seats, routes their artifacts between them, and brings the CEO only questions and decisions. The CEO guides and decides. Where no seat owns a task, the main session acts as the **CVO** only in a fresh session and only when the CEO explicitly asks (D16). Decisions D14 and D16: `decisions/2026-10-02-coordinator-seat.md`.
- **Record decisions as they are made**, in the decision record's CEO decisions log, then commit and push. Uncommitted work has been lost once in this cycle.
- **Never `git add -A` blindly.** It once swept an in-progress requirements draft onto the wrong branch. Stage named paths.
- **Agents hit usage limits and occasionally stall.** Commission them to write incrementally. When one stops, resume it with SendMessage and ask it to continue from disk. Run two or three at a time, not more.
- **Subagents in worktree isolation can only write inside their own worktree**, so copy their files onto the PR branch. The **auto-mode classifier** sometimes blocks GitHub board writes or fails transiently; if it does, ask the CEO or retry.
- **Agents hit rate limits.** When one fails, check disk for its partial file, then start a fresh agent told to *continue* from it rather than restart — old agents cannot be resumed across sessions.
- **Commission agents to write incrementally to disk** and to give a short summary back.
- **The CEO has caught errors the seats missed**, repeatedly, by reading the source text himself. Take his challenges seriously; several changed the outcome.

---

## Commissions (Coordinator)

### 2026-10-09 — PM/BA, STATUS refresh — sonnet, effort medium

Commission from the Coordinator (CEO ran /coordinator; the CEO asked for this in his words: "have the PM/BA refresh STATUS.md").

**Objective.** Refresh `products/haunt/STATUS.md` in the `candour` repo so a stranger can pick up the Haunts build from it today (2026-10-09). It was written 2026-10-02 and carries a dated note that the `haunts` repo has moved on. Establish where Haunts actually is from primary sources, and rewrite the stale parts. It is state, not authority: it summarises and never decides.

**Sources (read them; do not rely on this brief for facts).**
- `haunts` repo at `/Users/davidparrish/Documents/haunts` (read-only for you): `git log origin/main` (run `git -C /Users/davidparrish/Documents/haunts fetch -q` first), `gh pr list --repo deopea-david/haunts --state all`, `gh issue list --repo deopea-david/haunts --state all --limit 400`, and the board: `gh project item-list 1 --owner deopea-david --limit 500 --format json` and `gh project field-list 1 --owner deopea-david`.
- `candour`: `products/haunt/STATUS.md`, `decisions/2026-09-16-haunt-gate.md`, `decisions/2026-10-02-coordinator-seat.md` (D6, D8, D9, D22), `products/haunt/backlog-plan.md` (§7 statuses, the field table including `Wave`), `products/haunt/standup-routine.md`, `pipeline/agentic-agile.md` ("The per-ticket chain").

**What the Coordinator saw, to check rather than copy:** `haunts` main is at `dc9a0a0` (PR #358 merged 2026-10-04; #357 the same day; both MAINT-6). Closed issues: SPK-15, SPK-16, SPK-17, SPK-20, MAINT-1, MAINT-2, MAINT-3, MAINT-5. **SPK-21 (#355) and MAINT-4 (#308) are open with no PR.** MAINT-6 (#356) is open with no milestone, and one board item has no Status. The board has no `Wave` field, although backlog-plan.md defines one. All 344 board items are Backlog or Done; none is Ready.

**Write.**
1. Update the "As of" line, the phase, and every dated "has moved on" note (replace them with the current state).
2. A short "What has landed" section: each merged PR / closed ticket since the security baseline, with PR number and merge date, and what remains open of M0 (list each open SPK with its issue number and owner seat from the board).
3. Note, as findings for the owning seat (do not fix them yourself): MAINT-6's missing milestone and board Status, and where it sits in the per-ticket chain (merged; QA's wave-gate integration check and Done are QA's); the missing `Wave` field (the CTO sets it at wave planning); any other board/issue mismatch you find.
4. Keep the decision table, blocks, reading order and "how this company works" sections; correct only what is now wrong. Keep the decision table's wording unless a decision record says otherwise.
5. Add a section "Commissions (Coordinator)" at the end and paste this commission into it verbatim, under the heading "2026-10-09 — PM/BA, STATUS refresh — sonnet, effort medium".
6. Provenance line: "PM/BA · sonnet (Sonnet 5.5) · effort medium · 2026-10-09".

**Boundaries.** You own only `products/haunt/STATUS.md`. Do not edit any other file, any issue, the board, or the `haunts` repo. Work in your worktree; never switch branches in either main checkout. Stage the one file by name (never `git add -A`). Commit on a branch named `docs/haunt-status-refresh` with a Conventional Commit message like `docs(haunt): refresh STATUS.md for the M1 start`, ending with the line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Do not push and do not open a PR; the main session does that.

**Evidence.** Tag claims per `pipeline/evidence-standard.md`; for repo facts cite the command or commit.

**Verify before you finish.** Re-run the issue and PR listings and check every issue number, PR number and date in your "What has landed" section against them. Grep the file for "moved on" and "2026-10-02" and confirm no stale state remains.

**Model.** Sonnet, effort medium (step-down from your Opus default under `pipeline/model-selection.md` §5.1: an inventory whose errors can be caught by reading the output; the CEO also asked for one Opus seat at a time).

**Write incrementally to disk.** Reply in under 12 lines: the branch and commit SHA, your worktree path, what has landed, whether SPK-21 and MAINT-4 have landed, and the findings for other seats.

---

*PM/BA · sonnet (Sonnet 5.5) · effort medium · 2026-10-09*
