# Model and effort selection for the agent seats

**Author:** main session (orchestrator), at the CEO's request · **Date:** 2026-09-26 · **Status:** proposal; binding on merge
**Applies to:** every seat in `.claude/agents/`, and to the main session when it commissions them
**Evidence:** tagged per `pipeline/evidence-standard.md`. Every [E] was retrieved on 2026-09-26 from the link given.

---

## 0. The answer on one page

**No, the seats should not all use the same model.** Until now they all have: no agent definition sets a `model`, so every seat has run on the main session's model (Opus 5.5) at the session's effort level.

**What this proposes:**

1. **Each seat gets a default model and effort level** in its definition's frontmatter (§4). Judgment-heavy seats whose output feeds a CEO decision stay on **Opus**. The two highest-volume seats move to **Sonnet**: the Engineer, whose work is checked by tests, review and QA, and the Research Analyst, whose work is mostly reading.
2. **The orchestrator overrides the model per task** (§5), because Claude Code allows a per-call model override. It steps down to Haiku or Sonnet for mechanical work, and steps up for high-stakes, novel or failed work. **Effort cannot be overridden per call**, only set per seat. That limit shapes the design.
3. **The reviewer runs on a different model from the author wherever it can** (§5.4). Sonnet-written code is reviewed by an Opus CTO and verified by an Opus QA. This is a partial fix for a real bias, and §2 says plainly how partial it is.
4. **Fable is not a default for any seat.** Depending on the plan, Fable usage can bill to paid usage credits rather than the plan's included limits. In a subagent it bills **without asking**. That makes it spending money, which is the CEO's alone (Constitution 5.4). **Decision owed: see §7.**
5. **No second AI vendor for now** (§6). The evidence says errors correlate even across providers among strong models. Adding a vendor would bring a new cost and send Candour's private code to a new third party, for a gain the evidence says is small.
6. **Every commission and artifact records the model and effort it ran on**, so the metrics the agentic-agile adoption plan already records can show whether the choices work. The table is revisited after the first build wave.

---

## 1. What Claude Code allows, retrieved at source

