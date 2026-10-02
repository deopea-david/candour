#!/usr/bin/python3
# candour-guard-test: offline tests for .claude/hooks/candour-guard.py.
# Run: /usr/bin/python3 .claude/hooks/candour-guard-test.py   (exit 0 = all pass)
# Builds a throwaway git repo in a temp dir; touches nothing else.
import json, os, subprocess, sys, tempfile

GUARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "candour-guard.py")
T = tempfile.mkdtemp(prefix="candour-guard-test-")
R = os.path.join(T, "repo")
sh = lambda *a: subprocess.run(a, check=True, capture_output=True)
sh("git", "init", "-q", "-b", "main", R)
sh("git", "-C", R, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "i")
sh("git", "-C", R, "checkout", "-q", "-b", "feat/x")
sh("git", "init", "-q", "--bare", os.path.join(T, "remote.git"))
sh("git", "-C", R, "remote", "add", "origin", os.path.join(T, "remote.git"))
ENV = dict(os.environ, CLAUDE_PROJECT_DIR=R)


def rc(cmd, mode="auto"):
    d = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": cmd},
         "cwd": R, "permission_mode": mode}
    return subprocess.run(["/usr/bin/python3", GUARD], input=json.dumps(d), capture_output=True,
                          text=True, env=ENV).returncode


