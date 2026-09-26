# Agentic-Agile adoption — what Haunts takes from Microsoft's template, and what it does not

**Seat:** Product Manager / BA · **Date:** 2026-09-26 · **Version:** 0.1 (proposal; goes to the CEO through the orchestrator)
**Commissioned by:** the orchestrator, on the CEO's instruction to take advice from `microsoft/agentic-agile-template` before any Haunts ticket is created.
**Read against:** `constitution.md` v1.3 (Articles 1.5, 4, 5, 6); `decisions/2026-09-16-haunt-gate.md` **D27–D31**; `products/haunt/backlog-plan.md` v0.1; `backlog.csv`; `backlog-tickets.py`; `standup-routine.md` v0.1; `repo-security-baseline.md`; `code-licence-note.md`; `STATUS.md`; `requirements.md` at `7482241` (not edited). All read from disk on 2026-09-26, on branch `haunt/build-setup` at `31e23ed`.
**Also reflects:** a **CEO decision of 2026-09-26, relayed by the orchestrator during this work** — *requirement tickets include the template's files sections ("Files to create or modify", "File ownership"), marked TBD until the CTO has designed the architecture.* It is written in at §3. It is not yet in the decision record; **it should be recorded there as D32** (or whatever number is next) before the generator changes.

**Status: a proposal. Nothing has been created or changed** — no ticket, label, field, file in `haunts`, or edit to any existing Candour document. The changes this implies to our own documents are listed at §11 for the owning seats to make.

