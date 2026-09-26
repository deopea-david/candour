# Backlog plan — Haunts v1: epics, features, tasks

**Seat:** Product Manager / BA · **Date:** 2026-09-26 · **Version:** 0.2 (mapping approved at D30; ticket format per D31, D33, D34)
**Governing decision:** `decisions/2026-09-16-haunt-gate.md`, **D27** (CEO, 2026-09-26) · **Source of every requirement:** `products/haunt/requirements.md` v1.1, read from disk 2026-09-26
**Companion files:** `products/haunt/backlog.csv` (one row per epic, feature and task) · `products/haunt/backlog-build.py` (regenerates the CSV and re-runs the coverage check) · `products/haunt/standup-routine.md`

**Status: a proposal. Nothing has been created.** No repository, board, issue, label or milestone exists, and none will be created from this document without the CEO's explicit go-ahead. `products/haunt/STATUS.md` records that instruction: *"Do not create the repo, board or any tickets without the CEO's explicit go-ahead. He asked for this in writing. Ask first."*

**Evidence.** Almost everything here is about Candour's own files, read from disk on 2026-09-26 and cited by path and section. Four claims about how GitHub Projects behaves were retrieved this session and are tagged [E] with links (§13). Where something is this seat's judgment it is tagged [J].

---

## 0. The decision this asks for

**One decision: approve the mapping** — 17 epics, 67 features and 211 tasks, of which 197 are requirement tasks and 14 are planning and spike tasks — **or tell me what to move.**

