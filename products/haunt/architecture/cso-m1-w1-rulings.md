# CSO rulings for M1.W1: SPK-21's dependencies, the CSO note, and DATA-16

**Seat:** Chief Security Officer · **Date:** 2026-10-10 · **Revision 2:** 2026-10-10, for D68 · **Status:** Three rulings, revised once. **They prepare and flag; they do not certify** (Constitution 6.1: *"Agent reviews **prepare and flag; they do not certify**"*). §2 is for the CEO to approve or refuse. Nothing here edits ADR-0001, ADR-0002, the requirements, the wave plan, or any guard or config file in `haunts`.
**Revision 2 in one line:** the CEO's D68 replaced ESLint with Oxlint and Oxfmt, on TypeScript 7.0.2. **§0 is the new dependency decision and the re-rulings, and it wins wherever it conflicts with §1.** §2, the CSO note, is rewritten in place for the Ox files. §3 is unchanged.
**Authority:** the CEO, 2026-10-09: *"CSO: write the threat model alongside, and approve the B-strict dev tools."* Also the CTO's requests to this seat in `architecture/m1-wave-plan.md` §8 (candour PR #31, branch `docs/haunt-m1-wave-plan`). **For revision 2:** D68, CEO, 2026-10-10: *"I would say Ox tools over Biome thanks to the company behind it and the benefits the CTO found (e.g. the almost one to one rules which biome couldn't do). It is also designed to be high throughput, fast and for large codebases, covering us for the future and possibly other projects."* Recorded in `decisions/2026-09-16-haunt-gate.md` on candour branch `docs/haunt-d67-biome` (PR #35). It adopts the CTO's `architecture/ADR-0002-ox-lint-layer.md` (branch `docs/haunt-adr-0002-ox`, `bf4729b`, PR #38).
**Rules applied:** D40 (*"The CSO approves them as new dependencies"*), D41 (*"keeping dependencies minimal and exact-pinned, with the CSO approving any new ones"*) and D64 (*"The CSO approves the two new development tools"*). Also ADR-0001 §3 (*"No import plugin"*) and §6 item 2, and CSO conditions C16, C17 and C19 (`reviews/cso-review.md` §9.1).
**Template note:** `pipeline/templates/` has no template for a dependency decision or a security ruling [E: listed from disk, 2026-10-10]. This follows `reviews/cso-review.md`.
**Evidence tags** follow `pipeline/evidence-standard.md`. Registry facts were read from `https://registry.npmjs.org/<name>` on 2026-10-10. Transitive counts come from a lockfile I resolved on 2026-10-10 against `haunts` `main` at `dc9a0a0`. The register in §5 links every source. The npm registry is the single source for what a package declares about itself (licence, scripts, dependencies). I flag that once here rather than on every line.

Provenance: CSO · opus (Opus 5.5) · effort high · 2026-10-10 (first version and revision 2)

---

## 0. Revision 2 (D68): the Ox toolchain

**Read this first.** It rules on everything D68 changed: the new dependencies, condition T, and the controls ADR-0002 rebuilt around Oxlint. **Where it conflicts with §1, this section wins.** I tested every security claim it relies on myself, in a throwaway scratch directory, installing only with `--ignore-scripts` (§0.2). Three of the CTO's claims did not survive the test, and §0.7 states each once.

**No block.** My block is *"Release — for unresolved material vulnerabilities or absent threat modelling"* (`roles/cso.md`). Nothing here is a release. Each item below is an approval, a condition for SPK-21, or a recommendation.

### 0.1 The answer

| Package | Decision | Exact pin | Licence | Published | Install script |
|---|---|---|---|---|---|
| `oxlint` | **Approved, on G12 and G15 as re-ruled** (§0.5) | **1.86.0** | MIT | 2026-09-28 | none |
| `oxfmt` | **Approved, on G15 as re-ruled** (`-c` always; §0.5) | **0.71.0** | MIT | 2026-09-28 | none |
| `@swc/core` | **Approved, on conditions W1–W3** (§0.3) | **1.16.13** | Apache-2.0 | 2026-09-30 | **`postinstall`**, inert under `--ignore-scripts` |
| `eslint`, `typescript-eslint`, `@eslint-community/eslint-plugin-eslint-comments` | **Dropped. My approvals of them lapse** | — | — | — | — |
| `dependency-cruiser` | **Approved, pin unchanged.** Its conditions are now F1 as re-ruled, and C38 | 18.5.0 | MIT | 2026-09-30 | none |
| `jest` | **Approved, unchanged** (§1.3, §1.4) | 30.5.2 | MIT | 2026-09-18 | its two, as before |
| `@babel/preset-typescript` | **Approved, unchanged** (§1.5). It needs no TypeScript, so criterion 6 holds on 7.0.2 | 7.29.7 | MIT | 2026-05-25 | none |
| `typescript` | **Condition T reversed: stays at 7.0.2** (§0.4) | 7.0.2 | Apache-2.0 | 2026-07-08 | none |

**The CTO's totals are correct. I reproduced them** [E, R19]. Resolved independently against `haunts` `main` at **`cffa5d6`**, the set adds **406 lockfile entries**. **327 install on one machine**, both on macOS arm64 and on Linux x64 with glibc, which is what CI runs. Licences across the 406: MIT 339, ISC 26, `Apache-2.0 AND MIT` 11, BSD-3-Clause 9, Apache-2.0 9, BlueOak-1.0.0 8, BSD-2-Clause 1, 0BSD 1, `(MIT OR CC0-1.0)` 1, CC-BY-4.0 1. **No copyleft.** **Every entry resolves to `registry.npmjs.org` and carries an integrity hash.** Exactly three entries carry install scripts: `@parcel/watcher` 2.6.0, `unrs-resolver` 1.12.2 (both Jest's, §1.4) and `@swc/core` 1.16.13. `package.json` and `package-lock.json` are unchanged between `dc9a0a0` and `cffa5d6` [E, `git diff`]. The only change on `main` since my first version is one line in `CLAUDE.md` about pushing.

**A good sign about where these come from** [E, R18]: `oxlint`, `oxfmt`, `@swc/core` and the platform binaries I sampled (`@oxlint/binding-darwin-arm64`, `@oxlint/binding-linux-x64-gnu`, `@swc/core-darwin-arm64`, `@swc/core-linux-x64-gnu`) were each published by GitHub Actions with an SLSA provenance attestation. That ties each tarball to a build in its project's own repository. It does not prove the build was clean.

**The dropped three.** If ESLint ever returns (ADR-0002 §8(3)), it comes back for a fresh approval. The pins will have aged, and the registry has to be read again. **§1.7 falls away with them:** there is no ESLint for `eslint-config-expo` or `eslint-plugin-react-hooks` to plug into. Oxlint's native `react/rules-of-hooks` and `react/exhaustive-deps` are checked at PLAT-1 (ADR-0002 §10).

### 0.2 What I checked, and how

- **Registry** for each new package: version and publish time, licence, scripts, dependencies, optional dependencies, peers, and provenance [E, R18]. The npm registry is the single source for what a package declares about itself.
- **Lockfile:** `npm install --package-lock-only --ignore-scripts --save-dev --save-exact --before=2026-10-03` on copies of `haunts` `package.json` and `package-lock.json` at `cffa5d6`. Then I walked every added entry for licence, host, integrity and install script, and filtered by `os`, `cpu` and `libc` to count one machine [E, R19].
- **Install:** `npm ci --ignore-scripts` from that lockfile in the scratch directory. **No install script ran.**
- **Source read:** `@swc/core`'s `postinstall.js` [E, R20]; dependency-cruiser's `swc` loader [E, R21]. Each matched its public copy (the GitHub source differs from the tarball in whitespace only).
- **Planted violations:** against Oxlint, Oxfmt and dependency-cruiser, on Node 24.21.0 with `typescript` 7.0.2 [E, R22–R24]. §0.5 and §0.7 give the results.

### 0.3 `@swc/core`: why this use differs from my earlier refusal, and its conditions

**My refusal in §1.5** was of `@swc/core` as Jest's transform: *"a third install script and a third native binary for a job the preferred option does with neither."* Babel did that job with neither.

**Here, nothing does the job with neither.** The job is giving dependency-cruiser a real TypeScript parser under TypeScript 7. The alternatives are:
- **TypeScript 6.0.3 (condition T).** The CEO chose TypeScript 7 in D68, and that is a toolchain decision, not a security one.
- **`acorn`, dependency-cruiser's own fallback.** It is a loose parser, and §1.6 F1 exists because it can pass a boundary check quietly.
- **ADR-0002 §8(1): a home-made script reading `tsc --explainFiles`.** That puts a parser of unversioned, human-readable output on the security path. I rate it weaker than a native binary with provenance [J].

**So this use differs, and I approve it.**

**What the `postinstall` would do if it ran** [E, R20]: it checks that the native binding loads. If the binding fails, and neither `SWC_BINARY_PATH` nor `@swc/wasm` is present, it runs `npm install --no-save … @swc/wasm@<version>`. **That fetches a package from the network that is not in our lockfile and has no integrity hash of ours.** Under `--ignore-scripts` it never runs, and dependency-cruiser still parsed through `swc` without it [E, R24].

**Conditions:**
- **W1.** `--ignore-scripts` on every install, on every machine and in CI. That is already C31 and `CLAUDE.md`. It now also keeps `@swc/core` from fetching outside the lockfile. C30's install-script allow-list, when it lands, is exactly `@parcel/watcher`, `unrs-resolver` and `@swc/core`.
- **W2.** **Fixture F1 as re-ruled in §0.5**, with its sentinel rule. That is the proof that `swc` is the parser.
- **W3.** **`tools/check-all.ts` fails closed when `@swc/core` cannot parse.** Before it runs dependency-cruiser, it calls `parseSync` on a one-line TypeScript snippet, and if that throws, it stops with a message naming `npm ci --ignore-scripts`. **Why:** I removed the platform binding and ran dependency-cruiser again. It did not fail. It fell back to another parser **and still printed `"parser": "swc"` in its own summary** [E, R24]. In my fixtures the fallback still found every boundary edge, so the risk is small. But the hook runs on machines I cannot see, and a quiet fallback is G12's failure class. One call closes it.

