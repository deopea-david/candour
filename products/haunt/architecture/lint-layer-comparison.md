# Lint layer: Biome against Oxlint with Oxfmt, and the routes to TypeScript 7

**Seat:** CTO · **Date:** 2026-10-10 · **Status:** A tested comparison for the CEO to choose from. **Nothing here changes ADR-0001, D67, SPK-21 (#355), MAINT-4 (#308) or any ticket.** ADR-0002 will be written for the CEO's choice.
**Asked by:** the CEO, 2026-10-10, through the Coordinator. In his words: *"I feel downgrading to TS 7 for a single tool is not best practice. It is an important tool but are there any other options available, other than the ones listed?"* and *"Oxlint with Oxfmt is an interesting choice as well, replacing eslint & prettier/biome."* The comparison was then commissioned with his "Yes please".
**Supersedes nothing.** An ADR-0002 draft for Biome on TypeScript 6 exists in my worktree. It is **not committed** and stops here, as instructed.
**Evidence tags** follow `pipeline/evidence-standard.md`. "Tested" means a planted violation run on 2026-10-10 in throwaway directories in my scratch space, never in a checkout and never committed. Setup: Node 24.21.0, **`typescript` 7.0.2**, `oxlint` 1.86.0, `oxfmt` 0.71.0, `oxlint-tsgolint` 7.0.2003, `@biomejs/biome` 2.5.15, `dependency-cruiser` 18.5.0, `@swc/core` 1.16.13. Everything was installed with `npm install --ignore-scripts --before=2026-10-03`, so every package is at least 7 days old (D43's cooldown). Registry facts come from `https://registry.npmjs.org/<name>`, the single source for what a package declares about itself. Rule names come from each tool's shipped `configuration_schema.json` [E, read locally].

Provenance: CTO · opus (Opus 5.5) · effort high · 2026-10-10

---

## 1. The answer, for the CEO

1. **TypeScript 7 is reachable now, by two tested routes.** Neither Biome nor Oxlint needs the `typescript` package, so the only blocker was dependency-cruiser.
   - **Route A: keep dependency-cruiser and switch its parser to `swc`.** Under TypeScript 7.0.2 it found every planted boundary violation: relative, `@/` alias, type-only, `export *`, dynamic `import()` and `require`. It found the orphan too [E, tested]. **What it costs:** `@swc/core`, a second TypeScript parser. It is a native binary with an install script (inert under `--ignore-scripts`), and it adds about 37 packages per machine. dependency-cruiser also prints a permanent "missing TypeScript compiler" warning.
   - **Route B: drop dependency-cruiser and read the import graph from TypeScript 7 itself** (`tsc --explainFiles`). **This is the only route with no second compiler or parser of any kind.** On the same fixture it listed every edge except a bare `require(...)`, with real compiler resolution [E, tested]. **What it costs:** a home-made script of about 150–250 lines that reads text output with no stability promise. `require` must also be banned outright, which is cheap.
2. **For the lint layer, Oxlint is the better fit than Biome** [J, moderate confidence]. Its rules *are* ESLint's rules, so ADR-0001's checks port almost one to one. That includes things Biome lacks: `max-depth`, cyclomatic `complexity` 10, `Date.now`/`Math.random`/`globalThis.fetch` bans through `no-restricted-properties`, and `ban-ts-comment` with descriptions. Pointing it at its configuration with `-c` stops nested configuration files from silencing it, which Biome cannot do [E, tested].
3. **Neither tool has ESLint's `--no-inline-config`** [E, both `--help`]. For both, check 9(b) becomes the same home-made guard pass: copy the code, remove every disable token, and lint the copy with the guard configuration. **I tested that on both tools, and it turned every silenced violation back into an error** [E, tested].
4. **Oxlint's weak point is its plugin system.** About six of the CSO's guard rules need custom rules. In Oxlint those are **JavaScript plugins, which its own schema calls "alpha and not subject to semver"** [E, schema], and they are executable code run at every commit. Biome's equivalents are declarative GritQL files.
5. **Oxfmt costs little now and touches only check 13 and the hook** (§5). It is pre-1.0 (0.71.0).

**My recommendation** [J, moderate confidence]: **Oxlint with Oxfmt, plus dependency-cruiser on the `swc` parser (route A), on TypeScript 7.0.2.** Keep route B as the fall-back if the CSO refuses `@swc/core`. §7 gives the reasons and what it weakens.

## 2. What changed since D67

D67 adopted Biome while `typescript` stayed at 6.0.3. The reason it stayed was dependency-cruiser: its TypeScript parser needs the classic compiler API, which TypeScript 7.0 does not ship (`cso-m1-w1-rulings.md` §1.2). **Today's finding is that dependency-cruiser does not have to use that parser.** Its `parser` option also accepts `acorn` and `swc` [E, `src/main/options/normalize.mjs` and `src/meta.cjs` at 18.5.0: `swc: ">=1.0.0 <2.0.0"`]. I had not tested that before, and `biome-option.md` §1 should have. **That is a gap in my earlier note, and it changes its first finding:** Biome *can* reach TypeScript 7 after all, by route A or route B.

## 3. The lint layer, check by check

**Key:** **N** = native rule · **P** = plugin (Biome: GritQL; Oxlint: JavaScript plugin) · **S** = a `tools/check-*.ts` script, or dependency-cruiser · **✗** = not possible in the tool. "Tested" = shown on a planted violation today, or in `biome-option.md` for Biome where marked (b-o).

| Check | Biome 2.5.15 | Oxlint 1.86.0 | Evidence |
|---|---|---|---|
| 1 Folder allow-list | S (unchanged) | S (unchanged) | — |
| 2 Thin routes: imports, ≤ 40 lines | N `noRestrictedImports`, `noExcessiveLinesPerFile`, scoped by `overrides` | N `no-restricted-imports`, `max-lines`, scoped by `overrides` | both line limits tested |
| 3 No imports between features | N `noRestrictedImports` patterns; + S | N `no-restricted-imports` patterns; + S | both tested |
| 4 One public door | N; + S | N; + S | same mechanism [I] |
| **5** Domain purity: imports | N | N | [I] |
| **5** `Date.now()`, `Math.random()` | **P** | **N** `no-restricted-properties` | both tested |
| **5** argument-less `new Date()` | **P** | **P** (no `no-restricted-syntax` in Oxlint [E, schema]) | both tested; `new Date(iso)` passed in both |
| 6 Only the store touches storage; SQL placement | N + P; native half S | N + P; native half S | [I] |
| 7 Dependency direction, cycles, orphans | S (§4) | S (§4) | §4 |
| 8 (a)–(c) | S (§4) | S (§4) | §4 |
| 8(d) Core exports only functions, types, constants | P | P | not tested |
| **9(a)** Guarded rules cannot be disabled by comment | **S**: scan | **S**: scan | §3.1 |
| **9(b)** Guard pass ignores disable comments (C1) | **✗ built in; S** (strip-and-run) | **✗ built in; S** (strip-and-run) | both tested, §3.1 |
| 9(c) Unused disables are errors | N with `--error-on-warnings` | N `reportUnusedDisableDirectives: "error"` | both tested |
| 9(c) Every disable needs a description | **N**: a suppression without one is a parse error | **S**: Oxlint accepts a bare disable | both tested |
| 9(d) No known-violations file | S | S | — |
| 10 Guard files need a note | S (path list changes) | S (path list changes) | — |
| **11** Network globals, bare names | N `noRestrictedGlobals` | N `no-restricted-globals` | both tested |
| **11** Through `globalThis.fetch` | **P** | **N** `no-restricted-properties`, one entry per global object | both tested |
| **11** Networking imports | N | N | [I] |
| 12 No `any`; no `@ts-ignore`; `@ts-expect-error` only with a description | N `noExplicitAny`, `noTsIgnore`; description: **S** | **N** `typescript/no-explicit-any`, `typescript/ban-ts-comment` (`allow-with-description`) | Oxlint tested; Biome [E, schema] |
| **13** 250 lines a file | N `noExcessiveLinesPerFile` | N `max-lines` (`skipBlankLines`, `skipComments`) | both tested |
| **13** 60 lines a function, blank lines and comments skipped | N, but **comments counted** (no option) | N `max-lines-per-function` with both skips | Oxlint tested; Biome [E, schema] |
| **13** Complexity 10 | **Cognitive** complexity only: re-tune | **N** `complexity` 10, cyclomatic, as ADR-0001 | Oxlint tested |
| **13** Nesting depth 3 | **✗** (no rule; drop or P) | **N** `max-depth` | Oxlint tested; Biome [E, schema] |
| **13** 3 parameters | N `useMaxParams` | N `max-params` | Oxlint tested |
| 14 Kebab-case files; no default exports outside routes | N `useFilenamingConvention`, `noDefaultExport` | N `unicorn/filename-case`, `import/no-default-export` | Oxlint tested |
| 15, 16 | S (unchanged) | S (unchanged) | — |
| 17 Agent hook | runs Biome | runs Oxlint | — |
| **MAINT-4** | N `useConsistentFunctionStyle` (**nursery**) + `useArrowFunction`; `export default function` needs **P** | N `func-style` + `prefer-arrow-callback` catch only declarations and callbacks. **`const f = function…`, object values and `export default function` need P** | both tested on all MAINT-4 acceptance cases (§3.3) |
| **C8** SQL from strings | P | P | both tested |
| **C26(a)** Computed global access, including `(globalThis as any)[…]`; `new Function`; implied eval | P for computed access and `new Function`; `noGlobalEval` N; implied eval nursery or P | P for computed access; **N** `no-new-func`, `no-eval`, `no-implied-eval` | both tested, including the cast form |
| **C26(b)** Literal `require`/`import()` | P | P (`import/no-dynamic-require` is N for `require`) | both tested |
| C26(c) `NativeModules` and kin | N or P | N `no-restricted-imports` or P | not tested |
| C29 One opener per file | P | P | not tested |

**Counts** [I, from the table]: of the rows above, **Oxlint does natively nine things Biome needs a plugin, a script or a re-tune for**: `Date.now`/`Math.random`, `globalThis.fetch`, `@ts-expect-error` descriptions, cyclomatic complexity, nesting depth, comment-skipping function length, `new Function`, implied eval, and literal `require`. **Biome does natively two things Oxlint needs a plugin or script for**: a mandatory suppression description, and MAINT-4's function-expression cases.

### 3.1 Suppression handling: check 9 and CSO C1

**Neither tool can ignore disable comments in a run.**
- Biome has no such flag [E, `biome lint --help`, 2.5.15].
- Oxlint has none either [E, `oxlint --help`, 1.86.0; its options are `denyWarnings`, `maxWarnings`, `reportUnusedDisableDirectives`, `respectEslintDisableDirectives`, `typeAware` and `typeCheck`, from its schema].

| | Biome | Oxlint |
|---|---|---|
| Comment forms that silenced a guard rule [E, tested] | `biome-ignore` with an exact rule, a group (`lint/style`) or the bare category `lint`; `-all`; `-start`/`-end`; `lint/plugin` and `lint/plugin/<name>`; block comment; no space | `oxlint-disable-next-line` with a rule or with no rule (that silences everything); `oxlint-disable-line`; `/* oxlint-disable */` for the whole file; a JS-plugin rule by name |
| ESLint-style comments | not read | `eslint-disable*` is honoured by default. **`respectEslintDisableDirectives: false` turns that off** [E, tested: both forms then still failed] |
| Rule-configuration comments (`/* eslint rule: "off" */`) | none exist [E, [suppressions](https://biomejs.dev/analyzer/suppressions/), retrieved 2026-10-10, single source] | not honoured, in either the `eslint` or the `oxlint` form [E, tested]. C25(a)'s concern does not arise |
| Description required | **yes**: without one it is a parse error and the rule still fires [E, tested] | **no** [E, tested] |
| Unused disable fails | with `--error-on-warnings` [E, tested] | with `reportUnusedDisableDirectives: "error"` [E, tested] |
| **Nested configuration file silences the guard (a new bypass, "G15")** | **Yes, even with `--config-path` set to the guard file**, and excluding `**/biome.json` does not stop it [E, tested]. Needs a structure check | **No when the configuration is named with `-c`** [E, tested]. It does apply when Oxlint finds its own root configuration, so the hook also passes `-c` or `--disable-nested-config` |

**The replacement for `--no-inline-config` is the same for both** [E, tested on both]:
- **(1) A scan, `tools/check-suppressions.ts`, in the hook and in CI.** It fails on any disable comment naming a protected rule, a group, a whole category, a plugin, or no rule at all. Under Oxlint it also fails on a disable without a `-- reason`. A prototype for Biome failed all 12 planted forms and passed an allowed one.
- **(2) A guard pass, `tools/check-guard-pass.ts`, in CI.** It copies only code files into a temporary directory, replaces every disable token, and runs the guard configuration on the copy. Under Oxlint it also uses `-c guard.json --no-ignore`. **On both tools every silenced violation came back as an error; the one clean file passed.** This gives the property C1 asked for. It is our code rather than the tool's, which is the weakness that remains.

### 3.2 The CSO's bypass list, G1–G14

| # | Biome | Oxlint |
|---|---|---|
| G1 comment disables a rule | Scan + guard pass (§3.1) | Same, plus `respectEslintDisableDirectives: false` |
| G2 editing the configuration | Check 10 and the CEO's merge | Same |
| G3 files the linter does not read | `files.includes`; `vcs.enabled: false` | Default extensions plus `--no-ignore` in the guard pass; `check-structure.ts` either way |
| G4 computed globals | P (tested, including the cast) | P (tested, including the cast); `no-new-func`, `no-eval`, `no-implied-eval` N |
| G5 dynamic import or require | P (tested) | P for `import()`; N `import/no-dynamic-require` |
| G6 `NativeModules` and kin | N or P | N or P |
| G7 native reflection | S (unchanged) | S (unchanged) |
| G8 code hidden in `tools/` | S (graph, §4) | S (graph, §4) |
| G9 the runner switched off | `tools/check-all.ts` (unchanged) | Same |
| G10 weakening fixtures | Tier 1 (unchanged) | Same |
| G11 not running the hook | Unchanged | Unchanged |
| **G12 a tool failing quietly** | Biome needs no `typescript`. A path outside `files.includes` exits 1 [E, tested] | Oxlint needs no `typescript`. **New quiet-failure risk:** a JS plugin that throws or silently matches nothing. Each needs a fixture that must fail |
| G13 a general-purpose opener | P | P |
| G14 SQL from strings | P (tested) | P (tested) |
| **G15 nested configuration (new)** | **Open in the tool; closed by a structure check** | **Closed by `-c`** |

### 3.3 MAINT-4 [E, tested on its acceptance cases]

- **Biome:** `useConsistentFunctionStyle` (`style: "expression"`, a **nursery** rule) plus `useArrowFunction` flag a declaration, a `function` expression assigned to a `const`, a callback, and an object property value. They do **not** flag class members, getters and setters, shorthand methods, generators, or functions reading `this` or `arguments`. **`export default function` is not flagged**, so a GritQL plugin flags it (tested).
- **Oxlint:** `func-style: "expression"` flags only the declaration, and `prefer-arrow-callback` only the callback. **A `function` expression assigned to a `const` or used as an object value is not flagged, and neither is `export default function`.** That is ESLint's behaviour, so ADR-0001's own MAINT-4 design had the same gap [I]. A 20-line JavaScript plugin rule closed every case: everything flagged that should be, and nothing flagged that should not be (tested).
- **Under either tool, the `this` and `arguments` exceptions need no suppression comment,** because the rules do not flag them. An unnecessary suppression would fail 9(c) as unused.

### 3.4 Oxlint's JavaScript plugins and type-aware mode

- **JS plugins** take ESLint's plugin format. Oxlint's schema says: *"JS plugins are in alpha and not subject to semver"* [E, `configuration_schema.json`, 1.86.0]. In my tests, four guard rules (computed global access including through a cast, literal `import()`/`require`, SQL from strings, and argument-less `new Date()`) worked as written for ESLint, under TypeScript 7.0.2 [E, tested]. **Two cautions** [J]:
  - A minor Oxlint release may break a plugin. Every plugin rule therefore needs a must-fail fixture, and Dependabot's Oxlint PRs need the CSO's eye.
  - A plugin is JavaScript executed at every commit. That is exactly the exposure the CSO named for ESLint configurations (rulings §2.2), so plugin files belong on Tier 1.
- **Type-aware mode** (`--type-aware`) needs the separate `oxlint-tsgolint` package. Version 7.0.2003 is built on TypeScript 7. With `typescript` 7.0.2 installed, `typescript/no-floating-promises` fired on a planted floating promise [E, tested]. It brings its own platform binary of the Go TypeScript (6 platform entries, one per machine) [E, lockfile]. **No ADR-0001 check needs type information, so I would not install it now** [J]. It is the route to typescript-eslint's type-aware rules later, if wanted.

### 3.5 The tools themselves

| | Biome | Oxlint | Oxfmt |
|---|---|---|---|
| Version (≥ 7 days old) | 2.5.15 (2026-09-30) | **1.86.0** (2026-09-28). 1.87.0 (2026-10-05) is inside the cooldown | **0.71.0** (2026-09-28). Pre-1.0 |
| Licence | `MIT OR Apache-2.0` | MIT | MIT |
| Packages | 1 + 8 per-platform; 2 install per machine | 1 + per-platform bindings; 2 per machine (§6) | 1 + per-platform bindings |
| Install scripts | none | none | none |
| Needs `typescript` | no | no (optional peer `oxlint-tsgolint` for type-aware only; optional peer `vite-plus`, not installed) | no |
| Who maintains | The `biomejs` organisation's "Core Contributors", funded by sponsors and Open Collective; no company owner [E, [github.com/biomejs/biome](https://github.com/biomejs/biome), retrieved 2026-10-10] | **VoidZero Inc.**, which describes itself as *"the creators, maintainers, and contributors"* of Oxc, with Vite, Vitest and Rolldown alongside [E, [voidzero.dev](https://voidzero.dev/), retrieved 2026-10-10, **single source**]. Oxc's README: *"part of VoidZero's vision for a unified, high-performance toolchain"* [E, [github.com/oxc-project/oxc](https://github.com/oxc-project/oxc), retrieved 2026-10-10]. npm publisher: `boshen` [E, registry] | Same as Oxlint |
| Governance signal | Community project | **The same VoidZero page announces "VoidZero is joining Cloudflare"** [E, single source]. That is a change of owner in progress. I read it as neutral-to-positive for funding and unknown for direction [J] | Same |

**The CEO's reputation point holds as far as I can verify it** [I]. VoidZero states that it maintains Oxc, and Vite and Vitest are among the most-used JavaScript tools [K, high confidence]. The pending Cloudflare move is the one thing to watch.

## 4. The folder allow-list (checks 7 and 8) under TypeScript 7.0.2

Fixture, the same for every route: two features, `a` and `b`. `a` imports `b/internal` six ways: relative; through the `@/` alias; type-only (`import type`) from a `.tsx` file with JSX; `export * from`; dynamic `import()`; and `require()`. A `.ts` file uses TypeScript-only syntax (`interface`, `satisfies`). There is also an orphan file in `core/domain`.

| Route | Under TS 7.0.2 | Result [E, tested] |
|---|---|---|
| **(a) dependency-cruiser 18.5.0, `parser: "swc"`** (`@swc/core` 1.16.13) | Works | **All six edges found, including type-only (`tsPreCompilationDeps`) and the alias. The orphan was found. Exit code non-zero.** Two caveats: dependency-cruiser warns `missing-typescript-transpiler` on every run, so a genuinely missing parser can no longer be told apart by that warning; and alias edges are typed `undetermined` rather than `aliased`, because it cannot read `tsconfig.json` through TypeScript's API [E, `src/config-utl/extract-ts-config.mjs`: *"Silently fails if a supported version of the typescript compiler isn't available"*]. Our rules match on paths, not dependency types, so neither caveat breaks a check [I] |
| (a′) the same, `parser: "acorn"` (no extra package) | Works, partly | Found the five value edges and the orphan; **missed the type-only edge**. Not acceptable as the guard, but it shows the CSO's F1 concern is real [I] |
| **(b) restricted-import rules generated from `tools/structure.json`, plus a graph script** | Works for 3–6 | The linter's `no-restricted-imports` patterns are tested above. Two points: the rules are a deny-list, so a generator must write "everything except the allowed arrows" for each folder; and they match the import **text**, not the resolved file. **Oxlint's `import/no-relative-parent-imports`** [E, schema] would force every cross-folder import through `@/`, which makes text matching reliable [I]. **Orphans and check 8 still need a graph,** which is route (c) |
| **(c) a graph from TypeScript 7 itself: `tsc -p tsconfig.json --explainFiles`** | Works | **Listed five of the six edges, with the compiler's own resolution: alias, type-only (both imports of `rel.ts`), `export *`, `import()`. It did not list the bare `require(...)`.** The orphan shows as *"Matched by include pattern"* with no *"Imported via"* line, so orphans are detectable. `--traceResolution` also works [E, tested]. **No second parser or compiler.** Weak points: the output is human-readable text with no stability promise, so a format change could make the script see no edges and pass. That needs a must-fail fixture (F1's job). And `require` must be banned outright (`import/no-commonjs` in Oxlint, or a plugin in Biome). C26(b) already bans non-literal `require`, so a full ban costs little [J] |
| Oxlint's own import rules | Partial | `import/no-cycle` covers cycles. **No allow-list, orphan or restricted-paths rule exists** [E, schema rule list] |

**My reading** [J]: **(a) is the safest guard now.** dependency-cruiser's allow-list mode is what the CSO approved for checks 3–7 and C28, and `swc` is its own documented parser option rather than a workaround. **(c) is the cleanest end state,** with one TypeScript and no parser beside it, but it puts a home-made text parser on the security path. When dependency-cruiser supports TypeScript 7.1's public API (its v18.1.0 note expects that), route (a) can drop `swc` and use the one TypeScript.

## 5. Oxfmt

- **ADR-0001 sets no formatter,** and `haunts` has none today [I, from `package.json` at `dc9a0a0`].
- **What it costs:** 3 more packages on one machine, 21 lockfile entries [E, lockfile]. One more step in `check-all.ts` (`oxfmt --check`). A configuration file. Setting it up takes about 1–2 h [J]. There is **no reformatting churn**, because there is no app code yet, so this is the cheapest moment it will ever be.
- **What it touches:**
  - **Check 13 and check 2.** Line counts depend on formatting. A formatter makes them deterministic, which is good, but the 250/60/40 numbers then measure formatted code [I]. Starting both together avoids a later re-tune.
  - **Nothing security-bearing.** An ignore comment (`// oxfmt-ignore`, tested) affects only formatting. The configuration is Tier 2 at most, or unlisted (the CSO's call).
- **What it is:** pre-1.0 (0.71.0) [E, registry]. Its documentation says it *"aims to match Prettier's output"* and lists known divergences [E, [oxc.rs formatter guide](https://oxc.rs/docs/guide/usage/formatter.html), retrieved 2026-10-10, single source]. It formatted a planted badly formatted file and `--check` failed on it [E, tested].
- **If Biome is chosen,** Biome's own formatter does the same job with no extra package [K, high confidence].

## 6. The combinations, measured

Each set was resolved on 2026-10-10 against `haunts` `dc9a0a0` with `--package-lock-only --ignore-scripts --before=2026-10-03`. Each includes `jest` 30.5.2 and `@babel/preset-typescript` 7.29.7, as the CSO approved. "One machine" = macOS arm64 [E, lockfiles]. Every entry resolves to `registry.npmjs.org` with an integrity hash. No set has a copyleft licence.

| Set | `typescript` | New lockfile entries | One machine | Install scripts | Second TS parser or compiler |
|---|---|---|---|---|---|
| ESLint + typescript-eslint + dependency-cruiser (CSO-approved) | 6.0.3 | 424 | 392 | Jest's 2 | — (TS 6 is the one TypeScript) |
| Biome + dependency-cruiser (D67 as drafted) | 6.0.3 | 359 | 320 | Jest's 2 | — |
| Biome + dependency-cruiser on `swc` | **7.0.2** | 374 | 324 | Jest's 2 **+ `@swc/core`** | `swc` |
| Biome + `tsc --explainFiles` script | **7.0.2** | 326 | **287** | Jest's 2 | **none** |
| Oxlint + dependency-cruiser on `swc` | **7.0.2** | 385 | 324 | Jest's 2 **+ `@swc/core`** | `swc` |
| **Oxlint + Oxfmt + dependency-cruiser on `swc`** (recommended) | **7.0.2** | 406 | 327 | Jest's 2 **+ `@swc/core`** | `swc` |
| Oxlint + `tsc --explainFiles` script | **7.0.2** | 337 | **287** | Jest's 2 | **none** |
| Oxlint + `oxlint-tsgolint` (type-aware, not recommended now) | **7.0.2** | 344 | 289 | Jest's 2 | tsgolint's bundled Go TypeScript |

`@swc/core` declares `postinstall: node postinstall.js` [E, registry]. It did not run under `--ignore-scripts`, and dependency-cruiser still parsed with `swc`, because the platform binary arrives as an optional dependency [E, tested]. **The CSO has already refused `@swc/core` once**, as Jest's transform: *"a third install script and a third native binary for a job the preferred option does with neither"* (rulings §1.5). **The job here is different:** without it, dependency-cruiser cannot see type-only edges under TypeScript 7 (route a′). Whether that is enough is the CSO's call.

## 7. Recommendation [J, moderate confidence]

**Oxlint 1.86.0 + Oxfmt 0.71.0 + dependency-cruiser 18.5.0 on the `swc` parser, with `typescript` 7.0.2 kept.**

**Why Oxlint over Biome:**
- It ports ADR-0001's checks with ESLint's own rule names and numbers. Nesting depth, cyclomatic complexity 10, comment-skipping function length and `ban-ts-comment` survive unchanged. Under Biome, three of those are lost or re-tuned.
- `Date.now`, `Math.random` and `globalThis.fetch` are native, not plugins.
- Naming the configuration with `-c` closes the nested-configuration bypass that Biome leaves open.
- The CSO's rulings, threat model and conditions are written in ESLint terms, so less of them needs re-ruling.

**Why route (a) over (c) now:**
- It keeps a mature, CSO-approved graph tool on the security path, and the setting is a single option.
- It drops `swc` again when dependency-cruiser supports TypeScript 7.1.

**What this weakens, plainly:**
1. **Check 9(a) and 9(b) become our code** (the scan and the guard pass), as under Biome. Tested, but home-made.
2. **About six guard rules become JavaScript plugins in an alpha API,** run as code at every commit. Biome's GritQL equivalents are declarative. This is the main point in Biome's favour.
3. **`@swc/core` adds a native binary and an install script** (inert under `--ignore-scripts`) and about 37 packages, until dependency-cruiser supports TypeScript 7.1.
4. **dependency-cruiser's "missing TypeScript" warning becomes permanent,** so F1's must-fail fixture is the only reliable sign that parsing works.
5. **Oxfmt is pre-1.0.** Its failure mode is formatting churn, not security.
6. **Owner change:** VoidZero is joining Cloudflare (single source).

**The one combination with no second compiler or parser at all** is Oxlint (or Biome) + a `tsc --explainFiles` graph script on TypeScript 7.0.2. It is smallest (287 packages on one machine) and was tested on the fixture. It weakens checks 7 and 8 from a mature tool to a home-made parser of unversioned text output, and requires banning `require`. **I would take it only if the CSO refuses `@swc/core`** [J].

**What would change this recommendation:**
- The CSO refusing JavaScript plugins as guard controls. That would favour Biome, whose plugins are declarative.
- The CSO refusing `@swc/core`. That means route (c).
- dependency-cruiser releasing TypeScript 7.1 support. Then use route (a) without `swc`.
- An Oxlint `--no-inline-config`, or a Biome equivalent, would retire the guard-pass script.

**What the CSO would have to approve or re-rule (for the recommended set):**
- **Add:** `oxlint` 1.86.0 (MIT), `oxfmt` 0.71.0 (MIT), `@swc/core` 1.16.13 (Apache-2.0, `postinstall`, native binary).
- **Keep:** `dependency-cruiser` 18.5.0, `jest` 30.5.2, `@babel/preset-typescript` 7.29.7.
- **Remove from the approved set:** `eslint`, `typescript-eslint`, `@eslint-community/eslint-plugin-eslint-comments`.
- **Condition T is reversed:** `typescript` stays at 7.0.2.
- **Re-rule:** C1 and C25(a) on the scan and guard pass (§3.1); F1 re-proved with `swc`; F2 retired, since typescript-eslint is gone; G12 extended to JS plugins; G15.
- **Tiers to rename:** `eslint.guard.config.js` becomes the Oxlint guard configuration and the JavaScript plugin files (Tier 1). `eslint.config.js` becomes the main Oxlint configuration and the Oxfmt configuration (Tier 2, or unlisted for Oxfmt).
- **D67 itself would need the CEO to replace it,** since it names Biome.

**One disagreement, stated once** [J]: staying one TypeScript major behind until tools support it is normal practice rather than a bad one. TypeScript 7.0 shipped without a public API, and much of the ecosystem is waiting for 7.1. So I do not think TypeScript 6.0.3 was a mistake. **But today's tests show TypeScript 7 costs little more,** so I have no objection to moving now.

## 8. Where I looked, and what I did not do

**Looked:** Oxlint 1.86.0's `--help` and `configuration_schema.json` (its options and all 871 rule names). Biome 2.5.15's `--help` and schema. dependency-cruiser 18.5.0's source (`normalize.mjs`, `meta.cjs`, `extract-ts-config.mjs`). The npm registry for every version, licence, publish date, peer and install script. Eight lockfiles resolved from `dc9a0a0`. Pages retrieved 2026-10-10: Biome's suppressions page, the Oxc and Biome GitHub READMEs, voidzero.dev, and the Oxfmt guide. Tests on planted violations: the suppression forms and the guard pass for both tools, nested configuration for both, check 5, check 11 including `globalThis`, C8, C26(a)–(b), check 13's five limits, check 12, check 14, MAINT-4's acceptance cases for both tools, Oxlint type-aware mode, dependency-cruiser on `swc` and `acorn`, `tsc --explainFiles` and `--traceResolution`, and Oxfmt `--check`.

**Not done:**
- No route-(b) generator and no route-(c) script were written beyond reading `tsc`'s output by eye.
- No timing measurements.
- C26(c), C29 and 8(d) were not tested on either tool.
- No React rules checked for PLAT-1 (Oxlint has `react/rules-of-hooks` [E, schema]; Biome has `useHookAtTopLevel` [E, schema]).
- No Linux CI run.
- The Biome draft ADR-0002 is uncommitted and incomplete by instruction.