| Fact | Source |
|---|---|
| A subagent definition's frontmatter supports `model` (`sonnet`, `opus`, `haiku`, `fable`, a full model ID, or `inherit`) and `effort` (`low`, `medium`, `high`, `xhigh`, `max`; *"available levels depend on the model"*; *"Default: inherits from session"*) | [E, [sub-agents](https://code.claude.com/docs/en/sub-agents.md), "Supported frontmatter fields"] |
| *"When Claude invokes a subagent, it can also pass a `model` parameter for that specific invocation."* Resolution order: per-invocation parameter → frontmatter `model` → `CLAUDE_CODE_SUBAGENT_MODEL` → main conversation's model | [E, same page, "Choose a model"] |
| **There is no per-invocation effort parameter.** Effort comes from the frontmatter or the session. | [I, from the same page: the frontmatter field is documented and no invocation parameter for effort is. Consistent with the Agent tool's own schema in this session, which offers `model` and not `effort`] |
| A family alias such as `opus` resolves to **the main conversation's exact model** when that model is in the family. So `opus` today means Opus 5.5, and it tracks the session automatically. | [E, sub-agents, "Choose a model"] |
| Subagents inherit the main conversation's extended-thinking setting; *"There is no per-subagent thinking setting."* Opus 5.5 and Fable always think. | [E, sub-agents; [costs](https://code.claude.com/docs/en/costs.md), "You can't turn off thinking on Opus 5.5 or the Fable models"] |
| On a subscription, *"The subagent's own requests still draw on your usage. To spend less on them, choose a smaller model for a subagent."* | [E, costs, "Delegate verbose operations to subagents"] |
| *"Depending on your plan and seat tier, Fable usage can bill to usage credits instead of drawing on your plan's included limits."* In non-interactive mode and through the Agent SDK, *"When a Fable request there would bill to usage credits, Claude Code bills it without asking."* | [E, [model-config](https://code.claude.com/docs/en/model-config.md), "Fable and usage credits"] |
| Anthropic's guidance: *"for most tasks you should use the model's default effort level"*. If Claude had the context and still got it wrong, that signals a larger model; if it skipped a step, that signals more effort. Try a stronger model at default effort before raising effort on a weaker one. Haiku for simple work; Sonnet for routine and mechanical changes; Opus for subtle bugs, unfamiliar domains and architecture; Fable for complex multi-step work. | [E, [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code), single source (the vendor), read through a summarising fetch] |
| *"Sonnet handles most coding tasks well and costs less than Opus. Reserve Opus for complex architectural decisions or multi-step reasoning … For simple subagent tasks, specify `model: haiku`."* | [E, costs, "Choose the right model"] |
| List prices per million tokens (input/output): Fable 5.1 $10/$50, Opus 5.5 $4/$20, Sonnet 5 $2/$10, Haiku 4.5 $1/$5. **These matter here only as relative weights**, because Candour runs on a subscription (`cost-sheet-v3.md` §3.4.1), not per-token API billing. | [K — the `claude-api` skill's model table, cached 2026-06-24, not re-retrieved; Anthropic is the only publisher] |

**The design consequence.** The orchestrator can choose the **model** task by task, but the **effort** is fixed per seat. So each seat's effort is set for its typical work, and anything unusual is handled by changing the model, not the effort. That is also the order Anthropic's own guidance recommends.

## 2. Does a different model make review more independent? Partly.

- **Self-preference is real.** *"LLMs … disproportionately favor summaries written by themselves over those by other LLMs and from humans"*, and models can recognise their own outputs at better than chance [E, [Panickssery et al., NeurIPS 2024](https://arxiv.org/pdf/2404.13076)]. A reviewer on the author's own model is the configuration that bias is about. **This is the case for different models on author and reviewer.**
- **But errors correlate across models, and more so as models get stronger.** Across more than 350 LLMs, *"models agree 60% of the time when both models err"* on one leaderboard; shared provider and architecture raise the correlation; and *"larger and more accurate models have highly correlated errors, even with distinct architectures and providers."* Judges also overrate same-provider models, because they agree with those models' wrong answers [E, [Kim et al., ICML 2025](https://arxiv.org/abs/2506.07962)]. **Sonnet reviewed by Opus is same-provider, so the gain is real but limited.**
- **This matches what Candour has already recorded.** The evidence standard: *"every seat is the same model run by the same person … Four agent passes over Article 4 in September 2026 produced the same wrong answer; the human produced the right one."* Different models soften that finding. They do not overturn it.

**What follows [J]:** use different models for author and reviewer because it is nearly free. But **the independent checks remain the mechanical ones** (tests named by limb, the secret scan, the string and dependency checks) **and the CEO**. Nothing in this document should be read as making agent review independent.

## 3. The constraints the choice must respect

1. **Constitution 1.5, "cheap and boring by default".** On a subscription, the cost of a model choice is **usage-limit headroom**. When it is used up, the whole company stops until the window resets [E, costs: *"a seat-based usage window … shared across all models"*]. The Engineer and Research Analyst generate most of the tokens, so they are where a cheaper model buys the most headroom.
2. **Constitution 5.4: spending real money is the CEO's alone.** Fable may bill to usage credits, and bills silently in a subagent (§1). **So no seat defaults to Fable, and the orchestrator uses it only under a standing approval from the CEO** (§7).
3. **Errors that reach the CEO have cost the most in this company's history:** interpretive errors in gate packs, transposed arithmetic, stale legal citations. **So the seats whose output feeds a 5.4 decision keep the strongest default model**, and their efficiency comes from being commissioned less often and more precisely, not from a cheaper model.

## 4. Default model and effort per seat (the frontmatter this PR sets)

| Seat | `model` | `effort` | Why |
|---|---|---|---|
| **CGO** | opus | high | Legal and constitutional interpretation, gate packs, review packs. The seat whose errors the decision record corrects most often |
| **CFO** | opus | high | Published numbers under Article 2.1. Arithmetic is re-derived mechanically (Condition 6), but the model builds it |
| **CTO** | opus | high | Architecture, wave planning, and **review of every PR**. On Opus it reviews Sonnet-written code as a different model |
| **CSO** | opus | high | Threat models, security review, crypto choices (SPK-06). Security errors are silent and permanent |
| **Skeptic** | opus | xhigh | Its only job is finding what others missed. Thoroughness is the capability, so it gets the highest effort short of `max`. Moves to Fable for gate dissent if the CEO approves (§7), which would also make it a different model from the authors |
| **CVO** | opus | high | Idea development and proposals. In practice the main session often acts as CVO |
| **PM/BA** | opus | medium | Long, careful specifications, but mostly structured restatement of decided things. `medium` is Opus 5.5's own default. The orchestrator steps up to `pm-ba` on Fable only for a scope-change trade-off that goes to the CEO |
| **UX Lead** | opus | medium | Article 4 and dark-pattern judgments are load-bearing (they became acceptance criteria); accessibility checks are structured |
| **QA** | opus | medium | Verifies against written criteria, so thoroughness matters more than depth. **Kept on Opus so that it is a different model from the Engineer** |
| **Engineer** | sonnet | xhigh | Most of the build's tokens. Anthropic's guidance puts routine coding on Sonnet, and `xhigh` is the recommended level for coding and agentic work [K, `claude-api` skill]. Every line is then checked by tests, CTO review (Opus) and QA (Opus). **The orchestrator steps the Engineer up to Opus for named hard work** (§5.2) |
| **Research Analyst** | sonnet | high | Reading-heavy: many sources, mostly retrieval and summary. Its briefs are checked by the Skeptic at every gate |

**The built-in Explore agent** inherits the main session's model, capped at Opus [E, sub-agents]. The orchestrator passes `model: haiku` when it uses Explore for plain search (§5.1). No project override is added.

**`opus` is used as an alias, not a pinned ID**, so the seats move with the main session when the CEO changes model, and never run above it.

## 5. How the orchestrator chooses, task by task

The seat default is the starting point. The orchestrator changes the **model** (the only per-call lever) by these rules and **states the choice in the commission**.

### 5.1 Step down: Haiku or Sonnet

Use a smaller model for **mechanical work with a checkable output**: file and code search, inventories, reformatting, running scripts, fetching and summarising documentation, ticket generation from a script, and standup roll-ups. **Test:** could a wrong answer be caught by looking at the output? If so, step down.

### 5.2 Step up: Sonnet → Opus, or Opus → Fable (Fable only under §7)

Step up when any of these holds:
- **Stakes:** the output feeds a Constitution 5.4 decision, makes a claim about what a clause of the Constitution or of law requires, sets a published number, or touches a **promise-line**, **standing-condition** or `needs:cso-review` ticket.
- **Irreversibility:** schema rules, capture architecture (CAP-1), crypto, anything that cannot be fixed after shipping (`requirements.md` §20.1).
- **Novelty:** no precedent in the repository, or an unfamiliar platform API.
- **A capability failure:** the seat had the context, clearly tried, and still got it wrong.

**A thoroughness failure is not a reason to step up.** If the seat skipped a file or did not run the tests, re-commission it on the same model with a sharper brief. That follows Anthropic's own diagnostic (§1).

### 5.3 Named step-ups for Haunts, known now

- **Engineer → Opus:** the native capture modules (CAP-1 … CAP-3), the SQLite schema and the refresh rules (VEN-7 … VEN-12), and backup encryption (DATA-6 … DATA-8).
- **CTO → Fable (under §7):** the architecture ADR, and review of any PR the Engineer wrote on Opus, so the reviewer stays a different model from the author.
- **Skeptic → Fable (under §7):** every gate dissent memo and the annual audit.

### 5.4 Reviewer different from author

Wherever possible, the seat that checks work runs on a different model from the seat that made it: Engineer (Sonnet) → CTO (Opus) → QA (Opus). **Where that is not possible**, for example Opus-written documents reviewed by an Opus Skeptic with Fable unavailable, the review record says so. The mechanical checks and the CEO carry the weight. **The limit is disclosed, not hidden.**

### 5.5 Record it

Every commission states `model` and `effort`, and every artifact's provenance line records them, for example *"CTO · opus (Opus 5.5) · effort high"*. This costs one line. It is what lets the adoption plan's day-one metrics (first-pass QA rate and escaped defects) be read **by model**.

## 6. Other vendors' models: not now

**What it would take:** Claude Code runs Anthropic models only. The sub-agents documentation describes no other route [E, by absence, sub-agents]. So a second vendor means calling that vendor's own CLI or API from Bash, or paying for a review product such as Copilot code review, which the agentic-agile adoption plan already rejected on cost.

**Why not now [J]:**
1. **The gain is smaller than it looks.** Strong models from different providers still share errors (§2, Kim et al.).
2. **It is a new cost and a new third party.** Candour's private code, and in time its draft decision records, would go to another company under its terms. Candour holds no user data, so this is not an Article 4 problem. But it is a new supplier relationship, and under 5.4 and 1.5 that is the CEO's to open.
3. **Nothing has yet shown a need.** The escaped-defect metric does not exist until the build starts.

**What would change this:** after the first phases, escaped defects or CEO-found errors that a different vendor's review would plausibly have caught. At that point it comes to the CEO as a costed proposal, starting with one narrow use, such as a second reviewer on `needs:cso-review` PRs only.

## 7. Decisions for the CEO, one at a time

1. **Adopt §4 and §5**, which merging this PR does.
2. **Fable: a standing approval, or not?** First, the CEO checks the `/model` picker. If the Fable row says *"Requires usage credits"*, Fable is paid on his plan. The options:
   - **(a) No Fable.** The §5.3 step-ups use Opus instead, and §5.4's limit applies more often.
   - **(b) Fable within a monthly credit cap the CEO sets**, for the named uses in §5.3 only, logged in the decision record.
   - **(c) Fable per use, asked each time.**

   **If Fable draws on included limits, not credits,** the question becomes one of headroom only, and §5.3 applies without a money decision.

## 8. Review

Revisit this table at the **end of the first build wave**, and again at each phase review pack. Use the adoption plan's metrics read by model: first-pass QA rate per seat and model, escaped defects, spec defects, and usage-limit hits. **A default moves on evidence, not preference.** Any change is a PR to this file and the frontmatter.

## 9. Sources

- Claude Code docs, retrieved 2026-09-26: [sub-agents](https://code.claude.com/docs/en/sub-agents.md), [model-config](https://code.claude.com/docs/en/model-config.md), [costs](https://code.claude.com/docs/en/costs.md). Claude Code version in use: 2.1.278.
- Anthropic, [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code). Vendor guidance, single source.
- Panickssery, Bowman, Feng, [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/pdf/2404.13076), NeurIPS 2024.
- Kim, Garg, Peng, Garg, [Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962), ICML 2025.
- Candour: `pipeline/evidence-standard.md` (the same-model finding); `products/haunt/cost-sheet-v3.md` §3.4.1 (subscription, not API).