Everything else in this document is either the mechanics that follow from that approval, or a proposal addressed to another seat (the phase order is the CTO's to confirm). Two gaps at §11 stop specific tickets reaching Ready (§11.2, PRICE-7/8/9 placeholders; §11.8, UX and QA confirmations for VEN-20 and VEN-22); both are seat work. One question at §11.3 — who signs off `requirements.md` — is the CEO's, and can wait until after this approval.

**Coverage: 197 of 197 requirement IDs appear exactly once as a task. None is left out** (§4).

---

## 1. What D27 decided, and what this plan does with it

D27, verbatim where it binds: *"Code, tickets and the project board live in a new repository, **`deopea-david/haunts`**. `candour` remains the governance record: `requirements.md` stays the single source of every requirement and acceptance criterion, and **tickets track state only** — they link to requirement IDs rather than copying criteria, so the two cannot drift apart."* And: *"The backlog is split into epics, features and tasks so that progress can be tracked at each level… **The mapping of requirement IDs onto those levels is the PM/BA's to propose**, and it goes to the CEO before any ticket is created."*

What follows from that, as rules for every ticket:

1. **A task is exactly one requirement ID** (or one planning item). Its title is a label, not a restatement.
2. ~~**No ticket body contains acceptance criteria.** It carries the ID, a link to `requirements.md` on `main`, and the section.~~ *Superseded by D31: the ticket carries a generated, SHA-stamped copy, and the document wins.* QA verifies against the file, never against the ticket.
3. **A task reaches Done only when QA has verified it against every acceptance-criterion limb in `requirements.md`**, at a recorded commit of that file. Merged is not Done (§7).
4. **The CSV is generated, not hand-edited.** `backlog-build.py` holds the mapping, reads `requirements.md`, writes the CSV and fails loudly if an ID is missing, duplicated or unknown. When `requirements.md` gains an ID, the mapping gains a line and the script is re-run.

---

## 2. The shape, and where I departed from the starting proposal

The orchestrator's starting proposal: epics as product areas (about 12–20), features as demonstrable capabilities, tasks as one requirement ID each, plus a "Build planning and spikes" epic. **I have kept all of it.** Departures, each with its reason:

| Departure | Reason |
|---|---|
| **ONB (§9.1) is a feature inside the Entitlement epic, not its own epic** | Three tasks, and ONB-2 is built on ENT-4's manual composer — the same composer, by requirement. The requirements document already nests it under §9 |
| **NOT (§11) is a feature inside the Pricing epic** | NOT-6 requires the price-rise notice (PRICE-12) and the notices surface (NOT-2) to be *"the same surface, not two"*. Splitting them across epics invites the two implementations NOT-6 forbids |
| **MEM-1 and DFLT-1 get their own small epic, "Product-wide rules"** | Both are verified across the whole build (MEM-1(a) is a build-wide string search; DFLT-1(a) is a build-wide register with a CI check). Filed under any one feature area, they would read as that area's problem |
| **VEN-22 sits under the Confirm epic, not the Venue epic** | VEN-22 (*"No confirmation may be completed from a surface that has not presented the alternatives"*) binds every confirm path. The engineer who builds CONF-3 and the D3 notification path must see it beside them. Its `section` column still says 7.7.3, so its provenance is intact |
| **Five spikes added beyond the eight named** (SPK-10 to SPK-14), **plus one CFO task** (SPK-09) | Each is an open technical question in `requirements.md` §22 or §12.1 that blocks a named BLOCKING or MUST requirement. Leaving them off the board would leave those requirements un-Ready with no visible reason. §5 names what each unblocks |
| **Epic and feature rows carry no priority and no platform** | Those would be roll-ups of their tasks — a second copy of a fact that can drift. The board computes them from the tasks (§8 views) |
| **Mixed-priority requirements carry their highest limb's priority** | Seven requirements have limb-level priorities (§11.1). A ticket field holds one value; the highest is the safe one. QA reads the limbs from the file |

**Keys.** Epics `EP-<AREA>`, features `FT-<AREA>-<n>`, requirement tasks are keyed by their requirement ID (so `CAP-3` is both the key and the requirement), planning tasks `SPK-<nn>`. Keys are stable once tickets exist; the GitHub issue number is recorded against the key at creation.

**Counts.** 17 epics · 67 features · 211 tasks (197 requirement tasks + 14 planning tasks).

**Requirement tasks by priority:** BLOCKING 135 · MUST 59 · CUT-LINE 2 (CONF-18, PRIV-7) · PENDING-ESTIMATE 1 (ONB-3).
**All tasks by platform:** both 182 · none 21 · android 5 · ios 3.
**All tasks by owning seat:** engineer 181 · cto 12 · cgo 6 · pm-ba 3 · qa 3 · ux-lead 2 · cfo 2 · ceo 1 · cso 1.

"Owning seat" means **the seat whose work makes the requirement true** and who moves the ticket to Review. QA verifies every task regardless of owner; that is what the QA column is for, not an ownership claim.

---
## 3. The mapping — every epic and feature

Generated from `backlog.csv`, so it cannot disagree with it. Task titles, priorities, platforms and owners are in the CSV; they are not repeated here.

### EP-RULES — Product-wide rules: memories not volume; protective defaults

§3.1, §3.2 · accountable seat: pm-ba · 2 features, 2 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-RULES-1 | Celebrate memories, never volume, build-wide | MEM-1 |
| FT-RULES-2 | Protective defaults and the settings register | DFLT-1 |

### EP-CAP — Automatic visit capture

§4 · accountable seat: cto · 6 features, 10 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-CAP-1 | Native capture pipeline and verifiable teardown | CAP-1, CAP-7 |
| FT-CAP-2 | iOS visit capture | CAP-2 |
| FT-CAP-3 | Android visit capture | CAP-3 |
| FT-CAP-4 | Capture honesty: gaps, reduced accuracy, location denied | CAP-4, CAP-5, CAP-6 |
| FT-CAP-5 | One capture-failure notification, nothing else | CAP-8, CAP-9 |
| FT-CAP-6 | Battery measured on real devices before any claim | CAP-10 |

### EP-CONF — Confirming visits

§5 · accountable seat: pm-ba · 4 features, 20 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-CONF-1 | Confirm queue as a pull, not a push | CONF-1, CONF-12, CONF-13, CONF-14, CONF-15, CONF-16 |
| FT-CONF-2 | Candidate rows: nearest first, choice never assent | CONF-2, CONF-3, CONF-7, CONF-10, CONF-11, VEN-22 |
| FT-CONF-3 | Venue search in the confirm flow | CONF-4, CONF-5, CONF-6, CONF-8, CONF-9 |
| FT-CONF-4 | Note, rating and companions on the confirm row | CONF-17, CONF-18, CONF-19 |

### EP-SESS — Sessions

§6 · accountable seat: cto · 4 features, 9 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-SESS-1 | Derived sessions with durable overrides | SESS-1, SESS-2, SESS-9 |
| FT-SESS-2 | Session queue, split and merge | SESS-3, SESS-4, SESS-5 |
| FT-SESS-3 | Home inference the user can see and edit | SESS-6 |
| FT-SESS-4 | Whole sessions across entitlement and gaps | SESS-7, SESS-8 |

### EP-VEN — Venue index and venue identity

§7 · accountable seat: cto · 5 features, 23 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-VEN-1 | Bundled offline venue index | VEN-1, VEN-2, VEN-3, VEN-4, VEN-5, VEN-6, VEN-23 |
| FT-VEN-2 | Venue identity survives every refresh (schema rules) | VEN-7, VEN-8, VEN-10, VEN-11, VEN-12 |
| FT-VEN-3 | Refresh proposals and quarterly cadence | VEN-9, VEN-13, VEN-19 |
| FT-VEN-4 | Repair layer: merge, rename, reattach, undo | VEN-14, VEN-15, VEN-16, VEN-21 |
| FT-VEN-5 | Venue-identity regression fixture and release bar | VEN-17, VEN-18, VEN-20, VEN-24 |

### EP-VPAGE — The venue page

§8 · accountable seat: pm-ba · 3 features, 11 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-VPAGE-1 | Venue page: every visit, rating, note and verdict | VPAGE-1, VPAGE-2, VPAGE-5, VPAGE-7, VPAGE-9 |
| FT-VPAGE-2 | Honest, entitlement-blind aggregates at scale | VPAGE-3, VPAGE-4, VPAGE-8 |
| FT-VPAGE-3 | Ratings: true mean, trend and weighted order | VPAGE-6, VPAGE-10, VPAGE-11 |

### EP-LOOK — Journal-wide views

§8.1 · accountable seat: pm-ba · 5 features, 9 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-LOOK-1 | What Haunts has worked out about you | LOOK-1 |
| FT-LOOK-2 | Most-visited list and offline heatmap | LOOK-2 |
| FT-LOOK-3 | Recap and self-portrait | LOOK-3, LOOK-8 |
| FT-LOOK-4 | Save recap as image; no sharing prompts anywhere | LOOK-4, LOOK-5, LOOK-6, LOOK-7 |
| FT-LOOK-5 | Offline search including notes | LOOK-9 |

### EP-HEAD — Home-screen headlines

§8.2 · accountable seat: ux-lead · 4 features, 18 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-HEAD-1 | Headline slot, appearances and options | HEAD-1, HEAD-2, HEAD-3, HEAD-5, HEAD-15 |
| FT-HEAD-2 | Headline content rules and small-numbers honesty | HEAD-4, HEAD-6, HEAD-7, HEAD-8, HEAD-14 |
| FT-HEAD-3 | Ticker motion and screen-reader behaviour | HEAD-9, HEAD-10, HEAD-11, HEAD-16 |
| FT-HEAD-4 | Headline privacy: surfaces and sensitive places | HEAD-12, HEAD-13, HEAD-17, HEAD-18 |

### EP-ENT — Entitlement, trial, lapse and first run

§9, §9.1 · accountable seat: cto · 6 features, 17 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-ENT-1 | Entitlement as intervals, unknown stated honestly | ENT-1, ENT-2 |
| FT-ENT-2 | Trial and lapse: nothing hidden, nothing lost | ENT-3, ENT-4, ENT-5, ENT-9, ENT-10 |
| FT-ENT-3 | Location use stops at expiry, and says so | ENT-6, ENT-7, ENT-8 |
| FT-ENT-4 | Store lifecycle: cancel, restore, no covert identifier | ENT-11, ENT-12, ENT-13 |
| FT-ENT-5 | Entitlement-boundary QA fixtures | ENT-14 |
| FT-ENT-6 | First run and onboarding | ONB-1, ONB-2, ONB-3 |

### EP-PRICE — Pricing presentation and consumer notices

§10, §11 · accountable seat: cfo · 4 features, 20 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-PRICE-1 | Plans screen with honest per-unit prices | PRICE-1, PRICE-2, PRICE-3, PRICE-4, PRICE-5, PRICE-6 |
| FT-PRICE-2 | Point-of-sale disclosures | PRICE-7, PRICE-8, PRICE-9, PRICE-10, PRICE-13, PRICE-14 |
| FT-PRICE-3 | Published price commitments | PRICE-11, PRICE-12 |
| FT-PRICE-4 | In-app notices surface and cancellation | NOT-1, NOT-2, NOT-3, NOT-4, NOT-5, NOT-6 |

### EP-DATA — Store, export, import and backup

§12 · accountable seat: cto · 5 features, 15 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-DATA-1 | One SQLite store as a written contract | DATA-1, DATA-2 |
| FT-DATA-2 | Lossless export and own-archive import | DATA-3, DATA-4, DATA-5 |
| FT-DATA-3 | Opt-in encrypted backup | DATA-6, DATA-7, DATA-8, DATA-9, DATA-10, DATA-11, DATA-12 |
| FT-DATA-4 | Diagnostics that cannot hold journal content | DATA-13, DATA-14 |
| FT-DATA-5 | Import from a competitor's export | DATA-15 |

### EP-PHOTO — Photos by reference

§12.2 · accountable seat: cto · 3 features, 11 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-PHOTO-1 | Attach photos by reference with a kept thumbnail | PHOTO-1, PHOTO-2, PHOTO-5, PHOTO-10, PHOTO-11 |
| FT-PHOTO-2 | Missing-photo state as a designed normal state | PHOTO-7, PHOTO-8 |
| FT-PHOTO-3 | Photos in export, backup and import | PHOTO-3, PHOTO-4, PHOTO-6, PHOTO-9 |

### EP-LIC — Licences and attribution

§13 · accountable seat: cgo · 2 features, 6 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-LIC-1 | Data sources and licences screen | LIC-1, LIC-3, LIC-4, LIC-6 |
| FT-LIC-2 | Licence texts travel with redistributed data | LIC-2, LIC-5 |

### EP-PRIV — Privacy and honesty surfaces

§14 · accountable seat: cgo · 3 features, 8 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-PRIV-1 | Transmission claim, enforced and shown live | PRIV-1, PRIV-2, PRIV-8 |
| FT-PRIV-2 | Privacy declarations and public statements | PRIV-3, PRIV-4, PRIV-5 |
| FT-PRIV-3 | Quiet by default: review prompt and spoken labels | PRIV-6, PRIV-7 |

### EP-A11Y — Accessibility

§15 · accountable seat: ux-lead · 4 features, 10 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-A11Y-1 | No map-only or colour-only information | A11Y-1, A11Y-2, A11Y-3 |
| FT-A11Y-2 | Screen-reader labels and announcements | A11Y-6, A11Y-7, A11Y-8 |
| FT-A11Y-3 | Text size, touch targets and motion | A11Y-4, A11Y-5, A11Y-9 |
| FT-A11Y-4 | Per-release accessibility gate | A11Y-10 |

### EP-PLAT — Platform, storefront and release

§16 · accountable seat: cto · 3 features, 8 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-PLAT-1 | React Native app shell on iOS 26+ and Android | PLAT-1, PLAT-8 |
| FT-PLAT-2 | Store release readiness and schedule | PLAT-3, PLAT-4, PLAT-5 |
| FT-PLAT-3 | Name, icon and support statement before launch | PLAT-2, PLAT-6, PLAT-7 |

### EP-PLAN — Build planning and spikes

§22 · accountable seat: cto · 4 features, 14 tasks

| Feature | Title | Tasks |
|---|---|---|
| FT-PLAN-1 | Block lifts owed before build | SPK-01, SPK-02 |
| FT-PLAN-2 | Platform and device questions | SPK-03, SPK-05, SPK-07, SPK-10, SPK-14 |
| FT-PLAN-3 | Architecture and security choices | SPK-04, SPK-06, SPK-11, SPK-12, SPK-13 |
| FT-PLAN-4 | Sizing and costing of scope outside the estimate | SPK-08, SPK-09 |

---

## 4. Coverage check

Run by `backlog-build.py` on 2026-09-26 against `requirements.md` as it stands on branch `haunt/requirements` at commit `13ce2d1`. The script parses every table row whose first cell is a bold requirement ID and whose table has the five-column requirement shape.

| Check | Result |
|---|---|
| Requirement IDs in `requirements.md` | **197** |
| Requirement tasks in `backlog.csv` | **197**, all unique |
| IDs in `requirements.md` with no task | **none** |
| Tasks naming an ID not in `requirements.md` | **none** |
| IDs appearing as a task more than once | **none** |
| Duplicate keys in the CSV | **none** |
| Titles over 70 characters | **none** |

**Things that look like requirement IDs and are deliberately not tasks**, with the reason:

| Token | What it is | Why no task |
|---|---|---|
| **S-1, S-2, S-3** (§7.7.5) | The CTO's standing conditions that re-engage Block 4 | Triggers, not requirements; the cost-sheet CFO excluded them on the same ground (`cost-sheet-v3.md` §4.6). Their measurements **are** tasks: S-1 → **VEN-24**, S-2 → **CONF-9**, S-3 → the scope rule on **VEN-14/15/21** and **VPAGE-5**. The label `standing-condition` marks those tickets (§6) |
| **DEF-1 … DEF-7** (§3) | Definitions | Definitions bind every task; they are not buildable on their own. DEF-2's surfaces are tested through each surface's own requirement |
| **AC-1 … AC-6** | The Engineer's original drafting of the venue schema criteria | Adopted as **VEN-7 … VEN-12**; a task each would duplicate them |
| **R-1 … R-8** | The CTO's Block 4 ruling items | Mapped to requirement IDs at §7.7.7; **SPK-01** is the CTO's confirmation against that map |
| **P-FSA-1, P-FSA-2** (§19.1) | Preconditions for FSA ratings, which are deferred | Not v1 scope |
| **CAP-11 … CAP-14**, **ENT-15 … ENT-17**, **CONF-20** | Reserved ranges | Not yet written. The spikes that will write them are on the board: **SPK-02** (CAP-11…14), **SPK-10** (ENT-15…17). CONF-20 is post-MVP (§19.2) |

**Count drift, recorded.** `cost-sheet-v3.md` §4.6 counted **163** requirements on 2026-09-22 and said *"163 is a snapshot, and the PM/BA owns the real count."* The real count today is **197**. The difference is D19–D26 (VPAGE-10, VPAGE-11, LOOK-5 … LOOK-9, PHOTO-8 … PHOTO-11, HEAD-1 … HEAD-18, MEM-1, DFLT-1, LIC-6, PLAT-7, PLAT-8 and others). This is a fact for the CFO at SPK-09, not a finding against anyone.

---

## 5. The "Build planning and spikes" epic

Each is a task with an owner, a priority inherited from the most severe requirement it unblocks, and an exit that is a written artifact. **A spike is Done when its artifact is committed and the owning seat has written its answer into the place the answer belongs** — usually a line in `requirements.md` §22 (which only this seat edits) or a CTO note. QA does not verify spikes; the seat that consumes the answer confirms it.

| Key | What | Owner | Unblocks | Source |
|---|---|---|---|---|
| **SPK-01** | CTO confirms in writing that Block 4 limb (b) lifts against §7.7.7 | CTO | Every venue-identity task (EP-VEN, FT-CONF-2, FT-CONF-3). **Build commencement on venue work** | STATUS.md "Still owed at build planning"; `requirements.md` §0, §7.7.7 |
| **SPK-02** | Android device-matrix spike — CTO Block 2's lifting condition; writes CAP-11 … CAP-14 | CTO (Engineer runs it) | CAP-3, CAP-4, CAP-10; the Android build. **The larger live build risk** (STATUS.md) | `requirements.md` §4 note under CAP-10, §7.7.7 closing paragraph |
| **SPK-03** | Set Haunts' minimum Android version | CTO | HEAD-12(c), LOOK-2(e) on older devices; bounds SPK-02's matrix | §22 item 20 |
| **SPK-04** | Heatmap render test on a mid-range Android phone and an iPhone — **frame-time bar set before the test runs** | CTO | LOOK-2(l). If it fails, *"the heatmap waits and the ranked list ships regardless"* (D13) | §22 item 24 |
| **SPK-05** | Does `AccessibilityInfo.isReduceMotionEnabled()` read Android's *Remove animations*? Tested through the accessibility menu, never Developer options | Engineer; QA verifies | HEAD-10(b) (BLOCKING), A11Y-9 | §22 item 21 |
| **SPK-06** | Choose the KDF, its parameters and its dependency — *"Not to be picked by whoever is nearest the keyboard"* | CSO | DATA-6, DATA-7, DATA-8; the whole of FT-DATA-3 | §22 item 7 |
| **SPK-07** | Does a local notification require authorization, and what happens when it is declined? | Engineer, about one hour | NOT-3, NOT-5, CAP-8, CAP-9. **Twice-flagged**: the evidence standard requires it be *"resolved, or formally accepted in writing by the CEO, before it may anchor a third artifact"*. Resolving it costs an hour, so resolve it | §22 item 4; `pipeline/evidence-standard.md` "Twice-flagged is escalated" |
| **SPK-08** | Size the scope outside the 2,090 h estimate: HEAD-1 … HEAD-18, PHOTO-1 … PHOTO-11, LOOK-8, LOOK-9, the heatmap (LOOK-2), plus the items in §8's "Estimate basis" candidate list | CTO | SPK-09; ONB-3's PENDING-ESTIMATE decision; the honest phase plan | §22 items 22, 25; STATUS.md "Still open" |
| **SPK-09** | Re-cost once SPK-08 lands | CFO | The cost sheet's unsized sensitivity (`cost-sheet-v3.md` §4.5, §4.6) | STATUS.md: *"The CFO must re-cost once the CTO sizes them"* |
| **SPK-10** | Does the store permit a non-auto-charging trial alongside auto-renewable subscriptions? | CTO with CGO | ENT-10 (load-bearing or precautionary); writes ENT-15 … ENT-17 | §22 item 2; §9 reserved range |
| **SPK-11** | Photos C-1: a durable photo reference without full library authorization, on both platforms; plus the rest of §12.2.7's CTO list | CTO | All of EP-PHOTO. *"If it fails, §12.2.5 returns the design to the CEO"* | §22 item 15 |
| **SPK-12** | Backup architecture branch: the user-saved encrypted file as the only backup, or a cloud module as well | CTO | DATA-12's shape (§12.1 records both branches); FT-DATA-3 | §12.1; §24 reserved row |
| **SPK-13** | Name the competitor export formats DATA-15 imports, with retrieved format documentation | CTO | DATA-15; its untrusted-input review by the CSO | §22 item 17 |
| **SPK-14** | Does any API let an app relinquish its own location authorization? | Engineer, about one hour | ENT-8 — *"honest by construction rather than by instruction"* if yes | §22 item 5 |

**Not added as spikes, and why.** §22 item 1 (usability testing) needs the CEO's authorisation and a spend decision under Constitution 5.4 — it is recorded in §12, not put on a build board where it would sit un-actionable. §22 item 12 (closed venues are undetectable) has no requirement attached and no seat has been asked to do work on it; putting it on the board would create unowned work. §22 items 3, 13, 14, 16 and 18 are CGO or CEO rulings, not technical work. §22 item 11 (thirty shopfront names) waits on the CEO's authorisation.

---

## 6. Labels

GitHub labels are flat, so each carries a prefix. **Board fields (§8) are the primary structure; labels exist so the same facts are visible and filterable from the repository's issue list, where people also look.** The ticket script sets both from the CSV.

| Label | Values | Set from |
|---|---|---|
| `level:` | `epic`, `feature`, `task`, `spike`, `story` | CSV `level`; `spike` for `SPK-` keys. **`story`** is set by hand on implementation stories created by the CTO at wave planning from the `haunts` story template (D34; `agentic-agile-adoption.md` §3.2, Appendix B); the script never creates one |
| `prio:` | `blocking`, `must`, `cut-line`, `pending-estimate` | CSV `priority` |
| `platform:` | `ios`, `android`, `both`, `none` | CSV `platform` |
| `seat:` | `engineer`, `qa`, `cto`, `cso`, `cfo`, `cgo`, `ux-lead`, `pm-ba`, `ceo` | CSV `owner_seat` |
| `area:` | one per epic, e.g. `area:cap`, `area:ven` | the epic key |
| `promise-line` | — | the seven items of `requirements.md` §20.1: DATA-4, VEN-7 … VEN-12, CONF-3, SESS-1, PRIV-1, PRIV-8, CAP-4, VEN-21. **Cutting one is not a scope change; it is an overrule or an amendment** (§1 of the requirements) |
| `standing-condition` | — | VEN-24 (S-1), CONF-9 (S-2), VEN-14, VEN-15, VEN-21, VPAGE-5 (S-3). A change to any of these re-engages Block 4 |
| `mixed-priority` | — | HEAD-4, HEAD-5, HEAD-9, HEAD-13, HEAD-14, HEAD-15, PHOTO-9 (§11.1) |
| `needs:cso-review` | — | security-relevant tasks: DATA-6 … DATA-13, DATA-15, ENT-11, PRIV-8, PHOTO-11, CAP-1, SPK-06. **Proposed by this seat [J]; the CSO should confirm or widen the list** |
| `blocked` | — | set by hand, with the blocking key in the ticket's "Blocked by" field |
| `spec-defect` | — | set by an Engineer or QA when a criterion is wrong, untestable or contradicts another (standup routine §7); removed by the PM/BA when `requirements.md` is fixed. Counted per phase as a delivery measure (`agentic-agile-adoption.md` §7.2) |
| `escaped` | — | on a **new** issue raised for a defect in behaviour that a **Done** ticket covers. The body links the Done ticket and names who found it (QA, CTO/CSO, CEO at a demo, or a user after release). Counted per phase, CEO-found separately (§7.2) |
| `needs:ceo` | — | a ticket that cannot move until the CEO decides something. Today: **PLAT-5** (EU storefront, §22 item 9), **PLAT-7** (icon brief, §22 item 19) |

---

## 7. The board

**One GitHub Project, owned by `deopea-david`, linked to the `haunts` repository.** Columns are values of the built-in Status field.

| Column | Entry rule | Who moves a ticket in |
|---|---|---|
| **Backlog** | Every ticket starts here | Ticket script |
| **Ready** | Requirement ID linked; the spikes it depends on are Done; nothing in §11 blocks it; owner seat and platform set; **Files to create or modify, Interfaces to implement and File ownership set by the CTO (no longer TBD) and the `Wave` field set** (D33, D34); for a wave, every limb of every requirement in it is claimed by the ticket or one of its stories (the PM/BA's limb-coverage check, `agentic-agile-adoption.md` §3.2) | PM/BA |
| **In progress** | Someone is working on it; a branch exists | The owning seat |
| **In review** *(proposed as "Review (CTO/CSO)"; named "In review" as built)* | PR open, referencing the ticket with `Refs #n`, its body following the `haunts` PR template; tests for every acceptance-criterion limb exist. CSO reviews tickets labelled `needs:cso-review` as well | The owning seat |
| **QA** | CTO (and CSO where labelled) wrote the review record in the PR **at its head commit**, and the PR was merged at that head to `main` of `haunts`. Where the ticket has implementation stories, **all** of them are merged | The reviewing seat |
| **Done (QA-verified)** | **QA has verified every acceptance-criterion limb in `requirements.md` for this ID, on a named build, and recorded the `requirements.md` commit SHA it verified against and the evidence link** | **QA only** |

**Done means QA-verified against the acceptance criteria, not merged.** Two GitHub defaults work against this and must be changed when the board is created:

1. **New projects set Status to Done automatically when an issue is closed and when a pull request is merged** — GitHub's documentation: *"When issues or pull requests in your project are closed, their status is set to Done"* [E, retrieved 2026-09-26, §13 item 3]. **Both default workflows are switched off.**
2. **A PR whose description says `closes`, `fixes` or `resolves #n` closes that issue when merged into the default branch** [E, §13 item 4]. **PRs reference tickets with `Refs #n` only.** QA closes the issue when it moves it to Done.

**Implementation stories (D34).** Where the CTO splits a requirement, or one change serves several requirements, the work is an implementation story (`level:story`), a sub-issue of the requirement it mainly serves. **A story is closed by its reviewer when its PR is merged, with a comment naming the merge commit, and its Status is never set to Done.** D34 settles that D30's *"only QA moves a ticket to Done"* covers requirement tickets, which are QA's unit. Stories appear in the "Current wave" view, not in the Board view (§8).

**QA fails a ticket back, it does not reopen a new one.** Each time QA starts a verification it increments the ticket's `QA attempts` field (§8). A failure moves the ticket to **In progress** with a comment naming the limb that failed, e.g. *"CAP-4(a) fails: service-kill gap not recorded, build 0.3.1 (a1b2c3d)"*. The failed limb is named by its letter from `requirements.md`; the criterion text is not copied (D27).

**Features and epics.** A feature is Done when all its tasks are Done **and** it has been demonstrated end to end on both platforms it targets. An epic is Done when all its features are Done. **Neither is "done" in the Constitution's sense until it has been through a phase review** — Constitution 5.5: *"Every pipeline phase concludes with a review pack and demo presented to the CEO… Work is not 'done' until it has been reviewed."* The column is therefore labelled **"Done (QA-verified)"**, not "Done", so the board never claims more than it knows. A milestone closes only after the CGO's review pack and demo for that phase reach the CEO.

*Board as built, 2026-09-26 (CEO):* the column keeps the name **Done**, and its description reads *"QA-verified against the acceptance criteria"*. A **QA** column sits between In review and Done. The rule above is unchanged: only QA moves a ticket to Done. The built-in "Item closed" and "Pull request merged" workflows are off.

**Cut-line and scope changes.** A CUT-LINE task that the CEO cuts is closed as *not planned* with a link to its `requirements.md` §24 scope-change row. **A cut with no §24 row is not a cut** — this seat's charter blocks *"scope changes mid-build without a written trade-off"*. A BLOCKING task is never closed as not planned without the CEO's written overrule or an amendment.

---

## 8. Custom fields and views

GitHub Projects supports text, number, date, single-select and iteration fields, up to 50 in total, and table, board and roadmap layouts with filtering, sorting and grouping [E, §13 item 1]. Sub-issues give the epic → feature → task hierarchy, *"up to 100 sub-issues per parent issue and… up to eight levels"* [E, §13 item 2]; the largest parent here has seven children.

### Fields

| Field | Type | Values / notes |
|---|---|---|
| Status | built-in single select | the six columns in §7 |
| Level | single select | epic, feature, task, spike |
| Key | text | CSV `key` |
| Requirement ID | text | CSV `requirement_id` |
| Section | text | CSV `section` |
| Priority | single select | BLOCKING, MUST, CUT-LINE, PENDING-ESTIMATE |
| Platform | single select | ios, android, both, none |
| Owner seat | single select | the nine seats in §6 |
| ~~Phase~~ | — | **Removed by D36 (CEO, 2026-09-26): phases are GitHub milestones M0–M5 in `haunts`.** Views below that group or sort by Phase use the milestone instead |
| Estimate basis | single select | *In 2,090 h* · *Added after the estimate — unsized* · *Pending estimate* · *n/a*. **Filled by the CTO at SPK-08**, not by this seat |
| CTO hours | number | the CTO's estimate, when there is one |
| Blocked by | text | key(s) of the blocking ticket or decision |
| Verified against | text | QA's record at Done: `requirements.md@<sha>` plus the evidence link |
| **Wave** | text | `M<phase>.W<n>`, e.g. `M1.W2`. **Set by the CTO at wave planning** on whichever issue owns files (the requirement ticket or its stories); empty from the ticket script. A field, not a label, because wave values change as work is planned (D34; `agentic-agile-adoption.md` §4.2) |
| **QA attempts** | number | 0 from the ticket script; **QA adds one each time it starts verifying the ticket**. The QA first-pass rate is the share of Done tickets with `QA attempts = 1` (`agentic-agile-adoption.md` §7.2) |

**Candidates for "Added after the estimate", offered to the CTO for SPK-08 and not asserted [I].** From `requirements.md` §22 items 22 and 25 and `cost-sheet-v3.md` §4.2 and §4.6: HEAD-1 … HEAD-18; PHOTO-1 … PHOTO-11; LOOK-1 … LOOK-9; CONF-19; DATA-15; ONB-1 … ONB-3; PRICE-13, PRICE-14; PLAT-6; VEN-13, VEN-16; VPAGE-6, VPAGE-7; NOT-6. Added after the CFO's last count and so presumably also unsized: VPAGE-10, VPAGE-11, MEM-1, DFLT-1, LIC-6, PLAT-7, PLAT-8. **VEN-17 is unclear** — the CFO asked the CTO whether it sits inside the venue-remediation row (§4.2) and records no answer. The CTO decides every one of these; I have not sized anything.

### Views

| View | Layout | Filter / grouping | Who uses it |
|---|---|---|---|
| **Board** | board | Level = task or spike; columns by Status | everyone |
| **Epics** | table | Level = epic or feature; grouped by parent; sub-issue progress shown | CEO, PM/BA |
| **Blocking path** | table | Priority = BLOCKING, Status ≠ Done; sorted by Phase then Key | PM/BA, CTO |
| **By seat** | table | grouped by Owner seat; Status ≠ Done | each seat, at standup |
| **Review queue** | table | Status = In review | CTO, CSO |
| **QA queue** | table | Status = QA | QA |
| **Blocked** | table | label `blocked` or `needs:ceo` | PM/BA, orchestrator |
| **Planning and spikes** | table | Level = spike | CTO |
| **Phases** | table | grouped by Phase | CTO, CGO at phase review |
| **Current wave** | board | `Wave` = the wave in flight, all levels including `story`; columns by Status | CTO at the wave gate, Engineers |

A roadmap (timeline) view is possible but needs a date or iteration field; **I do not propose dates**, because the build calendar is the CTO's (PLAT-4 requires calendar to be modelled separately from effort) and a date set by this seat would be a guess wearing a plan's clothes.

---

## 9. What a ticket contains

> **Superseded in part by D31 (CEO, 2026-09-26):** tickets now carry the requirement, its acceptance criteria (lettered limbs as a checklist) and its source in full, stamped with the `requirements.md` commit they were copied from and generated by `backlog-tickets.py`. The document still wins where they differ, and QA still verifies against the document. The text below is the PM/BA's original proposal, kept for the record.
>
> **Superseded further by D33 and D34 (CEO, 2026-09-26):** the ticket body now follows `agentic-agile-adoption.md` §3.3. A **generated region** (summary, origin and context, requirement, acceptance criteria, invariants to preserve, negative constraints, dependencies, verification, stamp) is replaced whole on regeneration. A **CTO-maintained region** (files to create or modify, interfaces to implement, file ownership and wave) reads **TBD** until the CTO sets it at wave planning, and regeneration never touches it. `backlog-tickets.py` implements both, with `regenerate_body()` and a `--self-test`.

Generated from one CSV row. **No acceptance criterion is ever copied into a ticket.**

```
Title:   [CAP-3] Android capture via a declared location foreground service
Labels:  level:task  prio:blocking  platform:android  seat:engineer  area:cap
Parent:  FT-CAP-3 (sub-issue)

Requirement: CAP-3
Acceptance criteria: products/haunt/requirements.md, section 4, row CAP-3
  -> https://github.com/deopea-david/candour/blob/main/products/haunt/requirements.md
     (the script builds the link and the section anchor; this plan hard-codes no URL)
Verify against the file, never against this ticket.
```

**Links point at `main`, and QA records the SHA.** A link to `main` always shows the live criteria, which is D27's intent — the ticket cannot drift because it holds nothing to drift. The cost is that the criteria can change under an open ticket. That is answered by two rules: **(1)** any change to a requirement's criteria after its ticket leaves Backlog is a §24 scope-change row, which this seat already blocks without; **(2)** QA records the `requirements.md` commit SHA it verified against at Done, so an auditor can see exactly which text was met. **Precondition:** the `haunt/requirements` branch is merged to `main` of `candour` first (STATUS.md, "Before anything is created", step 1). Until then every link would 404.

---

## 10. Phase order — a proposal for the CTO to confirm

**This is a proposal, not a plan.** Build sequencing is the CTO's (the CTO holds the build-commencement block, Constitution 5.6). It is offered so the CTO has something concrete to correct rather than a blank. **Late in the order does not mean optional:** a MUST in M4 is exactly as required as a MUST in M1, and moving anything out of v1 is a §24 scope change. Each milestone closes with the CGO's review pack and demo to the CEO (Constitution 5.5). **Within a phase, the CTO runs the work as waves (D34):** batches with no shared files and no dependencies between them, each closed by a wave gate that writes one row to `docs/delivery-log.md` in `haunts`. A wave gate makes nothing "done"; the phase review does (`agentic-agile-adoption.md` §4.5).

| Phase | What | Features | Why here [J, PM/BA] |
|---|---|---|---|
| **M0 — Planning** | Block lifts, spikes, sizing | FT-PLAN-1 … 4 | SPK-01 and SPK-02 gate build commencement on venue and Android work; SPK-06, SPK-11, SPK-12 gate whole features |
| **M1 — Foundations that cannot be retrofitted** | The store contract, the schema rules, derived sessions, entitlement intervals, the JS-free capture path, and every **build-time enforcement check** | FT-DATA-1, FT-PLAT-1, FT-CAP-1, FT-ENT-1, FT-SESS-1, FT-VEN-1, FT-VEN-2, VEN-17 from FT-VEN-5; **plus the CI checks** in MEM-1(a), DFLT-1(a), PRIV-8, DATA-13, VPAGE-4, CAP-8(c), CONF-19(a) | `requirements.md` §20.1 calls the schema rules *"free now and unavailable later"* and says SESS-1 *"costs nothing now"*. A CI check written before the code it guards is cheap; one written after has to be argued past existing violations |
| **M2 — The core loop** | Capture → confirm → session → venue page → repair → export and re-import | FT-CAP-2 … 5, FT-CONF-1 … 4, FT-SESS-2 … 4, FT-VEN-3, FT-VEN-4, FT-VPAGE-1 … 3, FT-DATA-2, **ENT-4** (manual composer), FT-A11Y-1 … 3 built alongside | The loop is the product. ENT-4 comes forward because CAP-6 (usable with location denied) is untestable without it. DATA-4 is on the promise line and one serialiser serves export, restore and migration (DATA-5). Accessibility limbs are acceptance criteria of the screens they sit on, so they are built with them, not after |
| **M3 — Money, lapse and first run** | Trial, lapse, entitlement boundary, pricing, notices, onboarding | FT-ENT-2 … 6, FT-PRICE-1 … 4 | Depends on SPK-07 and SPK-10. PRICE-7/8/9 also wait on §11.2 |
| **M4 — Journal features added after the estimate, and backup** | Journal views, headlines, photos, encrypted backup, competitor import | FT-LOOK-1 … 5, FT-HEAD-1 … 4, FT-PHOTO-1 … 3, FT-DATA-3, FT-DATA-5 | Most of this is unsized (SPK-08). Backup waits on SPK-06 and SPK-12; photos on SPK-11; the heatmap on SPK-04; DATA-15 on SPK-13 |
| **M5 — Release readiness** | Field measurement, release bars, licences, privacy declarations, store readiness | FT-CAP-6, the rest of FT-VEN-5 (VEN-18, VEN-20, VEN-24), FT-A11Y-4, FT-LIC-1 … 2, FT-PRIV-2 … 3, FT-DATA-4 (DATA-14), FT-PLAT-2 … 3 | CAP-10 and VEN-24 share one real-week field run (VEN-24's source says so) and need a near-final build. PLAT-3's 14-day closed test and PLAT-7's icon are calendar time, so **they start earlier than M5** even though they finish there — PLAT-4 exists to stop waiting time being planned as effort |

**Dependencies the ticket script should record as "Blocked by"** (from the requirements' own cross-references): VEN-24 ← CAP-10 ← SPK-02; HEAD-10 ← SPK-05; NOT-3, NOT-5 ← SPK-07; ENT-10 ← SPK-10; ENT-8 ← SPK-14; DATA-6, DATA-7, DATA-8 ← SPK-06; DATA-12 ← SPK-12; PHOTO-1 … PHOTO-11 ← SPK-11; LOOK-2 ← SPK-04; DATA-15 ← SPK-13; ONB-3 ← SPK-08; every EP-VEN task and FT-CONF-2/FT-CONF-3 ← SPK-01; LOOK-5 ← PLAT-7.

---

## 11. Gaps and contradictions found while mapping

Listed, not fixed. **I have not edited `requirements.md`**, as instructed. Each item says who closes it and whether it stops a ticket reaching Ready.

**11.1 Seven requirements carry priorities per limb, and a ticket can hold only one.** HEAD-4 (*"BLOCKING for (b)–(c), MUST for (a) and (d)"*), HEAD-5, HEAD-9, HEAD-13, HEAD-14, HEAD-15, and PHOTO-9 (*"MUST for the no-copy, no-fail, plain-statement limbs; CUT-LINE for the relink option"*). The CSV takes the highest limb, and the `mixed-priority` label tells QA to read limb priorities from the file. **No change requested**; recorded so nobody reads HEAD-4's BLOCKING as covering limb (a). *Stops Ready: no.*

**11.2 PRICE-7, PRICE-8 and PRICE-9 still carry placeholders.** `requirements.md` §10.1 holds *"£[M]"*, *"£[P]"*, *"[T]"* and *"[C]%"*, and §22 item 8 still lists the CFO's three-year restatement as open — yet `cost-sheet-v3.md` exists and STATUS.md records the CFO block *"lifted in full"*. The figures probably exist now; they have not been carried into the requirements [I]. **Owner: this seat, with the CFO confirming the numbers.** *Stops Ready: yes, for PRICE-7, PRICE-8, PRICE-9.*

**11.3 `requirements.md` §0 and its header are stale, and sign-off is undefined.** The header reads *"Version 1.1 (draft for sign-off)"* and cites D1–D26. §0 still lists the CFO standing block as *"Live, narrowed"*, which STATUS.md contradicts, and its Condition 1 row cites `cost-sheet-v2.md`, superseded by v3. §0 also says *"sign-off of this document is the event that puts [the Block 4 lift] to that seat"*, but no document says who signs it off or how that is recorded. **Owner: this seat, to refresh §0; the CEO to say whether sign-off is his act or the CTO's SPK-01 confirmation is enough.** *Stops Ready: no — but tickets linking to a document headed "draft" is worth fixing before they exist.*

**11.4 HEAD-4 and HEAD-14 depend on criteria held outside `requirements.md`.** HEAD-4 requires headlines *"only from the enumerated template catalogue (T1–T9)"*, and HEAD-14 makes each template eligible *"only at its `ux-home-headlines.md` §5.2 threshold"*. Both sets of values live in a UX note, not in the requirements. D27 makes `requirements.md` *"the single source of every requirement and acceptance criterion"*. **Proposal:** the next revision of `requirements.md` names `ux-home-headlines.md` §3 and §5.2 as a normative annex, or lifts the catalogue and thresholds in. **Owner: this seat with UX.** *Stops Ready: no; QA reads both files meanwhile.*

**11.5 The Ticker is on the cut line while two of its requirements are BLOCKING.** §20.2 lists *"The headline Ticker (HEAD-2, HEAD-9 … HEAD-11) — recorded, not recommended"*; HEAD-9(a) and HEAD-10 are BLOCKING. This is not a contradiction in substance: BLOCKING applies **if** the Ticker ships. But the board will show BLOCKING tickets for something cuttable. **If the Ticker is cut**, one §24 row retires HEAD-9 and HEAD-11 and the Ticker limbs of HEAD-2 and HEAD-10. *Stops Ready: no.*

**11.6 Three cut-line entries have no requirement to cut.** §20.2 lists **`haunt.gpx` in the export**, but DATA-3's archive contents (*"`haunt-export.json`… `visits.csv` and `venues.csv`… and `README.txt`"*) include no GPX file, so there is nothing to cut. It lists **Android Auto Backup as a zero-config fallback**, which no requirement specifies. And **"the map entirely"** spans LOOK-2's heatmap limbs, A11Y-3 and part of A11Y-9 rather than any one ID. **Proposal:** the next revision gives each an ID or strikes it. **No ticket is created for any of them.** *Stops Ready: no.*

**11.7 PRIV-3 covers Apple's privacy label and nothing covers Google Play's.** PRIV-3: *"Crash data is declared on the App Privacy label"*. Android ships at launch (D1). Google Play has its own data declaration for apps, the Data safety section [K, high confidence, not retrieved this session]. No requirement asks for it. The CSV marks PRIV-3 `ios`, as written. **Owner: CGO to confirm the Android duty; this seat to add the requirement.** *Stops Ready: no, but it is a release gap on Android.*

**11.8 A cross-reference in §7.7.6 points at the wrong open item.** §7.7.6 item 5 says UX must confirm VEN-22 and the repair path, and QA must confirm S-2's fixture and VEN-20(a), and that *"Until both confirm… §22 item 14 carries it."* §22 item 14 is the CGO's household-exemption question. **Nothing in §22 tracks the UX and QA confirmations.** **Owner: this seat, to add the §22 row; UX and QA to confirm.** *Stops Ready: yes, for VEN-20 and VEN-22, until they confirm.*

**11.9 S-1 has no threshold.** §7.7.5: *"'Materially worse' is undefined in the ruling"*, flagged to the CTO. VEN-24(b) forces the comparison into the release pack; it does not make S-1 fire. **Proposal: the CTO sets the number in the same written confirmation as SPK-01.** *Stops Ready: no; stops VEN-24 reaching Done.*

---

## 12. Deliberately not on the board

| Item | Why not | Where it lives |
|---|---|---|
| Usability testing (§22 item 1) — *"the highest-value missing fact in this pipeline"* | Needs the CEO's authorisation and money (Constitution 5.4). A build board is the wrong place for a decision | `requirements.md` §19.2, §22 item 1 |
| EU storefront (§22 item 9) and the icon brief (§22 item 19) | CEO decisions. Their consequences are tickets (PLAT-5, PLAT-7) labelled `needs:ceo` | `requirements.md` §16.1, §22 |
| Launch bars: qualified human legal review (Constitution 6.1) including the refund duty; CGO confirmation of the privacy wording as a contract term | Not build work; no build creates them. They bar launch, not build | STATUS.md "Blocks and gates"; `requirements.md` §0, §19.2 |
| Architecture decision records and the CSO threat model | Seat artifacts under `/build`'s CTO+CSO step, kept in `candour` under `products/haunt/`. **They are not requirements and do not get requirement tasks**; the spikes that feed them do | CLAUDE.md "Where things live" |
| Deferred and out-of-scope items (§18, §19): FSA ratings, contacts selection (CONF-20), readable `haunt.html` export | Not v1 | `requirements.md` §18, §19 |
| Implementation sub-tasks *(superseded by D34)* | ~~Engineers add them under a task when they start it, as instructed.~~ **Now implementation stories (§7, D34):** created by the CTO at wave planning, only where a requirement is split or one change serves several; they name limbs by letter and never carry a requirement ID of their own | `haunts` story template (`agentic-agile-adoption.md` Appendix B) |

---

## 13. Evidence register

**External, retrieved this session (2026-09-26):**

1. GitHub Projects capabilities — layouts (*"a high-density table layout, as a kanban board, or a timeline-style roadmap"*), field types (date, number, single select, text, iteration; up to 50 fields), filtering, sorting, grouping, built-in workflows. [E] https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects · single-select detail: https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields — **single source (GitHub's own documentation), which is the authoritative source for this fact.**
2. Sub-issues — *"up to 100 sub-issues per parent issue and… up to eight levels of nested sub-issues"*. [E] https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
3. Default project workflows set Status to Done on close and on merge. [E] https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations
4. Closing keywords (`close`, `fix`, `resolve` and variants) close the linked issue when the PR merges into the default branch. [E] https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue

All four were read through a summarising fetch tool, not in the raw page; the quoted phrases are as that tool returned them. **Re-check them when the board is built**, since GitHub changes this product often [J].

**Model knowledge, not retrieved:** Google Play's Data safety section (§11.7) [K, high confidence].

**Candour files, read from disk 2026-09-26:** `constitution.md` v1.3; `roles/pm-ba.md`, `roles/qa.md`, `roles/engineer.md`; `pipeline/evidence-standard.md` v1.1; `pipeline/templates/requirements.md` (no template exists for a backlog plan, so none is used — stated rather than skipped); `products/haunt/STATUS.md`; `decisions/2026-09-16-haunt-gate.md` (D27); `products/haunt/requirements.md` v1.1 in full by structural parse and in the sections cited; `products/haunt/cost-sheet-v3.md` §4.2–§4.6.

---

## 14. Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-26 | 0.1 | First proposal: 17 epics, 67 features, 211 tasks (197 requirement + 14 planning); coverage 197/197; board, fields, views, labels; phase proposal for the CTO; nine gaps at §11 |
| 2026-09-26 | 0.2 | Ticket format per **D33** and **D34** (`agentic-agile-adoption.md` §3.3, §11): §6 labels gain `level:story`, `spec-defect`, `escaped`; §7 Ready rule requires the CTO-set files, interfaces, file ownership and wave; review recorded at the PR's head commit; implementation stories close on merge and never reach Done; column names as built ("In review"); §8 fields gain `Wave` and `QA attempts`, views gain "Current wave"; §9 and §12 superseded notes; §10 waves within phases. `backlog-tickets.py` regenerated to the §3.3 body. No mapping change: still 17 epics, 67 features, 211 tasks |