**When it leaves:** once dependency-cruiser supports TypeScript 7.1's public API (ADR-0002 §12). Then `parser` goes back to `tsc`, `@swc/core` is dropped, and the sentinel fixture stays to prove the new parser.

**The fallback I was asked about.** Had I refused `@swc/core`, I would have accepted ADR-0002 §8(1) only with the fixtures it already names: one that fails when the script parses zero edges from a non-empty project or meets a line it does not recognise, and one per edge kind. It is not needed now.

### 0.4 Condition T: reversed

**Condition T existed for two reasons** (§1.2): typescript-eslint's peer stopped below TypeScript 6.1, and dependency-cruiser could not use TypeScript 7 to parse. **Under D68, neither holds:**
- No lint tool loads `typescript`. `oxlint` and `oxfmt` have no `typescript` dependency [E, R18].
- dependency-cruiser parses through `swc`, and under 7.0.2 it caught every planted boundary violation I gave it [E, R24].
- Jest loads `jest.config.ts` through Node's own type stripping (R13), and the Babel preset strips types without TypeScript.

**So condition T is reversed. `typescript` stays at 7.0.2**, and SPK-21 does not change that line. Three consequences:
- **dependency-cruiser cannot read `tsconfig.json` through TypeScript's API.** It still resolves `@/` aliases when told where the file is, but if it is not told, a boundary crossing written with `@/` is missed. That is **C38** (§0.5).
- **commitlint's configuration loader** already runs on 7.0.2 at `cffa5d6`. H5's 38-case suite re-proves it in SPK-21.
- **§1.2's Dependabot note no longer applies.** A Dependabot PR moving `typescript` within 7.x is ordinary, and F1 (with `f1-swc`) turns red if `swc` cannot parse something TypeScript adds.

### 0.5 The re-rulings

**C1 (no comment can silence the CI guard pass): met, re-ruled.** ESLint's `--no-inline-config` is gone; Oxlint has no equivalent (ADR-0002 §5.1). It is met by three things together, and **I accept them**:
- (a) **`tools/check-suppressions.ts`**, in the hook and in CI, as C25(a) below sets it;
- (b) **`tools/check-guard-pass.ts`**, in CI: strip the disable tokens from a copy, then run `oxlint -c oxlint.guard.json --no-ignore --deny-warnings`. **One added condition: the copy goes in a directory made with `fs.mkdtemp` under `os.tmpdir()`, outside the repository.** Why: Oxlint honours `.gitignore`, and **`--no-ignore` does not override it** [E, R22]. A copy inside the repository would inherit the repository's ignore rules. ADR-0002 §5.2(b) says `--no-ignore` *"covers ignore files"*; for `.gitignore` it does not;
- (c) **`respectEslintDisableDirectives: false`**. Tested: an `eslint-disable-next-line` was then not honoured [E, R22].

It is weaker than ESLint's flag, because the scan and the guard pass are our code, tested only by our fixtures (ADR-0002 §5.4(1)). **Residual risk, stated:** a disable directive with a prefix Oxlint adds in future would get past both. The CTO commits to reading each Oxlint release for directive changes (ADR-0002 §12), and I hold him to it in my review of each Oxlint bump.

**C25(a) (only line-level disables, never a guard rule): re-ruled, with one change. The scan must use an allow-list, not a deny-list.**
- **What I found** [E, R22]: Oxlint honours a disable that names a rule **by an alias**. `// oxlint-disable-next-line eslint/no-restricted-globals` silenced the network rule. `@typescript-eslint/no-explicit-any` and `typescript-eslint/no-explicit-any` each silenced `typescript/no-explicit-any`. ADR-0002 §5.2(a) builds the protected list by reading rule names from `oxlint.guard.json`, which holds `no-restricted-globals`. A literal comparison would pass the alias. In CI the guard pass would still catch a guard rule, but checks 12, 13 and 14 are not in the guard pass, so an alias would silence them everywhere.
- **The condition:** a disable passes only if **every rule it names is on an allow-list held as a constant in `check-suppressions.ts`**. SPK-21 writes the list as **`func-style`, `prefer-arrow-callback`, and names beginning `maint-4/`**, which are MAINT-4's rules. Everything else fails, aliases included. The other parts of ADR-0002 §5.2(a) stand: next-line and line forms only; at least one rule named; a `-- <reason>`; every `eslint` comment fails, rule-configuration comments included.
- **Adding a rule to the allow-list later is a Tier 1 change.** Making a rule possible to silence loosens policy.
- **The scan matches `oxlint-` and `eslint` regardless of case.** Oxlint honours only lower case [E, R22: `OXLINT-DISABLE-NEXT-LINE` and `Oxlint-Disable-Next-Line` were not honoured], but the scan should not depend on that.
- **It must see three shapes that Oxlint honours** [E, R22]: no space after `//`; a block comment carrying `oxlint-disable-next-line`; and a JSX comment, `{/* oxlint-disable-next-line … */}`.
- **New fixtures, each must fail `check-suppressions`:** `9a-alias-eslint`, `9a-alias-ts`, `9a-nospace`, `9a-block-next-line`, `9a-jsx`.
- **What would lift the allow-list requirement:** a deny-list that maps every alias Oxlint accepts to its rule and passes all five fixtures. I prefer the allow-list, because it does not need to know the aliases.
- **C25(a)'s original concern**, rule-configuration comments, does not arise: Oxlint does not honour them in either spelling [E, ADR-0002 §5.1, the CTO's test; I did not repeat it]. `9a-config-comment` stays.

**F1 (dependency-cruiser really parses TypeScript): re-ruled. `f1-swc` stands. `f1-type-only` needs a sentinel rule, because as written it does not prove the parser is `swc`.**
- **What I found** [E, R24]: with `swc`'s platform binding removed, dependency-cruiser fell back, **still reported `"parser": "swc"`**, and **still failed `f1-type-only`**. It recorded the edge as `import`, not `type-only`. With `parser: "acorn"` set explicitly, it also caught that edge. The CTO's comparison (§4, row a′) saw `acorn` miss a type-only edge in a richer fixture. Both results are true. Whether the fallback sees a type-only edge depends on the file, so a fixture that only checks the path cannot tell which parser ran.
- **The condition:** `f1-type-only`'s own configuration adds **a sentinel rule that matches only `dependencyTypes: ["type-only"]`**, and its `expect.json` requires **the sentinel rule's name** in the message. Tested: the sentinel fired with `swc` and stayed silent without it [E, R24]. W3's preflight in `check-all.ts` is its partner on every commit.

