# Haunts M1 threat model: waves W1 to W5

**Seat:** Chief Security Officer · **Date:** 2026-10-10 · **Status:** The threat model for M1.W1–W5, written alongside the CTO's wave plan. **It prepares and flags; it does not certify** (Constitution 6.1: *"Agent reviews **prepare and flag; they do not certify**"*). **No block is exercised.** My block is *"Release — for unresolved material vulnerabilities or absent threat modelling"* (`roles/cso.md`), and nothing in M1.W1–W5 is a release. Everything below is a **threat**, a **condition** to be written into a ticket, or a **flag** to the seat that owns the decision.
**Authority:** the CEO, 2026-10-09: *"CSO: write the threat model alongside, and approve the B-strict dev tools."* The waves are those of `architecture/m1-wave-plan.md` (CTO, 2026-10-09; candour PR #31).
**Scope**, as commissioned: the B-strict guard checks and their bypass classes (W1); the Expo app shell and its first production dependencies (W2); `journal.db` and `capture.db` (D63) and the capture module's typed face (W3); the entitlement ledger (W4); the JS-free capture path (W5). **Out of scope:** Android capture code (CTO Block 2; it waits for SPK-02 and the Android wave), import, export, backup, screens, billing and release. Each is named in §6 where a condition waits for it.
**Companion:** `architecture/cso-m1-w1-rulings.md` (same date): the SPK-21 dependency decision, the CSO note for the CEO, and the two DATA-16 rulings. This document cites it rather than repeating it.
**Template note.** `pipeline/templates/` has no threat-model template (cost-sheet, decision-record, dissent-memo, gate-pack, idea-brief, proposal, requirements, research-brief, review-pack) [E: listed from disk, 2026-10-10]. This follows my previous practice in `reviews/cso-review.md`: page one for the CEO, then the threat model, then conditions and a register.
**Evidence tags** follow `pipeline/evidence-standard.md`. Sources are retrieved this session unless stated, and the register in §8 links them. Repository facts name the file and commit. Vendor documentation is the single source for how a vendor's product behaves; I flag that once here.

Provenance: CSO · opus (Opus 5.5) · effort high · 2026-10-10

---

## Page one — for the CEO

**Verdict.** M1.W1–W5 can proceed as planned from a security standpoint, **once SPK-21's toolchain is fixed** (TypeScript 6.0.3, condition T in the rulings) **and three conditions are written into tickets that do not yet carry them** (C10, C21, and C8's lint rule; §6.2). Nothing here needs money or a decision of yours beyond the CSO note (rulings §2) and, later, a maximum for the candidate-expiry setting (rulings §3.1 E2).

**The three risks that matter most in M1, in order:**

1. **The guards that keep PRIV-8 (no networking) and CAP-1 (no JavaScript in capture) true can be bypassed, or can fail silently.** These checks exist because AI agents will write most of the code (D64), and an agent under pressure to pass a check will find the gap in it [J]. I found three ways the guards could pass while broken. (a) As specified, typescript-eslint and dependency-cruiser cannot run on the TypeScript in `haunts` at all. (b) dependency-cruiser quietly falls back to a loose parser when it cannot parse. (c) One edited line in `package.json` would switch off the hook and CI together. Beyond those, twelve classes of bypass need a planted fixture each (§3). **Fixes:** condition T, fixtures F1 and F2, the `check-all.ts` entry point, the two-tier protected list, and new conditions C25–C28.
2. **Supply chain, on our machines first and in the app next.** SPK-21 adds 392 development packages, including two native binaries that run on every developer's machine and in CI. PLAT-1 adds the first production code, and every Expo package brings its own Swift and Kotlin. **On iPhone, nothing mechanical stops third-party code from opening a network connection.** That rests on the dependency review (C4) and on capturing the app's network traffic before each release (C5). That limit has stood since the architecture review, and it is stated again here so it is not forgotten.
3. **Location data kept, or recoverable, longer than we say.** Unconfirmed candidates can outlive their 30-day window if the user stops opening the app (rulings §3.1). Deleted rows linger in free pages unless `secure_delete` is set (rulings §3.2). Both files go into the phone's own backups by your decision (D61). **No ticket yet sets the iOS file protection class on either file** (C10). The fix is cheap: one line per file, plus a test.

**What I need from you, one at a time:** first, the CSO note for SPK-21 (rulings §2). Later, when the PM/BA proposes it, a maximum for the candidate-expiry setting (rulings §3.1).

---

## 1. What is at stake

| # | Asset | Where it lives in M1 | Why it matters |
|---|---|---|---|
| A1 | **The confirmed journal**: visits, with their times and places | `journal.db`, opened by JavaScript through Expo SQLite (D63; DATA-2.1) | The most sensitive thing the product holds. LOOK-2's design note: *"a heatmap of a person's own life is the single most revealing artifact this product can render"* (`requirements.md`) |
| A2 | **Unconfirmed candidates**: places the phone noticed and the user has not yet kept | `capture.db`, opened only by native code (D63; DATA-2.2) | Location the user has **not chosen** to keep, which Article 4's minimum-data rule bears on most directly: *"delete it when no longer needed"* |
| A3 | **Capture gaps and entitlement intervals** | `capture.db` (SESS-9, ENT-1) | Kept for years by design (DATA-16(d)). Their integrity decides how a session is described long after the fact |
| A4 | **The guard system**: the B-strict checks, their fixtures and their configuration | `haunts` repository: `eslint*.config.js`, `.dependency-cruiser.cjs`, `tools/`, `.pre-commit-config.yaml`, `.github/workflows/` | **The mechanism that keeps PRIV-8 and CAP-1 true for first-party code.** If it fails silently, every later guarantee is a belief |
| A5 | **The toolchain and the build**: developer machines, CI runners, `node_modules`, Expo prebuild | Each developer's machine; GitHub Actions; EAS later | The baseline's §1 names a poisoned build as the worst plausible breach, because it reaches every install |
| A6 | **Entitlement** | `capture.db` (ENT-1.1) | A revenue question more than a user-data one (`reviews/cso-review.md` §3.2), except where a forged interval corrupts A3 |

