# Standup routine — Haunts build

**Seat:** Product Manager / BA · **Date:** 2026-09-26 · **Version:** 0.1 (proposal, goes to the CEO with `backlog-plan.md`)
**Applies to:** the PM/BA, QA and Engineer seats, whenever any of them runs on Haunts work. **Board and columns:** `products/haunt/backlog-plan.md` §7.

---

## 1. The one fact this rests on

**Agents are stateless, so a standup is not a conversation.** No seat remembers yesterday, and no two seats are ever in the room together. A standup is therefore **a written entry**: each time a seat runs on Haunts work, it first reads the current state, then does its work, then **appends** a short dated entry to a shared file. The next seat to run — or the same seat in a new session — reads that file instead of remembering.

The file is the memory. If it is not written down, it did not happen.

---

## 2. Where entries live

**`docs/standups/YYYY-MM-DD.md` in the `deopea-david/haunts` repository**, one file per calendar day (UK date), created by whichever seat writes first that day.

- **Append only.** Never edit or delete another seat's entry. Corrections are a new entry that says what it corrects.
- Entries are committed on the branch the seat is working on and reach `main` with its PR. A seat that has no code change that session (QA verifying, PM/BA triaging) commits its entry directly to a `standups` branch that is merged daily — **the orchestrator's call, not this document's** [J].
- The PM/BA's summaries to the CEO (§6) are **not** kept here; they go to the CEO in chat. The file holds the working record only.

---

## 3. Before writing: what each seat reads (in this order, every run)

1. **Today's and yesterday's standup files** — especially any `BLOCKED` line naming your seat.
2. **The board, "By seat" view** filtered to your seat, and the **"Blocked"** view.
3. **Commits and PRs since the last entry by your seat:** `git log --since=<last entry>` on `main`, and open PRs referencing your tickets.
4. **For QA only:** the **"QA queue"** view.
5. **For every ticket you touch:** its row in `candour/products/haunt/requirements.md`, fetched fresh. Never work from memory of the criteria, and never from the ticket — tickets hold no criteria (D27).

---

## 4. The entry format — exact

```markdown
### <seat> · <HH:MM UK> · <session or agent id, if known>

**Done:** #<issue> <KEY> <what moved, one line> [, …]  — or "nothing moved"
**Next:** #<issue> <KEY> <what I will do next, one line> [, …]
**Blocked:** #<issue> <KEY> — <blocked by what, one line> — needs <seat | orchestrator | CEO>  — or "none"
**Notes:** <optional; at most two lines; anything the next reader would otherwise have to rediscover>
```

**Rules:**

- **Every line names a ticket number and its key** (`#42 CAP-4`). A line with no ticket is not an entry; it is chatter.
- **"Done" means a column move you made**, e.g. *"#42 CAP-4 → Review"* or, for QA, *"#42 CAP-4 → Done (QA-verified @ requirements.md a1b2c3d)"*. Code written but not moved is "Next".
- **Name failed limbs by letter**, never by pasting criteria: *"#42 CAP-4 back to In progress — (a) service-kill gap not recorded"*.
- **Five lines of content at most per entry.** Detail belongs in the ticket or the PR.
- **No entry claims anything the board does not show.** If the board and the entry disagree, the board is fixed first.

**Example**

```markdown
### engineer · 14:20 · run 7

**Done:** #42 CAP-4 → Review (PR #88); #45 CAP-6 → In progress
**Next:** #45 CAP-6 location-denied manual entry path
**Blocked:** #51 NOT-3 — waiting on SPK-07 answer (#12) — needs engineer (SPK-07 owner)
**Notes:** CAP-4 gap rendering reuses the SESS-8 surface, as the requirement says; no second query path.
```

---

## 5. When each seat writes

| Seat | Writes an entry | And also |
|---|---|---|
| **Engineer** | At the **start** of every run (a *Next* and any *Blocked* from reading §3) and at the **end** (what moved). One entry per run if the run is short | Moves its own tickets Backlog/Ready → In progress → Review. Opens PRs with `Refs #n`, **never** `closes`/`fixes`/`resolves` (backlog plan §7) |
| **QA** | At the **end** of every verification run, listing each ticket moved to Done or failed back | Is the **only** seat that moves a ticket to Done, and the only seat that closes an issue |
| **PM/BA** | **Once per working day** Haunts work happens, after reading every other entry that day | Triage: moves tickets Backlog → Ready, chases blockers, keeps the "Blocked" view honest, writes the CEO summary (§6), records scope changes in `requirements.md` §24 |

A day with no Haunts work has no file. **An empty day is not a missed standup.**

---

## 6. The PM/BA's summary to the CEO

