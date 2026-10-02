#!/usr/bin/python3
# candour-guard: Claude Code hook for the Candour repositories.
# CSO proposal, 2026-10-02 (pipeline/cso-advice-permission-mode.md, section 3).
# Changing this file needs a CSO note and the CEO's approval. Agents never edit
# the live copy; a change is drafted in a worktree and merged by the CEO.
#
# Events (dispatched on hook_event_name):
#   PreToolUse (Bash, Monitor)  blocks: merging or approving a PR; pushing to,
#       force-pushing or deleting main; GitHub ruleset, settings, ref, secret and
#       identity writes; publishing; headless, background, scheduled or bypass
#       runs; shell writes to the live Claude Code settings and hooks; and every
#       command while the session is in bypassPermissions mode.
#   ConfigChange   stops a running session loosening its own settings.
#   SessionStart   warns the CEO about bypass mode or unapproved controls.
#
# Fails closed: a Bash command that cannot be parsed or checked is blocked.
# It is a backstop for mistakes and drift, not a security boundary. It does not
# see programs that are not shell commands (a script's own code, a browser
# click), and pattern checks on interpreter code are best effort.
# Python 3.9 standard library only: runs on stock macOS /usr/bin/python3.

import json
import os
import re
import shlex
import subprocess
import sys

PROTECTED_BRANCHES = {"main"}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
OTHER_INTERPRETERS = {"python", "python3", "node", "perl", "ruby", "deno", "bun"}
WRAPPERS = {"command", "builtin", "nohup", "time", "noglob", "exec", "nice", "timeout",
            "stdbuf", "env", "xargs", "sudo", "caffeinate", "arch"}
SEPARATORS = {";", "&&", "||", "|", "&", "|&", "(", ")", ";;"}
GIT_OPTS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path",
                       "--super-prefix", "--config-env"}
WRITE_VERBS = {"cp", "mv", "rm", "ln", "chmod", "chown", "truncate", "install", "rsync", "dd",
               "unlink", "touch", "tee", "patch", "ditto", "rmdir", "mkdir"}
GIT_WRITE_SUBS = {"checkout", "restore", "reset", "stash", "apply", "am", "mv", "rm", "switch",
                  "merge", "pull", "rebase", "cherry-pick", "revert"}
EXEC_CONTEXT = re.compile(r"subprocess|os\.system|os\.popen|popen|check_call|check_output|"
                          r"execSync|execFile|spawn|child_process|system\s*\(|Open3|IO\.popen")


PROJECT = [None]  # the project root, fixed for the whole check (see pre_tool_use)


class Block(Exception):
    pass


def block(reason):
    raise Block(reason)


def is_python(name):
    return bool(re.match(r"^python3?(\.\d+)?$", name))


# ---------------------------------------------------------------- parsing

