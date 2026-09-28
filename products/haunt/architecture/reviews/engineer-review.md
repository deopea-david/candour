# Review: SPK-20 code architecture proposals (D59)

**Seat:** Engineer (non-author review; the CTO wrote the proposal, on Opus — this review runs on Sonnet per `pipeline/model-selection.md` §5.4) · **Date:** 2026-09-28 · **Document reviewed:** `products/haunt/architecture/architecture-proposals.md`, worktree `agent-afbde775b58a90044`, as of the CTO's 2026-09-27 version (change log: "First version, not yet reviewed by a second seat or the CSO")
**Reads against:** `decisions/2026-09-16-haunt-gate.md` (D27–D60), `products/haunt/requirements.md` v1.3, `haunts/docs/conventions.md`, `haunts/CLAUDE.md`
**Verdict: agree with Option B.** No blocking changes needed before the CEO decides D59. Both CTO findings are handled correctly — finding 1 (SQLite corruption) is fixed by the two-file design in the document itself; finding 2 (OS backups) is correctly routed to CSO/CGO/CEO rather than decided here. A handful of small items are noted below as accepted or deferred, none of them blocking.

**Framing note, so the reader knows what this review does and doesn't cover.** Per the evidence standard, a second agent pass over the same words is not independent verification of *interpretation* — it is independent verification of *arithmetic and of claims that a named source says X*. So this review does three things: (1) re-derives the buildability judgment from the requirements and conventions directly, in my own words, rather than checking the CTO's reasoning reads correctly; (2) retrieves the load-bearing sources myself and checks they say what the document says; (3) traces the worked example against the actual requirement text. Security and user-data policy are out of scope by the commission (CSO, CGO, CEO).

---

## 1. What I checked, and how

| Check | Method | Result |
|---|---|---|
| Both CTO findings, at source | Fetched sqlite.org, expo-sqlite's README/podspec, Android Auto Backup docs, Apple's iCloud backup doc myself | Both confirmed accurate — detail in §2 |
| A sample of load-bearing "industry practice" claims (E1/E2 Expo Router `src/app`, E4 Bulletproof React cross-feature rule, E20 `node:sqlite` stability) | Fetched each source myself | All three quoted accurately — detail in §3 |
| Every direct quote from `requirements.md` used in the proposal (CAP-1, CAP-1(b), VEN-7, VEN-8, VPAGE-4, DATA-1, DATA-2, DATA-13, PRIV-8) | Grepped `requirements.md` for the exact rows, compared word-for-word | All exact matches — no misquotes, no invented criteria |
| The worked example ("confirm a visit") | Traced step by step against VEN-7, CAP-1, SESS-1/3, VPAGE-3/6, DATA-2(b) | Holds together — detail in §4 |
| Whether the named tooling can actually enforce the boundaries claimed | Checked `import/no-restricted-paths`' zone mechanism against the ~10-feature layout | Enforceable, linear in the number of features — detail in §5 |
| What's missing (testing, errors, migrations, native boundary, theming) | Read §6.1, 6.4, 6.5, 6.9, 6.10 against the requirements' BLOCKING criteria | All five are covered; no material gap found — detail in §6 |

---

## 2. The two CTO findings, verified at source