Sent in chat by the orchestrator, **after** the PM/BA's daily entry, on days something changed. Per `CLAUDE.md`, *"Talking to the CEO"*: short, plain, leads with the answer, numbers and bad news included.

**At most five plain lines:**

1. **Progress:** tasks Done (QA-verified) today / total, and against the current phase — e.g. *"3 tasks QA-verified today; 41 of 211 overall; M1 at 18 of 26."*
2. **The one thing that matters most today** — good or bad, in one sentence.
3. **Blocked:** how many, and the worst one by name.
4. **Needs you:** a decision only the CEO can make — **one at a time**, or *"Nothing needs you."*
5. **Next:** what happens next, in one line.

No ticket numbers unless the CEO needs to open one. No jargon the CEO would have to look up. A day where a BLOCKING task failed QA says so on line 2.

---

## 7. How blockers escalate

| Blocked by | Who acts | How | Time limit before it goes up a level |
|---|---|---|---|
| **Another ticket or spike** | The seat that owns the blocking ticket | `Blocked` line naming it; the blocked ticket gets the `blocked` label and its "Blocked by" field set | Next PM/BA daily entry |
| **A seat's ruling** (CTO, CSO, CFO, CGO, UX) | **The orchestrator**, which commissions that seat | PM/BA's entry says *"needs <seat>"*; the orchestrator reads the file and commissions the seat with the ticket and the question | The orchestrator commissions within one working day of the entry [J] |
| **A spec defect** — a criterion that is wrong, untestable or contradicts another | **PM/BA** | The Engineer or QA writes it as a `Blocked` line naming the ID and limb; **nobody builds through it** (Engineer charter: *"raise spec defects… rather than building through them"*). The PM/BA answers in `requirements.md` and, if criteria change, a §24 row | Next PM/BA entry |
| **A CEO decision** (anything in Constitution 5.4 — money, pricing, user-data policy, kill/proceed, release) | **The CEO** | The ticket gets `needs:ceo`; the PM/BA's summary puts it on line 4, **one decision at a time** | Raised in the next summary; never decided by a seat |
| **A seat's block** (Constitution 5.6) | The blocking seat, or the CEO to overrule | Recorded as a block, citing the seat's charter ground; only the CEO may overrule, and every overrule is recorded in the decision record | Straight to the orchestrator and the CEO |

**A blocker listed on two consecutive days with no movement goes up one level automatically** — to the orchestrator if it was with a seat, to the CEO's summary if it was with the orchestrator. This is the standup's version of the evidence standard's *"twice-flagged is escalated"* rule [J, PM/BA]: a blocker that is merely repeated becomes furniture.

---

## 8. Handing work across Review → QA → Done

| Step | Who | What they do | What they write |
|---|---|---|---|
| **In progress → Review** | Engineer | Opens a PR with `Refs #n`; the PR lists, **by limb letter**, which test covers each acceptance-criterion limb of the requirement | Entry: *"#n KEY → Review (PR #p)"* |
| **Review → QA** | CTO (and CSO for `needs:cso-review`) | Approves and merges to `main`. **Merging does not make anything Done** | PR approval; the reviewer moves the ticket to QA |
| **QA → Done (QA-verified)** | QA | Verifies **every limb** in `requirements.md` for that ID on a named build, both platforms where the ticket says `both`; tries to break it (QA charter: *"try honestly to break it"*); records `requirements.md@<sha>`, the build, and the evidence link in the "Verified against" field; closes the issue | Entry: *"#n KEY → Done (QA-verified @ <sha>)"* |
| **QA → In progress (fail)** | QA | Moves it back with a comment naming the failed limb(s) by letter and the build. For a `mixed-priority` ticket, says whether a BLOCKING limb failed | Entry: *"#n KEY back to In progress — (b) fails on build <x>"* |
| **Untestable limb** | QA → PM/BA | If a limb cannot be executed as written, QA does **not** mark it passed or skipped. It writes a `Blocked` line *"needs PM/BA — KEY(c) not executable because …"* | Entry, as a blocker |

**QA verifies against the file, never against the Engineer's explanation** (QA charter: *"You verify against the spec, not against the Engineer's explanation of the code"*). A test that exists is not a limb that passes until QA has run it.

**A feature is demoable, not just green.** When the last task in a feature reaches Done, QA's entry says so, and the PM/BA's next summary tells the CEO the feature can be demonstrated. **Nothing is "done" in the Constitution's sense until its phase review pack and demo reach the CEO** (Constitution 5.5: *"Work is not 'done' until it has been reviewed"*).

---

## 9. Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-26 | 0.1 | First proposal |