def split_heredocs(text):
    """Heredoc bodies fed to a shell stay in the shell text; bodies fed to
    another interpreter are returned as code to scan; bodies written to a file
    are dropped (they are data, not commands)."""
    lines = text.split("\n")
    out, code, i = [], [], 0
    while i < len(lines):
        line = lines[i]
        m = re.search(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1", line)
        if not m:
            out.append(line)
            i += 1
            continue
        delim = m.group(2)
        head = re.split(r"&&|\|\||;|\||\(", line[: m.start()])[-1].split()
        head = unwrap(head)
        first = os.path.basename(head[0]) if head else ""
        i += 1
        body = []
        while i < len(lines) and lines[i].strip() != delim:
            body.append(lines[i])
            i += 1
        if first in OTHER_INTERPRETERS or is_python(first):
            # mark where the code goes, so it is checked with that segment's directory
            line = line[: m.end()] + " __CANDOUR_HEREDOC_%d__ " % len(code) + line[m.end():]
            code.append("\n".join(body))
        out.append(line)
        if first in SHELLS:
            out.extend(body)
        i += 1  # the delimiter line
    return "\n".join(out), code


def tokenize(text):
    text = text.replace("`", " ; ").replace("$(", " ( ").replace("\n", " ; ")
    lex = shlex.shlex(text, posix=True, punctuation_chars=";&|()<>")
    lex.whitespace = " \t\r\n"
    lex.whitespace_split = True
    lex.commenters = ""
    return list(lex)


def split_segments(tokens):
    segs, cur = [], []
    for t in tokens:
        if t in SEPARATORS or (t and set(t) <= set(";&|()")):
            if cur:
                segs.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur:
        segs.append(cur)
    return segs


def split_redirects(seg):
    """Return (argv without redirections, list of redirection targets)."""
    argv, targets, i = [], [], 0
    while i < len(seg):
        t = seg[i]
        if set(t) <= set("<>") and t:
            if argv and re.match(r"^\d+$", argv[-1]):
                argv.pop()  # the fd number in 2>file
            if i + 1 < len(seg):
                if seg[i + 1] == "&":
                    i += 1
                    if i + 1 < len(seg) and re.match(r"^\d+$", seg[i + 1]):
                        i += 1
                elif ">" in t:
                    targets.append(seg[i + 1])
                i += 2
                continue
        argv.append(t)
        i += 1
    return argv, targets


def unwrap(argv):
    """Strip leading assignments and wrapper commands; return the real argv."""
    changed = True
    while argv and changed:
        changed = False
        while argv and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0]):
            argv = argv[1:]
            changed = True
        if argv and os.path.basename(argv[0]) in WRAPPERS:
            name = os.path.basename(argv[0])
            argv = argv[1:]
            changed = True
            while argv and (argv[0].startswith("-") or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0])
                            or (name == "timeout" and re.match(r"^\d", argv[0]))):
                if name == "nice" and argv[0] == "-n" and len(argv) > 1:
                    argv = argv[1:]
                argv = argv[1:]
    return argv