**Personal data, end to end, in M1** [I, from the wave plan and the tickets]:
- **It enters** as a platform visit event (iOS `CLVisit` through the location manager; CAP-1).
- **It lives** as a candidate row in `capture.db`. Its fields are `arrivedAt`, `departedAt`, `lat`, `lon`, `horizontalAccuracyM` and `capturedAt` (DATA-2.2's first-version face, #361).
- **It moves** across the bridge to JavaScript through `listCandidates`, and becomes a visit in `journal.db` when the user adopts it (DATA-16's `adoptCandidate`).
- **It dies** when it is adopted, discarded or expired (DATA-16). With D61, **both files also leave the phone inside the phone's own backups**: Apple can read iCloud Backup for UK users without Advanced Data Protection, and Google Drive backups are end-to-end encrypted only behind a screen lock (`reviews/cso-review.md` §5.1, retrieved 2026-09-28). The CEO decided this knowingly in D61, and this document records it as an accepted risk (§5.1 D5), not a finding.
- **No M1 code sends anything off the device.** There is no network code in the design (PRIV-8).

**Blast radius, unchanged from the architecture review.** There is no server, so no breach on Candour's side can expose many users at once, **except a malicious build or update**, which reaches every install [J]. So in M1 the supply-chain and guard-system threats (A4, A5) carry more weight than the data-at-rest threats, though both are real.

## 2. Who attacks this, and how

| # | Attacker | Route in M1 | Most relevant waves |
|---|---|---|---|
| T1 | **Someone close to the user**: the most realistic attacker for a location journal [J] | An unlocked phone; a shared or known backup account; a computer holding an unencrypted phone backup; recovering deleted rows from a copied file | W3, W5 (data at rest, deletion) |
| T2 | **Anyone who gets into the user's Apple or Google account**, or a provider under legal compulsion | OS cloud backups, which include both files under D61 | W3 (accepted risk) |
| T3 | **A compromised package, build tool or update channel** | Code that runs at install time, at commit time (ESLint configs and plugins are executable), at prebuild (Expo config plugins), or inside the app (autolinked native code; JavaScript in the same runtime as ours) | W1, W2 |
| T4 | **An AI agent writing code**, not malicious but optimising to make a check pass [J] | Suppressing a rule, moving code to a path the check does not read, building an API name from strings, editing a fixture or a config, or adding a fallback the design forbids | W1 (every bypass class), W3–W5 |
| T5 | **Hostile JavaScript inside our own process**, from a compromised production dependency | Calling the capture module's typed face directly, or reaching any native module through React Native's module registry | W2, W3 |
| T6 | **A device thief** with a locked phone | OS file encryption; file protection class | W3 |

**T4 is new since the architecture review, and it is the reason W1 exists.** D64 records the CEO's own words: *"I want rules to be strict so that there is a good and understandable separation when using AI to code."* A check an agent can step around is not strict. §3 is written against T4 first and T3 second.

**T5, stated plainly** [I]: the typed face is an architectural boundary between **our** modules. It is **not** an access control against code running in the same JavaScript runtime. A malicious production package could call `listCandidates()` as easily as our own store does. It has no network to send the result through, which is PRIV-8's point, but that holds mechanically only for our own code and, on Android, for the whole process (C5). **The defence against T5 is dependency review (C4) and keeping the production tree small,** not the face.

---

## 3. M1.W1: the B-strict guards and the ways round them

**What W1 builds** (SPK-21 #355, then MAINT-4 #308): ADR-0001's checks 1–16, each with a planted violation that must fail, and that failure re-proved in CI on every PR (`tools/prove-checks.ts`; wave plan §3.1). **The security-bearing checks** are 6 (only the store touches storage; D63 guard b), 9 (rules a comment cannot silence), 10 (guard files need a note), 11 (no network), and the capture-isolation script (CAP-1(b)). **The ones that only shape the code** (size, naming, arrow functions) matter here only because they share the same runner and configuration files.

**The bypass classes.** For each: how an author (T4) or a poisoned tool (T3) would get round the check, what already stops it, and what I ask for. "Fixture" means a folder under `tools/guard-fixtures/` that must fail, so that `prove-checks` turns the gap red on every PR.

| # | Bypass class | Example | Already covered by | Gap, and the condition |
|---|---|---|---|---|
| G1 | **Comment that disables a rule** | `// eslint-disable-next-line no-restricted-globals` | Check 9(a) (`no-restricted-disable`), 9(c) (`reportUnusedDisableDirectives: "error"`), and 9(b), CI's guard pass with `--no-inline-config` (C1) | **A rule-configuration comment** (`/* eslint no-restricted-imports: "off" */`) is not a *disable* comment, and `no-restricted-disable` is described as reporting `eslint-disable` comments [E, R12; I that it does not see configuration comments]. CI's guard pass still catches it, because `--no-inline-config` ignores both kinds [E, R11]. **Condition C25(a):** the local configuration also uses `@eslint-community/eslint-comments/no-use`, allowing only `eslint-disable-next-line` and `eslint-disable-line`, so the hook catches it too. Fixture for each kind |
| G2 | **Editing the configuration** | Adding `ignores: ["src/features/look/**"]`, or loosening a rule | Check 10 (`## CSO note`) and the protected list (C23) | Check 10 sees that a heading exists, not who wrote it. **The CEO's merge is the control** (rulings §2.3). **Tiered list**, rulings §2.3 |
| G3 | **A file the linter does not read** | Networking code in `src/features/x/helper.mjs`, or a `.cjs` file, when the lint `files` globs name only `**/*.{ts,tsx}` | Check 1 (folder allow-list) restricts folders, not extensions [I, from ADR-0001 §3] | **Condition C25(b):** the ESLint `files` globs and dependency-cruiser's extensions cover **every extension Metro will bundle**, and `check-structure.ts` rejects any other code extension under `src/` and `modules/*/` (JavaScript side). Fixture: a `.mjs` file in a feature calling `fetch` fails |
| G4 | **A computed global** | `globalThis["fe" + "tch"](url)`, or `const g = globalThis; g[name]()` | Check 11 bans the globals, *"including through `globalThis`"*. `checkGlobalObject` matches property names it can read [K, high confidence: a computed key built at run time cannot be read statically] | **Condition C26(a):** `no-restricted-syntax` bans computed member access on `globalThis`, `global`, `window` and `self`, plus `eval`, `new Function`, `Function(...)` and string arguments to `setTimeout` and `setInterval` (ESLint core `no-eval`, `no-new-func`, `no-implied-eval`). Fixture for each |
| G5 | **A dynamic import** | `require(name)` or `import(name)` where `name` is not a literal | `no-restricted-imports` and dependency-cruiser read literal specifiers only [K, high confidence] | **Condition C26(b):** `require` and `import()` take string literals only, everywhere in `src/` and `modules/*/index.ts`. Fixture |
| G6 | **Going round JavaScript's networking to the native module beneath it** | `NativeModules.Networking.sendRequest(...)`, the module React Native's own `XMLHttpRequest` calls [K, high confidence]; or `requireNativeModule("…")` for any Expo module | Not covered: check 11 names globals and packages, not the module registry | **Condition C26(c):** ban `NativeModules`, `TurboModuleRegistry`, `requireNativeModule` and `requireOptionalNativeModule` everywhere except `modules/capture/index.ts`. Fixture. This also narrows T5's easiest route to capture data |
| G7 | **A native API reached by name** | Swift `NSClassFromString("NSURL" + "Session")`, `perform(_:)`, `dlopen`/`dlsym`; Kotlin `Class.forName("java.net.URL")` | `check-network.ts` is a text match on API names (C3), so a name assembled from parts passes it [I] | **Condition C27:** `check-network.ts` and `check-capture-isolation.ts` fail on `NSClassFromString`, `NSSelectorFromString`, `objc_getClass`, `perform(`/`performSelector`, `dlopen`, `dlsym`, `Class.forName`, `getDeclaredMethod`, `getMethod(` and `System.loadLibrary` in `modules/` and `plugins/`. **This also covers C7's purpose on Kotlin:** reflection is how a `core` class would reach a `bridge` class without an import. Fixture for Swift and for Kotlin |
| G8 | **Hiding code where the checks do not look** | Real code placed under `tools/guard-fixtures/` (excluded from the real lint run, wave plan §3.1) and imported from `src/`; a `patches/` folder applied by `patch-package` | Check 1 rejects unregistered folders such as `patches/` [I, from ADR-0001 §3] | **Condition C28:** dependency-cruiser forbids any import from `src/` or `modules/` into `tools/`; Metro's resolver blocks `tools/` (PLAT-1's `metro.config.js` already drops it from the watch list, and **watching is not the same as resolving**, so it must be blocked from resolution too); and `patch-package`, or any `postinstall` in our own `package.json`, needs a CSO approval like any new dependency. Fixture for the import |
| G9 | **Switching off the runner** | `"check": "true"` in `package.json` | Nothing, as #355 specifies it | **The hook and CI call `node tools/check-all.ts`**, a Tier 1 file. CI runs `prove-checks` as a separate step (rulings §2.2, H7) |
| G10 | **Weakening the proof** | Setting a fixture's `expect.json` to `"fails": false`, or deleting a fixture | `prove-checks` fails when a check has no failing fixture (#355, *"Fixture contract"*) | Changing or deleting an existing fixture is **Tier 1** (rulings §2.3) |
| G11 | **Not running the hook** | `--no-verify`, `SKIP=`, a clone without `pre-commit install` | For agents, the MAINT-6 guard and the deny rules in `haunts/.claude/settings.json` [E, read at `dc9a0a0`]; for everyone, CI | **Residual risk, stated plainly:** while `haunts` is private on GitHub Free, a red CI cannot stop a merge (`traceability.yml` header). The control is the CEO not merging on red (D39) |
| G12 | **The tool fails quietly** | dependency-cruiser cannot parse TypeScript and falls back to `acorn-loose` [E, rulings R4]; typescript-eslint meets a TypeScript it does not support | Not covered as specified. TypeScript 7.0.2 breaks both (rulings §1.2) | **Condition T** (TypeScript 6.0.3), **fixture F1** (a TypeScript-only file crossing a boundary must fail `depcruise`), and **fixture F2** (the parser throws on an unsupported TypeScript), all in rulings §1.6 |
| G13 | **The storage opener becomes a general tool** | A store function `openDb(name)` lets a feature open `capture.db` by passing the name | Check 6 matches file-name **literals** (D63 guard b), so a name built at run time passes it [I] | **Condition C29 (DATA-2.1, W3):** `openDatabaseAsync` and `openDatabaseSync` may be called only in `core/store/open-journal.ts` and the venue opener, each with a string literal naming its own file. `no-restricted-syntax` enforces it, with a fixture. The store exports opened handles, never an opener |
| G14 | **SQL built from strings** | `` db.run(`DELETE FROM visit WHERE id = ${id}`) `` | ADR-0001 §2.3 states the rule (C8), and #360 and #361 cite it. **No check in ADR-0001 §3 names it, and #355's file list does not include it** [E, #355 body, read 2026-10-10] | **C8, to be written into SPK-21:** a guard-pass rule failing on a template literal or a concatenation as the first argument of `run`, `get`, `all`, `exec` or `prepare`, plus a native grep for string interpolation passed to `sqlite3_prepare*` or `sqlite3_exec`. Fixture for each language. **Flag to the CTO** (§6.2) |

**Three things the guards do not cover, and are not meant to** [I]:
- **Third-party code.** Lint and the native scans see only our files. That is C4 and C5's job (§4).
- **Type-level escapes.** Check 12 bans `any` and `@ts-ignore`. A cast does not change what a syntactic rule sees, so `(globalThis as any).fetch` is still caught by G4's rule.
- **Intent.** A check can stop a call it can name. It cannot judge whether a new native API that is not on the list reaches the network. That remains review: mine on every `needs:cso-review` PR, and the CTO's on every PR.

**MAINT-4 (W1, second).** The arrow-function rule is not a security rule, and ADR-0001 §4 says check 9(a) does not cover it. Its PR touches `eslint.config.js`, which is **Tier 2**: it needs a CSO note, and my review at its head commit is the approval. **Its fixtures are new folders, so they are Tier 2 as well.** I agree with the CTO's `needs:cso-review` label on it.

---

## 4. M1.W2: the Expo app shell and its first production dependencies (PLAT-1, #267)

**What W2 adds** (wave plan §3.2; #267): the Expo project at the repository root (`app.config.ts`, `metro.config.js`, `eas.json`, the app `tsconfig.json`), **every npm dependency M1 needs** (Expo SDK 58, React, React Native, Expo Router, `expo-sqlite`, `expo-build-properties`, `jest-expo`, React Native Testing Library), a `prepare` script, `docs/dependencies.md`, and a placeholder screen. **This is the first code that ships in the app,** and the first production dependency tree.

| # | Threat | Attacker | Control in place or planned | Condition |
|---|---|---|---|---|
| S1 | **Third-party code inside the app reaches the network, or reads capture data** (T5) | T3, T5 | PRIV-8's five layers. Only Android's release manifest without `INTERNET` is mechanical for third-party code (C5, subject to SPK-22). On iOS: review (C4) and device capture each release (C5) | **C4 starts here.** `docs/dependencies.md` lists **every** production package in the resolved lockfile and **every autolinked native module**, each with its declared network behaviour. I review the list at PLAT-1. **The CI check that fails on an unlisted dependency** is placed by the CTO as a later M1 story (wave plan §5, *"PRIV-8(d), the dependency check, as a story"*). **Until it lands, no ticket may add a production dependency**, which the wave plan already rules for W3–W5 (§4) |
| S2 | **Install-time and build-time code** (Expo config plugins run at prebuild; `app.config.ts` runs at build time; npm install scripts) | T3 | `--ignore-scripts` on every install (CI; `CLAUDE.md`). Exact pins and the lockfile (C16) | **C17 at PLAT-1:** `docs/dependencies.md` records every package with an install script. **Condition C30:** a `tools/check-lockfile.ts` (Tier 1 by its name) fails CI if any `resolved` URL is not `https://registry.npmjs.org/`, if any entry lacks `integrity`, or if a `hasInstallScript` entry appears that is not on the recorded list. It lands with PLAT-1 at the latest. **Flag to the CTO:** it is not in any ticket's files yet |
| S3 | **The hooks stop being installed** | T4 (by accident) | D41: *"once the Expo `package.json` exists (M1), its `prepare` step runs `pre-commit install"`*. #267 adds `"prepare": "pre-commit install"` | **It will not run.** npm runs `prepare` on `npm ci` and on a plain `npm install` [E, TM1]. With `ignore-scripts`, *"npm does not run scripts specified in package.json files"* [E, TM1]. `haunts` requires `npm ci --ignore-scripts` (`CLAUDE.md`; CI). **Condition C31:** keep `--ignore-scripts`, and do not drop it to make `prepare` work. Keep `pre-commit install` as an explicit, documented step, as `CLAUDE.md` already says. Make `check-all.ts` warn when `.git/hooks/pre-commit` is not pre-commit's. **Flag to the CTO:** D41's `prepare` idea and the baseline's `--ignore-scripts` cannot both hold. I recommend the second; dropping `--ignore-scripts` would let 392 development packages run install code, two of which have install scripts today (rulings §1.4) |
| S4 | **A secret or environment value compiled into the app** | T4 | Baseline: no secrets in `EXPO_PUBLIC_*` (`SECURITY.md`). C21: nothing from `process.env` into `extra` | **C21 has no ticket** [E, `gh issue list --search "C21"`, 2026-10-10: none]. It belongs to PLAT-1, where `app.config.ts` is born. The grep goes in a Tier 1 `tools/check-*.ts`. **Flag to the CTO** (§6.2) |
| S5 | **An update channel** | T3 | Baseline §8.4: EAS Update stays off without code signing. Check 11 bans importing `expo-updates` | **At PLAT-1:** `expo-updates` must not be in the resolved tree, and `docs/dependencies.md` says so. Banning the import does not stop autolinking if the package arrives as a dependency of another [K, moderate confidence on Expo's autolinking] |
| S6 | **Development tooling in the release binary** | T3 | None yet | **At PLAT-1:** the PR states whether `expo-dev-client`'s native code, or any dev-menu or dev-server code, is present in a production build, and what it can reach. Release builds are M5, so this is a record now and a check at the first release build (C5, C18). Release `Info.plist` must carry no App Transport Security exception [K, moderate: development builds may add one for the local bundler] |
| S7 | **Expo's ESLint configuration brings `eslint-plugin-import`** (the CTO's flag) | T3 | ADR-0001 §3, *"No import plugin"* | **Confirmed, and refused in advance** (rulings §1.7). Install `eslint-plugin-react-hooks` directly instead, decided at PLAT-1 |
| S8 | **Deep links trigger actions** | T1 (a link sent to the user), T3 | Expo Router makes every route reachable by URL once a scheme is set [K, high confidence] | **Condition C32, standing from M2:** no route performs a state change on navigation alone (adopt, discard, delete, export, a settings change). Each needs a user gesture on the screen. Nothing in M1 has such a route; the condition is recorded now so the first one is built right. **Flag to the CTO and UX** |
| S9 | **SDK 58 is a beta** (D53) | T3 (unreviewed code), and defects | D53: *"the CTO checks the beta's reported issues"* | **No security condition of mine.** The CEO accepted the beta in D53. My review at PLAT-1 adds one question: does any listed SDK 58 issue touch file protection, backup rules, `expo-sqlite`'s open path or the network? |
| S10 | **Android shell with no capture** | — | The capture module declares no Android implementation until Block 2 lifts (wave plan §3.3) | **Android's backup rules follow D61** (included). `android:allowBackup` defaults to true in Expo [E, `reviews/cso-review.md` S2]. Any change to that is a CEO decision, made in the `plugins/` backup file (ADR-0001 §2.3) |

**I agree with the CTO's `needs:cso-review` label on PLAT-1** (wave plan §8): the first production dependencies and the `prepare` script.

---

## 5. M1.W3–W5: the two files, the typed face, the ledger and the JS-free capture path

### 5.1 W3: `journal.db` (DATA-2.1, #360) and `capture.db` with the typed face (DATA-2.2, #361)

| # | Threat | Attacker | Control | Condition |
|---|---|---|---|---|
| D1 | **Files in a directory that is backed up or exposed** | T1, T2 | C9: `Library/Application Support/<bundle id>/`, cited by #360 and #361 [E, issue bodies, 2026-10-10] | None new. Applies as written |
| D2 | **Weak or unset file protection** | T6, T1 | iOS gives third-party app data Class C, *"Protected Until First User Authentication"*, by default. It *"protects data from attacks that involve a reboot"* [E, TM2] | **C10 is cited by no W3 ticket** [E, `gh issue view 360/361`, 2026-10-10: C8 and C9 only]. **Condition, to be added to both:** set `NSFileProtectionCompleteUntilFirstUserAuthentication` **explicitly** on each store file and its `-wal`, `-shm` and `-journal` companions, and test that each file carries it after first open, after a migration and after a checkpoint. The default happens to match, which is why this is cheap. Setting and testing it explicitly is what stops a later change (a new directory, a copy, a restore) from silently moving a file to Class D. `capture.db` **must** stay at Class C, because it is written in the background while locked (`reviews/cso-review.md` §3.3). **Flag to the CTO** (§6.2) |
| D3 | **Two SQLite copies corrupting one file** | Integrity and availability, no attacker | D63's three guards: (a) one connection on one serial queue (#361); (b) check 6 plus `check-capture-isolation.ts` (SPK-21); (c) native code never opens `venues.db` (#361) | **C29** (G13): the opener cannot be reused for another file |
| D4 | **SQL injection** across the bridge or in the store | T4, T5 | C8, cited by #360 and #361 | **The lint and grep must exist** (G14, SPK-21). On the native side, every command's arguments are bound parameters, never interpolated |
| D5 | **Both files in the phone's own backups** | T2 | **D61, the CEO's decision:** *"So the journal is not excluded from the OS's own backups."* PRIV-1's revised sentence (D66) is written to match | **Accepted risk, recorded and not reopened.** One security consequence follows: **deleted rows must not travel in those backups.** That is why `secure_delete` and the truncating checkpoint matter (rulings §3.2; **C24** for `journal.db`) |
| D6 | **Plaintext files** | T1, T6 | By design: DATA-1 (BLOCKING) requires every field to be legible with the `sqlite3` command-line tool, so no file-level encryption (`reviews/cso-review.md` §3.3) | **Accepted by design.** The protection is the OS's file encryption (D2) |
| D7 | **The typed face as an attack surface** (JavaScript into native) | T4, T5 | #361: *"validates every command (typed, bounded)"* | **Condition C33 (DATA-2.2):** the bounds are written down and tested. `EntitlementSnapshot.source` becomes a **closed set of values** (for example `'app-store' \| 'play'`, plus a test-only value compiled out of release), not a free `string`. Native validation rejects a snapshot whose interval ends before it starts; whose timestamps do not parse as ISO-8601 with an offset; whose dates fall before a fixed product epoch, or more than 24 hours after the device clock; or which has more than a stated number of intervals. Candidate ids passed to `markAdopted` and `discard` are checked as the identifier format native code issues. Unknown keys are refused. The change event carries **table names only, never row data**, as #361 already specifies. Each rule has a native test |
| D8 | **Hostile JavaScript in our own runtime reads capture data** | T5 | None mechanical (§2) | **Accepted residual, stated.** The defence is C4. **No `modules/capture` function returns more than its caller needs:** `listGaps` already takes a range, and later additions should follow that pattern [J] |
| D9 | **A migration that destroys data** | Integrity | #361: *"Migrations are append-only; a changed migration fails to apply"* | None new |

**I agree with the CTO** that DATA-2, DATA-2.1 and DATA-2.2 carry `needs:cso-review` (wave plan §8).

### 5.2 W4: sessions (SESS-1.1, #362), the entitlement ledger (ENT-1.1, #363), legibility (DATA-1, #195)

| # | Threat | Attacker | Control | Condition |
|---|---|---|---|---|
| E1 | **Forged entitlement** from JavaScript | T5, or the user | `recordEntitlement` is the only write path (#363). An import never grants entitlement (DATA-5(c)) | **Revenue, not user data** (`reviews/cso-review.md` §3.2). C33's validation bounds it. My earlier flag stands for ENT-2 (M3): prefer native reading of the platform's signed entitlement over trusting a JavaScript call |
| E2 | **Corrupted interval history.** Intervals are kept for years (SESS-9) and decide how a session is described, so one bad snapshot rewrites the past | T4, T5 | Snapshots are appended, never edited (#361, *"snapshot append"*) | **C33**, plus a native test that a malformed snapshot leaves the ledger's answer for every earlier instant unchanged |
| E3 | **"Unknown" lets capture run.** Capture records under *entitled* and *unknown* (#363), so for capture the ledger fails open | — | The CTO's rule: resolve *"in the customer's favour for capture while never taking money"* (`subscription-sizing-note.md` §3.1, cited in #363) | **I accept the fail-open, because the ledger only narrows capture; it never starts it** [J]. **Condition C36 (ENT-1.1, CAP-1):** no code path starts location monitoring, or overrides the user's own capture setting or the OS's location authorisation, because of a ledger answer. The recorder writes only for a visit the OS delivered, which requires the user's authorisation. Test: the ledger reports *entitled*, monitoring is off, and nothing starts |
| E4 | **Session overrides attached to the wrong thing** | Integrity | SESS-2(c): overrides anchor to visit identifiers, never to a session (#362, wave plan §3.4) | None. Security-neutral |
| E5 | **A field needs the app to read it** | — | DATA-1 test-only (#195): no BLOB, explicit offsets | None. It supports D6's design: the user can read their own data |

**I agree with the CTO's label on ENT-1.1** (wave plan §8). SESS-1.1, SESS-9 and DATA-1 need no CSO review [J]. They add no storage path, no bridge command and no dependency.

### 5.3 W5: the JS-free capture path (CAP-1, #8), deletion (DATA-16, #352), durability tests (SESS-9, #52)

| # | Threat | Attacker | Control | Condition |
|---|---|---|---|---|
| R1 | **JavaScript enters the recording path** (CTO Block 3) | T4 | C7 (`Core` is its own Swift module, #361), `check-capture-isolation.ts` (SPK-21), and CAP-1(a)'s end-to-end test (#8) | **C27** extends the isolation check to reflection. The CTO writes Block 3's lift after this PR and DATA-2.2 merge (wave plan §9, F2). I agree it should be lifted against its own condition, not on the design alone |
| R2 | **A write fails while the phone is locked, and the code "saves" the visit somewhere else** | T4 (with good intentions), T1 | Class C makes `capture.db` writable after first unlock (D2). Before first unlock after a reboot, it cannot be opened [I, from TM2] | **Condition C34 (CAP-1):** **no fallback store.** If `capture.db` cannot be opened or written, the visit is not written anywhere else: not `UserDefaults`, not a temporary file, not a queue persisted to disk. Once CAP-4 lands (M2), the miss becomes a capture gap. Test: simulate an open failure, and assert that no file is created or changed outside the store directory. **This is the most likely well-meant mistake on this ticket** [J] |
| R3 | **The debug instruments ship** (the Hermes-start marker and the synthetic-visit harness) | T3, and anyone able to drive the harness | #8: *"compiled out of release builds (PRIV-8: nothing that measures ships)"* | **Condition C35 (CAP-1):** both live behind `#if DEBUG`, in files of their own. The harness is never reachable by URL scheme, launch argument, notification or the typed face in any build. **From the first release-configuration build** (whichever comes first: CI's or M5's), a check asserts the harness's and the marker's symbol names are absent from the release binary. In W5, the PR shows one Release build with them absent |
| R4 | **Candidates outlive their window, or deleted rows can be recovered** | T1, T2 | DATA-16 (#352); C15 | **Rulings §3.1 and §3.2:** E1 (expiry on every start and every return to the foreground, not only *"once per process"* as #352 now says); E2 (a native ceiling, before release); `secure_delete = ON` and `wal_checkpoint(TRUNCATE)` after each deletion batch; no routine `VACUUM`; no FTS. **Disagreement with #352's wording, stated once:** the issue says *"run the reconcile and the expiry after migrating, once per process"*. On iOS a process can stay suspended for days and then resume, so a candidate past its window could be shown. E1 asks for the foreground as well. It costs one listener in `core/store` [J] |
| R5 | **Adoption across two files breaks** (a crash between inserting the visit and deleting the candidate) | Integrity | DATA-2's idempotent adoption through a unique `source_candidate_id`, plus the start-up reconcile; DATA-16(c) tests a kill between the two steps | None new |
| R6 | **The change event leaks data** | T5 | It carries table names only (#361) | Kept as part of C33 |

**I agree with the existing `needs:cso-review` labels on CAP-1 and DATA-16.**

---

## 6. Conditions: C1–C23 carried forward, and what is new

### 6.1 C1–C23 (`reviews/cso-review.md` §9.1): where each is discharged

"Discharged" means the wave and ticket whose merged work, with its fixture or test, makes the condition true. **"Not in W1–W5"** says where it goes instead, and why it cannot be earlier.

| # | Condition (short) | Discharged in | How, or why not in M1.W1–W5 |
|---|---|---|---|
| C1 | ESLint's inline configuration disabled for security rules in CI; `reportUnusedDisableDirectives` | **W1, SPK-21 (#355)** | `eslint.guard.config.js` run with `--no-inline-config` (check 9(b)); 9(a) and 9(c); fixtures for G1. Strengthened by C25(a) |
| C2 | Imported networking banned, not only the globals | **W1, SPK-21**; re-proved **W2, PLAT-1 (#267)** | Check 11's import bans, with fixtures by package name in W1. They are proved again against the real packages once PLAT-1 installs them. Strengthened by C26 |
| C3 | Wider native deny list in `check-network.ts` | **W1, SPK-21** | `tools/check-network.ts` with the `reviews/cso-review.md` §2 list, plus C27's reflection names |
| C4 | The dependency check covers the full lockfile and autolinked native modules | **Started W2, PLAT-1**; **the CI check is not in W1–W5** | PLAT-1 writes `docs/dependencies.md` across the resolved tree and autolinked modules, and I review it. **The failing CI check is a later M1 story** (wave plan §5, *"PRIV-8(d), the dependency check, as a story"*). It is safe to wait because no W3–W5 ticket may add a dependency (wave plan §4) |
| C5 | The `INTERNET` spike before M1 ends; iOS network capture as a release gate | **Not in W1–W5** | SPK-22 (ADR-0001 §6 item 5) decides PRIV-8(e) (wave plan §5). The iOS capture and App Privacy Report are release work, PRIV-8(f), in M5. **M1 cannot end without SPK-22** if C5 is to hold as written |
| C6 | Ciphertext-only transport if cloud backup is ever chosen | **Not in M1** | Only if the CEO chooses a cloud backup (`requirements.md` §12.1). Nothing in M1 networks |
| C7 | `ios/Core` its own Swift module, or a check on Bridge names | **W3, DATA-2.2 (#361)**, proved in **W5, CAP-1 (#8)** | `Capture.podspec` compiles `Core` as its own module (#361), and `check-capture-isolation.ts` comes from SPK-21. CAP-1(b) shows each failing on a planted reference. **Kotlin's half** (reflection, C27) goes with the Android wave |
| C8 | No SQL built by string interpolation, checked mechanically | **W1, SPK-21** (the checks); **W3, DATA-2.1 and DATA-2.2** (comply) | **Gap: no check in ADR-0001 §3 names it, and #355 does not list it** (G14). It must be added to SPK-21's guard configuration and native scan, with fixtures. #360 and #361 already cite C8 |
| C9 | Stores in `Library/Application Support/<bundle id>/` | **W3, DATA-2.1 (#360) and DATA-2.2 (#361)** | `open-journal.ts` and `CaptureStore.swift`. Both tickets cite C9 |
| C10 | iOS protection class set and tested on every store file and companion | **W3, DATA-2.1 and DATA-2.2** | **Gap: neither ticket cites C10** (D2). Each sets Class C explicitly and tests it on `.db`, `-wal`, `-shm` and `-journal`. QA confirms on a device |
| C11 | Android capture not `directBootAware`; no device-protected storage | **Not in W1–W5** | It applies to Kotlin, which waits for CTO Block 2 and SPK-02 (wave plan §6). It goes in the Android capture stories (M1.W8) |
| C12 | Export and backup staging files in the cache directory, deleted after the share sheet | **Not in M1.W1–W5** | No export or backup file is written in these waves. It goes with the tickets that write the export (DATA-3, DATA-4) and the backup file |
| C13 | HEAD-12's privacy cover gets a native home and a ticket | **Not in M1** | It has a ticket: HEAD-12 (#140) sits in **M4** [E, `gh issue list`, 2026-10-10]. That half of C13 is met. Its native home is decided when M4 is planned |
| C14 | Hostile-archive fixture for DATA-5 as well as DATA-15; the zip library approved by the CSO | **Not in W1–W5** | Import is not in these waves. It goes with DATA-5 and DATA-15, where the zip library comes to me for approval |
| C15 | `capture.db` retention: delete, never only flag | **W3, DATA-2.2** (`markAdopted` and `discard` delete); **W5, DATA-16 (#352)** (expiry, `secure_delete`, checkpoint, E1); **E2 before release** | Rulings §3. **Only fully discharged once E2 exists, or once the CEO accepts the residual in writing** |
| C16 | Lockfile discipline: `npm ci` in CI, and the dependency check reads the resolved lockfile | **W1, SPK-21** (`checks.yml` installs with `npm ci --ignore-scripts` from the lockfile, and the lockfile is resolved with the 7-day cooldown); **W2, PLAT-1** (C30) | Rulings §1.6 and §2.2 (H7) |
| C17 | Install scripts listed; a new one fails CI | **W1, SPK-21** (the PR lists `@parcel/watcher` and `unrs-resolver`); **W2, PLAT-1** (`docs/dependencies.md`, and C30 fails on a new one) | Rulings §1.4 |
| C18 | Native dependencies recorded (pods and Gradle) for each release build | **Started W2, PLAT-1**; **discharged at the first release build (M5)** | #267 starts `docs/dependencies.md` citing C18. Resolved pod and Gradle lists can only be archived per release build, and there are none in M1 |
| C19 | ESLint and commitlint run from the lockfile inside `pre-commit` | **W1, SPK-21** | The hook in rulings §2.2: `language: unsupported`, running `node tools/check-all.ts`, which calls the locally installed binaries. commitlint already does this (`docs/conventions.md` §9.1) |
| C20 | Maestro CLI pinned with a checksum | **Not in W1–W5** | Maestro arrives with the first end-to-end flow, not in M1.W1 (wave plan §8) |
| C21 | No `process.env` values in `extra` or `EXPO_PUBLIC_*`, enforced by a grep | **W2, PLAT-1** | **Gap: no ticket carries it** [E, issue search, 2026-10-10]. `app.config.ts` is born in PLAT-1, so the grep belongs there, in a Tier 1 `tools/check-*.ts`, with a fixture |
| C22 | No stored backup key at MVP; `ThisDeviceOnly` / non-exportable if ever stored | **Not in M1** | It belongs to SPK-06 and the backup work |
| C23 | New guard files join the baseline's protected list (CEO approval) | **W1, SPK-21**, with **the CEO's approval** | Rulings §2: two tiers, written into `SECURITY.md` and `CLAUDE.md` rule 3, and enforced by check 10 as a tripwire |

**Count:** 23 conditions. **Discharged inside W1–W5:** C1, C2, C3, C7, C8, C9, C10, C16, C17, C19, C21, C23 (12). **Started in W1–W5, finished later:** C4, C15, C18 (3). **Not in W1–W5:** C5, C6, C11, C12, C13, C14, C20, C22 (8). **Three of the twelve need a ticket edit first** (C8, C10, C21; §6.3).

### 6.2 New conditions from this threat model

Each is cheap: a lint rule, a fixture, a few lines of native code or a test. I estimate the set at **1–2 days, inside the tickets named, with no running cost** [J].

| # | Condition | Ticket (wave) | From |
|---|---|---|---|
| T | `typescript` 7.0.2 → 6.0.3, so the lint and dependency tools can install and run | SPK-21 (W1) | Rulings §1.2 |
| F1, F2 | dependency-cruiser must fail on a TypeScript-only boundary crossing; typescript-eslint must throw on an unsupported TypeScript | SPK-21 (W1) | Rulings §1.6; G12 |
| H1–H7 | The hook and CI proofs | SPK-21 (W1) | Rulings §2.2 |
| C24 | `secure_delete = ON` on `journal.db` | DATA-2.1 (W3). **Recommended; the CTO owns the decision** | Rulings §3.2 |
| C25 | (a) `eslint-comments/no-use`, allowing only `-next-line` and `-line` disables; (b) lint and dependency-cruiser cover every extension Metro bundles, and other code extensions are rejected | SPK-21 (W1) | G1, G3 |
| C26 | Ban computed global access, `eval` and its kin, non-literal `require`/`import()`, and `NativeModules`/`TurboModuleRegistry`/`requireNativeModule` outside the capture face | SPK-21 (W1) | G4–G6 |
| C27 | Native reflection names fail the scans (Swift and Kotlin) | SPK-21 (W1) | G7 |
| C28 | No import from `src/` or `modules/` into `tools/`; Metro blocks `tools/` from resolution; `patch-package` or a root `postinstall` needs CSO approval | SPK-21 (W1) and PLAT-1 (W2) | G8 |
| C29 | One opener per file: `openDatabase*` only in its owning file, with a literal argument | SPK-21 (the rule and its fixture) or DATA-2.1 (W3): **the CTO places it** | G13 |
| C30 | `tools/check-lockfile.ts`: registry host, integrity, install-script allow-list | PLAT-1 (W2) at the latest | S2 |
| C31 | Keep `--ignore-scripts`; `pre-commit install` stays an explicit step; `check-all.ts` warns when the hook is not installed | PLAT-1 (W2) | S3 |
| C32 | No route changes state on navigation alone | Standing, from the first such route (M2) | S8 |
| C33 | The typed face's bounds, written down and tested; `source` a closed set; event carries no row data | DATA-2.2 (W3) | D7, E2 |
| C34 | No fallback store in the recording path | CAP-1 (W5) | R2 |
| C35 | Debug instruments under `#if DEBUG`, unreachable from outside, and absent from the release binary by check | CAP-1 (W5); the check at the first release build | R3 |
| C36 | A ledger answer never starts capture or overrides the user's setting or the OS's authorisation | ENT-1.1 (W4), CAP-1 (W5) | E3 |
| E1 | Expiry on every start and every return to the foreground | DATA-16 (W5) | Rulings §3.1 |
| E2 | Native expiry ceiling at CONF-15's maximum | Before release; **needs the CEO to set the maximum** | Rulings §3.1 |

### 6.3 Flags, each to the seat that holds the decision

- **CEO:** the CSO note for SPK-21 (rulings §2). Later, a maximum for the candidate-expiry setting (E2), when the PM/BA proposes one.
- **CTO, before SPK-21 starts:**
  - condition T (the TypeScript version is your toolchain call);
  - `node tools/check-all.ts` as the hook and CI entry (**my one disagreement with #355's interface**, stated in rulings §2.2);
  - add `tools/check-all.ts` and `SECURITY.md` to #355's files, and widen its `CLAUDE.md` entry to rule 3;
  - write C8's checks into #355 (G14);
  - place C25–C29.
- **CTO, before W2 and W3:**
  - add **C10** to #360 and #361;
  - add **C21** and **C30** to #267;
  - choose between D41's `prepare` and `--ignore-scripts` (C31; I recommend keeping `--ignore-scripts`);
  - replace `eslint-config-expo` at PLAT-1 (S7);
  - **#352's "once per process"** against E1 (my second disagreement, stated once in §5.3 R4).
- **PM/BA:** a maximum for CONF-15's setting (E2).
- **UX and CTO:** C32, when the first state-changing screen is designed.
- **QA:** C10 on a device at W3; C35's release-binary check at the first release build.

## 7. Where I looked, and what would overturn this

**Read in full:** the wave plan (candour PR #31); ADR-0001; `reviews/cso-review.md`; the CSO rulings of the same date; `requirements.md` v1.4 rows CAP-1, CONF-15, SESS-9, ENT-1, DATA-1, DATA-2, DATA-16, PRIV-8 and PLAT-1; decision entries D29, D32, D40, D41, D43, D53, D61, D63, D64, D65 and D66. **`haunts` at `dc9a0a0`:** `CLAUDE.md`, `SECURITY.md`, `.pre-commit-config.yaml`, `package.json`, `package-lock.json`, `tsconfig.json`, `.github/dependabot.yml`, `.github/workflows/traceability.yml`, `docs/conventions.md` §9, `.claude/settings.json` and `.claude/hooks/haunts-guard.py` (searched). **Issues:** #355, #360 and #361 (searched for C-numbers), #361 and #363 in full, and the CTO sections of #8, #352 and #267.
**Not read:** the bodies of #362, #195, #52 and #308 beyond the wave plan's description of them; the SDK 58 release notes; any Expo source. **No code was run against `haunts`**, and no M1 code exists yet. This threat model is about a design and a plan, and must be revisited against what merges (§9).

**What would overturn its main findings:**
- **Risk 1 (guard bypass):** a demonstration that the checks as SPK-21 builds them fail on each of G1–G14's examples without the new conditions. I would then withdraw the conditions that turn out redundant.
- **Risk 2 (supply chain):** a mechanism that denies sockets to third-party code on iOS. I know of none [K, high confidence], and finding one would let C5's iOS half become a control instead of evidence.
- **Risk 3 (retention):** the platforms bounding background visit delivery to an app that is never opened (rulings §3.1), or a CEO decision to exclude both files from OS backups, which would reduce, though not remove, the case for `secure_delete`.
- **Any [K] claim in §8's list** found wrong at retrieval. Each is labelled where it is used.

## 8. Evidence register

This document's own sources are numbered **TM**. A bare **R**-number points to the rulings' register (`cso-m1-w1-rulings.md` §5). Facts carried from `reviews/cso-review.md` say so where they are used, with that review's retrieval date (2026-09-28); they were not re-retrieved today unless listed here.

| # | Claim | Source, retrieved 2026-10-10 |
|---|---|---|
| TM1 | npm runs `prepare` on `npm ci` and on a local `npm install` with no arguments; with `ignore-scripts`, *"npm does not run scripts specified in package.json files"* | [npm docs, `scripts.md` @v11.6.0](https://github.com/npm/cli/blob/v11.6.0/docs/lib/content/using-npm/scripts.md); [`ignore-scripts` definition @v11.6.0](https://github.com/npm/cli/blob/v11.6.0/workspaces/config/lib/definitions/definitions.js) (the local npm is 11.19.0; the docs version read is 11.6.0) |
| TM2 | iOS Data Protection classes; Class C, *"Protected Until First User Authentication"*, is *"the default class for all third-party app data not otherwise assigned"* and *"protects data from attacks that involve a reboot"* | [Apple Platform Security, Data Protection classes](https://support.apple.com/guide/security/data-protection-classes-secb010e978a/web) |
| TM3 | `haunts` repository facts: `package.json` (`typescript` 7.0.2), `CLAUDE.md` (`npm ci --ignore-scripts`; security rules), `SECURITY.md` (the guard-rails list), `.pre-commit-config.yaml`, `traceability.yml` (CI install; GitHub Free cannot block a merge), `.claude/settings.json` deny rules | Local reads of `deopea-david/haunts` at `dc9a0a0` (worktree `.claude/worktrees/cso-m1`) |
| TM4 | Ticket facts: #355's file list and interface; #360 and #361 cite C8 and C9 but not C10; #361's typed face and validation note; #363's three-state rule; #8's debug instruments; #352's *"once per process"*; #267's `prepare` and `docs/dependencies.md`; no issue mentions C21; HEAD-12 is #140 in M4 | `gh issue view` and `gh issue list --search` on `deopea-david/haunts`, 2026-10-10 |
| TM5 | The waves, files, labels and requests to the CSO | `products/haunt/architecture/m1-wave-plan.md`, CTO, 2026-10-09 (candour PR #31, worktree `cto-m1-waves`) |
| R1–R17 | Registry, source and documentation facts on the SPK-21 tools, Expo's ESLint configuration and SQLite | `cso-m1-w1-rulings.md` §5 |

**[K] claims carried, each to be upgraded before it anchors a ticket:**
- `checkGlobalObject` cannot read keys computed at run time (G4);
- `no-restricted-imports` and dependency-cruiser read literal specifiers only (G5);
- React Native's `XMLHttpRequest` is built on `NativeModules.Networking` (G6);
- Expo Router makes every route reachable by URL once a scheme is set (S8);
- autolinking includes a package that arrives transitively (S5);
- development builds may add an App Transport Security exception (S6);
- no mechanism on iOS denies third-party code sockets (§7).

## 9. Revisit when

- **Each wave's merge.** I review the merged interfaces against this model at the W3 and W5 gates the wave plan defines, and record the result here.
- **CTO Block 2 lifts** (SPK-02): the Android threats (C11, C27's Kotlin half, the foreground service, exported components) join this model before the Android wave is planned.
- **A production dependency is added** beyond PLAT-1's.
- **The CEO revisits D61**, or chooses a cloud backup (C6).

## 10. Change log

| Date | Change |
|---|---|
| 2026-10-10 | First version (CSO), alongside the M1 wave plan. C1–C23 mapped; C24–C36, T, F1–F2, H1–H7 and E1–E2 added |
