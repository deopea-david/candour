# Guard tooling options: six suggestions to replace SPK-21's scripts with tools, each tested

**Seat:** CTO · **Date:** 2026-10-11 · **Status:** A tested build-vs-buy note for the CEO to choose from. **Nothing here changes ADR-0001, ADR-0002, SPK-21 (PR #367) or any ticket.** No file on PR #367's branch was touched.
**Asked by:** the CEO, 2026-10-11, through the Coordinator. Authority: his "Yes" to *"shall I commission … The CTO: test each of the five suggestions on planted violations, as it did for the Ox comparison. Opus, because these are unfamiliar tools."* A sixth suggestion was added mid-run: *"Can we have a custom syntax rule for oxlint to error on oxlint disables?"*
**Template:** `pipeline/templates/` has no build-vs-buy template. This follows `lint-layer-comparison.md`.
**Evidence tags** follow `pipeline/evidence-standard.md`. **"Tested"** means a planted violation run on 2026-10-11 in throwaway directories in my scratch space, never in a checkout and never committed. The register in §10 lists every retrieved source as R1–R14.

Provenance: CTO · opus (Opus 5.5) · effort high · 2026-10-11

**What I tested against.**
- **The code:** PR #367 at `252f838` (`ci/SPK-21-b-strict-scaffolding`). I exported it with `git archive` into scratch and installed its lockfile with `npm ci --ignore-scripts`. **Baseline:** `node --test tools/prove-checks.ts` passed **145 of 145** there [E, tested].
- **The planted violations:** SPK-21's own fixtures under `tools/guard-fixtures/`. Where they left a gap, I added probes of my own, each named `p-*`, `s-*`, `k-*`, `st-*` or `x-*` below. **I mark those as mine, because they are not proofs the CSO has accepted.**
- **The tools:**
  - **npm:** `oxlint` 1.86.0 and `oxlint-plugin-eslint` 1.86.0, installed with `--ignore-scripts --before=2026-10-04`, so both are at least 7 days old (D43).
  - **Release binaries,** each downloaded into its own empty folder:
    - **SwiftLint 0.65.1** (`portable_swiftlint.zip`, published 2026-08-21);
    - **ktlint 1.8.0** (2025-11-14);
    - **detekt-cli 1.23.8** (`-all.jar`, 2025-02-21).
  - **Runtimes:** dependency-cruiser 18.5.0 from the PR's lockfile. Node 24.21.0, Apple Swift 6.4 and Zulu JDK 17.0.19 on macOS arm64.

---

## 1. The answer, for the CEO

| # | Suggestion | Outcome |
|---|---|---|
| 1 | SwiftLint and ktlint for the native halves of `check-capture-isolation.ts` and `check-network.ts` | **Partly covered for Swift; not covered for Kotlin. Neither script can be deleted.** SwiftLint matched the script on **all 7 Swift fixtures** with 55 lines of YAML, but it misses one SQL shape. A single `// swiftlint:disable` comment silences it, and it **skips its custom rules and passes** when SourceKit is unavailable. ktlint has no rule you can configure for this. Custom rules mean writing Kotlin, compiling a JAR and building it with Gradle. detekt caught **1 of the 8 Kotlin fixtures** (3 with JDK type resolution). Neither tool reads Objective-C, C or Java. |
| 2 | Oxlint for `check-structure.ts` (naming, barrels, folders) | **Partly covered.** File naming is already Oxlint's (`unicorn/filename-case`). With `oxlint-plugin-eslint` selectors, Oxlint also passed checks 14 (hook and screen names), 15 and 16, plus the folder list **for code files**. **Not covered:** non-code files in unknown folders (tested: they pass), the README feature list, G15, C37, 9(d) and C25(b). The script stays. At most about 50 of its 217 lines could go. |
| 3 | `CLAUDE.md` instead of the suppression scan and guard pass | **Facts only; the CSO rules (§5).** The CSO's position (rulings §0.9) is: keep the guard pass; the scan may go on conditions S1–S3. |
| 4 | `oxlint-plugin-eslint` for `guard-plugin.ts` and `style-plugin.ts` | **Covered with config, with two gaps. I recommend against a wholesale move.** The package is **first-party**: the Oxc project publishes it with every Oxlint release, under MIT, with no dependencies and with provenance. **All 17 PR fixtures for the two plugins passed.** Of my 24 probes, it **missed 2 the plugin catches**: a type cast around the SQL, and destructuring from a cast `globalThis`. **The config grows to 294 selector entries**, because an Oxlint override *replaces* a rule's whole list rather than adding to it. |
| 5 | dependency-cruiser for `check-core.ts` | **Not covered.** 8(a), the manifest, and 8(c), the 30% budget, cannot be expressed in it. Its dependents-count rule is a different rule from 8(b): it **passed a file used by only one feature** (through two of that feature's files) and **failed a legitimate transitive share** [E, tested]. |
| 6 | An Oxlint rule that errors on disable comments | **Works, but can be silenced in the normal lint pass.** A bare `/* oxlint-disable */`, or a file-level disable naming the rule, silenced it and the `fetch` together, and the build **passed** [E, tested]. **Inside the guard pass's comment-stripped copy, it judged 29 of 29 cases correctly** [E, tested]. That copy is the one place no comment can reach. |

**My recommendation** [J, moderate confidence], with the reasons in §8:

1. **Adopt suggestion 6, placed in the guard pass.** Add a `guard/no-disable` rule of about 30 lines to `guard-plugin.ts`. Run the guard pass in the hook as well as in CI, and **delete `check-suppressions.ts`** (123 lines).
   - It keeps everything the scan protected: the allow-list, the required reason, and the non-guard rules the CSO flagged to me.
   - The parser now recognises each comment shape, so the scan's own shape-matching code is no longer needed.
   - **No new dependency.** It needs the CSO's note and the CEO's approval (Tier 1).
2. **Keep `guard-plugin.ts`.** Its 372 lines sit on the security path. They see through casts, which selectors cannot do without one entry per shape. They avoid a 294-entry config whose overrides fail silently.
   - **Optional:** replace only `style-plugin.ts` (82 lines) with 12 selectors. That is worth doing only if the CSO approves `oxlint-plugin-eslint` for another reason.
3. **Keep the native scripts, `check-structure.ts` and `check-core.ts`.** No tool tested removes them. Two would add toolchains (a Swift binary and SourceKit, and a JVM jar), each with its own suppression syntax to police.

**Our own code this removes:** about **90 lines net** (−123 for the scan, +about 30 for the rule), or about 160 if `style-plugin.ts` also goes. **New toolchains:** none.

---

## 2. Suggestion 1: SwiftLint and ktlint (and detekt) for the native scans

### 2.1 What the two scripts do today

`check-network.ts` (106 lines) and `check-capture-isolation.ts` (146 lines) are **text scans** with regular expressions over `modules/` and `plugins/`. They cover `.swift`, `.m`, `.mm`, `.h`, `.c`, `.cpp`, `.kt`, `.kts` and `.java` [E, R1].
- **C3:** network APIs.
- **C27:** reflection and dynamic loading.
- **DATA-2(d):** which file may name which database. This one also scans TypeScript.
- **CAP-1(b):** `ios/Core` and android `core` import no bridge, Expo or React.
- **CAP-8(c):** notifications only in `modules/capture/`.
- **C8 (native half):** no interpolated or concatenated SQL. It uses a small argument splitter that handles nested brackets.

A text scan cannot be silenced by a comment, because it honours none.

### 2.2 Results, check by check

**Key:** **covered (tested)**; **covered with config**; **partly covered** (says what stays a script); **not covered**. Fixture names are SPK-21's; `s-`/`k-` probes are mine.

| Check | SwiftLint 0.65.1 (regex `custom_rules`) | ktlint 1.8.0 | detekt 1.23.8 |
|---|---|---|---|
| **C3** network APIs | **Covered with config.** `11-native-swift` failed. My probes `s-import-network`, `s-comment` and `s-string` failed, as the script does | **Not covered.** Stock ktlint exited 0 on `11-native-kotlin`. No configurable rule exists; a custom rule is a compiled Kotlin JAR [E, R7] | **Partly covered.** `ForbiddenImport` caught `k-import-okhttp` and `k-import-httpurl`. **It missed `11-native-kotlin` itself**, which uses a fully qualified `okhttp3.OkHttpClient()` with no import. **Stays a script** |
| **C27** reflection | **Covered with config.** `c27-swift` and `c27-isolation-swift` failed | Not covered | **Partly covered.** `ForbiddenMethodCall` caught `Class.forName` and `URL.openConnection` **only with type resolution on a JDK classpath**. Without `--classpath` the rule ran and exited 0 |
| **DATA-2(d)** database names | **Covered with config, path-scoped.** `6-journal-db-swift` and `s-capture-db-elsewhere` failed; `s-ok-capture-db` passed | Not covered | **Not covered.** No string-literal rule. `6-capture-db-kotlin` and `6-journal-db-kotlin` passed. The **TypeScript half** (`6-capture-db-ts`) is outside every native tool's scope: **stays a script** |
| **CAP-1(b)** core imports | **Covered with config.** `cap1-core-swift` and `s-attr-import` failed; `s-ok-bridge-expo` passed | Not covered | **Covered with config.** `cap1-core-kotlin` failed; `k-core-ok` and `k-bridge-expo-ok` passed. **Needs its own detekt run**: 1.23 allows one path scope per rule per config |
| **CAP-8(c)** notifications | **Covered with config.** `cap8-notification-swift` failed; `s-ok-capture-notification` passed | Not covered | **Partly covered.** `k-notification-import` failed. **The fixture `cap8-notification-kotlin`, with no import, passed.** A third run is needed for the scope |
| **C8** SQL from strings | **Partly covered.** `c8-swift`, `s-sql-multiline` and `s-sql-concat` failed. **`s-sql-nested` (a call with a comma inside the first argument) passed.** A regex cannot balance brackets; the script's splitter can | Not covered | **Not covered.** `c8-kotlin` passed |
| **Objective-C, C, C++, Java** (`.m`, `.mm`, `.h`, `.c`, `.cpp`, `.java`) | **Not covered.** SwiftLint reads only `.swift` (`s-objc`) | Not covered | **Not covered.** `k-java-file` passed |

**Counts** [E, tested]:
- **SwiftLint:** 7 of 7 Swift fixtures, and 12 of 14 of my Swift probes. It missed `s-sql-nested`, and it never read `s-objc`: that probe "failed" only because SwiftLint found no `.swift` file to lint.
- **detekt without type resolution:** 1 of 8 Kotlin fixtures. **With a JDK classpath:** 3 of 8.
- **ktlint:** 0.
- **The scripts today:** all 15 fixtures and all 22 probes.

### 2.3 What the tested coverage costs

- **SwiftLint can be silenced by a comment.** Both `// swiftlint:disable:next c3_apple_network` and `// swiftlint:disable all` above a `URLSession` gave exit 0 [E, tested]. `swiftlint lint --help` has no switch to ignore them [E, tested].
  - **A mitigation works:** a custom rule matching `swiftlint:(disable|enable)` fired on all three spellings I tried, including one that names the rule itself [E, tested].
  - **That rule is still one more thing the CSO's suppression rules would have to cover** [I].
- **SwiftLint fails open without SourceKit.** With `--disable-sourcekit` it printed *"Skipping enabled rule 'custom_rules' because it requires SourceKit"* and **exited 0** on a `URLSession` [E, tested].
  - **Linux:** SourceKit comes from a Swift toolchain, at `/usr/lib/libsourcekitdInProc.so` or the path in `LINUX_SOURCEKIT_LIB_PATH` [E, R5].
  - **The CI runner:** GitHub's `ubuntu-24.04` image ships Swift 6.4 [E, R12]. So CI need not move to macOS. **I did not test on Linux** (no Linux machine here).
  - **The guard against fail-open is a must-fail fixture**, as G12 already requires for Oxlint's plugins [I].
- **detekt fails open in two ways I hit while testing.**
  - `--disable-default-rulesets` **switched off the `style` rule set, which holds `ForbiddenImport`, and every fixture passed** [E, tested].
  - `ForbiddenMethodCall` needs type resolution, which runs only when `--classpath` is given; without it the rule is quiet [E, tested; R9 marks it "Requires Type Resolution"].
  - **Its documentation site describes 2.0:** `forbiddenImports` is rejected by 1.23.8, which wants `imports` [E, tested; R9].
  - **`@file:Suppress("ForbiddenImport")` silenced it** [E, tested].
- **Coverage for Android APIs needs the Android classpath.** `NotificationCompat`, `WebView` or OkHttp used by fully qualified name can only be caught by `ForbiddenMethodCall` with `android.jar` and the dependencies on the classpath. That means wiring detekt into the Gradle build [I, from the two results above].

### 2.4 The tools

| | SwiftLint | ktlint | detekt |
|---|---|---|---|
| **Version tested** | 0.65.1 (2026-08-21) | 1.8.0 (2025-11-14); 2.0.0-ALPHA-4 is out | 1.23.8 (2025-02-21) is the latest stable; 2.0.0-alpha.6 (2026-08-04) |
| **Licence** | MIT | MIT | Apache-2.0 |
| **Maintainer, activity** | `realm` org; last commit 2026-09-28; 19.7k stars; 529 open issues | `ktlint` org (moved from Pinterest); last commit 2026-10-09; 6.7k stars | `detekt` org; last commit 2026-10-08; 7.1k stars. **Stable line 20 months old** |
| **Footprint** | 37 MB universal macOS binary (12 MB zip); Linux arm64 zip 64 MB | 71 MB self-executing JAR | 70 MB `-all` JAR |
| **CI needs** | SourceKit: a Swift toolchain. Already on `ubuntu-24.04` [E, R12]; else macOS runners at **$0.062 a minute against $0.006 for Linux** [E, R11] | A JVM (JDK 17 is the default on `ubuntu-24.04` [E, R12]) | A JVM; Android classpath for type resolution |
| **Custom rules** | Regex rules in YAML, with `included`/`excluded` path regexes [E, R5]. Swift-language rules need a Bazel build of SwiftLint [E, R5] | **A Kotlin `RuleSetV2Provider` compiled into a JAR with Gradle, loaded by `-R`** [E, R7] | Kotlin rule sets, also compiled; `ForbiddenImport`, `ForbiddenMethodCall` and others built in |
| **Scan only `ios/Core`?** | **Yes.** `included: '/modules/capture/ios/Core/'` scoped CAP-1(b) correctly [E, tested] | n/a | Yes, `includes` glob; one scope per rule per config |
| **Supply chain** | GitHub release asset, outside the npm lockfile and its integrity hashes. SHA-256 is published only for the Bazel asset [E, R4] | GitHub release with a `.asc` signature [E, R6] | GitHub release jar [E, R8] |

**Verdict on suggestion 1** [J, high confidence]: **neither script goes.**
- **Kotlin:** nothing tested does the Kotlin half without writing Kotlin.
- **Other languages:** nothing reads Objective-C, C or Java.
- **TypeScript:** nothing covers DATA-2(d)'s TypeScript half.
- **Swift:** SwiftLint duplicates the script's Swift regexes almost exactly, at the price of a second toolchain, a comment syntax to police, and a fail-open mode.
- **What would overturn it:** Haunt's Swift growing large enough that SwiftLint's style rules earn their place on their own merits (they are not guard rules). Or the native modules moving to Swift-only with Objective-C, C and Java banned by `check-structure.ts`, which would shrink the script to its Kotlin half.

---

## 3. Suggestion 2: Oxlint for `check-structure.ts`

### 3.1 What I tested

`check-structure.ts` (217 lines) also exports the walker and helpers every other `check-*.ts` uses, and it runs **first**, before any Ox tool loads (G15, H8) [E, R1]. I built a candidate on Oxlint's `unicorn/filename-case` plus `oxlint-plugin-eslint`'s `no-restricted-syntax`. It uses selectors such as `Program:not(:has(…))`, scoped by `overrides` globs taken from `tools/structure.json`.

**One limit shaped the test.** The same plugin package loaded twice under two names is one plugin. The second name was *"not found"*, even through a different specifier resolving to the same file [E, tested]. **So each concern needs its own Oxlint run and configuration.** I used three: folders, names and barrels.

| Check | Result | Evidence |
|---|---|---|
| 14 file names kebab-case | **Covered (tested), already Oxlint's** today | `14-filename` |
| 14 `use-*.ts` exports `useX`; `*-screen.tsx` exports `XScreen`, and only those do | **Covered with config** | `14-hook-name`, `st-screen-misnamed`, `st-screen-empty` failed; `1-clean` passed |
| 14 folder names kebab-case | **Partly covered:** caught only because the folder list catches any unknown folder. Under `anyDepthBelow` (`modules/capture/android/**`) nothing would | `14-folder-case` failed via check 1 [I for the android case] |
| 15 one strings file per feature | **Covered with config** | `15-strings` |
| 16 no barrels; no file that only re-exports | **Covered with config.** Oxlint's native `oxc/no-barrel-file` counts only `export *` [E, R1 schema], so selectors were needed | `16-barrel`, `16-reexport-file`, `st-export-star` failed; `st-feature-index-ok`, `st-mixed-ok` passed |
| 1 folder allow-list | **Partly covered: code files only.** **A `.svg` or `README.md` in an unknown folder passed** (exit 0) once any code file existed elsewhere [E, tested]. **Stays a script** | `1-folder`, `1-folder-subfolder` failed; `st-folder-noncode`, `st-folder-md` passed when they should fail |
| 1 feature list matches `src/features/README.md` | **Not covered** (a Markdown file) | — |
| G15 nested or JS Ox configs; C37 `.eslintignore`; 9(d) known-violations file and `--ignore-known` | **Not covered.** They are configuration files, and G15 must run before Oxlint loads anything | — |
| C25(b) code extensions lint does not read | **Not covered**, by definition: Oxlint cannot report a file it does not read | — |

**Verdict** [J, high confidence]: **keep the script.**
- About 50 lines (checks 14, 15 and 16) could move.
- The cost would be three extra Oxlint configurations and runs, plus `oxlint-plugin-eslint`.
- The other 160-odd lines, and the helpers, stay either way.
- **What would overturn it:** an Oxlint rule that lints paths rather than files, or a reason to adopt `oxlint-plugin-eslint` anyway. Then moving 14, 15 and 16 costs little.

---

## 4. Suggestion 4: `oxlint-plugin-eslint` for the guard and style plugins

### 4.1 What the package is

- **Who publishes it.** It is published by the Oxc project itself, from `oxc-project/oxc`, `npm/oxlint-plugin-eslint`. The author is *"Boshen and oxc contributors"*. Its only npm maintainer is `boshen` [E, R2].
  - **Publication:** by GitHub Actions as an npm trusted publisher, with an SLSA provenance attestation for 1.86.0 [E, R2].
- **How it is maintained.** It ships **in the same release commit as Oxlint**: `release(apps): oxlint v1.86.0 && oxfmt v0.71.0` on 2026-09-28, and the same for 1.83–1.87 [E, R3]. 35 versions since 2026-03-10; 1.87.0 on 2026-10-05 [E, R2].
  - **I judge it maintained**, for as long as Oxlint is [I].
- **What it contains.** MIT, **no dependencies**, no install scripts, 2.9 MB, 292 rule files [E, tested]. Its README: *"ESLint's built-in rules as an Oxlint plugin"*; rules are prefixed `eslint-js/` [E, R2]. `index.js` states that the rules are ESLint's code, copied at a pinned ESLint commit [E, tested].
- **The caveat it does not remove.** It **is** an Oxlint JS plugin, and Oxc's documentation says *"JS plugins are currently in alpha"* [E, R10]. **G12's must-fail fixtures apply to it exactly as to our plugin.** The difference is who maintains the code: Oxc rather than us.

### 4.2 Results

I generated a candidate `oxlint.guard.json` with every `guard/*` rule and `style/core-exports` rewritten as `eslint-js/no-restricted-syntax` selectors. I ran it beside today's configuration on the same cases [E, tested].

| Rule the plugin replaces | Selector result | PR fixtures | My probes |
|---|---|---|---|
| `guard/no-clock` | **Covered with config** | `5-new-date` fail, `5-new-date-arg` pass | `p-call-date`, `p-globalthis-date` fail |
| `guard/no-sql-strings` | **Partly covered** | `c8-template`, `c8-concat` fail; `c8-ok` pass | `p-sql-join`, `p-sql-paren`, `p-sql-bare`, `p-sql-computed` fail. **`p-sql-cast` (`` db.runAsync(`… ${id}` as string) ``) passed; the plugin catches it** |
| `guard/no-computed-global` | **Partly covered** | `c26a-computed`, `c26a-cast` fail | `p-window-computed`, `p-destructure-plain` fail. **`p-destructure-cast` (`const { [k]: f } = globalThis as unknown as …`) passed; the plugin catches it** |
| `guard/literal-import` | **Covered with config** | `c26b-import` fail | `p-import-template-ok` pass |
| `guard/no-native-registry` | **Covered with config** | `c26c-namespace` fail, `c26c-allowed` pass | `p-require-registry`, `p-require-destructure` fail |
| `guard/db-opener` | **Covered with config, slightly stricter** | `c29-opener`, `c29-opener-wrong-name` fail, `c29-opener-ok` pass | `p-opener-bare` fail, `p-opener-venues-ok` pass. **`p-opener-template` (a backquoted `journal.db`) now fails** |
| `guard/no-remote-source` | **Covered with config** | `11-remote-source` fail, `11-local-source` pass | `p-jsx-string`, `p-uri-template`, `p-uri-concat` fail |
| `style/core-exports` | **Covered with config, stricter** | `8d-class-export` fail, `8d-ok` pass | `p-core-export-specifier`, `p-core-let`, `p-core-new` fail. **`p-core-internal-class` (an unexported class) now fails.** That is because a selector cannot follow `class A {}; export { A }`, so the candidate bans top-level classes in `src/core/` outright |
| Size limits (check 13) | **Already native.** `max-lines`, `max-lines-per-function`, `complexity`, `max-depth`, `max-params` are Oxlint's own; no plugin is involved | `13-*` all fail in both | — |
| `globalThis.fetch` (check 11) | **Already native** (`no-restricted-properties`). Only the *computed* form needs the guard rule (above) | `11-global-this`, `11-fetch` fail in both | — |

**Totals** [E, tested]:
- **All 25 PR fixtures I ran gave the same verdict in both configurations.**
- **Of my 24 probes:**
  - the plugin matched my expectation on 23. The odd one out was my mistake: the existing `no-restricted-imports` already refuses `import * as RN from 'react-native'`.
  - the selectors **missed 2** the plugin catches, and **were stricter on 2**.
- **Other behaviour:**
  - **Missing plugin:** Oxlint exits 1 with *"Failed to load JS plugin: oxlint-plugin-eslint"*. It fails closed [E, tested].
  - **Disable comments:** `// oxlint-disable-next-line eslint-js/no-restricted-syntax` silences a selector exactly as it silences a `guard/` rule [E, tested]. **So the scan and the guard pass are needed either way.**

### 4.3 What it costs

- **Configuration size.** 25 distinct selectors became **294 entries across 9 scopes** (about 136 KB of JSON).
  - **Why:** in Oxlint a later `overrides` entry **replaces** a rule's options for the files it matches.
  - **So:** every scope that needs one extra selector (the domain's clock rule, the two opener files, the capture module's registry exemption, core's export rule) must repeat the whole list.
- **A new silent failure mode.** I caused one myself. My generator's last override, for core test files, dropped `no-clock` from domain tests without a word [I, from my own generated file].
  - **Today:** that mistake would be a code change in a reviewed plugin.
  - **With selectors:** it is a list quietly missing from one glob, caught only if a fixture covers that glob.
- **Our own code removed:** `guard-plugin.ts` 372 + `style-plugin.ts` 82 = **454 lines of TypeScript**. They would become about 300 lines of regex and selector strings in JSON. **Those strings are code, just not TypeScript** [J].
- **`check-guard-pass.ts` changes.** Its copy outside the repository would need `node_modules`, or an absolute plugin path, to resolve the package. That ends G12's *"imports nothing"* property for the guard pass [I].

**Verdict** [J, moderate confidence]: **keep `guard-plugin.ts`.**
- It is on the PRIV-8 and DATA-2 path, and its `unwrap()` sees through every cast and parenthesis.
- A selector needs one more entry per wrapper shape, repeated in every scope.
- The gain is about 150 net lines, and the cost is a weaker and more fragile security configuration.
- **`style-plugin.ts` is different.** It has one scope and no security role, and 12 selectors replace it. **Worth doing only if the CSO approves the package anyway.**
- **What would overturn this:** Oxlint adding additive overrides, or rule instances under different names. Either removes the duplication. Or Oxlint shipping native `no-restricted-syntax`, which would remove the JS-plugin dependency.

---

## 5. Suggestion 3: the suppression guards, facts only (the CSO rules)

The Coordinator asked me not to rule on this. **These are facts, proved by the fixtures at `252f838`** [E, R1; R13].

**What the two scripts catch today:**
- **`tools/check-suppressions.ts`** (123 lines; hook and CI). Every `oxlint-`/`eslint` mention in a code file under `src/` and `modules/<name>/` must be:
  - a lower-case line-level disable;
  - naming rules;
  - with only allow-listed rules (`func-style`, `prefer-arrow-callback`, `maint-4/*`);
  - ending `-- <reason>`.
  - **Its 17 must-fail fixtures:** `9a-rule`, `-line`, `-nospace`, `-block-next-line`, `-jsx`, `-case`, `-file`, `-range`, `-bare`, `-plugin`, `-alias-eslint`, `-alias-ts`, `-native-name`, `-size`, `-eslint`, `-config-comment` and `9c-no-reason`. **One positive control:** `9a-allowlisted`.
- **`tools/check-guard-pass.ts`** (75 lines; CI only). It copies code outside the repository, replaces every `oxlint-disable`/`eslint-disable` token and runs `oxlint.guard.json`.
  - **Its fixtures:** `9b-guard-pass` (a disabled `fetch` still fails) and `9b-ignore-file` (an ignore file cannot hide a `fetch`).
- **Oxlint 1.86.0 has no switch that ignores disable comments.** The CSO checked this: rulings §0.9.1 and R28/R29 there. In my run, `/* oxlint-disable */` above a `fetch` passed the main lint (§7).

**What a `CLAUDE.md` rule alone would leave to review.** The rule already exists in `haunts` `CLAUDE.md` (CSO §0.9.2). Without the scripts:
- **Silencing a guard rule:** nothing in the hook or CI would stop a comment silencing a network, SQL or registry rule (PRIV-8, DATA-2).
- **Silencing other rules:** or one of checks 2, 12, 13 or 14. `9a-size` shows a disable of `max-lines-per-function`.
- **The reason requirement:** nothing would enforce it.
- **`reportUnusedDisableDirectives`** catches only a comment that silences nothing (`9c-unused`).
- **Who would see it:** a reviewer who happens to read that line; otherwise the CSO at pre-release, by its own account.

**The CSO's position (rulings §0.9.4, candour PR #47 at `37883bf`)** [E, R13]: keep the CI guard pass. The scan may go, on S1–S3:
- **S1:** widen the guard pass's fixtures to the shape and alias fixtures.
- **S2:** CSO-1 lands first.
- **S3:** rewrite the `CLAUDE.md` sentence.

If the guard pass is dropped too, the CSO states it will block release on PRIV-8 grounds should a silenced guard rule be present.

**One flag in §0.9 is mine to answer:** without the scan, nothing protects checks 2, 12, 13 and 14 or the reason requirement. **§7 answers it.**

---

## 6. Suggestion 5: dependency-cruiser for `check-core.ts`

`check-core.ts` (158 lines) enforces check 8 [E, R1]:
- **(a)** every core file is listed in `src/core/MANIFEST.md` with a valid reason;
- **(b)** a file listed as shared by named features is imported, **transitively**, by **two or more distinct features**;
- **(c)** core is at most 30% of non-test lines.

**(d)** is `style/core-exports` (§4).

**What dependency-cruiser 18.5.0 offers.** A module rule with `numberOfDependentsLessThan`, counting **direct** dependents that match `from.path` [E, R14, read from `src/validate/match-module-rule-helpers.mjs`]. I added:

`{ module: { path: '^src/core/', numberOfDependentsLessThan: 2 }, from: { path: '^src/features/' } }`

…to the PR's real configuration and ran four cases [E, tested]:

| Case | `check-core.ts` 8(b) | dependency-cruiser rule |
|---|---|---|
| One feature imports `shared.ts` (`8b-shared` shape) | fails | **fails** ✓ |
| **Two files of one feature** import it | fails (counts distinct features) [I, from the code] | **passes** ✗ |
| Two features import it | passes | passes ✓ |
| **Two features import `wrap.ts`, which imports `shared.ts`** | passes (transitive) [I, from the code] | **fails** ✗ |

| Part | Result |
|---|---|
| 8(a) manifest and reasons | **Not covered.** dependency-cruiser cannot read a Markdown table |
| 8(b) used by two features | **Not covered.** It is a different rule: it counts files, not features, and is direct, not transitive. It also applies to every core file, not only those the manifest calls shared |
| 8(c) 30% line budget | **Not covered.** No line-count rule |

**Verdict** [J, high confidence]: **keep the script.** **What would overturn it:** dependency-cruiser adding a dependents rule that groups by a captured path segment and follows transitive edges. I found none in 18.5.0's rule schema.

---

## 7. Suggestion 6: an Oxlint rule that errors on disable comments

### 7.1 What I built

A JS-plugin rule of **31 lines**. It reads `context.sourceCode.getAllComments()` and reports any comment that is a lint directive, unless it is all of these:
- a line-level `oxlint-disable`;
- naming only allow-listed rules;
- with `-- <reason>`.

I built two variants: one reports **at the comment**, the other **at line 1** of the file. It ran on all 17 `9a`/`9c` fixtures, `9b-guard-pass` and `9a-allowlisted`, plus nine attacks of mine (`x1`–`x9`). Each case ran as the hook does: `oxlint -c .oxlintrc.json --deny-warnings` with `reportUnusedDisableDirectives: "error"` [E, tested].

### 7.2 Every spelling the CSO's fixtures use: caught

**Both variants failed every one of the 17 `9a`/`9c` fixtures.** That includes no space, block, JSX, upper case, file-level, range, bare, the `eslint/` and `typescript-eslint/` aliases, an `eslint` config comment and a missing reason.
- **Comment shapes need no code.** The parser hands the rule every comment, whatever its shape. **The scan's shape-specific code is not needed** [E, tested].
- **One artefact of my setup:** `9a-allowlisted` failed for an unrelated reason. MAINT-4's rule is not yet in `maint-4.json`, so the directive was "unused".

### 7.3 The decisive case: can it be silenced? **Yes, in the normal pass**

| Attack (mine) | Rule at the comment | Rule at line 1 | Both rules on |
|---|---|---|---|
| `x1` `// oxlint-disable-next-line no-restricted-globals, meta/no-disable, … -- x` above `fetch` | caught | caught | caught |
| `x2` same, as `oxlint-disable-line` on the `fetch` line | caught only as an *unused directive* | caught | caught |
| `x3` / `9a-file` **bare `/* oxlint-disable */` at the top** | **passes, `fetch` and all** | **passes** | **passes** |
| `x4` `/* oxlint-disable no-restricted-globals, meta/no-disable, meta/no-disable-top */` at the top | caught only because one named rule was off ("unused") | same | **passes** |
| `x5` bare `// oxlint-disable-line` on the `fetch` line | **passes** | caught | caught |
| `x6` a disable of the rule above a line carrying a disable | caught | caught | caught |
| `x7` file-level disable at the **bottom** | caught (`fetch` still fires) | caught | caught |
| `x8` two block comments on line 1 | — | — | **passes** |
| `x9` `eslint/` alias plus the rule's name, file-level | **passes** | caught | caught |

**So a single bare `/* oxlint-disable */` at the top of a file silenced the rule and the network ban together, in every variant** [E, tested]. **No report location escapes a file-level directive.** The rule therefore **cannot replace the guard pass** [I, from the table].

### 7.4 Inside the guard pass it cannot be silenced

The guard pass already rewrites `oxlint-disable` to an inert token in its copy. I applied the same rewrite to all 29 cases. I ran the rule taught to read the inert token: one changed line. **All 29 gave the right verdict, including `9a-allowlisted` passing, and including every attack in §7.3** [E, tested].
- **The reason:** in the copy, no comment is a directive any more, so nothing can switch the rule off. The rule still reads what each comment *was*.
- **What I did not test:** I ran this with the main configuration on the stripped copies, not with `oxlint.guard.json` alone. The rule reads only comments, so I expect the same result under the guard configuration [I]. **That is S1's test to run.**

### 7.5 What it replaces

- **The guard pass: no.** It is what makes the rule unsilenceable.
- **The suppression scan: yes, if the rule runs inside the guard pass.**
  - **What it keeps:** the allow-list, the reason requirement, and protection of the non-guard rules (checks 2, 12, 13, 14). Those are the parts the CSO flagged to me in §0.9.4.
  - **What it drops:** the scan's shape-matching code.
  - **Where the rule lives:** in `guard-plugin.ts`, which is the one file the guard pass already copies. So it respects G12's *"imports nothing"*.
- **Commit-time feedback:** the CSO recommends running the guard pass in the hook too (§0.9.4). That costs one more Oxlint run per commit, well under a second on today's tree [E, tested on a one-file tree; I for M1's size].
- **In the normal lint pass:** the rule could also run there as early feedback. It catches every shape except a file-level directive, which the guard pass then catches.

**Beside the CSO's position.** The CSO keeps the guard pass and lets the scan go on S1–S3. This proposal **is consistent with that and adds one thing**: the scan's protections move into the guard pass instead of being dropped. **It answers the CSO's flag to me.** It is a Tier 1 change (`guard-plugin.ts`, `check-suppressions.ts`, fixture `expect.json` files), so it needs the CSO's note and the CEO's approval.

---

## 8. Recommendation

[J, moderate confidence overall; high on suggestions 1, 2 and 5]

**Weighed against D64.** The CEO's reason, quoted in D64, is: *"I want rules to be strict so that there is a good and understandable separation when using AI to code."* I count a change as good only if it keeps every check at least as strict, removes our code, and adds no toolchain the CSO must police separately.

| | Our code removed | New toolchains or packages | Strictness | Adopt? |
|---|---|---|---|---|
| 1 SwiftLint / ktlint / detekt | **≈ 0** (both scripts stay for Kotlin, Objective-C, C, Java and TypeScript) | Swift binary + SourceKit; 1–2 JVM jars | Weaker: comment-silenceable, fail-open modes, misses nested SQL and fully qualified Kotlin | **No** |
| 2 Oxlint for structure | ≈ 50 of 217 lines | `oxlint-plugin-eslint`; 3 more configs and runs | Equal where covered; the script stays for the rest | **No, for now** |
| 3 `CLAUDE.md` only | 198 lines | none | Weaker (§5) | **The CSO's call; superseded by 6** |
| 4 `oxlint-plugin-eslint` for the guard plugin | 454 TS lines → ≈ 300 JSON lines | `oxlint-plugin-eslint` | 2 misses, 2 stricter; fragile overrides | **No** (optional for `style-plugin.ts` only) |
| 5 dependency-cruiser for core | 0 | none | Different rule (2 wrong verdicts of 4) | **No** |
| **6 no-disable rule in the guard pass** | **−123 + ≈ 30** | **none** | **Equal or stricter.** Shapes handled by the parser; cannot be silenced in the copy | **Yes** |

**What I would adopt:** suggestion 6, as §7.5 describes, landing **after** CSO-1 (S2) and with S1's widened fixtures retargeted to the guard pass.

**What stays a script:** `check-network.ts`, `check-capture-isolation.ts`, `check-structure.ts`, `check-core.ts`, `check-guard-pass.ts` and `guard-plugin.ts` (with one rule added). **No new toolchain.**

**What the CSO would have to approve:**
1. **The no-disable rule** (Tier 1): `guard-plugin.ts` gains `guard/no-disable`. `check-suppressions.ts` is deleted. The 17 `9a`/`9c` fixtures are retargeted to `check-guard-pass.ts`. The guard pass is added to the hook. This is the CSO's S1–S3 plus this rule.
2. **Only if the CEO wants `style-plugin.ts` gone:** `oxlint-plugin-eslint` 1.86.0 as a new dependency (D40, D41), exact-pinned in lockstep with `oxlint`, with a G12 must-fail fixture.
3. **Only if the CEO overrules me on suggestion 1:** SwiftLint (and detekt) as release binaries outside the npm lockfile, with a pinned checksum. Plus a self-ban rule on `swiftlint:disable`, and must-fail fixtures that would catch the SourceKit and type-resolution fail-open modes.

**Disagreement, stated once.** The CEO's instinct, *"surely these can be oxlint checks"*, is right for the per-file rules: file names, hook and screen names, strings files and barrels. My tests confirm it. **It is wrong for what most of these scripts actually guard:**
- folders and files lint never reads;
- other languages;
- a Markdown manifest;
- a line budget;
- comments that switch the linter itself off.

**Those are why the scripts exist.** I would rather keep about 600 lines of tested TypeScript we understand than trade them for three toolchains. Each comes with its own way to be silenced and its own way to pass when misconfigured. I hit four such modes in one afternoon.

---

## 9. Where I looked, and what I did not do

**Read:**
- in `haunts` at `252f838`: every `tools/check-*.ts`, both plugins, `oxlint.guard.json`, `.oxlintrc.json`, `.dependency-cruiser.cjs`, `tools/structure.json`, `src/core/MANIFEST.md`, `tools/prove-checks.ts`, `checks.yml`, and every fixture cited above;
- in candour: the CSO's rulings §0.9 (PR #47, `37883bf`), `lint-layer-comparison.md`, ADR-0001's D64 line and `decisions/2026-09-16-haunt-gate.md` D64.

**Ran:**
- the PR's 145 proofs (baseline);
- 25 guard fixtures and 24 probes against both Oxlint configurations;
- 7 Swift and 8 Kotlin fixtures, plus 14 Swift and 8 Kotlin probes, against the scripts, SwiftLint and detekt (and ktlint on two);
- 9 structure fixtures and 7 probes against three Oxlint configurations;
- 4 dependency-cruiser cases;
- 29 directive cases in four modes.

**Not done:**
- **No Linux run** of SwiftLint: SourceKit on `ubuntu-24.04` is [I] from R5 and R12.
- **No detekt run with the Android classpath** (no Android project yet).
- **Not built:** a ktlint custom rule set. I judged the cost from R7, not from building one.
- **Not tested:** the selector fixes for the two §4.2 gaps.
- **Not tested on PR #367's own tree:** the guard pass with the no-disable rule (§7.4 used an equivalent rewrite).

**Disposal:** all downloads and sandboxes are in my session scratch space. None is in a checkout.

---

## 10. Evidence register

Retrieved 2026-10-11.
- **R1** — `haunts` PR #367 at `252f838`, the files named in §9, read from `git archive 252f838`. Includes `node_modules/oxlint/configuration_schema.json` at 1.86.0 for `oxc/no-barrel-file`'s options.
- **R2** — `https://registry.npmjs.org/oxlint-plugin-eslint` and `…/1.86.0`. Name, description, repository, maintainer, author, licence, versions, publish times, `_npmUser.trustedPublisher`, `dist.attestations`. *(Single source for what the package declares about itself.)*
- **R3** — `https://github.com/oxc-project/oxc/commits/main/npm/oxlint-plugin-eslint`, read through the GitHub API: the five latest commits are Oxlint release commits, 2026-09-14 to 2026-10-05. Repository: MIT, last push 2026-10-11.
- **R4** — `https://github.com/realm/SwiftLint` and `/releases/tag/0.65.1`, read through the GitHub API: MIT, last commit 2026-09-28, release assets and sizes.
- **R5** — `https://github.com/realm/SwiftLint/blob/main/README.md`. Regex `custom_rules` keys; `included`/`excluded` path regexes; Swift custom rules need Bazel; Linux SourceKit path.
- **R6** — `https://github.com/ktlint/ktlint` and `/releases/tag/1.8.0`, read through the GitHub API: MIT, last commit 2026-10-09, assets and the `.asc` signature.
- **R7** — `https://github.com/ktlint/ktlint/blob/master/documentation/release-latest/docs/api/custom-rule-set.md`. *"A ruleset is a JAR containing one or more RuleV2s"*; Gradle build; `-R` flag.
- **R8** — `https://github.com/detekt/detekt` and `/releases/tag/v1.23.8`, read through the GitHub API: Apache-2.0, last commit 2026-10-08; latest stable 1.23.8 of 2025-02-21; 2.0.0-alpha.6 of 2026-08-04.
- **R9** — `https://detekt.dev/docs/rules/style/`. `ForbiddenImport` (no type resolution) and `ForbiddenMethodCall` ("Requires Type Resolution"). **The page shows 2.0's key `forbiddenImports`; 1.23.8 rejected it** [E, tested].
- **R10** — `https://oxc.rs/docs/guide/usage/linter/js-plugins`. *"JS plugins are currently in alpha"*; selectors listed as supported.
- **R11** — `https://docs.github.com/en/billing/reference/actions-runner-pricing`. Linux 2-core $0.006 a minute, macOS $0.062 a minute. *(Single source; it is the vendor's own price list.)*
- **R12** — `https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md`. Swift 6.4; JDK 17 default; Kotlin 2.4.20.
- **R13** — candour `products/haunt/architecture/cso-m1-w1-rulings.md` §0.9, branch of PR #47 at `37883bf`.
- **R14** — `dependency-cruiser` 18.5.0, `src/validate/match-module-rule-helpers.mjs`, `dependentsCountsMatch`, read from the PR's installed tree.