MUST_BLOCK = [
    # merge and approval, in the forms deny rules miss
    "gh pr merge 12 --merge", "GH_TOKEN=x gh pr merge 12", "timeout 30 gh pr merge 12",
    "/opt/homebrew/bin/gh pr merge 12", "sh -c 'gh pr merge 12'", "bash -lc \"gh pr merge 12\"",
    "eval 'gh pr merge 12'", "echo $(gh pr merge 12)", "x=`gh pr merge 1`", "gh 'pr' 'merge' 3",
    "gh pr merge --auto 3", "gh pr review 3 --approve", "bash <<EOF\ngh pr merge 3\nEOF",
    "gh api -X PUT repos/deopea-david/candour/pulls/3/merge", "gh api --method=PUT /repos/o/r/pulls/3/merge",
    "gh api repos/o/r/merges -f base=main -f head=feat", "gh api graphql --input q.json",
    "gh api graphql -f query='mutation{mergePullRequest(input:{pullRequestId:\"x\"}){clientMutationId}}'",
    "gh api graphql -f query='mutation { enablePullRequestAutoMerge(input:{}) { clientMutationId } }'",
    "curl -X PUT -H 'Authorization: token x' https://api.github.com/repos/o/r/pulls/1/merge",
    "python3 -c \"import subprocess; subprocess.run(['gh','pr','merge','1'])\"",
    "node -e \"require('child_process').execSync('gh pr merge 1')\"",
    # push to main, force, deletion
    "git push origin main", "git push origin HEAD:main", "git push origin feat/x:main",
    "git push origin HEAD:refs/heads/main", "git push origin +feat/x", "git push -f origin feat/x",
    "git push --force-with-lease origin feat/x", "git push origin :main", "git push --delete origin main",
    "git push --all origin", "git push --mirror", "git -C . push origin main", "git 'push' origin main",
    "git -c push.default=current push origin main", "/usr/bin/git push origin main",
    "cd . && git push origin main", "git -c alias.p=push p origin main", "FOO=1 git push origin main",
    "git push origin 'refs/heads/*:refs/heads/*'", "nohup git push origin main &", "xargs git push origin main",
    "git config alias.p push", "git config remote.origin.push refs/heads/feat/x:refs/heads/main",
    "python3 - <<'EOF'\nimport subprocess\nsubprocess.run(['git','push','origin','main'])\nEOF",
    # GitHub settings, rulesets, refs, identity
    "gh api -X PUT repos/o/r/rulesets/1 --input r.json", "gh api -X DELETE repos/deopea-david/candour/rulesets/1",
    "gh api -X PATCH repos/deopea-david/candour -f visibility=private", "gh api -X PATCH repos/o/r/git/refs/heads/main -f sha=a",
    "gh api -X PUT repos/o/r/contents/README.md -f message=x -f content=eA==", "curl -d '{}' https://api.github.com/repos/o/r/rulesets",
    "gh repo edit --visibility public", "gh repo delete o/r --yes", "gh repo sync", "gh secret set X",
    "gh auth token", "gh auth switch -u other", "gh alias set m 'pr merge'", "gh workflow disable ci.yml",
    # publishing
    "gh release create v1", "gh gist create f.md --public", "npm publish", "eas submit -p ios",
    # unattended or scheduled work
    "claude -p 'do things'", "claude --dangerously-skip-permissions", "claude --bg 'x'", "crontab /tmp/c",
    "launchctl load ~/Library/LaunchAgents/x.plist", "at now + 1 hour",
    "osascript -e 'tell app \"Terminal\" to do script \"ls\"'",
    # the live controls
    "echo '{\"disableAllHooks\": true}' > .claude/settings.local.json", "sed -i '' 's/x/y/' .claude/settings.json",
    "cp /tmp/x .claude/hooks/candour-guard.py", "rm .claude/hooks/candour-guard.py",
    "git checkout other -- .claude/settings.json", "W=.claude; echo x > $W/settings.local.json",
    "cat /tmp/new > ~/.claude/settings.json",
    "python3 - <<'EOF'\nopen('.claude/settings.json','w').write('{}')\nEOF",
    # F1: running a live hook script is allowed only as `python3 <script>`; nothing else rides on it
    "python3 .claude/hooks/candour-guard-test.py .claude/settings.json",
    "python3 .claude/hooks/candour-guard-test.py .claude/hooks/candour-guard.py",
    "python3 -i .claude/hooks/candour-guard-test.py", "PYTHONINSPECT=1 python3 .claude/hooks/candour-guard-test.py",
    "export PYTHONINSPECT=1; /usr/bin/python3 .claude/hooks/candour-guard-test.py",
    "sh -c 'PYTHONINSPECT=1 python3 .claude/hooks/candour-guard-test.py'",
    "python3 .claude/hooks/other.py", "python3 .claude/hooks/../settings.json",
    "node .claude/hooks/candour-guard-test.py", "python3 .claude/hooks/candour-guard-test.py > .claude/hooks/out.txt",
    "python3 .claude/hooks/candour-guard-test.py && cp /tmp/x .claude/hooks/candour-guard.py",
    "python3 .claude/hooks/candour-guard-test.py <<'EOF'\nprint(1)\nEOF",
    # unparseable input fails closed
    "echo \"unbalanced",
]
MUST_ALLOW = [
    "git status", "git push -u origin feat/x", "git push origin feat/x", "git -C . push origin feat/x",
    "git push origin HEAD", "git push", "git push origin feat/x:feat/x", "git log --oneline -3 main",
    "git merge main", "git diff main...feat/x", "git commit -m 'gh pr merge note'",
    "gh pr create --title t --body 'Refs #1. Merge: the CEO runs gh pr merge'", "gh pr view 3",
    "gh pr comment 3 --body 'review record'", "gh pr review 3 --comment -b ok",
    "gh api repos/deopea-david/candour/rulesets/23570113", "gh api repos/o/r/pulls/3",
    "gh api graphql -f query='{ repository(owner:\"o\",name:\"r\"){ id } }'",
    "gh api repos/o/r/issues/3/comments -f body='hi'", "gh api repos/o/r/milestones --method POST -f title=M0",
    "gh issue create --title t --body b", "gh auth status", "gh ruleset list", "gh release view v1",
    "gh workflow run secret-scan.yml", "gh repo sync --help 2>&1 | grep force",
    "cat > notes.md <<'EOF'\nTo merge, run gh pr merge 3 --merge\nEOF", "cat .claude/settings.json",
    "ls .claude/hooks", "cp /tmp/x .claude/worktrees/w/.claude/settings.json",
    "cd .claude/worktrees/w && sed -i '' 's/a/b/' .claude/settings.json",
    "python3 - <<'EOF'\np='CLAUDE.md'\ns=open(p).read().replace('Merge: gh pr merge <PR>','Merge: gh pr merge <PR> --merge')\nopen(p,'w').write(s)\nEOF",
    "claude --version 2>/dev/null", "claude doctor", "crontab -l", "launchctl list",
    "curl -s https://api.github.com/repos/o/r", "npm test", "python3 scripts/check.py",
]

fail = 0
for c in MUST_BLOCK:
    if rc(c) != 2:
        fail += 1; print("NOT BLOCKED:", repr(c))
for c in MUST_ALLOW:
    if rc(c) != 0:
        fail += 1; print("WRONGLY BLOCKED:", repr(c))
if rc("git status", mode="bypassPermissions") != 2:
    fail += 1; print("NOT BLOCKED: any command in bypassPermissions mode")
sh("git", "-C", R, "checkout", "-q", "main")
for c in ("git push", "git push origin", "git push origin HEAD"):
    if rc(c) != 2:
        fail += 1; print("NOT BLOCKED on main:", c)
print("%d must-block, %d must-allow, %d failures" % (len(MUST_BLOCK) + 4, len(MUST_ALLOW), fail))
sys.exit(1 if fail else 0)
