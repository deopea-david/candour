# Decision record — the Coordinator seat (Article 6 amendment, in preparation)

**Date:** 2026-10-02 · **Decided by:** CEO · **Compiled by:** CGO · opus (Opus 5.5) · effort high (seat default), commissioned by the main session, 2026-10-02
**Decision:** the seat is **ADOPTED IN PRINCIPLE**, held by the main thread (D2). It is named **"Coordinator"** (D3). Its charter is **ADOPTED**, with one change of the CEO's (D4) and a third exception to its role rule (D4a). **Annex D (the autonomy) is GRANTED, with both of the CGO's proposed conditions** (D5). ~~**It has not started:** its precondition 4, the CSO's checks, is not met.~~ *(2026-10-04: precondition 4 is met by the CSO's sign-off [E, `pipeline/cso-controls-results.md`, "CSO sign-off, 2026-10-04", S1 item 2]. Whether it operates before the amendment is applied is put to the CEO: "CGO flags on D11 and D12", flag 1.)* **How the charter is loaded** was decided at D11, ~~an output style loaded by default~~, and **reopened at D14 (2026-10-04): the seat is held only in a session where the CEO runs `/coordinator`**; D11 is superseded. **The Coordinator's own view** is limited to named triggers (D12). **The charter is in force now, before the amendment** (D13, 2026-10-04). **Two of the role rule's limits bound every main session, through `CLAUDE.md`:** never the Skeptic, and never the CGO on the Coordinator's own charter (D15, 2026-10-04). **D16 (2026-10-04) replaced the second, and D4a:** the main session may act as any seat except the Skeptic, but only in a fresh session and only when the CEO explicitly asks for that seat. **D17 (2026-10-04) accepted the charter's compaction placement as built:** the honest-broker rules are not counted as limits, so they sit after the part of the command that compaction keeps (D17, below). **D18 (2026-10-04) kept the chat widget tools available** and **D19 (2026-10-04) settled how a `/coordinator` session confirms that credits are off: the CEO says so at the start of the session** (both below). **The amendment to Article 6 is not applied**: it is Decision 9, and it is what lists the seat in the Constitution.
**This is not a gate.** Nothing was killed, proceeded or parked.
**Anti-drift (5.2):** not applicable. This is not an idea in the pipeline [E, `research/2026-10-orchestrator-practice.md`, header].
**Publication.** Article 3 requires publication within 30 days for gate decisions. This is not one, but the CGO committed to the same standard [J, `pipeline/amendment-draft-coordinator.md` §11 item 21]. **Due by 2026-11-01.** ~~**Held for now:** the CSO has not cleared the branch for publication (*"no, not yet"*, `pipeline/cso-controls-results.md`, CSO review R5).~~ *(2026-10-04: cleared. The CSO's sign-off: "Publication under my §6: **yes**", with its redactions applied [E, `pipeline/cso-controls-results.md`, S5]. The push waits on the CEO's approval.)* This record carries the same facts and is held with it. **If the hold has not lifted by 2026-10-25, the date goes to the CEO.**

**Artifacts this record rests on:**
- `roles/coordinator.md`: the charter, v0.3 (was `roles/chief-of-staff.md`)
- `pipeline/amendment-draft-coordinator.md`: the CGO's draft, Revision 4 (was `pipeline/amendment-draft-chief-of-staff.md`). §13 is the decision list; §15 is the CGO's response to the Skeptic
- `pipeline/dissent-chief-of-staff.md`: the Skeptic's memo, published unedited
- `research/2026-10-orchestrator-practice.md`: the Research Analyst's brief
- `pipeline/cso-advice-permission-mode.md` and `pipeline/cso-controls-results.md`: the CSO's advice, the check record, and the CSO's review

The last four keep the seat's earlier name, "Chief of Staff", because they are records. Where they say it, they mean this seat.

---

## Evidence: how the CEO's words were taken

