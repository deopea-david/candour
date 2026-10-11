# CAP-15, CAP-16 and CAP-17: sizing and wave placement

**Seat:** Chief Technology Officer · **Date:** 2026-10-10 (committed 2026-10-11) · **Slug:** `haunt` · **Status:** sizing memo. **It prepares and flags; it does not certify** (Constitution 6.1). It decides nothing reserved to the CEO (5.4).
**Authority for the work:** D69's "Owed" line, *"the CTO sizes them"* (`decisions/2026-09-16-haunt-gate.md`), and the Coordinator's commission of 2026-10-10. Requirements are CAP-15, CAP-16 and CAP-17 in `requirements.md` v1.5 (on `main`), with §22 items 40 to 43. This answers §22 item 41.
**Template note:** `pipeline/templates/` has no sizing template; this follows the layout of `design-feasibility-and-sizing.md` §5 and says so.
**Unit and method:** the unit of `design-feasibility-and-sizing.md` (itself the unit of the 2,090-hour estimate): **focused solo hours, 7.5 h a day, 37.5 h a week**, including the item's own first verification and design coverage. **Every hour figure here is [J].** Low and high are plain sums of the line lows and highs, so a reader can re-derive them; they overstate the spread, as in `design-feasibility-and-sizing.md` §5.
**Model:** Sonnet, effort high, chosen by the Coordinator because these are small features inside an existing design (`pipeline/model-selection.md` §5.0).

Provenance: CTO · sonnet (Sonnet 5.5) · effort high · 2026-10-10

---

## 0. The answer on one page

| Requirement | Low | Point | High | What drives the range |
|---|---:|---:|---:|---|
| **CAP-15** the "Haunts missed this" entry | 20 | 29 | 39 | The overlap sentence (limb e) and how many surfaces the "appears everywhere" test (limb a) must cover |
| **CAP-16** the counts-only summary | 25 | 36 | 51 | Whether a file-share mechanism already exists from DATA-3, and the two device-level network checks (limb a) |
| **CAP-17** the in-app diary | 10.5 | 15 | 21 | The classification script that QA's computation needs (limb a); the app side is small |
| **Total** | **56** | **80** | **111** | |

- **+2.7% to +5.3% on the 2,090 h (+3.8% at the point).** It is **outside the 2,090 h**: scope added after the estimate, joining §22 items 22, 25 and 30. The composer (ENT-4), the export and import (DATA-3 to DATA-5) and the gap surface (CAP-4) are already in the 2,090 h; only the increments are counted here [J].
- **Ongoing: about 0.75 to 1.5 h per release** (the device-level network check for CAP-16 and the marker label in three themes), so **roughly 5 to 15 h a year** at 6 to 10 releases [J, the cadence is the one assumed in `design-feasibility-and-sizing.md` §6].
- **Placement: not M1.W8.** CAP-15 and CAP-16 build in **M2**. Their only M1 piece is **two columns in migration `0001`** (DATA-2.1, M1.W3), which is free now and costs a migration later (§2). CAP-17's last limb is the published result, so by my own rule that ticket sits at **M5** with SPK-02.
- **`block-2-review.md` §5, "the hours are about the same": it does not hold** (§3). The in-app tooling alone is about the size of the whole 75-hour line.

## 1. The sizing

Each line is Low / Point / High. Lines marked * are the ones the others lean on.

### 1.1 CAP-15, a visit Haunts missed

| # | Work | L | P | H |
|---|---|---:|---:|---:|
| 1 | **Schema.** Two plain columns on the `visit` table: the marker, and the creation time that CAP-17 needs. A `CHECK` that a row with a `source_candidate_id` cannot carry the marker (limb d, enforced in the database, not only in the screen). `visits.ts` and `docs/schema/journal-db.md`. **Folded into `0001`.** | 1.5 | 2 | 3 |
| 2 | **Composer control:** a labelled text control in ENT-4's composer, set and clear on edit, and the plain-sentence refusal for an adopted visit | 3 | 4.5 | 6 |
| 3 | **Overlap, said once (limb e):** query visits and waiting candidates (through `listCandidates`, never `capture.db`) that overlap the new range; one plain sentence; offer to open that one; never block the save | 4 | 6 | 8 |
| 4 | **The plain-words label** on the visit's own row and page, screen-reader text, large type, and a look in the three themes | 2 | 3 | 4 |
| 5 | **Export and import (limb c):** field in `haunt-export.json`, column in `visits.csv`, a sentence in `README.txt`, the DATA-4 full-store diff, the DATA-5 round trip. Small because the serialiser carries visit fields as data and the marker is a normal field | 3 | 4.5 | 6 |
| 6 | **Tests (limbs a, b, f, g, h):** the fixture; "appears everywhere, unqualified"; the open-with-`sqlite3` legibility check; the no-engagement enumeration of construction sites as CAP-8(c) does it; location-denied and expired-entitlement states; hide-the-control-and-nothing-is-removed | 6 | 9 | 12 |
| | **CAP-15** | **19.5** | **29** | **39** |