**Finding 1 — two copies of SQLite corrupting one file.** Confirmed on all three legs:
- **sqlite.org's own text**, §2.3, matches the document's quote exactly, including the "at least one commercial product … released with exactly this bug" line [E, https://www.sqlite.org/howtocorrupt.html, fetched 2026-09-28]. The mechanism is real: two library copies keep separate mutex-protected lists of open connections, so a `close()` on one can clear locks the other still thinks it holds.
- **expo-sqlite vendors its own SQLite and renames symbols to avoid the iOS system copy** — confirmed against the README on `main` [E, https://raw.githubusercontent.com/expo/expo/main/packages/expo-sqlite/README.md, fetched 2026-09-28: "Replace sqlite3 symbols to prevent conflict with iOS system sqlite3"].
- **The iOS podspec copies `vendor/sqlite3/sqlite3.c` into the pod and compiles it there** — confirmed by fetching the podspec directly [E, https://github.com/expo/expo/blob/main/packages/expo-sqlite/ios/ExpoSQLite.podspec, fetched 2026-09-28: `vendor_sqlite_src!` copies `sqlite3.c`/`sqlite3.h` from `vendor/` into `ios/` before the pod builds].

So the premise is right (Expo SQLite is a second, distinct copy from whatever native Swift/Kotlin code would normally link), the corruption mechanism is right, and **the fix is right**: if `capture.db` is opened only by native SQLite and `journal.db` is opened only by Expo SQLite's copy, no file is ever opened by two library copies at once, so the §2.3 mechanism cannot arise for either file. This is a structural fix, not a mitigation. I also checked the second half of the finding (migration ordering when iOS relaunches the app for a visit before JS has run): the logic holds — a native relaunch that has never run JS cannot hit a schema JS hasn't migrated yet if native code owns and migrates only its own file.

One consequence worth surfacing for the CTO, not a defect: the two-file split also **simplifies** DATA-2(b)'s concurrency fixture ("simultaneous native write and JS read"). Under the redesign, JS never opens `capture.db` directly — it only calls the capture module's typed functions, which read `capture.db` natively and hand back plain values. So the remaining concurrency case is ordinary same-process, same-library WAL concurrency (one writer, one reader, one copy of SQLite), which is exactly what WAL is for — a materially easier property to guarantee than the original four-consumer, one-file design. The document already flags that DATA-2's wording needs a §24 row; this is a reason the new wording will be easier to satisfy, not harder.

**Finding 2 — OS backups.** Confirmed:
- **Android Auto Backup**, default-on from API 23, includes "files in the directory returned by `getDatabasePath(String)`, which also includes files created with the `SQLiteOpenHelper` class" [E, https://developer.android.com/identity/data/autobackup, fetched 2026-09-28 — exact match to the document's quote].
- **iOS**: I could not load Apple's current backup-guide page directly (it is client-rendered and returned only its title to two fetch attempts, including via a reader proxy). I confirmed the underlying mechanism from the same page's readable fragments — nonpurgeable data is backed up by default and `isExcludedFromBackup` is the opt-out for files that don't need to be [E, same URL, partial render, fetched 2026-09-28] — which supports the claim but is **short of a verbatim match** to the document's quoted phrase "Included in iCloud and device backups." I'd class this citation as corroborated-but-not-fully-verified rather than confirmed outright; it does not change the finding (this is well-established iOS behaviour [K, high confidence] independently of the exact page text), but I'm flagging the gap per the evidence standard rather than silently upgrading it.

The document correctly routes this as a user-data policy question to the CSO, CGO and then the CEO, not as something it decides. That's the right call under Constitution 5.4, and it's outside this review's scope by the commission — I'm not assessing the policy answer, only that the architecture doesn't quietly pre-empt it. It doesn't: `core/store/paths.ts` (JS side) and the native `CaptureStore` (native side) are named as the one place per side the store files' locations are set, so either backup answer is a localized change. I'd soften the document's own "a one-line change" phrasing slightly — Android's granular exclusion needs a `dataExtractionRules` XML resource plus a manifest reference, not literally one line — but the substance (a single, well-known point of control, not a scattered one) is correct.

---

## 3. Spot-checked "industry practice" claims

| Claim | Verified against | Result |
|---|---|---|
| Expo Router: `src/app` is routes-only; config stays at root; custom roots "highly discouraged", "will not accept bug reports" | Fetched the live page [E, https://docs.expo.dev/router/reference/src-directory/, 2026-09-28] | Exact match |
| Bulletproof React: organize by features folder; don't import across features, compose at the app level; "shared -> features -> app" via `import/no-restricted-paths`; "you don't need all of these folders for every feature" | Fetched the doc directly [E, https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md, 2026-09-28] | Exact match, including the folder-selectivity quote used in §4.B |
| `node:sqlite` is Release Candidate from Node 24.15.0, no flag needed | Fetched Node's own v24 docs [E, https://nodejs.org/docs/latest-v24.x/api/sqlite.html, 2026-09-28] | Exact match — this is load-bearing because it underwrites the whole "store logic tested against real SQLite in CI, not a device" testing story |

Every direct requirement quote used in the proposal (CAP-1, CAP-1(b), VEN-7, VEN-8, VPAGE-4, DATA-1, DATA-2, DATA-13, PRIV-8) was checked word-for-word against `requirements.md` v1.3 and matches exactly. No invented or loosened acceptance criteria.

I did not re-verify every citation (E9–E13 Expo Modules/Turbo Modules comparison, E22–E25 testing tools, E29–E33 the rest of §6). These are sampled, not load-bearing to the *decision* between A/B/C the way the two named findings and the boundary-enforcement mechanism are, and nothing in them reads as implausible against what I know of these tools [K].

---

## 4. The worked example ("confirm a visit") — holds together

Traced step by step against the requirements it claims to satisfy:

- **VEN-7** ("the venue row is copied… `first_referenced_at` is set") is implemented exactly as worded, inside the same transaction that inserts the visit — not as a separate step that could be skipped or reordered.
- **CAP-1** (no JavaScript in the recording path) is respected structurally: steps 1–2 name only Swift/Kotlin files with no import of React or the bridge, and the isolation check (`check-capture-isolation.ts`) is a mechanical backstop, not a convention.
- **SESS-3** ("one row per night") is produced by a pure function (`deriveSessions`) fed from the two stores plus overrides — matches SESS-1/2's requirement that sessions are derived, never stored as ground truth.
- The **idempotency claim** for the confirm step is correct, and I checked the failure window specifically: the transaction that writes the visit (with a unique `source_candidate_id`) commits *before* `markAdopted()` is called on the capture module. A crash in that window leaves an orphaned "not yet adopted" candidate whose visit already exists — exactly the case the described app-start reconciliation sweep (query `journal.db` for already-used `source_candidate_id`s, mark the matching `capture.db` rows adopted) fixes. I could not find a crash ordering that produces a duplicate or a lost visit under the described sequence.
- **VPAGE-3/6** (the venue page's true mean over the complete visit set, entitlement-blind) is satisfied by `getVenue`/`listForVenue`/`venueSummary` reading only journal repositories, with `core/store/entitlement.ts` named as the only entitlement reader and excluded from that import graph — matches VPAGE-4's requirement and its CI check.

No step in the six-file, six-function chain is asserted without a requirement ID or a named mechanism behind it. This is the one place a plausible-sounding worked example most often turns out to paper over a gap, and I didn't find one here.

---

## 5. Can the boundaries really be enforced by the named tooling?

Yes, and the mechanism scales the way the document implies. `import/no-restricted-paths`' zones are declared per-pair (`target`, `from`, optional `except`), so "no feature imports another feature" across ~10 `features/*` folders needs one zone per feature (target = that feature, from = `features/*`, except = itself) — ten short entries, not a combinatorial blow-up, and it's the same construction Bulletproof React itself uses for its own (smaller) feature set, which I confirmed at source in §3. `no-restricted-imports` on named import sources (`expo-sqlite`, `modules/capture`) and `no-restricted-globals` with `checkGlobalObject: true` for the network ban are both standard, single-purpose rules doing one job each, not one rule trying to do everything. The two bespoke TypeScript checks (`check-capture-isolation.ts`, `check-network.ts`) are each a single grep-shaped check over a bounded file set — plausible to write and to keep correct.

The one enforcement gap the document names honestly rather than glosses over: the `core/` entry rule ("code enters core only if two features need it, or a requirement names it, or it touches storage") is enforced by CTO review, not by a tool. That's a real, if modest, risk — a junk-drawer core is exactly the failure mode Option C's package walls would prevent mechanically. I don't think it's blocking: the rule is written down, has a stated test ("`core/` exceeds about a quarter of `src/` by lines" in the ADR's "Revisit when" section), and a one-developer-plus-agents team can hold a review-time rule for this scope of app. But it is the one place B's story is "checked, not hoped for" only partway, and I'd want it re-examined if the team composition changes.

---

## 6. What's missing? — testing, errors, migrations, native boundary, theming

I looked for the five things the commission named as commonly missing from architecture proposals. None is materially absent:

- **Testing** (§6.9): layered correctly — pure domain functions in Jest (fast, no I/O), store logic against real SQLite via `node:sqlite` (verified as RC-stable in §3, so this isn't resting on an experimental flag), components via React Native Testing Library, native via XCTest/JUnit, instrumented tests for the two BLOCKING capture criteria, Maestro end-to-end against the shipped binary. The `tools/limb-coverage.ts` idea (map every requirement limb to its evidence, let QA judge it) is a sound instrument — it doesn't grade itself, which is the right call given D30/D34 already reserve "Done" for QA.
- **Error handling** (§6.10): the honesty-states-are-data / genuine-faults-throw split is the correct read of the requirements (several ACs, e.g. CAP-2(b), SESS-5, PHOTO-7, explicitly want an "unknown"/"gap" state rendered, not an exception swallowed or thrown). Per-route `ErrorBoundary` plus a diagnostics channel that is typed to exclude free-text (so DATA-13 is structural, not policy) is a reasonable, checkable design.
- **Migrations** (§6.1): plain numbered SQL, `PRAGMA user_version`, one migrator per file/owner — this is Expo's own documented pattern (confirmed in the document's own E17 citation, which I did not need to re-verify given it's Expo's plain reference page and not one of the two contested findings) and avoids the JS-only-migration trap that rules out Drizzle for the native side.
- **The native-module boundary** (§6.4): the Core/Bridge split with a mechanical isolation check is the strongest part of the document — it turns CAP-1(b), a BLOCKING criterion, into a CI-checkable fact rather than a promise.
- **Theming** (§6.5): inherits the CTO's own already-adopted standard (`design-feasibility-and-sizing.md` §4.1) and just gives it a home (`ui/theme`, `ui/primitives`, `ui/variants` with a README register per D52's "listed, with its reason" condition) — nothing new invented here, correctly deferred to the standard already set.

---

## 7. Findings, with disposition

| # | Finding | Disposition |
|---|---|---|
| 1 | SQLite two-copy corruption risk, and the two-file fix | **Fixed** — verified correct at source (§2); no further action needed from the CTO on the technical design. The §24 wording row for DATA-1/DATA-2 the document already proposes is the right next step |
| 2 | OS-level backups (Android Auto Backup, iOS device backups) copy the store by default | **Deferred**, correctly, to CSO → CGO → CEO as user-data policy (Constitution 5.4). Architecture doesn't pre-empt it: file locations are centralized per side, so either answer is a small, localized change. Minor: soften "a one-line change" — Android's path needs a `dataExtractionRules` resource, not literally one line |
| 3 | `core/` entry-rule enforcement is review-only, not mechanical | **Accepted** — real but modest risk, honestly disclosed by the CTO, with a stated revisit trigger. Worth re-examining only if team composition changes |
| 4 | The JSX-literal (no-bare-text-outside-`strings/`) lint rule is unnamed, deferred to MAINT-4 | **Accepted as flagged** — already tagged [K] by the CTO, correctly left open rather than guessed at |
| 5 | iOS backup citation (E33) could not be fully re-verified verbatim; underlying mechanism corroborated, not a verbatim match | **Accepted, flagged** — doesn't change finding 2's substance, but per the evidence standard this citation shouldn't be treated as fully confirmed on a future artifact without a better source |
| 6 | DATA-2(b)'s concurrency fixture gets materially simpler under the two-file design (same-process WAL concurrency, not two-library coordination) | **Note for the CTO**, not a problem — worth stating explicitly in the §24 row so PM/BA rewrites the acceptance criterion to match what's actually being tested |

No finding rises to "changes needed" before the CEO decides D59.
