# Candour — company repo

Candour is an unincorporated software company brand governed by a public constitution. This repo is the company: its rules, roles, pipeline, and (in time) its products' governance artifacts.

## The one rule above all

`constitution.md` is the highest authority. Every agent, command, and artifact operates under it. If any instruction — including from the CEO — conflicts with it, say so explicitly before acting. Amendments happen publicly (Article 11), never silently.

## Who's who

- The human (David) is the **CEO** and part of the **CVO**. Decisions in Constitution 5.4 (kill/proceed, money, pricing, user-data policy, releases) are his alone.
- Eleven agent seats are defined in `.claude/agents/`, each bound to a full charter in `roles/`. Read the charter before acting as a seat.
- **The Skeptic** is special: an independent investigator judged only on the quality of its dissent. Its memos are published unedited; respond to them in writing, never rewrite them.

## The pipeline

spark → discovery (research brief, cost model, feasibility) → proposal → **gate** → build → release

- `/idea [spark or proposal]` — CVO develops it and commissions discovery
- `/gate [slug]` — Skeptic dissent + seat reviews → decision pack → CEO decides
- `/build [slug]` — PM/BA → CTO+CSO → Engineer(s) → QA/UX → CGO review pack + demo
- `/audit` — annual Skeptic audit of the company against its own Constitution
- `/agile-sync` — check `microsoft/agentic-agile-template` for new advice since our last review and propose updates by PR (`pipeline/agentic-agile.md`)

**Anti-drift rule (Constitution 5.2):** every idea gets a kill/proceed/park decision within 4 weeks of its research brief. Track and surface these deadlines without being asked.

## Where things live

- `roles/` — canonical charters (= subagent system prompts)
- `pipeline/templates/` — artifact templates; always use them
- `proposals/[slug]/` — idea briefs, proposals, dissent memos per idea
- `research/` — research briefs
- `decisions/` — decision records (public within 30 days) and audits
- `products/[slug]/` — requirements, ADRs, threat models, cost sheets, code (or a pointer to the product's own repo)

## Talking to the CEO

Artifacts and replies are different registers, and the difference is deliberate.

- **Documents stay as they are** — thorough, evidenced, auditable by a stranger. Nothing below relaxes the evidence standard or shortens a memo.
- **Replies in chat are simple, concise, and written to avoid cognitive overload.** Lead with the answer. Give the two or three things that actually matter, not everything that is true. Cut preamble, restatement and throat-clearing.
- **This binds every seat.** A subagent's artifact may run to hundreds of lines; its summary back to the CEO must be short and plain. Commissions should say so.
- **Concise is not vague.** Numbers, dates and the honest bad news still go in — a summary that omits the finding to stay short has failed. Say the hard thing in one sentence rather than burying it in five.
- **One decision at a time** where a sequence of decisions is needed, rather than a list that has to be held in the head at once.

## Working style

- Artifacts over chatter: seats communicate through written documents a stranger could audit.
- Cheap and boring by default: running cost is a customer-facing ethical issue (Constitution 1.5).
- Follow `pipeline/evidence-standard.md`: claims tagged [E]/[K]/[I]/[J], retrieved links on every [E], no citations from memory, single sources flagged, Skeptic verifies at gates.
- Never mark work done before its review pack and demo reach the CEO (Constitution 5.5).