**How the template was read.** Every template file cited here was retrieved with `gh api` at commit [`491179b`](https://github.com/microsoft/agentic-agile-template/tree/491179beb2ff6a195aa29808391f75797e06996b) (the head of `main`, committed 2026-06-05) and saved outside our working tree. **The template's agent-facing files (`AGENTS.md`, the Claude adapter `CLAUDE.md`, `copilot-instructions.md`) are written to be executed by any agent that reads them** — `AGENTS.md` tells the agent to run a six-step dialogue and make two commits. **None of those instructions was followed.** They are quoted here as a document under evaluation. Nothing was cloned into `candour`, nothing was committed, and nothing on GitHub was changed.

**Evidence tags** follow `pipeline/evidence-standard.md`. Quotations from template files are [E] with a link to the file at the pinned commit. Claims about our own rules quote the clause. Where the recommendation is this seat's judgment it is tagged [J].

---

## 0. The answer on one page

**The template is sensible and mostly agrees with how Candour already works.** Its core idea — *"When you give it a well-specified story with acceptance criteria, file boundaries, and negative constraints, you get production-quality code"* [E, [README.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/README.md)] — is what `requirements.md` and D31 already do for the first two of those three. **What we lack, and should take, is the third: file boundaries, and the wave discipline that uses them.** That matters to us more than to most teams, because our Engineers run as parallel agent instances in separate worktrees.

**How much weight the template bears.** It is one source, written by its authors about their own method. The accompanying blog post offers no measured results, and says itself that this *"isn't a finished process"* [E, blog, §13 item 2]. The template's own retrospective scores its own prompts and its own work (composite 4.1/5), which is self-assessment [E, §13 item 17]. **So every "adopt" below rests on this seat's judgment of the practice's merits, not on evidence that it works** [J].

**The biggest changes to our setup:**

1. **Requirement tickets gain the template's headings** (§3). Most are filled honestly from what we already hold: Summary, Origin and context, Invariants to preserve, Negative constraints, Dependencies. **Files to create or modify, Interfaces to implement and File ownership are emitted as TBD**, per the CEO's decision, and are filled by the **CTO at wave planning, once the architecture ADR exists**. A ticket with TBD files cannot enter **Ready**. The requirement text and criteria stay exactly as D31 set them — copied in full, stamped with the SHA, the document wins.
2. **Implementation stories are the exception, not the rule** (§3.4). This overturns part of the orchestrator's starting view. With files on the requirement ticket, most requirements are the unit of work themselves. A separate story, in the template's full format, is created **only** where the CTO splits a requirement or one change serves several requirements (the schema, the CI checks). Stories reference acceptance-criterion limbs by letter and never copy criteria by hand, because D31 requires copies to be generated.
3. **Waves inside Kanban** (§4). The board stays Kanban (D30). The **CTO** groups Ready tickets into **waves** — parallel batches with no shared files and no dependencies between them — records a **Wave** field, and closes each wave with a **wave gate**: every PR reviewed at its head commit, `main` green, the next wave's interfaces written down. **A wave gate makes nothing "done"**; only the CGO's phase review pack and demo do (Constitution 5.5).
4. **Five numbers recorded from day one** (§7): merge conflicts per wave, QA first-pass rate, escaped defects (and who found them), spec defects, and **the founder's own hours per phase** — the last because `cost-sheet-v3.md` says *"Actual hours will replace it at the first yearly review."* The template's eight-dimension scoring, composite scores and prompt-quality self-grading are **rejected**.
5. **The `haunts` repo gets a lean `CLAUDE.md`, a story issue template, a PR template and a delivery log** (Appendices A–D), committed **after** the CSO's baseline, which stays the first commit (D29). **No template file is copied**, so no MIT notice is owed; an acknowledgement line is recommended anyway (§6.4).

**Does the ticket format change?** Yes, in shape; not in substance. Same requirement text, same criteria, same SHA stamp, same "document wins"; new headings around them, a TBD files block the generator never overwrites, two new labels (`spec-defect`, `escaped`, plus `level:story`), and two new board fields (`Wave`, `QA attempts`). §3.3 gives the exact heading list for `backlog-tickets.py`.

**Conflicts.** **None with the Constitution** in anything recommended for adoption. **Two practices conflict with CEO decisions and are rejected:** closing tickets from PRs (`Closes #N`) and agents moving work to done conflict with **D30** (*"only QA moves a ticket to Done"*); the template's onboarding, whose first commit is *"an exact copy of the unmodified template"*, conflicts with **D29** and STATUS.md's *"The CSO's security baseline is the repo's first commit"*. **One tension is flagged, not resolved:** the template assumes a human code reviewer; Candour has none (§8, §9).

**Layout.** §2 is the verdict on every practice; §3–§10 answer the eight questions in the brief; §11 lists the changes owed to our own documents; §12 holds the decisions and disagreements; §13 is the evidence register; Appendices A–D are the draft `haunts` files; **§14, last, lists the practices that should apply company-wide.**

**Decisions for the CEO, one at a time** (§12): **first**, approve the ticket format in §3 — including that implementation stories close when merged and never show "Done", which clarifies D30's scope. **Second**, whether he will record his own hours per phase (§7.3). Nothing else here is his to decide; waves belong to the CTO.

---

## 1. What the template is

A starter repository published by Microsoft under the MIT licence [E, [LICENSE](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/LICENSE): *"Copyright (c) 2025 Microsoft Corporation"*]. Its README carries a caution: *"Agentic-Agile methodology is an **active area of investigation** with the potential for unanticipated results"* [E, README]. Its parts:

| Part | What it is | Relevance to Haunts |
|---|---|---|
| `MANIFESTO.md` | Five values, thirteen principles | The principles are the useful part (§2) |
| `AGENTS.md` | *"Universal onboarding orchestrator"*: an agent runs a six-step dialogue and makes two commits | Rejected as a mechanism (§9); its baseline behaviours are reused |
| `.github/ISSUE_TEMPLATE/agentic-story.md` | The story format | Adapted (§3) |
| `.github/contributor-templates/CONTRIBUTOR_PR_TEMPLATE.md` | PR template for contributors **to the template itself** (adapters, combos) | Structure borrowed; content does not fit (§6.3) |
| `docs/epic-decomposition-example.md` | Epic → stories → dependency graph → waves, worked example | Adopted as the CTO's wave-planning method (§4) |
| `docs/evaluation-framework.md` | Eight measurement dimensions | Five numbers taken; the rest rejected (§7) |
| `docs/templates/retrospective.md` | Per-wave retrospective with dimension scores | Adapted into a delivery log and a review-pack section (§7) |
| `docs/agent-surface-selection.md` | Which agent surface for which task | Confirms our choice; nothing to add (§2 row 27) |
| `platform-adapters/` | Per-tool instruction files, one tracker adapter, a CI placeholder, "combos" | Rejected: we use one tool, one tracker. The Claude + GitHub + Actions combo is marked *"Status: Stub"* [E, [combo](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/combos/claude-github-github-actions.md)] |
| `.github/workflows/require-copilot-review.yml` | CI fails unless GitHub Copilot has reviewed the PR's head commit | Rejected; one idea kept (§8) |
| `STYLE.md` | Placeholder style guide | Deferred to the CTO (§6.2) |
| `mcp.json` | Example MCP config with a GitHub token, filesystem and memory servers | Rejected (§9) |
| `docs/sample-issues/`, `docs/retrospectives/` | Worked examples and the template team's own retrospective | Read as evidence of how it runs in practice |

---

## 2. Practice by practice: adopt, adapt or reject

Each row: the practice, as the template states it; Candour's existing equivalent; the verdict; why. Sections §3–§10 carry the detail for the rows that matter.

| # | Practice (template) | Candour today | Verdict | Reason |
|---|---|---|---|---|
| 1 | **Spec-first stories**: *"Agents operate against well-defined specifications with acceptance criteria, file boundaries, and negative constraints"* (Manifesto, principle 1) | `requirements.md`: 197 IDs, QA-verifiable criteria, lettered limbs; D31 puts them on tickets | **Adopt** — already largely true | The missing piece is file boundaries (row 4) |
| 2 | Story **Summary** | Ticket title is a label; no one-sentence summary | **Adopt** | Generated from the requirement's first sentence; free |
| 3 | **Originating Prompt**: *"Paste the exact prompt by default"* (story template) | CEO's words quoted in D-entries; commissions to seats not kept | **Adapt** (§5) | Requirement tickets: Origin = the decision record, linked not copied. Stories and agent runs: the orchestrator's **commission**, verbatim, as the first comment |
| 4 | **Files to Create or Modify** and **File Ownership**: *"No other story in the same wave should touch these files"* | Nothing | **Adopt** — on requirement tickets as **TBD until the CTO sets them** (CEO decision, 2026-09-26) | The one practice we lack that prevents parallel agents colliding |
| 5 | **Interfaces to Implement** | Architecture ADR (not yet written) | **Adopt**, TBD on requirement tickets; filled by the CTO | Interfaces come from the architecture, which does not exist yet |
| 6 | **Invariants to Preserve** | Promise line (§20.1), standing conditions, MEM-1, DFLT-1, PRIV-8 exist but are not on tickets | **Adapt** — generated from what we hold | Makes the product-wide rules visible where the work happens |
| 7 | **Negative Constraints** | `requirements.md` §18 (out of scope), per product | **Adapt** — product-wide exclusions linked; story-level ones set at wave planning | Honest: per-requirement negatives do not exist to generate |
| 8 | **Dependencies** | `Blocked by` field and generator map | **Adopt** — already done | — |
| 9 | Story **Delivery** section, *"Added post-implementation"* (sample issues) | QA's `Verified against` field | **Reject** | A second record of the same fact |
| 10 | **Effort Estimate** tick-box (S/M/L) (sample issues) | `CTO hours` field; SPK-08 | **Reject** | The CTO's hours are the estimate the cost sheet uses |
| 11 | **Waves**: *"Work executes in small parallel batches with review gates between them"* (principle 7) | Kanban (D30); phases M0–M5 (CTO to confirm) | **Adopt, inside Kanban** (§4) | Waves are a grouping of work in flight, not a timebox; D30's reason for rejecting iterations still holds |
| 12 | **Decompose by dependency graph, then assign waves** (epic-decomposition example) | Epics/features mapped to requirements (D30) | **Adopt** as the CTO's wave-planning method | Our epics are product areas; the dependency graph is new work for the CTO |
| 13 | **Interface contracts at a gate enable parallel work**: *"define the interface first (at a review gate) and let both implement in parallel"* | Nothing | **Adopt** | Cheapest way to widen parallelism safely |
| 14 | **Issues first**: *"Every work request must be captured as a GitHub Issue before implementation begins"* (README) | Implied by the board | **Adopt** — made explicit in `CLAUDE.md` | — |
| 15 | **Close issues from PRs** (`Closes #`), agents move `phase:done` | **D30**: only QA moves to Done; closing automations off; PRs use `Refs #n` | **Reject** | Conflicts with D30 (§9) |
| 16 | **Review**: *"review remains a human responsibility until trust is established through measured outcomes"* (Claude adapter) | CTO/CSO agent seats review; QA verifies; CEO sees the demo | **Adapt, with a flag** (§8, §9) | We have no human code reviewer. Stated, not hidden |
| 17 | **`require-copilot-review` workflow** | CTO/CSO review column | **Reject**; keep its *head-commit* rule (§8) | A second vendor and a cost; it cannot be made blocking on a free private repo anyway |
| 18 | **Every finding reaches a terminal state**: *"fixed, accepted, or deferred"* (principle 6) | Not formalised for code review | **Adopt** — in the PR review record | Cheap; makes review auditable |
| 19 | **Eight-dimension evaluation framework** | Standups; phase review packs | **Adapt: five numbers** (§7) | Most dimensions need data we cannot collect honestly, or self-scoring |
| 20 | **Retrospective template** with 1–5 dimension scores and prompt-quality scores | Phase review pack (5.5) | **Adapt** — a one-line-per-wave delivery log; a retrospective section in the CGO's pack | Self-scoring by the same model that did the work adds no information (§7.4) |
| 21 | **Onboarding dialogue** and **two-commit baseline** (`AGENTS.md`) | CSO baseline is the first commit (D29) | **Reject** | Conflicts with D29; imports third-party text (§9) |
| 22 | **Platform-adapter layers** | One tool (Claude Code), one tracker (GitHub) | **Reject** | Indirection with nothing to switch between |
| 23 | **Agent context file** (`CLAUDE.md`) | `candour/CLAUDE.md`; CSO's draft section for `haunts/CLAUDE.md` | **Adopt** — Appendix A | — |
| 24 | **`STYLE.md`** | CTO charter: *"the technical standards the Engineers follow"* | **Adapt** — the CTO writes it at architecture; commit format now, in `CLAUDE.md` | Code style is the CTO's to set |
| 25 | **Label taxonomy** `phase:`, `priority:`, `effort:`, `category:`, `type:` (sample issue 12) | backlog-plan §6 | **Adapt** (§6.5) | Two added, template's status-as-label rejected |
| 26 | **`mcp.json`** with a PAT, filesystem and memory servers | CSO agent rules | **Reject** | A token-bearing config in a repo that will go public (§9) |
| 27 | **Agent surface selection**: CLI agents with branch isolation for parallel stories | Claude Code subagents in git worktrees | **Adopt** — already our practice | Cloud coding agents rejected: cost (Art. 1.5) and code leaves our environment for no gain [J] |
| 28 | **TDD**: *"write a failing test first, then implement to pass"* (`AGENTS.md` Quick Start) | Standup §8: PR lists a test per limb | **Adopt** — tests named by limb | — |
| 29 | **Autonomy earned through evidence** (principle 10) | Nothing explicit | **Adopt** — parallelism widens only on measured results (§4.4) | Cheap brake on the most likely failure |
| 30 | **Budget for the full cycle**: *"Plan for review, rework, and integration"* (principle 13) | CTO estimates | **Adopt** — flag to the CTO for SPK-08 | Review and rework are real hours in the price base |
| 31 | **Amendment template** for mid-execution changes (template retrospective, rec. 2) | `requirements.md` §24 scope-change log; D-entries | **Already have** | §24 is stricter: no trade-off, no change |
| 32 | **Capture sub-agent prompts** (template retrospective, rec. 3) | Commissions not kept | **Adopt** as row 3 | — |
| 33 | **Sample issues** kept in `docs/`, `sample` label | — | **Reject** | Not needed |
| 34 | *"Ask before assuming… surface the question to the human"* (`AGENTS.md`) | Route to the owning seat; the CEO only for 5.4 decisions | **Adapt** | Sending every ambiguity to the CEO would breach `CLAUDE.md`'s "one decision at a time" register |

---

## 3. The story format, and how it fits a ticket that is one requirement

### 3.1 The mismatch, stated plainly

The template's story is a **unit of work**: it knows its files before it starts. Its template asks for an *"Explicit list of files this story will touch. This prevents overlap with parallel stories"* [E, [agentic-story.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/.github/ISSUE_TEMPLATE/agentic-story.md)].

Our task is a **unit of verification**: one requirement ID, which QA checks limb by limb against `requirements.md` (backlog plan §1 rule 1; D31 point 4). It cannot know its files today, because **no architecture exists yet**. The CTO's ADR is step 2 of `/build`, after requirements (`.claude/commands/build.md`: *"cto subagent: architecture ADR + standards; cso subagent: threat model alongside it"*).

The template treats the issue as the specification (*"The specification is the program"*, README). **We do not, and should not start.** D27 and D31 make `requirements.md` the single source of truth, and D31 requires every ticket to say *"if the ticket and the document differ, the document wins."* That difference is deliberate and kept.

### 3.2 The fit: two layers, the second used only when needed

**Layer 1: the requirement ticket (every one of the 197 tasks).** It carries the D31 copy of the requirement and its criteria, **and** the template's headings around it. Under the CEO's decision of 2026-09-26, it **includes** "Files to create or modify" and "File ownership", **marked TBD until the CTO has designed the architecture**. When the CTO plans the wave that will build it, the CTO replaces TBD with the files, the interfaces and the wave. **For most requirements that is enough, and the requirement ticket is itself the unit of work**: one branch, one PR, one QA verification.

**Layer 2: the implementation story (only when needed).** The CTO (or an Engineer, proposing to the CTO) creates a story in the template's full format, as a **sub-issue of a requirement ticket**, in exactly two cases:

1. **A requirement is too big for one PR**, or its limbs belong in different parts of the code. Examples: CAP-4's four gap causes, or LOOK-2's twelve limbs.
2. **One change serves several requirements.** The SQLite schema serves DATA-1, VEN-7 … VEN-12 and SESS-1. The CI checks serve MEM-1(a), DFLT-1(a), PRIV-8 and DATA-13.

In case 2, a GitHub issue has **one** parent. The REST documentation's add-sub-issue call offers a `replace_parent` option described as *"replace the sub-issues current parent issue"*, in the singular [E, §13 item 19], from which I infer a single parent [I]. So the story sits under the requirement it mainly serves. It lists **every** limb it implements, including other requirements', under an **Implements** heading. The other requirement tickets list it in their Files section (*"via #n"*).

**Why stories are not the default, overturning part of the starting view.** The starting view created stories as sub-issues for all work at wave planning. With files on the requirement ticket (the CEO's decision), a story per requirement would duplicate the ticket for no gain. It would also roughly double the issue count on a board that already holds 295 [J]. **What would overturn this:** if the CTO's architecture shows most requirements spanning many modules, stories become the norm, and nothing in this design prevents that.

**Stories never copy acceptance criteria.** D31 point 2 says copies are *"generated by `products/haunt/backlog-tickets.py` rather than typed"*. A story is hand-written by the CTO, so it names limbs by ID and letter (*"CAP-4(a), CAP-4(b)"*) and points to the parent ticket. It may add **engineering criteria** of its own, such as "an interface conforms to its contract" or "a migration is reversible". Those are not requirements and QA does not verify them; the CTO checks them at review.

**Limb coverage (new; this seat's check).** At wave planning, **every limb of every requirement in the wave must be claimed**, either by the requirement ticket itself or by one of its stories. The PM/BA checks this before the wave starts and names any limb nobody has claimed. Without the check, the two-layer model would lose that traceability [J].

### 3.3 Exactly what `backlog-tickets.py` should emit for a requirement ticket

The body is split into two regions:

- **The generated region** holds everything D31 governs. On regeneration from a new `requirements.md` commit, it is replaced whole.
- **The CTO-maintained region** holds the files, interfaces and ownership. **Regeneration never touches it.**

HTML comment markers make the split; GitHub does not render them [K, high confidence]. Without the split, D31 point 3 (*"regenerated from the new commit, not edited by hand"*) would wipe the CTO's work every time a requirement changed.

| # | Heading | Content | Filled by | Honest today? |
|---|---|---|---|---|
| — | *(first line)* | `**CAP-4** · BLOCKING · platform: both · owner: engineer · [§4](link) · wave: TBD` | generator | Yes |
| — | *(marker)* | `<!-- generated:begin requirements.md@<sha>: replaced on regeneration; do not edit by hand -->` | generator | — |
| 1 | `### Summary` | The requirement's first sentence (the generator's existing `first_sentence()`) | generator | Yes |
| 2 | `### Origin and context` | The requirement's **Source** cell, verbatim, plus a link to the decision record, and one fixed line: *"The CEO's words are quoted in the decision entries named here; they are not copied into tickets."* (§5) | generator | Yes |
| 3 | `### Requirement` | Full requirement text (D31) | generator | Yes |
| 4 | `### Acceptance criteria (QA-verifiable)` | Full criteria, with lettered limbs as a checklist (D31) | generator | Yes |
| 5 | `### Invariants to preserve` | **(a) On every ticket (product-wide)**, one line and a link each: **MEM-1** (never encourage drinking or reward visit frequency; *"a count may appear only as a plain fact"*); **DFLT-1** (protective default, user can change it; every setting in the register); **PRIV-8** (no analytics, telemetry or measurement SDK; no outbound call site outside the backup module); and the transmission promise as narrowed by D12 (PRIV-1, §12.2.8). **(b) Ticket-specific**, from the existing label sets: `promise-line` → *"On the promise line (§20.1). Cutting or weakening it is an overrule or an amendment, not a scope change."* `standing-condition` → *"A standing condition of Block 4 (§7.7.5). A change here re-engages the CTO's block."* `mixed-priority` → *"Limbs carry different priorities; read them in the document."* `needs:cso-review` → *"Security-relevant: the CSO reviews the PR."* | generator | Yes, entirely from rows we already hold |
| 6 | `### Negative constraints` | Fixed line: *"Nothing listed in `requirements.md` §18 (Explicitly out of scope for v1) is built under this ticket"*, linked. Then: *"Story-level constraints: set at wave planning."* | generator | Yes. No per-requirement list exists, so none is invented |
| 7 | `### Dependencies` | `Blocked by:` (from the existing map); `Parent:` the feature; `Mentioned in the text:` every known requirement ID that the requirement or its criteria name, found by pattern and checked against the parsed ID set, **labelled "not necessarily a dependency"** | generator | Yes. The mentions list is mechanical and says so |
| 8 | `### Verification` | *"QA verifies every limb against `requirements.md` at a recorded commit, and records that SHA in 'Verified against' at Done. Only QA moves this ticket to Done (D30)."* | generator | Yes |
| — | *(stamp)* | The existing D31 stamp, unchanged | generator | Yes |
| — | *(markers)* | `<!-- generated:end -->`, then `<!-- cto-maintained: regeneration never overwrites below this line -->` | generator (once) | — |
| 9 | `### Files to create or modify` | **`TBD: set by the CTO once the architecture ADR exists, at wave planning. This ticket cannot enter Ready while this says TBD.`** | CTO | TBD by design (CEO decision) |
| 10 | `### Interfaces to implement` | The same TBD line | CTO | TBD |
| 11 | `### File ownership` | A table `File \| Owned by this ticket in wave \| Notes`, with one row reading `TBD` | CTO | TBD |

**On creation, the generator writes the whole body. On regeneration, it replaces only the text between `generated:begin` and `generated:end`.** If either marker is missing, it fails loudly rather than guessing [J]. This is a small change to how the ticket-creation step writes bodies; the parsing is unchanged.

**Who fills the TBD sections, and when.** The **CTO** fills them at **wave planning**, which starts only once the architecture ADR and the CSO's threat model exist. The assigned Engineer may propose changes in the ticket's comments. The CTO decides, because file ownership across parallel work is a coordination decision, and the CTO holds the build-commencement block (Constitution 5.6). Some tickets are owned by a seat that writes no code: the CGO's licence tasks, the CFO's, the CEO's PLAT-5 (storefront) and UX's PLAT-7 (icon). For those, the CTO writes *"none (no code)"* or the document path. **Spikes** get the same three sections; for a spike, the answer is usually its artifact path.

**New board fields the generator sets:** `Wave` (text, empty) and `QA attempts` (number, 0). **A new label** it must know but sets on nothing today: `level:story`, for stories created later by hand from the Appendix B template. The existing labels are unchanged.

**Epic and feature tickets:** no change. **Spike tickets** change in four ways:

- Add `### Summary`: the first sentence of the "What" cell.
- Rename `### Source` to `### Origin and context`.
- Add `### Negative constraints` with the line *"A spike produces a written answer. No product code reaches `main` under a spike ticket; prototype code stays on its spike branch."* **This seat proposes this rule; it does not exist yet, and the CTO should confirm it** [J].
- Add the three CTO-maintained sections.

### 3.4 Implementation stories: the format

Appendix B is the issue template. Its headings are the template's seven core sections, which the GitHub adapter says to keep: *"Keep all seven core sections — agents depend on them for reliable parsing"*. It also says to *"Add team-specific fields (e.g., Wave, Points, Component) at the end rather than replacing existing sections"* [E, [issue-trackers/github/quickstart.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/issue-trackers/github/quickstart.md)]. Added at the end: **Implements** (the limbs), **Commission** (§5), **Wave**, and **Done means**.

**How a story ends.** A story is complete when its PR is merged after the CTO has reviewed it at the PR's head commit. **The reviewer closes the story issue with a comment naming the merge commit. A story never has its Status set to Done.** The requirement ticket moves to **QA** when all its stories are merged. QA then verifies the requirement, which is QA's unit (QA charter: *"You verify against the spec, not against the Engineer's explanation of the code"*).

**This needs the CEO's confirmation, because it touches D30.** D30 says *"only QA moves a ticket to Done, and GitHub's built-in 'Item closed' and 'Pull request merged' automations are switched off so nothing else can."* With those automations off, closing a story does not set it to Done (backlog plan §7, citing GitHub's documentation at its §13 item 3), so D30's wording still holds. But a story is an issue closed by someone other than QA, and **what D30's "ticket" covers is the CEO's to decide**. The alternative is for stories to pass through QA as well, which doubles QA's work on the same limbs. I recommend the first option (§12, Decision 1).

---

## 4. Waves, the Kanban board and the phases

### 4.1 What a wave is, in the template

*"Group stories into waves based on dependencies. Stories in the same wave must have no file overlap and no dependencies on each other"*, and each wave ends in a review gate [E, [epic-decomposition-example.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/epic-decomposition-example.md)]. The example's lesson worth keeping is: *"Review gates are not overhead, they are coordination. The Wave 2 review gate that defines the service interface is what makes Wave 3 parallelism possible"* [E, same].

### 4.2 Waves inside Kanban, not instead of it

D30 chose Kanban because *"the work is agents commissioned as needed, not sprints, and no build calendar exists yet to size iterations against."* **A wave as defined above is not an iteration.** It has no length and no date. It is a set of tickets that can safely be built at the same time. So it sits **inside** Kanban without reopening D30 [I]:

- **The board's columns and rules are unchanged.** A ticket still moves Backlog → Ready → In progress → In review → QA → Done, and only QA moves it to Done.
- **A wave is a value of a new `Wave` field** (text, format `M<phase>.W<n>`, e.g. `M1.W2`). It is set on whichever issue owns files: the requirement ticket, or its stories.
- **One new view, "Current wave":** filter `Wave = <current>`, grouped by Status. It sits alongside the nine views in backlog plan §8.
- **A label for the wave is rejected.** Wave values change as work is planned, and labels are meant to mirror stable facts (backlog plan §6) [J].

**Is a Wave field worth having? Yes** [J]. Without it, the file-ownership rule has nothing to be checked against. "No two tickets in the same wave own the same file" needs a recorded wave.

### 4.3 Who plans waves

**The CTO**, on three grounds:

1. The CTO's charter gives it *"the technical standards the Engineers follow"*.
2. Backlog plan §10 already leaves phase sequencing to the CTO.
3. File ownership depends on the architecture, which is the CTO's.

**The method is the template's worked example:** list the components, draw the dependency graph, give each ticket its files, then group into waves. Two tickets that need the same file go in consecutive waves. An interface shared across a wave is written down at the preceding wave gate.

Other seats contribute:

| Seat | Contribution at wave planning |
|---|---|
| **PM/BA** | The limb-coverage check (§3.2). Confirms no promise-line or standing-condition limb has been left unclaimed. Moves the wave's tickets to Ready |
| **CSO** | Names which wave tickets need `needs:cso-review` beyond the existing list, and flags any wave touching the backup, KDF or import surfaces |
| **Engineer** | May propose a split into stories; the CTO decides |
| **Orchestrator** | Commissions the Engineer instances, one per ticket or story in the wave, each in its own worktree (the commission is recorded, §5) |

**A flag to the CTO: files every feature touches** [J]. Some files in a React Native app are edited by almost every ticket. The package manifest and lockfile, the navigation registry and the database migrations are examples. **So, by design, are MEM-1's string table and DFLT-1's settings register**: MEM-1(a) is a *"Build-wide string-table and store-metadata search"*, and DFLT-1(a) is *"a committed settings register"*. Left as single files, they make parallel waves impossible. **The CTO's architecture should make them additive** (one strings file per feature, one migration file per ticket, one register entry file per setting), or give each a single owner per wave. This is cheap to decide now and costly to retrofit.

### 4.4 How wide a wave may be: earned, not assumed

The Manifesto's principle 10: *"Agent autonomy is earned through evidence… expand scope only where results justify trust"* [E, [MANIFESTO.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/MANIFESTO.md)]. **Proposal** [J]:

- The first waves run **at most two** Engineer instances in parallel.
- The CTO may widen to three or four only after **two consecutive waves with zero merge conflicts, and no escaped defect traced to either wave**.
- Any conflict or escaped defect narrows it again.

This costs nothing, and it uses the numbers in §7.

### 4.5 The wave gate, and how it relates to the phase review pack

| | **Wave gate** | **Phase review (Constitution 5.5)** |
|---|---|---|
| **When** | When every ticket in the wave has a merged PR | End of each phase, M0 … M5 |
| **Who** | **CTO**, plus the CSO where any ticket carries `needs:cso-review` | **CGO** compiles; **CEO** receives, with a demo |
| **Checks** | (1) Every PR was reviewed **at its head commit** (§8). (2) `main` is green: tests, `secret-scan`, and the PRIV-8, MEM-1 and DFLT-1 checks once they exist. (3) No merge conflicts, or they are counted. (4) Interfaces for the next wave are written down. (5) A delivery-log row is written (Appendix D) | *"What this phase set out to do vs what it did"*, the demo, seat reports, compliance, open dissent (`pipeline/templates/review-pack.md`) |
| **Makes anything "done"?** | **No.** Tickets still need QA, and nothing is done in the Constitution's sense until reviewed | **Yes.** Constitution 5.5: *"Work is not 'done' until it has been reviewed."* A milestone closes only after the pack and demo reach the CEO (backlog plan §7) |
| **Written record** | One row in `docs/delivery-log.md` in `haunts`, and a CTO standup entry | The review pack in `candour`, which **rolls up the wave rows** (§7.5) |

**QA runs continuously and is not held for the wave gate.** Tickets reach the QA column as their PRs merge. What the wave gate checks is integration; what QA checks is the requirement. They are different things, and neither substitutes for the other.

**The phases M0 … M5 stay as proposed** (backlog plan §10, for the CTO to confirm). Each phase contains several waves. **M0 has no waves** except where a spike builds a prototype (SPK-02's device matrix), because the other spikes produce documents, not code.

**The CEO is not at wave gates.** The template's principle 4, *"Humans design, agents execute, both review"*, would put a human there. At Candour, the CEO sees the phase demo; the wave gate is a seat's job. §9 states what that costs.

---

## 5. "Originating prompt" versus the decision record and seat commissions

**What the template asks:** *"Capture the original human prompt that triggered this work… Paste the exact prompt by default"* [E, agentic-story.md]. Its Claude adapter: *"The originating human prompt must be preserved in the issue"* [E, [Claude adapter](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/agent-tools/claude/CLAUDE.md)]. **The purpose is retrospective:** so that prompt quality can later be compared with outcome quality [E, retrospective template §2].

**What Candour already has.** The CEO's instructions that shape the product are recorded **as D-entries**, often quoting his words. D24 quotes *"I like this idea in general, allowing customisation by the user"*, and D23 quotes *"the usage stats are high and are only likely to grow"*. Every requirement's **Source** cell names the D-entry or condition it came from.

**Where it goes, by kind of ticket:**

| Ticket | "Originating prompt" becomes | Why |
|---|---|---|
| **Requirement ticket** | **`Origin and context`**: the Source cell, generated, with a link to the decision record. **The CEO's words are not pasted.** | They are already quoted, once, in the public record. A third copy (chat → D-entry → ticket) can drift. D31's answer to drift is to generate copies, and the Source cell already *is* the pointer |
| **Implementation story, or any ticket an agent is commissioned to build** | **`Commission`**: the orchestrator's commission to the Engineer (or other seat), **verbatim, as the first comment**, dated, naming the seat and the orchestrator run. Follow-up corrections become further comments headed `Correction 1`, `Correction 2` | This is the real "prompt" in our process. It is what the template's own retrospective found missing: *"Capture sub-agent prompts… the sub-agent's prompt is not captured as a first-class artifact"* [E, §13 item 17] |
| **A CEO direction given in chat that changes scope** | **Never pasted from chat into a ticket.** It becomes a D-entry first, then a §24 row, then the tickets are regenerated (D31 point 3) | The decision record is the record. Chat is not |

**Two rules for commissions.**

1. **No secrets and no personal data in a commission**, because `haunts` will become public, issues included (D28; `repo-security-baseline.md` §0 item 4: *"issue and PR text is not scanned at all"*).
2. **Commissions follow the "Talking to the CEO" register only in what comes back to him.** The commission itself may be as long as the work needs.

**What it buys.** When QA fails a ticket or a spec defect is raised, the cause can be traced: the requirement (this seat's fault), the commission (the orchestrator's), the agent, or the review. That tag is recorded with the defect (§7.2). It is the template's prompt-to-outcome correlation, done as a cause tag rather than as a score.

---

## 6. The `haunts` repository scaffolding

### 6.1 What goes in, and in what order

`haunts` is private and empty (STATUS.md). **Nothing below is created without the CEO's go-ahead** (STATUS.md: *"Do not create the repo, board or any tickets without the CEO's explicit go-ahead"*).

| Order | Commit | Files | Owner | Source |
|---|---|---|---|---|
| **1** | **CSO security baseline**: first, unchanged (D29) | `.pre-commit-config.yaml`, `.gitleaks.toml`, `.github/workflows/secret-scan.yml`, `.github/dependabot.yml`, `.gitignore`, `SECURITY.md`, optionally `.claude/settings.json` | CSO; orchestrator commits | `repo-security-baseline.md` §4–§8 |
| **2** | **Process scaffolding** | `CLAUDE.md` (Appendix A, which **contains the CSO's §8.3 section verbatim**); `.github/ISSUE_TEMPLATE/implementation-story.md` (Appendix B); `.github/pull_request_template.md` (Appendix C); `docs/delivery-log.md` (Appendix D). `docs/standups/` is created by the first standup entry | PM/BA drafts (here); CTO and CSO confirm; orchestrator commits | This note |
| 3 | Licence and notices | `LICENSE`, `README.md` licence section, `THIRD_PARTY_NOTICES`, `CONTRIBUTING.md` | CGO drafts; CEO decides | `code-licence-note.md` §7; its CEO decisions are still open |
| 4 | Code standards | `STYLE.md` | **CTO**, at architecture | §6.2 |

**The PR template must be on the default branch to apply.** GitHub: *"Templates are available to collaborators when they are merged into the repository's default branch"* [E, §13 item 21]. Agents create PRs with `gh pr create --body …`, which does not load the template [K, medium confidence]. So `CLAUDE.md` tells agents to write the body to the template's headings.

### 6.2 `AGENTS.md`, `CLAUDE.md`, `STYLE.md`

- **`CLAUDE.md`: adopt, as the single agent context file** (Appendix A). We use one agent tool. The template's own Claude adapter lists the naming options and allows *"a comprehensive CLAUDE.md and a shorter copilot-instructions.md that references it"* [E, Claude adapter]. One file cannot disagree with itself.
- **`AGENTS.md`: none for now** [J]. It would be a second copy of `CLAUDE.md` for tools we do not use. If a second tool is ever adopted, `AGENTS.md` becomes a two-line pointer to `CLAUDE.md`, never a copy. **The template's `AGENTS.md` is rejected outright as a mechanism** (§9).
- **`STYLE.md`: deferred to the CTO.** The template's file is placeholders (*"Customize this guide for your project's conventions"*) [E, [STYLE.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/STYLE.md)]. Formatter, linter, naming and test layout are technical standards, which belong to the CTO (CTO charter). Until then, `CLAUDE.md` carries the two process rules that cannot wait: the commit format, and three of the template's **hard bans**, which are good and cost nothing. Those are *"No `TODO` comments without a linked issue"*, *"No suppressed linter warnings without a justifying comment"*, and no credentials in source (already the CSO's rule).
- **Merging with the CSO's agent rules.** The CSO drafted a section *"for `haunts/CLAUDE.md` (binding on every seat)"* (`repo-security-baseline.md` §8.3). **Appendix A includes it word for word**, because its rule 3 forbids edits to *"this section without a CSO note and the CEO's approval"*.

### 6.3 Issue and PR templates

- **Requirement tickets have no issue template.** They are generated (D31) and never created by hand. Their format is §3.3.
- **Implementation stories: `.github/ISSUE_TEMPLATE/implementation-story.md`** (Appendix B), the template's seven sections plus four.
- **PR template: `.github/pull_request_template.md`** (Appendix C). The template's `CONTRIBUTOR_PR_TEMPLATE.md` is for contributions to **the template repository** (its checkboxes are *"New adapter"*, *"New quickstart combo"*), and it opens with **`Closes #`**, which D30 forbids. So its structure was borrowed: summary, related issue, changes, testing, checklist. Its content was not.
- **No blank-issue lockdown or public issue forms yet.** `haunts` is private. When it goes public, the contribution policy (code-licence-note §7.3, CEO Decision 4 there) decides what outsiders may file.

### 6.4 Copying template files, and the MIT notice

**Recommendation: copy no template file.** The appendices are written from scratch for Candour. They reuse the template's **section headings**, short phrases such as "Negative Constraints" and "File Ownership", and its **ideas**.

**If a file were copied**, the MIT licence's condition applies: *"The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software"* [E, [LICENSE](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/LICENSE)]. That would sit alongside the planned PolyForm Noncommercial licence without conflict. `code-licence-note.md` §4.1 gives the principle, *"the outbound licence covers Candour's own code only"*, and §4.5 finds MIT inbound terms compatible. The copied file would keep its MIT notice and be listed in `THIRD_PARTY_NOTICES`.

**Whether headings and ideas alone attract the notice.** My view is that they do not: copyright protects expression, not methods or short phrases [K, medium confidence; not retrieved]. **That is a licence interpretation, so it is flagged to the CGO, not asserted.**

**An acknowledgement line is recommended anyway** (Appendix A, last line). It is honest, it is free, and it does not depend on the legal answer [J].

**The same applies in `candour`** if the company-level version copies any text. `candour`'s governance documents are CC BY-SA 4.0 (`LICENSE.md`). Mixing MIT text into them would need the MIT notice kept with that text; the CGO should confirm [K].

### 6.5 The label taxonomy, reconciled with backlog plan §6

The template's taxonomy is `phase:` (5), `priority:` (5), `effort:` (5), `category:` (7), and `type:epic`, `type:story`, `sample` [E, [sample issue 12](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/sample-issues/12-configure-label-taxonomy-and-metadata-scheme.md)]. It shares our `dimension:value` convention: *"A consistent prefix convention (`dimension:value`) makes labels filterable and unambiguous"* [E, same].

| Template label set | Ours (backlog plan §6) | Verdict |
|---|---|---|
| `phase:planned/next/now/blocked/done` | Board **Status** field (D30) | **Reject.** Status held in two places drifts, and `phase:done` set by whoever finishes breaks D30. Our `blocked` label is kept only as a filter aid on top of the `Blocked by` field (plan §6) |
| `priority:0-crit … 4-trivial` | `prio:blocking/must/cut-line/pending-estimate` | **Keep ours.** Our values are defined terms in `requirements.md` with consequences (the cut line, §20) |
| `effort:X-Small … X-Large` | `CTO hours` field | **Reject.** One estimate, the CTO's |
| `category:*` | `area:<epic>` | **Keep ours** |
| `type:epic/story` | `level:epic/feature/task/spike` | **Keep ours; add `level:story`** |
| `sample` | — | **Reject** |
| — | `platform:`, `seat:`, `promise-line`, `standing-condition`, `mixed-priority`, `needs:cso-review`, `needs:ceo`, `blocked` | **Keep, unchanged** |
| (template suggests `retro-workaround` for its D8 measure) | — | **Reject**; the two below measure what matters to us |
| — | **`spec-defect` (new)** | Set by an Engineer or QA when a criterion is wrong, untestable or contradicts another (standup §7). Removed by the PM/BA when fixed. **It measures this seat's own work** (§7) |
| — | **`escaped` (new)** | On a new issue raised for a defect found in behaviour that a **Done** ticket covers. The body links the Done ticket and says who found it (§7) |

---

## 7. Measurement and retrospectives

### 7.1 What the template proposes, and its own advice to start small

Eight dimensions, each with a 1–5 rubric. The dimensions are spec quality, decomposition, agent reliability, partnership efficiency, delivery, governance, cost and process maturity. They roll up into a composite score and a maturity level [E, [evaluation-framework.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/evaluation-framework.md)]. The framework itself says: *"Do not try to measure all eight dimensions on day one"*, and its "Operator Takeaway" names three metrics: *"Merge conflict count"*, *"Spec-to-implementation fidelity"*, *"Escaped defect rate"* [E, same]. It also warns, rightly: *"Agent parallelism inflates traditional activity metrics… Measure: Stories accepted (not PRs opened)"* [E, same].

### 7.2 The five numbers to record from day one

| # | Number | Definition for Haunts | Who records it | Where |
|---|---|---|---|---|
| 1 | **Merge conflicts per wave** | Conflicts met when merging a wave's PRs. **Target zero**; any conflict names the file, which is a decomposition finding for the CTO | CTO, at the wave gate | `docs/delivery-log.md` (Appendix D) |
| 2 | **QA first-pass rate** | Of requirement tickets reaching Done, the share with `QA attempts = 1`. QA increments `QA attempts` each time it starts a verification. This is the template's *"first-pass acceptance"*, measured **against the requirement, by QA**, not by the reviewer | QA (the field); CTO rolls it up at the wave gate | Board field; delivery log |
| 3 | **Escaped defects, and who found them** | A defect in behaviour covered by a **Done** ticket, filed as an `escaped` issue. The **finder** is recorded: QA (a later regression), CTO/CSO, **CEO at a demo**, or (after release) a user. **CEO-found defects are counted separately**. STATUS.md records that *"The CEO has caught errors the seats missed, repeatedly"*, and the evidence standard says of September 2026: *"None was caught by a seat. All were caught by the founder."* The count shows whether that is still true of code | Whoever finds it files it; the PM/BA counts | `escaped` label; delivery log; review pack |
| 4 | **Spec defects** | `spec-defect` blockers raised against `requirements.md` in the period, with the cause tag from §5 (requirement / commission / agent / review). **This measures this seat's work.** It is the template's D1 "spec quality", counted from events instead of scored | PM/BA | `spec-defect` label; delivery log |
| 5 | **Founder hours per phase** | The CEO's own hours spent on Haunts in the phase, roughly (to the half-day) | **The CEO, if he agrees** (§12, Decision 2) | Review pack, per phase; passed to the CFO |

**Why number 5, which the template does not name in that form.** The template's D7 measures *"Cost-per-resolved-issue"* [E]. For Candour, one cost number matters more than any other, and it is already owed. The price rests on the CTO's **2,090 "focused solo hours"**. `cost-sheet-v3.md` says: *"Actual hours will replace it at the first yearly review."* It also warns that if agents do much of the work, *"pricing at 2,300.5 hours × £32.71 while also carrying the agents' subscription… counts the same work twice. That is Article 9's first loophole"* (read on disk, lines 802 and 902). **Without a record kept as the work happens, the first yearly review will have to estimate the actual hours after the fact** [I]. Only the CEO can record his hours. Agent spend is a subscription already on the cost sheet (§3.4.1), and **per-ticket token accounting is rejected**: the effort of measuring it would exceed its value, and Article 1.5 says *"Operating cost discipline is an ethical obligation, because our customers pay our costs"* [J].

**Lead time and wave cycle time need no recording.** GitHub already timestamps issue and PR events, so they can be computed at phase end if the CGO wants them [K, high confidence].

### 7.3 Rejected, with reasons

| Template measure | Why not |
|---|---|
| **pass^k** (run the same spec k times) | Costs k agent runs per ticket for a periodic audit. Article 1.5 [J] |
| **Prompt-quality scores**, 1–5 on four criteria | The scorer is the same model that did the work. The evidence standard: *"every seat is the same model run by the same person… A process that answers an interpretive failure by adding agent passes is prescribing more of what already failed."* The template's own retrospective scored its operator's prompts at 4.0–5.0 across the board [E, §13 item 17]. A score that is always high carries no information [I] |
| **Composite score and maturity levels 1–5** | Self-assessment, as above. The cause-tagged defect counts (§7.2 #4) carry the same signal without the pretence of precision |
| **Cognitive-load survey; human-time share** | One human. He can say it in a sentence at the phase review |
| **Change failure rate (rollback/hotfix)** | Nothing is released until M5, and release is the CEO's (Constitution 5.4). Revisit after launch |
| **Test counts, PRs merged, issues closed** | Activity. The template itself warns against these |

### 7.4 Retrospectives

**Adapt; do not add a new document.** The template's retrospective template is a per-wave document with dimension scores [E, [retrospective.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/templates/retrospective.md)]. At Candour:

- **Per wave:** one row in `docs/delivery-log.md`, written by the CTO at the wave gate. The row has the five numbers and one sentence: *"Change for next wave"*. That keeps the template's per-wave feedback loop at a tenth of the weight.
- **Per phase:** the CGO's review pack gains a section, **"Delivery measures and retrospective"**. It holds the wave rows rolled up, founder hours, the escaped and spec defects with their causes, and **at most five action items**, each with an owner. Each action item must reach a terminal state by the next phase review: *"fixed, accepted, or deferred"*, the template's rule for findings (principle 6), applied to our own process. This is a change to `pipeline/templates/review-pack.md`, a company template, so it is proposed to the CGO (§11, §14).

### 7.5 How the numbers reach the CEO

Two routes:

- **Standup summary:** line 1 of the PM/BA's standup summary may say *"Wave M1.W2 closed: 0 conflicts, 5 of 6 passed QA first time."*
- **Phase review:** the phase review pack carries the table.

Nothing else goes to him. The `CLAUDE.md` register (*"Give the two or three things that actually matter"*) applies to metrics as much as to prose.

---

## 8. Their review gate versus our review column

**What theirs does.** `require-copilot-review.yml` fails a PR's check unless a review by `copilot-pull-request-reviewer` exists **on the PR's current head commit**. The code checks `r.commit_id === pr.head.sha` and otherwise reports *"Copilot has not reviewed the latest commit on this PR"* [E, [require-copilot-review.yml](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/.github/workflows/require-copilot-review.yml)].

**Rejected as a mechanism**, for three reasons:

1. **It adds a vendor and a cost.** Copilot code review is a paid GitHub Copilot feature [K, medium confidence; pricing not retrieved]. Our review seats already exist.
2. **It cannot block anything here yet.** While `haunts` is a private repository on a Free personal account, *"'CI must pass before merge' cannot be enforced"*: rulesets and branch protection for private repositories need a paid plan (`repo-security-baseline.md` §6, [E] there). A failing check is only advice until go-public.
3. **The reviewer's identity cannot be checked.** Every seat acts through the same GitHub account (`deopea-david`), and GitHub states: *"Pull request authors cannot approve their own pull requests"* [E, §13 item 20]. So a CTO "approval" cannot be a GitHub approval, and a workflow checking for a reviewer login would check for the author.

**What we do instead:**

- **The review is a written record in the PR**, in the fixed block at the bottom of the PR template (Appendix C). It gives the seat (CTO; CSO where `needs:cso-review`), **the head commit reviewed**, the verdict, and a findings table where every finding is **fixed**, **accepted** (with a reason) or **deferred** (with an issue number).
- **Kept from their workflow: the review is pinned to the head commit.** Any push after the review record invalidates it, and the reviewer re-reviews the new head. The merge happens only at the reviewed head. This is the one idea in the workflow worth having, and it costs a line [J].
- **Mechanical checks do what an independent reviewer would otherwise do.** Tests named by limb, `secret-scan`, and (from M1) the PRIV-8 dependency check, the MEM-1 string search and the DFLT-1 register check. Unlike a second agent's opinion, these are re-derivable (evidence standard: *"Arithmetic re-derivation is genuinely independent because a formula can be recomputed. Interpretation is not"*).
- **"Never merge on red"** is enforced by the agent rules, because branch protection cannot enforce it while private (CSO rule 7, Appendix A).
- **QA verifies independently after merge**, against the document, not the PR (standup §8).
- **At go-public**, the CSO's §6 switches on a ruleset requiring `secret-scan`. The same ruleset could then require the test job [J; for the CSO].

---

## 9. Conflicts with the Constitution or a CEO decision

**With the Constitution: none found in anything this note recommends adopting.** I checked each adopted practice against:

- Articles 1.5 (cost), 4 (product ethics) and 5 (5.4 human decision points, 5.5 reviews, 5.6 blocks);
- Article 6 and 6.1 (*"Agent reviews prepare and flag; they do not certify"*).

**Where I looked, and what would overturn this:** the table in §2 against those articles. A practice that let an agent decide a 5.4 matter (release, money, pricing, user-data policy) or mark work done before its review would overturn it. None does.

**With CEO decisions: two practices conflict, and both are rejected.**

1. **Closing tickets from PRs, and agents marking work done.** The template's PR template opens with `Closes #`. Sample issue 14 requires *"Each PR references its story issue (`Closes #N`)"* and has agents move labels to `phase:done`. The Claude adapter's workflow ends *"Update documentation affected by the change. Close the issue."* [E, §13 items 6, 14, 11]. **D30:** *"only QA moves a ticket to Done, and GitHub's built-in 'Item closed' and 'Pull request merged' automations are switched off so nothing else can."* Backlog plan §7 already requires `Refs #n`. **Rejected; Appendices A and C say so on their face.**
2. **The onboarding dialogue's first commit.** `AGENTS.md` step 4: *"Commit 1 — Baseline: An exact copy of all template files, committed as-is"* [E, [AGENTS.md](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/AGENTS.md)]. **D29** and STATUS.md: *"The CSO's security baseline is the repo's first commit (D29)… No product code before it."* It would also bring in about sixty third-party files under MIT, with the notice duty (§6.4), plus a `mcp.json` built around a GitHub token. **Rejected.** And, as the brief required, **its instructions were not executed in producing this note.**

**A tension, flagged rather than resolved.** The template's Claude adapter says *"review remains a human responsibility until trust is established through measured outcomes"*. Its manifesto says *"You can outsource execution but not understanding"* [E]. **At Candour, no human reads the code before QA.** The CTO and CSO seats review, and they are the same model as the Engineer. This does not breach the Constitution: 6.1 permits agent review so long as it *"prepare[s] and flag[s]"* and is never represented as certifying. And the human decision that matters, release to real users, is the CEO's under 5.4, with qualified human review before launch for *"anything involving personal data at scale"* (6.1). **But the template's warning applies to us with more force than to them**, and it should be said rather than discovered. What partly answers it:

- mechanical checks (§8);
- QA against the document;
- the CEO's demo at each phase;
- the escaped-defect count by finder (§7.2 #3), which will show whether reviews are catching what they should.

**What would resolve it:** a human code review before release, which is a spend decision (5.4) and is not recommended here.

**Two smaller mismatches, not conflicts:**

- The template's *"Ask before assuming… surface the question to the human"* would route every ambiguity to the CEO. Ours routes it to the owning seat, and the CEO gets only 5.4 matters, one at a time (`CLAUDE.md`). Adapted in Appendix A.
- The template's *"Each batch produces shippable increments"* (principle 7) must not be read as "released": release is 5.4. Waves produce merged work, never releases.

---

## 10. Changes to the standup routine

`standup-routine.md` v0.1 needs seven changes, for the orchestrator to apply once the CEO approves §3 (this seat can make them; it has not, as instructed):

1. **§3 item 5 is stale after D31.** It says *"never from the ticket — tickets hold no criteria (D27)"*. **Replace with:** *"Read the requirement in `requirements.md`, fetched fresh. The ticket carries a stamped copy (D31); if the stamp is older than the document's latest commit touching that ID, work from the document and say so in your entry."*
2. **§4 entry header gains the wave:** `### <seat> · <HH:MM UK> · <run id> · wave <M1.W2 or –>`.
3. **§5 gains the CTO (and CSO) as writers.** The CTO writes an entry when a wave is planned (which tickets, which files are contested, parallelism) and one at the wave gate (the delivery-log row, in one line). The CSO writes when it reviews a `needs:cso-review` PR.
4. **§5, Engineer:** the first entry of a run links the **Commission** comment it is working from (§5).
5. **§6, the CEO summary, line 1** may carry the wave result in a clause (§7.5). **Still five lines at most.**
6. **§7 blockers:** a spec defect also gets the `spec-defect` label. A defect found in a Done ticket's behaviour is filed as an `escaped` issue and noted as a `Blocked` or `Notes` line naming the finder.
7. **§8 hand-off:** "Review → QA" becomes: *"The reviewer writes the review record at the PR's head commit (PR template), merges only at that head, closes any story issue with the merge commit, and moves the requirement ticket to QA when all its work is merged."* Also fix the column name: §8 and backlog plan §7 say "Review (CTO/CSO)"; **the board as built says "In review"** (D30, plan §7 note).

---

## 11. Changes this implies to our own documents (not made)

| Document | Change | Owner |
|---|---|---|
| `decisions/2026-09-16-haunt-gate.md` | Record the CEO's 2026-09-26 decision (files sections on requirement tickets, TBD until the CTO sets them) as the next D-entry. Record Decisions 1–2 below when made | Orchestrator |
| `products/haunt/backlog-tickets.py` | §3.3 headings; generated/CTO-maintained markers; regeneration replaces only the generated region; `Wave` and `QA attempts` fields; spike-ticket headings; product-wide invariant lines | PM/BA (this seat), after Decision 1 |
| `products/haunt/backlog-plan.md` | §6 add `level:story`, `spec-defect`, `escaped`. §7 **Ready** entry rule gains *"Files and file ownership set by the CTO (not TBD)"*, and the column name is fixed to "In review". §8 add fields `Wave`, `QA attempts` and the view "Current wave". §9 note pointing to this document | PM/BA |
| `products/haunt/standup-routine.md` | The seven changes in §10 | PM/BA |
| `pipeline/templates/review-pack.md` | Add "Delivery measures and retrospective" (§7.4) | CGO (company template) |
| `products/haunt/STATUS.md` | "Before anything is created" gains step 6: the process-scaffolding commit (§6.1) after the CSO baseline | Orchestrator |
| CTO's architecture ADR | Address the shared-file flag (§4.3); confirm the spike negative constraint (§3.3); write `STYLE.md` | CTO |
| `requirements.md` | **None.** Not edited | — |

---

## 12. Decisions for the CEO, and this seat's disagreements

### 12.1 Decisions, one at a time

**Decision 1: approve the ticket format.** Requirement tickets keep the D31 copy and gain the template's headings. The files sections read TBD until the CTO fills them at wave planning (as he has already decided), and a ticket cannot be Ready while they say TBD. Implementation stories are created only where a requirement is split or one change serves several. **Stories are closed by the reviewer when merged and never show "Done"**; only requirement and spike tickets reach Done, and only QA moves them there. That last point is the part that needs him, because it says what D30's "ticket" covers. *Recommended: approve.* Once approved, this seat changes the generator and the plan, and ticket creation can resume.

**Decision 2 (after Decision 1): will he record his own hours on Haunts, roughly, per phase?** It is the only way to know the actual hours that `cost-sheet-v3.md` says will replace the 2,090-hour estimate at the first yearly review. The alternative is to reconstruct them afterwards. The recording falls on him, so it is his call. *Recommended: yes, to the half-day, noted weekly.*

**Not his:** waves, wave width and file ownership (CTO); labels and fields (PM/BA, within D30); the PR review record (CTO/CSO); the review-pack section (CGO); the MIT/acknowledgement question (CGO).

### 12.2 Disagreements and negative findings, each stated once

1. **With the orchestrator's starting view** (stories as sub-issues for all work at wave planning): overturned in part (§3.2). **What would change my mind:** an architecture in which most requirements span several modules.
2. **With the template, on scoring.** I recommend no 1–5 scores of any kind. **Overturn:** a scorer independent of the work, human or mechanical. The CEO scoring a sample at a phase review would qualify.
3. **Negative finding: "the template shows these practices work."** It does not. The blog post gives no measured outcomes, and the retrospective is self-scored. **Where I looked:** the README, the manifesto, the evaluation framework, all three retrospective files, and the blog post (retrieved, §13). **Overturn:** published results from teams other than its authors'.
4. **Negative finding: "Copilot review could enforce our review gate."** It could not while the repository is private on a free account, and it could not identify our seats (§8). **Where I looked:** the workflow file; `repo-security-baseline.md` §6; GitHub's approval documentation. **Overturn:** a paid plan plus separate GitHub identities per seat, neither of which is proposed.
5. **Confidence.** High on the ticket and label mechanics, which rest on our own files. Medium on the wave width (§4.4) and the shared-file flag (§4.3): both are judgment calls, and the CTO may know better.

---

## 13. Evidence register

**Template files, retrieved 2026-09-26 with `gh api repos/microsoft/agentic-agile-template/contents/<path>?ref=491179b…`**, all at [commit `491179b`](https://github.com/microsoft/agentic-agile-template/tree/491179beb2ff6a195aa29808391f75797e06996b). The repository metadata reports licence `MIT`, default branch `main`, last push 2026-06-05, and 96 stars [E, `gh api repos/microsoft/agentic-agile-template`]. **All of it is a single source: the template's authors describing their own method.** Base URL for the links below: `https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/`.

1. `README.md`: ["spec is the program"; five-step getting started; three starter metrics](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/README.md)
2. **Blog post**: Daniel Epstein, *Why Agent Development Needs Agile (Not Just Prompts)*, dated 19 May 2026, [developer.microsoft.com/blog/agentic-agile-why-agent-development-needs-agile-not-just-prompts/](https://developer.microsoft.com/blog/agentic-agile-why-agent-development-needs-agile-not-just-prompts/). The README's link (devblogs.microsoft.com) redirects there. **Read through a summarising fetch tool, not in the raw page.** As that tool returned them, the post says *"This isn't a finished process"* and invites feedback, and it reports no metrics, developer counts or project numbers. **(single source)**
3. [`MANIFESTO.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/MANIFESTO.md): values and principles 1–13
4. [`AGENTS.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/AGENTS.md): read as a document; **not executed**
5. [`.github/ISSUE_TEMPLATE/agentic-story.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/.github/ISSUE_TEMPLATE/agentic-story.md)
6. [`.github/contributor-templates/CONTRIBUTOR_PR_TEMPLATE.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/.github/contributor-templates/CONTRIBUTOR_PR_TEMPLATE.md)
7. [`docs/epic-decomposition-example.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/epic-decomposition-example.md)
8. [`docs/evaluation-framework.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/evaluation-framework.md)
9. [`docs/agent-surface-selection.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/agent-surface-selection.md)
10. [`docs/templates/retrospective.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/templates/retrospective.md)
11. [`platform-adapters/agent-tools/claude/CLAUDE.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/agent-tools/claude/CLAUDE.md): read as a document; **not executed**. Also [`quickstart.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/agent-tools/claude/quickstart.md) in the same directory, skimmed
12. [`platform-adapters/issue-trackers/github/README.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/issue-trackers/github/README.md) and [`quickstart.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/issue-trackers/github/quickstart.md)
13. [`platform-adapters/combos/claude-github-github-actions.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/platform-adapters/combos/claude-github-github-actions.md): *"Status: Stub"*
14. Sample issues [12](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/sample-issues/12-configure-label-taxonomy-and-metadata-scheme.md), [13](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/sample-issues/13-create-first-epic-decomposition-with-wave-plan.md), [14](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/sample-issues/14-run-first-wave-with-parallel-agent-execution.md); also 07 and the sample index, skimmed
15. [`STYLE.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/STYLE.md)
16. [`.github/workflows/require-copilot-review.yml`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/.github/workflows/require-copilot-review.yml)
17. [`docs/retrospectives/2026-06-consolidation.md`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/docs/retrospectives/2026-06-consolidation.md): the template team's own retrospective. Self-scored prompts 4.0–5.0, composite 4.1/5, and the recommendation to *"Capture sub-agent prompts"*. Its two companion files (originating prompts; wave-6 review report) were fetched and not relied on
18. [`LICENSE`](https://github.com/microsoft/agentic-agile-template/blob/491179beb2ff6a195aa29808391f75797e06996b/LICENSE): MIT, *"Copyright (c) 2025 Microsoft Corporation"*

Also fetched and skimmed, not relied on: `CONTRIBUTING.md`, `CONTRIBUTING-AGENTS.md`, `SECURITY.md`, `.github/copilot-instructions.md`, `platform-adapters/combos/README.md`, `platform-adapters/ci-cd/README.md`.

**GitHub documentation, retrieved 2026-09-26 through a summarising fetch tool** (the quoted phrases are as the tool returned them; GitHub's own documentation is the authoritative single source for these facts):

19. Sub-issues REST API: `replace_parent`, *"replace the sub-issues current parent issue"*. [docs.github.com/en/rest/issues/sub-issues](https://docs.github.com/en/rest/issues/sub-issues). The Projects page on sub-issues ([adding-sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)) was also read; it does not state the number of parents. **The single-parent conclusion is an inference [I].**
20. *"Pull request authors cannot approve their own pull requests."* [docs.github.com, approving a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)
21. PR template locations, including `.github/pull_request_template.md`; *"Templates are available to collaborators when they are merged into the repository's default branch."* [docs.github.com, creating a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)

**Model knowledge, not retrieved:**

- HTML comments are not rendered in GitHub issue bodies [K, high].
- `gh pr create --body` does not load the PR template [K, medium].
- Copilot code review is a paid feature [K, medium].
- Copyright does not protect methods or short phrases [K, medium; **for the CGO**].
- GitHub timestamps issue and PR events [K, high].

**Candour files, read from disk 2026-09-26** (branch `haunt/build-setup` at `31e23ed`):

- `constitution.md` Articles 1, 5, 6, 10;
- `roles/pm-ba.md`, plus the charter summaries of `cto`, `engineer`, `qa`, `cgo` and `cso`;
- `pipeline/evidence-standard.md`; `pipeline/templates/review-pack.md`;
- `.claude/commands/build.md`; `LICENSE.md`;
- `decisions/2026-09-16-haunt-gate.md` D23–D31;
- from `products/haunt/`: `backlog-plan.md` in full; `backlog-tickets.py` in full; `backlog.csv` header; `standup-routine.md` in full; `STATUS.md` in full; `repo-security-baseline.md` §0, §6 and §8; `code-licence-note.md` §0 and §7; `cost-sheet-v3.md` (lines cited); `requirements.md` §3.1, §3.2, §14, §18, §20 and §24.

---

## Appendix A: draft `haunts/CLAUDE.md`

Ready to commit after the CSO baseline, subject to the CTO's and CSO's confirmation. The security section is the CSO's text, **verbatim** from `repo-security-baseline.md` §8.3. Links to `candour` point at `main`, which assumes the `haunt/build-setup` work has been merged there.

````markdown
# Haunts: code repository

Haunts is a private, on-device journal of places visited, built by Candour. This
repository holds its code, tickets and board. **The governance record lives in the public
repository [deopea-david/candour](https://github.com/deopea-david/candour) and wins over
anything here**: the Constitution, the decision record, the requirements and the seat charters.

## Before any work, read

1. Your ticket, then its requirement in
   [requirements.md](https://github.com/deopea-david/candour/blob/main/products/haunt/requirements.md).
   The ticket holds a stamped copy. **If they differ, the document wins.**
2. Today's and yesterday's files in `docs/standups/`, and the board's "By seat" and
   "Blocked" views.
3. The decision entries (D-numbers) your ticket cites, in
   [decisions/2026-09-16-haunt-gate.md](https://github.com/deopea-david/candour/blob/main/decisions/2026-09-16-haunt-gate.md).
4. Your seat's charter in [roles/](https://github.com/deopea-david/candour/tree/main/roles) and the
   [Constitution](https://github.com/deopea-david/candour/blob/main/constitution.md).
   If any instruction conflicts with the Constitution, stop and say so.

## What binds every change

- **MEM-1:** Haunts never encourages drinking and never rewards the frequency or volume of
  visits. A count appears only as a plain fact.
- **DFLT-1:** every setting defaults to its protective value and is in the settings register.
- **PRIV-8 and PRIV-1:** no analytics, telemetry or measurement SDK; no outbound network
  call outside the backup module and the routes PRIV-1 names.
- **Decisions no agent makes** (Constitution 5.4): money, pricing, user-data policy,
  release to real users, kill or proceed. Raise them; never decide them.

## How work flows

- **Issues first.** No code without a ticket in **In progress** for your run.
- **Stay inside your files.** Touch only the files in your ticket's *File ownership*. If you
  need another, stop and write a `Blocked` standup line for the CTO. A ticket whose files
  still say TBD is not ready to build.
- **Tests by limb.** Every acceptance-criterion limb has a test whose name starts with the
  limb, e.g. `CAP-4(a) ...`. Write it failing first where practical.
- **Do not build through a spec defect.** If a criterion looks wrong or untestable, add the
  `spec-defect` label and a `Blocked` line naming the ID and limb.
- **Branches:** one per ticket, `<key>-<short-description>`, e.g. `cap-4-gap-records`.
- **Commits:** Conventional Commits scoped by ticket key, e.g.
  `feat(CAP-4): record a gap on service kill`.
- **Pull requests:** the body follows `.github/pull_request_template.md`, every heading.
  Reference tickets with `Refs #n` only. **Never write close, closes, fix, fixes, resolve or
  resolves before an issue number.** Only QA closes requirement tickets and moves them
  to Done (D30).
- **Review:** the CTO (and the CSO for `needs:cso-review`) records the review in the PR at
  its head commit. A push after the review needs a new review. Merge only at the reviewed
  head.
- **Dependencies:** name any new dependency in the PR, with its licence and why it is needed.
  No GPL-family licences. No code copied from the web without its source and licence recorded.
- **Hard bans:** no `TODO` without a linked issue; no suppressed linter warning without a
  comment saying why.
- **Standups:** append an entry to `docs/standups/YYYY-MM-DD.md` at the start and end of every
  run, in the format of
  [standup-routine.md](https://github.com/deopea-david/candour/blob/main/products/haunt/standup-routine.md) §4.
- **Reporting back:** summaries to the orchestrator are short and plain. The detail lives in
  the ticket, the PR and the standup file.

## Secrets and security (binding; from the CSO baseline, D29)

1. **Install hooks first.** In any new clone, run `pre-commit install` before your first
   commit. Worktrees share the hooks of their main clone.
2. **Never bypass a hook.** No `--no-verify` or `-n` on commit, no `SKIP=`, no changing
   `core.hooksPath`, no `pre-commit uninstall`, no setting `GITLEAKS_CONFIG` or
   `GITLEAKS_CONFIG_TOML`.
3. **Never suppress a finding.** No `gitleaks:allow`, no `.gitleaksignore`, no edits to
   `.gitleaks.toml`, `.pre-commit-config.yaml`, `.github/workflows/secret-scan.yml`,
   the security block of `.gitignore`, `SECURITY.md` or this section without a CSO note
   and the CEO's approval. **A finding is a stop, not a puzzle.**
4. **Never read, print or copy a secret.** Do not open `.env*` (except `.env.example`),
   keystores, `.p8`/`.p12` files, `credentials.json` or `~/.gradle/gradle.properties`.
   Do not run `eas credentials` or `eas env:*`. Never put a secret value in code, tests,
   fixtures, commit messages, issues, pull requests, tickets or chat. **A secret an agent
   has seen counts as leaked.**
5. **If you see a secret anywhere** (a diff, a file, command output): stop, do not commit,
   and report **the path and the type only, never the value** to the orchestrator.
   Do not try to rewrite history yourself.
6. **Stage named paths only.** Never `git add -A` or `git add .`.
7. **Never merge on a red `secret-scan`.** Never force-push to `main`.
8. **Workflows:** pin every action to a full commit SHA; default to
   `permissions: contents: read`; never use `pull_request_target`; reference secrets only
   as `${{ secrets.NAME }}` and never echo them.
9. **Nothing leaves the device.** Adding Firebase, analytics, crash reporting or any SDK
   or config that sends data off the phone changes user-data policy, which Constitution
   5.4 reserves to the CEO. It is never an agent's decision.
10. **No secret in `EXPO_PUBLIC_*`.** Those values are compiled into the app in plain text.

---

Process shaped in part by
[microsoft/agentic-agile-template](https://github.com/microsoft/agentic-agile-template) (MIT).
No file from it is copied here.
````

---

## Appendix B: draft `.github/ISSUE_TEMPLATE/implementation-story.md`

````markdown
---
name: Implementation story
about: Build work under a requirement ticket. Created by the CTO at wave planning.
title: '[STORY] <requirement key>: <what it builds>'
labels: 'level:story'
assignees: ''
---

<!-- Use only when a requirement is split, or one change serves several requirements.
Never copy acceptance criteria here. Name limbs by ID and letter; the requirement ticket and
requirements.md hold the text, and the document wins. -->

## Summary
<!-- One sentence: what this story delivers. -->

## Implements
Parent: #
<!-- Every limb this story makes true, e.g. CAP-4(a), CAP-4(b), SESS-8(c). -->

## Context
<!-- Why this is a separate story. Link the architecture ADR section it follows. -->

## Scope

### Files to create or modify
- `path/to/file` — what changes

### Interfaces to implement
<!-- Contracts this story must meet, as written at the last wave gate or in the ADR. -->

### Invariants to preserve
- MEM-1, DFLT-1, PRIV-8 and PRIV-1 (see CLAUDE.md), and the parent ticket's invariants.
- <!-- Contracts from earlier waves that this must not break. -->

## Engineering criteria
<!-- Optional checks the CTO verifies at review, e.g. "migration is reversible".
These are not requirements; QA does not verify them. -->
- [ ]

## Negative constraints
- Does NOT

## Dependencies
- Blocked by #

## File ownership
Wave: `M_.W_`

| File | Owned by this story in this wave | Notes |
|---|---|---|
| | | |

## Commission
<!-- The orchestrator's commission is posted verbatim as the first comment when work
starts. Corrections follow as "Correction 1", "Correction 2". No secrets and no personal
data: this repository will be public. -->

## Done means
Merged after the CTO's review at the PR's head commit. The reviewer closes this issue with
the merge commit. **A story never moves to Done**: QA verifies the parent requirement.
````

---

## Appendix C: draft `.github/pull_request_template.md`

````markdown
<!-- Keep every heading. Never write close/closes/fix/fixes/resolve/resolves before an issue
number: only QA closes requirement tickets (D30). -->

## Ticket
Refs #
Requirement limbs covered: <!-- e.g. CAP-4(a), CAP-4(b) -->
requirements.md read at: `<sha>`
Wave: `M_.W_`
Commission: <!-- link to the commission comment -->

## What changed and why
<!-- Two to five lines. -->

## Tests, by limb
| Limb | Test (file and name) | Passes locally |
|---|---|---|
| | | |

## File ownership
- [ ] Every changed file is in the ticket's File ownership list, or is listed here with the
      CTO's agreement:

## Checks
- [ ] `secret-scan` green; no hook bypassed
- [ ] No new dependency, or: name, licence (no GPL family), why it is needed
- [ ] No outbound network call added outside the backup module (PRIV-8)
- [ ] New user-facing text passes the MEM-1 term search; any new setting is in the
      settings register (DFLT-1). Until those CI checks exist, say how this was checked
- [ ] `needs:cso-review` on the ticket? Then CSO review requested

## Spec defects, shortcuts and debt
<!-- Anything built around rather than through; anything you would flag to the CTO. "None" is
an answer. -->

---

## Review record (reviewer fills in)
Seat: CTO / CSO · Head commit reviewed: `<sha>` · Verdict: approve / changes needed

| # | Finding | Disposition: fixed / accepted (why) / deferred (#issue) |
|---|---|---|
| | | |

<!-- A push after this record needs a new review. Merge only at the reviewed head. -->
````

---

## Appendix D: draft `docs/delivery-log.md`

````markdown
# Delivery log: Haunts

One row per wave, appended by the CTO at the wave gate. The CGO rolls these rows into each
phase review pack. Definitions: candour `products/haunt/agentic-agile-adoption.md` §7.2.

| Wave | Gate date | Tickets / stories merged | Engineers in parallel | Merge conflicts (files) | QA first pass (Done at attempt 1 / Done) | Spec defects (cause) | Escaped defects (found by) | Change for next wave |
|---|---|---|---|---|---|---|---|---|
````

---

## 14. Company-level practices, not Haunts-specific

The CEO wants a company-level version of this advice in `candour` (the orchestrator is handling that). These adopted practices should apply to **every** Candour product. Each would land as a pipeline template or charter change, not a constitutional amendment [J; the CGO should confirm that none needs Article 11].

1. **Tickets wrap a generated, stamped copy of the requirement, and the document wins** (D31, generalised). The template's headings go around it: Summary, Origin and context, Invariants, Negative constraints, Dependencies. → `pipeline/templates/` (a ticket-format page), PM/BA charter.
2. **Files to create or modify, Interfaces and File ownership appear on every ticket, TBD until the CTO sets them from the architecture.** A ticket cannot be Ready while they say TBD. → CTO charter (*Produces*: wave plans and file ownership), `/build` step 2.
3. **Waves inside Kanban.** The CTO groups Ready work into waves with disjoint files and no internal dependencies. Each wave closes with a wave gate: review at the head commit, `main` green, next interfaces written. **A wave gate never makes work "done"; only the phase review pack and demo do** (Constitution 5.5). → `/build` step 3, CTO charter.
4. **Parallelism is earned.** At most two parallel Engineer instances until two waves run clean; narrow again on any conflict or escaped defect.
5. **Implementation stories only when a requirement is split or a change spans requirements.** Stories name limbs by letter and never copy criteria by hand; the reviewer closes them on merge; only QA moves requirement tickets to Done. *(Subject to the CEO's Decision 1.)*
6. **The commission is the originating prompt.** It is recorded verbatim on the ticket when an agent starts work. The CEO's words live in D-entries and are linked, not copied into tickets. → `/build`, orchestrator practice.
7. **PRs reference tickets with `Refs #n` only.** The review record is written in the PR, pinned to the head commit, and every finding ends fixed, accepted or deferred. **Tests are named by acceptance-criterion limb.** → a company PR template.
8. **Five measures, from day one:** merge conflicts per wave; QA first-pass rate; escaped defects by finder (CEO-found counted separately); spec defects with cause; founder hours per phase (for the cost sheet's actual-hours restatement). **No self-scored ratings.** → `pipeline/templates/review-pack.md` gains "Delivery measures and retrospective"; a delivery-log template.
9. **One agent context file per product repository** (`CLAUDE.md`). It embeds the CSO's agent rules verbatim, links to the governance record rather than copying it, and is committed after the security baseline. → a `pipeline/templates/` starter.
10. **Labels `spec-defect`, `escaped` and `level:story`**, alongside the D30 board: status lives only in the Status field, never in labels.
11. **Copy no third-party template file; acknowledge the source.** Where text is copied, its licence notice travels with it. → CGO.

**Haunts-specific, not for the company version:** the product-wide invariants (MEM-1, DFLT-1, PRIV-8/PRIV-1), the shared-file list in §4.3, phases M0–M5, and the D29/D30 specifics beyond the general rules above.
