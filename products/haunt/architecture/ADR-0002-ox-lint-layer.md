# ADR-0002 — Oxlint and Oxfmt as the lint and format layer, with dependency-cruiser on `swc`, on TypeScript 7

**Status:** **Adopted** — CEO, 2026-10-10, **D68** (`decisions/2026-09-16-haunt-gate.md`, candour PR #35, branch `docs/haunt-d67-biome`). D68 replaces D67 (Biome). No Biome ADR was ever committed.
**Date:** 2026-10-10 · **Deciders:** CEO (decision); CTO (the comparison behind it and this record) · **Supersedes:** ADR-0001, **only** in the parts listed in §2. Everything else in ADR-0001 stands and stays binding.
**The decision, in the CEO's words (D68):** *"I would say Ox tools over Biome thanks to the company behind it and the benefits the CTO found (e.g. the almost one to one rules which biome couldn't do). It is also designed to be high throughput, fast and for large codebases, covering us for the future and possibly other projects."* On TypeScript he added a concern, which §11 answers: *"if the tool goes unmaintained or takes a long time to support TS 7."*
**Behind it:** `lint-layer-comparison.md` (candour PR #36, `9f97afc`), the tested comparison that recommended this combination [J, moderate confidence].
**Corrected 2026-10-10 against the CSO's revision 2 rulings** (`cso-m1-w1-rulings.md` §0, candour PR #33; SPK-21 #355 carries the same text). Her tests overturned three claims in this ADR's first version: **(i)** `f1-type-only` does not prove `swc` runs (§5.3); **(ii)** the suppression scan must use an allow-list, because Oxlint honours rule-name aliases (§5.2(a)); **(iii)** the guard pass must copy the tree outside the repository, because `--no-ignore` does not override `.gitignore` (§5.2(b)). New conditions C37, C38 and W1–W3, and G15 widened to Oxfmt and to JavaScript configuration files, are written in (§5.2(c)–(g), §4). §5, §6 and §9 now state what the CSO ruled, and §13 logs the change.
**Evidence tags** follow `pipeline/evidence-standard.md`. "Tested" means a planted violation run on 2026-10-10 in a throwaway directory in the CTO's scratch space, never in a checkout and never committed. Setup: Node 24.21.0, `typescript` 7.0.2, `oxlint` 1.86.0, `oxfmt` 0.71.0, `dependency-cruiser` 18.5.0, `@swc/core` 1.16.13, installed with `npm install --ignore-scripts --before=2026-10-03`. Rule names and options come from the `configuration_schema.json` shipped in `oxlint` 1.86.0, and flags from `oxlint --help` and `oxfmt --help` [E, read locally]. Registry facts come from `https://registry.npmjs.org/<name>`, the single source for what a package declares about itself. **"CSO's test" marks a result from the CSO's own run, not repeated by me** [E: `cso-m1-w1-rulings.md` §0.2 and §0.5, evidence register R22–R24, read 2026-10-10].
**Binding on:** the lint, format and dependency-graph layer of `deopea-david/haunts`. A ticket whose files contradict this record is a spec defect.

Provenance: CTO · opus (Opus 5.5) · effort high · 2026-10-10; corrected 2026-10-10 by CTO · sonnet (Sonnet 5.5) · effort high (§13)

---

## 1. Context

- **ADR-0001 §3 put most of its 17 checks on ESLint,** with typescript-eslint and `@eslint-community/eslint-plugin-eslint-comments`. dependency-cruiser holds the dependency graph (checks 3–7, and the JSON that check 8 reads). `tools/check-*.ts` scripts hold the rest.
- **The CSO approved that set on 2026-10-10, on condition T:** `typescript` moves from 7.0.2 to 6.0.3, because typescript-eslint (peer `<6.1.0`) and dependency-cruiser (`<7.0.0`) cannot use TypeScript 7.0, which ships no classic compiler API (`cso-m1-w1-rulings.md` §1.2).
- **D67 then chose Biome,** still on TypeScript 6.0.3. The CEO asked whether TypeScript 7 could be kept, and for other options. The comparison found two things:
  1. **dependency-cruiser does not need the `typescript` package to parse.** Its `parser` option also takes `swc`. Under TypeScript 7.0.2 it then found every planted boundary violation, including a type-only import, and the orphan [E, tested, comparison §4].
  2. **Oxlint's rules are ESLint's rules,** so ADR-0001's checks port almost one to one. Nesting depth, cyclomatic complexity 10, comment-skipping function length, `ban-ts-comment` with descriptions, and the `Date.now`, `Math.random` and `globalThis.fetch` bans are all native. Biome lacked several of them (comparison §3).
- **D68 adopts that combination.** This record sets out the replacement for each ESLint-held part, says plainly what is weaker, and gives every home-made guard a planted violation that must fail.

## 2. What this ADR supersedes in ADR-0001, and nothing else

| ADR-0001 | Superseded by |
|---|---|
| §2.1 layout: the two lines `eslint.config.js` and `eslint.guard.config.js` | §3.1 here |
| §3's **tool column**, for checks 2, 3, 4, 5, 6, 7 (parser only), 8(d), 11, 12, 13, 14 and 17 | §4 here |
| §3 **check 9, parts (a)–(c)**, and the basis on which CSO condition C1 is met | §5 here |
| §3 **"New development dependencies"** | §6 here |
| §4 **MAINT-4**: the rules and where they live | §7 here |
| §6 follow-ups 2–4, where they name ESLint files | §10 and §11 here |
| (new) **a formatter**. ADR-0001 set none | §3.3 here |
| (new) **the nested-configuration bypass, G15** | §5.2(c) here |
| (new) **ignore files hiding code from the main pass (C37)**, and **dependency-cruiser resolving `@/` aliases (C38)** | §5.2(e), §5.2(f) here |

**Unchanged and still binding:** the layout otherwise; the dependency direction (§2.2); storage (D63); everything §2.4 carries; checks 1, 7's rules, 8(a)–(c), 9(d), 10's mechanism, 15 and 16; CAP-1's two scripts; "no import plugin"; "no production dependency"; the cost envelope; and the revisit list. **dependency-cruiser stays** for checks 7 and 8 and as the cross-check on 3–6, now parsing through `swc`. **`typescript` stays at 7.0.2**, which `haunts` already pins, so condition T is reversed; the CSO agreed (rulings §0.4).

## 3. Decision

### 3.1 Files

```
haunts/
├── .oxlintrc.json               the main configuration. Extends the two files marked (e) below, and adds
│                                checks 2 (line limit), 8(d), 12 (lint half), 13 and 14 (naming half)
├── oxlint.guard.json        (e) the guard: boundary, network and SQL rules and the guard plugin's rules ONLY.
│                                No ignorePatterns. CI also runs it alone, on a copy OUTSIDE the repository with every disable comment removed (§5.2(b))
├── .oxfmtrc.json                Oxfmt's configuration (§3.3)
├── .dependency-cruiser.cjs      unchanged in role; adds parser: "swc" (§4, check 7)
└── tools/
    ├── oxlint/
    │   ├── guard-plugin.ts      the guard rules Oxlint has no native rule for (§4), one rule per concern. Imports only `node:` built-ins (G12)
    │   ├── style-plugin.ts      check 8(d)
    │   ├── maint-4.json     (e) MAINT-4's rules. SPK-21 creates it as {}; MAINT-4 fills it (§7)
    │   └── maint-4-plugin.ts    MAINT-4 creates it (§7)
    ├── check-suppressions.ts    check 9(a), 9(c)'s description half, and C25(a) (§5.2)
    └── check-guard-pass.ts      check 9(b): "strip the comments, then lint" (§5.2)
```

- **Configuration is JSON with comments, not code.** Oxlint reads `.json` and `.jsonc` in every runtime. JavaScript and TypeScript configuration files are "experimental" [E, `oxlint --help`]. **We use JSON only.** It is data read by the binary, unlike ESLint's executable configuration [I]. **So no `oxlint.config.*` or `oxfmt.config.*` may exist anywhere**: both tools execute one if they find it (§5.2(c)).
- **The plugins are code.** Oxlint loads ESLint-format plugins listed under `jsPlugins` [E, schema]. **They are written in TypeScript:** Oxlint 1.86.0 loaded `.ts` plugin files under Node 24, through Node's type stripping [E, tested]. That keeps D41's rule that every `haunts` script is TypeScript. The plugins must use only syntax that can be erased [K, high confidence: Node's type stripping rejects enums and parameter properties].
- **`extends` composes plugins, and paths resolve from the file that names them.** With `.oxlintrc.json` extending `oxlint.guard.json` and `tools/oxlint/maint-4.json`, the guard plugin and the MAINT-4 plugin both loaded and fired in one run. The path `./maint-4-plugin.ts`, written inside `tools/oxlint/maint-4.json`, resolved next to that file [E, tested]. (Biome resolved such paths from the root, which is the opposite.)
- **`tools/structure.json` registers `tools/oxlint/`.**

### 3.2 How it runs

- **Pre-commit (`node tools/check-all.ts`), in this order:** `tools/check-structure.ts` first, so a root `oxlint.config.*` or `oxfmt.config.*` is refused before any Ox tool runs; the `@swc/core` preflight (§5.2(g)); C37's ignore check (§5.2(e)); `oxlint -c .oxlintrc.json`; `tools/check-suppressions.ts`; `oxfmt -c .oxfmtrc.json --check`; dependency-cruiser; then the other "both" checks as before.
- **CI (`node tools/check-all.ts --ci`):** all of that, plus `tools/check-guard-pass.ts`, plus the CI-only checks as before.
- **The runner always names the configuration with `-c`, for Oxlint and Oxfmt alike.** Named that way, Oxlint does not read nested configuration files or a root `oxlint.config.ts`, and Oxfmt does not execute a root `oxfmt.config.ts`. Without `-c`, a nested `.oxlintrc.json` turned a guard rule off for its folder [E, tested both], a bare `oxlint` used a root `oxlint.config.ts` to switch a guard rule off, and a bare `oxfmt --check` **ran** a root `oxfmt.config.ts` [E, CSO's test, rulings §0.5, R22–R23]. Both tools exit 1 when the file named by `-c` is missing, so naming it fails closed. That is G15 (§5.2(c)).
- **The runner never passes `--ignore-pattern`, `--ignore-path`, `-A`/`--allow` or `--quiet`**, and `check-all.ts` is Tier 1 (C37).
- **Oxlint fails closed in the three ways we tested** [E, tested, exit code 1 each time]:
  - a file it cannot parse;
  - a JS plugin that fails to load (*"Failed to load JS plugin"*);
  - a JS plugin rule that throws while linting (*"Error running JS plugin"*), even on a file with no other error.

  What it does **not** catch is a plugin rule that runs cleanly and matches nothing. Only a must-fail fixture catches that (§5.3).

### 3.3 The formatter: Oxfmt

- **ADR-0001 set no formatter,** and `haunts` has none today. Oxfmt 0.71.0 is added under D68.
- **The hook runs `oxfmt -c .oxfmtrc.json --check` and never rewrites files.** A hook that rewrites files changes what is committed behind the author's back. `npm run format` (`oxfmt -c .oxfmtrc.json`) is the convenience that writes. `--check` failed on a planted badly formatted file [E, tested in the comparison §5].
- **Configuration:** `.oxfmtrc.json` with Oxfmt's defaults, which aim to match Prettier's output [E, [oxc.rs formatter guide](https://oxc.rs/docs/guide/usage/formatter.html), retrieved 2026-10-10 in the comparison, **single source**]. SPK-21 settles whether it also formats Markdown, JSON and YAML. My default is code files only, so that documentation does not churn [J].
- **It interacts with check 13 and check 2.** Line counts depend on formatting. A formatter makes them deterministic, which is good, but the 250, 60 and 40 limits now measure formatted code [I]. Starting both together, before there is app code, avoids a later re-tune and any reformatting churn.
- **Nothing in the formatting is security-bearing,** but Oxfmt can execute code if it finds a TypeScript configuration file (§5.2(c)). An `oxfmt-ignore` comment affects only formatting [E, tested in the comparison]. `.oxfmtrc.json` stays off the protected list, which the CSO agreed **only on G15's conditions** (rulings §0.6): `-c` on every Oxfmt command, and no `oxfmt.config.*` anywhere.

## 4. Enforcement — the checks under Oxlint

Only the rows whose tool changes are listed. **N** = native Oxlint rule; **P** = a rule in `tools/oxlint/guard-plugin.ts` or `style-plugin.ts`; **S** = a script or dependency-cruiser. **G** = in `oxlint.guard.json` (so in the guard pass); otherwise in `.oxlintrc.json`. Each check still needs a planted violation that fails before it is trusted (D32), and `prove-checks` re-proves it on every PR.

| # | Check (unchanged) | Tool under ADR-0002 | Where | Tested? |
|---|---|---|---|---|
| 2 | Thin routes: imports | N `no-restricted-imports`, scoped to `src/app/**` by `overrides`, as a deny-all group with `!` exceptions for a feature's `index.ts`, `@/ui`, `expo-router` and `react` | G | patterns: yes. The `!` form: **no**, fixture in SPK-21 |
| 2 | Thin routes: ≤ 40 lines | N `max-lines` 40, scoped by `overrides` | main | yes (comparison) |
| 3 | No imports between features | N `no-restricted-imports` `patterns`; dependency-cruiser | G | yes |
| 4 | One public door | N `no-restricted-imports` `patterns`; dependency-cruiser | G | same mechanism as 3 [I] |
| 5 | Domain purity: imports | N `no-restricted-imports`, scoped to `src/core/domain/**` | G | [I] |
| 5 | `Date.now()`, `Math.random()` | N `no-restricted-properties`, scoped the same way | G | yes |
| 5 | Argument-less `new Date()` | P `guard/no-clock`. Oxlint has no `no-restricted-syntax` [E, schema] | G | yes; `new Date(iso)` passes |
| 6 | Only `core/store` touches storage | N `no-restricted-imports` (`expo-sqlite`, `modules/capture`) outside `core/store`; SQL text placement P; native half S, unchanged | G | [I] |
| 7 | Dependency direction, cycles, orphans | dependency-cruiser, rules unchanged, **`parser: "swc"`**, **`options.tsConfig: { fileName: "tsconfig.json" }` and a `not-to-unresolvable` rule (C38)**. Also N `import/no-cycle` | S | **yes, under TypeScript 7.0.2**: relative, type-only, `export *`, `import()`, `require`, and the orphan (comparison §4). **Aliases: only with C38** (CSO's test); fixture `f1-alias` |
| 8(d) | Core exports only functions, types, constants | P `style/core-exports`, scoped to `src/core/**` | main | no: fixture in SPK-21 |
| 11 | Network globals, bare names | N `no-restricted-globals` | G | yes |
| 11 | Through `globalThis`, `global`, `window`, `self` | N `no-restricted-properties`, one entry per global object and name | G | yes, for `globalThis.fetch` |
| 11 | Networking imports (C2's list) | N `no-restricted-imports`, with `importNames` for `expo-file-system`'s network functions | G | [I] |
| 11 | `Image.prefetch`; remote `expo-image` and `Image` sources | N `no-restricted-properties` for `Image.prefetch`; P `guard/no-remote-source` for a `source` or `uri` that is not a local asset | G | no: fixture in SPK-21 |
| 12 | Lint half | N `typescript/no-explicit-any`; N `typescript/ban-ts-comment` with `ts-ignore` and `ts-nocheck` banned and `ts-expect-error: "allow-with-description"` | main | `ban-ts-comment`: yes |
| 13 | Size | N `max-lines` 250 (tests exempt by `overrides`); N `max-lines-per-function` 60 (`skipBlankLines`, `skipComments`); N `complexity` 10 (cyclomatic, as ADR-0001); N `max-depth` 3; N `max-params` 3 | main | all five: yes |
| 14 | Naming, lint half | N `unicorn/filename-case` (kebab-case); N `import/no-default-export`, off for `src/app/**` by `overrides`. The rest stays in `check-structure.ts` | main | yes |
| 17 | Agent early warning (optional) | The hook runs `oxlint -c .oxlintrc.json` on the edited file | — | — |
| C8 | SQL never built from strings | P `guard/no-sql-strings`: a template literal with substitutions, `+`, `.concat(…)` or `.join(…)` as the first argument of the methods #355 lists | G | template and `+`: yes |
| C26(a) | Computed global access; `eval` and its kin | P `guard/no-computed-global`, including through `as` casts and non-null assertions; N `no-eval`, `no-new-func`, `no-implied-eval` | G | yes, including `(globalThis as any)["fe" + "tch"]` |
| C26(b) | `require` and `import()` take literals | P `guard/literal-import` for `import()`; N `import/no-dynamic-require` | G | yes |
| C26(c) | `NativeModules` and kin only in `modules/capture/index.ts` | N `no-restricted-imports` with `importNames` (`react-native`, `expo-modules-core`); P `guard/no-native-registry` for access through a namespace import; exception by `overrides` | G | no: fixture in SPK-21 |
| C29 | One opener per database file | P `guard/db-opener`: `openDatabaseAsync` and `openDatabaseSync` only in the two opener files, each with a string literal naming its own file | G | no: fixture in SPK-21 |

**What is weaker in this table, stated plainly:**
- **Six guard rules are JS plugin rules** (`no-clock`, `no-sql-strings`, `no-computed-global`, `literal-import`, `no-native-registry`, `db-opener`), plus `no-remote-source`. Under ESLint they were built-in `no-restricted-syntax` selectors. **Oxlint's own schema says JS plugins *"are in alpha and not subject to semver"*** [E, `configuration_schema.json`, 1.86.0]. A minor Oxlint release may change the API they use. A rule that then matches nothing fails open, so each has its own must-fail fixture (§5.3).
- **The plugins are executable code run at every commit.** That is the exposure the CSO named for ESLint configurations (rulings §2.2). It moves from the configuration into the plugin files, which is why I propose the guard plugin for Tier 1 (§9).
- **dependency-cruiser cannot read `tsconfig.json` through the TypeScript API under TypeScript 7.** It prints a "missing TypeScript" warning on every run [E, tested; `src/config-utl/extract-ts-config.mjs`: *"Silently fails if a supported version of the typescript compiler isn't available"*], so **the warning can no longer tell us that parsing failed.** My first version of this ADR said alias edges were merely typed `undetermined` and that no check broke [I]. **That was wrong for aliases:** the CSO found that an `@/features/b/internal` import from feature `a` did **not** trip the boundary rule unless `.dependency-cruiser.cjs` set `options.tsConfig` [E, CSO's test, rulings §0.5 (C38), R24]. **C38 closes it** (§5.2(f)).
- **dependency-cruiser's quiet fallback.** With `swc`'s platform binding removed, dependency-cruiser fell back to another parser **and still printed `"parser": "swc"`** [E, CSO's test, R24]. So **fixture F1 with its sentinel rule, and the W3 preflight, are the reliable signals** (§5.2(g), §5.3).
- **Nothing is dropped.** Unlike the Biome draft, every ADR-0001 number survives unchanged.

## 5. Check 9 under Oxlint: what replaces `--no-inline-config`

### 5.1 What a comment can do in Oxlint [E, tested unless marked]

These silenced a guard rule in 1.86.0 (comparison §3.1):
- `// oxlint-disable-next-line <rule>`, and the same **with no rule, which silences every rule** on the line;
- `// oxlint-disable-line <rule>`;
- `/* oxlint-disable */` for the rest of the file, and `/* oxlint-disable <rule> */` … `/* oxlint-enable */` for a range;
- a JS plugin rule named in any of those forms (`guard/no-clock`).

ESLint-style comments (`eslint-disable*`) are honoured by default. **`respectEslintDisableDirectives: false` turns that off**; both forms then still failed [E, tested]. **Rule-configuration comments** (`/* eslint no-restricted-globals: "off" */`) are not honoured, in either the `eslint` or the `oxlint` spelling [E, tested]. So C25(a)'s original concern does not arise in Oxlint.

**Found by the CSO's tests after the first version of this ADR** [E, CSO's test, rulings §0.5, R22]:
- **Aliases.** A disable that names a rule by an alias is honoured: `// oxlint-disable-next-line eslint/no-restricted-globals` silenced the network rule, and `@typescript-eslint/no-explicit-any` and `typescript-eslint/no-explicit-any` each silenced `typescript/no-explicit-any`.
- **Case.** `OXLINT-DISABLE-NEXT-LINE` and `Oxlint-Disable-Next-Line` were **not** honoured.
- **Three shapes are honoured:** no space after `//`; a block comment carrying `oxlint-disable-next-line`; and a JSX comment, `{/* oxlint-disable-next-line … */}`.

What Oxlint does **not** have:
- **No switch to ignore disable comments** [E, `oxlint --help`, 1.86.0. Its options are `denyWarnings`, `maxWarnings`, `reportUnusedDisableDirectives`, `respectEslintDisableDirectives`, `typeAware` and `typeCheck`, from its schema].
- **No requirement that a disable carries a description.** A bare disable is accepted [E, tested].

What Oxlint does natively:
- **An unused disable is an error** with `reportUnusedDisableDirectives: "error"` (exit 1) [E, tested]. That is check 9(c)'s first half, unchanged.

### 5.2 The replacement: a scan, a guard pass, and `-c`

**(a) `tools/check-suppressions.ts`, in the hook and in CI.** It replaces check 9(a), the description half of 9(c), and C25(a). **It uses an allow-list, not a deny-list** (C25(a) as re-ruled, rulings §0.5).

- **Why.** My first version built a protected list from the rule names in `oxlint.guard.json` and compared names literally. Oxlint honours aliases (§5.1), so a literal comparison lets `eslint/no-restricted-globals` through. In CI the guard pass would still catch a guard rule, but **checks 2, 12, 13 and 14 are not in the guard pass**, so an alias would silence them everywhere.
- **What it reads.** Every file with a C25(b) code extension under `src/` and `modules/*/` (the JavaScript side). It finds every comment containing `oxlint-` or `eslint`, **matched regardless of case** (Oxlint honours only lower case, but the scan should not depend on that), in **all three shapes Oxlint honours** (§5.1).
- **A comment passes only if all of the following hold:**
  - it is `oxlint-disable-next-line` or `oxlint-disable-line`;
  - it names at least one rule;
  - **every rule it names is on the allow-list**, a constant in the script: **`func-style`, `prefer-arrow-callback`, and names beginning `maint-4/`** (MAINT-4's rules, §7);
  - it ends with `-- <reason>`.
- **So it fails on:**
  - a disable naming no rule;
  - a block or file form (`/* oxlint-disable */`, `oxlint-enable`);
  - **any `eslint`-prefixed comment of any kind:** disables and rule-configuration comments alike. They do nothing under `respectEslintDisableDirectives: false`, and allowing a second syntax only invites confusion;
  - **any rule not on the allow-list**: guard rules, `guard/*` and `style/*` plugin rules, checks 2, 12, 13 and 14, and every alias of any of them;
  - a missing `-- reason`.
- **Adding a rule to the allow-list is a Tier 1 change,** because it makes a rule possible to silence.
- **What would lift the allow-list requirement:** a deny-list that maps every alias Oxlint accepts to its rule and passes the five alias and shape fixtures (§5.3). The allow-list is preferred because it does not need to know the aliases.

Each message names the fix: change the code, or ask the CTO to change the rule. **This is the comment scan the Coordinator's commission names.**

**(b) `tools/check-guard-pass.ts`, in CI only.** It replaces check 9(b), the guard pass. This is **"strip the comments, then lint"**:
1. Make a temporary directory with **`fs.mkdtemp` under `os.tmpdir()`, outside the repository**, and copy into it only files with C25(b) code extensions under `src/` and `modules/*/`, plus `oxlint.guard.json` and `tools/oxlint/guard-plugin.ts`.
2. In the copy, replace every `oxlint-disable` and `eslint-disable` token with an inert token.
3. Run the locked binary: `oxlint -c oxlint.guard.json --no-ignore --deny-warnings` on the copy.

**This gives the property `--no-inline-config` gave: no comment can silence the guard pass.** On the comparison's planted files, every silenced violation came back as an error, and the one clean file passed [E, tested]. Two more things follow from copying code only:
- **no nested configuration reaches the copy** (G15);
- **no ignore file reaches it either, `.gitignore` included, only because the copy is outside the repository.** My first version said `--no-ignore` "covers ignore files" and relied on it. **It does not cover `.gitignore`:** Oxlint honours `.gitignore`, and `--no-ignore` did not override it [E, CSO's test, rulings §0.5 (C1(b)), R22]. A copy inside the repository would inherit the repository's ignore rules. `--no-ignore` stays on the command line as a second guard, not as the control. `oxlint.guard.json` sets no `ignorePatterns` (a Tier 1 file).

**(c) G15, configuration files that change what runs: closed by `-c`, with a structure check behind it. Widened to Oxfmt and to JavaScript configuration files** (rulings §0.5).
- **The bypasses** [E, tested both ways, 2026-10-10; Oxfmt and the JavaScript names from the CSO's test, R22–R23]:
  - a `.oxlintrc.json` in any folder turns rules off for that folder when Oxlint finds configuration itself; with `-c` it is not read;
  - a bare `oxlint` loads a root `oxlint.config.ts`, and in the CSO's run used it to switch a guard rule off; under `-c` it was ignored;
  - **Oxfmt executes a TypeScript configuration file:** with `.oxfmtrc.json` removed, a bare `oxfmt --check` found a root `oxfmt.config.ts` and **ran** it (the CSO's marker file was written); with `-c .oxfmtrc.json` it did not.
- **The control:**
  - `check-all.ts`, the agent hook (check 17) and the guard pass always pass `-c`, **to Oxlint and to Oxfmt**; the hook runs `oxfmt -c .oxfmtrc.json --check`, never a bare `oxfmt`. Both tools exit 1 when the file named by `-c` is missing.
  - **`tools/check-structure.ts` fails on any `.oxlintrc*` or `.oxfmtrc*` outside the repository root, and on any `oxlint.config.*` or `oxfmt.config.*` anywhere, the root included.** §3.1 says we use JSON only, so a JavaScript configuration file has no legitimate place. A bare `oxlint` or `oxfmt`, run in an editor or by hand, then also sees one configuration.
- **The JavaScript and TypeScript configuration names**, which my first version inferred from `--help` and did not test, are now tested for both tools by the CSO [E, CSO's test]. The structure check still matches by prefix.

**(d) Check 9(d) is unchanged.** There is no known-violations file, and never `--ignore-known`.

**(e) C37, ignore files cannot hide code from the main pass.**
- **The finding** [E, CSO's test, rulings §0.5, R22]: `.eslintignore` and `.gitignore` each silenced `oxlint -c .oxlintrc.json` for the paths they list. **`.gitignore` did so even for a file git still tracks,** and `--no-ignore` did not override it.
- **Why it matters:** the guard pass escapes this because it lints a copy outside the repository. But **checks 2, 12, 13 and 14 run only from `.oxlintrc.json`**, so one line in `.gitignore` would switch them off for a folder.
- **The control:** `check-structure.ts` fails on any `.eslintignore`; `check-all.ts` fails when `git ls-files -ci --exclude-standard` lists any file (a tracked file that an ignore rule matches; none at `cffa5d6` [E, rulings §0.5]); and it never passes `--ignore-path` or `--ignore-pattern`.

**(f) C38, dependency-cruiser must resolve `@/` aliases.** `.dependency-cruiser.cjs` sets `options.tsConfig: { fileName: "tsconfig.json" }` **and** includes a `not-to-unresolvable` rule (`to: { couldNotResolve: true }`, severity `error`). Without `tsConfig`, an `@/` import across a boundary was caught only by the unresolvable rule, not the boundary rule; with it, the edge resolved and the boundary rule fired [E, CSO's test, R24]. Fixture `f1-alias` (§5.3).

**(g) `@swc/core` conditions W1–W3** (rulings §0.3). **W1:** `--ignore-scripts` on every install, on every machine and in CI, because `@swc/core`'s `postinstall`, if it ran and the binding failed to load, would `npm install` `@swc/wasm` from outside our lockfile. **W2:** fixture F1 with its sentinel rule (§5.3). **W3:** `tools/check-all.ts` calls `parseSync` from `@swc/core` on a one-line TypeScript snippet before running dependency-cruiser, and if that throws, **stops with a message naming `npm ci --ignore-scripts`** (the quiet fallback, §4).


### 5.3 Planted-violation fixtures (each under `tools/guard-fixtures/`; each must fail unless marked)

**For the home-made guards:**

| Fixture | Planted | Must fail |
|---|---|---|
| `9a-bare` | `// oxlint-disable-next-line` (no rule) above `fetch(u)` | `check-suppressions` |
| `9a-rule` | `// oxlint-disable-next-line no-restricted-globals -- x` above `fetch(u)` | `check-suppressions` |
| `9a-line` | `fetch(u); // oxlint-disable-line no-restricted-globals -- x` | `check-suppressions` |
| `9a-file` | `/* oxlint-disable */` at the top of a file calling `fetch` | `check-suppressions` |
| `9a-range` | `/* oxlint-disable no-restricted-globals */` … `/* oxlint-enable */` | `check-suppressions` |
| `9a-plugin` | `// oxlint-disable-next-line guard/no-clock -- x` above `new Date()` in `core/domain` | `check-suppressions` |
| `9a-alias-eslint` (C25(a)) | `// oxlint-disable-next-line eslint/no-restricted-globals -- x` above `fetch(u)` | `check-suppressions` (not on the allow-list) |
| `9a-alias-ts` (C25(a)) | `// oxlint-disable-next-line @typescript-eslint/no-explicit-any -- x` above an `any` | `check-suppressions` |
| `9a-nospace` | `//oxlint-disable-next-line no-restricted-globals -- x` above `fetch(u)` | `check-suppressions` |
| `9a-block-next-line` | `/* oxlint-disable-next-line no-restricted-globals -- x */` above `fetch(u)` | `check-suppressions` |
| `9a-jsx` | `{/* oxlint-disable-next-line no-restricted-globals -- x */}` above a JSX line calling `fetch(u)` | `check-suppressions` |
| `9a-eslint` | `// eslint-disable-next-line no-restricted-globals -- x` above `fetch(u)` | `check-suppressions`, **and** `oxlint` (the comment is not honoured) |
| `9a-config-comment` (C25(a)) | `/* eslint no-restricted-globals: "off" */` | `check-suppressions` |
| `9a-size` | `// oxlint-disable-next-line max-lines-per-function -- x` | `check-suppressions` (check 13 is not on the allow-list) |
| `9a-allowed` | `// oxlint-disable-next-line maint-4/arrow-only -- reads this` above a `function` that reads `this` | **passes** (`"fails": false`). Proves the scan is not blanket: the rule is on the allow-list. Lands with MAINT-4, which creates the rule |
| `9b-guard-pass` | `9a-rule`'s file, with the scan **not** run | `check-guard-pass` |
| `9b-ignore-file` | an `.eslintignore` and a `.gitignore` listing `src/features/look/`, beside a file there calling `fetch` | `check-guard-pass` (a violation in a `.gitignore`d path must still fail, because the copy is outside the repository) |
| `9c-unused` | `// oxlint-disable-next-line max-depth -- x` with nothing to suppress | `oxlint` (`reportUnusedDisableDirectives`) [tested] |
| `9c-no-reason` | `// oxlint-disable-next-line typescript/no-explicit-any` with no `-- reason` | `check-suppressions` |
| `g15-nested-config` | `src/features/look/.oxlintrc.json` turning `no-restricted-globals` off, beside a file calling `fetch` | `oxlint -c` (the hook) **and** `check-structure` **and** `check-guard-pass` |
| `g15-js-config` | a root `oxfmt.config.ts` and a root `oxlint.config.ts` | each fails `check-structure` |
| `c37-eslintignore` | an `.eslintignore` listing a folder | `check-structure` |
| `c37-tracked-ignored` | a tracked file matched by an ignore rule. Its `command` builds a throwaway git repository in a temporary directory, because a nested `.git` cannot be committed [I] | `check-all` (`git ls-files -ci --exclude-standard`) |

**For the JS plugins (G12, extended).** Each guard plugin rule has its own must-fail fixture, so a rule that silently stops matching after an Oxlint update turns the build red: **`guard-plugin.ts` imports nothing but `node:` built-ins,** so a file outside Tier 1 cannot change a guard rule: with a helper file, the plugin failed to load in the guard pass, exit 1 [E, CSO's test, R22]. **Four rules have not been run yet** (`no-native-registry`, `db-opener`, `no-remote-source`, `core-exports`), so their fixtures are the first evidence they work.
- `5-new-date`;
- `c8-template`, `c8-concat`;
- `c26a-computed`, `c26a-cast`;
- `c26b-import`;
- `c26c-namespace`;
- `c29-opener`;
- `11-remote-source`;
- `8d-class-export` (the style plugin).

Plus `g12-plugin-load`, a copy of the guard configuration naming a plugin path that does not exist, which must fail [tested: exit 1].

**For the parsers (F1 re-proved, F2 replaced):**
- `f1-swc`: a `.ts` file using TypeScript-only syntax (`interface`, `satisfies`) importing across a forbidden boundary must fail `depcruise`. Run with the sentinel below.
- **`f1-type-only` (new), with a sentinel rule:** the only violation is an `import type` across a boundary. It must fail `depcruise`. **On its own that does not prove the parser is `swc`** (my first version said it did). With `swc`'s binding removed, dependency-cruiser fell back, still printed `"parser": "swc"`, and still failed this fixture, recording the edge as `import`; with `parser: "acorn"` set it also caught the edge. The comparison's richer fixture saw `acorn` miss a type-only edge (§4 row a′). Both are true: whether the fallback sees the edge depends on the file [E, CSO's test, R24]. **So the fixture's own configuration adds a sentinel rule that matches only `dependencyTypes: ["type-only"]`, and its `expect.json` requires the sentinel rule's name in the message.** The sentinel fired with `swc` and stayed silent without it [E, CSO's test]. The W3 preflight (§5.2(g)) is its partner on every commit.
- **`f1-alias` (new, C38):** an `@/` import across a feature boundary must fail `depcruise` **with the boundary rule's name**, not only the unresolvable rule's. The fixture carries its own `tsconfig.json` with `paths` for `@/` [I].
- `f2-parse` (replaces F2): a `.ts` file Oxlint cannot parse must fail `oxlint` [tested: exit 1, *"Expected `,` or `)`"*]. F2's original subject, typescript-eslint meeting an unsupported TypeScript, no longer exists, because no lint tool here loads `typescript`.

**For the formatter:** `fmt-check`, a badly formatted file, must fail `oxfmt --check`.

### 5.4 What is weaker than ADR-0001, plainly

1. **Check 9(a) and 9(b) are now our code, not the tool's.**
   - ESLint's `--no-inline-config` is maintained and tested by the ESLint project. Ours is maintained by us and tested only by our fixtures [J].
   - An Oxlint release that adds a new disable spelling would pass the scan until we notice. The guard pass (b) is robust to a new *form* of `oxlint-disable`, because it removes the token wherever it appears. **But a token spelt differently would get past both** [I].
2. **The guard rests partly on an alpha API.** Seven rules (§4) are JS plugin rules, *"alpha and not subject to semver"*. Their fixtures turn breakage red, but cannot stop it happening, and a broken plugin rule blocks every commit until it is fixed [J].
3. **More executable code on the security path:** the scan, the guard pass and the plugins, all ours, where ESLint had built-in `no-restricted-syntax`.
4. **dependency-cruiser's parse-failure signal is gone** (§4). F1 and `f1-type-only` replace it.
5. **`@swc/core` is a native binary with an install script** (`postinstall: node postinstall.js`). It is inert under `--ignore-scripts`; the platform binary arrives as an optional dependency, and parsing still worked without the script running [E, tested]. The CSO refused it once as Jest's transform (rulings §1.5). It is needed here for a different job (§6), and **the CSO approved it for that job on conditions W1–W3** (rulings §0.3; §5.2(g)).
6. **Oxfmt is pre-1.0** (0.71.0). Its failure mode is formatting churn, not security [J].
7. **Owner change in progress.** VoidZero, which maintains Oxc, states it is joining Cloudflare [E, [voidzero.dev](https://voidzero.dev/), retrieved 2026-10-10 in the comparison, **single source**].

**What is better than ADR-0001 as adopted:**
- **TypeScript 7.0.2 stays.** No lint tool loads `typescript`, so F2's failure class disappears.
- **The configuration is data,** not executable JavaScript.
- **Every ADR-0001 number survives.**
- **The guard pass removes the token itself** rather than trusting a flag.
- **The JS plugins are in ESLint's plugin format** [E, schema], so a return to ESLint would carry them over unchanged [I]. That keeps the lock-in low.

## 6. Development dependencies (approved by the CSO, 2026-10-10)

**Status.** The CSO ruled on this set in revision 2 (`cso-m1-w1-rulings.md` §0.1, candour PR #33): `oxlint` 1.86.0 and `oxfmt` 0.71.0 **approved on G12 and G15 as re-ruled**; `@swc/core` 1.16.13 **approved on conditions W1–W3**; `dependency-cruiser` 18.5.0, `jest` 30.5.2 and `@babel/preset-typescript` 7.29.7 approved, unchanged; `eslint`, `typescript-eslint` and the eslint-comments plugin dropped, their approvals lapsed; condition T reversed. She reproduced the totals below (406 lockfile entries; 327 on one machine) [E, rulings §0.1, R19]. The text below is my original resolution, kept for the record.

Resolved on 2026-10-10 against `haunts` `main` at **`cffa5d6`** with `npm install --package-lock-only --ignore-scripts --save-dev --save-exact --before=2026-10-03` [E, local lockfile]. `package.json` and `package-lock.json` are identical at `dc9a0a0` and `cffa5d6` [E, `git diff`], so the comparison's figures carry over. Registry facts: `npm view <name>@<pin>`, 2026-10-10 [E, single source for what each package declares].

| Change | Package | Exact pin | Licence | Published | Notes |
|---|---|---|---|---|---|
| **Add** | `oxlint` | **1.86.0** | MIT | 2026-09-28 | 19 per-platform bindings in the lockfile, one per machine. **No install script.** Optional peers `oxlint-tsgolint` and `vite-plus`, **neither installed** |
| **Add** | `oxfmt` | **0.71.0** | MIT | 2026-09-28 | 19 per-platform bindings, one per machine; one dependency (`tinypool` 2.2.0). **No install script.** Optional peers `svelte` and `vite-plus`, not installed |
| **Add** | `@swc/core` | **1.16.13** | Apache-2.0 | 2026-09-30 | **`postinstall: node postinstall.js`**, inert under `--ignore-scripts`. 12 per-platform binaries (Apache-2.0 AND MIT), one per machine; `@swc/counter`, `@swc/types`. Optional peer `@swc/helpers`, not installed. **Approved on W1–W3** (§5.2(g)) |
| **Drop** | `eslint` | ~~10.12.0~~ | | | approved 2026-10-10; no longer needed |
| **Drop** | `typescript-eslint` | ~~8.71.0~~ | | | approved on condition T; no longer needed |
| **Drop** | `@eslint-community/eslint-plugin-eslint-comments` | ~~4.8.1~~ | | | no longer needed |
| Keep (approved) | `dependency-cruiser` | 18.5.0 | MIT | 2026-09-30 | now with `parser: "swc"`; F1 re-proved (§5.3) |
| Keep (approved) | `jest` | 30.5.2 | MIT | | |
| Keep (approved) | `@babel/preset-typescript` | 7.29.7 | MIT | | |
| **Condition T reversed** | `typescript` | **7.0.2** (the approved 6.0.3 is not applied) | Apache-2.0 | 2026-07-08 | `haunts` already pins 7.0.2, so **its `package.json` line does not change**. commitlint's loader (peer `typescript >=5`) already runs on it today. H5's 38-case suite re-proves that |

**The whole SPK-21 set** [E, lockfiles resolved the same way]:

| | ESLint set (approved, TS 6.0.3) | **D68 set (TS 7.0.2)** |
|---|---|---|
| New lockfile entries | 424 | **406** |
| Installed on one machine (macOS arm64) | 392 | **327** (comparison §6) |
| Install scripts | `@parcel/watcher`, `unrs-resolver` (Jest's) | **the same two, plus `@swc/core`** |
| Registry host; integrity hashes | all `registry.npmjs.org`; all present | the same [E, lockfile] |
| Licences of the 406 | — | MIT 339, ISC 26, `Apache-2.0 AND MIT` 11 (the `@swc/core-*` binaries), BSD-3-Clause 9, Apache-2.0 9, BlueOak-1.0.0 8, BSD-2-Clause 1, 0BSD 1, `(MIT OR CC0-1.0)` 1, CC-BY-4.0 1. **No copyleft** [E, lockfile] |

- **Not added:** `oxlint-tsgolint`, for type-aware rules. No ADR-0001 check needs type information. It would bring its own Go TypeScript binary, and it would need a separate approval if ever wanted (§12).
- **New trust:** three native binaries per machine (Oxlint, Oxfmt, `swc`). They run on developer machines and the CI runner, never in the app.
- **No production dependency.** Unchanged from ADR-0001.

## 7. MAINT-4 — the arrow-function rule under Oxlint (replaces ADR-0001 §4's "how it lands" and "the rules")

- **The rule is unchanged** (`docs/conventions.md`, "TypeScript style").
- **It gets its own file:** `tools/oxlint/maint-4.json`, which `.oxlintrc.json` extends. SPK-21 creates it as `{}`, and MAINT-4 fills it. **No file is shared between the two tickets any more**, which removes the one exception in the wave plan's file-ownership rule. There is still one Oxlint invocation and no second linter.
- **The rules:**
  - N `func-style: ["error", "expression"]` flags a `function` declaration.
  - N `prefer-arrow-callback` flags a callback.
  - **Neither flags a `function` expression assigned to a `const` or used as an object value, nor `export default function`** [E, tested]. ESLint behaves the same, so ADR-0001's design had the same gap [I].
  - **P `maint-4/arrow-only`** in `tools/oxlint/maint-4-plugin.ts`, about 15 lines, closes those cases.
- **What the plugin flags** [E, tested on MAINT-4's acceptance cases, 2026-10-10]:
  - **Flagged:** a declaration (by `func-style`); a `function` expression assigned to a `const`, used as a callback, or used as an object property value; `export default function`.
  - **Not flagged:** class methods, constructors, getters and setters; object shorthand methods, getters and setters; generator expressions.
- **`this` and `arguments`: a change from the comparison, made to fit MAINT-4's acceptance case.**
  - The case says these exceptions *"are explained with an inline suppression comment"*. The comparison's plugin skipped such functions. A suppression there would then have been unused, and failed check 9(c).
  - **The plugin therefore flags them too.** The author keeps the `function` form with `// oxlint-disable-next-line maint-4/arrow-only -- reads this` (or `-- reads arguments`).
  - Tested: both suppressions were honoured and **not** reported as unused, and the rule fired on the same functions without them [E, tested].
  - The scan accepts them, because `maint-4/*` is on its allow-list and a reason is given.
- **Route files** are written `const VenueRoute = () => <VenueScreen />; export default VenueRoute;`, as ADR-0001 §4 said.
- **On check 9(a)'s allow-list.** ADR-0001 §4 left MAINT-4's rules unprotected; under the allow-list: `func-style`, `prefer-arrow-callback` and `maint-4/*` are the only rules a line-level disable may name (§5.2(a)). MAINT-4's rules are not guard rules.
- **The plugin is executable code,** so MAINT-4's PR carries a `## CSO note` under check 10. Its tier is the CSO's call; I propose Tier 2 (§9).

## 8. Fallbacks

**(1) If the CSO refuses `@swc/core` (not taken: she approved it on W1–W3, rulings §0.3): drop dependency-cruiser and read the graph from TypeScript 7 itself.**
- **What it is.** The comparison calls this route B in §1 and row (c) in §4; **the two labels name the same route**, a slip in my memo.
- **How it works.** A Tier 1 script, `tools/check-graph.ts`, runs `tsc -p tsconfig.json --explainFiles` on the pinned TypeScript 7.0.2. It reads the compiler's own resolution of every import, then applies `tools/structure.json`'s allow-list (check 7). It finds orphans (a file *"Matched by include pattern"* with no *"Imported via"* line) and enforces C28. It writes the JSON that `check-core.ts` reads (check 8(a)–(c)).
- **What else changes.** Oxlint's `import/no-cycle` takes cycles. `import/no-commonjs` bans `require` outright, because `tsc` did not list a bare `require(...)` [E, tested, comparison §4]. C26(b) already bans non-literal `require`, so a full ban costs little [J]. The comparison counts this set at **287 packages on one machine**, with no second parser or compiler of any kind [E, comparison §6, for Oxlint without Oxfmt; Oxfmt adds about 3, I].
- **What it is worth.** About 150–250 lines and 6–10 h [J].
- **What it weakens.** A mature graph tool on the security path becomes a home-made parser of human-readable output with no stability promise. A format change could make it see no edges and pass. **Its fixtures must therefore include one that fails when the script parses zero edges from a non-empty project, or meets an output line it does not recognise.** It also needs one must-fail fixture per edge kind: relative, alias, type-only, `export *`, `import()`, plus the orphan.

**(2) If the CSO refuses JS plugins as guard controls:** I have no fallback that keeps Oxlint whole. The seven plugin rules would need a parser, so the choices are ESLint for the guard pass alone, or Biome's declarative GritQL plugins (comparison §3). **That would come back to the CEO as a new decision**, not be settled here.

**(3) If Oxlint itself goes unmaintained:** the configuration uses ESLint's rule names and the plugins use ESLint's plugin format, so **a return to ESLint is the cheapest exit** [I]. ESLint's set is already CSO-approved, except for condition T.

## 9. What the CSO must approve or re-rule

I do not approve dependencies or edit the CSO's files. For the CSO, under D68. **Status 2026-10-10: ruled.** Her revision 2 (`cso-m1-w1-rulings.md` §0) approved the set, reversed condition T and re-ruled the rows below; the rows are corrected to match her rulings.

| Item | What changes | Where in this ADR |
|---|---|---|
| **Dependencies** | Add `oxlint` 1.86.0, `oxfmt` 0.71.0, `@swc/core` 1.16.13. Drop `eslint`, `typescript-eslint`, `@eslint-community/eslint-plugin-eslint-comments`. Keep `dependency-cruiser`, `jest`, `@babel/preset-typescript` | §6 |
| **Condition T** | Reverse it: `typescript` stays at 7.0.2. No lint tool loads `typescript`, and dependency-cruiser parses through `swc` | §1, §6 |
| **C1** | Re-ruled: ESLint's `--no-inline-config` is gone. It is met by the scan, the "strip the comments, then lint" guard pass **run on a copy outside the repository** (`--no-ignore` does not override `.gitignore`), and `respectEslintDisableDirectives: false` | §5.2 |
| **C25(a)** | Re-ruled: `eslint-comments/no-use` is gone. The scan uses an **allow-list** (`func-style`, `prefer-arrow-callback`, `maint-4/*`), allows only `oxlint-disable-next-line` and `oxlint-disable-line` with a rule and a reason, and fails on every `eslint` comment, rule-configuration comments included. It matches case-insensitively and sees three shapes | §5.2(a) |
| **F1** | Re-proved with `swc`, plus `f1-type-only` **with a sentinel rule** (without it, it does not prove the parser), the W3 preflight, and `f1-alias` (C38) | §5.2(f)–(g), §5.3 |
| **F2** | Retired as written: typescript-eslint is gone. Replaced by `f2-parse` | §5.3 |
| **G12** | Extended to JS plugins: one must-fail fixture per plugin rule, plus `g12-plugin-load`. The quiet-failure risk moves from "tool cannot parse" to "plugin rule matches nothing" | §3.2, §5.3 | `guard-plugin.ts` imports only `node:` built-ins |
| **G15 (new)** | Configuration files that change what runs. Closed by `-c` on **every Oxlint and Oxfmt command**, the structure check (`.oxlintrc*` and `.oxfmtrc*` outside the root; `oxlint.config.*` and `oxfmt.config.*` anywhere) and the guard pass | §5.2(c) |
| **C37 (new)** | Ignore files cannot hide code from the main pass | §5.2(e) |
| **C38 (new)** | dependency-cruiser resolves `@/` aliases | §5.2(f) |
| **W1–W3 (new)** | `@swc/core`: `--ignore-scripts` always; the sentinel; the fail-closed preflight | §5.2(g) |
| **Protected-list tier names** | Tier 1: `eslint.guard.config.js` → **`oxlint.guard.json`** and **`tools/oxlint/guard-plugin.ts`**; `tools/check-*.ts` now also covers `check-suppressions.ts` and `check-guard-pass.ts` (and `check-graph.ts` under fallback 1). Tier 2: `eslint.config.js` → **`.oxlintrc.json`**, **`tools/oxlint/style-plugin.ts`**, **`tools/oxlint/maint-4.json`** and **`tools/oxlint/maint-4-plugin.ts`**. Unlisted (my proposal): **`.oxfmtrc.json`**. Rulings §2.2's "`eslint*.config.js` (an ESLint config is executable JavaScript)" now applies to the plugin files, not the configuration | §3.1, §4, §7 |
| **Check 10's path list** (`tools/traceability.ts`) | Follows the tiers above | — |

**The CSO decided** whether `@swc/core`'s new job justifies it after the earlier refusal: **it does, on W1–W3** (rulings §0.3). Fallback 1 is not taken.

## 10. Consequences

**What gets easier:**
- **TypeScript 7.0.2 stays,** with no lint tool loading `typescript`.
- **ADR-0001's checks port with their numbers intact.** The CSO's rulings, written in ESLint terms, mostly still read true.
- **Fewer packages than the approved ESLint set:** 406 lockfile entries against 424, and 327 on one machine against 392 (§6).
- **The configuration is data.**
- **MAINT-4 owns files of its own,** so W1 no longer needs a shared-file exception.
- **A formatter from the first line of app code.**
- **Speed.** The CEO named Oxlint's design for throughput and large codebases. I did not measure it [K, moderate confidence that it is much faster than ESLint].

**What gets harder:**
- **More code of our own to keep:** two scripts (`check-suppressions.ts`, `check-guard-pass.ts`) and about eight plugin rules on an alpha API.
- **A new bypass class (G15)** to keep closed.
- **`@swc/core`** with its install script and about 15 lockfile entries, until dependency-cruiser supports TypeScript 7.1.
- **Dependabot's Oxlint PRs need the CSO's eye,** because a minor release may break a plugin.
- **PLAT-1 (#267) changes.** The CSO ruled to install `eslint-plugin-react-hooks` (rulings §1.7), and there is no ESLint to plug it into. Oxlint's native `react/rules-of-hooks` and `react/exhaustive-deps` [E, schema] are the replacements, to be verified against React's rules at PLAT-1. PLAT-1's CTO region is edited when W2 is prepared, not today.

**What it costs** [J]:
- **About the same one-off hours as ADR-0001's 42–69 h.**
  - The scan and the guard pass take about 6–10 h, and the plugins about 4–6 h.
  - That is roughly offset by writing one Oxlint configuration rather than two ESLint ones.
  - Oxfmt adds 1–2 h.
- **£0 to run.**

**Replacement lines for the wave plan** (applied on PR #31 on 2026-10-10; kept for the record) (candour PR #31, branch `docs/haunt-m1-wave-plan`, `products/haunt/architecture/m1-wave-plan.md` at `9d2b383`), for the Coordinator to route. The commission named §3.1 and §4. §0 and §8 also name ESLint, so their lines are here too.

- **§0, line 24.** Replace the sentence with: *"**No two tickets in the same wave list the same file.** There is no exception: MAINT-4's rules live in their own file, `tools/oxlint/maint-4.json`, which SPK-21 creates as `{}` and `.oxlintrc.json` extends (ADR-0002 §7)."*
- **§3.1, line 64.** Replace with: *"**The dependency cannot be split away.** MAINT-4's rules need Oxlint installed and wired into the hook and CI, and SPK-21 is what installs and wires it. ADR-0002 §7 gives MAINT-4 its own extended file, so there is still one Oxlint invocation and no second linter."*
- **§3.1, line 66.** Replace with: *"**The split:** SPK-21 creates `tools/oxlint/maint-4.json` as `{}` and makes `.oxlintrc.json` extend it. MAINT-4 fills that file, adds `tools/oxlint/maint-4-plugin.ts`, its fixtures and its documentation change. **No file is listed by both tickets.** MAINT-4 still starts after SPK-21 merges, because it needs Oxlint installed."*
- **§3.1, line 67.** Replace with: *"**Why SPK-21 does not install Jest-Expo or React Native Testing Library**, although ADR-0001 §3 lists them: they need `expo` and `react-native` installed as peers [K, medium], and those are product dependencies, which a spike may not land. They arrive with PLAT-1 in W2. Expo's ESLint configuration is no longer wanted (D68, ADR-0002 §10): PLAT-1 uses Oxlint's native `react/rules-of-hooks` and `react/exhaustive-deps`, verified there, so the import-plugin flag falls away."*
- **§4, line 111 (table row).** Replace with: *"| `.oxlintrc.json`, `oxlint.guard.json`, `.oxfmtrc.json`, `tools/oxlint/` | All lint rules; the guard; the formatter; plugins | SPK-21 creates all of them. MAINT-4 then owns `tools/oxlint/maint-4.json` and `tools/oxlint/maint-4-plugin.ts` only (§3.1). Guard files: any PR touching them carries a `## CSO note` (check 10) |"*
- **§8, line 159.** Replace *"MAINT-4 (it edits `eslint.config.js`, a guard file under check 10)"* with *"MAINT-4 (it fills `tools/oxlint/maint-4.json` and adds a JavaScript plugin, both under check 10)"*.
- **§8, lines 162–164.** Replace the three ESLint bullets with two: *"- `oxlint` and `oxfmt` (D68, ADR-0002 §6)"* and *"- `@swc/core`, as dependency-cruiser's parser under TypeScript 7 (D68, ADR-0002 §6)"*.
- **§8, line 168.** Replace *"and Expo's ESLint configuration (see the import-plugin flag in §3.1)"* with *"(Expo's ESLint configuration is no longer wanted: D68, ADR-0002 §10)"*.

## 11. Follow-ups

| # | Item | Owner |
|---|---|---|
| 1 | Approve or refuse the §6 set; re-rule the §9 items; rename the tiers. The Tier 1 changes need the CEO's approval | CSO, done 2026-10-10 (rulings §0); CEO's approval of the Tier 1 changes still to come |
| 2 | Edit SPK-21 (#355) and MAINT-4 (#308) to this layout | CTO, done 2026-10-10 |
| 3 | Route the wave-plan lines (§10) | Coordinator; done (PR #31, 2026-10-10) |
| 4 | PLAT-1 (#267): Oxlint's React rules in place of `eslint-plugin-react-hooks`, verified | CTO at W2 preparation; CSO |
| 5 | MAINT-4's generated text (its title, *"ESLint enforces the arrow-function preference"*, and *"when ESLint arrives"*) comes from `backlog-plan.md` §5, which only regeneration may change. The plan's MAINT-4 entry should name Oxlint | PM/BA |
| 6 | `docs/conventions.md` §7 names ESLint. MAINT-4 changes it, as that ticket already lists. §9.2's `typescript` row stays at 7.0.2, so SPK-21 no longer edits it | Engineer |
| 7 | Write the CSO's revision 2 rulings into SPK-21 (#355) and keep this ADR in step with it | CTO, done 2026-10-10 |

## 12. Revisit when

- **dependency-cruiser supports TypeScript 7.1's public API** (its v18.1.0 note expects to) [E, quoted in the comparison §4]. Then set `parser` back to `tsc` and drop `@swc/core`.
- **The CEO's concern (D68): dependency-cruiser goes unmaintained, or lags a TypeScript major.** The trigger is any one of these [J on the thresholds]:
  - no dependency-cruiser release for six months;
  - a TypeScript syntax we use that `swc` cannot parse, shown by F1 or `f1-type-only` going red;
  - dependency-cruiser still unable to use TypeScript 7 three months after TypeScript 7.1 ships.

  **Then take fallback 1 (§8):** the graph script reading TypeScript's own `--explainFiles` output. **With `swc` as the parser, a new TypeScript major matters less than it did,** because dependency-cruiser no longer reads TypeScript's API to parse. What matters is whether `swc` parses the syntax we write, which F1 tests on every PR [I].
- **Oxlint ships a way to ignore disable comments, or to forbid disabling named rules.** Then retire `check-guard-pass.ts` and most of `check-suppressions.ts`.
- **Oxlint changes its disable syntax or adds a new form.** Then update the scan and add a fixture in the same Dependabot PR.
- **Oxlint stops letting `.gitignore` override `--no-ignore`, or dependency-cruiser reads `tsconfig.json` without being told.** Then C37 or C38 is redundant, and the CSO would withdraw it (rulings §0.8).
- **JS plugins leave alpha** (a semver promise). Then lighten the Dependabot caution. **Oxlint adds `no-restricted-syntax`.** Then move the plugin rules to native selectors where they fit.
- **VoidZero's move to Cloudflare changes Oxc's licence, ownership or release cadence.** Then weigh fallback 3 (§8).
- **Oxfmt reaches 1.0, or churns formatting between minors.** Then re-check pins and the line limits.
- **Type-aware rules are wanted** (for example `no-floating-promises`). Then `oxlint-tsgolint`, built on TypeScript 7, under a new CSO approval.

## 13. Change log

| Date | Change |
|---|---|
| 2026-10-10 | Adopted (D68). Supersedes ADR-0001 §2.1's two ESLint lines, §3's tool column for the checks in §4, check 9(a)–(c), §3's dependency list, and §4. Adds Oxfmt and G15. Replaces D67's Biome, for which no ADR was committed. |
| 2026-10-10 | Corrected against the CSO's revision 2 rulings (`cso-m1-w1-rulings.md` §0), adding no new decision. **Three claims overturned by her tests:** (i) `f1-type-only` does not prove `swc` runs, so it gains a sentinel rule, with the W3 preflight (§5.2(g), §5.3); (ii) the suppression scan uses an allow-list, because Oxlint honours rule-name aliases (§5.2(a), §5.1); (iii) the guard pass copies the tree outside the repository, because `--no-ignore` does not override `.gitignore` (§5.2(b)). **Added:** C37 (§5.2(e)), C38 (§5.2(f)), W1–W3 (§5.2(g)), G15 widened to Oxfmt and to JavaScript configuration files (§3.2, §3.3, §5.2(c)), the alias, case and shape findings (§5.1), the new fixtures (§5.3), and the status of §6, §8 and §9. §10's wave-plan lines and §11 are marked as done |
