# Haunts M1 — wave plan, file ownership and milestone confirmation

**Seat:** Chief Technology Officer · **Date:** 2026-10-09 · **Status:** the plan for M1's first five waves, plus an outline of the rest. **Prepares and flags; does not certify** (Constitution 6.1). It decides nothing reserved to the CEO (Constitution 5.4).
**Authority for the work:** the CEO's words of 2026-10-09, relayed in the Coordinator's commission: *"CTO: plan the first wave, beginning with SPK-21 (the B-strict scaffolding) and MAINT-4 (the arrow-function lint rule). Then the two-file store (D63), the JS-free capture path (CAP-1), and the entitlement and session foundations. Fill each ticket's files section, set the Wave field, and confirm or move the provisional milestones."*
**Binding inputs:** `architecture/ADR-0001-code-architecture.md` (D64) §2–§4 and §6; D33, D34, D63 (`decisions/2026-09-16-haunt-gate.md`); `pipeline/agentic-agile.md` items 2–5 and "The per-ticket chain"; `requirements.md` v1.4 (commit `dbeba1b`); `haunts` `docs/conventions.md` (§2 story keys, §8 spike rule, §11).
**Template note:** `pipeline/templates/` has no wave-plan template [E: listed from disk, 2026-10-09]. This follows the method in `agentic-agile-adoption.md` §4.3: components, dependency graph, files per ticket, then waves.
**Evidence tags** follow `pipeline/evidence-standard.md`. Repository facts carry the command or file they came from. Statements about Expo, SQLite or the platforms that I did not retrieve today are [K] and say so.

Provenance: CTO · opus (Opus 5.5) · effort high · 2026-10-09

---

## 0. The answer on one page