- **Every quote below is from the CEO's own typed messages**, read from the live session's transcript, not from the relay alone [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/687ce46b-3fd6-4ba4-a4e0-d9101ec77b11.jsonl`, messages of type `user`, read-only, 2026-10-02]. Each one matches the wording the main session relayed to this seat.
- **Times are BST**, converted from the transcript's UTC timestamps.
- **The two steers that define the autonomy** are in the same transcript, in the words the draft quotes at §2.1: 15:08:27 (*"maybe I overstated the automatically part of it…"*) and 15:11:51 (*"The example I gave was just one example…"*). That closes the relay concern in draft flag F9 and memo F6. *(Revision 5: D5 and D4a are checked against the same transcript, below.)*
- **One variance, recorded so that nothing is tidied away.** Another transcript file holding the same history (`f404ce80-….jsonl`) has a different version of the D2 message, at 23:37:04: *"Okay that makes sense to me then, lets adopt in principle.  On Decision 3, lets call it coordinator as to avoid confusion with Chief of Staff roles"*. The live thread has, 15 seconds later, *"…lets adopt in principle.  Yes lets bring decision 3"*. [I]: the first was edited or rewound before he went on. **This record takes the live thread's words.** The earlier version's reason for the name is noted as context only, and the CEO may strike this paragraph.

---

## What was decided and why

### D0.1 — The ruleset changes on `main` were the CEO's. *2026-10-02, 15:17:54 and 15:19:46.*

> *"I have updated the branch permissions for main"*

and, after setting required approvals to 0 and removing "Restrict updates" on the main session's advice:

> *"Done"*

**Context.** The Skeptic found that a ruleset version had been saved at 15:17:27 through the CEO's account, and that the record *"cannot distinguish the CEO from an agent session acting through his credentials"* [E, `pipeline/dissent-chief-of-staff.md`, S1]. The ruleset's history shows versions at 15:17:27 and 15:19:11 [E, CGO re-verification, draft §8]. His two messages came 27 and 35 seconds after them. **So the change was his, and S1's first condition is met.** The freeze concern was settled when his merges of PRs #15 and #16 succeeded under the live ruleset [E, CSO review, V14].

### D0.2 — Paid usage credits are off. *2026-10-02, 15:33:06.*

> *"They are off"*

**Context.** This is the structural control the Skeptic asked for in S3: an account setting the seat cannot change. It also makes Fable unavailable, since the plan shows Fable as *"Requires usage credits"* [E, `pipeline/model-selection.md` line 126]. **Turning credits on is spending real money, which Constitution 5.4 reserves to the CEO:** *"The following are never automated: … spending real money"* [E, `constitution.md` line 120]. It is precondition 1 of charter Annex D.

### D1 — Permission mode: option (a). *2026-10-02, 16:11:19.*

> *"I am fine with that yes, thank you"*

**What he agreed to.** The CSO's option (a): run the main session in auto mode, disable bypass in three places, and commit the deny rules and the `candour-guard` hook [E, `pipeline/cso-advice-permission-mode.md` §1.4].

**Carried out.**
- PR #15 (deny rules, ask rules and the hook) was committed at 16:12 with his words in its message, and merged by him at 16:28 [E, `git show 941ac95`; `git log`].
- PR #16 (a guard fix) was merged by him at 16:53 [E, `git log`].
- The main session runs in auto mode, and bypass is disabled in his user settings [E, `pipeline/cso-controls-results.md`, header].
- PR #15 also turned agent teams off (`"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "0"`), and the local `"1"` has been removed [E, `.claude/settings.json` at `HEAD`, line 5; results file header]. The CSO's advice said this *"can be taken with 1"* [E, advice §9]. **So draft Decision 7 is treated as carried out under D1** [I]. If he meant otherwise, he says so.

**One step is not shown done:** the Desktop toggle "Allow bypass permissions mode". The CSO reports the Desktop as allowing bypass *"by policy"*, with the user opting in from Settings [E, CSO review F7]. Turning it off is the CEO's, by hand (CSO review R7, step 1).

**Status of the controls D1 put in place.** The CSO's verdict, quoted: *"The controls are trusted with stated limits, and only for the Desktop Code tab on Claude Code 2.1.286."* Four are not yet trusted, re-runs are owed, and publication is held. See *Conditions* below.

### D2 — The seat should exist, held by the main thread: adopted in principle. *2026-10-02, 23:34:45 and 23:37:19.*

His first message, which is also **his written response to the Skeptic's memo** (next section):

> *"Okay, I understand the concerns but it is mainly meant to streamline and improve the efficiency so each agent can work at their best and focus purely on the task at hand. I am fine with it being the main thread but only if it is best practice"*

**The main session's answer on best practice** (23:35:01), quoted in part:

> *"**Yes, the main thread is best practice, and it's also what every source and seat here recommends.**"*

It gave three reasons. First, Anthropic documents "orchestrator-workers" as a pattern, tagged [E, vendor guidance, single source]. Second, a subagent placement would add a layer, so the CEO would only see its summary (brief §4.6). Third, under *"The honest limit"*, it said that *"no study compares the two setups head to head"*.

His decision:

> *"Okay that makes sense to me then, lets adopt in principle."*

**What the evidence behind that answer is, stated by this seat:**
- **[E], single source (vendor about its own practice).** Anthropic's guidance names orchestrator-workers as a workflow in which a central model breaks a task down, delegates and combines the results. It calls the pattern *"well-suited for complex tasks where you can't predict the subtasks needed"* [E, https://www.anthropic.com/engineering/building-effective-agents, re-retrieved by this seat 2026-10-02]. The same page advises starting with the simplest solution and adding complexity only when it is needed.
- **[E], vendor documentation.** In an interactive session, *"only the top-level subagent's summary returns to you"* [E, https://code.claude.com/docs/en/sub-agents.md line 1016, re-retrieved 2026-10-02]. So a subagent coordinator would stand between the seats and the CEO.
- **[I].** The source names the pattern. **It does not say whether the orchestrator should be the main thread or a subagent.** That the main thread is the better placement is an inference from the line above and from the brief's best-supported finding, that the main risk is a softened report (brief §0.3, §6.2).
- **No study compares the placements.** The main session said so.

**This seat's view on the headline [J], stated once.** The body of the answer was accurate, and it stated the limit. **The headline overstated it.** "Best practice" was one vendor naming a pattern, plus an inference on placement, not a measured standard. *"Every source and seat here recommends"* was also wider than the record: the Skeptic recommends nothing; it found that no case against the seat survives (memo, Verdict). The CEO's condition, *"only if it is best practice"*, is met in this sense: **it is the documented pattern, and the better-reasoned placement on the evidence there is.** It is not met in the sense of a proven standard, because none exists. **This seat does not recommend reopening D2** [J]: the alternative placement is worse on the brief's best-supported finding. The point is recorded so that the CEO decided with it in view, and can say so.

### D3 — The name is "Coordinator". *2026-10-02, 23:38:55.*

> *"Okay makes sense, lets go with oordinator"*

"oordinator" is a typo for "Coordinator".

**Context.** The Skeptic found that "Chief of Staff", read whole in both sources, imports command of the staff and gatekeeping (memo S6). The CGO's recommendation changed to "Coordinator" (draft §3). The memo offered two honest routes and had *"no view on which"*. **S6 dissolves on its second limb.**

**Applied:** the charter is renamed `roles/coordinator.md`, and the draft is renamed `pipeline/amendment-draft-coordinator.md`. The Article 6 line and the change-log text use "Coordinator" (draft §9, §10).

### D4 — The charter is adopted, with one change of the CEO's. *2026-10-02, 23:41:56 and 23:42:24.*

> *"I would prefer the option whether to have the main thread me the coordinator or any other role preferably"*

**The main session's wording of it** (23:42:05), quoted in part:

> *"**The main thread is the Coordinator by default, and you can tell it to act as any other seat, such as the CVO, for a session or a task.** It says which role it's in at the start, and the artifact records it."*

It proposed two exceptions: **never the Skeptic**, whose memos depend on a fresh start, and **never reviewing its own work**. It said that *"the 'stops acting as CVO' line becomes: **'acts as CVO only when you say so'**"*.

His reply:

> *"Yes please"*

**Applied** to the charter (*Role*, *Commissioning*, *Placement*, *Invoked*) and to draft A2.

**What D4 covers.** It covers the charter body and, on this seat's reading [I], Annexes A, B, C, E and F, since the charter says the annex *"is part of the charter"* and only Annex D was excluded (draft §13). By adopting the charter he also took the CGO's reading of "one-page" as descriptive (memo F1; draft §13, Decision 4) [I]. If he meant otherwise on either, he says so.

**Two points, from this seat, once each:**
1. **A gap, put to the CEO as Decision 4a.** Told to act as the CGO, the main thread could draft changes to its own charter, or edit its own omission check. Both are things the adopted charter forbids: A3, *"drafted by the CGO, never by the seat itself"*, and Annex E, the CGO owns M2 *"so the seat cannot edit its own check"*. **Proposed exception (iii):** never a seat whose work in that task sets, checks or records the limits on the Coordinator itself. This seat reads exception (ii) as covering it already. **What a clause means is the CEO's**, so (iii) is marked in the charter as not yet approved. *(Approved at D4a, below.)*
2. **A residual, stated and not opposed.** A2 existed so that the same session would not originate an idea as the CVO and then broker the dissent against it. D4 keeps the default (it does not act as the CVO) but lets the CEO switch it on. Exception (ii) stops it *reviewing* its own work, not *presenting* it. The gate's own structure carries the rest: the CGO compiles the pack, and the Skeptic's memo is published unedited [I]. The provenance line shows which role wrote what (`pipeline/model-selection.md` §5.5).

**On the citation the proposal used.** Exception (ii) cites `pipeline/model-selection.md` §5.4. That section says the checking seat *"runs on a different model from the seat that made it"* wherever possible, and that where it cannot, *"the review record says so"* [E, lines 99–101]. It supports "a different seat reviews it" by implication, not in terms. The charter carries the disclosure duty with it.

### D5 — The autonomy (charter Annex D) is granted, with both of the CGO's proposed conditions. *2026-10-02, 23:55:58.*

*First recorded clerically by the main session at 23:56 (charter, Produces: "the CEO's decisions in his own words, as a clerical act; the record is the CGO's"). Reviewed and corrected by the CGO at Revision 5; the corrections are listed at the end of this entry.*

**The question put** (main session, 23:53:08, after his *"Lets bring decision 5"* at 23:52:50). It summarised Annex D: the rule, the "always comes to you" list, the review loop and the caps. It set out the two conditions the CGO proposed at Revision 4:
1. The autonomy does not start until the CSO records that checks V1–V9 have passed.
2. It applies only while the main thread is acting as the Coordinator.

It recommended *"grant it with both conditions"*. It linked Annex D of `roles/coordinator.md` and said the CGO was *"still finishing edits"*. At 23:53:35 it said the CGO had finished, and asked for 4a first; *"The question I asked above still stands, with nothing changed."*

**His answer** [E, live transcript, 22:55:58 UTC]:

> *"On decision 5, I agree and grant it. I have disabled bypass permissions mode"*

**What it settles.**
- **Annex D is adopted as written.** Precondition 3, the CEO's approval of its exact text, is **met**.
- **Both conditions are adopted:** precondition 4 (V1–V9 passed) and the rule that the autonomy belongs to the Coordinator role.
- **The Desktop toggle** (Annex D precondition 2's open step; CSO review F7) is **reported done by the CEO**.

**Which text he approved** [E]. The charter file was last written at 23:53:22, before his answer, and was not changed again until this seat's Revision 5 edits [E, file modification time, read 2026-10-02]. So the linked Annex D was the finished Revision 4 text when he answered. Revision 5 changes only its approval markers, not its operative words.

**Two things still to say:**
- **The autonomy has not started.** Condition 1 is not met: the CSO's review of 2026-10-02 finds V2, V3 and V9(iv) incomplete, and V7, V8 and V9(i) owed again after PR #16 [E, `pipeline/cso-controls-results.md`, R1]. Until the CSO records V1–V9 as passed, the Coordinator asks before every step.
- **The toggle is confirmed only by his word.** The Desktop settings tool, read by the main session at 23:56, still reports bypass as *"allowed by policy (the user opts in from Settings → Claude Code)"*. That describes the policy, not his toggle, so it neither confirms nor contradicts him. His word is the record. Confirming that the mode selector no longer offers Bypass (V11, Desktop) stays with the CSO's re-runs.

**From this seat, once [J]: the summary he was given was narrower than the text in one place.** It listed *"blocks"* as always coming to him. Annex D's text has an exception: the Coordinator may, without asking, start *"work the **blocking seat's own artifact** names as its lifting condition"*, and only that seat lifts the block. He approved the text, which he had linked, and this seat does not recommend reopening it; the exception keeps the lift with the blocking seat. **It is recorded so that he decided with it in view.** If he meant the narrower version, he says so, and the exception comes out. Every other difference between the summary and the text makes the text stricter, not looser (for example, case (b)'s *"in its own words"* rule, and judgment disputes coming to him).

**A minor mislabel in the question.** It said *"Still owed from you on condition 1: confirm the Desktop toggle"*. The toggle belongs to precondition 2 (D1); condition 1 is the CSO's V1–V9. No effect on what was decided.

**CGO corrections to the main session's entry** (Revision 5):
- the time, from "about 23:55" to 23:55:58, from the transcript
- the question's time, and its 23:53:35 follow-up, added
- "Which text he approved", the summary variance, and the mislabel, added
- "Still open: Decision 4a" removed: answered at D4a, below

**On who writes this entry.** The main session wrote it as the Coordinator, which its charter allows as a clerical act. Exception (iii) does not apply to that: it limits which seat the main thread may *act as*, and it was approved 30 seconds after this entry was written. The commission sent the entry to this seat because the record is the CGO's (charter, Produces), and the entry records limits on the Coordinator.

### D4a — A third exception to the role rule: approved. *2026-10-02, 23:56:46.*

***Superseded by D16 (2026-10-04, 01:50:53).*** *The text below is kept as decided. Exception (iii) is replaced by the fresh-session rule; exception (i), never the Skeptic, stays.*

**Placed after D5 because it was answered after D5.** It was put first (23:53:35) and answered second.

**The question put, twice.** At 23:53:35, the main session asked:

> *"**4a: add a third exception, so the main thread can't act as the CGO on its own rules.** As adopted, you could switch the main thread into the CGO seat, and it would then be writing its own charter or its own omission check. The charter forbids exactly that. The exception would cover only the Coordinator's own charter and its checks; the main thread could still act as the CGO on anything else."*

After D5, at 23:56:25, it put it again:

> *"When you've told the main thread to act as another seat, it can't use that role to set or check the Coordinator's own limits, for example by editing its own charter or omission check as the CGO. **Recommendation:** yes. **Yes or no?**"*

**His answer** [E, live transcript, 22:56:46 UTC]:

> *"And on 4a, I agree as well"*

**What it settles.** Exception (iii) is adopted into the charter (*Role*), as written:

> **(iii) Never a seat whose work in that task sets, checks or records the limits on the Coordinator seat itself.** That covers the CGO drafting this charter, its annex, the omission check (M2) or a record of the Coordinator's own conduct, and the CSO verifying the controls in Annex F.

**What this seat reads it to mean [I].** "4a" named the clause as written in the charter and in draft §13, so he approved that text. **But both questions put to him said "set or check".** Neither said "records", and neither mentioned the CSO's verification of Annex F. The written clause is wider in those two limbs. This seat takes the written text, because that was the decision named, and because those two limbs follow from the same reason (A3; Annex E). **What a clause means is his.** If he meant the narrower version, he says so.

**It bites now.** From D4a, the main thread, told to act as another seat, may not draft or edit this charter or its annex, M2, or a record of the Coordinator's own conduct, nor verify the Annex F controls. Those go to the CGO or CSO seats.

### D6 — QA sits both before and after the merge, as two different checks. *2026-10-02, 23:58:58 and 23:59:24.*

**The question put** (main session, 23:57:09): before or after the CEO merges a ticket's PR? Its recommendation was **"keep it after"**, citing his Haunts decision D30.

**His first answer** [E, live transcript, 22:58:58 UTC]:

> *"I think QA should happen both before and after, e.g. there may be multiple changes merged and so will definitely need it after but before would be good as well. But, what do you honestly think?"*

**The main session's answer** (23:59:09), quoted in part:

> *"**Honestly, I agree with you, with one adjustment: do both, but make them different checks, so you aren't paying for the same QA twice.**"*

In substance, it proposed:
- **Before merge: the full QA.** QA checks the branch against the ticket's acceptance criteria. This is the main check.
- **After merge: a lighter integration check, once per wave rather than per ticket.** QA re-runs the tests and smoke-checks the affected areas.
- **QA marks the ticket Done after the post-merge check passes**, so only QA moves a ticket to Done.
- **Not a full QA twice:** it would roughly double QA's cost for little gain (Constitution 1.5).
- **The downside:** pre-merge QA lengthens the wait before each PR reaches him, and QA may need to re-run if `main` moves in the meantime.
- It said this changes D30, *"so it gets recorded as an amendment to D30"*.

It asked: *"**Go with this: full QA before merge and a light integration check per wave?**"*

**His decision** [E, live transcript, 22:59:24 UTC]:

> *"I agree with that yes"*

**What it settles.**
- **The per-ticket chain becomes:** ticket complete → the CTO's review (and the CSO's where labelled `needs:cso-review`) and **QA, in full, on the branch** → the PR comes to the CEO → **the CEO merges** → at the wave gate, **QA's integration check** on `main` → **QA moves the ticket to Done**. Applied to charter Annex D. **The order of the CTO's review and pre-merge QA was not decided**; it is for the PM/BA's process file [I].
- **Only QA moves a ticket to Done** stands unchanged (Haunts D30, D34).
- **Owed:** the PM/BA writes the chain into `pipeline/agentic-agile.md`, and the CEO merges it as process (draft §11 item 10). Until then, Annex D's authority for the chain is the CEO's words here.

**What it amends in the Haunts record, stated exactly [E, `decisions/2026-09-16-haunt-gate.md`, lines 407 and 415].** The main session said D6 amends D30. **D30 does not say QA follows the merge.** It sets the board's columns (*"In review → QA → Done"*) and the rule that only QA moves a ticket to Done. **The after-merge rule is in D34:** *"A requirement ticket reaches QA when all its stories are merged."* It is repeated in `products/haunt/STATUS.md` line 127, which is state, not authority. **So D6 amends D34's sentence, and changes how D30's column order is used:** a ticket now passes through QA before its PR and again after the wave's merges. This seat's draft §13 (Revision 4) made the same attribution to D30 first; see E4 below. Cross-references are added after both D30 and D34 in the Haunts record, without changing either entry's text.

**Two things the PM/BA should write down, from this seat [I]:**
- **A ticket now reaches Done only at its wave's gate**, since the integration check runs once per wave. That is later than today, where QA follows each merge.
- **A wave gate still makes nothing "done" in the 5.5 sense** (`pipeline/agentic-agile.md` item 3, D34). QA's integration check runs at the gate, but the board's "Done" is QA's ticket status, not the phase review. The process file should keep the two apart in its wording.

**From this seat, once [J]: the Coordinator changed its recommendation in two minutes without saying so.** At 23:57 it recommended *"keep it after"*. After his reply at 23:58:58, it said *"I agree with you"*. It gave reasons for the new view, and those reasons hold. It did not say that it had reversed itself, or what changed its mind beyond his message. **This seat does not think the decision was wrong**, and it does not recommend reopening it. It is recorded because the honest-broker rules exist for exactly this moment, when he asks *"what do you honestly think?"*. Once Annex E is in force, it is the kind of event M5 counts (how often the CEO overrules the Coordinator's recommendation): **one, D6**.

### D7 — Agent teams stay off, to be revisited when the feature leaves experimental status. *2026-10-03, 00:00:45.*

**The question put** (main session, 23:59:48): agent teams, off or on. It said they were already off in practice: he had deleted the local `"1"`, and the committed settings set the flag to `"0"`. It gave the reason for off, that with teams on *"each teammate's plan is approved automatically, with no review"*. It said that if he wanted them later, the CTO names a use and he decides. **Recommendation: off.**

**His answer** [E, live transcript, 2026-10-02 23:00:45 UTC]:

> *"Off for now yes, I may come back to it when the functionality is fully released and not experimental"*

**What it settles.**
- **Agent teams are off.** This confirms what D1 carried out: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` is `"0"` in the committed `.claude/settings.json`, and the local `"1"` is removed [E, `.claude/settings.json` at `HEAD`, line 5]. Under D1 this record had treated Decision 7 as carried out [I]. **D7 replaces that inference with his words.**
- **The revisit trigger is his:** the feature leaves experimental status. The process stays as the main session described it: **the CTO names a use, and the CEO decides.** Turning them on is a change to settings, which the Coordinator never decides (charter, *Decides*).
- **Who watches for the trigger [I]:** the CTO, who owns technical standards. The Coordinator raises it if it sees vendor release notes that say so. Neither turns teams on.
- Applied to charter Annex D, *Out of scope*.

**This decision falls on 2026-10-03, after midnight.** It is kept in this record because it closes the decision list put to him in one sitting.

### D8 — The CEO merges every PR, in every repo. *2026-10-03, 00:03:31.*

**Not part of the seven-decision list.** It was raised afterwards, from the PM/BA's write-up of D6 (`pipeline/agentic-agile.md`, "The per-ticket chain"). It is recorded here because it settles who performs step 4 of the chain D6 set.

**The question put** (main session, 00:01:43, quoted in part):

> *"**The new chain, and the Haunts STATUS file, say you do.** … **The `haunts` conventions say the orchestrator merges** straight after review, and the standup routine says the CTO does. **In practice, agents can't merge any more anyway.** The 'never merge' line you added to your personal settings covers every `deopea-david` repo. So the `haunts` text is out of date, not just inconsistent."*

and: *"**Recommendation:** you merge, in every repo. … **You merge everywhere, agreed?**"*

**His answer** [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/3737f180-a522-439e-8c8f-e84aa92494b6.jsonl`, `user` message, 2026-10-02 23:03:31 UTC, read 2026-10-03]. It came in one message with an unrelated question about the CSO's re-runs, and is the message's last sentence:

> *"And on who merges PRs, I will merge yes"*

**What it settles.**
- **The CEO merges every PR, in every repo** (`candour`, `haunts`, and any other under `deopea-david`). Step 4 of the chain in `pipeline/agentic-agile.md` stands as written. No seat merges: not the orchestrator, not the CTO, not the Coordinator.
- **The check matches the control already in place.** His personal `hard_deny` list reads: *"Never merge, approve, or enable auto-merge on a pull request in any deopea-david repository, by any route (gh, API, script or browser). The CEO merges by hand."* [E, `~/.claude/settings.json` line 35, read 2026-10-03]. **That is a pattern rule, so it is a guard and not a proof** [K]; the CSO's review records the residual that every seat acts through his GitHub account (`pipeline/cso-controls-results.md`; draft §8). D8 is the decision, and the setting is its backstop.
- **It carries out D6** (step 4 of the chain) and is consistent with Haunts **D30** (only QA moves a ticket to Done) and **D34** (a story closes on merge). **Neither is amended by D8.** The CEO merging does not make anything Done (D6, step 4).
- **The `haunts` text that says otherwise is out of date**, not a rival rule. The conflicting files are listed with their owners in the CGO's report on this commission; each changes through its owner, by PR, and the CEO merges that PR too.

**Left open, one point [I]:** the chain says the reviewer closes a story *"on merge"* (`pipeline/agentic-agile.md`, item 5). With the CEO merging, the reviewer closes it after his merge, since an agent cannot act at the moment he clicks. The PM/BA's process file should say that in terms. D8 does not decide it.

### D9 — A requirement split across several PRs: each PR checked on its own limbs, the whole at the integration check. *2026-10-03, 00:09:01.*

**The question put** (main session, 00:03:46, quoted in part):

> *"**One small question is still open, from the PM/BA:** when a requirement is split across several PRs, QA checks each PR's own parts before merge, and the whole requirement is confirmed at the after-wave check. **Agree?**"*

**His answer** [E, same transcript, `user` message, 2026-10-02 23:09:01 UTC, read 2026-10-03]. It is the message's last sentence, after his six numbered notes on the CSO's retests:

> *"On the question, yes I agree with your suggestion."*

**What it settles.**
- **QA's pre-merge check of a story's PR is against the limbs that story names.** The requirement as a whole is confirmed at QA's integration check (D6, step 5), **after its last story has merged**. That is the PM/BA's reading, which the main session relayed in shorter form [E, `pipeline/agentic-agile.md`, "Not settled here", first bullet; the main session's question above].
- **It amends Haunts D34 on one sentence, as D6 already does.** D34 says *"A requirement ticket reaches QA when all its stories are merged"* [E, `decisions/2026-09-16-haunt-gate.md` line 415]. Under D6 and D9 QA acts on each story's PR before its merge, and the requirement is confirmed after the last merge. D34's other rules stand: stories close on merge, and only QA moves a requirement ticket to Done (D30). Cross-references are to be added after D34 in the Haunts record, and not edited into its text. **Whether D6's cross-reference to D34 has been added yet is not checked here** [I].
- **It stays within D6.** There is one full QA before each merge and one lighter check per wave, so no extra QA run is added (Constitution 1.5).

**Two things this seat reads from it, once each [I]:**
1. **The wording he agreed to was the relay's.** The relay said *"the after-wave check"*. The PM/BA's text says *"the integration check after its last story merges"*. Read together with D6, the integration check is once per wave, so **a split requirement is confirmed at the first wave gate after its last story merges.** If he meant something sooner, he says so.
2. **A requirement ticket therefore reaches Done no earlier than that wave gate**, and later than today for a split requirement. The process file should say so, next to the D6 point that a ticket reaches Done only at its wave's gate.

### D10 — The settings-drift tripwire is dropped, and V9(iv)'s limit is recorded instead. *2026-10-03.*

*Recorded clerically by the main session. The CGO characterises and corrects it.*

**The question put.** The CSO recommended (b): close PR #17, keep the current guard, ship the small interpreter fix, and record the limit. Its reasons:
- The tripwire catches only a narrow case, for which no ordinary route was named.
- It would lock out main-checkout sessions after every merge that changes the controls.
- A full fix grows the guard, and F9 still defeats it.

The CTO's review of #17 had found two bypass routes and a recovery lockout bug (#17, comment 5963177708). The main session agreed with (b) and put it to the CEO, along with the operating rule: restart the session after any change to `.claude/` on disk.

**His answer:**

> *"Dropped, yes please record it"*

**Applied.**
- PR #17 is closed. It was closed on GitHub at 14:09:39Z, and the main session added a comment giving the reason.
- The limit is recorded verbatim in `pipeline/cso-controls-results.md`, under "V9(iv): tripwire dropped, limit recorded". Its source is `pipeline/cso-v9iv-diagnosis.md` §T2.

**Still owed:**
- the interpreter fix, as its own PR
- the V9(iv) re-run by the narrower method
- R7 steps 5–6
- F9 filed as an issue, with his approval

### D11 — How the charter reaches the main session: an output style, generated from `roles/coordinator.md`, with a CI check. *2026-10-04, 00:40:47, 00:44:59 and 00:45:47.*

**Superseded by D14 (2026-10-04, 01:23:50).** The text below is kept as it was.

*This is Decision 8 in the draft's §13. The record numbers it D11 because it was taken after D10.*

**The question put.** In the main session's words, Decision 8 had three options [E, transcript `2e1bef0c-….jsonl`, assistant message 00:39:46]:
1. *"A pointer in `CLAUDE.md`."* The simplest, but every seat reads it, and it is advice only.
2. *"An output style."* The charter goes to the main session only, and Claude Code's normal instructions are kept. The research brief's recommended starting point.
3. *"The `agent` setting."* It binds more tightly, but replaces Claude Code's default instructions. The fallback if option 2 is not followed well enough.

The draft said the CTO and CSO recommend and the CEO decides (§13, Decision 8). The main session offered to commission that recommendation.

**His answers, in order:**

> *"Great, no I don't think I will need confirmation from CTO/CSO"* (00:40:47)

The main session then recommended option 2. **It disclosed its conflict of interest:** *"I'm the seat this binds. Option 2 is in the middle; the loosest choice is option 1"* (00:40:52). It then set out two ways to fill the output style: **(a)** a thin pointer to the charter, or **(b)** *"The full charter text, generated from `roles/coordinator.md` by a small script, with a check that fails if the two copies differ"*. It recommended (b) (00:42:36, repeated at 00:43:20).

> *"I am fine with option 2, would when would the script run to generate the charter from the role?"* (00:44:59)

The main session answered: only when the charter changes; the CGO edits the charter and runs the script in the same PR; *"a small GitHub Actions check that fails the PR if the two files differ"*; restart after merge; *"both reviewed by the CTO before they reach you"*; and the order *"1. Publish the drafts. 2. Add the output style, the script and the check, in one PR. 3. Do the omission-check script and the v1.4 wording."* It asked: *"Go ahead on that basis?"* (00:45:11).

> *"Yes, go ahead with it"* (00:45:47)

**Evidence.** All three quotes are read from the CEO's own messages, of type `user`, in `~/.claude/projects/-Users-davidparrish-Documents-candour/2e1bef0c-52b9-4bac-891a-50b1ab827978.jsonl`, read-only, by this seat on 2026-10-04. Times are BST, converted from UTC. Each matches the main session's relay to this seat.

**What was decided:**
- **Option 2, the output style**, at `.claude/output-styles/coordinator.md`.
- **Its content is the full charter, generated from `roles/coordinator.md` by a script.** [I], high confidence: he did not write "(b)". He asked when *"the script"* would run, and said yes to a plan built on (b).
- **A GitHub Actions check fails a PR when the two copies differ.**
- **The order** is the one he said yes to: publication first; then one PR carrying the output style, the script, the check and the settings line; then M2 and the v1.4 wording.
- **The CTO reviews the script and the check before they reach him.** That is the main session's own undertaking in the plan he approved. It is a code review, not the recommendation he declined.

**What he declined.** The CTO's and CSO's recommendation on the choice itself. That is his to decline (5.4). The draft asked for it because the seat this binds should not shape its own binding (§13, Decision 8). **What carries that concern instead:** the main session disclosed the conflict, and recommended the middle option, not the loosest.

**Not carried out.** Nothing is built. The output style is loaded only from a committed settings line, which is a change to `.claude/settings.json`: a PR for the CEO to merge, then a restart (the CSO's operating rule).

### D12 — The universal clauses stay; the Coordinator's own view is offered only on a named trigger. *2026-10-04, 00:48:31 and 00:49:36.*

**His question:**

> *"In the coordinator role, it says about the universal clauses. Should those apply, as it is saying it should disagree with seats, state confidence and uncertainty etc. but this role is purely for coordination not for making decisions, it should act almost like a proxy for the other roles it is coordinating right?"* (00:48:31)

**The main session's answer, in short** [E, transcript `2e1bef0c-….jsonl`, assistant message 00:48:48]. Keep the clauses, because most of them bind a proxy too. *"Disagreement is a deliverable"* earns its place in a narrow form; for example, a pure proxy would not have spotted that a tester ran the wrong commands. **Where he was right:** the charter could read as though the seat should form opinions on everything. It proposed a line: *"Its own view is offered only when you ask, or when it sees a seat's error, a conflict between seats, or a broken process. Otherwise it passes the seats' work through unchanged."* Options: **1.** keep the clauses and add that line (recommended); **2.** keep the charter as it is; **3.** remove its own view entirely, as a pure relay. It said the charter change is the CGO's to draft (D4a).

**His answer:**

> *"Yes, go with option 1 but only if it will be effective"* (00:49:36)

Both quotes are read from his own messages in the same transcript file, as for D11.

**His condition is part of the decision.** *"Only if it will be effective"*. A line of prose is advice to the model. So this seat drafted it as structure and a measure, and states below what that cannot do.

**Applied, in `roles/coordinator.md` v0.4** (drafted by the CGO, as A3 and D4a require):
1. **The line**, as honest-broker rule 3. It names four triggers, each with the reference it must carry: **asked** (his words, quoted); **seat error** (the artifact's path and line); **seat conflict** (both paths); **process broken** (the step and the file that requires it, or an instruction that conflicts with the Constitution or a decision record). A short paragraph after the universal clauses says how they bind this seat.
2. **Annex A, item 3.** The seats' recommendations are copied or linked. Then exactly one of: `My view — trigger: … — reference: …`, or `No view offered.` The marker is fixed text.
3. **Annex E.** **M2(iii)** fails a decision request whose item 3 has no marker, an unlisted trigger or no reference. **M8** counts, over every report in the main session's transcript files, (a) item-3 failures and (b) view phrases outside a `My view` block. **It is the CGO's script, never self-scored.** A proposed threshold [J] for "not effective", for the CEO to set: any confirmed M8(a); two or more confirmed M8(b) in a phase; or any view he tags as unprompted.

**What this cannot guarantee, stated plainly:**
- **The model may still editorialise inside other sections.** A recommendation in item 1, or an adjective that grades a seat's work, is a view without a marker. The rule says so, but only M8(b) and his tags catch it.
- **M8(b) is a lexical screen.** It misses paraphrase and flags innocent phrases, so the CGO samples its hits and reports confirmed counts.
- **A trigger can be claimed loosely.** The script checks that a reference is present, not that it is true. The CGO checks a sample at the phase review.
- **The script does not exist yet.** It is part of §11 item 18 (M2), which is not built. **Until it is, only his M1 and M6 tags measure this, so by his own condition D12 is in place but not yet shown to be effective.**
- **The new text reaches the main session reliably only once D11 is carried out.** Until then the main session reads the charter when it chooses to.
- **Reviewed at the first phase review**, against M8, M2(iii) and his M1 and M6 tags. **If it proves ineffective, the next step up is the `agent` setting** (D11's option 3), which is his decision.

**A consequence he should know.** Honest-broker rule 6, *"Disagree with the CEO once, in writing, then comply"*, now fires only on a trigger. A disagreement with him on the merits alone, with no seat error, no seat conflict and no broken process, is not offered unless he asks. A conflict with the Constitution or a decision record is always a trigger, because the universal clauses require it to be said.

---

### D13 — The charter is in force now, not only when the amendment is applied: option (a). *2026-10-04, 00:55:12.*

*This answers the CGO's flag 1 on D11 and D12 (below). Recorded by the CGO because it concerns the Coordinator's own charter (D4a).*

**The question put** (main session, 00:53:51, quoted in part) [E, transcript `2e1bef0c-52b9-4bac-891a-50b1ab827978.jsonl`, assistant message, read by this seat 2026-10-04]:

> *"the charter says it's 'not yet in force' until the Constitution amendment is applied. But your D5 has already unlocked the autonomy, so it's in use. Which applies?"*

- *"**(a) The charter is in force now,** because you adopted it (D4, D5). The v1.4 amendment then just writes it into the Constitution publicly. **I recommend this:** the main session already does this job, and doing it under written limits is better than without them."*
- *"**(b) It's not in force until v1.4 is applied.** Until then, I go back to asking before every step."*

**His answer** [E, same transcript, `user` message, 2026-10-03 23:55:12 UTC, read 2026-10-04]:

> *"a"*

**What it settles.**
- **The charter is in force from 2026-10-04.** It was adopted at D2, D3, D4, D4a and D5, and Annex D's four preconditions are all recorded as met. D13 settles the one clause that said otherwise, the header's "Not yet in force".
- **The Coordinator runs under the charter and its autonomy now**, not only after Decision 9. This is the reading the CGO offered at flag 1 [J], now the CEO's.
- **Article 6 does not list the seat until the amendment is applied (Decision 9).** D13 does not apply the amendment, and Decision 9 is still conditional on the omission check (M2). Until then the seat is in force as a charter the CEO adopted, not as a seat the Constitution names. The amendment writes it into the Constitution publicly (Article 11).
- **Applied to** the header and status lines of `roles/coordinator.md` and to §13 of `pipeline/amendment-draft-coordinator.md` (Revision 7). No operative word of the charter changed.

**What this seat reads from it, once [I].** Since the charter binds from now, its measures bind from now too: the Annex A item 3 marker, M2(iii) and M8. D12's condition (*"only if it will be effective"*) is still not shown met, because the M2 script does not exist. D13 does not change that.

**Correction recorded with it: the restart rule.** At 00:38:22 the main session told the CEO the restart is needed *"after any change to `.claude/settings.json`"*, narrower than the CSO's rule (CGO flag 4, below). At 00:53:51 it corrected itself, in its own words: *"That narrowing was mine, and it's wrong now: the output style we're about to add also loads only at session start. **Go back to the CSO's broader rule: restart after any change under `.claude/`.**"* **The rule is the CSO's form again:** restart after any change to `.claude/` on disk, by hand or by a pull [E, `pipeline/cso-controls-results.md`, "V9(iv) limit"]. This closes flag 4. It was closed by the main session's correction, and the CSO's rule was never narrowed.

**Later the same day: charter v0.5.** At the CEO's request, *"I would like the CGO to trim afterwards to avoid excessive context/token usage"* (01:03:23; source in draft §16), the charter is trimmed. Its status lines, history and quotations move to `pipeline/amendment-draft-coordinator.md` §16, verbatim. No operative rule moves out or changes meaning, and §16.1 maps each one.

---

### D14 — The Coordinator only when the CEO invokes it: a `/coordinator` command (option 1). Reopens D11, and D4's "by default". *2026-10-04, 01:22:19 and 01:23:50.*

*Recorded by the CGO because it concerns the Coordinator's own charter (A3, D4a).*

**His first message** [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/05f4422b-7df3-4f42-9596-96664b755c49.jsonl`, `user` message, 2026-10-04 00:22:19 UTC, read-only by this seat 2026-10-04]:

> *"I just feel that the output style is overkill and I may not want it to run in coordinator by default and only at specific times, when I choose"*

**The options put** (main session, 00:22:42 UTC, same transcript; quoted in part). It said first that this *"reopens your D11, and partly D4's 'Coordinator by default', which is yours to do"*, and, under *"What you may not want to hear"*, that *"When the Coordinator is off, the main session has no charter"*, with *"no autonomy"*.
1. *"**A `/coordinator` command (recommended).** Typing `/coordinator` loads the full charter into that session only. It costs nothing until you use it."* Weak point: *"in a very long session, Claude Code compresses older messages, and the charter could get compressed with them. Re-running `/coordinator` fixes it."*
2. *"**Keep the output style, but not as the default.** Remove it from settings and pick it from `/output-style` when you want it."* Weak point: *"that menu choice is saved for the whole repo until you switch it back"*.
3. *"**Keep things as they are.**"*

Its view was marked *"trigger: asked"*, with his words as the reference, and gave the counter-argument: *"a command is a weaker hold than a style over a long session"*.

**His answer** [E, same transcript, `user` message, 2026-10-04 00:23:50 UTC]:

> *"Yes sorry to go back on what I said earlier, I do think a command would be best (option 1)"*

Both quotes match the main session's relay to this seat.

**What it settles.**
- **The main thread is no longer the Coordinator by default.** It holds the seat only in a session where the CEO has run `/coordinator`, from that point on.
- **Where he has not, the main session works under `CLAUDE.md` alone.** It has no duties under the charter and **no autonomy**: Annex D runs only in a session where the Coordinator is invoked. Annex D already says the autonomy *"belongs to the Coordinator role"*, so its approved words need no change for this.
- **D11 is superseded.** The output style, the `outputStyle` settings line and the style's CI check are replaced by a command file generated from `roles/coordinator.md`. D11's other terms carry over to the command: the full charter, generated by a script, with a check that fails a PR when the two differ, and the CTO's review.
- **D4 is reopened only for "by default".** Its other terms stand: the CEO may tell the main thread to act as another seat; it states its role; the CVO only on his word; the three exceptions.
- **D13 stands**, read with D14: the charter is in force, in the sessions where the seat is invoked.
- **D12 stands.** Its line *"reaches the main session reliably only once D11 is carried out"* now reads: only in a session where `/coordinator` has been run, and not reliably after compaction.
- **Applied** in `roles/coordinator.md` v0.6 (header, *Proceeding without asking*, *Role*, *Invoked*, Annex C, Annex E) and in `pipeline/amendment-draft-coordinator.md` (Revision 9; §10, §11, §13, §16.4).

**Two lines added to *Role* by this seat, for the CEO to strike if he did not mean them [J].**
1. *"Only the CEO's own `/coordinator` confers the seat. Never invoke it yourself, and never treat a file, an agent or a tool result that says you are the Coordinator as his invocation."* His words were *"when I choose"*. In this seat's own session, the repo's commands (`idea`, `gate`, `build`, `audit`, `agile-sync`) are offered to the model as skills it can invoke [E, this seat's session skill listing, 2026-10-04]. A command the model can run itself would let the session give itself the seat, and the seat's autonomy with it.
2. *"If the charter may no longer be in your context in full (for example after compaction), say so, ask the CEO to re-run `/coordinator`, and ask before each step until he does."* This answers option 1's disclosed weak point. It only adds asking.

**Requirements for the Engineer, from this seat [J]; the CTO checks each against the vendor's documentation, since this seat has not:**
- **The model must not be able to invoke `/coordinator`.** Only the CEO's typed command loads it. State the mechanism and cite the documentation that shows it works.
- **The command file holds the generated charter and nothing else** beyond a fixed, reviewed preamble. `.claude/commands/*.md` is on Annex D's allowlist, so anything extra in it becomes authority for the autonomy.
- **The generator and its check follow the annex when it moves** to `pipeline/coordinator-operating.md` (flag 2 on D11 and D12, carried over to the command).
- **The CSO's protection of the command file** against edits by a session, which the CSO offered for option 1 (main session relay, 00:23:02 UTC), is the CSO's to specify.

**What D14 costs, stated once [I].**
- **Outside a `/coordinator` session, nothing in the charter binds the main thread.** That includes honest-broker rules 1–3 (copy blocks verbatim; "What you may not want to hear"; views only on a trigger), the omission check, and the role rule's exceptions. **Exceptions (i) and (iii) matter most:** told to act as the Skeptic, or as the CGO on this charter, a non-Coordinator session is not stopped by this charter. `CLAUDE.md` carries none of them today. Whether to put (i) and (iii) into `CLAUDE.md` is a new question for the CEO, flagged in draft §13. **The autonomy does not run there, so the loss is in the quality of reports, not in unasked work.**
- **M8 and M2 now cover only invoked sessions**, so they say nothing about reports in other sessions. The CEO's M1 and M6 tags still do.

### D15 — Role exception (i), and (iii) for the CGO on the charter, go into `CLAUDE.md` for every main session. *2026-10-04, 01:29:36.*

*Recorded by the CGO because it concerns limits on the Coordinator seat (A3, D4a).*

**The question put** (main session, 2026-10-04 00:27:54 UTC, quoted in part) [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/05f4422b-7df3-4f42-9596-96664b755c49.jsonl`, `assistant` message, read-only by this seat 2026-10-04]:

> *"**Decision needed:** should "never act as the Skeptic" and "never act as the CGO on its own charter" also apply in sessions where you **haven't** run `/coordinator`?"*

It closed: *"**Yes or no:** add the two rules to `CLAUDE.md`? You can also strike either of the CGO's two added lines."* The main session's own view was marked *"trigger: process broken"*, with D14 and the charter's Role exceptions as its reference, and gave the counter-argument: *"it adds to `CLAUDE.md`, which every seat reads"*.

**His answer** [E, same transcript, `user` message, 2026-10-04 00:29:36 UTC]:

> *"Yes"*

He did not strike either of the two lines this seat added to *Role* at D14. They stand.

**What it settles.**
- **`CLAUDE.md`, "Who's who", gains one line:** *"Two limits on the main session, whether or not `/coordinator` has been run (D15): it never acts as the Skeptic, and it never acts as the CGO on the Coordinator's own charter or annex. It commissions those seats instead."* Nothing else in `CLAUDE.md` changed.
- **"On the main session" is deliberate [J].** `CLAUDE.md` loads into every subagent, including the Skeptic and the CGO themselves. An unscoped *"never act as the Skeptic"* would be read by the Skeptic.
- **"Or annex" is not an extension.** The charter says the Operating annex *"is part of the charter"* [E, `roles/coordinator.md`, header].
- **This closes the gap D14 opened for exception (i), and for (iii) as far as the CGO and the charter go**, in the form put to him ("What D14 costs", above).

**What the question put did not cover, flagged once [I].** This seat's draft question was wider: the CGO *"(or the CSO)"* on the Coordinator's *"charter, annex, omission check or controls"* [E, `pipeline/amendment-draft-coordinator.md` §13, Revision 9]. The words put to him named only the CGO and *"its own charter"*. So, outside a `/coordinator` session, nothing yet stops the main session acting as **the CSO verifying the Annex F controls**, or as **the CGO writing the omission check (M2) or a record of the Coordinator's own conduct**. Exception (iii) covers all of these inside an invoked session. **This seat did not add them, because his yes was to the narrower words.** Whether to is one yes or no for him, and not urgent: the main session commissions those seats in practice, and the autonomy does not run outside an invoked session.

**Applied** in `CLAUDE.md` and in `pipeline/amendment-draft-coordinator.md` (Revision 10; §13, §16.5).

***The CGO line was replaced by D16 (2026-10-04, 01:50:53). The Skeptic line stands.*** *The text above is kept as decided.*

**D15 follow-up: the gap above, put to him and answered. *2026-10-04, 01:49:57.*** The main session put it at 00:48:07 UTC (same transcript, `assistant` message): *"**One small gap remains, optional and not urgent.** In ordinary sessions, nothing stops the main session acting as the CSO checking its own controls, or as the CGO writing its own omission check. … **Do you want that covered too?** Yes or no, whenever you like."* The question came from this seat's optional question to the main session (should the CSO-on-its-own-controls case, and the CGO-on-its-own-check case, also be guarded outside `/coordinator`?).

**His answer** [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/05f4422b-7df3-4f42-9596-96664b755c49.jsonl`, `user` message, 2026-10-04 00:49:57 UTC, read-only by this seat 2026-10-04]. The first sentence of his message:

> *"No, that is fine."*

**What it settles.** `CLAUDE.md` is not extended to the CSO on its own controls or the CGO on the omission check. **He then went further in the same message, and that is D16, below.** [I] Read together, the two answers leave the case where it is under D16: allowed in a fresh session, when he asks.

---

### D16 — The main session may be any seat except the Skeptic, but only in a fresh session and only when he asks. Replaces D4a and the CGO line of D15. *2026-10-04, 01:49:57 and 01:50:53.*

*Recorded by the CGO because it concerns limits on the Coordinator seat (A3). Commissioned by the main session (Coordinator); written by a Sonnet run of the CGO seat. The CTO reviews the branch before the CEO merges it.*

**His words**, the rest of the message quoted at D15's follow-up [E, same transcript, `user` message, 2026-10-04 00:49:57 UTC]:

> *"Honestly, other than the skeptic, I don't necessarily see why the main session can't be any other role but only on new sessions and only when specifically asked for"*

**The main session's reading, put back to him** (same transcript, `assistant` message, 2026-10-04 00:50:09 UTC; quoted in part):
- *"The main session may act as any seat except the Skeptic. That includes the CGO on the Coordinator's own charter, and the CSO on its own controls."*
- *"Only in a fresh session, and only when you explicitly ask for that seat. A session that has been coordinating can't switch roles partway through."*
- *"This replaces your D4a (never the CGO on its own limits), and the CGO line we just added to `CLAUDE.md` (D15). The Skeptic line stays."*
- *"Why it still works: a fresh session hasn't been in the room. So 'never reviewing its own work' is satisfied by starting fresh, rather than by banning seats."*
- Under *"What you may not want to hear"*: *"one gap the old rule closed is reopened. A fresh session acting as the CGO could loosen the Coordinator's charter. It's still only a draft: the CTO reviews it and you merge it, and its record shows which session wrote it. So the backstop is your merge."* Its view: *"No view offered."* It asked: *"Is that reading right? Yes, or correct me."*

**His answer** [E, same transcript, `user` message, 2026-10-04 00:50:53 UTC]:

> *"Correct yes"*

Both of his messages were read from his own transcript by this seat, and match the words in the commission.

**What it settles.**
- **The main session may act as any seat except the Skeptic.** That includes the CGO on the Coordinator's own charter, and the CSO on its own controls.
- **Only in a fresh session, and only when he explicitly asks for that seat.** A session that has been coordinating, or in which `/coordinator` has been run, cannot switch roles partway through.
- **D4a is replaced.** Exceptions (ii) *never reviewing its own work* and (iii) *never a seat that sets, checks or records the limits on the Coordinator* leave the charter's *Role*. Exception (i), *never the Skeptic*, stays. D4's *"for a session or for a task"* is narrowed to a fresh session: he did not say it applies mid-session, and the main session's reading, which he confirmed, says it cannot.
- **D15 is replaced in part.** The CGO line in `CLAUDE.md` goes; the Skeptic line stays, and `CLAUDE.md` now carries the fresh-session rule in one line.
- **"Never reviewing its own work" is now met by starting fresh,** not by banning seats. [I] This is the main session's reasoning, which he confirmed; `pipeline/model-selection.md` §5.4 (*"Reviewer different from author"*) is a separate rule that D16 does not touch.
- **Stated residual** (put to him in the reading above, and confirmed): a fresh session acting as the CGO could loosen the Coordinator's charter. The backstop is the CTO's review plus his merge (D8), and the provenance line, which records which session wrote the artifact (`pipeline/model-selection.md` §5.5).

**Applied** in `roles/coordinator.md` v0.8 (header; *Role*; *Commissioning*; *Invoked*), in `CLAUDE.md` ("Who's who"), and in `pipeline/amendment-draft-coordinator.md` (Revision 11; §10 item 3, §11 item 1, §13). **Not touched: Annex D.** Its approved words (precondition 3) say the autonomy *"does not run while the main thread acts as another seat"* and still read true under D16. The charter's ordering is kept: every rule still sits before Annex A, and the command's Annex A begins at about byte 19,200, inside the 19,300 limit.

*The last sentence above was wrong: correction C3, 2026-10-04. It is kept as written.*

**Two things for the CEO to strike if he did not mean them [J].**
1. *"Decline, and tell the CEO to start a new session"*, in the charter's *Role*. It is how a session that has been coordinating refuses a mid-session role switch, and his words *"only on new sessions"* require it.
2. The CVO is folded into the general rule (*"any seat except the Skeptic"*); the charter's separate *"acts as the CVO only when the CEO says so"* line is gone. D16's *"explicitly asks"* covers it, and it is no looser.

---

### D17 — The honest-broker rules sit after the compaction window, as built: they are not counted as "limits". *2026-10-04, 13:22:31 and 13:23:12.*

*Recorded by the CGO because it concerns the Coordinator's own charter (A3). Commissioned by the main session (Coordinator); written by a Sonnet run of the CGO seat. It answers the question this seat put at `pipeline/amendment-draft-coordinator.md` §16.6 ("The minimum"). **The charter is unchanged by it:** v0.9, no word re-worded, nothing regenerated.*

**The question this seat put** (draft §16.6). Every limit now fits in the first 5,000 tokens that Claude Code keeps of a skill after compaction: 4,537 tokens net [E, draft §16.6, one run, single source]. The honest-broker rules are 744 tokens. Adding them makes **about 5,281**, over 5,000, and they could not then fit without re-wording rules, which this seat would not do to make text fit. So: do they count as limits? As built they do not. They sit after the window, so compaction cuts them, not the limits. The closing marker is always cut as well (the whole command is about 9,000 tokens), so after any compaction the session stops acting without asking and asks the CEO to re-run `/coordinator` (charter *Role*).

**How it was put to him** (main session, 2026-10-04 12:22:31.952 UTC, `assistant` message) [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/05f4422b-7df3-4f42-9596-96664b755c49.jsonl`, read-only by this seat 2026-10-04]. Quoted in part. It relayed the question: *"the CGO puts it to you as a choice: are the honest-broker rules "limits" that must survive compression too?"*, and told him what he would lose: *"Compression drops those rather than the limits"* and *"Every compression will trigger a re-run."* It closed: *"**Accept the honest-broker rules sitting past the cut-off, yes or no?**"*

**The main session's view, put to him,** labelled *"trigger: asked"* (same message): *"I'd accept it as it stands [J]."* Its reason: after compression the closing line is gone, the session can't act without asking, and it asks him to re-run `/coordinator`. Its strongest counter-argument, in its words: *"a report written in that gap could soften a block."* Its confidence: *"medium-high."*

**His answer** [E, same transcript, `user` message, 2026-10-04 12:23:12.912 UTC; it matches the word in the commission]:

> *"Yes"*

**What it settles.**
- **The placement is accepted as built.** The honest-broker rules (copy blocks verbatim; *"What you may not want to hear"*; a view only on a named trigger) are not "limits" for the purposes of the compaction window. They stay after Annex F, words unchanged. Charter v0.9 stands; the command is not regenerated.
- **The cost, stated once.** After a compaction, until he re-runs `/coordinator`, those rules are not in the session's context. Re-running restores the whole charter.
- **The gap is the one the main session named, and it is real [I].** The *Role* fail-safe makes the session ask before each *step*. It does not by itself govern how a *report* is worded, and it depends on the session noticing that the closing marker is missing, which is model compliance, the same dependence C3 recorded for the fail-safe. What would catch a softened block is the omission check (M2(i): every block appears verbatim in the report). **It is not merged** [E, same transcript, main session's report, 12:22:31 UTC: *"Omission-check output: not run; the script isn't merged yet"*], so until it is, only his own tags (M1, M6) measure it. Draft §13 condition 6 (the omission check gates Decision 9) is unchanged.

**Two things this seat flags, once each. Neither is a block.**
1. **Scope of the yes [I].** What was put to him named the honest-broker rules. The same cut also takes the mandate, *Must always ask*, the universal clauses, *Placement*, *Produces*, *Invoked*, and **Annex A (the report format, including the item-3 marker) and Annex E (the measures)**, which draft §16.6 lists as "not counted" [J]. What was put to him did not name those [E, same transcript, `assistant` message, 12:22:31 UTC]. This seat reads his yes as covering what was put to him, and treats the rest as this seat's judgment [J], which merging PR #22 approves (D8). It is the same kind of loss (report quality, not extra authority), and a re-run restores it. If he wants it settled separately, it is one line from him.
2. **The label *"trigger: asked"*.** Charter honest-broker rule 3 defines *asked* as: the CEO asked for your view on this matter, in this task, with *"his words, quoted"* as the reference [E, `roles/coordinator.md`, rule 3]. The reference given was the CGO's question, not his words. None of his typed messages between 11:30 UTC and his *"Yes"* asks for a view on this matter [E, same transcript, `user` messages read in that span: 12:16:16, 12:18:59, 12:19:33, 12:19:40, 12:23:12 UTC, and two shell commands of his at 12:05]. Whether the view was triggered by another named trigger is not shown. The effect is nil here: the view was short, marked and labelled [J], and he answered *"Yes"* to the question and not to the view. But M2(iii) and M8, when built, would fail this report, which is the check working as designed. Flagged to the CEO: it concerns the Coordinator's own conduct, and no seat's block covers it.

**Applied** in `pipeline/amendment-draft-coordinator.md` (Revision 13; §13; a dated note under §16.6). No other file.

### D18 — The widget tools stay available. *2026-10-04, 13:29:45.*

*Recorded by the CGO because it concerns the Coordinator's own conditions (A3). Commissioned by the main session (Coordinator); written by a Sonnet run of the CGO seat. Times are BST, converted from the transcript's UTC timestamps.*

**What the CSO found.** The in-chat widget's `sendPrompt(text)` can send text *"as if the user typed it"*, and no click, confirmation or marking of the message as widget-sent is documented [E, `pipeline/cso-controls-results.md`, "Widget sendPrompt, 2026-10-04"; the CSO's own conclusion is [I], with likelihood low [J]]. It recommended a flag, not a block, and one deny rule, `mcp__*__show_widget`, at a cost of €0 and the loss of inline charts and diagrams in this repository's sessions [E, same section].

**The question put to him** (main session, 2026-10-04 12:28:50 UTC, `assistant` message) [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/0c6ad0a8-7bbf-41a1-854b-c438904372e6.jsonl`, read-only by this seat 2026-10-04]: *"should the CSO open the small PR to deny the chat widget in this repo? The cost is that I can't draw diagrams or charts inline here."*

**His answer** [E, same transcript, `user` message, 2026-10-04 12:29:45.971 UTC; it is the second line of a two-line message, the first being "Pushed"]:

> *"No, we want those tools to be available"*

**What it settles.**
- **No deny rule for the widget tool.** `.claude/settings.json` is not changed by it, and the CSO opens no PR for one.
- **The residual risk is accepted by him, and is stated here once.** A message sent from a widget would be treated as if he had typed it, so it could stand in for a "Yes", an approval or a `/coordinator` [I, the CSO's reading]. The CTO's re-review of #23 adds that a widget-sent message almost certainly carries `origin.kind: "human"`, so the omission check (M2) would count it as his words [E, main session's report to him, 2026-10-04 12:39:18 UTC, same transcript; the CTO's review itself is not cited by this seat]. **That is inference: no widget-sent message exists locally to check** [I]. What the controls lose is the property the CSO named, that *"the CEO's own message"* is consent; what they keep is every deny rule and the guard, which a forged "Yes" cannot defeat [E, CSO section above].
- **What would overturn it.** A vendor statement, or a test he runs in a throwaway session, showing that `sendPrompt` needs a click or marks its message as widget-sent. Then the risk narrows, and the CSO's own note applies: *"a message from a widget is not the CEO's"* in the charter would do [E, CSO section, "What would overturn this"].

**Still open: one optional rule, not answered by him.** The main session also offered a one-line charter rule: widgets never send decisions, approvals or slash commands. **He has not answered it.** It is recorded as open and **no word of it is in the charter** [J: this seat did not add it on its own reading]. It would also need room in the limits window (see D19, Applied).

**Applied.** This record only.

### D19 — A `/coordinator` session confirms that credits are off because the CEO says so, at the start of the session (option 1). *2026-10-04, 13:41:51.*

*Recorded by the CGO because it concerns the Coordinator's own charter (A3). Commissioned by the main session (Coordinator); written by a Sonnet run of the CGO seat.*

**The gap.** Annex C told the session to confirm that credits are still off *"using the check the CTO establishes (§11 of the amendment draft)"* [E, `roles/coordinator.md` v0.9, Annex C, the "Before relying on that stop" bullet]. **No such check exists** [E, main session's report, 2026-10-04 12:34:14 UTC, same transcript: *"the CTO never established one"*]. A new `/coordinator` session therefore raised it as a flag and asked before every step, which defeats the autonomy granted at D5. This is the open condition 8 below.

**The question put to him** (main session, 2026-10-04 12:34:14 UTC, `assistant` message, same transcript), two options:
1. *"You tell it at the start of each `/coordinator` session, for example "credits are off"."*
2. *"Ask the CTO to find a check the session can run itself, if the Desktop or account exposes one."*

The main session's own suggestion was *"1 now, and the CTO looking into 2 at no rush"* [E, same message; its label as a view is not checked here].

**His answer** [E, same transcript, `user` message, 2026-10-04 12:40:51.393 UTC]:

> *"option 1"*

**What it settles.**
- **His word is the check.** At the start of a `/coordinator` session, the session asks him to confirm that credits are off, unless he has already said so in that session. Until he confirms, it treats the setting as unknown and asks before each step.
- **Credits remain off by D0.2.** This changes how a session confirms it, not the setting. Turning credits on is still his decision alone (5.4).
- **What it costs, stated once.** One sentence from him at the start of each session, and, after a compaction, one more with the re-run of `/coordinator` (the charter is then re-read in full). Without it, every step waits for his yes.
- **The limit of the check [I].** It is his statement of a setting, not a reading of the account. If the setting were changed without his remembering, the session would not see it. Option 2 (the CTO looking for a self-check) was not chosen; **it was not researched, and this seat does not know whether such a check exists.** Condition 8 is closed as to the method, and nothing stops him asking for option 2 later.

**Applied.**
- **Charter v0.10, Annex C**, the "Before relying on that stop" bullet: *"confirm that credits are still off"*; his own word in the session is the confirmation (D19); at the start of a `/coordinator` session, ask him to confirm credits are off, unless he has already said so in that session; until he confirms, treat the setting as unknown and ask before each step; if a usage-limit or billing message suggests otherwise, treat it as unknown again. **The reference to "the check the CTO establishes" is removed.** The last two sentences of the bullet (Fable unavailable while credits are off; turning credits on is the CEO's alone) are unchanged. The charter's earlier trigger, "whenever a usage-limit or billing message appears", is kept in the narrower form just quoted [J]: this seat kept it rather than drop a check the CEO did not ask to drop. Annex D's text is untouched.
- **The command regenerated** from the charter (`scripts/build-coordinator-command.py`). The limits end at **byte 12,491 of the 12,500-byte ceiling**: 9 bytes of headroom [E, measured on the generated command; the test `test_every_limit_fits_in_the_compaction_window` passes]. **Any further limit added to Annex C to F will not fit without moving or trimming something,** including the optional widget rule under D18. Do not raise the ceiling (the test says so); re-measure the window first (draft §16.6).
- **Not updated, flagged:** `pipeline/amendment-draft-coordinator.md` §11 item 24 (the CTO's credit-check task) and its §16 still describe the CTO establishing a check [I; not read in full by this seat for this commission]. They need a one-line note that D19 supersedes them. *(Done, 2026-10-04: commit `30b3b51`. See C4.)*

**This is a charter change, so merging the PR is what adopts it (D8).** It is one line of Annex C, not Annex D, so precondition 3 is not engaged [I].

---

## CGO flags on D11 and D12

Each is a **flag, not a block**. This is not a gate. Each is put once.

1. **Whether the autonomy operates before the amendment is applied is a question of what a clause means, and it is the CEO's.** The charter's header says it is *"Not yet in force"* and that until Decision 9 *"the main session works under `CLAUDE.md`"* [E, `roles/coordinator.md`, header]. Annex D's preconditions do not include the amendment, and all four are now recorded. The main session told the CEO at 00:43:20: *"From here, I start the next written step myself and tell you afterwards."* He did not object. **This seat's reading [J]:** D5 is a 5.4 grant that stands on its own, and the header describes the seat's constitutional status rather than suspending D5. **But the two texts point different ways, and the seat that benefits should not settle it.** One line from him settles it.
   *(2026-10-04: settled by the CEO at D13: option (a), the charter is in force now.)*
2. **D11's script must follow the annex when it moves.** The Operating annex is part of the charter and moves to `pipeline/coordinator-operating.md` when the amendment is applied (charter header). The script and the CI check should cover both files from the start, or the annex silently drops out of the output style at Decision 9 [I]. *(2026-10-04: the output style is now the `/coordinator` command (D14), generated by `scripts/build-coordinator-command.py`, which still reads `roles/coordinator.md` only. A tripwire test now fails the day `pipeline/coordinator-operating.md` appears and the command does not contain it [E, `scripts/build-coordinator-command-test.py`]. The flag stays open until the generator follows the move. When it does, it should keep the limits first; draft §16.5.)*
3. **The `agent` setting is a stronger binding, not a proven cure for editorialising.** It replaces the default instructions with the charter. That makes the charter more prominent, but nothing this seat has read shows it reduces unprompted views [I, low confidence; not researched]. If M8 shows D12 failing, the next step should be put to him with that uncertainty stated, and with option 3 of D12 (a pure relay) beside it.
4. **The restart rule was restated more narrowly to the CEO than the CSO recorded it.** The main session told him at 00:38:22 that the restart is needed *"after any change to `.claude/settings.json`"*, not after a guard-file change. The CSO's operating rule is *"after any change to `.claude/` on disk, by hand or by a pull, restart the session"* [E, `pipeline/cso-controls-results.md`, "V9(iv) limit"]. The main session's reasoning may be right for the guard script. **The CSO's rule stands until the CSO narrows it.** Owner: the CSO. *(2026-10-04: closed. The main session corrected the narrowing at 00:53:51, and the CSO's broader rule is restored; see D13.)*

---

## Written response to the dissent memo

### The CEO's response (Constitution 1.6; 5.3)

> *"Okay, I understand the concerns but it is mainly meant to streamline and improve the efficiency so each agent can work at their best and focus purely on the task at hand. I am fine with it being the main thread but only if it is best practice"*

He did not add to it.

**Whether it is an answer or an acknowledgement.** The CGO's charter asks: *"Has the dissent been answered in writing, or merely acknowledged?"* [E, `roles/cgo.md` line 19]. This seat's judgment [J]: **it is an answer to the question he decided.** That question was whether the seat should exist, and he gave the reason it should. The memo's own verdict on that question is that *"I looked for a case that the seat should not exist, and none survives"* [E, memo, Verdict].

**What it does not engage.** The memo's residual on trust: *"Chartering an intermediary makes the principal trust it more"* (memo, the case against, item 5; S5). That residual is carried by the design, not by his response. The amendment is not applied until the omission check (M2) exists and has run (draft §5, §9). 5.3 does not strictly bind here, because this is not a gate (memo, header). Constitution 1.6 is satisfied: *"No significant decision proceeds without a documented counter-argument"* [E, `constitution.md` line 38].

### Point by point

**The CEO did not answer each objection, and this record does not write answers for him.** The point-by-point response is the CGO's, at draft §15. The CEO's part is the decisions that carry those responses out, which are listed beside each one.

| Memo item | CGO response (draft §15) | CEO decision that carries it out | Status |
|---|---|---|---|
| **S1** Decision 0 on an incomplete fact | Accepted; the error is recorded (below) | **D0.1** (the change was his); **D1** (redrafted from the live ruleset); his merges of #15 and #16 | **Dissolved** on all three of the memo's conditions |
| **S2** Autonomy authorised by files the seat writes | Accepted; the allowlist on `main`; the CEO's own words; QA placement to a process file; M2 checks citations | **D5** (Annex D's exact text, granted) and **Decision 6** (QA placement, owed) | **Open** until Decision 6 and M2 (§11 item 18) |
| **S3** Money has no structural control | Accepted; largely overtaken | **D0.2** (credits off); precondition 1 of Annex D | **Dissolved** on the memo's terms. The check method is still owed (CTO, §11 item 24) *(Settled by D19: the CEO's word at session start; see conditions, row 8.)* |
| **S4** The Article 6 line contradicts the charter | Accepted; *"decides no matter reserved to the CEO"* | Applied at **Decision 9** | **Dissolved in text** |
| **S5** The check on the main risk does not exist | Accepted, going further; the whole amendment waits for M2 | **Decision 9** is conditional on it | **Open**: M2 is not built |
| **S6** The name rests on a partial reading | Accepted; recommendation changed | **D3** ("Coordinator") | **Dissolved** |
| **F1** "One-page charter" | Partly accepted; the annex splits off on application | **D4** (the charter adopted, with the CGO's reading) [I] | **Closed** unless the CEO reads it otherwise |
| **F2** Case (b) as authority | Accepted; the seat's own recommendation only | **D5** | **Closed in text** by D5 |
| **F3** Who defers a finding | Accepted; only the reviewing seat | **D5**; §11 item 10 | **Closed in text** by D5; §11 item 10 **open** |
| **F4** Evidence defects in the brief | Accepted as a flag | none needed | **Open**: Research Analyst, §11 item 26 |
| **F5** Article 3 and publication order | Accepted | none yet | **Open and held** (CSO review R5) |
| **F6** Autonomy on a paraphrase of a relay | Accepted | His words are now checked against his transcript (above); **D5** | **Open** only for publication of the verbatim commissions (§11 item 27). D5 approved the exact text, which he had linked; the summary he was given differed in one place (D5, above) |
| Steering (a): path choice | Accepted; the path list includes every cited file | none needed | **Open**: §11 item 16 |
| Steering (b): model choice | Noted | none needed | Disclosed; Fable unavailable while credits are off |
| "Abandon in six months" | Accepted as residuals, with owners | none needed | CSO re-verifies at each phase review (§11 item 25) |

---

## Conditions attached

| # | Condition | Owner | Due / gates what |
| - | --------- | ----- | ---------------- |
| 1 | ~~**Decision 4a**: yes or no to exception (iii)~~ **Met: D4a, 23:56:46** | CEO | In force now |
| 2 | ~~**Decision 5**: Annex D's exact text, in his own words, including the two Revision 4 proposals~~ **Met: D5, 23:55:58** | CEO | The autonomy still waits on condition 3 (precondition 4) |
| 3 | *(Met, 2026-10-04: the CSO's sign-off, S1. Kept as it was:)* **The CSO's outstanding checks:** V2 (the full deny list; `claude auto-mode config`); V3(a) and V3(b); V9(iv) by the revised method; V7, V8 and V9(i) re-run after PR #16; V13 and the V6 checkout sentinel (with the CEO's prior approval); V10 in the Desktop | CSO; CEO by hand where the review says so (R7) | **Gates publication (R5)**, and **gates the autonomy**: Annex D precondition 4, adopted at D5 |
| 4 | **The Desktop bypass toggle is off, and the mode selector does not offer Bypass** | CEO, by hand | Completes D1; **gates publication (R5)** |
| 5 | **One redaction:** connector providers named in `pipeline/cso-controls-results.md` become kinds (email, file storage, calendar) | CSO, as author of that file's review | **Gates publication (R5)** |
| 6 | **The M2 omission check and template markers** exist, and have run before a decision request | CGO (spec, owner), Engineer (script) | **Gates Decision 9** (the amendment) |
| 7 | **Publication** of this record with the draft, the memo, the brief and the CSO files | CGO, once the CSO clears it | **Due 2026-11-01** [J, the CGO's commitment]. If still held on 2026-10-25, the date goes to the CEO |
| 8 | ~~**The usage-credit check method** (how the seat confirms credits are still off)~~ **Settled by D19 (2026-10-04, 13:40:51):** the CEO states it at the start of each `/coordinator` session; no CTO check is needed | ~~CTO (§11 item 24)~~ CEO | ~~Before Annex D relies on the stop at a usage limit~~ In force: charter v0.10 is merged (PR #24) |
| 9 | **The verbatim commissions** for this amendment are published with this record | Main session (§11 item 27) | With condition 7 |

**On the next Desktop update past 2.1.286**, the CSO re-runs V1–V9 and V13 (CSO review R2, R7 step 8). That is standing, not a condition of these decisions.

---

## Overrules exercised

**None.** No block was raised. The CGO's draft records *"Blocks: none. This is not a gate"* [E, draft §12]. The CSO's findings are flags: *"Each is a **flag, not a block**. My block covers release only"* [E, CSO review R4].

---

## Errors made in reaching these decisions

Recorded here because they shaped what the CEO was told. Each has the original words, who made the error, who caught it, and its effect.

**E1. "`main` is unprotected."**
- **The claim.** The CGO's draft, Revision 2, §8: *"`main` is **not protected**"*. The main session repeated it to the CEO (draft §8, §15 S1).
- **The error.** **The CGO and the main session both checked only GitHub's classic branch-protection endpoint**, which does not report rulesets. A ruleset, "Main" (id 23570113), had applied to the default branch since **2026-09-17** [E, draft §8, re-verified at the API].
- **Caught by:** the Skeptic (memo S1). Not by either seat that made it.
- **Effect.** Decision 0 was drafted on a wrong fact, and was redrafted as Decision 1 from the live ruleset. The same defect class, one mechanism of two read and reported as both, is already on record from the amortisation verification.

**E2. "Subagents cannot start subagents."**
- **The claim.** The main session's first reply to the CEO, 14:45:32: *"**It can't be a subagent.** In Claude Code, subagents can't start other subagents, so an orchestrator built as a subagent couldn't commission anyone."*
- **The error.** By default, a subagent can start subagents of its own, *"up to three layers below the main conversation"* [E, https://code.claude.com/docs/en/sub-agents.md line 1014, re-retrieved by this seat 2026-10-02]. The vendor's version note says nesting was off by default only in v2.1.217–2.1.218 [E, same, lines 1037–1038]. Where the claim came from is not known.
- **Caught by:** the Research Analyst. The brief's table answers *"Can a subagent start other subagents?"* with *"**Yes.**"* [E, brief §4.1].
- **Effect.** It framed the placement as forced rather than chosen. **D2 does not rest on it** [I]: the answer the CEO accepted relies on the filter argument (brief §4.6), which assumes nesting exists.

**E3 (minor). A misquotation in the D4 proposal.**
- **The claim.** The main session told the CEO that *"the charter says the main thread is the Coordinator 'unless the CEO says that session is doing something else'"*.
- **The error.** The charter v0.2 said *"unless the CEO says otherwise"* [E, `roles/chief-of-staff.md` v0.2, *Invoked*, read 2026-10-02 before the rename]. The quoted words are not in it.
- **Caught by:** this seat, while compiling this record.
- **Effect.** None on substance; the meaning is close. It is recorded because quotation marks are a promise of exact words, and this seat runs the honest-broker rule *"Copy, never paraphrase"*.

**O1 (this seat's judgment, not an error of fact).** The best-practice headline at D2, discussed under D2 above.

**Related, recorded elsewhere and not repeated.** The CSO found that "2.1.283" in the brief, the memo and its own advice was the terminal CLI's version. The Desktop checks ran on 2.1.286 [E, CSO review R2].

---

## Corrections

A correction to this record preserves the original text verbatim, names the error, attributes it, and is dated.

**C1, 2026-10-04 (CGO). D6, "What it settles": "Applied to charter Annex D."**
- **The original text,** first bullet, last two sentences: *"Applied to charter Annex D. **The order of the CTO's review and pre-merge QA was not decided**; it is for the PM/BA's process file [I]."* It stays in place, unedited.
- **The error.** D6 was not applied to the charter. Annex D still reads *"Then QA. … Where QA sits relative to the merge is his decision; until he makes it, QA follows his merge"* [E, `roles/coordinator.md` v0.4 and v0.5, Annex D]. D6 was written into `pipeline/agentic-agile.md`, "The per-ticket chain", which is on `main`.
- **Attributed to:** this seat, which compiled D6. Found by this seat while trimming the charter to v0.5.
- **Effect [I, high confidence]:** none on what governs. Annex D's chain applies only *"until a process file says otherwise"*, and the process file now does. A reader of the charter alone is told the old order.
- **Not fixed in the charter at first,** because Annex D's words are the text the CEO approved at D5 (precondition 3). The fix needed one yes or no from him to a new Annex D text: `pipeline/amendment-draft-coordinator.md` §16.3, flag 1.
- **The CEO's answer: yes. 2026-10-04, 01:14:57.** The question put (main session, 00:11:54 UTC): *"May the CGO update that one line of Annex D to match D6? It changes your approved text only to bring it into line with your later decision."* His answer, the first line of his message: *"1. Yes"* [E, `~/.claude/projects/-Users-davidparrish-Documents-candour/2e1bef0c-52b9-4bac-891a-50b1ab827978.jsonl`, `user` message, 2026-10-04 00:14:57 UTC, read-only by this seat 2026-10-04; it matches the main session's relay].
- **Applied** in charter v0.5, Annex D, "The per-ticket chain": full QA on the branch before the PR; the CEO merges every PR (D8); the integration check once per wave; QA moves the ticket to Done only after it (D6); a split requirement checked per PR and confirmed at the integration check after its last story merges (D9). **Precondition 3 now covers Annex D's text as amended by this yes** [I, high confidence]. No other word of Annex D changed.

**C2, 2026-10-04 (CGO). C1's application of D6 to Annex D: "then a PR".**
- **The original text,** Annex D v0.5, "The per-ticket chain": *"Ticket complete, then the CTO's review (and the CSO's where the ticket is labelled `needs:cso-review`) and **full QA on the branch** against the ticket's acceptance criteria, then a PR."*
- **The error.** `pipeline/agentic-agile.md` opens the PR at step 1, when the Engineer completes the ticket, and records the review and QA in it (steps 2–3) [E, `pipeline/agentic-agile.md`, "The per-ticket chain", lines 48–50]. This seat's v0.5 text put the PR after both. It was carried over from the earlier wording.
- **Found by:** the CTO, in its review of PR #22 (flag 2), as relayed by the main session to the CEO at 00:22:49 UTC [E, transcript `05f4422b-….jsonl`, assistant message]. Not by this seat.
- **Fixed in v0.6:** *"Ticket complete and its PR opened, then the CTO's review (…) and **full QA on the branch** against the ticket's acceptance criteria, each recorded in the PR."* No other word changed.
- **Why without a new question to the CEO [J]:** his C1 yes was to update Annex D *"to match D6"*, and the process file is D6 written out and on `main`. D6's own words (*"the PR comes to the CEO"*) fit a PR opened earlier. **But this changes Annex D's approved text (precondition 3), so merging the PR is what approves it**, as the CTO said of #22. If he wants it put to him separately, it is one yes or no.

**C3, 2026-10-04 (CGO). D16, "Applied": "inside the 19,300 limit"; and the estimate behind it in draft §16.5.**
- **The original text,** D16's "Applied" paragraph, last sentence: *"The charter's ordering is kept: every rule still sits before Annex A, and the command's Annex A begins at about byte 19,200, inside the 19,300 limit."* The same figure is in the draft's Revision 11: *"the command's Annex A begins at about byte 19,200, and every rule sits before it"*. Both rest on draft §16.5 (Revision 10, made at D15): *"The Engineer estimates the charter at about 5,500–6,200 tokens … On that estimate, 5,000 tokens is about 18,750–21,000 bytes"*, and its residual, which assumed *"3.75 bytes a token"* at the low end. All three stay in place, unedited.
- **The error.** There was no 19,300-byte limit. The figure came from an estimate this seat recorded as unverified (*"this seat has no tokenizer and did not verify it"*, §16.5) and then relied on as if it were measured. Measured, the command runs at about 2.7 to 3.0 bytes a token: the CTO put bytes 0 to 19,199 at **about 6,400 to 6,950 tokens** [E, CTO review of #22 at `b87501a`, F1, retrieved 2026-10-04 with `gh api repos/deopea-david/candour/pulls/22/reviews`], and this seat measured 2.74 on the v0.9 command [E, draft §16.6]. So the 5,000-token window ended at about byte 13,700 to 15,000, inside Annex D. **"Every rule sits before" the cut was false:** Annex D's per-ticket chain, *Always comes to the CEO*, the caps and *Out of scope*, and all of Annex F, were past it.
- **Attributed to:** this seat. §16.5 was written by an Opus run of the CGO; the D16 entry and Revision 11 by a Sonnet run of the CGO, which carried §16.5's estimate forward. The underlying estimate was the Engineer's, relayed by the main session; using it unverified was this seat's error.
- **Found by:** the CTO, in its review of PR #22 at `b87501a` (F1). Not by this seat.
- **Effect [I, high confidence].** None in practice: the charter was not yet merged. Had it been, a compacted Coordinator session would have kept the grant of autonomy and lost its caps and Annex F, and the *Role* fail-safe would have worked only if the session noticed the cut.
- **Fixed in charter v0.9** (draft Revision 12, §16.6): every limit now sits inside the window, measured at 4,537 tokens net (4,647 at the upper reading); the charter ends with a closing marker that *Role* tells the session to check for; and a test holds the limits to the first 12,500 bytes and the marker to the last line. **No rule's words changed; Annex D's approved text is byte-identical.**

**C4, 2026-10-04 (CGO). D19: its time, three stale lines, and a broken table row.**
- **The original text,** all kept above in place unless noted: (1) D19's heading time *"13:41:51"* and the same time in conditions row 8; (2) D19, *Applied*, last bullet: *"Not updated, flagged: … They need a one-line note that D19 supersedes them."*; (3) the written-response table, row S3: *"The check method is still owed (CTO, §11 item 24)"*; (4) conditions row 8, which said the charter change was *"awaiting his merge"* and whose strikethrough ran across table cells, so the row showed six cells in a four-column table.
- **The errors.** (1) The CEO's *"option 1"* is stamped 12:40:51.393 UTC in the transcript the entry cites, which is **13:40:51 BST**, not 13:41:51: one minute out. The heading and row 8 keep the original text; this correction is the right time. (2) The note was made in commit `30b3b51` (`pipeline/amendment-draft-coordinator.md`, §11 item 24 and §16). (3) D19 settled the method, so S3's *"still owed"* was no longer true. (4) Charter v0.10 is merged (PR #24), so *"awaiting his merge"* was no longer true.
- **Attributed to:** the CGO run that wrote D19, for (1) and the table row; (2)–(4) went stale when the later commit and PR #24 landed, which that run could not have known.
- **Found by:** the main session's memory note listing these as owed to the CGO's next pass, and this seat's consistency sweep (`pipeline/consistency-sweep-2026-10-04.md`).
- **Effect [I]:** none on any decision. D19's content, the CEO's words and the charter are unchanged.
- **Row 8 as it stood, verbatim:** `` | 8 | ~~**The usage-credit check method** (how the seat confirms credits are still off) | CTO (§11 item 24) | Before Annex D relies on the stop at a usage limit~~ **Settled by D19 (2026-10-04, 13:41:51):** the CEO states it at the start of each `/coordinator` session; no CTO check is needed. Applied in charter v0.10, awaiting his merge | CEO | In force on merge | ``
- **Fixed in place:** the row 8 table cells only (the same words, split into the right cells, with the stale *"awaiting his merge"* replaced by *"merged (PR #24)"*), and short dated italic notes beside (2) and (3).

**This seat prepares and flags; it does not certify.** Every decision above is the CEO's (Constitution 5.4; Article 11.1).
