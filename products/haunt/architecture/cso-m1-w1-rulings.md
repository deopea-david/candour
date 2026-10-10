# CSO rulings for M1.W1: SPK-21's dependencies, the CSO note, and DATA-16

**Seat:** Chief Security Officer · **Date:** 2026-10-10 · **Status:** Three rulings. **They prepare and flag; they do not certify** (Constitution 6.1: *"Agent reviews **prepare and flag; they do not certify**"*). §2 is for the CEO to approve or refuse. Nothing here edits ADR-0001, the requirements, the wave plan, or any guard or config file in `haunts`.
**Authority:** the CEO, 2026-10-09: *"CSO: write the threat model alongside, and approve the B-strict dev tools."* Also the CTO's requests to this seat in `architecture/m1-wave-plan.md` §8 (candour PR #31, branch `docs/haunt-m1-wave-plan`).
**Rules applied:** D40 (*"The CSO approves them as new dependencies"*), D41 (*"keeping dependencies minimal and exact-pinned, with the CSO approving any new ones"*) and D64 (*"The CSO approves the two new development tools"*). Also ADR-0001 §3 (*"No import plugin"*) and §6 item 2, and CSO conditions C16, C17 and C19 (`reviews/cso-review.md` §9.1).
**Template note:** `pipeline/templates/` has no template for a dependency decision or a security ruling [E: listed from disk, 2026-10-10]. This follows `reviews/cso-review.md`.
**Evidence tags** follow `pipeline/evidence-standard.md`. Registry facts were read from `https://registry.npmjs.org/<name>` on 2026-10-10. Transitive counts come from a lockfile I resolved on 2026-10-10 against `haunts` `main` at `dc9a0a0`. The register in §5 links every source. The npm registry is the single source for what a package declares about itself (licence, scripts, dependencies). I flag that once here rather than on every line.

Provenance: CSO · opus (Opus 5.5) · effort high · 2026-10-10

---

## 1. Dependency decision for SPK-21 (`haunts` #355)

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

### 2.1 What you are approving, in plain words

**Two things, both needed before SPK-21 merges.** `SECURITY.md` requires them: changes to the guard rails *"need a written note from the CSO seat and the CEO's approval, recorded in the decision record in the `candour` repository"* [E, `haunts` `SECURITY.md` at `dc9a0a0`].

1. **One new commit hook.** Every commit will run the architecture checks (ADR-0001, D64) on the committer's machine, and is refused if any check fails. The exact lines are in §2.2. Nothing else in `.pre-commit-config.yaml` changes.
2. **More files join the protected list (C23; ADR-0001 §6 item 2).** These are the files that, once SPK-21 creates them, decide whether the architecture checks run at all. In future, changing them needs **a CSO note and your approval**, as the secret-scanning files already do. Two of them need only a CSO note (§2.3 explains the two tiers). SPK-21 also writes this list into `SECURITY.md` and `CLAUDE.md` security rule 3, because those two files are where agents and people read the rule.