def expand(s, env):
    s = re.sub(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?", lambda m: env.get(m.group(1), m.group(0)), s)
    return os.path.expanduser(s)


def git_out(cwd, *args):
    try:
        r = subprocess.run(["git", "-C", cwd] + list(args), capture_output=True, text=True, timeout=3)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


# ---------------------------------------------------------------- live controls

def live_control(path, cwd, env):
    """True if the path is a live Claude Code control file: the project's own
    .claude/settings*.json or .claude/hooks (not a worktree's copy), the user's
    ~/.claude/settings.json or ~/.claude.json, or managed settings."""
    p = expand(path, env)
    if not re.search(r"\.claude|managed-settings|ClaudeCode", p):
        return False
    if "$" in p:
        return bool(re.search(r"\.claude/(settings|hooks)", p))  # unresolvable: fail closed
    if not os.path.isabs(p):
        p = os.path.join(cwd, p)
    p = os.path.normpath(p)
    home = os.path.expanduser("~")
    project = PROJECT[0] or cwd
    if p in (os.path.join(home, ".claude", "settings.json"), os.path.join(home, ".claude.json")):
        return True
    if "managed-settings" in p or "Application Support/ClaudeCode" in p:
        return True
    pc = os.path.join(project, ".claude")
    if p.startswith(os.path.join(pc, "worktrees") + os.sep):
        return False
    return p in (os.path.join(pc, "settings.json"), os.path.join(pc, "settings.local.json")) or \
        p == os.path.join(pc, "hooks") or p.startswith(os.path.join(pc, "hooks") + os.sep)


def check_control_writes(argv, targets, cwd, env):
    if any(live_control(t, cwd, env) for t in targets):
        block("writing to the live Claude Code settings or hooks (the CEO changes these by hand)")
    if not argv:
        return
    name = os.path.basename(argv[0])
    writes = name in WRITE_VERBS or (name == "sed" and any(re.match(r"^-[a-zA-Z]*i", a) or a == "--in-place"
                                                          for a in argv[1:])) \
        or (name == "perl" and any(re.match(r"^-[a-zA-Z]*i", a) for a in argv[1:])) \
        or (name == "git" and any(a in GIT_WRITE_SUBS for a in argv[1:4])) \
        or name in OTHER_INTERPRETERS or is_python(name)
    if writes and any(live_control(a, cwd, env) for a in argv[1:]):
        block("writing to the live Claude Code settings or hooks (the CEO changes these by hand)")


# ---------------------------------------------------------------- git

def check_git(argv, cwd, env, depth):
    i, aliases = 1, {}
    while i < len(argv) and argv[i].startswith("-"):
        a = argv[i]
        if a in GIT_OPTS_WITH_VALUE and i + 1 < len(argv):
            if a == "-C":
                cwd = os.path.join(cwd, expand(argv[i + 1], env))
            elif a == "-c":
                kv = argv[i + 1]
                if kv.lower().startswith("alias."):
                    k, _, v = kv.partition("=")
                    aliases[k[6:]] = v
                if re.match(r"(?i)(core\.hookspath|remote\..*\.push|url\..*insteadof|push\.default)", kv):
                    block("git -c changes hooks, push routing or remote URLs")
            i += 2
            continue
        i += 1
    if i >= len(argv):
        return
    sub, rest = argv[i], argv[i + 1:]
    alias = aliases.get(sub)
    if alias is None and sub not in ("push", "config", "status", "log", "diff", "show", "add",
                                     "commit", "fetch", "branch", "rev-parse"):
        alias = git_out(cwd, "config", "--get", "alias." + sub)
    if alias:
        if alias.startswith("!"):
            check_text(alias[1:], cwd, env, depth + 1)
            return
        parts = shlex.split(alias)
        sub, rest = parts[0], parts[1:] + rest
    if sub == "push":
        check_git_push(rest, cwd)
    elif sub == "config":
        joined = " ".join(rest)
        reading = re.search(r"(^| )(--get|--get-all|--list|-l|--get-regexp|--show-origin)( |$)", joined)
        if not reading and re.search(r"(?i)(alias\.|core\.hookspath|remote\.\S*\.push|url\.\S*insteadof|"
                                     r"branch\.\S*\.pushremote|remote\.pushdefault|push\.default)", joined):
            block("git config change to aliases, hooks or push routing")
    elif sub in ("filter-repo", "filter-branch", "replace"):
        block("history rewriting")


def check_git_push(args, cwd):
    opts, pos, j = [], [], 0
    while j < len(args):
        a = args[j]
        if a == "--":
            pos.extend(args[j + 1:])
            break
        if a.startswith("-"):
            opts.append(a)
            if a in ("--repo", "-o", "--push-option", "--receive-pack", "--exec") and j + 1 < len(args):
                j += 1
        else:
            pos.append(a)
        j += 1
    flat = " ".join(opts)
    if re.search(r"(^| )(--all|--mirror|--branches)( |$)", flat):
        block("git push --all or --mirror would update main")
    if re.search(r"(^| )(--force\S*|-[a-zA-Z]*f[a-zA-Z]*)( |$)", flat):
        block("force push (pushed branches are never rewritten)")
    if re.search(r"--receive-pack|--exec", flat):
        block("git push --receive-pack or --exec")
    deleting = bool(re.search(r"(^| )(--delete|-[a-zA-Z]*d[a-zA-Z]*)( |$)", flat))
    refspecs = pos[1:]
    current = git_out(cwd, "symbolic-ref", "--quiet", "--short", "HEAD")
    if not refspecs:
        if current is None or current in PROTECTED_BRANCHES:
            block("git push with no refspec, from main or from a directory the guard cannot read. "
                  "Name the branch explicitly: git push -u origin <branch>")
        mode = (git_out(cwd, "config", "--get", "push.default") or "simple").lower()
        if mode == "matching":
            block("push.default=matching could update main; name the branch explicitly")
        remote = pos[0] if pos else (git_out(cwd, "config", "--get", "branch.%s.pushRemote" % current)
                                     or git_out(cwd, "config", "--get", "remote.pushDefault") or "origin")
        if git_out(cwd, "config", "--get-all", "remote.%s.push" % remote):
            block("remote.%s.push is configured; name the branch explicitly" % remote)
        if mode in ("upstream", "tracking"):
            up = git_out(cwd, "config", "--get", "branch.%s.merge" % current) or ""
            if up.replace("refs/heads/", "") in PROTECTED_BRANCHES:
                block("this branch's upstream is main")
        return
    for spec in refspecs:
        if spec.startswith("+"):
            block("force refspec (+)")
        if "*" in spec:
            block("wildcard refspec")
        src, dst = (spec.split(":", 1) if ":" in spec else (spec, spec))
        if ":" in spec and src == "":
            deleting = True
        names = [dst] + ([src] if deleting else [])
        for name in names:
            if not name:
                continue
            n = re.sub(r"^refs/(heads|remotes/[^/]+)/", "", name)
            if n in ("HEAD", "@"):
                n = current or "HEAD"
            if n in PROTECTED_BRANCHES or n == "HEAD":
                block("push to, or deletion of, main")


# ---------------------------------------------------------------- gh

GH_WRITE_ENDPOINTS = re.compile(
    r"pulls/[^/]+/merge|/merges\b|merge-upstream|rulesets|/protection|/collaborators|/invitations|"
    r"/keys\b|/hooks\b|/actions/(secrets|variables|permissions|workflows/[^/]+/(enable|disable))|"
    r"/environments|/pages\b|/releases|/git/refs|/contents/|^/?gists|/forks\b|/transfer|/visibility|"
    r"/vulnerability-alerts|/automated-security-fixes|/branches/[^/]+/rename|^/?user/repos|"
    r"^/?orgs/[^/]+/repos|/generate\b")
GH_REPO_ROOT = re.compile(r"^/?repos/[^/]+/[^/]+/?$")
GQL_MUTATIONS = re.compile(
    r"(?i)mergePullRequest|enablePullRequestAutoMerge|mergeBranch|updateRepository\b|deleteRepository|"
    r"(create|update|delete)RepositoryRuleset|(create|update|delete)BranchProtectionRule|"
    r"\bupdateRefs?\b|\bcreateRef\b|\bdeleteRef\b|createCommitOnBranch|addPullRequestReview|"
    r"submitPullRequestReview|createGist|cloneTemplateRepository|createRepository\b|"
    r"transferRepository|archiveRepository|updateRepositoryWebCommitSignoffSetting")


def check_gh(argv):
    args = argv[1:]
    if not args or "--help" in args or "-h" in args or args[0] in ("help", "--version", "version"):
        return
    sub, rest = args[0], args[1:]
    verb = rest[0] if rest else ""
    flat = " ".join(rest)
    if sub == "pr":
        if verb == "merge":
            block("gh pr merge: the CEO merges")
        if verb == "review" and re.search(r"(^| )(--approve|-a)( |$)", flat):
            block("approving a pull request: approval is the CEO's")
    elif sub == "api":
        check_gh_api(rest)
    elif sub == "repo" and verb in ("edit", "delete", "rename", "archive", "unarchive", "create", "fork",
                                     "sync", "deploy-key", "autolink", "set-default"):
        read_only = (verb == "set-default" and re.search(r"(^| )(--view|-v)( |$)", flat)) or \
            (verb in ("deploy-key", "autolink") and len(rest) > 1 and rest[1] in ("list", "view"))
        if not read_only:
            block("gh repo %s changes repository settings or publishes" % verb)
    elif sub == "release" and verb not in ("list", "view", "download", "verify", "verify-asset", ""):
        block("gh release %s is publishing" % verb)
    elif sub == "gist" and verb in ("create", "new", "edit", "delete", "rename"):
        block("gh gist %s is publishing" % verb)
    elif sub in ("secret", "variable") and verb in ("set", "delete", "remove"):
        block("gh %s %s" % (sub, verb))
    elif sub == "auth" and verb not in ("status", ""):
        block("gh auth %s changes or exposes the GitHub identity" % verb)
    elif sub == "workflow" and verb in ("enable", "disable"):
        block("gh workflow %s" % verb)
    elif sub == "alias" and verb in ("set", "import", "delete"):
        block("gh alias %s" % verb)
    elif sub == "ruleset" and verb not in ("list", "ls", "view", "check", ""):
        block("gh ruleset %s" % verb)
    elif sub == "extension" and verb in ("install", "upgrade", "exec", "create"):
        block("gh extension %s runs downloaded code" % verb)


def check_gh_api(rest):
    method, endpoint, has_body, body, j = None, None, False, [], 0
    while j < len(rest):
        a = rest[j]
        if a in ("-X", "--method") and j + 1 < len(rest):
            method = rest[j + 1].upper()
            j += 2
            continue
        if a.startswith("--method="):
            method = a.split("=", 1)[1].upper()
        elif a.startswith("-X") and len(a) > 2:
            method = a[2:].upper()
        elif a in ("-f", "-F", "--field", "--raw-field", "--input") and j + 1 < len(rest):
            has_body = True
            body.append(rest[j + 1])
            j += 2
            continue
        elif re.match(r"^(--field=|--raw-field=|--input=|-f.|-F.)", a):
            has_body = True
            body.append(a)
        elif a in ("-H", "--header", "-q", "--jq", "-t", "--template", "--hostname", "--cache",
                   "-p", "--preview") and j + 1 < len(rest):
            j += 2
            continue
        elif not a.startswith("-") and endpoint is None:
            endpoint = a
        j += 1
    if endpoint is None:
        return
    body_text = " ".join(body)
    if endpoint.strip("/") == "graphql":
        if GQL_MUTATIONS.search(body_text) or "--input" in rest or any(x.startswith("--input=") for x in rest):
            block("a GraphQL mutation that merges, approves, publishes or changes settings")
        return
    method = method or ("POST" if has_body else "GET")
    if method == "GET":
        return
    ep = re.sub(r"^https?://api\.github\.com", "", endpoint)
    if GH_WRITE_ENDPOINTS.search(ep) or GH_REPO_ROOT.match(ep):
        block("gh api %s %s writes merges, settings, refs or published content" % (method, ep))
    if re.search(r"pulls/[^/]+/reviews", ep) and re.search(r"(?i)APPROVE", body_text):
        block("approving a pull request through the API")


# ---------------------------------------------------------------- other programs

def check_other(name, argv):
    flat = " ".join(argv)
    if name in ("curl", "wget", "http", "https", "xh"):
        if re.search(r"(api|uploads)\.github\.com|github\.com/", flat) and \
                re.search(r"(?i)(-X\s*|--request[ =])(PUT|POST|PATCH|DELETE)|(^| )(-d|--data\S*|--json|-F|--form|-T)( |=|$)|"
                          r"(^| )(PUT|POST|PATCH|DELETE)( |$)", flat):
            block("a write request to the GitHub API outside gh")
    elif name == "claude":
        if not re.match(r"^claude( (--version|-v|-h|--help|doctor|auto-mode (defaults|config|critique)|"
                        r"mcp (list|get)( \S+)?))?$", flat):
            block("starting or reconfiguring Claude Code from a shell (headless, background and "
                  "bypass runs are out of scope)")
    elif name == "crontab" and argv[1:] != ["-l"]:
        block("crontab changes schedule unattended work")
    elif name == "launchctl" and len(argv) > 1 and argv[1] not in (
            "list", "print", "print-cache", "print-disabled", "blame", "version", "help"):
        block("launchctl %s can schedule unattended work" % argv[1])
    elif name in ("at", "batch"):
        block("%s schedules unattended work" % name)
    elif name == "osascript":
        block("osascript drives other applications (terminal, browser) outside these checks")
    elif name in ("npm", "pnpm", "yarn", "bun") and "publish" in argv[1:3]:
        block("package publish")
    elif name == "eas" and len(argv) > 1 and argv[1] in ("submit", "update", "credentials", "env",
                                                          "secret", "metadata:push"):
        block("eas %s publishes or touches credentials" % argv[1])
    elif name == "fastlane":
        block("fastlane publishes to the stores")
    elif name == "open" and re.search(r"(?i)\.(command|tool)\b|-a\s+(terminal|iterm)", flat):
        block("open runs a script in another terminal, outside these checks")


def check_code(code, cwd, env):
    """Best-effort scan of code an interpreter will run (python -c, node -e,
    a heredoc fed to python). Only code that can run commands is checked."""
    if re.search(r"open\(|write_text|writeFile|shutil\.|os\.(remove|rename|replace|unlink)|unlinkSync|rmSync", code):
        for path in re.findall(r"[\"']([^\"'\n]*\.claude[^\"'\n]*)[\"']", code):
            if live_control(path, cwd, env):
                block("interpreter code writing to the live Claude Code settings or hooks")
    if not EXEC_CONTEXT.search(code):
        return
    flat = re.sub(r"[\"'\\\[\](),+]", " ", code)
    flat = re.sub(r"\s+", " ", flat)
    if re.search(r"\bgh pr merge\b|\bgh pr review\b.*(--approve|-a\b)", flat):
        block("interpreter code that merges or approves a pull request")
    if GQL_MUTATIONS.search(flat):
        block("interpreter code with a GitHub mutation that merges, approves or changes settings")
    if re.search(r"\bgh api\b", flat) and re.search(r"pulls/\S+/merge|/merges\b|rulesets|/protection", flat) \
            and re.search(r"(?i)\b(PUT|PATCH|POST|DELETE)\b", flat):
        block("interpreter code that writes GitHub merges, rulesets or protection")
    if re.search(r"\bgit\b(?: \S+){0,6} push\b", flat) and \
            re.search(r"(?<![\w/-])main\b|--all|--mirror|--force|(^| )-f( |$)", flat):
        block("interpreter code that pushes to main or force-pushes")
    if re.search(r"\bgh (release|gist) (create|upload|edit)|\bnpm publish\b|\bclaude -p\b|"
                 r"--dangerously-skip-permissions|\bcrontab\b|launchctl (load|bootstrap|submit)", flat):
        block("interpreter code that publishes or starts unattended work")


# ---------------------------------------------------------------- dispatch

def check_text(text, cwd, env=None, depth=0):
    if depth > 4:
        block("command nesting too deep to check")
    env = dict(env or {})
    body, code_blobs = split_heredocs(text)
    seen, start_cwd = set(), cwd
    for seg in split_segments(tokenize(body)):
        raw, targets = split_redirects(seg)
        if raw and all(re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", t) for t in raw):
            for t in raw:  # NAME=value on its own: remember it for cd and -C
                k, _, v = t.partition("=")
                env[k] = expand(v, env)
            continue
        if raw and raw[0] == "export":
            for t in raw[1:]:
                if "=" in t:
                    k, _, v = t.partition("=")
                    env[k] = expand(v, env)
            continue
        argv = unwrap(raw)
        check_control_writes(argv, targets, cwd, env)
        if not argv:
            continue
        name = os.path.basename(argv[0])
        if name in ("cd", "pushd") and len(argv) > 1:
            cwd = os.path.join(cwd, expand(argv[1], env))
            continue
        if name in SHELLS:
            for k, a in enumerate(argv[1:], 1):
                if a.startswith("-") and "c" in a[1:] and k + 1 < len(argv):
                    check_text(argv[k + 1], cwd, env, depth + 1)
                    break
            continue
        for a in raw:
            m = re.match(r"^__CANDOUR_HEREDOC_(\d+)__$", a)
            if m and int(m.group(1)) < len(code_blobs):
                seen.add(int(m.group(1)))
                check_code(code_blobs[int(m.group(1))], cwd, env)
        if name in OTHER_INTERPRETERS or is_python(name):
            for k, a in enumerate(argv[1:], 1):
                if a in ("-c", "-e", "--eval", "-p", "--print") and k + 1 < len(argv):
                    check_code(argv[k + 1], cwd, env)
            continue
        if name == "eval":
            check_text(" ".join(argv[1:]), cwd, env, depth + 1)
        elif name == "git":
            check_git(argv, cwd, env, depth)
        elif name == "gh":
            check_gh(argv)
        else:
            check_other(name, argv)
    for n, blob in enumerate(code_blobs):  # code whose marker was not reached
        if n not in seen:
            check_code(blob, start_cwd, env)


def pre_tool_use(data):
    if data.get("permission_mode") == "bypassPermissions":
        block("this session is in bypassPermissions mode, which Candour does not use (Decision 1). "
              "Restart the session in auto mode")
    cwd = data.get("cwd") or os.getcwd()
    root = os.environ.get("CLAUDE_PROJECT_DIR")
    if not root:
        common = git_out(cwd, "rev-parse", "--path-format=absolute", "--git-common-dir")
        root = os.path.dirname(common) if common else cwd
    PROJECT[0] = os.path.normpath(root)
    command = (data.get("tool_input") or {}).get("command")
    if isinstance(command, str):  # a Monitor WebSocket watch has no command
        check_text(command, cwd)


LOOSENING = re.compile(r'"disableAllHooks"\s*:\s*true|"defaultMode"\s*:\s*"bypassPermissions"|'
                       r'"skipDangerousModePermissionPrompt"\s*:\s*true|'
                       r'"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"\s*:\s*"1"')


def config_change(data):
    source = data.get("source")
    if source == "project_settings":
        return {"decision": "block",
                "reason": "project settings change by merge to main and take effect in a new session"}
    if source in ("local_settings", "user_settings"):
        try:
            with open(data.get("file_path") or "") as f:
                content = f.read()
        except Exception:
            return {"decision": "block", "reason": "unreadable settings change"}
        if LOOSENING.search(content):
            return {"decision": "block", "reason": "the change would loosen Candour's controls"}
    return None


def session_start(data):
    msgs = []
    if data.get("permission_mode") == "bypassPermissions":
        msgs.append("This session is in bypass permissions mode. Candour runs in auto mode (Decision 1).")
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
    rc = subprocess.run(["git", "-C", root, "diff", "--quiet", "origin/main", "--",
                         ".claude/settings.json", ".claude/hooks"], capture_output=True, timeout=5).returncode
    if rc == 1:
        msgs.append("The checked-out .claude/settings.json or .claude/hooks differ from origin/main, "
                    "so the controls in force are not the approved ones.")
    elif rc != 0:
        msgs.append("Could not compare .claude/settings.json and .claude/hooks with origin/main.")
    if msgs:
        print(json.dumps({"systemMessage": "candour-guard: " + " ".join(msgs)}))


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        print("candour-guard: unreadable hook input; blocked", file=sys.stderr)
        sys.exit(2)
    event = data.get("hook_event_name")
    try:
        if event == "PreToolUse":
            pre_tool_use(data)
        elif event == "ConfigChange":
            out = config_change(data)
            if out:
                print(json.dumps(out))
        elif event == "SessionStart":
            session_start(data)
        sys.exit(0)
    except Block as b:
        print("candour-guard blocked this: %s. If it is needed, the CEO does it himself." % b,
              file=sys.stderr)
        sys.exit(2)
    except SystemExit:
        raise
    except Exception as e:  # fail closed
        if event == "PreToolUse":
            print("candour-guard could not check this command (%s), so it is blocked. "
                  "Rewrite it more simply." % type(e).__name__, file=sys.stderr)
            sys.exit(2)
        if event == "ConfigChange":
            print(json.dumps({"decision": "block", "reason": "guard error"}))
        sys.exit(0)


if __name__ == "__main__":
    main()
