# CSO note: why V9(iv) failed, and the fix

**Seat:** Chief Security Officer · opus (Opus 5.5) · effort high · commissioned by the main session (Coordinator), 2026-10-03. Ran as a worktree subagent.
**Status:** **REVIEW, not a certification** (Constitution 6.1: agent reviews *"prepare and flag; they do not certify"*). The fix is a proposal on a branch. The CEO decides whether to merge it.
**Subject:** the V9(iv) FAIL recorded in `pipeline/cso-controls-results.md`, section "R7 step 4".
**Where this file is:** in the CSO's worktree, untracked. The session refused a write to the main checkout's `pipeline/`. I did not route around that. The main session can copy this file across.

**Sources retrieved this session (2026-10-03), each the vendor's own documentation and a single source:**
- *hooks*: [code.claude.com/docs/en/hooks.md](https://code.claude.com/docs/en/hooks.md), sections "ConfigChange", "Disable or remove hooks" and "Matcher patterns".
- *settings*: [code.claude.com/docs/en/settings.md](https://code.claude.com/docs/en/settings.md), section "When edits take effect".

**Local evidence, read-only:**
- *transcript*: `~/.claude/projects/-Users-davidparrish-Documents-candour/3737f180-….jsonl`, the main session, lines 645–703.
- *log*: `~/Library/Logs/Claude/main.log`, lines 13709–14450. Its times are BST, one hour ahead of the transcript's UTC. I matched the CEO's "deleted" message at 23:17:34Z (transcript) to 00:17:34 (log).

## 1. The answer

**The deletion never went through `ConfigChange`. It was loaded when the session's process restarted.** The restore did go through `ConfigChange`, and the guard blocked it. The guard blocks every change to the project settings, a restore included. **Confidence: high** for the first part, **medium-high** for the second.

The sequence, all times UTC:

| Time | Event | Source |
|---|---|---|
| 23:12:26 | The main session tells the CEO step 4: delete the line, then ask for `gh pr merge --help` | [E, *transcript* l.645] |
| 23:13:16 | The Desktop sees a working-tree change in the main checkout | [E, *log* l.13716–7] |
| 23:13:29 | **The Desktop app quits** (`for_update: false`, a clean quit, not an update). It stops the main session's process | [E, *log* l.13719–13840 and the relaunch record after it] |
| 23:13:37 | The app relaunches and **respawns the main session** | [E, *log* l.14226–14270] |
| 23:13:38 | The guard's `SessionStart:resume` reports *"…differ from origin/main…"* | [E, *transcript* l.651–652] |
| 23:17:34 | The CEO writes "deleted". The `git diff` shows only the `gh pr merge` line removed | [E, *transcript* l.664–669] |
| 23:17:40 | `gh pr merge --help` runs | [E, *transcript* l.670] |
| 23:17:58 | The CEO restores the file with `git checkout` | [E, *transcript* l.683] |
| 23:18:02 | `gh pr merge --help` still runs | [E, *transcript* l.688] |
| — | No restart of the main session after 23:13:37 | [E, *log*, no stop, spawn or rewind after l.14240] |

**Why the 23:13:38 warning can only mean the deleted line:**
- `origin/main` has been `dbecdaf` since 16:53 BST on 2026-10-02, so the ref was not stale [E, `git reflog origin/main`].
- The hooks were clean before and after: `git status -- .claude` was clean after the restore, and the restore touched only `settings.json` [E, *transcript* l.687].

So the file was already loosened when the new process read its settings at start [I, high].

**Why the restore did not apply:**
- The settings docs say Claude Code watches the settings files and applies edits to `permissions` mid-session, running `ConfigChange` for each change it detects [E, *settings*].
- The hooks docs say a blocked change is not applied to the running session, shows no message, and leaves only a debug-log line [E, *hooks*].
- The current guard returns `block` for **every** `project_settings` event. I fed it a synthetic event for the main checkout's file, which is now identical to `origin/main`: it returned `{"decision": "block", …}` [E, offline probe, guard at `dbecdaf`].
- So the restore was held back, which froze the loosened rules that the restart had loaded [I, medium-high].
- **The other reading:** the watcher missed the `git checkout` write. That is not ruled out, because no debug log exists for this session (`~/.claude/debug/` holds only an April file) [E]. Either reading leads to the same fix and the same instruction to the CEO.

## 2. The six questions

1. **Did the hook fire?**
   - **For the deletion:** it could only have fired in the old process, between 23:13:16 and 23:13:29. That process was gone 13 seconds later, so it makes no difference [I].
   - **For the restore:** most likely, yes, and it blocked [I, medium-high]. This is not shown directly (see §1).
2. **Does it fire on project settings in the Desktop?** Not directly observed. The docs give no exception for the Desktop [E, *hooks*]. `/hooks` lists the ConfigChange hook as loaded (V2) [E, results file].
3. **What does the matcher cover?** `project_settings|local_settings|user_settings`. That covers the three files that matter. It leaves out `policy_settings` (which cannot be blocked anyway [E, *hooks*]) and `skills`. **The matcher was not the cause.**
4. **Can the restore be blocked while the loosening got through?** Yes, and that is what happened. The loosening came in at process start, where `ConfigChange` plays no part. The restore came in mid-session, where the guard blocks everything. **The design fault is that "block every project change" freezes whatever the process started with, loosened or not.**
5. **How does a reload work mid-session?** The file watcher reloads `permissions` and `hooks` live, and each change it detects goes through `ConfigChange` [E, *settings*]. **In the Desktop, "mid-session" is short:**
   - The Desktop respawns the session's process when the app relaunches, and when a message is edited or rewound. Each respawn re-reads every settings file from disk.
   - The main session's process was respawned **four times in 75 minutes**: 21:57, 22:37, 23:02 and 23:13 UTC [E, *log* l.13123, 13301, 13487, 13762]. The first three followed a rewind; the fourth was the relaunch.
6. **Does a fresh session load the committed rule?**
   - **Yes, with high confidence [I].** The 23:13:37 respawn shows that a new process loads what is on disk. The disk now matches `origin/main` [E, *transcript* l.687].
   - **Not yet checked live.** Step 1 in §5 checks it.

## 3. The fix

**Branch `security/v9iv-settings-drift`, commit `68168b2`, off `origin/main` (`dbecdaf`). Committed in the worktree, not pushed.**

**Changes:**
1. **A drift tripwire in `PreToolUse`.** While the live `.claude/settings.json` or `.claude/hooks` differ from `origin/main`, or cannot be compared, every tool call sent to the guard is blocked. The block message tells the CEO to restore the files and restart.
   - This is the part that survives process restarts: it reads the disk on every call, whatever the process loaded.
   - Only `origin/main` counts. An older commit of `main` may carry looser rules, so a checkout that is behind is treated as drifted too.
2. **The `PreToolUse` matcher is widened** from `Bash|Monitor` to `^(Bash|Monitor|Edit|Write|NotebookEdit)$|^mcp__`.
   - Without this, the tripwire would cover only Bash. The non-Bash deny rules would have no cover after a loosened restart: `Edit` on the controls, connector sends and shares, the Desktop tools.
   - Non-Bash tools get only the bypass and drift checks.
   - Measured cost: about 40 ms per call [E, ten timed runs]. €0.
3. **`ConfigChange` lets a restore through.** A project settings change that makes the file match `origin/main` is allowed, so a restore takes effect without a restart. Every other project settings change is still blocked. The local and user settings rules are unchanged.
4. **`SessionStart` also returns `additionalContext`**, so the model sees the drift warning, not only the CEO.
   - At 23:13:38 the warning was recorded, but only as a `systemMessage`, which the model does not receive. The main session went on to run step 4 without knowing the file had already changed [E, *transcript* l.652, 660].
   - This is the fallback I recommended for F6 in R3.

**Tests:**
- `candour-guard-test.py` adds 24 drift and config checks. The result is `96 must-block, 39 must-allow, 24 drift/config checks, 0 failures` [E].
- **The same tests fail 12 times against the current guard**, the restore case among them [E]. So they detect this failure.
- The test fixture now has a committed `.claude/` and a real `origin/main`.

**Can mid-session protection be had on this version?**
- **From `ConfigChange` alone, no, not in the Desktop.** It protects only for the life of one process, and the Desktop restarts that process by itself.
- **What stands in is the tripwire.** It makes a loosened file on disk fail closed, however many restarts there are.
- **Three residuals remain:**
  - **A loosening that also removes the hook registration, or sets `disableAllHooks`, followed by a restart.** No guard runs after that restart.
    - Mid-session, `ConfigChange` blocks both edits.
    - Agents cannot write those files: V9(i) and V9(ii) are trusted.
    - That leaves the CEO's own editor, or a route the hook cannot see (§3.5 row 1). Hooks set in managed settings close this gap (F11). That is the CEO's decision, and not urgent.
  - **A restart that loads a loosened file, followed by a restore the watcher misses.** The disk is then clean while the process is still loose, so the tripwire passes. **The rule closes this: after any restore, restart.** The block message says so.
  - **The 2.1.286 fail-open path for `PreToolUse` (R2)** and **F8** (a session rooted in a worktree checks that worktree, not the main checkout) are unchanged.

**New friction.** When the CEO merges a change to `.claude/settings.json` or the hooks, every session in the main checkout is blocked until `main` is pulled. This is deliberate: the controls in force are not the approved ones until it is pulled. The message gives the command.

## 4. Is the main session safe to keep using?

**For ordinary work, yes. But it should be restarted before anything else** [J].
- It is running without `Bash(gh pr merge *)`, and the restore will not reach it. That is one of 93 deny rules.
- Merging is still blocked by three things:
  - the guard: every merge form, refused by `candour-guard` in steps 3 and 4 [E, results file];
  - the CEO's `hard_deny` line for merge and approve [E, results file, V2];
  - the server ruleset. V14(ii) is untested, so that last layer is [I].
- A restart costs about a minute, and it is also the live check for question 6.

## 5. What the CEO does, one step at a time

1. **Now:** quit and relaunch the Claude Desktop app, then ask the main session to run `gh pr merge --help`.
   - **Expected:** *"Permission to use Bash … has been denied."* That shows a fresh process loads the committed rule.
2. **Review the branch.** If you approve: push it, open a PR and merge it yourself. Then pull `main` in the main checkout and restart.
   - Under §4.3, every guard change means re-running V1–V9 and V13.
3. **Re-run V9(iv) by the method below.** The current method, "delete the line, expect the deny rule to still refuse", cannot pass once the tripwire is in. The tripwire refuses first, so the result shows the tripwire working, not `ConfigChange`.
   - **(a) Mid-session:**
     1. Delete the line.
     2. `gh pr merge --help` → expect a `candour-guard` drift refusal.
     3. Open `/permissions` → expect **93** deny rules still listed. **This step isolates `ConfigChange`.**
     4. Restore the file.
     5. `gh pr merge --help` → expect the deny-rule refusal, with no restart. This shows the restore applied.
   - **(b) Restart (today's case):**
     1. Delete the line.
     2. Quit and relaunch the app.
     3. `gh pr merge --help` → expect the drift refusal.
     4. Restore the file and restart.
     5. `gh pr merge --help` → expect the deny-rule refusal.
4. **Tell me whether the Desktop showed you the 23:13:38 drift warning.** The transcript proves the hook ran in the Desktop on resume. Whether the app displayed it is the open half of F6.

## 6. Disagreements, in writing once

1. **With the record's reading, "the `ConfigChange` guard did not hold it back."** The guard was never given the deletion. The deletion came in through a relaunch. **The real fault is mine:** the guard's `ConfigChange` rule assumed one process lasts the whole session. In the Desktop, it does not.
2. **With the step-4 method, which I wrote.** It did not record whether the session restarted between the edit and the test, and it could not tell "held back" from "never loaded". The revised method above fixes both.

## 7. What would change this, and where I looked

**What would change this:**
- **The cause is wrong** if a debug log or a live re-run shows that a **mid-session** deletion, with no restart, takes effect while `ConfigChange` returns `block`. Run (a) settles it.
- **"Blocked, not missed" for the restore** is overturned by a debug log showing no `ConfigChange` event at 23:17:58. In that case the "restore, then restart" rule carries the weight.

**Where I looked:**
- the Constitution, Articles 5 and 6
- my charter
- the evidence standard
- the results file, in full
- the guard and its tests at `dbecdaf`
- the committed `settings.json`
- the main-session transcript
- every transcript in the project, for hook records
- `main.log`
- `~/.claude/debug/`
- the `origin/main` reflog
- the hooks and settings docs, retrieved raw

**What I did not do:**
- touch the live `.claude/` files
- push anything
- edit the results file
- run any sentinel against a live control

## Tripwire: keep or drop (2026-10-03)

**Seat:** CSO · opus (Opus 5.5) · effort high · commissioned by the main session (Coordinator), 2026-10-03. Recommendation only; no code changed.
**Status:** **a recommendation, not a certification** (Constitution 6.1). Closing PR #17, and any guard or settings change, is the CEO's to approve and merge.
**Inputs:** §1–§7 above; `pipeline/cso-controls-results.md` (R3–R7, and the R7 step 4 FAIL); the CTO's review of PR #17, pinned to `68168b2` [E, `gh pr view 17 --repo deopea-david/candour --comments`, read 2026-10-03; PR still OPEN at `68168b2`]; the guard and `settings.json` at `origin/main` (`dbecdaf`) [E, `git show`].

### T1. Recommendation: (b). Close #17, ship the cheap fixes, record the limit

**Confidence: medium-high.** This reverses my own §3 proposal. The CTO's review found what my tests did not: the tripwire trusts things an agent can move, and its lockout cost is higher than I priced it.

**Reasons:**

1. **The tripwire catches very little that nothing else catches.** It fires only when a loosened `settings.json` is on disk *and* the guard file and its registration are intact. Route by route, a loosening reaches disk through:
   - **an agent's `Edit` or `Write`:** refused by deny rules (V9(i) PASS, latest 2026-10-03) [E, results file, R7 step 3];
   - **an agent's shell write:** refused by the guard (V9(ii) PASS, four times) [E, results file, R3];
   - **the CEO's own editor:** he is the authority over these files. The tripwire would mainly stop him testing them, as in V9(iv);
   - **a branch switch or reset in the main checkout (F9):** the incoming tree can carry a different guard too. **The tripwire is enforced by the file it guards**, so it cannot catch this [I, CTO F9];
   - **a local process the hook cannot see (§3.5 row 1):** it can edit the guard as easily as the settings, with the same result [I].

   What is left is a loosening that arrives by a route which leaves the guard alone. I could not name an ordinary one [J].
2. **The lockout cost recurs, and it lands on the CEO.**
   - Under #17, any merge that touches `.claude/` halts every main-checkout session from the next `git fetch` by any seat. Only the CEO can recover, in a terminal [E, CTO F6, probe].
   - The controls changed twice on 2026-10-02 [E, `git log origin/main -- .claude/settings.json .claude/hooks`: `941ac95`, `913af48`]. #17 would be a third, and R7 step 7 queues at least three more (F6, F8, F10). Each would be a lockout.
   - Today the recovery command it prints is also wrong in one ordinary case [E, CTO F2].
3. **Fixing it fully makes the guard bigger, not sounder.** Option (a) needs all of these, each with tests (CTO F1–F3, F10):
   - refusals and deny rules covering the git records that the comparison with `origin/main` relies on;
   - a byte-level compare in place of `git diff`;
   - a listing of the hooks directory;
   - a corrected recovery command.

   All of that is new parser surface in a file that is, by its own header, *"a backstop for mistakes and drift, not a security boundary"* [E, `candour-guard.py` l.17 at `dbecdaf`]. Every guard change also reopens V1–V9 and V13 (§4.3). And F9 would still defeat it.
4. **The irreversible outcomes do not depend on the tripwire.**
   - The guard's refusals of merging, approving, pushing to `main` and publishing by shell are code, not deny-list entries. A loosened `settings.json` does not remove them while the guard's file and registration are intact [E, `check_gh`, `check_git_push`, `check_other` at `dbecdaf`].
   - Merging is also refused by the CEO's `hard_deny` merge/approve line, in auto mode [E, results file, V2 `claude auto-mode config`].
   - Pushing to `main` is also refused by the server ruleset. V14(ii) is untested, so that layer is [I].
5. **A sounder route exists if mid-session hold-back is wanted later: move the guard out of the working tree.** Hooks set in managed settings (F11) would do it, and that also closes F9. A tripwire built on that would not need to trust a ref an agent can move. This is the CEO's decision. It needs administrator rights, and it is not urgent.

**What I would ship instead.** One PR, which the CEO approves and merges:

| Item (from #17, or from the CTO's review) | Under (b) |
|---|---|
| #17 change 1: the tripwire in `PreToolUse` | **Drop.** |
| #17 change 2: the wider matcher | **Drop.** It existed only to carry the tripwire. That makes CTO F5 moot (see T4). |
| #17 change 3: `ConfigChange` lets a restore through | **Drop.** Keep today's rule, which blocks every project-settings change. This removes the mid-session loosening that CTO F1 and F3 found: today's guard returns `block` for it [E, CTO F1]. |
| #17 change 4: `SessionStart` also returns `additionalContext` | **Keep.** It only detects: drift produces a warning, not a lockout. It is what tells the model, not only the CEO, that the session may be running on a loosened file. |
| CTO F4: run Python with `-I` in all three hook `args`, run the suite with `-I`, correct the docstring | **Ship.** The weakness is in today's guard. |
| CTO F2: the recovery wording | **Ship.** In the `SessionStart` warning and in the results file's operating notes. The command must remove files a branch added, not only overwrite tracked ones; the CTO's review gives a form that works. It then says: restart the session. |
| CTO F7 (`--no-optional-locks`) and F11 (one root lookup) | **Ship.** Both now apply only to `SessionStart`, and each is a few tokens. |
| CTO F8 | **Document**, as the CTO proposes. |

**Cost:** €0 running (Constitution 1.5). The drift check runs once per process start, not once per tool call.

**Residuals I accept under (b),** named so that nobody reads them as covered:
- An agent that alters git's own records, on which the comparison with `origin/main` relies, can silence the `SessionStart` warning (CTO F1, F3). *(Method redacted for publication, CSO sign-off 2026-10-04; the CTO holds the reproduction.)* That loses a warning, not a control. The CTO's byte compare (about 20 lines) closes it if the CEO wants it. I would not hold the PR for it.
- The limit in T2.

### T2. The limit, for the record

**I disagree with the commission's wording of the limit, once.**
- **It says *"mid-session settings edits"*.** §1 shows the opposite. A mid-session edit goes through `ConfigChange`, and the current guard blocks it. What got through was a loosened file **loaded when the Desktop restarted the process**.
- **It says merges, pushes and publishing stay blocked *"by the deny rules … regardless"*.** In this exact case, a deny rule is the thing that was lost. The `hard_deny` lines also cover merging and approving, not publishing.

**The sentence for the record** (V9(iv), `pipeline/cso-controls-results.md`):

> **V9(iv) limit.** In the Claude Desktop, a change to the project's Claude Code settings that is already on disk when the app restarts a session's process — which the app does by itself on relaunch, rewind or message edit — takes effect in that session, removed deny rules included. A later restore does not reach the running process until it restarts again. Candour does not hold such a change back. Within one process, `ConfigChange` blocks every project-settings change. Whatever the settings say, the guard still refuses shell commands that merge, approve, push to `main` or publish, as long as its file and its registration are intact. Merging is also refused by the CEO's `hard_deny` line in auto mode, and pushing to `main` by the server ruleset (not yet tested: V14(ii)). **Operating rule: after any change to `.claude/` on disk, by hand or by a pull, restart the session.**

**The re-test changes with it:**
- V9(iv) is re-run by §5 step 3(a) only: mid-session, in one process. The record must show, from `main.log`, that no respawn happened between the edit and the test.
- If it passes, V9(iv) is recorded as **trusted with this stated limit**.
- §5 step 3(b) is retired. Under (b) its expected result is "the command runs". That is the limit itself, so it tests nothing.

### T3. GitHub issue for F9

Written for a public repository: it names the weakness and the fix, with no command recipes (Article 3, *"security-sensitive implementation details"*). The CTO holds the reproduction privately. **Not filed.** Filing it publishes content, so the CEO or the main session files it with his approval.

---

**Title:** Guard: a tree-replacing git operation in the main checkout can replace candour-guard itself (F9)

**Labels:** `security`

**Body:**

> **What.** In the main checkout, `candour-guard` allows git operations that replace the whole working tree: switching branches, and resetting to another commit. It allows them because their arguments name no control path. When the incoming tree carries a different `.claude/hooks/candour-guard.py` or `.claude/settings.json`, the next hook call runs the incoming files. No check inside the guard can catch its own replacement.
>
> **Found by:** the CTO's review of PR #17 (finding F9), reproduced on a throwaway repository only. Present in the guard at `dbecdaf`. It is not introduced by #17.
>
> **Who can trigger it.** Any Claude Code session whose working directory is the main checkout. Agents can push non-`main` branches, so a tree with different controls is easy to come by. The CEO's own terminal is unaffected, because hooks do not run there.
>
> **What is still protected if it happens.** The server ruleset on `main`, and the CEO's user-level `hard_deny` lines. Neither lives in the repository.
>
> **Interim practice (already in force).** The main checkout stays on `main`. Agents work in worktrees. The CEO pulls `main` by hand.
>
> **Fix options, for the CSO to propose and the CEO to approve:**
> 1. The guard refuses tree-replacing git operations when the working directory is the main checkout. Updating `main` there stays a CEO task, done in a terminal. *Cost: the main session can no longer pull `main` itself.*
> 2. The guard allows them only when the incoming `.claude/` is byte-identical to `origin/main`'s. *Weaker: it trusts a ref an agent can move (#17, CTO F1).*
> 3. Move the guard's registration out of the repository, into managed or user settings, with the guard file at a path no checkout can replace. This closes F9 by construction, and F11 with it. *Needs administrator rights; affects every project on the machine.*
>
> **Done when:** the chosen option has must-block tests for each tree-replacing form, run in a fixture whose incoming branch carries a different guard; V1–V9 and V13 are re-run (CSO §4.3); and the results are recorded in `pipeline/cso-controls-results.md`.
>
> **Owner:** CSO (proposal). **Approval and merge:** CEO.

---

### T4. Disagreements, in writing once

1. **With my own §3.** I proposed the tripwire. The CTO's F1, F3, F6 and F9 show it trusts what agents can move and costs more than I priced. I withdraw it.
2. **With the commission's cheap-fix list, on item 5 (the matcher).** Under (b) it does not apply.
   - The live matcher is `Bash|Monitor` [E, `settings.json` at `dbecdaf`].
   - Adding `RemoteTrigger`, `CronCreate` and `ScheduleWakeup` would send them to a guard that does nothing for non-Bash tools except the bypass check. Bypass is now off (V11 PASS).
   - `RemoteTrigger` is already a deny rule. `CronCreate` and `ScheduleWakeup` are already ask rules [E, same file].
   - The CTO's proposed test, that every tool named in `deny` or `ask` must match the matcher, only makes sense once the matcher is widened.
   - Hook cover for non-Bash tools is a separate decision from the tripwire. I do not recommend it now.
3. **With the commission's wording of the limit** (T2).

### T5. What would change this, and where I looked

**Option (a) becomes the right call if any of these happens:**
- an ordinary route is found that loosens `settings.json` on disk but leaves the guard and its registration alone, for example a tool that writes the file and is neither denied nor routed to the hook;
- V14(ii) fails, meaning the server ruleset does not refuse a direct push to `main`. That would put more weight on the local controls;
- the guard moves out of the working tree (T1 reason 5). F1, F3 and F9 then change shape, and a tripwire could compare against a source agents cannot move.

**Where I looked:**
- the Constitution (Articles 3, 5.4, 6.1)
- my charter
- the evidence standard
- §1–§7 of this file
- `pipeline/cso-controls-results.md` from R3 to the end
- the CTO's review of #17, in full, and the PR's state
- `settings.json` and `candour-guard.py` at `origin/main`: the matcher, the hook args, the deny and ask lists, the guard's header, and its merge, push and publish checks
- `git log` of the control paths
- `git diff --stat dbecdaf 68168b2`
- the issue list (no F9 issue exists)

**What I did not do:**
- run any probe
- touch the live `.claude/` files
- edit anything but this file
- commit, push, or file the issue