**What you are not approving:** any dependency (that is §1, the CSO's own approval under D40, D41 and D64); any change to an existing hook; any spending. **It costs nothing to run** [J]. Each commit takes a few seconds longer while the code is small. If the hook becomes slow later, changing it comes back to you.

**If you refuse (1):** the checks still run in CI, but only after a push. Agents would learn about a violation a round-trip later, and while `haunts` is private on GitHub Free, CI can turn red but cannot stop a merge (`traceability.yml` header). **If you refuse (2):** a PR could switch a check off by editing its configuration, and only my review would notice.

### 2.2 The hook, exactly

Added to the `repo: local` hooks, after `forbid-signing-and-credential-files` and before the two `commit-msg` hooks:

```yaml
      # D64, ADR-0001 §3: the B-strict checks marked "both" (SPK-21). Runs the
      # tools `npm ci` installed from the lockfile; nothing is fetched at commit
      # time, and it fails closed without `npm ci`. CI runs the same script with
      # --ci, a superset (.github/workflows/checks.yml). CSO note: candour
      # products/haunt/architecture/cso-m1-w1-rulings.md §2.
      - id: architecture-checks
        name: Architecture checks (ADR-0001, D64)
        language: unsupported
        entry: node tools/check-all.ts
        pass_filenames: false
        always_run: true
```

**Why each line** [K, high confidence on pre-commit's semantics unless marked]:
- **`language: unsupported`** runs the command as written, with no environment that pre-commit builds itself. It is the same choice the file already makes for commitlint (`docs/conventions.md` §9.1), and it is what C19 asks: tools run from the lockfile, never a second unlocked copy.
- **No `stages:`.** The file's `default_stages: [pre-commit]` applies, so the hook does not run again on the commit message.
- **`pass_filenames: false` and `always_run: true`.** The checks read the whole tree. The dependency graph and the folder allow-list cannot be judged one file at a time, and a commit that only deletes a file or edits `tools/structure.json` must still run them. pre-commit stashes unstaged changes before running hooks, so the tree checked is the tree being committed.
- **`entry: node tools/check-all.ts`, not `npm run check`. This is one disagreement with the CTO's interface for SPK-21, stated once.** #355 says *"The pre-commit hook and CI call only these two scripts"* (`npm run check`, `npm run check:ci`). With that design, **the `scripts` block of `package.json` becomes an off-switch for the hook and CI at once.** One edited line (`"check": "true"`) would silence both, in a file that changes with every dependency. Calling a file under `tools/check-*.ts` puts that switch inside a file that is already protected (§2.3) and that check 10 already watches. `npm run check` can stay as a convenience for people, defined as `node tools/check-all.ts`. **The CTO adds `tools/check-all.ts` to SPK-21's files.** If the CTO keeps `npm run check` as the entry, this note does not cover it: `package.json`'s `scripts` block would then have to join the Tier 1 list, and the note would come back to you.

**Exposure, stated plainly** [I]: like the commitlint hook, this one runs code from the working tree at commit time. That means `tools/*.ts`, `eslint*.config.js` (an ESLint config is executable JavaScript), `.dependency-cruiser.cjs`, and `node_modules` as installed from the lockfile. A branch that changes those files changes what runs on the committer's machine. That is why they are on the list in §2.3.

**What the Engineer shows in the PR before I record my review** (D32's rule: a control never seen to block is a belief):
- **H1.** A commit carrying a planted violation (an import from one feature into another) is refused, and the message names the fix.
- **H2.** A clean commit is accepted.
- **H3.** In a clone without `npm ci`, a commit is refused, with a message saying to run `npm ci --ignore-scripts`.
- **H4.** A commit that changes only `tools/structure.json`, in a way that breaks the allow-list, is refused (`always_run`).
- **H5.** No regression elsewhere. The 38-case commit-message suite from `docs/conventions.md` §9.3 still gives 38 of 38, and a planted fake key is still refused by gitleaks.
- **H6.** The hook does not run at the `commit-msg` stage.
- **H7.** In CI, `.github/workflows/checks.yml` runs `node tools/check-all.ts --ci`. It runs **`node tools/prove-checks.ts` as a separate step**, so the proof that every check fails on its planted violation runs even if `check-all.ts` is broken. It installs with `npm ci --ignore-scripts --no-audit --no-fund`, pins every action to a full SHA, and sets `permissions: contents: read`.

### 2.3 The protected list: what is added, in two tiers

**Today's protected list** [E, `haunts` `SECURITY.md` and `CLAUDE.md` rule 3 at `dc9a0a0`]: `.pre-commit-config.yaml`, `.gitleaks.toml`, `.github/workflows/secret-scan.yml`, the security block of `.gitignore`, `SECURITY.md`, and `CLAUDE.md`'s security section. Also `.github/dependabot.yml` (D43, D62), `.claude/settings.json` and `.claude/hooks/` (MAINT-6).

**Tier 1: CSO note and your approval, recorded as a decision entry, exactly like today's list.** These files decide whether a security-bearing check runs, or what it accepts.

| File | Why it is a control |
|---|---|
| `eslint.guard.config.js` | The CI pass for boundary, network and SQL rules, run with inline configuration disabled (check 9(b), C1). The one ESLint pass that a comment cannot silence |
| `.dependency-cruiser.cjs` | Which code may reach storage, the capture module and each feature (checks 3–7) |
| `tools/check-*.ts` (every file matching, including `check-all.ts`) | Capture isolation (CAP-1(b), D63 guard b), the native network ban (C3), the core manifest, the folder rules, and the runner the hook calls |
| `tools/prove-checks.ts`, and any change to or deletion of an existing folder under `tools/guard-fixtures/` | The proof that each check fails on its planted violation. Editing a fixture's `expect.json` to `"fails": false` would quietly retire a check. **Adding a new fixture folder is Tier 2**: it can only strengthen |
| `.github/workflows/checks.yml` | Runs every check in CI, and the proofs |
| `.github/workflows/traceability.yml`, `tools/traceability.ts`, `tools/conventions.ts` | Check 10 lives here, and so does the commit-message hook's code (`docs/conventions.md` §9.1). Switching check 10 off would switch off the tripwire for every other file in this table |
| **When created:** `docs/dependencies.md` (PLAT-1), and the config plugins under `plugins/` that remove `INTERNET` or set backup rules (SPK-22, D61) | The dependency record behind PRIV-8(d) and C4, and the two manifest controls. They join the list on creation, with no further approval needed |

**Tier 2: a CSO note only. My review at the PR's head commit is the approval, and you merge as usual.**

| File | Why a lighter tier is safe |
|---|---|
| `eslint.config.js` | Its boundary, network and SQL rules are repeated in `eslint.guard.config.js`, which CI enforces regardless. Most edits here will be style and size tuning, such as MAINT-4's arrow-function block, and asking you to approve each one would cost your time for no security gain [J] |
| `tools/structure.json` | The folder allow-list. A new folder is an architecture question (the CTO reviews it), and I check that it does not open a path round the guard. That is a review, not a policy change |
| A **new** folder under `tools/guard-fixtures/` | It adds a proof and cannot remove one |

**Not on either list:** `src/core/MANIFEST.md`, which needs a CTO note (check 10), and `package.json` and its lockfile. Any new dependency already needs a CSO approval under D40 and D41, and Dependabot's updates are governed by D43.

**How the list is enforced, honestly** [I]:
- **Check 10** fails a PR that touches any file above without a `## CSO note` heading. Its list of paths must match this table exactly, and a fixture proves it fails.
- **But check 10 can only see that a heading exists, not who wrote it.** Any author, agent or human, can type `## CSO note`. **The real control is that you merge every PR (D8, D39), and you do not merge a Tier 1 change without my review at its head commit and your approval on the record.** Check 10 is a tripwire that makes a change visible; it is not authentication.
- **SPK-21 writes the list** into `SECURITY.md` ("Changes to the guard rails") and into `CLAUDE.md` security rule 3. Both are already Tier 1 files, so your approval here covers those two edits. **The CTO adds `SECURITY.md` to SPK-21's file table**; `CLAUDE.md` is already in it, but only for one line outside the security section, so that entry widens to include rule 3.

### 2.4 For the decision entry

The Coordinator, or the CGO, records your answer as the next free D-number in `decisions/2026-09-16-haunt-gate.md`. Suggested wording, if you approve: *"The CSO's note for SPK-21 is approved (`architecture/cso-m1-w1-rulings.md` §2): one pre-commit hook running `node tools/check-all.ts`, and the protected list extended in two tiers as §2.3 sets out."*

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

**[K] claims carried, each to be upgraded before it anchors a ticket:** pre-commit's stash of unstaged changes and the `language: unsupported` semantics (§2.2); npm's `prepare` running only for the root project and git dependencies (§1.3); Jest's ESM mode being experimental (§1.5); `secure_delete` being set per connection (§3.2); flash wear-levelling (§3.2); the CLI-only scope of the `glob` 10.x advisory (§1.3); `overrides` on peer dependencies (§1.2).

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-10 | First version (CSO): §1 dependency decision and §2 CSO note posted to `haunts` #355 (comments 6097283953 and 6097285838); §3 DATA-16 rulings |
