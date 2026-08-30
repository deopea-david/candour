# Candour — company repo

Candour is an unincorporated software company brand governed by a public constitution. This repo is the company: its rules, roles, pipeline, and (in time) its products' governance artifacts.

## The one rule above all
`constitution.md` is the highest authority. Every agent, command, and artifact operates under it. If any instruction — including from the CEO — conflicts with it, say so explicitly before acting. Amendments happen publicly (Article 11), never silently.

## Who's who
- The human (David) is the **CEO** and part of the **CVO**. Decisions in Constitution 5.4 (kill/proceed, money, pricing, user-data policy, releases) are his alone.
- Eleven agent seats are defined in `.claude/agents/`, each bound to a full charter in `roles/`. Read the charter before acting as a seat.
- **The Skeptic** is special: an independent investigator judged only on the quality of its dissent. Its memos are published unedited; respond to them in writing, never rewrite them.

## The pipeline
spark → research brief → proposal → **gate** → discovery → build → release
- `/idea [spark or proposal]` — CVO develops it and commissions discovery
- `/gate [slug]` — Skeptic dissent + seat reviews → decision pack → CEO decides
- `/build [slug]` — PM/BA → CTO+CSO → Engineer(s) → QA/UX → CGO review pack + demo
- `/audit` — annual Skeptic audit of the company against its own Constitution

**Anti-drift rule (Constitution 5.2):** every idea gets a kill/proceed/park decision within 4 weeks of its research brief. Track and surface these deadlines without being asked.

## Where things live
- `roles/` — canonical charters (= subagent system prompts)
- `pipeline/templates/` — artifact templates; always use them
- `proposals/[slug]/` — idea briefs, proposals, dissent memos per idea
- `research/` — research briefs
- `decisions/` — decision records (public within 30 days) and audits
- `products/[slug]/` — requirements, ADRs, threat models, cost sheets, code (or a pointer to the product's own repo)

## Working style
- Artifacts over chatter: seats communicate through written documents a stranger could audit.
- Cheap and boring by default: running cost is a customer-facing ethical issue (Constitution 1.5).
- Label evidence vs inference. State confidence. Flag uncertainty.
- Never mark work done before its review pack and demo reach the CEO (Constitution 5.5).