### 1.2 CAP-16, the counts-only summary

| # | Work | L | P | H |
|---|---|---:|---:|---:|
| 1 | **The counts:** a pure function in `core/domain` taking visits, gaps and a date range; "whole stay inside one gap row" as CAP-11 defines it; a partly covered miss counts as missed. Gaps come only through `listGaps`. The 7 / 3 / 1 fixture is the test (limb d) | 3 | 4.5 | 6 |
| 2 | **The file:** exactly six keys, a file name with no personal data, written to the cache directory and deleted after the share sheet (threat model C12) | 2 | 3 | 4 |
| 3 | **Settings row and preview screen:** the exact text shown on screen before sharing, a date range control, large type, accessibility, three themes | 5 | 7.5 | 10 |
| 4 | **Handing the file to the share sheet, and cancel.** If DATA-3's export has already put a file-share mechanism in the app, this is the low end. If not, it adds the dependency, and the CSO must approve it (§4) | 3 | 5 | 8 |
| 5 | **Limb (a) at device level:** network blocked, export completes; no outbound request on iOS (App Privacy Report or proxy) and Android (network capture); no new import, permission or manifest entry; PRIV-8's five layers pass with no allow-list change. These are device passes, not unit tests | 4 | 6 | 8 |
| 6 | **Tests (limbs b, c, e, f, g):** user-action-only, with no state written about whether the user exported; the 0/0/0, 12/3/2 and 40/0/0 previews and the banned-words list; the key set and the string search for every name, note, rating and coordinate; separate from the full export; airplane mode in every entitlement state. Wiring the strings into MEM-1(a)'s build-wide search | 8 | 10 | 15 |
| | **CAP-16** | **25** | **36** | **51** |

### 1.3 CAP-17, the in-app diary

| # | Work | L | P | H |
|---|---|---:|---:|---:|
| 1 | The creation-time column in schema (line 1.1-1 carries the migration; this is its spec and legibility test, limb b) | 0.5 | 0.75 | 1 |
| 2 | Composer sets the creation time once, in local time with offset; it is not editable and has no screen | 1 | 1.5 | 2 |
| 3 | Export: field in the JSON and CSV, a README sentence (limb b) | 1.5 | 2 | 3 |
| 4 | **The classification script** (limb a): reads `haunt-export.json`, applies CAP-11's rules, and returns recorded, covered, silent miss, partly covered, late, and excluded under 10 minutes. TypeScript, under `tools/`, with the four-entry fixture. **It is measurement tooling for SPK-02, not app code.** It reuses line 1.2-1's gap-containment function | 6 | 9 | 12 |
| 5 | The result template that names the diary kind per phone (limb c), and the copy check that nothing says adding a miss makes Haunts reliable (limb d) | 1.5 | 2 | 3 |
| | **CAP-17** | **10.5** | **15.25** | **21** |

**Sums:** 19.5 + 25 + 10.5 = 55.5 low; 29 + 36 + 15.25 = 80.25 point; 39 + 51 + 21 = 111 high. Rounded in §0.

**What would move the figures** [J]:
- **A new migration instead of folding into `0001`:** +2 to 4 h for the three requirements together, and a migration slot, which the wave plan allows once per wave (§4 of `m1-wave-plan.md`).
- **UX and CGO ruling that "visits recorded" may not be shown (CAP-16 caution 2):** removes one integer and its limbs; about −1 to −2 h. The fallback in v1.5 keeps everything else.
- **QA adding a fourth count** (§22 item 43 (2)(iii)): about +1 to 2 h in the function, the preview and the tests.
- **Item 40 (does the control stay):** moves no hours. CAP-15(h) was written so either answer fits. It does change what is written off, which is the CFO's note (item 42).