| Wave | Tickets (issue) | Engineers in parallel | Model (recommended) | What it leaves for the next wave |
|---|---|---|---|---|
| **M1.W1 — set-up** | **SPK-21** (#355), then **MAINT-4** (#308); MAINT-7 (#359) carries the wave's standup entries | **1, in sequence** | Sonnet, xhigh | Every ADR-0001 check live, each seen to fail on a planted violation; the arrow-function rule live |
| **M1.W2 — app shell** | **PLAT-1** (#267) | 1 | Sonnet | An Expo app that builds on iOS and Android; every M1 npm dependency installed once; app `tsconfig` strict |
| **M1.W3 — the two store contracts (core-first)** | **DATA-2.1** (#360) journal side · **DATA-2.2** (#361) capture side, iOS | 2 | Sonnet · **Opus** (native + schema) | `journal.db` store and migrator; `capture.db` native owner; the capture module's whole typed face |
| **M1.W4 — sessions and entitlement** | **SESS-1.1** (#362) derived sessions with durable overrides · **ENT-1.1** (#363) entitlement ledger, iOS · **DATA-1** (#195) legibility test | 2 | Sonnet · **Opus** | `deriveSessions`; the ledger's three-state answer; both schemas proved legible |
| **M1.W5 — the JS-free capture path** | **CAP-1** (#8) iOS · **DATA-16** (#352) iOS + JS · **SESS-9** (#52) tests | 2 | **Opus** · Sonnet | A visit recorded with no JavaScript; candidates deleted, never flagged; intervals and gaps proved durable |

- **At most two Engineers at once** (`pipeline/agentic-agile.md` item 4), and **never more than one Opus seat at a time** (the CEO's instruction for this build). W3 to W5 pair one Opus Engineer on native code with one Sonnet Engineer on TypeScript. The Opus CTO review and the Opus QA run between those, not alongside a running Opus Engineer.
- **No two tickets in the same wave list the same file**, with one declared exception: `eslint.config.js` passes from SPK-21 to MAINT-4 at SPK-21's merge, in W1, which runs in sequence (§3.1).
- **Android capture code waits for SPK-02.** CTO Block 2 is live. Every requirement above that names both platforms gets its Android half in a later M1 wave, as a story created when Block 2 lifts (§6). **M1 cannot close until SPK-02 has run** — at least two real weeks on three phones.
- **Milestones:** M1's order is confirmed. **28 tickets move out of M1**, because their last acceptance limb needs a surface or a service that does not exist until a later phase. Their M1 groundwork, chiefly the build-time checks, stays in M1 as stories (§7).

---

## 1. Inputs that shaped the plan

1. **The wave rule.** Waves contain no file overlap and no dependency inside the wave (`pipeline/agentic-agile.md` item 3; the template's worked example, quoted at `agentic-agile-adoption.md` §4.1). Shared `core/` changes go in a wave before the waves that use them (ADR-0001 check 15).
2. **Stories only where D34 allows:** a requirement too big for one PR or whose limbs sit in different code, or one change serving several requirements. Story keys are the parent's key, a dot and a number (`docs/conventions.md` §2).
3. **The spike rule.** No code that ships in the app reaches `main` under a spike ticket; repository tooling may (`docs/conventions.md` §8; SPK-21's own negative constraint). **So SPK-21 creates no app code.** The Expo app itself arrives under PLAT-1, a requirement ticket, in W2.
4. **D63's guards** decide the store split: one owner per file, the capture module's typed face as the only bridge, adoption idempotent through `source_candidate_id`.
5. **CTO Block 2** (Android capture on undocumented OEM behaviour) is live and lifts only with the SPK-02 device-matrix spike. Its condition reads: *"The spike runs before product code, on at least a Pixel, a Samsung and a Xiaomi, over ≥2 real weeks"* [E: `android-and-stack-note.md` §1.7]. I read "product code" there as Android capture code and apply it to all of it, storage included (§6).
6. **CTO Block 3** (JavaScript in the visit-recording path) is engaged on the record [E: `block-4-ruling.md` §2.4, line 118]. Its lift condition is *"a capture design in which the Swift and Kotlin modules write to SQLite directly and JavaScript reads later"* [E: `android-and-stack-note.md` §4]. ADR-0001 §2.3 and D63 are that design. CAP-1 in W5 is where the design is built and checked. `STATUS.md` does not list Block 3 (§9, F2).
7. **Models** (`pipeline/model-selection.md` §4, §5.2): the Engineer defaults to Sonnet; the orchestrator steps it up to Opus for the native capture modules and the SQLite schema. The recommendation column in §0 follows that rule; the Coordinator states the model in each commission.

## 2. Components and the dependency graph

```
SPK-21 checks ──► MAINT-4 rule ──► PLAT-1 app shell (package.json, tsconfig, Jest app project)
                                        │
                     ┌──────────────────┴───────────────────┐
              DATA-2.1 journal.db store              DATA-2.2 capture.db owner (iOS) + typed face
              (db interface, migrator, visit)        (schema 0001, serial queue, 6 functions + event)
                     │            │                       │                    │
                     │            └────────┬──────────────┘                    │
                     │                SESS-1.1 deriveSessions            ENT-1.1 ledger (iOS)
                     │                + overrides + cache                       │
                     │                     │                                    │
               DATA-1 legibility      SESS-9 durability tests ◄─────────────────┤
                                                                          CAP-1 recording path (iOS)
               DATA-16 adopt / expire / reconcile ◄── DATA-2.1 + DATA-2.2
```

**Why this order** [J]: every journal-side ticket after W3 calls the four-method database interface and the migrator; every capture-side ticket calls `CaptureStore` and the typed face. Building those first, alone in their wave, is check 15's core-first rule. SESS-1 and SESS-2 are one workstream: the derivation takes the overrides as input, and each ticket's tests need the other. They are built as one story, SESS-1.1. CAP-1's recorder must ask the ledger whether capture is entitled (*"receive the platform event, read entitlement, and write to `capture.db`"*, CAP-1), so ENT-1.1 precedes it.

## 3. The waves

### 3.1 M1.W1 — set-up: SPK-21, then MAINT-4

- **The dependency cannot be split away.** MAINT-4's rule needs ESLint installed and wired into the hook and CI, and SPK-21 is what installs and wires it. ADR-0001 §4 (binding) also requires **one** ESLint configuration and one invocation, so MAINT-4 cannot carry a configuration of its own.
- **The order:** SPK-21 is built, reviewed, QA'd and merged first. MAINT-4 then branches from that `main`.
- **The split:** SPK-21 creates `eslint.config.js` with an **empty, marked block** at its end (`// MAINT-4: TypeScript style — arrow functions (ADR-0001 §4)`). MAINT-4 edits only that block. Its fixtures, its documentation change and nothing else are its own. **This is the one file two tickets in one wave list, and they list it in sequence, never at the same time.** If the CEO prefers the wave rule applied literally, MAINT-4 becomes wave M1.W2 on its own and everything else moves up one. The work and the order would be identical.
- **Why SPK-21 does not install Expo's ESLint configuration, Jest-Expo or React Native Testing Library**, although ADR-0001 §3 lists them: they need `expo` and `react-native` installed as peers [K, medium], and those are product dependencies, which a spike may not land. They arrive with PLAT-1 in W2. **A flag for the CSO and the W2 Engineer:** Expo's ESLint configuration may bring in `eslint-plugin-import` [K, medium, not checked today]. If it does, it conflicts with the CSO's "no import plugin" preference (ADR-0001 §3), and the core rules plus dependency-cruiser should be used without it.
- **Planted violations become permanent.** SPK-21 commits one fixture per check under `tools/guard-fixtures/<id>/`, and `tools/prove-checks.ts` runs every fixture in CI and fails if a check passes on its planted violation. "Seen to fail" (D32) is then re-proved on every PR rather than once.

### 3.2 M1.W2 — app shell: PLAT-1

PLAT-1 creates the Expo project at the repository root (ADR-0001 §2.1; `docs/conventions.md` §11): `app.config.ts`, `metro.config.js`, `eas.json`, the app `tsconfig.json` with check 12's flags, and the first route and placeholder screen. It moves the tooling's `tsconfig.json` to `tools/tsconfig.json`. **It installs every npm dependency M1 needs** (Expo SDK, Expo Router, `expo-sqlite`, `expo-build-properties`, `jest-expo`, React Native Testing Library), so no W3–W5 ticket touches `package.json` or the lockfile. It also does the two M1 items in `docs/conventions.md` §11: the `prepare` script that installs the hooks, and widening type checks to the app. It starts `docs/dependencies.md`, the dependency record PRIV-8(d) and CSO C18 need.

- **D53:** the build uses Expo SDK 58; *"CTO checks its bugs"*. The Engineer pins an exact version and lists its known issues in the PR; I check them at review. I have not retrieved SDK 58's release state today [K: unknown].
- **PLAT-8(a)** (deployment target iOS 26.0) is set here, in `app.config.ts`. PLAT-8 itself moves to M5 (§7).
- **PLAT-1 stays in the QA column after merge.** Its single limb includes *"the capture modules are native (CAP-1)"*, which is true on both platforms only after the Android capture story (§6).

### 3.3 M1.W3 — the two store contracts (core-first)

| | DATA-2.1 (#360), journal side | DATA-2.2 (#361), capture side (iOS) |
|---|---|---|
| Owns | `src/core/store/` base: the four-method interface (`run`, `get`, `all`, `transaction`) [E: `architecture-proposals.md` line 526], the Expo SQLite and `node:sqlite` adapters, `open-journal.ts` (the only place `journal.db` is opened, in Application Support per CSO C9), `migrate.ts`, the migration registry, `0001-journal-base.sql` (the `visit` table with a unique `source_candidate_id`), `visits.ts`, `docs/schema/journal-db.md` | `modules/capture/`: the Expo module config, `index.ts` (**the whole typed face, written once**: `listCandidates`, `listGaps`, `entitlementIntervals`, `markAdopted`, `discard`, `recordEntitlement`, one change event), `schema/0001-capture-base.sql`, `ios/Core/CaptureStore.swift` (one connection on one serial queue: D63 guard (a)), `ios/Core/CaptureSchema.swift`, `ios/Bridge/CaptureModule.swift`, the native tests, `docs/schema/capture-db.md` |
| Implements | DATA-2(a) journal half, DATA-2(b) JS half (the fixture is completed with the Android story) | DATA-2(a) capture half, DATA-2(c) iOS, DATA-2(e) |

- **The face is written in full here** so that ENT-1.1, CAP-1, SESS-1.1 and DATA-16 build on it without editing it. The first-version types are in DATA-2.2's issue; DATA-2.2 may refine names in its PR, and what merges is the contract the W4 and W5 tickets build on.
- **`markAdopted` and `discard` delete rows from the start**, never flag them (DATA-16's rule, CSO C15). DATA-16 then adds the expiry and the reconcile.
- **Android, until Block 2 lifts:** the module declares no Android implementation. An Android build must still build and start (PLAT-1); the face reports capture as unavailable there rather than crashing. The exact mechanism is DATA-2.2's to propose.

### 3.4 M1.W4 — sessions and entitlement

- **SESS-1.1 (#362), a story under SESS-1, implementing SESS-1(a)(b) and SESS-2(a)(b)(c):** `core/domain/sessions.ts` derives sessions from visits, overrides, entitlement intervals and gaps, with time and parameters passed in (check 5). `core/store/sessions.ts` keeps a deletable cache. `core/store/overrides.ts` stores overrides as rows anchored to **visit** identifiers, never to a session (SESS-2(c)). `core/store/capture.ts` is the wrapper over the face (ADR-0001 §2.1). One migration, `0002-sessions.sql`. Sessions carry their partiality as data (which gaps and entitlement boundaries they straddle), so that SESS-8 can render it in M2 and SESS-9(b) can compare it.
- **ENT-1.1 (#363), a story under ENT-1, implementing ENT-1(a) on iOS:** `ios/Core/EntitlementLedger.swift` answers *"was capture entitled at t?"* natively with three answers — entitled, not entitled, unknown. The rule I set for M1 comes from my own earlier design: unknown is *"a first-class state, distinct from 'unentitled'"*, and the app must *"resolve in the customer's favour for capture while never taking money"* [E: `subscription-sizing-note.md` §3.1, line 111]. So capture records under *entitled* and *unknown*, never under *not entitled*. **ENT-2 (M3) owns how unknown is stated and how it resolves when a cached interval expires offline**; that is the sizing note's open question 4, and the M1 rule may tighten then.
- **DATA-1 (#195), test-only:** both schemas applied to `node:sqlite`; no BLOB column; every timestamp column ISO-8601 with an explicit offset. It runs after W3 because it reads both W3 schemas.

### 3.5 M1.W5 — the JS-free capture path

- **CAP-1 (#8), iOS half:** `ios/Core/VisitRecorder.swift` takes a platform visit, asks the ledger, and writes a candidate through `CaptureStore`. `ios/Bridge/CaptureAppDelegateSubscriber.swift` wires the location manager at launch without starting JavaScript. CAP-1(a)'s evidence needs a debug-only marker that records whether Hermes started, and a synthetic-visit harness. **Neither may ship in a release build** (PRIV-8). CAP-1(b)'s two mechanisms (Core as its own Swift module, CSO C7; `tools/check-capture-isolation.ts`) come from SPK-21 and DATA-2.2. Authorisation prompts and starting or stopping monitoring are CAP-2 and CAP-7, not this ticket.
- **DATA-16 (#352), iOS and JS:** `core/store/candidates.ts` holds `adoptCandidate` (insert the visit, then `markAdopted`), the start-up reconcile, and expiry. **Expiry runs in JavaScript**, by `discard`, because CONF-15's window is a user setting that lives in the journal, and adding a native command to carry it would widen the typed face beyond ADR-0001 §2.3 [J]. The cost is that an expired candidate stays in `capture.db` until the app next opens. The CSO is asked to accept or reject that (§8). Whether `secure_delete` is set is the CSO's call; DATA-16 sets whatever the CSO decides.
- **SESS-9 (#52), tests only:** the iOS half of (a) reads intervals and gaps natively with no JavaScript; (b) rebuilds the session cache after a lapse and resubscribe and compares the partiality data exactly. Its Kotlin half joins the Android wave.

## 4. Contested files and the rules that keep them uncontested

| File | Why every ticket wants it | Rule |
|---|---|---|
| `package.json`, `package-lock.json` | Any dependency | **SPK-21 in W1 (dev tools), PLAT-1 in W2 (everything else M1 needs).** No W3–W5 ticket adds a dependency; one that finds it needs one stops and writes a `Blocked` line for the CTO |
| `src/core/MANIFEST.md` | Check 8(a): every core file is listed | **At most one ticket per wave adds `core/` files**: DATA-2.1 (W3), SESS-1.1 (W4), DATA-16 (W5). Tests are not listed. A PR touching it carries a `## CTO note` (check 10) |
| `src/core/store/migrations/index.ts` | The migration registry | **At most one migration per wave**: `0001` DATA-2.1 (W3), `0002` SESS-1.1 (W4). Numbers are assigned here, not chosen by the Engineer |
| `modules/capture/index.ts`, `ios/Bridge/CaptureModule.swift` | The typed face and the module class | **Written whole by DATA-2.2 in W3.** Later tickets add Core files only |
| `modules/capture/ios/Core/CaptureStore.swift` | The one connection | DATA-2.2 creates (W3); only DATA-16 modifies it in M1 (W5, to apply the CSO's deletion setting) |
| `tools/structure.json` | Check 1: every folder | **SPK-21 registers every folder M1 needs in one go** (§2.1's tree, the ten features, the M1 sub-folders in this plan). A ticket needing a new folder stops and asks |
| `eslint.config.js` | All lint rules | SPK-21, then MAINT-4's marked block only (§3.1). A guard file: any PR touching it carries a `## CSO note` (check 10) |
| `docs/standups/YYYY-MM-DD.md` | Every seat's entry | **Exempt by design:** append-only and written by every seat (`standup-routine.md` §2). No ticket's ownership table lists it. A conflict there is resolved by keeping both entries and is counted in the delivery log separately from code conflicts |

## 5. The rest of M1, outlined and not yet placed

These are planned at the W5 gate, against the interfaces W3–W5 actually merge. **No Wave field is set on them today.** Planning them now would fix files against code that does not exist yet [J].

| Provisional wave | Work | Note |
|---|---|---|
| M1.W6 | Venue schema rules: VEN-8, VEN-10, VEN-11, VEN-12 (migration `0003`, `core/store/venues.ts`, the refresh path). **Alongside:** the theme token system as a story (typed tokens and Mono, so that M2's screens use tokens from the first line; THEME-10(c), THEME-2(a)'s contrast check) | I check VEN-8's trigger myself at that PR (`block-4-lift.md` §3.4). Opus for the schema (§5.2) |
| M1.W7 | Venue index pipeline: VEN-17, VEN-2, VEN-3, VEN-4, VEN-5, VEN-6, VEN-23. **Alongside:** the MEM-1(a) string check and the DFLT-1(a) settings register, each as a story, before M2 adds strings and settings | **Open conflict, raised now:** VEN-17 requires the harness, a Python program, to live in the product repository with a `PYTHONHASHSEED` sweep, and D41 says all `haunts` scripts are TypeScript. Porting it, or an exception, is a decision to make before W7 (§9, F5) |
| M1.W8 | **Android, blocked by SPK-02:** the Kotlin halves of DATA-2 (story), ENT-1 (story), CAP-1, DATA-16 and SESS-9 | Created as stories when Block 2 lifts |
| when SPK-22 lands | PRIV-8(e), Android release manifest without `INTERNET`; PRIV-8(d), the dependency check, as a story | |

## 6. Block 2 and Android

- **What waits:** every line of Kotlin in `modules/capture/`. That covers the capture-file owner, the ledger, the recorder, deletion and the native read tests.
- **What does not wait:** the Android **app build** (PLAT-1), and all TypeScript, which is shared.
- **The consequence, stated plainly:** DATA-2, DATA-16, CAP-1, SESS-9 and PLAT-1 can each be verified **limb by limb on iOS** in W3 to W5, but **none of them reaches Done** until its Android story merges, after SPK-02. So **M1 closes no earlier than SPK-02's two real weeks on three phones, plus the Android wave.** SPK-02 (#280) is open in Backlog today [E: `STATUS.md`, "M0 spikes still open"].
- **What would change this:** the CEO overruling Block 2, or SPK-02 running now in parallel with W1–W5. The second is the cheap path [J]: it is calendar time, not effort, and it is the larger build risk (`block-4-ruling.md` §2.4).
- **A narrower reading I am not adopting:** that Block 2 covers only background execution (CAP-3), so that Kotlin storage could proceed now. It is defensible, because SQLite on Android is documented behaviour. I am not adopting it, because the block's text says *"before product code"*, and narrowing my own block to suit the plan is the kind of move the block exists to prevent.

## 7. Milestones: confirmed, and what moved

**Principle** [J]: a requirement ticket sits in the milestone where its **last** limb can be verified. QA verifies a requirement whole (D9). A ticket in M1 whose last limb needs a screen, a billing service or a release review would hold M1 open for no reason, or tempt someone to close M1 with it unverified. The groundwork stays in M1, as a story or as part of SPK-21.

| Moved | From → to | Why |
|---|---|---|
| **ENT-1** (#146) | M1 → **M3** | ENT-1(b) (*"intervals survive reinstall-while-offline"*) needs the billing layer to restore intervals after a delete-and-reinstall [I]. ENT-1(a) is built in M1 as ENT-1.1. If the PM/BA reads "reinstall" as an update in place, ENT-1 can be verified at the M1.W4 gate and close early |
| **ENT-2** (#147) | M1 → **M3** | Its six constructed states include refunded, revoked, billing retry and grace period, which exist only with StoreKit and Play Billing (M3; SPK-10) |
| **CAP-7** (#9) | M1 → **M3** | (a) expires a trial (ENT-3, M3) and checks the Android foreground service stops (CAP-3, M2; Block 2). It is the same behaviour as ENT-6 (M3) |
| **FT-ENT-1** (#145) | M1 → **M3** | Both of its tasks moved |
| **VEN-1** (#64) | M1 → **M2** | (a) runs *"the full core loop in aeroplane mode"*; the loop is M2 |
| **VEN-7** (#72) | M1 → **M2** | Its test deletes the index and renders the **venue page** (M2). Its copy-on-reference rule is built with the venue schema in M1.W6 |
| **THEME-1, 2, 3, 4, 5, 6, 7, 10, 11, 12** (#328, #329, #326, #330, #323, #331, #332, #322, #324, #325) and **FT-THEME-1, FT-THEME-2** (#321, #327) | M1 → **M4** | Each needs the primary screens, the headlines, the entitlement fixtures (ENT-14) or the icon setting (PLAT-9) for its last limb. **The token system and the contrast check stay in M1** as a story (M1.W6), before screens multiply in M2, as backlog plan §10 intended |
| **MEM-1** (#3), **DFLT-1** (#5), **FT-RULES-1** (#2), **FT-RULES-2** (#4), **EP-RULES** (#1) | M1 → **M5** | MEM-1(b) is a release-pack review, and DFLT-1(b)–(d) need every setting to exist. **Their CI checks stay in M1** (M1.W7 stories), written before the code they guard |
| **PRIV-8** (#242), **PRIV-1** (#240), **PRIV-2** (#241), **FT-PRIV-1** (#239) | M1 → **M5** | PRIV-8(f) is checked on device at each release, and (e) waits on SPK-22. PRIV-1 diffs store copy, onboarding and backup screens; PRIV-2 needs every transmission path and the PRIV-9 note (M5). **PRIV-8(a)–(c) are built in M1.W1 by SPK-21** |
| **PLAT-8** (#268) | M1 → **M5** | (b) needs the basemap asset pack (M4) and (c) the release device matrices (M5). (a) is set by PLAT-1 in M1.W2 |
| **MAINT-6** (#356) | none → **M0** | Agent controls, done before any build work, like MAINT-1, 2, 3 and 5 (all M0) |

**29 moves** (28 out of M1, plus MAINT-6 into M0). **Confirmed in M1:** SPK-21, MAINT-4, MAINT-7, PLAT-1, DATA-1, DATA-2, DATA-16, CAP-1, SESS-1, SESS-2, SESS-9, the venue tickets other than VEN-1 and VEN-7, and their features.

**M2–M5:** I confirm the **phase order** (backlog plan §10). I have **not** checked every ticket inside M2–M5 against this principle today. Each phase gets that check at its own wave planning. The milestone descriptions are updated to say so, and each keeps its Constitution 5.5 sentence.

## 8. For the CSO

**Tickets in W1–W5 that need CSO review** (`needs:cso-review`):
- **Already labelled:** SPK-21, CAP-1, DATA-16.
- **Added today:** MAINT-4 (it edits `eslint.config.js`, a guard file under check 10); PLAT-1 (the first production dependencies; the hook-installing `prepare` script, `docs/conventions.md` §11); DATA-2, together with its stories DATA-2.1 and DATA-2.2 (the generated body of DATA-2 already says *"Security-relevant"* but the label was missing; C8 parameterised SQL, C9 store location); ENT-1.1 (the only write path for entitlement; an import must never grant it, DATA-5(c)).

**SPK-21's development dependencies, for approval before the Engineer installs them** (D40's rule, D64), all exact-pinned:
- `eslint`
- `typescript-eslint`
- `@eslint-community/eslint-plugin-eslint-comments` (named in D64)
- `dependency-cruiser` (named in D64)
- `jest`, plus one TypeScript transform for the plain-Node test projects. The Engineer proposes which, with its dependency count.

Not in SPK-21 (they need Expo installed, so they come with PLAT-1): `jest-expo`, React Native Testing Library, and Expo's ESLint configuration (see the import-plugin flag in §3.1). The Maestro CLI (C20) arrives with the first end-to-end flow, not in M1.W1. **The proofs run on Node's built-in test runner**, which adds no dependency [J].

**Also for the CSO:**
- **The pre-commit change needs the CEO's approval.** SPK-21 must add one hook to `.pre-commit-config.yaml`, and that file changes only *"with a CSO note and CEO approval"* [E: the file's own header; `SECURITY.md`]. ADR-0001 §6 item 2 and C23 (new guard files join the protected list) also need the CEO's approval. **Both are needed before SPK-21 can merge.**
- **DATA-16's expiry runs in JavaScript (§3.5).** An expired candidate stays in `capture.db` until the app next opens. Accept or reject.
- **`secure_delete` or `VACUUM` for `capture.db`** (DATA-16) is the CSO's to set.

## 9. Findings, flags and disagreements, each stated once

- **F1. SPK-01 (#279) is closed.** Its "done when" is met: the lift is committed on `main` (`block-4-lift.md`, `211f1fd`), and nothing in v1.4 touched VEN-7…VEN-12 or the §7.2 preconditions [E: `git diff a530dd3 HEAD -- products/haunt/requirements.md` shows no change to those rows], so overturn item 1 has not fired. **What remains is other seats' work, not this spike's:**
  - **PM/BA:** write S-1's numeric trigger into §7.7.5 and VEN-24(b). `requirements.md` line 347 still reads *"materially worse than 25 m"*; the lift asked for this on 2026-09-28.
  - **PM/BA:** the prose errata in VEN-9, VEN-11 and the `venue_ref` precondition.
  - **Any seat but the CTO:** recompute the 1.177 Rayleigh factor (gate Condition 6).
  - **CTO:** check VEN-8's trigger at the first venue-schema PR (M1.W6).
- **F2. Block 3 is missing from `STATUS.md`** (PM/BA). It is engaged on the record (§1 item 6). I will write its lift confirmation when CAP-1's iOS half and DATA-2.2 merge, against its own condition, rather than lift it on a design alone.
- **F3. Two ticket titles are stale against v1.4** (PM/BA, regeneration). The bodies were regenerated at `6e32e86`, but the titles still read *"One SQLite file"* (DATA-1, #195) and *"SQLite as a written contract for four consumers"* (DATA-2, #196). D63 changed both.
- **F4. ENT-1(b)'s "reinstall"** (PM/BA). Is it delete-and-reinstall or update-in-place? The first needs billing (M3); the second is testable in M1. I placed ENT-1 on the first reading.
- **F5. VEN-17 against D41** (CEO decision, via PM/BA). VEN-17 needs a Python harness with a `PYTHONHASHSEED` sweep in the product repository; D41 makes every `haunts` script TypeScript. Before M1.W7, one must give way: port the harness, or record an exception. I lean towards an exception scoped to `tools/venue-index/` [J], because a port risks changing the outputs the Block 4 discharge rests on.
- **F6. The optional check 17** (an agent `PostToolUse` lint hook) is not in SPK-21. It is a CSO-baseline file and needs the CEO's approval (ADR-0001 §3). If wanted, it is its own `MAINT-n` ticket.
- **F7. M1's length is now set by SPK-02, not by W1–W5** (§6). This is the most consequential line in this plan for the calendar.

## 10. Where I looked, and what would change this plan

**Read in full for this plan:** ADR-0001; `requirements.md` v1.4 rows CAP-1…CAP-10, SESS-1…SESS-9, ENT-1, ENT-2, ENT-6, DATA-1…DATA-16, MEM-1, DFLT-1, PRIV-1, PRIV-2, PRIV-8, PLAT-1, PLAT-8, THEME-1…THEME-7 and THEME-10…THEME-12, VEN-1…VEN-8, VEN-10…VEN-12, VEN-17 and VEN-23, and CONF-15; D33, D34, D63, D64; `backlog-plan.md` §7–§10; `agentic-agile-adoption.md` §3–§4; `pipeline/agentic-agile.md`; `standup-routine.md` v0.4; `block-4-lift.md`; `android-and-stack-note.md` §1.7 and §4; `subscription-sizing-note.md` §3.1; `architecture-proposals.md` §6.1 and its file tree; `cso-review.md` §9.1. **In `haunts`:** `CLAUDE.md`, `docs/conventions.md`, `.pre-commit-config.yaml`, `package.json`, `tsconfig.json`, the story template, and every ticket edited [E: `gh issue view`, 2026-10-09].
**Not read:** the M2–M5 tickets beyond those moved into them (§7); the Expo SDK 58 release notes (§3.2).

**What would change it:**
- **SPK-02 starting, or Block 2 overruled:** W8 moves forward.
- **DATA-2.2's merged face differing from its issue:** W4 and W5 build on what merged, and the Engineer says so in the PR.
- **The CSO rejecting JavaScript-driven expiry:** DATA-16 gains a native command, and the typed face changes by a new ADR, not quietly.
- **A merge conflict, or an escaped defect, in any wave:** parallelism drops to one (`pipeline/agentic-agile.md` item 4).

## 11. Change log

| Date | Change |
|---|---|
| 2026-10-09 | First version. Waves M1.W1–W5 placed; W6–W8 outlined; 29 milestone moves; SPK-01 closed; MAINT-6 placed in M0 and set to QA |