**F2 (a tool degrades quietly on an unsupported TypeScript): retired as written, and `f2-parse` accepted.** typescript-eslint is gone, and no lint tool loads `typescript`. `f2-parse` (a `.ts` file Oxlint cannot parse must fail, exit 1 in the CTO's test) is the right replacement. The rest of F2's purpose now belongs to F1's sentinel.

**G12 (a tool fails quietly), extended to Oxlint's JS plugins: I accept JS plugins as guard controls.** Oxlint's schema calls them *"alpha and not subject to semver"* (ADR-0002 §4). My reasons:
- They are our own code, Tier 1, reviewed at every change. ESLint's `no-restricted-syntax` was the tool's code, but `eslint-plugin-eslint-comments` was third-party code run at commit, which I approved.
- **Two of the three ways they can break fail closed** [E, R22, agreeing with ADR-0002 §3.2]: a plugin that will not load exits 1, and a rule that throws exits 1.
- **The third, a rule that silently matches nothing, fails open.** Only a must-fail fixture catches it. So **every plugin rule gets one**, as the CTO lists: `5-new-date`, `c8-template`, `c8-concat`, `c26a-computed`, `c26a-cast`, `c26b-import`, `c26c-namespace`, `c29-opener`, `11-remote-source`, `8d-class-export`, plus `g12-plugin-load`. **Four of those rules have not been run yet** (`no-native-registry`, `db-opener`, `no-remote-source`, `core-exports`; ADR-0002 §4), so their fixtures are the first evidence they work.
- **`guard-plugin.ts` imports nothing but `node:` built-ins.** Otherwise a file outside Tier 1 could change a guard rule. The guard pass already enforces this: I gave the plugin a helper file and copied it as the guard pass does, and the plugin failed to load, exit 1 [E, R22]. So a helper cannot reach `main` green.
- **A Dependabot PR that bumps `oxlint`, `oxfmt` or `@swc/core` is merged only on a green `prove-checks`.** That is already the rule (D39). I state it because those PRs are where a plugin breaks.

**G15 (nested configuration): accepted, and widened to Oxfmt and to JavaScript configuration files.**
- **Confirmed** [E, R22]: a nested `.oxlintrc.json` turning `no-restricted-globals` off silenced it for a bare `oxlint`, and not under `-c`.
- **Also found:**
  - **Oxfmt executes a TypeScript configuration file.** With `.oxfmtrc.json` removed, a bare `oxfmt --check` found a root `oxfmt.config.ts` and **ran it**: my marker file was written. With `-c .oxfmtrc.json` it did not [E, R23].
  - **A bare `oxlint` loads a root `oxlint.config.ts`.** In my run it used it to switch a guard rule off; under `-c .oxlintrc.json` it was ignored [E, R22].
  - Both tools exit 1 when the file named by `-c` is missing [E, R22, R23], so naming it fails closed.
- **The condition:**
  - every Oxlint **and Oxfmt** invocation names its configuration with `-c`. The hook runs `oxfmt -c .oxfmtrc.json --check`, never a bare `oxfmt`;
  - `tools/check-structure.ts` fails on any `.oxlintrc*` or `.oxfmtrc*` outside the repository root, **and on any `oxlint.config.*` or `oxfmt.config.*` anywhere, the root included.** ADR-0002 §3.1 says *"We use JSON only"*, so a JavaScript configuration file has no legitimate place.
- **Fixtures:** `g15-nested-config` (as ADR-0002 §5.3 gives it) and **`g15-js-config`** (a root `oxfmt.config.ts` and a root `oxlint.config.ts`; each must fail `check-structure`).

**New condition C37: ignore files cannot hide code from the linter.**
- **What I found** [E, R22]: `.eslintignore` and `.gitignore` each silenced `oxlint -c .oxlintrc.json` for the paths they list. **`.gitignore` did so even for a file git still tracks**, and `--no-ignore` did not override it. (`.oxlintignore` is not read.)
- **Why it matters:** the CI guard pass escapes this, because it lints a copy outside the repository. **But checks 2, 12, 13 and 14 run only from `.oxlintrc.json`**, in the hook and in CI, so one line in `.gitignore` would switch them off for a folder. Only `.gitignore`'s security block is protected.
- **The condition, for SPK-21:**
  - `check-structure.ts` fails on any `.eslintignore`;
  - `check-all.ts` fails when `git ls-files -ci --exclude-standard` lists any file, meaning a tracked file that an ignore rule matches. There are none at `cffa5d6` [E];
  - `check-all.ts` never passes `--ignore-path` or `--ignore-pattern`.
- **Fixtures:** `c37-eslintignore` and `c37-tracked-ignored`.

**New condition C38: dependency-cruiser must resolve `@/` aliases.**
- **What I found** [E, R24]: under TypeScript 7.0.2, an `@/features/b/internal` import from feature `a` **did not trip the boundary rule** unless `.dependency-cruiser.cjs` set `options.tsConfig`. Without it, only a `couldNotResolve` rule caught the import. With `tsConfig: { fileName: "tsconfig.json" }`, the edge resolved to `src/features/b/internal.ts` and the boundary rule fired.
- **The condition:** `.dependency-cruiser.cjs` sets `options.tsConfig`, **and** includes a `not-to-unresolvable` rule (`to: { couldNotResolve: true }`, severity `error`). **Fixture `f1-alias`:** an `@/` import across a feature boundary fails `depcruise` **with the boundary rule's name**, not only the unresolvable rule's.

**A recommendation, not a condition: let the hook see guard-rule changes in `.oxlintrc.json`.** A Tier 2 edit to `.oxlintrc.json` turned two guard rules off for the main pass. Run alone, the guard configuration still caught them [E, R22]. CI's guard pass catches this before merge, so the control holds. But the hook is where agents learn of a problem first. About ten lines in `check-all.ts` could fail when `.oxlintrc.json` sets any rule that `oxlint.guard.json` configures, or any `guard/*` rule. That is the CTO's call [J].

### 0.6 The protected list, renamed

§2.3 carries the renamed tiers. **I agree with the CTO's proposal, with two notes.** First, `.oxfmtrc.json` stays off the list only on G15's conditions above. Second, the allow-list in `check-suppressions.ts` is Tier 1 by that file's name, and that is intended.

### 0.7 Where the tests disagreed with ADR-0002, stated once

None of these is a block. Each is a correction for the CTO to write into SPK-21 (#355).
1. **ADR-0002 §5.3:** `f1-type-only` *"proves the parser is `swc`"*. It does not, because the fallback also fails it. **Fix:** the sentinel rule (F1, §0.5).
2. **ADR-0002 §5.2(a):** the scan's protected list is read from `oxlint.guard.json` and compared literally, but Oxlint honours aliases. **Fix:** the allow-list (C25(a), §0.5).
3. **ADR-0002 §5.2(b):** `--no-ignore` *"covers ignore files"*, but it does not cover `.gitignore`. That is harmless in the guard pass only if the copy is made outside the repository (C1(b), §0.5), and it is not harmless for the main pass (C37).

Two smaller additions are not disagreements: G15 widened to Oxfmt and to JavaScript configuration names, and C38.

### 0.8 What would overturn revision 2

- **`@swc/core`:** evidence that its `postinstall` runs despite `--ignore-scripts`, or a compromised release. Or dependency-cruiser supporting TypeScript 7.1, which retires it anyway.
- **JS plugins as guard controls:** an Oxlint release in which a broken plugin neither fails closed nor fails its fixture. I would then take ADR-0002 §8(2) to the CEO.
- **Condition T's reversal:** TypeScript syntax we use that `swc` cannot parse, shown by `f1-swc` going red. Then dependency-cruiser needs a different parser, or condition T returns.
- **C37 and C38:** an Oxlint release that ignores `.gitignore` under `--no-ignore`, or a dependency-cruiser that reads `tsconfig.json` without being told. Each would make its condition redundant, and I would withdraw it.
- **The allow-list:** as stated under C25(a).

---

## 1. Dependency decision for SPK-21 (`haunts` #355)

> **Superseded in part by §0 (revision 2, D68).** The ESLint packages are dropped, condition T is reversed, and F1 and F2 are re-ruled there. Jest, the Babel transform, dependency-cruiser's pin, the install-script findings in §1.4 and the transform criteria in §1.5 still stand. §1 is kept as written so the record shows what was decided first.

### 1.1 The answer

| Package | Decision | Exact pin | Published | Licence | Own tree (transitive, no peers) | New to `haunts` in this set | Install scripts in its tree |
|---|---|---|---|---|---|---|---|
| `eslint` | **Approved** | **10.12.0** | 2026-10-02 | MIT | 76 | 76 | none |
| `typescript-eslint` | **Approved, on condition T** (§1.2) | **8.71.0** | 2026-09-28 | MIT | 26 | 16 | none |
| `@eslint-community/eslint-plugin-eslint-comments` | **Approved** | **4.8.1** | 2026-09-12 | MIT | 2 | 1 | none |
| `dependency-cruiser` | **Approved, on condition T and fixture F1** | **18.5.0** | 2026-09-30 | MIT | 42 | 39 | none (its `prepare: husky` runs only in its own repository) |
| `jest` | **Approved** | **30.5.2** | 2026-09-18 | MIT | 330, of which 34 are per-platform binaries | 282 | **two**, both inert under `--ignore-scripts` (§1.4) |
| Transform: **`@babel/preset-typescript`** | **Approved (my preferred option)** | **7.29.7** | 2026-05-25 | MIT | 33 | 10 | none |
| `typescript` (existing) | **Change approved: 7.0.2 → 6.0.3** (condition T) | **6.0.3** | 2026-04-16 | Apache-2.0 | 0 | −20 binaries | none |
| Transform: `ts-jest` | **Refused** | — | — | MIT | — | — | — |
| Transform: `@swc/jest` with `@swc/core` | **Refused** | — | — | MIT / Apache-2.0 | — | — | `@swc/core` has `postinstall` |

The "new" column counts in the order listed, so later rows exclude what earlier rows brought. **The whole set adds 424 lockfile entries. On one machine that is 392 installed packages**, because only one of each package's per-platform binaries installs, and the lockfile lists every platform. **Licences across all 424:** MIT 351, ISC 28, Apache-2.0 17, BSD-3-Clause 10, BSD-2-Clause 7, BlueOak-1.0.0 8, 0BSD 1, `(MIT OR CC0-1.0)` 1 (`type-fest`), and CC-BY-4.0 1 (`caniuse-lite`, browser data reached through Babel's `browserslist`). There is **no copyleft licence** [E, the lockfile's licence fields, R10]. **Every entry resolves to `registry.npmjs.org` and carries an integrity hash** [E, R10].

**Jest is 282 of the 392.** I approve it because ADR-0001 §2.4 names Jest, which binds the CEO's D64, and because `jest-expo` needs it in W2 anyway. For the plain-Node domain and store projects alone, Node's built-in test runner would add nothing. That is an observation, not a disagreement: re-opening the test runner is the CTO's call, and the ADR settled it.

**Verified at the end of the session, 2026-10-10:** `npm view <name>@<pin> version license` returned the pinned version and the licence shown above for all seven pinned packages: `eslint` 10.12.0 MIT; `typescript-eslint` 8.71.0 MIT; `@eslint-community/eslint-plugin-eslint-comments` 4.8.1 MIT; `dependency-cruiser` 18.5.0 MIT; `jest` 30.5.2 MIT; `@babel/preset-typescript` 7.29.7 MIT; `typescript` 6.0.3 Apache-2.0 [E, R1–R6, R9].

### 1.2 Condition T: TypeScript must move from 7.0.2 to 6.0.3 in the same PR

**This is the finding that matters most in §1.** As specified, SPK-21 cannot install its own tools.

- `haunts` pins `typescript` 7.0.2 [E, `package.json` at `dc9a0a0`]. **TypeScript 7.0.2 ships no `main` entry and no `lib/typescript.js`.** Its package exports only `./unstable/*` paths [E, R6]. The classic compiler API that linters and analysers call is gone from it.
- **`typescript-eslint` 8.71.0 and 8.71.1 both declare the peer `typescript >=4.8.4 <6.1.0`.** So does the current canary, `8.71.2-alpha.2` [E, R2]. Its own documentation says *"If the issue is open, we do not have official support yet"* [E, R7]. TypeScript 7 support is an open pull request (#12803) for a 7.1 backend over IPC [E, R8].
- **I ran it.** Resolving the six packages against `typescript` 7.0.2 fails with `ERESOLVE … peer typescript@">=4.8.4 <6.1.0" from typescript-eslint@8.71.0` [E, R10, run locally 2026-10-10]. With `typescript` at 6.0.3, it resolves cleanly.
- **dependency-cruiser 18.5.0 supports `typescript: ">=2.0.0 <7.0.0"`** [E, its `src/meta.cjs` at the tag, R4]. Under TypeScript 7 it would not see TypeScript as available.

**What the condition says:** SPK-21 changes `typescript` to **6.0.3**, the last 6.x release [E, R6]. That keeps one TypeScript in the tree, which `tsc`, typescript-eslint, dependency-cruiser and commitlint's config loader (peer `typescript >=5`, `docs/conventions.md` §9.2) can all use. I approve that version change as the CSO. **Choosing the toolchain is the CTO's call, so this is also a flag to the CTO.** The alternative I can see is to keep TypeScript 7 for `tsc` and install `@typescript/typescript6`, Microsoft's side-by-side TypeScript 6 API package [E, R6]. But typescript-eslint and dependency-cruiser load `typescript` by that name, not `@typescript/typescript6`. Making them use it would need npm `overrides` on peer dependencies, which I have not tested [K, low confidence that it works cleanly]. I would not approve that without seeing it work.

**Dependabot:** its grouped weekly PR may later propose `typescript` 7.x. That PR must fail `npm ci`, as my run did, and must not be merged. No change to `.github/dependabot.yml` is needed for that [I]. If the CTO prefers a quieter board, an `ignore` entry for `typescript` majors would do it. That file is a baseline file, so the change would need a CSO note and the CEO's approval (D62).

**What would lift condition T:** a typescript-eslint release whose `typescript` peer includes 7.x, plus a dependency-cruiser release whose supported range includes it. Then 7.x can return through Dependabot.

### 1.3 What I checked, per package

For every row I read, from the registry: the version and its publish time; the licence; the direct dependencies; the peer dependencies; any `preinstall`, `install` or `postinstall` script; deprecation; and the repository URL [E, R1–R5, R9]. Then I resolved the whole set into a lockfile with `npm install --package-lock-only --ignore-scripts --before=2026-10-03`. That fetches metadata only: no tarball is downloaded and nothing runs. From that lockfile I walked each package's dependency tree and listed every entry with `hasInstallScript`, every licence, every resolved host, and every entry missing an integrity hash [E, R10].

**Why `--before=2026-10-03`:** it resolves every transitive package to a version **at least 7 days old**. That is the same cooldown the CEO approved for Dependabot (D43: *"7-day cooldown"*). A compromised release is usually caught and pulled within days, and a 7-day hold keeps most of that exposure out [J]. **For the same reason I pin `typescript-eslint` 8.71.0, not 8.71.1:** 8.71.1 was published on 2026-10-05, five days ago [E, R2]. Dependabot will offer it next week.

- **`eslint` 10.12.0:** 30 direct dependencies. Peer `jiti` is optional and needed only for a TypeScript config file, which SPK-21 does not use (`eslint.config.js`). Node engines `^20.19.0 || ^22.13.0 || >=24` cover `.nvmrc` 24.21.0 [E, R1]. **ESLint 10 keeps all three of C1's controls:** `noInlineConfig`, `--no-inline-config` and `reportUnusedDisableDirectives: "error"` [E, R11].
- **`typescript-eslint` 8.71.0:** four direct dependencies, all `@typescript-eslint/*` at the same version. Peer `eslint ^8.57.0 || ^9.0.0 || ^10.0.0` is met by ESLint 10 [E, R2].
- **`@eslint-community/eslint-plugin-eslint-comments` 4.8.1:** two direct dependencies, `escape-string-regexp` and `ignore`. Peer `eslint … || ^10.0.0` [E, R3]. It provides `no-restricted-disable`, which check 9(a) uses [E, R12].
- **`dependency-cruiser` 18.5.0:** 18 direct dependencies, each exact-pinned by the author. Among them are `acorn-loose`, `prompts` (for its `--init`), `watskeburt` (git diffs for `--affected`), `is-installed-globally` and `tsconfig-paths-webpack-plugin` [E, R4]. Node engines `^22||^24||>=26` [E, R4]. **Its declared `prepare: husky` script runs only when developing dependency-cruiser itself**, and the resolved lockfile marks no install script for it [E, R10; K, high confidence on npm's `prepare` semantics].
- **`jest` 30.5.2:** four direct dependencies. **It already brings Babel 7:** `jest-config` 30.5.2 depends on `@babel/core ^7.27.4` and on `babel-jest` [E, R5]. **It loads `jest.config.ts` through Node's own type stripping** when `process.features.typescript` is set, so `ts-node` and `esbuild-register` are not needed [E, R13, `readConfigFileAndSetRootDir.ts` at `v30.5.2`]. Node 24.21.0 sets it [E, run locally]. One transitive package carries a deprecation notice: `glob` 10.5.0, reached through `test-exclude` for coverage. The notice is generic to old `glob` lines. The CLI injection fixed in the 10.x line concerned `glob`'s command-line tool, which nothing here runs [K, moderate]. It is acceptable for a development dependency, and Dependabot will move it.

### 1.4 The two install scripts, both inside Jest's tree

| Package | Script | What it does [E, source read 2026-10-10, R14] | Under `--ignore-scripts` |
|---|---|---|---|
| `@parcel/watcher` 2.6.0 (from `jest-haste-map`) | `install: node scripts/build-from-source.js` | Runs `node-gyp rebuild` **only if** `npm_config_build_from_source` is `'true'`. Otherwise it does nothing; the prebuilt binary comes from an optional per-platform package | Not run |
| `unrs-resolver` 1.12.2 (from `jest-resolve`) | `postinstall: node postinstall.js` | Calls `napi-postinstall`'s `checkAndPreparePackage`, a fallback for older npm versions that do not install the per-platform binding | Not run |

`haunts` already installs with `--ignore-scripts`: CI runs `npm ci --ignore-scripts --no-audit --no-fund`, and `CLAUDE.md` tells every clone to run `npm ci --ignore-scripts` [E, `.github/workflows/traceability.yml` and `CLAUDE.md` at `dc9a0a0`]. **Both packages ship native code (Rust and C++ binaries) that runs on the developer's machine and the CI runner.** That is new for `haunts`. The binaries come from the registry with integrity hashes, through optional dependencies [E, R10]. I accept it for development tooling [J]. It stays a supply-chain exposure on the committer's machine, not in the app.

### 1.5 The transform: preferred option, and the criteria for any other

**Preferred: `@babel/preset-typescript` 7.29.7**, used through the `babel-jest` that Jest already installs. It adds 10 packages beyond Jest, because `@babel/core` 7 is already present [E, R10]. **It must be the 7.x line.** The 8.x line (8.0.7) needs `@babel/core ^8` [E, R9], which would put a second Babel major in the tree beside Jest's. It strips types without checking them, which is correct: `tsc` does the checking.

**Refused, with reasons:**
- **`ts-jest` 29.4.14:** its peer is `typescript >=4.3 <7`, it runs the TypeScript compiler API, and it brings `handlebars` and seven other packages for a job Babel already does here [E, R9]. **What would overturn this:** a need for type-checked tests that `tsc` cannot meet.
- **`@swc/jest` 0.2.39 with `@swc/core` 1.16.13:** `@swc/core` declares `postinstall: node postinstall.js` and ships a native binary per platform [E, R9]. That is a third install script and a third native binary for a job the preferred option does with neither. **What would overturn this:** test run times the Engineer measures as unworkable with Babel.
- **Node's own `module.stripTypeScriptTypes`** in a local transform would add nothing, and it exists in Node 24.21.0. But it prints *"stripTypeScriptTypes is an experimental feature and might change at any time"* [E, run locally]. Its output also keeps ES module syntax, which Jest runs only in its experimental ESM mode [K, high confidence]. **Not refused, and not preferred:** acceptable if the Engineer meets every criterion below.

**Criteria for any transform the Engineer proposes instead** (all must hold):
1. No install script anywhere in its tree, under the lockfile.
2. No native binary.
3. At most 15 packages beyond what `jest` 30.5.2 already brings.
4. Permissive licences only (no GPL family; `haunts` `CLAUDE.md`).
5. Every package in its tree at least 7 days old when locked.
6. It works with TypeScript 6.0.3, or needs no TypeScript at all.
7. It strips types only. Type-checking stays with `tsc`.
8. It is proved by fixture: a domain test using TypeScript-only syntax (an `interface`, a type annotation and a `satisfies`) runs and passes in the plain-Node project.

### 1.6 Conditions on the install itself (SPK-21's PR)

1. **Exact pins** as in the §1.1 table, in `devDependencies`, and nothing else added. A package outside this table needs a new CSO approval.
2. **Lock with the cooldown:** `npm install --save-dev --save-exact --ignore-scripts --before=<today minus 7 days>`. Then `npm ci --ignore-scripts` from the result succeeds, and `npm run typecheck` passes on TypeScript 6.0.3.
3. **The PR body lists:** each package and version from §1.1 with its licence; the new lockfile entry count; and the two install-script packages from §1.4. That is C17's record until `docs/dependencies.md` exists (PLAT-1, W2).
4. **Fixture F1 (dependency-cruiser parses TypeScript):** a guard fixture whose `.ts` file uses TypeScript-only syntax and imports across a forbidden boundary must **fail** `depcruise`. **Why:** when parsing fails, dependency-cruiser falls back to `acorn-loose` without stopping [E, `src/extract/acorn/parse.mjs` at `v18.5.0`, R4]. A missing or unsupported TypeScript would then pass the boundary checks quietly. The fixture turns that silence into a red build.
5. **Fixture F2 (the TypeScript parser refuses an unsupported TypeScript):** set typescript-eslint's parser to fail, not warn, on an unsupported TypeScript version. Its documentation offers that: *"make the parser throw, so that unsupported versions fail your lint run"* [E, R7]. This catches a future bump to TypeScript 7 at the lint step rather than as a quiet degradation.

### 1.7 The CTO's flag: Expo's ESLint configuration and `eslint-plugin-import`

**The flag is correct, and the problem is larger than the import plugin.**

- **`eslint-config-expo` 58.0.4**, the `next` tag and the SDK 58 line, **depends on `eslint-plugin-import ^2.30.0`** and on `eslint-import-resolver-typescript` [E, R15]. So do 57.0.2 (`latest`) and the 58 canary [E, R15].
- **`eslint-plugin-import` 2.32.0 is the newest release, published 2025-06-20, and its peer range stops at ESLint 9** (`… || ^8 || ^9`). **`eslint-plugin-react` 7.37.5, which the Expo config also brings, stops at `^9.7`** [E, R15]. Against ESLint 10, npm resolves the Expo config only by printing `ERESOLVE overriding peer dependency`, and it places `eslint-plugin-import` in the lockfile [E, R10, run locally 2026-10-10].
- **My view for PLAT-1 (W2)** [J]: **I will refuse `eslint-config-expo` while it depends on `eslint-plugin-import`.** It would contradict ADR-0001 §3 (*"No import plugin … ESLint's built-in rules plus dependency-cruiser do that job"*), and it would run two plugins outside their supported ESLint range. **PLAT-1 should instead install `eslint-plugin-react-hooks` directly.** Version 7.1.1 supports ESLint 10, is MIT-licensed and has five dependencies [E, R15]. It can also add `eslint-plugin-expo` (peer `eslint >=8.10`, three dependencies [E, R15]) if the CTO wants Expo's own rules. Both are approved or refused at PLAT-1 with exact pins. Neither is approved today.
- **The other path, refused in advance:** dropping to ESLint 9.39.5 (the `maintenance` tag) to fit Expo's config. That keeps the import plugin in the tree and buys nothing for security.
- **What would overturn this:** an `eslint-config-expo` release that drops `eslint-plugin-import`, or one that supports ESLint 10 and lets the import plugin be left out.

---

## 2. CSO note for SPK-21: one new hook, and the protected list (for the CEO)

> **Revised for D68 (revision 2).** The hook line is unchanged. What it runs, the file names on the protected list, and the tests are now Oxlint's and Oxfmt's. **You have not yet approved the first version** [E: no decision entry approves it, `decisions/2026-09-16-haunt-gate.md` on `docs/haunt-d67-biome`, read 2026-10-10], so this is the version to decide on.

### 2.1 What you are approving, in plain words

**Two things, both needed before SPK-21 merges.** `SECURITY.md` requires them: changes to the guard rails *"need a written note from the CSO seat and the CEO's approval, recorded in the decision record in the `candour` repository"* [E, `haunts` `SECURITY.md` at `cffa5d6`].

1. **One new commit hook.** Every commit runs the architecture checks (ADR-0001 and ADR-0002; D64 and D68) on the committer's machine, through one script, `tools/check-all.ts`. The commit is refused if any check fails. That script runs, in order:
   - **Oxlint**, `oxlint -c .oxlintrc.json`;
   - **the suppression scan**, `tools/check-suppressions.ts`, which refuses any comment that would silence a protected rule;
   - **Oxfmt in check mode**, `oxfmt -c .oxfmtrc.json --check`, which **never rewrites a file**;
   - **dependency-cruiser**, parsing through `swc`;
   - **the other `tools/check-*.ts` scripts** marked "both".

   The exact hook lines are in §2.2. Nothing else in `.pre-commit-config.yaml` changes.
2. **More files join the protected list (C23; ADR-0001 §6 item 2; ADR-0002 §9).** These are the files that, once SPK-21 creates them, decide whether the architecture checks run at all. **Tier 1** files need **a CSO note and your approval** in future, as the secret-scanning files already do. **Tier 2** files need only a CSO note (§2.3 explains the two tiers). SPK-21 also writes this list into `SECURITY.md` and `CLAUDE.md` security rule 3, because those two files are where agents and people read the rule.

**What you are not approving:** any dependency (that is §1, the CSO's own approval under D40, D41 and D64); any change to an existing hook; any spending. **It costs nothing to run** [J]. Each commit takes a few seconds longer while the code is small. If the hook becomes slow later, changing it comes back to you.

**If you refuse (1):** the checks still run in CI, but only after a push. Agents would learn about a violation a round-trip later, and while `haunts` is private on GitHub Free, CI can turn red but cannot stop a merge (`traceability.yml` header). **If you refuse (2):** a PR could switch a check off by editing its configuration, and only my review would notice.

### 2.2 The hook, exactly

Added to the `repo: local` hooks, after `forbid-signing-and-credential-files` and before the two `commit-msg` hooks:

```yaml
      # D64, D68; ADR-0001 §3 and ADR-0002 §3.2: the B-strict checks marked
      # "both" (SPK-21): Oxlint, the suppression scan, Oxfmt --check (never
      # rewrites), dependency-cruiser and the tools/check-*.ts scripts. Runs
      # the tools `npm ci --ignore-scripts` installed from the lockfile;
      # nothing is fetched at commit time, and it fails closed without them.
      # CI runs the same script with --ci, a superset
      # (.github/workflows/checks.yml). CSO note: candour
      # products/haunt/architecture/cso-m1-w1-rulings.md §2.
      - id: architecture-checks
        name: Architecture checks (ADR-0001, ADR-0002; D64, D68)
        language: unsupported
        entry: node tools/check-all.ts
        pass_filenames: false
        always_run: true
```

**Why each line** [K, high confidence on pre-commit's semantics unless marked]:
- **`language: unsupported`** runs the command as written, with no environment that pre-commit builds itself. It is the same choice the file already makes for commitlint (`docs/conventions.md` §9.1), and it is what C19 asks: tools run from the lockfile, never a second unlocked copy.
- **No `stages:`.** The file's `default_stages: [pre-commit]` applies, so the hook does not run again on the commit message.
- **`pass_filenames: false` and `always_run: true`.** The checks read the whole tree. The dependency graph and the folder allow-list cannot be judged one file at a time, and a commit that only deletes a file or edits `tools/structure.json` must still run them. pre-commit stashes unstaged changes before running hooks, so the tree checked is the tree being committed.
- **`entry: node tools/check-all.ts`, not `npm run check`.** With `npm run check`, **the `scripts` block of `package.json` would become an off-switch for the hook and CI at once.** One edited line (`"check": "true"`) would silence both, in a file that changes with every dependency. Calling a file under `tools/check-*.ts` puts that switch inside a file that is already protected (§2.3) and that check 10 already watches. **The CTO agreed and withdrew the `npm run` interface** [E, CTO ruling on #355, comment 6097413790, 2026-10-10]. `npm run check` stays as a convenience for people.
- **Inside `check-all.ts`, every Oxlint and Oxfmt command names its configuration with `-c`, and none passes `--ignore-path`, `--ignore-pattern`, `-A`/`--allow` or `--quiet`** (ADR-0002 §3.2; G15, C37 in §0.5). Without `-c`, a nested or JavaScript configuration file could switch rules off, and Oxfmt would execute a TypeScript one [E, R22, R23].

**Exposure, stated plainly** [I]: like the commitlint hook, this one runs code from the working tree at commit time. Under D68 that means:
- **our own scripts:** `tools/*.ts`;
- **our own Oxlint plugins:** `tools/oxlint/*-plugin.ts`, which Oxlint loads and runs in Node at every commit. Under ESLint the executable part was the configuration; under Oxlint it is the plugins;
- **`.dependency-cruiser.cjs`**, which is still executable JavaScript;
- **three native binaries** from the lockfile: Oxlint, Oxfmt and `swc`, through dependency-cruiser.

**The Oxlint and Oxfmt configurations are JSON data, not code** (ADR-0002 §3.1), **as long as G15 holds.** A branch that changes any of these files changes what runs on the committer's machine. That is why they are on the list in §2.3.

**What the Engineer shows in the PR before I record my review** (D32's rule: a control never seen to block is a belief):
- **H1.** A commit carrying a planted violation (an import from one feature into another) is refused, and the message names the fix.
- **H2.** A clean commit is accepted.
- **H3.** In a clone without `npm ci`, a commit is refused, with a message saying to run `npm ci --ignore-scripts`.
- **H4.** A commit that changes only `tools/structure.json`, in a way that breaks the allow-list, is refused (`always_run`).
- **H5.** No regression elsewhere. The 38-case commit-message suite from `docs/conventions.md` §9.3 still gives 38 of 38 **on `typescript` 7.0.2**, and a planted fake key is still refused by gitleaks.
- **H6.** The hook does not run at the `commit-msg` stage.
- **H7.** In CI, `.github/workflows/checks.yml` runs `node tools/check-all.ts --ci`. It runs **`node tools/prove-checks.ts` as a separate step**, so the proof that every check fails on its planted violation runs even if `check-all.ts` is broken. It installs with `npm ci --ignore-scripts --no-audit --no-fund`, pins every action to a full SHA, and sets `permissions: contents: read`.
- **H8 (new for D68).** A commit is refused when `swc` cannot load (move `@swc/core`'s platform binding aside and commit), with a message naming `npm ci --ignore-scripts` (W3, §0.3). A commit adding a root `oxfmt.config.ts` is refused by `check-structure` before Oxfmt runs (G15).

### 2.3 The protected list: what is added, in two tiers

**Today's protected list** [E, `haunts` `SECURITY.md` and `CLAUDE.md` rule 3 at `cffa5d6`]: `.pre-commit-config.yaml`, `.gitleaks.toml`, `.github/workflows/secret-scan.yml`, the security block of `.gitignore`, `SECURITY.md`, and `CLAUDE.md`'s security section. Also `.github/dependabot.yml` (D43, D62), `.claude/settings.json` and `.claude/hooks/` (MAINT-6).

**Tier 1: CSO note and your approval, recorded as a decision entry, exactly like today's list.** These files decide whether a security-bearing check runs, or what it accepts.

| File | Why it is a control |
|---|---|
| `oxlint.guard.json` | The guard configuration: the boundary, network and SQL rules and the guard plugin's rules, and nothing else. CI's guard pass runs it alone on a copy with every disable comment removed (check 9(b), C1). It is the one Oxlint pass that a comment cannot silence |
| `tools/oxlint/guard-plugin.ts` | Seven guard rules as code, run at every commit and in CI: check 5's clock ban, check 11's remote-source ban, C8 (SQL from strings), C26(a)–(c) and C29 (one opener per file). Changing it changes what the guard pass can see |
| `.dependency-cruiser.cjs` | Which code may reach storage, the capture module and each feature (checks 3–7). Now also its `parser: "swc"`, its `tsConfig` setting and its unresolvable rule (C38) |
| `tools/check-*.ts` (every file matching) | The runner the hook calls (`check-all.ts`, with W3's `swc` preflight and C37's ignore check); the comment scan and its allow-list (`check-suppressions.ts`, C25(a)); the guard pass (`check-guard-pass.ts`, C1); capture isolation (CAP-1(b), D63 guard b); the native network ban (C3); the core manifest; the folder rules (`check-structure.ts`, including G15 and C37). **If ADR-0002 §8(1) is ever taken, `check-graph.ts` is Tier 1 by this row** |
| `tools/prove-checks.ts`, and any change to or deletion of an existing folder under `tools/guard-fixtures/` | The proof that each check fails on its planted violation. Editing a fixture's `expect.json` to `"fails": false` would quietly retire a check. **Adding a new fixture folder is Tier 2**: it can only strengthen |
| `.github/workflows/checks.yml` | Runs every check in CI, and the proofs |
| `.github/workflows/traceability.yml`, `tools/traceability.ts`, `tools/conventions.ts` | Check 10 lives here, and so does the commit-message hook's code (`docs/conventions.md` §9.1). Switching check 10 off would switch off the tripwire for every other file in this table |
| **When created:** `docs/dependencies.md` (PLAT-1), and the config plugins under `plugins/` that remove `INTERNET` or set backup rules (SPK-22, D61) | The dependency record behind PRIV-8(d) and C4, and the two manifest controls. They join the list on creation, with no further approval needed |

**Tier 2: a CSO note only. My review at the PR's head commit is the approval, and you merge as usual.**

| File | Why a lighter tier is safe |
|---|---|
| `.oxlintrc.json` | The main configuration: size (checks 2 and 13), check 12's lint half, naming (check 14), and `extends` of the guard and MAINT-4's file. **An edit here can switch a guard rule off for the main pass** [E, R22], **but the CI guard pass runs `oxlint.guard.json` alone and still catches it**, and C25(a)'s allow-list is in a Tier 1 file. Most edits will be tuning, and asking you to approve each would cost your time for no security gain [J]. §0.5 recommends a cheap hook-side check |
| `tools/oxlint/style-plugin.ts` | Check 8(d) (core exports only functions, types and constants). That is architecture, not security. It is executable code, so it needs my review at the head commit |
| `tools/oxlint/maint-4.json`, `tools/oxlint/maint-4-plugin.ts` | MAINT-4's arrow-function rules. They are style rules, not guard rules (ADR-0002 §7). The plugin is executable code, so it needs my review. **MAINT-4 needs no change to a Tier 1 file**, because SPK-21 writes `maint-4/` into the scan's allow-list (C25(a)) |
| `tools/structure.json` | The folder allow-list. A new folder is an architecture question (the CTO reviews it), and I check that it does not open a path round the guard. That is a review, not a policy change |
| A **new** folder under `tools/guard-fixtures/` | It adds a proof and cannot remove one |

**Not on either list:**
- **`.oxfmtrc.json`**, as the CTO proposes, **on G15's conditions** (§0.5). It is JSON with no plugin key [E, R23], it affects only formatting, the runner always names it with `-c`, and `check-structure` bans the JavaScript configuration names that Oxfmt would otherwise execute;
- `src/core/MANIFEST.md`, which needs a CTO note (check 10);
- `package.json` and its lockfile. Any new dependency already needs a CSO approval under D40 and D41, and Dependabot's updates are governed by D43.

**How the list is enforced, honestly** [I]:
- **Check 10** fails a PR that touches any file above without a `## CSO note` heading. Its list of paths must match this table exactly, and a fixture proves it fails.
- **But check 10 can only see that a heading exists, not who wrote it.** Any author, agent or human, can type `## CSO note`. **The real control is that you merge every PR (D8, D39), and you do not merge a Tier 1 change without my review at its head commit and your approval on the record.** Check 10 is a tripwire that makes a change visible; it is not authentication.
- **SPK-21 writes the list** into `SECURITY.md` ("Changes to the guard rails") and into `CLAUDE.md` security rule 3. Both are already Tier 1 files, so your approval here covers those two edits. **The CTO has added both to SPK-21's files** [E, #355 body, read 2026-10-10].

### 2.4 For the decision entry

The Coordinator, or the CGO, records your answer as the next free D-number in `decisions/2026-09-16-haunt-gate.md`. Suggested wording, if you approve: *"The CSO's note for SPK-21 (revision 2, D68) is approved (`architecture/cso-m1-w1-rulings.md` §2): one pre-commit hook running `node tools/check-all.ts`, which runs Oxlint, the suppression scan, Oxfmt in check mode and dependency-cruiser, and the protected list extended in two tiers as §2.3 sets out. Tier 1 adds `oxlint.guard.json`, `tools/oxlint/guard-plugin.ts`, `.dependency-cruiser.cjs`, every `tools/check-*.ts`, `tools/prove-checks.ts` with the existing fixtures, `checks.yml`, and check 10's files. Tier 2 adds `.oxlintrc.json`, `tools/oxlint/style-plugin.ts`, `tools/oxlint/maint-4.json`, `tools/oxlint/maint-4-plugin.ts`, `tools/structure.json` and new fixture folders."*

---

## 3. DATA-16 (`haunts` #352): two rulings

### 3.1 Expiry in JavaScript: **accepted, with two conditions and one residual risk named**

**The question** (wave plan §3.5): expiry runs in JavaScript through `discard`, because CONF-15's window is a user setting held in `journal.db`, and a native command to carry it would widen the typed face beyond ADR-0001 §2.3. The cost is that *"an expired candidate stays in `capture.db` until the app next opens"*.

**Why I accept it.** The typed face is a security boundary as well as an architectural one. It has six functions and one event, and each new command is a new way for JavaScript to reach native storage. Keeping it closed is worth something [J]. And for a user who opens the app now and then, the overrun is bounded by the time between opens. While the app is not running, the leftover candidates sit in a file protected by the operating system (C10) [I].

**Where the cost is real.** CAP-1 records visits in the background with no JavaScript. **A user who leaves capture on and stops opening Haunts keeps adding candidates, and with JavaScript-only expiry none of them ever expires** [I, from CAP-1 and §3.5]. With D61, those rows also travel in the phone's own backups. That is the *"second, silent location history"* C15 was written to prevent. Article 4 is quoted in DATA-16 itself: *"Collect the minimum data necessary, state why, and delete it when no longer needed."*

**Conditions:**
1. **E1, in DATA-16 (W5).** Expiry runs **each time JavaScript starts and each time the app returns to the foreground, before any list of candidates is read for display.** An expired candidate is then never shown or counted, which is what CONF-15(a) needs. Test it by limb: age a candidate past its window, return the app from the background, and assert that it is gone from `capture.db` before the first `listCandidates` result reaches a screen.
2. **E2, before release, not before DATA-16 merges: a native ceiling.** On each native write, `Core` deletes candidates older than a fixed ceiling. **The ceiling is the largest value CONF-15's setting may take**, so the backstop never deletes anything the user's own setting would keep. It lives entirely inside `Core`: no new command and no change to the face, so no new ADR is needed. It never touches gaps or entitlement intervals, so DATA-16(d) holds. It is a constant, so CONF-15(b) (*"byte-identical before and after"* a trial ends) holds too [I]. **It needs a number that does not exist yet.** CONF-15 says *"default 30 days, user-adjustable"* and gives no maximum [E, `requirements.md` CONF-15]. **Flag to the PM/BA:** propose a maximum for the setting. Capping how long unconfirmed location may be kept is user-data policy, so **the CEO decides it** (Constitution 5.4: *"anything affecting user data policy"*).

**Residual risk, until E2 exists:** candidates can outlive their window without limit for a user who records but never opens the app. **This is not a block today.** My block applies to release, and nothing is being released. I will list E2 as an open item at the pre-release security review. It is closed either by the backstop being built, or by the CEO accepting the residual in writing.

**What would overturn this ruling:** evidence that iOS and Android stop delivering visits to an app the user has not opened for some period, which would bound the overrun without E2 [K: I am not aware of such a rule on either platform; not checked]. Or the CTO choosing to widen the face after all, by a new ADR, which would make native expiry exact.

### 3.2 `secure_delete` or `VACUUM` for `capture.db`: **`secure_delete = ON`, a truncating checkpoint after each deletion, and no routine `VACUUM`**

**The facts** [E, SQLite documentation, R16 and R17]:
- *"When secure_delete is on, SQLite overwrites deleted content with zeros."* It is *"normally off"* unless compiled otherwise. *"Applications that wish to avoid leaving forensic traces after content is deleted or updated should enable the secure_delete pragma … or else run VACUUM after the delete or update."*
- The `FAST` setting *"leav[es] forensic traces on freelist pages"*.
- `VACUUM` copies the database to a temporary file and back, and needs *"as much as twice the size of the original database file … in free disk space"*. The VACUUM page itself calls it *"an alternative to setting PRAGMA secure_delete=ON"*.
- `wal_checkpoint(TRUNCATE)` checkpoints, and then *"the WAL file is truncated to zero bytes upon successful completion"*.
- `secure_delete` does not scrub the shadow tables of virtual tables such as FTS3 and FTS5.

**Why this matters here.** Under D61, `capture.db` and its companion files go into the phone's own backups. A discarded candidate (a place the user chose *not* to keep) would otherwise survive in free pages and in the `-wal` file, and travel into iCloud or Google Drive. The attacker who would look for it is the one my threat model ranks first: **someone close to the user**, with the phone or the backup in hand [J; `reviews/cso-review.md` §1].

**The ruling, for DATA-16 to implement in `CaptureStore.swift` (and later in Kotlin):**
1. **`PRAGMA secure_delete = ON`** (not `FAST`) **on every connection to `capture.db`, immediately after it is opened.** The setting belongs to the connection, so setting it once at schema creation is not enough [K, high confidence].
2. **After each deletion batch** (adopt-and-reconcile, discard, expiry, and the E2 backstop), run **`PRAGMA wal_checkpoint(TRUNCATE)`**, so that page images from before the deletion do not remain in `capture.db-wal`. If the checkpoint is blocked by a reader, retry at the next batch. One connection on one serial queue (D63 guard a) makes this rare [I].
3. **No routine `VACUUM`.** It doubles the space needed, rewrites the whole file, and does nothing that 1 and 2 do not already do here.
4. **`capture.db` uses no FTS or other virtual table**, because those keep their own copies that `secure_delete` does not reach.

**Tests (DATA-16, native):**
- **(i)** After open, `PRAGMA secure_delete` returns `1`.
- **(ii)** Write a candidate whose latitude is a distinctive `double`. Discard it and let the checkpoint run. Then search the raw bytes of `capture.db` and of any `-wal` file for that value's eight-byte pattern, and assert it is absent. Repeat for expiry and for adoption.

**The honest limit** [K, high confidence]: no SQLite setting guarantees that bytes are physically erased from flash storage, because wear-levelling relocates blocks. The floor under all of this is file encryption (iOS Data Protection, C10; Android file-based encryption, C11). This ruling removes the copy that someone could recover by *opening the file*, which is the one that matters for a backup.

**Cost:** extra writes when rows are deleted. `capture.db` is small and deletes a handful of rows a day [J]. No running cost.

**Recommended for `journal.db` too (flag to the CTO, DATA-2.1 in W3).** A visit the user deletes is the clearest case for leaving no trace, for example a place they do not want someone close to them to find. The same `secure_delete = ON` in `open-journal.ts` costs a line. I record it as **condition C24** in the M1 threat model. It is not part of DATA-16.

---

## 4. Where I looked, and what would overturn these rulings

**Read:** `constitution.md`; `roles/cso.md`; `pipeline/evidence-standard.md`; the wave plan (candour PR #31) in full; ADR-0001; `reviews/cso-review.md`; `repo-security-baseline.md` §0–§9; `requirements.md` v1.4 rows CAP-1, CONF-15, SESS-9, ENT-1, DATA-1, DATA-2, DATA-16, PRIV-8 and PLAT-1; decision entries D29, D32, D40, D41, D43, D53, D61, D63, D64, D65 and D66. **In `haunts` at `dc9a0a0`:** `CLAUDE.md`, `SECURITY.md`, `.pre-commit-config.yaml`, `package.json`, `package-lock.json`, `tsconfig.json`, `.github/dependabot.yml`, `.github/workflows/traceability.yml`, `docs/conventions.md` §9, `.claude/settings.json`, `.claude/hooks/haunts-guard.py` (searched for path lists), and issue #355. **Plus** the registry and source files in §5.

**Not done:** I installed nothing and ran no package code. The lockfile was resolved from metadata only. So **no tool in §1 has been run against `haunts`.** Fixtures F1 and F2 and the hook tests H1–H7 are how the Engineer proves they work.

**Revision 2 (D68), additionally read:** ADR-0002 (`bf4729b`) and the CTO's comparison (`lint-layer-comparison.md`, `9f97afc`) in full; the D68 entry; the CTO's dependency list on #355 (comment 6100254984) and #355's revised body; `haunts` `main` at **`cffa5d6`**: `SECURITY.md`, `package.json`, `package-lock.json` and `.pre-commit-config.yaml`, plus `git diff dc9a0a0 cffa5d6` (one `CLAUDE.md` line). **Run, in a scratch directory outside any checkout:** the lockfile resolution and `npm ci --ignore-scripts` (§0.2), and planted violations against `oxlint` 1.86.0, `oxfmt` 0.71.0 and `dependency-cruiser` 18.5.0 with `@swc/core` 1.16.13, on `typescript` 7.0.2 (R22–R24). **Not run:** any test on Linux; the four untested plugin rules (§0.5 G12); Oxlint's rule-configuration comments (the CTO's test, not repeated); any timing. **Nothing was installed in, or committed to, `haunts`.**

**What would overturn:**
- **§1.2 (condition T):** a typescript-eslint and a dependency-cruiser release that support TypeScript 7, or a demonstrated `overrides` setup that runs both on TypeScript 6's API beside a TypeScript 7 `tsc`.
- **§1.5 (the transform):** measured run times that make Babel unworkable, or a transform meeting all eight criteria with fewer packages.
- **§1.7 (Expo's config):** an `eslint-config-expo` release without `eslint-plugin-import`.
- **§2 (the `check-all.ts` entry):** the CTO showing that `package.json`'s scripts can be protected as cheaply. My answer would then be to add the `scripts` block to Tier 1 instead.
- **§3:** as stated under each ruling.

---

## 5. Evidence register

All retrieved on 2026-10-10 by this seat.

| # | Claim | Source |
|---|---|---|
| R1 | `eslint` 10.12.0: publish time, MIT, 30 direct dependencies, peers, engines, no install script; the `maintenance` tag at 9.39.5 | [registry.npmjs.org/eslint](https://registry.npmjs.org/eslint) |
| R2 | `typescript-eslint` 8.71.0 (2026-09-28) and 8.71.1 (2026-10-05): MIT, four dependencies, peer `typescript >=4.8.4 <6.1.0`, peer `eslint … ^10.0.0`; canary `8.71.2-alpha.2` has the same peer | [registry.npmjs.org/typescript-eslint](https://registry.npmjs.org/typescript-eslint) |
| R3 | `@eslint-community/eslint-plugin-eslint-comments` 4.8.1: MIT, two dependencies, peer up to `^10.0.0` | [registry.npmjs.org/@eslint-community/eslint-plugin-eslint-comments](https://registry.npmjs.org/@eslint-community%2feslint-plugin-eslint-comments) |
| R4 | `dependency-cruiser` 18.5.0: MIT, 18 pinned dependencies, `prepare: husky`, engines; supported `typescript >=2.0.0 <7.0.0`; falls back to `acorn-loose` on a parse error | [registry.npmjs.org/dependency-cruiser](https://registry.npmjs.org/dependency-cruiser); [`src/meta.cjs` @v18.5.0](https://github.com/sverweij/dependency-cruiser/blob/v18.5.0/src/meta.cjs); [`src/extract/acorn/parse.mjs` @v18.5.0](https://github.com/sverweij/dependency-cruiser/blob/v18.5.0/src/extract/acorn/parse.mjs); [`src/extract/transpile/index.mjs` @v18.5.0](https://github.com/sverweij/dependency-cruiser/blob/v18.5.0/src/extract/transpile/index.mjs) |
| R5 | `jest` 30.5.2: MIT, four dependencies; `jest-config` 30.5.2 depends on `@babel/core ^7.27.4` and `babel-jest`; `babel-jest` peer `@babel/core ^7.11.0 \|\| ^8.0.0-0` | [registry.npmjs.org/jest](https://registry.npmjs.org/jest); [/jest-config](https://registry.npmjs.org/jest-config); [/babel-jest](https://registry.npmjs.org/babel-jest) |
| R6 | `typescript` 7.0.2: no `main`, exports only `./unstable/*`, 20 per-platform binaries; 6.0.3 is the last 6.x (2026-04-16), with `main: ./lib/typescript.js`; `@typescript/typescript6` 6.0.2 re-exports the TypeScript 6 API with a `tsc6` command | [registry.npmjs.org/typescript](https://registry.npmjs.org/typescript); [/@typescript/typescript6](https://registry.npmjs.org/@typescript%2ftypescript6) |
| R7 | typescript-eslint's TypeScript support policy; *"If the issue is open, we do not have official support yet"*; the parser can be made to throw on an unsupported version | [`docs/users/Dependency_Versions.mdx` @v8.71.1](https://github.com/typescript-eslint/typescript-eslint/blob/v8.71.1/docs/users/Dependency_Versions.mdx) |
| R8 | TypeScript 7 support is an open PR (#12803, a 7.1 backend over IPC); the TypeScript 6 support issue (#12123) is closed | [typescript-eslint #12803](https://github.com/typescript-eslint/typescript-eslint/pull/12803); [#12123](https://github.com/typescript-eslint/typescript-eslint/issues/12123) (GitHub search API) |
| R9 | `@babel/preset-typescript` 7.29.7 (MIT, peer `@babel/core ^7.0.0-0`) and 8.0.7 (peer `@babel/core ^8.0.0`); `ts-jest` 29.4.14 peers and dependencies; `@swc/jest` 0.2.39; `@swc/core` 1.16.13 with `postinstall` | [/@babel/preset-typescript](https://registry.npmjs.org/@babel%2fpreset-typescript); [/ts-jest](https://registry.npmjs.org/ts-jest); [/@swc/jest](https://registry.npmjs.org/@swc%2fjest); [/@swc/core](https://registry.npmjs.org/@swc%2fcore) |
| R10 | The resolved lockfile: `ERESOLVE` against TypeScript 7.0.2; clean against 6.0.3; 424 new entries (34 per-platform); licence counts; every `resolved` on `registry.npmjs.org`; integrity on every entry; `hasInstallScript` only on `@parcel/watcher` 2.6.0 and `unrs-resolver` 1.12.2; per-package trees; `eslint-config-expo` 58.0.4 adds `eslint-plugin-import` with `ERESOLVE overriding peer dependency` | Local run, 2026-10-10: `npm` 11.19.0, Node 24.21.0, `npm install --package-lock-only --ignore-scripts --before=2026-10-03` on a copy of `haunts` `package.json` and `package-lock.json` at `dc9a0a0`, in the session scratchpad. **Reproducible, not published** |
| R11 | ESLint 10: `noInlineConfig`, `--no-inline-config`, `reportUnusedDisableDirectives: "error"`, `--report-unused-inline-configs` | [`docs/src/use/configure/rules.md` @v10.12.0](https://github.com/eslint/eslint/blob/v10.12.0/docs/src/use/configure/rules.md); [`command-line-interface.md` @v10.12.0](https://github.com/eslint/eslint/blob/v10.12.0/docs/src/use/command-line-interface.md) |
| R12 | `no-restricted-disable` reports `eslint-disable` comments for named rules | [`docs/rules/no-restricted-disable.md` @v4.8.1](https://github.com/eslint-community/eslint-plugin-eslint-comments/blob/v4.8.1/docs/rules/no-restricted-disable.md) |
| R13 | Jest 30.5.2 loads `jest.config.ts` natively when `process.features.typescript` is set; otherwise it uses `ts-node` or `esbuild-register` | [`packages/jest-config/src/readConfigFileAndSetRootDir.ts` @v30.5.2](https://github.com/jestjs/jest/blob/v30.5.2/packages/jest-config/src/readConfigFileAndSetRootDir.ts); [`docs/Configuration.md` @v30.5.2](https://github.com/jestjs/jest/blob/v30.5.2/docs/Configuration.md) |
| R14 | The two install scripts' source | [`@parcel/watcher@2.6.0/scripts/build-from-source.js`](https://unpkg.com/@parcel/watcher@2.6.0/scripts/build-from-source.js); [`unrs-resolver@1.12.2/postinstall.js`](https://unpkg.com/unrs-resolver@1.12.2/postinstall.js) |
| R15 | `eslint-config-expo` 58.0.4, 57.0.2 and the 58 canary depend on `eslint-plugin-import ^2.30.0`; `eslint-plugin-import` 2.32.0 (2025-06-20) peer up to `^9`; `eslint-plugin-react` 7.37.5 peer up to `^9.7`; `eslint-plugin-react-hooks` 7.1.1 peer up to `^10.0.0`; `eslint-plugin-expo` 1.1.0 peer `>=8.10` | [/eslint-config-expo](https://registry.npmjs.org/eslint-config-expo); [/eslint-plugin-import](https://registry.npmjs.org/eslint-plugin-import); [/eslint-plugin-react](https://registry.npmjs.org/eslint-plugin-react); [/eslint-plugin-react-hooks](https://registry.npmjs.org/eslint-plugin-react-hooks); [/eslint-plugin-expo](https://registry.npmjs.org/eslint-plugin-expo) |
| R16 | `secure_delete` (on, fast, the FTS limitation); `wal_checkpoint(TRUNCATE)` | [SQLite, PRAGMA statements](https://www.sqlite.org/pragma.html) |
| R17 | `VACUUM` needs up to twice the file's size, and is an alternative to `secure_delete` for removing traces | [SQLite, VACUUM](https://www.sqlite.org/lang_vacuum.html) |

**Revision 2 (D68), retrieved or run 2026-10-10 by this seat:**

| # | Claim | Source |
|---|---|---|
| R18 | `oxlint` 1.86.0 (2026-09-28; 1.87.0 on 2026-10-05, inside the cooldown) and `oxfmt` 0.71.0 (2026-09-28): MIT, no install scripts, 19 optional platform bindings each, optional peers only (`oxlint-tsgolint`, `vite-plus`; `svelte`, `vite-plus`), `oxfmt` depends on `tinypool` 2.2.0 (MIT). `@swc/core` 1.16.13 (2026-09-30): Apache-2.0, `postinstall: node postinstall.js`, 12 optional platform binaries (`Apache-2.0 AND MIT`), depends on `@swc/counter` 0.1.3 and `@swc/types` 0.1.28. Each of these and the sampled binaries published by GitHub Actions with an SLSA provenance attestation (`https://slsa.dev/provenance/v1`). No `typescript` dependency in any of them | [registry.npmjs.org/oxlint](https://registry.npmjs.org/oxlint); [/oxfmt](https://registry.npmjs.org/oxfmt); [/@swc/core](https://registry.npmjs.org/@swc%2fcore); [/@swc/core-darwin-arm64](https://registry.npmjs.org/@swc%2fcore-darwin-arm64); [/@swc/core-linux-x64-gnu](https://registry.npmjs.org/@swc%2fcore-linux-x64-gnu); [/@oxlint/binding-darwin-arm64](https://registry.npmjs.org/@oxlint%2fbinding-darwin-arm64); [/@oxlint/binding-linux-x64-gnu](https://registry.npmjs.org/@oxlint%2fbinding-linux-x64-gnu); [/tinypool](https://registry.npmjs.org/tinypool); [/@swc/counter](https://registry.npmjs.org/@swc%2fcounter); [/@swc/types](https://registry.npmjs.org/@swc%2ftypes) |
| R19 | The D68 lockfile against `cffa5d6`: 406 added entries, none removed; 327 install on macOS arm64 and 327 on Linux x64 glibc; licence counts as §0.1; every `resolved` on `registry.npmjs.org`; integrity on every entry; `hasInstallScript` on exactly `@parcel/watcher` 2.6.0, `unrs-resolver` 1.12.2 and `@swc/core` 1.16.13; no tracked-but-ignored file in `haunts` at `cffa5d6` (`git ls-files -ci --exclude-standard` empty) | Local run, 2026-10-10: Node 24.21.0, npm 11.19.0, `npm install --package-lock-only --ignore-scripts --save-dev --save-exact --before=2026-10-03` on copies of `haunts` `package.json` and `package-lock.json` at `cffa5d6`, in the session scratchpad. **Reproducible, not published** |
| R20 | `@swc/core`'s `postinstall.js`: validates the native binding; on failure, unless `SWC_BINARY_PATH` or `@swc/wasm` is present, runs `npm install --no-save … @swc/wasm@<version>` | [unpkg.com/@swc/core@1.16.13/postinstall.js](https://unpkg.com/@swc/core@1.16.13/postinstall.js), byte-identical to the installed tarball's copy |
| R21 | dependency-cruiser uses `swc` only when `parser === "swc" && isAvailable()`; `isAvailable` is false when `@swc/core` fails to import, and extraction then falls through to the other parsers | [`src/extract/swc/extract.mjs` @v18.5.0](https://github.com/sverweij/dependency-cruiser/blob/v18.5.0/src/extract/swc/extract.mjs); [`src/extract/swc/parse.mjs` @v18.5.0](https://github.com/sverweij/dependency-cruiser/blob/v18.5.0/src/extract/swc/parse.mjs) (whitespace-only differences from the tarball) |
| R22 | Oxlint 1.86.0, tested: a nested `.oxlintrc.json` silences a rule without `-c` and not with it; a root `oxlint.config.ts` is used by a bare run and ignored under `-c`; `.eslintignore` and `.gitignore` (even for a tracked file) silence `oxlint -c`, and `--no-ignore` does not override `.gitignore`; `.oxlintignore` is not read; disables honoured with no space, as a block `next-line`, in JSX, and by alias (`eslint/…`, `@typescript-eslint/…`, `typescript-eslint/…`); not honoured in upper or mixed case, or as `eslint(…)`; `eslint-disable` not honoured under `respectEslintDisableDirectives: false`; `.oxlintrc.json` can turn an extended guard rule off while `-c oxlint.guard.json` alone still reports it; a throwing plugin rule exits 1; a plugin whose helper import is missing exits 1 (*"Failed to load JS plugin"*); a missing `-c` file exits 1. `--help`: `.eslintignore` is the default ignore path, `--disable-nested-config` exists | Local run, 2026-10-10, scratchpad. **Reproducible, not published** |
| R23 | Oxfmt 0.71.0: `-c` accepts `.json`, `.jsonc`, `.ts`, `.mts`, `.cts`, `.js`, `.mjs`, `.cjs`; `.gitignore` and `.prettierignore` used by default; its schema has no plugin key. Tested: with no `.oxfmtrc.json`, a bare `oxfmt --check` executed a root `oxfmt.config.ts` (marker file written); with `-c .oxfmtrc.json` it did not; a missing `-c` file exits 1 | `oxfmt --help` and `configuration_schema.json` from the installed 0.71.0; local run, 2026-10-10. **Reproducible, not published** |
| R24 | dependency-cruiser 18.5.0 on `typescript` 7.0.2, tested: with `parser: "swc"`, `f1-swc` and `f1-type-only` fail (exit 1); a five-file fixture (type-only from `.tsx` with JSX, `export *`, `import()`, generics, abstract class) gives every edge, and a sentinel rule on `dependencyTypes: ["type-only"]` fires; **with the `swc` platform binding removed, the summary still says `"parser": "swc"`, every path edge is still found, the type-only edge is typed `import`, and the sentinel does not fire**; explicit `acorn` also catches `f1-type-only`; an `@/` alias crossing a boundary trips the boundary rule only with `options.tsConfig` set, and otherwise only a `couldNotResolve` rule | Local run, 2026-10-10, scratchpad. **Reproducible, not published** |
| R25 | ADR-0002 and the CTO's comparison; D68 as recorded; the CTO's dependency list for this seat | `products/haunt/architecture/ADR-0002-ox-lint-layer.md` (`bf4729b`) and `lint-layer-comparison.md` (`9f97afc`), candour branch `docs/haunt-adr-0002-ox`; `decisions/2026-09-16-haunt-gate.md` D68 on `docs/haunt-d67-biome`; [`haunts` #355, comment 6100254984](https://github.com/deopea-david/haunts/issues/355#issuecomment-6100254984) |

**[K] claims carried, each to be upgraded before it anchors a ticket:** pre-commit's stash of unstaged changes and the `language: unsupported` semantics (§2.2); npm's `prepare` running only for the root project and git dependencies (§1.3); Jest's ESM mode being experimental (§1.5); `secure_delete` being set per connection (§3.2); flash wear-levelling (§3.2); the CLI-only scope of the `glob` 10.x advisory (§1.3); `overrides` on peer dependencies (§1.2).

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-10 | First version (CSO): §1 dependency decision and §2 CSO note posted to `haunts` #355 (comments 6097283953 and 6097285838); §3 DATA-16 rulings |
| 2026-10-10 | **Revision 2, for D68 (CSO):** new §0. `oxlint` 1.86.0, `oxfmt` 0.71.0 and `@swc/core` 1.16.13 approved on conditions; the three ESLint packages dropped; condition T reversed. C1, C25(a), F1, F2, G12 and G15 re-ruled; C37 and C38 added; W1–W3 for `@swc/core`. §2 rewritten in place for the Ox hook and files, with H8 added; §1 marked superseded in part. Posted to `haunts` #355 |