**Not included:** the measurement run itself (carrying the phones, the protocol, QA's analysis and the publication). I have not re-sized it (§3). Nor the CFO's, UX's and CGO's review hours, nor the beta's recruitment.

## 2. Where they fit in the waves

**The principle** (`m1-wave-plan.md` §7): *a requirement ticket sits in the milestone where its last limb can be verified*, and QA verifies a requirement whole (D9). Groundwork whose own limbs can be proved earlier stays earlier, as a story.

**The Coordinator's guess, M1.W8, does not survive that test.** M1.W8 is the wave for the **Kotlin halves** of the M1 requirements (`m1-wave-plan.md` §5 and §6). CAP-15 to CAP-17 contain **no native code on either platform**: the marker is a database column, the counts come through the existing `listGaps`, and the share sheet is a JavaScript call. There is nothing for W8 to build. Their limbs also need surfaces that M1 does not have.

| Requirement | Builds in | Why (last limb under the principle) | M1 groundwork |
|---|---|---|---|
| **CAP-15** | **M2**, after ENT-4's composer and DATA-3 to DATA-5's serialiser merge | Limbs (a) and (c) need the timeline, venue page, sessions and the export. The same composer files as ENT-4 mean it is **sequential after ENT-4, not parallel with it** | **Two columns and the `CHECK` in `0001`** (lines 1.1-1 and 1.3-1, about 2 to 4 h), a change to DATA-2.1 (#360). That ticket is still open and no code has merged [E: `gh issue view 360 --repo deopea-david/haunts` and `git log origin/main` in `haunts`, 2026-10-10], so this is the cheap moment. **I do not edit the ticket; the PM/BA owns the change** |
| **CAP-16** | **M2**, after CAP-4's gap surface and DATA-3's file-share mechanism | It reads gap rows and, if DATA-3 has landed, reuses the mechanism. Limb (a) needs a release-shaped Android build to capture traffic | None. `listGaps` is already in the typed face that W3 writes whole |
| **CAP-17** | App fields: **M2, as part of CAP-15's story**. The classification script: with **SPK-02's tooling**. The requirement ticket: **M5** | Its limb (c) asserts *"the published result lists the diary kind per phone"*, and that result is the SPK-02 measurement already placed at M5 | Same `0001` column as CAP-15 |

**Two findings against the placement the requirements imply:**

1. **CAP-15 limb (a) names search, and search is M4 (LOOK-9).** By my own rule the ticket would then close at M4. **Recommendation:** the PM/BA amends (a) to the surfaces that exist when CAP-15 builds, and gives LOOK-9, VPAGE and the later surfaces a missed-visit row in their own fixtures (LOOK-9(b) already asserts every matching entry in every state; about 1 h each, already in line 1.1-6). That lets CAP-15 close in M2. **If (a) is left as written, CAP-15 is an M4 ticket.** Amending a criterion is the PM/BA's, through §24; I flag it and do not decide it.
2. **My own recommendation in `block-2-review.md` §3 and `m1-wave-plan.md` §6** was to start the measurement *"as soon as M1.W8's capture story is on a phone"*. That is still right for a **paper or note diary** on the CEO's phone. **The in-app diary route cannot start then:** the entry control is in the M2 composer and the counts file and QA's computation need the M2 export. The volunteer beta is therefore **M2-gated** [I].

**File ownership, for whoever plans M2** [J]:
- CAP-15 and the CAP-17 app fields share the composer, `visits.ts`, the serialiser and `core/MANIFEST.md`. **One story, not two tickets in a wave.**
- The CAP-17 script is under `tools/` and touches none of them, so it may run in the same wave as CAP-15.
- CAP-16 adds `package.json` only if DATA-3 has not. **If it must, it stops with a `Blocked` line for the CTO** (the wave plan's contested-file rule), and the CSO approves the dependency.
- **I set no Wave field.** The tickets do not exist yet; M2 waves are planned when M1 closes.

## 3. Does `block-2-review.md` §5, *"the hours are about the same"*, still hold?

**No. I wrote it without a calculation, and the calculation does not support it.**

- **What it compared.** The 75-hour line (*"2 weeks / 75 h"*, `android-and-stack-note.md` §0.3 and the table at line 251) with *"a measurement run plus a little in-app tooling"*.
- **The in-app tooling is not little.** It is **56 to 111 h, point 80**, which by itself equals the whole 75-hour line at the point and exceeds it at the high end [J].
- **What I cannot say.** `android-and-stack-note.md` does not break the 75 h into parts [E: the note read at lines 30, 114, 227 and 251, 2026-10-10], so I cannot say how much of it was a throwaway harness that the production Kotlin module (already inside the 5 to 7 week Android line) has now replaced. I **have not re-sized the run** (protocol, oversight, analysis, publication). A sensible reading is that the run is smaller than 75 h and the tooling is not [I, low confidence], which puts the new total **above** the old line, not equal to it.
- **What the CFO should do.** Do not fold these hours into the 75-hour spike line. Carry them as **scope added after the estimate**, separately, with **the labour-at-risk marked on the CAP-15 and CAP-16 lines** (if item 40 goes the other way, or the measurement fails, that labour is written off as a cost in the year, Constitution Definitions). CAP-15 is not wasted by a failed measurement if the control stays (item 40, *"a repair tool for the user's own journal"*); CAP-16 and CAP-17 mostly are.
- **This is a correction to my own earlier memo.** `block-2-review.md` is merged and I am not editing it here. The Coordinator decides whether a one-line erratum is wanted.

## 4. Flags, each to the seat that decides (none is a block)

- **CSO.** If CAP-16 needs `expo-sharing`: *"Local file URL to share"*, no permissions mentioned, *"Included in Expo Go"* [E, [Expo, Sharing](https://docs.expo.dev/versions/latest/sdk/sharing/), retrieved 2026-10-10]. The same page says the library can also *receive* data shared from other apps; I did not read how that is enabled. **Whether the library adds a manifest entry or intent filter must be checked against PRIV-8's *"no manifest entry"* limb before approval.** React Native's own `Share` documents `url` only as *"a URL to share"*, with no statement about file URLs or Android [E, [React Native, Share](https://reactnative.dev/docs/share), retrieved 2026-10-10], so **I do not know that it can share a file** on both platforms. The summary also touches threat model **C12** (staging files deleted after the share sheet).
- **PM/BA.** (1) Add the two columns and the `CHECK` to DATA-2.1's scope and to `docs/schema/journal-db.md`. (2) Decide whether to amend CAP-15(a) (§2 finding 1). (3) CAP-17 mixes an app feature and a measurement artefact; it needs two tickets or one story plus an SPK-02 limb. (4) Source of CAP-16's file format: *"a small plain-text file"* with *"exactly six fields"* and *"the key set"* reads as a keyed format, but the format is not named. **Name it.**
- **QA.** A user can change the phone's clock, so "created on the same local day" (CAP-17) can be defeated by an honest-but-careless carrier as well as a dishonest one. The creation time is a device-clock reading, not evidence. Say so in the result's method [J].
- **UX and CGO.** §22 item 43 stands; I add nothing to it.
- **CFO.** §3 above; item 42.

## 5. Negative findings, with what would overturn them and where I looked

| Finding | What would overturn it | Where I looked |
|---|---|---|
| **These features belong in M2, not M1.W8** | A native (Swift or Kotlin) piece found in any of the three, for example a platform share API the JavaScript call cannot reach | CAP-15 to CAP-17 text in `requirements.md` v1.5; `m1-wave-plan.md` §3 to §7; the two share-sheet pages above |
| **The hours are not "about the same" as the 75-hour line** | A breakdown of the 75 h showing the in-app tooling was inside it | `android-and-stack-note.md` lines 30, 114, 227 and 251. I did not find a breakdown |
| **React Native's built-in `Share` is not established to carry a file** | A retrieved statement, or a device test, showing it does on iOS and Android | The RN Share page, which is silent |

**Read for this memo:** `constitution.md`; `roles/cto.md`; `design-feasibility-and-sizing.md` (all); `block-2-review.md` (all); `m1-wave-plan.md` (all); `requirements.md` v1.5, CAP-3, CAP-4, CAP-8, CAP-11 to CAP-17, DATA-3 to DATA-5, ENT-4, LOOK-9, §22 items 40 to 43, §24; `backlog-plan.md` §10; `pipeline/model-selection.md` §4 to §5.0; `threat-model-m1.md` C12; `haunts` issue #360. **Not read:** the other §7 tickets in M2, the CSO's rulings on dependencies, and Expo's receive-data documentation.
