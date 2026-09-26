# Haunts — status and hand-off

**As of:** 2026-09-26 · **Branch:** `haunt/requirements` (based on the merge of PR #1) · **Phase:** requirements complete; build not started
**Product name:** Haunts (D9) · **Slug, branches, paths:** `haunt` — unchanged, do not rename · **Code repo:** `deopea-david/haunts` (D27, not yet created)

This note exists so a new session can pick up without the conversation that produced it. **It summarises; it does not decide.** Where it and the decision record disagree, the decision record wins.

---

## Read these, in this order

1. `decisions/2026-09-16-haunt-gate.md` — **the source of truth.** Conditions 1–10, Corrections C1–C6, and **CEO decisions D1–D26**, which is where the product actually got decided.
2. `products/haunt/requirements.md` — ~200 numbered requirements with acceptance criteria. §22 is the open-items list; §23 (suggestions) is closed.
3. `products/haunt/cost-sheet-v3.md` — the publishable cost sheet, including the §20 addendum on pay-once step-downs.
4. `constitution.md` — **v1.3** (tagged `v1.3`). Amended twice during this cycle; read it fresh, not from memory.

Seat notes behind the decisions, if needed: `block-4-ruling.md`, `venue-index-*.md`, `map-options-comparison.md`, `map-tiles-note.md`, `ux-home-headlines.md`, `ux-note-pricing.md`, `subscription-*.md`, `compliance-note.md`, `feasibility-note.md`, `android-and-stack-note.md`. Earlier cost sheets (`cost-sheet.md`, `-v2.md`) and the pricing and window models are **superseded** and kept for the record.

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
| D27 | Code, tickets and board in a separate repo named **`haunts`**; backlog split into **epics → features → tasks**; tickets link to requirement IDs, never copy them |

## Blocks and gates

- **Block 4 (CTO, venue index):** limb (a) withdrawn; **limb (b) lifts with signed-off requirements containing R-1–R-5 and R-7.** Requirements now exist — the CTO confirms lift at build planning.
- **CFO block:** lifted in full (v1.3 published a period).
- **Block 2 (CTO, Android device matrix):** live — now the larger build risk.
- **Launch bars, not build bars:** qualified human legal review (Constitution 6.1), including the refund duty, which no build creates a mechanism for; CGO confirmation of the privacy wording as a contract term; the three name checks for "Haunts" (App Store collision, UK trademark, domain).

## Still open

**CEO decisions** (in `requirements.md` §22):
- **Item 9 — EU storefront:** UK only at launch, or EU too relying on the accessibility microenterprise exemption. Recommendation prepared in §16.1.
- **Item 19 — commission the icon brief** from UX. The icon is a **blocking launch requirement** and on the critical path. Artwork itself is a human or tooling spend.

**Technical, for build planning:** Android minimum version (item 20); map render test on two phones (24); a possible React Native reduce-motion bug on Android (21); several pieces of scope **not in the 2,090-hour estimate** — headlines, heatmap (55–95 h), photos, search-in-notes, self-portrait. The CFO must re-cost once the CTO sizes them.

**Never done, and should be:** usability testing of any kind (item 1).

---

## Next step

**Set up the build: repo, board and tickets.** Decided so far (D27): a separate repo, `deopea-david/haunts`; a backlog of epics → features → tasks; tickets link to requirement IDs and track state only.

> **Do not create the repo, board or any tickets without the CEO's explicit go-ahead.** He asked for this in writing. Ask first.

**Before anything is created, in order:**
1. **The CEO merges the PR** carrying `haunt/requirements` into `main`, so ticket links can point at a stable commit.
2. **Repo visibility — public or private** — is the CEO's to decide. Not yet asked.
3. **`gh` needs the `project` scope** to create a board. The token for `deopea-david` has `repo`, `workflow`, `gist`, `read:org` only. The CEO runs `gh auth refresh -h github.com -s project` himself (it is interactive). The GitHub MCP connector is **not** authorised, so use `gh`.
4. **The PM/BA proposes the backlog mapping** — which requirement IDs sit under which feature and epic — plus the written standup routine. The CEO sees it before any ticket exists.

**Standups are written, not a conversation.** Agents are stateless, so a standup is each seat (PM/BA, QA, Engineer) reading the board and recent commits and recording a short dated status. The PM/BA summarises for the CEO.

**Still owed at build planning:** the CTO's written confirmation that Block 4 limb (b) lifts against `requirements.md` §7.7.7.

---

## How this company works — things a new session should know

- **Replies to the CEO are short and plain; documents stay thorough.** One decision at a time. This is in `CLAUDE.md` and binds every seat's summary.
- **Seats are the agents in `.claude/agents/`**, each bound to its charter in `roles/`. **The main session is the orchestrator** (CEO, 2026-09-26): it commissions the seats, routes their artifacts between them, and brings the CEO only questions and decisions. The CEO guides and decides. Where no seat owns a task, the main session has acted as the **CVO**.
- **Record decisions as they are made**, in the decision record's CEO decisions log, then commit and push. Uncommitted work has been lost once in this cycle.
- **Never `git add -A` blindly.** It once swept an in-progress requirements draft onto the wrong branch. Stage named paths.
- **Agents hit rate limits.** When one fails, check disk for its partial file, then start a fresh agent told to *continue* from it rather than restart — old agents cannot be resumed across sessions.
- **Commission agents to write incrementally to disk** and to give a short summary back.
- **The CEO has caught errors the seats missed**, repeatedly, by reading the source text himself. Take his challenges seriously; several changed the outcome.
