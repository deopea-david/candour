# Biome in place of ESLint: an option for the CEO

**Seat:** CTO · **Date:** 2026-10-10 · **Status:** An option, not a switch. Nothing here changes ADR-0001, SPK-21 (#355) or any ticket. Adopting it would need an ADR-0001 amendment, which the CEO decides, and the CSO's approval of the dependency (D40, D41).
**Asked by:** the CEO, 2026-10-10, relayed by the Coordinator: *"What if we used biome instead of eslint?"*
**Evidence tags** follow `pipeline/evidence-standard.md`. "Tested" means a planted violation run on 2026-10-10 in a throwaway directory in my scratch space. It was never in a checkout and never committed. Setup: Biome 2.5.15, TypeScript 7.0.2, Node 24.21.0, `npm install --ignore-scripts`. Biome's documentation is the single source for anything marked [E] that I did not test.

Provenance: CTO · opus (Opus 5.5) · effort high · 2026-10-10

---

## 1. The answer, for the CEO

**Biome could replace ESLint and typescript-eslint for most of the lint layer, and it runs under TypeScript 7. Two things argue against it.**

1. **It does not get us to TypeScript 7.** dependency-cruiser still needs TypeScript's compiler API. dependency-cruiser holds checks 3–7, F1 and the JSON that check 8 reads, and Biome has no allow-list dependency graph to replace it. Under 7.0.2 dependency-cruiser cruised **0 modules and passed** a planted boundary violation [E, tested]. Its own release note says support waits for TypeScript 7.1's public API: *"typescript@7.1.0 is expected to ship with a public API - so that's the first version in the TypeScript 7 (formerly tsgo) version range dependency-cruiser will be able to support"* ([v18.1.0 release](https://github.com/sverweij/dependency-cruiser/releases/tag/v18.1.0), retrieved 2026-10-10). So `typescript` 6.0.3 stays, with or without Biome.
2. **Check 9 weakens.** Any Biome rule, plugin rules included, can be silenced by a comment, and Biome has no switch that ignores suppression comments [E, tested; [suppressions](https://biomejs.dev/analyzer/suppressions/); `biome lint --help`, 2.5.15]. ESLint's `--no-inline-config` is what CI's guard pass (9(b), CSO C1) rests on. With Biome, that guard becomes a `tools/check-*.ts` text scan that fails on any `biome-ignore` naming a guarded rule or `lint/plugin`. It is workable, but it is a home-made control where ESLint's is built in [J].

**What it gives:** about 90 fewer packages, one native binary and no install script (§3), and faster lint [K]. **My recommendation** [J]: **not now.** Revisit it when dependency-cruiser supports TypeScript 7, or if lint time becomes a real cost. Then the gain would be both fewer packages and TypeScript 7, rather than fewer packages alone.

## 2. Check by check

**Key:** **N** = native Biome rule · **P** = Biome plugin (GritQL) · **S** = needs a `tools/check-*.ts` script (or stays with dependency-cruiser or `tsc`) · **✗** = not possible in Biome. "Tested" = proved on a planted violation.

| Check | What it needs | Biome | Evidence |
|---|---|---|---|
| 1 Folder allow-list | Folders only from `structure.json` | **S** (already a script) | No change |
| 2 Thin routes | Restricted imports in `src/app/`, ≤ 40 lines | **N**: `noRestrictedImports` plus `noExcessiveLinesPerFile`, scoped with `overrides` | [E, both rules and `overrides` in Biome 2.5.15's `configuration_schema.json`]; line limit tested |
| 3 No imports between features | Path patterns | **N** `noRestrictedImports` (`patterns`), and dependency-cruiser | **Tested:** `check 3: no imports between features` raised |
| 4 One public door | Deep imports refused | **N** `noRestrictedImports` patterns, and dependency-cruiser | [I], same mechanism as check 3 |
| 5 `core/domain` pure: no `Date.now()`, no argument-less `new Date()`, no `Math.random()` | Syntax bans | **P** for the three calls; **N** for the import bans | **Tested:** a plugin flagged all three, and did not flag `new Date(iso)`. Biome has no `no-restricted-syntax` |
| 6 Only `core/store` touches storage; SQL text placement | Import bans, syntax | **N** + **P**; native half **S** (as now) | [I] from checks 3 and C8 |
| 7 Dependency direction, no cycles, no orphans | Allow-list graph | **S: dependency-cruiser stays.** Biome's `noImportCycles` covers cycles only | [E, schema] |
| 8 Core cannot quietly grow (a–c), exports only (d) | Manifest, JSON graph; (d) syntax | (a–c) **S** (dependency-cruiser JSON); (d) **P** | [I] |
| **9(a)** No disabling guarded rules by comment | Disallow targeted disables | **S.** Biome cannot forbid its own suppressions | **Tested:** `// biome-ignore lint/style/noRestrictedGlobals` silenced `fetch`; `// biome-ignore lint/plugin` silenced the check-5 plugin. Docs list `biome-ignore`, `biome-ignore-all`, `-start`/`-end` and `lint/plugin` ([suppressions](https://biomejs.dev/analyzer/suppressions/)) |
| **9(b)** CI guard pass with inline config ignored | A mode that ignores suppressions | **✗ in Biome; S as a replacement** (a scan that fails on any suppression of a guarded rule) | `biome lint --help` (2.5.15) has `--suppress` (to write suppressions) and no flag to ignore them [E, run locally] |
| 9(c) Unused disables are errors | Unused-suppression report | **N** [K, moderate: Biome reports unused suppressions; not tested] | Not verified |
| 9(d) No known-violations file | dependency-cruiser | **S** (unchanged) | — |
| 10 Guard files need a note | Path list | **S** (unchanged); `biome.json` and `*.grit` would replace the ESLint configs on the Tier 1 list | — |
| **11** Network globals, including through `globalThis` | Global bans | **N** `noRestrictedGlobals` for bare names; **P** for `globalThis.x` | **Tested:** `fetch` flagged natively; `globalThis.fetch` only by a plugin. **The computed form `(globalThis as …)['fe' + 'tch']` was not caught** by my plugin (the cast wraps it). ESLint has the same limit, which C26(a) closes with a syntax ban; a plugin can do the same [I] |
| 11 Networking imports | Import bans | **N** `noRestrictedImports` | [I] |
| 12 Strict TS: no `any`, no `@ts-ignore` | Lint half | **N** `noExplicitAny`, `noTsIgnore`; `@ts-expect-error` needing a description **unverified** | [E, schema]; `tsc` half unchanged |
| **13** Size and complexity: 250 lines a file, 60 a function, complexity 10, depth 3, 3 parameters | Five limits | **N** for four: `noExcessiveLinesPerFile`, `noExcessiveLinesPerFunction`, `noExcessiveCognitiveComplexity` (cognitive, not ESLint's cyclomatic: the numbers would need re-tuning), `useMaxParams`. **Nesting depth: no native rule found**, so **P** or dropped | **Tested:** the file and function limits both fired. The others: [E, schema] |
| 14 Naming and style | Kebab-case files, no default exports | **N** `useFilenamingConvention`, `noDefaultExport` (with `overrides` for routes) | [E, schema] |
| **MAINT-4** Arrow functions only | Ban declarations and function expressions | **N:** `useConsistentFunctionStyle` (`style: "expression"`, **nursery**, so unstable) plus `useArrowFunction` | **Tested:** both fired. Nursery rules can change between minor versions [K] |
| 15 No hot shared files | Script | **S** (unchanged) | — |
| 16 No barrel files | Re-export bans | **N** `noBarrelFile`, `noReExportAll`, scoped | [E, schema] |
| 17 Agent hook | Runs the linter | **S** (would run Biome instead) | — |
| **C8** SQL not built from strings | Call-argument syntax | **P** | **Tested:** a plugin flagged a template literal with a substitution and a `+` concatenation in `run`/`runAsync`, and passed a parameterised call. Biome's recommended `useTemplate` would also nudge concatenation into template literals, so the plugin must cover both |

**The CSO's G1–G14 under Biome:**

| # | Under Biome |
|---|---|
| G1 comment disables a rule | **Worse.** Every suppression form silences plugins too, and no mode ignores them. Only a script (S) closes it |
| G2 editing the configuration | Same: check 10 and the CEO's merge. `biome.json` and `plugins/*.grit` join Tier 1 |
| G3 files the linter does not read | Same, as **S** (`check-structure.ts`) plus Biome's `files.includes` |
| G4 computed globals | **P** (a syntax ban, as C26(a)); `noGlobalEval` and `noImpliedEval` are **N** [E, schema]; `new Function` is **P** |
| G5 dynamic import or require | **P** |
| G6 `NativeModules` and similar | **N** `noRestrictedImports`/`noRestrictedGlobals` with `overrides`, or **P** |
| G7 native reflection | **S** (unchanged; Biome does not read Swift or Kotlin) |
| G8 code hidden in `tools/` | **S** (dependency-cruiser) and **N** (`noRestrictedImports`) |
| G9 the runner switched off | Same (`tools/check-all.ts`) |
| G10 weakening fixtures | Same (Tier 1) |
| G11 not running the hook | Same |
| **G12 a tool failing quietly** | **Better for lint:** Biome parses TypeScript itself and needs no `typescript` package [E, it ran under 7.0.2 with no TypeScript API]. **Unchanged for dependency-cruiser**, which needs TypeScript < 7 (§1). F1 still needed; F2 would go |
| G13 a general-purpose opener | **P** (C29) |
| G14 SQL from strings | **P** (C8, tested) |

**Counts:** of the 17 checks plus MAINT-4 and C8, Biome natively covers the lint parts of 2, 3, 4, 11 (bare names and imports), 12, 13 (four of five limits), 14, 16 and MAINT-4. Plugins cover 5, 8(d), 11 through `globalThis`, and C8. **9(a) and 9(b) move to a script, and 9(b) loses its built-in tool.** 1, 7, 8(a–c), 9(d), 10, 15 and 17 are scripts or dependency-cruiser either way.

## 3. Footprint, licence, and what the CSO would review

| | ESLint route (CSO-approved) | Biome route |
|---|---|---|
| Lint packages | `eslint` (76 new), `typescript-eslint` (16 new), `eslint-comments` plugin (1 new): **93 lockfile entries** [E, CSO rulings §1.1] | `@biomejs/biome` 2.5.15 plus 8 per-platform CLI packages: **9 lockfile entries, 2 installed on any one machine** [E, local lockfile] |
| Whole M1.W1 set, on one machine | **392** [E, CSO rulings §1.1] | **about 301** (392 − 93 + 2) [I, arithmetic on the CSO's count; not resolved as a lockfile] |
| Install scripts | none in the lint tools | **none** (`hasInstallScript` absent on all 9) [E, local lockfile] |
| Native code | none in the lint tools | **one 56 MB Rust binary per machine** (`@biomejs/cli-darwin-arm64`) [E, `du`] |
| Licence | MIT | **`MIT OR Apache-2.0`** [E, registry and lockfile] |
| Published | — | 2.5.15, last modified 2026-09-30, so past the 7-day cooldown [E, registry] |
| Needs `typescript` | yes, < 6.1 | **no**, but dependency-cruiser still does |

**What the CSO would review:** the package and its 8 platform packages (exact pin, licence, integrity, registry host); the native binary on developer and CI machines, which is new trust much like Jest's two; **the replacement for 9(b)**, a script that is stronger or weaker than `--no-inline-config` and has to be proved by fixtures; **the GritQL plugins as security controls**, which become Tier 1 files; and whether nursery rules are acceptable in a guard. `eslint-plugin-react-hooks` (PLAT-1) has no Biome equivalent I have verified. That would need checking at PLAT-1, against Biome's React domain.

## 4. Where I looked, and what would change this

**Looked:** Biome 2.5.15 installed and run in scratch on planted violations (checks 3, 5, 11, 13, MAINT-4, C8, and the suppression forms); its `configuration_schema.json` for rule names and options; `biome lint --help`; [biomejs.dev/linter/plugins](https://biomejs.dev/linter/plugins/) and [biomejs.dev/analyzer/suppressions](https://biomejs.dev/analyzer/suppressions/) (retrieved 2026-10-10); the npm registry for version, licence and platform packages; dependency-cruiser's v18.1.0 release note. **Not done:** a full lockfile resolution of the Biome route; a test of 9(c), `@ts-expect-error` descriptions, nesting depth or `useMaxParams`; the React rules.

**What would change the recommendation:**
- dependency-cruiser supporting TypeScript 7 (so the Biome route would also bring TypeScript 7);
- Biome adding a mode that ignores suppression comments, or a way to forbid suppressing named rules (which would restore 9(a) and 9(b) as built-in controls);
- lint time becoming a measured cost.
