# Haunts: the security baseline that forms the first commit of `haunts`

**Seat:** Chief Security Officer · **Date:** 2026-09-26 · **Status:** A specification and a set of findings. **It prepares and flags. It does not certify** (Constitution 6.1: *"Agent reviews **prepare and flag; they do not certify**"*). Nothing here has been installed, committed or changed on GitHub.

> ### Correction 1 — 2026-09-26, after acceptance testing (CSO)
>
> **Classification: CORRECTION.** The CEO approved this baseline as **D32**. The Engineer then built it and ran §11's tests (`RESULTS.md`, Engineer, 2026-09-26; local commit `0f8bfa4` in `haunts`, not pushed). **Two statements in this spec were wrong, and one open question is now answered.** I checked both errors at source myself before accepting the fixes. The changes below are made in place and marked *(Correction 1)* where they occur.
>
> 1. **`check-merge-conflict` needs `args: ["--assume-in-merge"]`.** *Was:* the hook listed with no arguments (§3, §4.1). *Why it was wrong:* at the pinned SHA the hook exits early, with `if not is_in_merge() and not args.assume_in_merge: return 0`. It only checks while `MERGE_MSG` exists together with `MERGE_HEAD` or an in-progress rebase [E, [`check_merge_conflict.py` @3e8a870](https://github.com/pre-commit/pre-commit-hooks/blob/3e8a8703264a2f4a69428a0aa4dcb512790b2c8c/pre_commit_hooks/check_merge_conflict.py), read 2026-09-26]. So as specified, it would not have caught the case §3 names: a half-resolved file committed from a parallel worktree. T10 **failed** on the spec's config and passes with the fix [E, RESULTS.md T10]. **Fix confirmed.** Its cost: a line of exactly seven `=` characters (a Markdown setext underline of that length) now fails the hook [E, the patterns in the same file]. That is acceptable.
> 2. **`--max-decode-depth` defaults to 5, not 0, and CI must use 5.** *Was:* §5.2 said decode and archive depth both *"default to 0"*, and that decoding was enabled "in CI only, not in the hook". *Why it was wrong:* I cited the README at the tag, which does say `default "0"`. **The code at the same tag says otherwise**: `rootCmd.PersistentFlags().Int("max-decode-depth", 5, …)`. The archive depth really is 0 [E, [`cmd/root.go` @83d9cd6, L91–92](https://github.com/gitleaks/gitleaks/blob/83d9cd684c87d95d656c1458ef04895a7f1cbd8e/cmd/root.go#L91), read 2026-09-26]. So the hook already decodes to depth 5, and a base64-encoded key inside JSON was blocked by the hook [E, RESULTS.md D-3]. My CI value of 2 would have made CI **weaker** than the hook, the opposite of what I intended. **Fix confirmed:** CI uses `--max-decode-depth=5`. *Lesson, adopted as practice:* for a pinned binary, flag defaults are read from the source at the pinned SHA, not from the README.
> 3. **T2 answered: gitleaks' path rules never fire on binary files, whether staged (hook) or in history (CI)** [E, RESULTS.md §5, tested with gitleaks 8.30.1; the same rule fired on a text `.pem` as a control]. So for keystores, and for any other binary signing material such as `.p12` and `.mobileprovision`, **the local filename hook and CI's filename step are the only controls.** §3 and §5.2 called that design belt and braces. It is load-bearing. **New residual gap** [I, from this finding]: a binary keystore *inside an archive* (`.zip`, `.tar.gz`) is caught by neither control. The filename rules don't match archive names, and `--max-archive-depth` extracts into path rules that skip binaries. Flagged in §12. It is not a precondition for the first push.
> 4. **Confirmed by testing, previously inferred:** gitleaks keywords are case-insensitive (T4) [E, RESULTS.md]. Hooks run from a git worktree (T13). Hook and CI output is redacted (T11: 46 outputs checked against every generated value, none present).
> 5. **Accepted non-security departures:** the `SECURITY.md` placeholder reads *"TBD — CEO decision pending"*. `CLAUDE.md` carries a one-line heading above §8.3's text. `.claude/settings.json` is committed, as §8.3 allowed. Everything else in `haunts` commit `0f8bfa4` matches this spec's code blocks **line for line** [E, checked mechanically by me against the working tree of `/Users/davidparrish/Documents/haunts`, 2026-09-26].
>
> **Still open after testing:** T14 (first push: `secret-scan` green, including the checksum step, which was not run locally) and T15 (the Claude Code deny rules, which need an interactive session).

**Slug:** `haunt` · **Product name:** Haunts (D9) · **Answers:** D29 (*"Referred to the **CSO**, whose charter covers secret hygiene, to specify the baseline"*) and the CVO's two additions recorded under it.
**Decisions bearing on it:** D27 (separate repo `deopea-david/haunts`), D28 (private now, public later), D29 (secret scanning before any code), D12 and the product's "nothing leaves the device" promise (relevant to §8.4), and the stack in `android-and-stack-note.md` (React Native + Expo, Swift and Kotlin capture modules).

**Template note.** `pipeline/templates/` holds nine templates and none is a security specification or threat model [E, listed from disk 2026-09-26]. This note follows the eight questions put to this seat, in their order, and adds the charter's overturn clause (§12). I say so here so the change of format is visible.

**Method.** Every version, SHA, checksum, price, plan entitlement and vendor statement below was retrieved during this session, on **2026-09-26**, and the link travels with the claim. Versions and commit SHAs were read from the GitHub API for each project (`gh api repos/<owner>/<repo>/releases/latest` and `.../commits/<tag>`), which is the primary source. Where I relied on training knowledge I tag it [K] and say how confident I am. **Nothing is cited from memory.**

**What I did not do.** I did not install gitleaks, trufflehog or anything else (instruction: the orchestrator installs after CEO approval). So **no config in this note has been executed**. Every config is written against the retrieved documentation, and §11 lists the acceptance tests that must pass before the first commit is made. The `candour` history check (§10) was therefore a pattern search, not a gitleaks run.

---

## 0. The answers, before the working

1. **Tools: gitleaks v8.30.1, run by the `pre-commit` framework v4.6.x, with three cheap hooks from `pre-commit-hooks` v6.0.0 and one local filename block.** gitleaks is MIT-licensed, ships an official pre-commit hook, redacts by default in that hook, needs no network, and works the same on JS, Swift and Kotlin because it scans text diffs, not languages. Revs are pinned by **commit SHA**, not tag.
2. **The CVO's first point is confirmed, and it is stronger than it was put.** While `haunts` is private, **GitHub gives it no secret scanning and no push protection at all**. GitHub's secret scanning covers user-owned private repositories only on Enterprise Managed Users or Enterprise Server [E, §6]. So during the private phase, **the CI job is the only server-side control there is**, not a backstop to another one.
3. **CI: do not use `gitleaks-action`.** It needs no licence key for a personal account [E]. But it is under a proprietary EULA (*"All Rights Reserved"*), it runs a gitleaks version hard-coded in the action rather than the one we pin, and it was built to comment on PRs. The workflow in §5 downloads the same gitleaks binary the hook uses, checks its SHA-256 against the published checksum, and scans **all history on every push and PR**. That costs about one Actions minute a run [J], inside the free 2,000 a month [E].
4. **The CVO's second point is confirmed and widened.** A full-history scan is a condition of going public. It must also cover things `git log` does not see. PR refs survive force-pushes on GitHub [E]. **Actions logs become visible to everyone** when a repo goes public [E]. And issue and PR text is not scanned at all. §9 gives the procedure. If anything is found: **rotate first, verify the old credential is dead, then rewrite.** Because the repo will still be private at that point, the cheapest clean state may be a fresh repository rather than a scrubbed one. That is a CEO call at the time.
5. **`candour` history check: clean.** I searched all 50 commits on every local and remote ref, including tags and the stash, with 18 patterns (§10). No credentials, private keys, tokens, `.env` files or signing files were found, and nothing was ever committed then deleted. GitHub's own secret scanning and push protection are already **enabled** on `candour`, and GitHub reports **zero** secret-scanning alerts [E, read via the API].
6. **Money: the baseline costs nothing.** Every tool is free and open source, and the CI fits in the free tier. Two things near it *would* cost money, and I flag them without recommending either now. (a) Branch protection or rulesets on a *private* personal repo need GitHub Pro [E]. I recommend not buying it for a short private phase (§6). (b) **If** Haunts ever ships over-the-air updates through EAS Update, signing them needs a paid EAS plan [E]. That is a CTO question with a CSO recommendation attached (§8.4).
7. **Decisions for the CEO.** Only one is needed before the first commit: **approve this baseline** so the orchestrator can install the tools and make the commit. Later there are two more, one at a time: the contact address `SECURITY.md` names for vulnerability reports (it is personal data, so it is his call, §8.2), and at go-public, fresh repo versus GitHub Support if the scan finds anything (§9.3).

---

## 1. What is secret in this repository, who wants it, and how bad it gets

A short threat model, because the tool choices only make sense against it.

**What makes this repo unusual.** Haunts has **no server**. Nothing leaves the device except user-chosen backup to the user's own cloud (STATUS.md, "What Haunts is"). So there are almost no *runtime* secrets: no database password, no API key the app uses to call home. **Nearly every secret this repo will ever touch is a build, signing or distribution credential.** [I, from the stated architecture]

| Secret | What an attacker could do with it | Recovery |
|---|---|---|
| **App Store Connect API key** (`AuthKey_XXXX.p8`, a PEM private key) | Act on the App Store Connect API for the account: builds, TestFlight, metadata. | Revoke in App Store Connect. *"If you suspect a private key is compromised, immediately revoke the key"*. The private key *"is available for download a single time"* [E, [Apple, Creating API keys](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api); [Apple, Revoking API keys](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys)]. Revocation cannot be undone [E, same]. |
| **Android upload keystore** (`.jks` / `.keystore`) and its passwords | Sign builds Google Play will accept as coming from us, if they also have Play Console access. | Resettable. Under Play App Signing, Google holds the app signing key, and a lost or compromised upload key is reset by Google on request [E, [Google Play Console Help, Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en)]. |
| **Apple distribution certificate (`.p12`) and provisioning profiles** | Sign iOS builds as us. | Revoke and reissue in the Apple Developer account [K, high confidence]. |
| **`EXPO_TOKEN`** (Expo personal or robot access token) | *"Anyone with this token can perform actions on your behalf"* [E, [Expo, Programmatic access](https://docs.expo.dev/accounts/programmatic-access/)]. That includes builds and, **if EAS Update is used, publishing an update straight to installed apps** [K, high confidence, see §8.4]. | Delete it from the Expo access-token page, which *"immediately"* blocks it [E, same]. |
| **GitHub tokens** (a PAT in a script, for instance) | Push to the repo, including to the workflow. | Revoke in GitHub settings [K]. |
| `google-services.json` / `GoogleService-Info.plist` | These are Firebase configuration. **Haunts should not have them at all.** See §8.4. | n/a |

**The worst plausible breach.** Someone gets enough signing and distribution credentials to ship a malicious build or update of an app that holds **a person's complete location history**. The whole promise of this product is that this data never leaves the phone, and a poisoned update is the one path that breaks that promise from our side [J]. Everything in this baseline exists to keep those credentials out of the one place that becomes public: git history.

**Who attacks.** (a) Automated harvesting of public repositories for credentials. This is routine, which is why GitHub scans public pushes by default [K, high confidence; GitHub's free public-repo scanning, §6, is the evidence it is considered routine]. (b) Anyone who can read the repo while it is private. That includes collaborators, installed GitHub Apps and the AI agents working in it. (c) A supply-chain compromise of a tool or action we run in CI. Pinning by SHA answers that.

**Three leak channels, not one.** This is the part most baselines miss.
1. **Git history.** It is published in full when the repo goes public (D29).
2. **CI logs.** When a repo goes public, *"Actions history and logs will be visible to everyone"* [E, [GitHub Docs, Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)]. A scanner that prints the secret it found has leaked it a second time. **Every gitleaks call in this note uses `--redact`.**
3. **Agent transcripts.** An AI agent that reads a `.env` file or prints a key sends that value into its context and its logs. **A secret an agent has read counts as leaked**, the same as one in history [J, this seat's rule]. §8.3 has agent rules and Claude Code deny rules for this.

---

## 2. Pre-commit secret scanning: which tool and which hook manager

### 2.1 Scanner

| Candidate | Current release (retrieved) | Licence (retrieved) | Verdict |
|---|---|---|---|
| **gitleaks** | **v8.30.1**, 2026-03-21 [E, [release](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1)] | MIT [E, GitHub API `license.spdx_id`] | **Chosen.** |
| trufflehog | v3.97.9, 2026-09-24 [E, [release](https://github.com/trufflesecurity/trufflehog/releases/tag/v3.97.9)] | **AGPL-3.0** [E, GitHub API] | **Rejected for the hook. Used once, at the go-public gate, as a second opinion** (§9). |
| detect-secrets (Yelp) | v1.5.0, **2024-05-06** [E, [release](https://github.com/Yelp/detect-secrets/releases/tag/v1.5.0)] | Apache-2.0 [E, GitHub API] | **Rejected.** |

**Why gitleaks.**
- **It has an official pre-commit hook, and that hook redacts.** The hook in the gitleaks repo at v8.30.1 runs `gitleaks git --pre-commit --redact --staged --verbose` [E, [`.pre-commit-hooks.yaml` at v8.30.1](https://github.com/gitleaks/gitleaks/blob/v8.30.1/.pre-commit-hooks.yaml)]. `--redact` matters here more than usual, because an agent running `git commit` reads the hook's output (§1, channel 3).
- **It covers this stack's formats out of the box.** Its default config at v8.30.1 has 222 rules [E, counted in [`config/gitleaks.toml` at v8.30.1](https://github.com/gitleaks/gitleaks/blob/v8.30.1/config/gitleaks.toml)]. They include `private-key`, which is what an App Store Connect `.p8` is, `pkcs12-file`, a **path** rule for `.p12`/`.pfx` files, `gcp-api-key`, which catches the `AIza…` key in a Firebase config, `github-pat` and `github-fine-grained-pat`, `npm-access-token`, `anthropic-api-key`, `openai-api-key`, `jwt`, and `generic-api-key` [E, same file].
- **It has gaps, and §4.2 fills them.** There is **no Expo rule** and **no rule for Java keystores** (`.jks`/`.keystore`) or provisioning profiles [E, searched the same file]. The custom `.gitleaks.toml` adds these. *(Correction 1: for binary files, gitleaks' path rules never fire, so keystores are caught only by the filename hook and CI's filename step. See §3.)*
- **It is language-agnostic.** It scans `git log -p` patches [E, [README at v8.30.1](https://github.com/gitleaks/gitleaks/blob/v8.30.1/README.md): *"Under the hood, gitleaks uses the `git log -p` command to scan patches"*]. So JS, Swift, Kotlin, Gradle, plists and JSON are all just text to it.
- **The same binary runs locally, in CI and at the go-public gate,** with the same config. One engine, one set of rules, one version to keep in step (§5.3).
- **It needs no network.** It sends nothing anywhere.

**Why not trufflehog in the hook.** Its distinguishing feature is **verification**. *"A verified result means TruffleHog confirmed the credential is valid by testing it against the service's API"* [E, [README at v3.97.9](https://github.com/trufflesecurity/trufflehog/blob/v3.97.9/README.md)]. On every commit, that means network calls carrying candidate secrets to their issuers. That is slow, and it answers a question we don't ask, because **we rotate regardless of whether a leaked key still works** (§9.3). Its AGPL-3.0 licence is not a problem for running it locally [J, not legal advice; Constitution 6.1 applies to licence interpretation]. But as a *second, independent engine at the go-public gate*, run with `--no-verification` (a documented flag, [E, same README]), it is worth its one-off cost. Two engines with separate rule sets are two sources in the evidence standard's sense. Two runs of the same engine are one.

**Why not detect-secrets.** Its last release is more than two years old [E, above]. Its model is a committed `.secrets.baseline` file of known findings. That baseline is itself a place for an agent to "fix" a failing hook by adding the finding to it [J]. gitleaks has the same risk through `.gitleaksignore` and `gitleaks:allow`, and §4.2, §5 and §8.3 close it off. detect-secrets would add a second suppression mechanism for no gain.

### 2.2 Hook manager

| Candidate | Current release (retrieved) | Verdict |
|---|---|---|
| **`pre-commit` framework** | **v4.6.2**, 2026-08-10 [E, [release](https://github.com/pre-commit/pre-commit/releases/tag/v4.6.2)] | **Chosen.** |
| lefthook | v2.1.14, 2026-09-14 [E, [release](https://github.com/evilmartians/lefthook/releases/tag/v2.1.14)], MIT | Rejected, narrowly. |
| husky | not retrieved | Rejected. |

**Why `pre-commit`.**
- **It pins the scanner's version in the repo, not on the machine.** The hook's `rev` fixes which gitleaks runs, and with `language: golang` pre-commit builds that exact version. *"new in 3.0.0: pre-commit will bootstrap `go` if it is not present"* [E, [pre-commit.com](https://pre-commit.com/)]. With lefthook or husky, the hook runs whatever `gitleaks` is on the PATH, so two machines, or an agent's sandbox, can quietly run different rule sets [I].
- **Revs can be frozen to SHAs.** *"pre-commit assumes that the value of `rev` is an immutable ref (such as a tag or SHA)"*, and `autoupdate --freeze` will *"Store 'frozen' hashes in `rev` instead of tag names"* [E, pre-commit.com]. Tags can be moved. SHAs cannot.
- **It has a built-in way to forbid files by name.** `language: fail` is *"A lightweight language to forbid files by filename"* [E, pre-commit.com]. §3 uses it.
- **It is already on this machine.** But only under a pyenv interpreter, not on the default PATH. `pre-commit --version` fails in a plain shell, and `PYENV_VERSION=3.14.5 pre-commit --version` reports **4.6.0** [E, run locally 2026-09-26]. Homebrew's formula is 4.6.2 [E, `brew info`]. **The orchestrator must put one or the other on the PATH** before `pre-commit install`, or the hook won't run in agent shells.
- **It covers git worktrees.** Hooks live in the shared git directory. Inside a worktree of `candour`, `git rev-parse --git-path hooks` returns the main clone's `.git/hooks` [E, run locally]. So one `pre-commit install` in the main clone covers every agent worktree [I, from that result].

**Why not husky.** It installs through an npm `prepare` script, so it needs a `package.json` before it can guard anything. The first commit in D29 comes **before** any product code. It also runs whatever scanner is on the PATH (same objection as above) [J].

**Why lefthook was close.** It is fast, a single binary, and can auto-install from an npm devDependency, which is the one thing `pre-commit` lacks: a fresh clone is unguarded until someone runs `pre-commit install` [K, high confidence]. That gap is real. **The CI job closes it**, and the agent rules require `pre-commit install` as the first step in any clone (§8.3). If the CTO later prefers lefthook for build hooks, the security baseline can move with it. What must not change is the pinned gitleaks version and the CI job [J].

**Residual risk, stated plainly.** Every local hook can be skipped. The gitleaks README says so itself: prefix `SKIP=gitleaks` to the commit [E, [README at v8.30.1](https://github.com/gitleaks/gitleaks/blob/v8.30.1/README.md)]. `git commit --no-verify` skips them all [K, certain]. Local hooks catch mistakes. They cannot stop a determined or careless bypass. That is the CVO's point, and §5 is the answer.

---

## 3. Other cheap hooks at pre-commit: what's in, what's out

The bar is: cheap (well under a second on a normal commit), deterministic, and **security-relevant or history-relevant**. History-relevant counts because everything committed will be published (D28).

| Hook | In/out | Why |
|---|---|---|
| `gitleaks` (gitleaks v8.30.1) | **In** | The scanner (§2). |
| `detect-private-key` (pre-commit-hooks v6.0.0) | **In** | *"Checks for the existence of private keys"* [E, [pre-commit-hooks README at v6.0.0](https://github.com/pre-commit/pre-commit-hooks/blob/v6.0.0/README.md)]. It duplicates gitleaks' `private-key` rule **deliberately**. The most damaging secret in this stack is a PEM private key (the `.p8`), and the gitleaks rule needs the whole block: header, at least 64 body characters, and footer [E, `private-key` regex in `config/gitleaks.toml` at v8.30.1]. A truncated or partly pasted key slips past that and is still a leak. A second, independent implementation costs nothing [J]. |
| **`forbid-signing-and-credential-files`** (local, `language: fail`) | **In** | Blocks by **filename**: keystores, `.p8`/`.p12`/`.pfx`, provisioning profiles, `.pem`/`.key`/`.cer`, `credentials.json`, `google-services.json`, `GoogleService-Info.plist`, `.env*` except `.env.example`. **Why a filename check as well as gitleaks:** a keystore is **binary**. *(Correction 1: tested, and this check is not a spare. gitleaks' path rules **never fire on binary files**, staged or in history [E, RESULTS.md T2, gitleaks 8.30.1]. For `.jks`/`.keystore`/binary `.p12`/`.mobileprovision`, this hook is the **only** local control, and CI's filename step is the only server-side one.)* |
| `check-added-large-files` (`--maxkb=1024`) | **In** | *"Prevents giant files from being committed"* [E, pre-commit-hooks README]. History-relevant: a binary committed once is in history for good. Haunts has a ~0.8 GB optional map store (D22) and a 2.85 GB source tile file (`map-tiles-note.md`). Neither must ever enter git. I set 1 MB rather than the 500 kB default so that app icons and splash images fit [J]. The CTO may tune it. |
| `check-merge-conflict` **with `--assume-in-merge`** *(Correction 1)* | **In** | *"Check for files that contain merge conflict strings"* [E, same]. Without `--assume-in-merge` it checks only while a merge is in progress, so it would miss the case below [E, source at the pinned SHA; see Correction 1]. Cheap. With several agents on parallel worktrees, conflict markers are a realistic way for a broken file, or a half-resolved one that kept both sides of a config, to be committed [J]. |
| `detect-aws-credentials` | Out | No AWS in this stack. |
| `no-commit-to-branch` | Out, **flagged to CTO/PM** | It would stand in locally for branch protection, which a Free private repo can't have (§6). But it blocks the first commit on `main` unless skipped, and a baseline that starts by telling someone to use `SKIP=` teaches the wrong habit [J]. It is a workflow choice, not a secret control. |
| `forbid-submodules` | Out, **flagged to CTO** | Submodules pull outside code in without review. That is a supply-chain point, but it is not about secrets. |
| `check-case-conflict`, `check-json`, `check-yaml`, `end-of-file-fixer`, formatters, linters | Out | Not security. They belong to the CTO's engineering standards, not this baseline. |
| `npm audit` / dependency scanning at pre-commit | Out | Slow, needs the network, and noisy. Dependabot alerts cover it at no cost (§6). |
| trufflehog, detect-secrets as extra hooks | Out | §2.1. |

---

## 4. The config files for the first commit

All four files below go in the **first commit** of `haunts`, together with `.gitignore` (§7), `SECURITY.md` and the agent rules (§8), and the CI workflow (§5). **None has been executed yet.** §11 lists the tests that must pass before the commit is made.

### 4.1 `.pre-commit-config.yaml`

Revs are frozen to the commit SHAs the release tags point to. I read these from the GitHub API on 2026-09-26: `gitleaks/gitleaks` tag `v8.30.1` → `83d9cd684c87d95d656c1458ef04895a7f1cbd8e`, and `pre-commit/pre-commit-hooks` tag `v6.0.0` → `3e8a8703264a2f4a69428a0aa4dcb512790b2c8c` [E, `gh api repos/<repo>/commits/<tag>`]. The `# frozen:` comment is the format `pre-commit autoupdate --freeze` writes [K, high confidence], so a later `autoupdate --freeze` keeps the style.

```yaml
# .pre-commit-config.yaml: haunts security baseline (CSO, 2026-09-26).
# Local hooks catch mistakes. They can be skipped, so CI repeats the scan
# (.github/workflows/secret-scan.yml). Changing this file needs a CSO note
# and CEO approval (SECURITY.md). Never commit with --no-verify or SKIP=.
minimum_pre_commit_version: "4.6.0"
default_install_hook_types: [pre-commit]

repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: 83d9cd684c87d95d656c1458ef04895a7f1cbd8e  # frozen: v8.30.1
    hooks:
      - id: gitleaks            # gitleaks git --pre-commit --redact --staged --verbose

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: 3e8a8703264a2f4a69428a0aa4dcb512790b2c8c  # frozen: v6.0.0
    hooks:
      - id: detect-private-key
      - id: check-added-large-files
        args: ["--maxkb=1024"]
      - id: check-merge-conflict
        # Without --assume-in-merge this hook checks only while a merge is in
        # progress, so a staged file with conflict markers would pass.
        args: ["--assume-in-merge"]

  - repo: local
    hooks:
      - id: forbid-signing-and-credential-files
        name: Forbid signing material and credential files
        language: fail
        entry: >-
          Signing material or a credential file is staged. It must never enter
          this repository, because every commit becomes public (D28). Unstage it,
          keep it outside the repo, and see SECURITY.md.
        files: '(?i)(^|/)(\.env(\.[^/]*)?|credentials\.json|google-services\.json|googleservice-info\.plist|[^/]+\.(jks|keystore|p8|p12|pfx|mobileprovision|provisionprofile|pem|key|cer|der|certsigningrequest))$'
        exclude: '(?i)(^|/)\.env\.example$'
```

Notes on it:
- The `gitleaks` hook uses `language: golang`. It builds gitleaks v8.30.1 from source the first time. The first install took about 24 s [E, RESULTS.md §2]. Go is installed on this machine (`/opt/homebrew/bin/go`) [E, `which go`], and pre-commit would bootstrap Go anyway [E, §2.2].
- The hook finds `.gitleaks.toml` by itself. gitleaks' config precedence ends with *"(target path)/.gitleaks.toml"* [E, [README at v8.30.1](https://github.com/gitleaks/gitleaks/blob/v8.30.1/README.md)]. **An environment variable (`GITLEAKS_CONFIG` or `GITLEAKS_CONFIG_TOML`) outranks the file** [E, same]. So an agent could point the hook at an empty config. That is why CI passes `--config` explicitly, and why §8.3 forbids setting those variables.

### 4.2 `.gitleaks.toml`

It extends the built-in rules rather than replacing them. *"useDefault will extend the default gitleaks config built in to the binary"* [E, README at v8.30.1]. Consequence: **the rule set is whatever the pinned binary carries**, which is why the version is pinned in two places and must be bumped in both together (§5.3). Path-only rules are a documented pattern: the default config's own `pkcs12-file` rule is a `path` with no `regex` [E, `config/gitleaks.toml` at v8.30.1]. The allowlist syntax is the v8.21+ `[[rules.allowlists]]` form [E, README]. gitleaks uses Go regular expressions, which **do not support look-ahead** [K, certain], so `.env.example` is allowed through a rule allowlist rather than a negative look-ahead.

```toml
# .gitleaks.toml: haunts secret-scanning rules (CSO, 2026-09-26).
# Extends gitleaks' built-in rules for the pinned version (v8.30.1).
# Changes need a CSO note and CEO approval (SECURITY.md). No global
# allowlists, and no .gitleaksignore: CI fails if one exists.

title = "haunts"

[extend]
useDefault = true

# Keystores, Apple API keys, certificates and provisioning profiles, by path.
# Keystores are binary, so content rules cannot see them.
[[rules]]
id = "haunts-signing-material"
description = "Signing material or platform key file. It lives outside the repo (SECURITY.md)."
path = '''(?i)(?:^|/)[^/]+\.(?:jks|keystore|p8|p12|pfx|mobileprovision|provisionprofile|pem|key|cer|der|certsigningrequest)$'''
tags = ["haunts", "signing"]

# EAS local credentials and cloud-SDK config. Haunts has no backend, so a
# Firebase or Google config file here is a finding in its own right.
[[rules]]
id = "haunts-credential-file"
description = "Credential or cloud-SDK configuration file."
path = '''(?i)(?:^|/)(?:credentials\.json|google-services\.json|googleservice-info\.plist|service-account[^/]*\.json)$'''
tags = ["haunts", "credentials"]

# .env files. Only .env.example, holding placeholders, may be committed.
[[rules]]
id = "haunts-dotenv-file"
description = ".env file. Only .env.example (placeholders only) may be committed."
path = '''(?i)(?:^|/)\.env(?:\.[^/]*)?$'''
tags = ["haunts", "dotenv"]
    [[rules.allowlists]]
    description = "The placeholder template"
    paths = ['''(?i)(?:^|/)\.env\.example$''']

# gitleaks has no Expo rule. A literal EXPO_TOKEN value is a finding;
# a reference such as ${{ secrets.EXPO_TOKEN }} is not, because '$' is excluded.
[[rules]]
id = "haunts-expo-token"
description = "EXPO_TOKEN written as a literal. Use an EAS or GitHub Actions secret."
regex = '''EXPO_TOKEN\s*[:=]\s*["']?([A-Za-z0-9_\-]{20,})'''
keywords = ["expo_token"]
tags = ["haunts", "expo"]

# npm auth token written literally in .npmrc (a ${NPM_TOKEN} reference is fine).
[[rules]]
id = "haunts-npmrc-literal-token"
description = "Literal npm auth token in .npmrc. Use ${NPM_TOKEN}."
regex = '''_authToken\s*=\s*([^\s$][^\s]{7,})'''
keywords = ["_authtoken"]
tags = ["haunts", "npm"]

# Keystore and certificate passwords written as quoted literals in Gradle,
# Kotlin DSL or JSON. System.getenv(...) and ${VAR} do not match.
[[rules]]
id = "haunts-signing-password"
description = "Keystore or certificate password written as a literal."
regex = '''(?i)\b(?:storePassword|keyPassword|keystorePassword)\b["']?\s*[:=]?\s*["']([^"'$\s]{6,})["']'''
keywords = ["storepassword", "keypassword", "keystorepassword"]
tags = ["haunts", "signing"]

# React Native's gradle.properties convention, e.g. MYAPP_UPLOAD_STORE_PASSWORD=...
[[rules]]
id = "haunts-gradle-properties-password"
description = "Signing password in gradle.properties. Keep it in ~/.gradle/gradle.properties or the keychain."
regex = '''(?i)\b[A-Z0-9_]*(?:STORE|KEY)_PASSWORD\s*=\s*([^\s$]{6,})'''
keywords = ["store_password", "key_password"]
tags = ["haunts", "signing"]
```

**Keywords.** gitleaks uses keywords as a quick pre-filter [E, README: *"Rules that contain keywords will perform a quick string compare check"*]. I have written them in lower case because the built-in rules do: `gcp-api-key` matches `AIza…` with the keyword `"aiza"` [E, `config/gitleaks.toml`]. From that I infer the comparison is case-insensitive [I]. *(Correction 1: confirmed by T4. The lower-case `expo_token` keyword matched upper-case text [E, RESULTS.md].)*

*(Correction 1)* **The three path rules above fire only on text files.** gitleaks' path rules never fire on binary files [E, RESULTS.md T2]. They still earn their place: they catch `.pem` files, text-format `.p8` keys, `.env` files, `credentials.json` and `google-services.json`. The comment above `haunts-signing-material` says "content rules cannot see" keystores. In fact no gitleaks rule can. The committed file keeps that comment, because it is accurate as far as it goes, and this note is the record.

---

## 5. The CI backstop

### 5.1 Why not `gitleaks/gitleaks-action`

The question put to me: does the action need a licence for a personal account's private repo? **No.** The README says `GITLEAKS_LICENSE` is *"required for organizations, not required for user accounts"*, and the EULA's opening terms say *"If you are using the Software to scan repositories owned by a Personal Account… then no License Key is required"* [E, [gitleaks-action README at v3.0.0](https://github.com/gitleaks/gitleaks-action/blob/v3.0.0/README.md); [LICENSE.txt at v3.0.0](https://github.com/gitleaks/gitleaks-action/blob/v3.0.0/LICENSE.txt)]. The current release is **v3.0.0**, 2026-05-30, which moved to Node 24; v2 *"will stop working"* from 2026-09-16 [E, same README].

**I still recommend against it**, for four reasons:
1. **It is not open source.** Since v2.0.0 it is under the *"GITLEAKS-ACTION END-USER LICENSE AGREEMENT"*, *"Copyright © 2022 Gitleaks LLC - All Rights Reserved"*. The EULA bars modification and says licence-key requirements *"are automatically enforced by the Software"* [E, same]. The CLI it wraps is MIT (§2.1). Nothing is gained by taking on a proprietary EULA to call an MIT binary. Candour's company default leans to open source (LICENSE.md presumes open source for product code) [J; that presumption is about our code, not our tools, so this is my judgment, not a rule].
2. **It runs a gitleaks version of its own choosing.** `GITLEAKS_VERSION` *"Defaults to a hard-coded version number"* [E, same]. Our rule set is whatever binary runs (§4.2), so CI must run exactly the version the hook runs.
3. **It phones home for organisation accounts.** It sends licence-validation data to keygen.sh [E, same]. That doesn't apply to a personal account today. It would if `haunts` ever moved to an organisation, and the terms could change [J].
4. **Its PR comments and SARIF upload are not wanted.** The README itself advises against its code-scanning use: *"it gives a false sense of security"* because an alert shows resolved while *"the secret is still visible in the commit history"* [E, same]. That is exactly the point of D29.

### 5.2 `.github/workflows/secret-scan.yml`

`actions/checkout` is pinned to **v7.0.1** → `3d3c42e5aac5ba805825da76410c181273ba90b1` [E, [release](https://github.com/actions/checkout/releases/tag/v7.0.1); SHA from `gh api repos/actions/checkout/commits/v7.0.1`]. GitHub's own hardening guidance: *"Pinning an action to a full-length commit SHA is currently the only way to use an action as an immutable release"* [E, [GitHub Docs, Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)]. `fetch-depth: 0` *"fetch[es] all history for all branches and tags"*. `persist-credentials: false` opts out of leaving the token in git config [E, [checkout README at v7.0.1](https://github.com/actions/checkout/blob/v7.0.1/README.md)].

gitleaks is downloaded from its GitHub release and checked against the published checksum. For `gitleaks_8.30.1_linux_x64.tar.gz` that is `551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb`. It matches both the release's `gitleaks_8.30.1_checksums.txt` and the digest GitHub reports for the asset [E, [checksums file](https://github.com/gitleaks/gitleaks/releases/download/v8.30.1/gitleaks_8.30.1_checksums.txt); `gh api .../releases/tags/v8.30.1`].

```yaml
# .github/workflows/secret-scan.yml: haunts security baseline (CSO, 2026-09-26).
# The backstop for local hooks, which can be skipped (--no-verify, SKIP=, or a
# clone without `pre-commit install`). While haunts is private, GitHub provides
# no secret scanning for it, so this job is the only server-side check.
# It scans ALL history on every push and PR. Output is redacted, because Actions
# logs become public when the repository does.
# Changing this file needs a CSO note and CEO approval (SECURITY.md).
name: secret-scan

on:
  push:
  pull_request:
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: secret-scan-${{ github.ref }}
  cancel-in-progress: true

jobs:
  gitleaks:
    name: gitleaks (full history)
    runs-on: ubuntu-24.04
    timeout-minutes: 10
    env:
      GITLEAKS_VERSION: "8.30.1"   # keep in step with .pre-commit-config.yaml
      GITLEAKS_SHA256: "551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb"  # linux_x64, from gitleaks_8.30.1_checksums.txt
    steps:
      - name: Check out all history, branches and tags
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Install gitleaks (pinned version, checksum verified)
        run: |
          set -euo pipefail
          curl -sSfL -o "$RUNNER_TEMP/gitleaks.tar.gz" \
            "https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz"
          echo "${GITLEAKS_SHA256}  $RUNNER_TEMP/gitleaks.tar.gz" | sha256sum --check --strict
          tar -xzf "$RUNNER_TEMP/gitleaks.tar.gz" -C "$RUNNER_TEMP" gitleaks
          "$RUNNER_TEMP/gitleaks" version

      - name: No suppression file
        run: |
          if [ -e .gitleaksignore ]; then
            echo "::error::.gitleaksignore is not permitted in this repository (SECURITY.md)."
            exit 1
          fi

      - name: No signing or credential file anywhere in history
        run: |
          set -euo pipefail
          hits="$(git log --all --name-only --format= | sort -u \
            | grep -Ei '(^|/)(\.env(\.[^/]*)?|credentials\.json|google-services\.json|googleservice-info\.plist|[^/]+\.(jks|keystore|p8|p12|pfx|mobileprovision|provisionprofile|pem|key|cer|der|certsigningrequest))$' \
            | grep -Eiv '(^|/)\.env\.example$' || true)"
          if [ -n "$hits" ]; then
            echo "::error::Signing or credential file(s) in history. Treat as leaked: rotate first (SECURITY.md)."
            echo "$hits"
            exit 1
          fi

      - name: Scan all history for secrets (redacted)
        run: |
          # --max-decode-depth=5 is the v8.30.1 binary's real default (cmd/root.go;
          # its README says 0), so the hook decodes to 5. Lower would make CI weaker.
          "$RUNNER_TEMP/gitleaks" git . \
            --config .gitleaks.toml \
            --log-opts="--all" \
            --redact \
            --ignore-gitleaks-allow \
            --max-decode-depth=5 \
            --max-archive-depth=2 \
            --no-banner \
            --verbose
```

**Design choices, each deliberate:**
- **All history on every run, not just the new commits.** The repo is small and gitleaks reads `git log -p`, so this should take seconds [J; to be confirmed on the first run]. It means **the go-public scan is running continuously**, and a secret committed and then deleted on a branch is still caught. When the repo is large enough for this to cost real minutes, switch to a range scan plus a weekly full scan [J].
- **The filename step is separate from gitleaks, and it is the only CI control for binary signing material.** *(Correction 1: gitleaks' path rules never fire on binary files in history [E, RESULTS.md T2]. A `.jks` committed with `--no-verify` was caught by this step alone.)* It prints filenames only, never contents.
- **`--ignore-gitleaks-allow` makes CI stricter than the hook.** It is a documented flag: *"ignore gitleaks:allow comments"* [E, README]. A `gitleaks:allow` comment passes locally and **fails in CI**. That is intended. The only legitimate way to accept a false positive is a reviewed allowlist entry in `.gitleaks.toml`, with CEO approval (§8.2).
- **`--max-decode-depth=5` and `--max-archive-depth=2`.** *(Correction 1. This bullet originally said both default to 0, citing the README, and set decode depth to 2 "in CI only". That was wrong.)* In the pinned binary, decode depth **defaults to 5** and archive depth to 0 [E, [`cmd/root.go` @83d9cd6](https://github.com/gitleaks/gitleaks/blob/83d9cd684c87d95d656c1458ef04895a7f1cbd8e/cmd/root.go#L91)]. So the hook already decodes a base64-encoded `.p8` in JSON, and CI states 5 explicitly so the two stay equal. Archive traversal is on in CI only. It catches *text* secrets inside archives, but **not a binary keystore inside an archive**, because path rules skip binaries [I, from T2]. See §12.
- **`permissions: contents: read`, no secrets and no `pull_request_target`.** The job needs nothing else. After go-public, a fork's PR runs with no access to secrets [K, high confidence], and this job has none to give.
- **No scheduled run.** The rules are pinned, so re-scanning unchanged history finds nothing new. Scans happen on change.

**Cost.** GitHub Free for personal accounts includes *"2,000 minutes per month"* of Actions, and Actions usage *"is free for standard GitHub-hosted runners in public repositories"* [E, [GitHub Docs, GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)]. At about one minute a run [J], that is roughly 2,000 pushes a month while private, and free once public.

### 5.3 Keeping the pins current: `.github/dependabot.yml`

```yaml
# .github/dependabot.yml: keep SHA-pinned actions current (CSO baseline).
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

GitHub recommends Dependabot for keeping referenced actions current [E, [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)]. The file syntax is from training [K, high confidence]. Validate it on first push: GitHub flags an invalid `dependabot.yml` in the repo's Insights → Dependency graph → Dependabot tab [K].

**The gitleaks version is pinned in two places, and Dependabot updates neither.** One is the `rev` in `.pre-commit-config.yaml`. The other is `GITLEAKS_VERSION` + `GITLEAKS_SHA256` in the workflow. **Rule: bump them together in one PR.** Take the new SHA-256 from that release's `_checksums.txt`, and run `pre-commit autoupdate --freeze --repo https://github.com/gitleaks/gitleaks`. Check quarterly, and on any gitleaks security advisory [J].

---

## 6. GitHub-side protections: private personal repo versus public

`deopea-david` is a **personal (User) account** [E, `gh api user` → `"type":"User"`]. The API did not return the plan (`plan: null`, most likely a token-scope limit), so **I could not confirm Free or Pro** [E, same call]. The table assumes Free, and notes where Pro changes the answer.

| Protection | `haunts` while **private** (personal account, Free) | `haunts` once **public** | Source |
|---|---|---|---|
| **Secret scanning** | **Not available.** User-owned repositories get it only on *"GitHub Enterprise Cloud with Enterprise Managed Users"* or Enterprise Server. Pro does not change this. | **Free and automatic.** *"Public repositories: Secret scanning runs automatically for free."* | [E, [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)] |
| **Push protection (repository-level)** | **Not available** [I: it is a secret-scanning feature, and secret scanning is unavailable, per the row above]. | Available, off by default: it *"Is disabled by default, and can be enabled by a repository administrator"*. `candour`, a public personal repo, has it **enabled** [E, API], which shows it is available on this account for public repos. | [E, [Push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection)] |
| **Push protection for users** (account-level) | **Does not cover it.** It *"Stops you from pushing secrets to public repositories on GitHub"*. Private repos are outside it. | On: it *"Is enabled by default"*. | [E, same page] |
| **Dependabot alerts** | **Available on Free**: the plan lists *"Dependabot alerts"*. Must be switched on in settings [K]. | Available. | [E, [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)] |
| **Branch protection / rulesets** (e.g. require `secret-scan` to pass before merging to `main`) | **Not available on Free.** Protected branches for private repos are a Pro feature. *"Rulesets are available in public repositories with GitHub Free… and in public and private repositories with GitHub Pro, GitHub Team, and GitHub Enterprise Cloud."* | **Available free.** | [E, [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans); [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)] |
| **Actions minutes** | 2,000/month on Free (3,000 on Pro). | Free for standard runners. | [E, [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)] |
| **Actions logs** | Visible to collaborators. | *"Actions history and logs will be visible to everyone."* | [E, [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)] |
| **Code scanning (CodeQL), private vulnerability reporting** | Not in scope of this baseline. | Free for public repos [K, high confidence]. Turn on private vulnerability reporting at go-public so `SECURITY.md` has a private route [J]. | [K] |

**What this means.**
- **While private, the only server-side secret check is our own CI job.** GitHub adds nothing. That is why I call the CVO's CI point necessary, not merely prudent.
- **While private, "CI must pass before merge" cannot be enforced on Free.** CI still runs and still goes red. It just can't *block* a merge. The CEO and the agent rules (§8.3) enforce "don't merge on red". **I do not recommend buying Pro for this** [J]: the private phase is meant to be short, there is one human committer, and a red scan on `main` is visible and fixable before going public, which is the moment that matters. *Overturn:* if the private phase runs for many months, or several people get write access, Pro's rulesets become worth their cost. **I could not retrieve Pro's price.** The pricing page as fetched lists Free, Team and Enterprise only [E, [github.com/pricing](https://github.com/pricing)].
- **Switch on at go-public, in this order** (§9.4): secret scanning (automatic), repo push protection, a ruleset on `main` requiring the `secret-scan` check and blocking force-pushes, Dependabot alerts, and private vulnerability reporting.

---

## 7. `.gitignore` entries for credentials and signing material

This is a **convenience, not a control.** `git add -f` overrides `.gitignore` [K, certain]. The hooks and CI are the control. Merge this block with the Expo template's `.gitignore`. That template, read at source, already ignores `*.jks`, `*.p8`, `*.p12`, `*.key`, `*.mobileprovision`, `*.pem` and `.env*.local`, and it also ignores the generated `/ios` and `/android` folders [E, [expo/expo `templates/expo-template-default/gitignore`](https://github.com/expo/expo/blob/main/templates/expo-template-default/gitignore), last changed 2026-05-13 at `d7354e9`]. Expo's own local-credentials guide says: *"Remember to add **credentials.json** and all of your credentials to **.gitignore**"*, naming `android/keystores/release.keystore` and `ios/certs/*` [E, [Expo, Local app credentials](https://docs.expo.dev/app-signing/local-credentials/)].

```gitignore
# ---- Security baseline (CSO, 2026-09-26). See SECURITY.md. ----
# Changing this block needs a CSO note and CEO approval.

# Environment files. Only .env.example (placeholders only) is committed.
.env
.env.*
!.env.example

# Android signing
*.jks
*.keystore
android/keystores/

# Apple signing, certificates and App Store Connect API keys (AuthKey_*.p8)
*.p8
*.p12
*.pfx
*.cer
*.der
*.certSigningRequest
*.mobileprovision
*.provisionprofile
*.pem
*.key
ios/certs/

# EAS local credentials
credentials.json

# Cloud-SDK config. Haunts has no backend; adding one is a CEO decision (SECURITY.md).
google-services.json
GoogleService-Info.plist
service-account*.json

# Machine-local signing properties (keep in ~/.gradle/gradle.properties instead)
local.properties

# Secret-scan reports can contain partial findings
gitleaks-report*.json
trufflehog-report*.json

# Map stores and tile files (D22). Never in git.
*.mbtiles
# ---- end security baseline ----
```

**Where I depart from Expo, and why.** Expo's guide says you *"may choose to commit the default **.env** file"* and ignore only `.env*.local` [E, [Expo, Environment variables](https://docs.expo.dev/guides/environment-variables/)]. **I block every `.env` except `.env.example`.** In a repo that goes public, a committed `.env` invites exactly the edit that leaks: someone adds one real value to the file that is already tracked [J]. Non-secret defaults can live in `app.config.ts` or `.env.example`. *Overturn:* if the CTO shows a build that genuinely needs a committed `.env`, allow that single named file with a CEO-approved allowlist entry.

**Flag to the CTO: `/ios`, `/android` and `debug.keystore`.** If the CTO commits the native folders instead of generating them (continuous native generation), note that React Native's Android template ships a `debug.keystore` [K, high confidence]. The baseline **blocks** it. Generate it locally rather than allowlisting it, because an allowlisted filename is a path by which a real keystore can arrive under that name [J].

---

## 8. Where secrets live instead, and the rules for agents

### 8.1 The map

| Secret | Lives in | Never in |
|---|---|---|
| App Store Connect API key (`.p8`) | Password manager, or macOS Keychain. For EAS Submit, uploaded to **EAS-managed credentials** [K, high confidence that EAS stores ASC API keys]. On disk only briefly, **outside any git working tree**. | The repo, `~/Downloads` left lying, chat, tickets. |
| Android upload keystore + passwords | **EAS-managed credentials** (EAS generates and stores the keystore [K, high confidence]), with a backup copy in the password manager. For local Gradle builds, passwords go in `~/.gradle/gradle.properties`, outside the repo [K, React Native convention]. | `android/`, `gradle.properties` in the repo. |
| Apple distribution certificate, provisioning profiles | EAS-managed credentials [K]. | The repo. |
| Values an EAS build needs | **EAS environment variables with visibility "Secret"**: *"Not readable outside of the EAS servers, including on the website and in EAS CLI."* File values (e.g. a certificate) are supported as file-type variables [E, [Expo, EAS environment variables](https://docs.expo.dev/eas/environment-variables/)]. | `EXPO_PUBLIC_*`. Expo: *"Do not store sensitive info, such as private keys, in `EXPO_PUBLIC_` variables. These variables will be visible in plain-text in your compiled application"* [E, [Expo, Environment variables](https://docs.expo.dev/guides/environment-variables/)]. |
| `EXPO_TOKEN` (only if CI ever runs EAS) | A **GitHub Actions secret**, referenced as `${{ secrets.EXPO_TOKEN }}`. Prefer a **robot** token with a limited role over a personal token: personal tokens let *"Anyone with this token… perform actions on your behalf"*, while robot users *"can only authenticate via an access token"* with role-based permissions [E, [Expo, Programmatic access](https://docs.expo.dev/accounts/programmatic-access/)]. Robot users are an Expo **organisation** feature [E, same]; whether that needs a paid plan I did not retrieve. | Workflow files, `.env`, logs. **Not needed by the baseline**: the secret-scan job uses no secrets. |
| Local developer config that is not secret | `.env.local` (ignored), or `app.config.ts`. | — |

**The macOS Keychain** is fine for passwords. `security add-generic-password` / `find-generic-password` store and read them without leaving them in files [K, high confidence]. For key *files*, a password manager's attachments are easier to back up. What matters is that neither lives inside a working tree [J].

### 8.2 Draft `SECURITY.md` for the `haunts` repository

```markdown
# Security

## Reporting a vulnerability

Please report security problems privately to **[CONTACT: to be decided by the CEO]**.
Please do not open a public issue. Once this repository is public, you can also use
GitHub's private vulnerability reporting (Security tab → Report a vulnerability).

## Secrets never enter this repository

This repository will be made public, and making a repository public publishes every
past commit on every branch, not just the current files. So **no secret may ever be
committed, on any branch, even briefly.** A secret that reaches a commit is treated as
leaked, whether or not the commit was pushed.

Secrets include: App Store Connect API keys (`AuthKey_*.p8`), Android keystores and
their passwords, Apple certificates (`.p12`) and provisioning profiles, EAS `credentials.json`,
Expo access tokens (`EXPO_TOKEN`), GitHub or npm tokens, and any `.env` file other than
`.env.example`. Haunts has no backend, so there should be almost no runtime secrets at all.

Where they live instead: EAS-managed credentials; EAS environment variables with
**Secret** visibility; GitHub Actions secrets; a password manager or the macOS Keychain.
Never inside a working tree. Never in `EXPO_PUBLIC_*` variables, which are compiled
into the app in plain text.

## Guard rails

- **Local hooks.** Run `pre-commit install` once in every clone (worktrees share it).
  The hooks run gitleaks, a private-key check, a large-file check, a merge-conflict
  check, and a block on signing and credential filenames.
- **CI.** `.github/workflows/secret-scan.yml` scans the whole history on every push and
  pull request. **Never merge on a red secret-scan.**
- **Changes to the guard rails** (`.pre-commit-config.yaml`, `.gitleaks.toml`,
  `.github/workflows/secret-scan.yml`, the security block of `.gitignore`, this file)
  need a written note from the CSO seat and the CEO's approval, recorded in the
  decision record in the `candour` repository.

## False positives

Never use `gitleaks:allow` comments (CI ignores them) and never add a `.gitleaksignore`
(CI fails if one exists). Raise the finding instead. If the CSO confirms it is false,
the fix is a narrow allowlist entry in `.gitleaks.toml`, with a comment naming the approval.

## If a secret is committed

1. **Stop.** Do not push. Do not paste the value anywhere, including chat and tickets.
2. **Rotate or revoke it at the issuer first**: App Store Connect (revoke key),
   Play Console (request upload-key reset), Expo (delete token), GitHub (revoke token).
   If the commit was never pushed **and** the value was never shown in any tool or agent
   output, you may drop the commit locally, but rotate anyway if there is any doubt.
3. **Confirm the old credential no longer works**, and check the issuer's activity logs
   for use during the exposure window.
4. **Only then** remove it from history. A human does this, not an agent, using
   `git-filter-repo --sensitive-data-removal`, and contacts GitHub Support for cached
   views and pull-request refs if the commit was pushed.
5. Record what happened in `products/haunt/` in the `candour` repository.
```

**The contact address is a CEO decision.** A reporting address is personal data, and the choice between a personal address, a role address or GitHub's private reporting only is his. Until he chooses, the placeholder stays, and it must be filled before go-public [J].

### 8.3 Agent rules: a section for `haunts/CLAUDE.md` (binding on every seat)

```markdown
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
```

**Enforcement for Claude Code agents: a draft `haunts/.claude/settings.json`.** Claude Code supports `permissions.deny` rules such as `"Read(./.env)"` [E, [Claude Code settings](https://code.claude.com/docs/en/settings)]. **They are best-effort, and the documentation says so.** Read and Edit deny rules apply to the built-in file tools and to *"file commands Claude Code recognizes in Bash, such as `cat`, `head`, `tail`"*, but *"They don't apply to… arbitrary subprocesses that read or write files indirectly, like a Python or Node script"*. For OS-level enforcement it points to the sandbox [E, [Claude Code permissions](https://code.claude.com/docs/en/permissions)]. Bash rules *"match the whole command text, with `*` standing in for any text"* [E, same]. So these rules make a mistake less likely. They do not replace CI.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "deny": [
      "Read(**/.env)",
      "Read(**/.env.local)",
      "Read(**/.env.*.local)",
      "Read(**/.env.production)",
      "Read(**/.env.development)",
      "Read(**/credentials.json)",
      "Read(**/*.p8)",
      "Read(**/*.p12)",
      "Read(**/*.pfx)",
      "Read(**/*.jks)",
      "Read(**/*.keystore)",
      "Read(**/*.mobileprovision)",
      "Read(**/*.pem)",
      "Read(**/*.key)",
      "Read(~/.gradle/gradle.properties)",
      "Bash(git commit *--no-verify*)",
      "Bash(git commit -n*)",
      "Bash(git commit * -n*)",
      "Bash(SKIP=*)",
      "Bash(git -c core.hooksPath*)",
      "Bash(git config *core.hooksPath*)",
      "Bash(pre-commit uninstall*)",
      "Bash(GITLEAKS_CONFIG*)",
      "Bash(git push *--force*)",
      "Bash(git push -f*)",
      "Bash(git filter-repo*)",
      "Bash(git filter-branch*)",
      "Bash(eas credentials*)",
      "Bash(eas env:*)"
    ]
  }
}
```

The patterns are gitignore-style for Read rules [E, same permissions page]. I have not loaded this file, so **each pattern is untested** [I]. The acceptance tests (§11, T15) include checking it with `/status` and a trial denied command. `.env.example` is deliberately *not* denied, so agents can read the template. Whether this file is committed to `haunts` or kept in local settings is the orchestrator's choice. The CEO's approval of this baseline covers either [J].

### 8.4 Two things near this baseline that are not in it: flags

1. **EAS Update (over-the-air JS updates). Flag to the CTO, and to the CFO if adopted.** A token able to publish an update can push new JavaScript to every installed copy **without store review** [K, high confidence]. For an app holding location history, that is the widest blast radius in §1. Expo's end-to-end code signing for updates ensures *"ISPs, CDNs, cloud providers, and even EAS itself cannot tamper with updates"*, but it is *"only available to accounts subscribed to the EAS Production or Enterprise plans"*, and its private key must be stored *"outside of your source control"* [E, [Expo, EAS Update code signing](https://docs.expo.dev/eas-update/code-signing/)]. **My recommendation** [J]: ship v1 with store-reviewed updates only. Adopt EAS Update only with code signing, costed on the cost sheet. `cost-sheet-v3.md` has no EAS line [E, grepped 2026-09-26].
2. **Firebase or any Google config file. Flag to the CEO.** `google-services.json` and `GoogleService-Info.plist` configure Firebase SDKs [K, certain]. Their appearance would mean an SDK that talks to Google servers had been added to a product whose promise is that nothing leaves the device (STATUS.md, "What Haunts is"). That is a user-data-policy change, reserved by Constitution 5.4: *"anything affecting user data policy"*. The baseline blocks the files, so the question has to come to him rather than arrive in a commit.

---

## 9. The go-public gate

**The CVO's point is confirmed, and I make it a precondition of the D28 switch to public.** It is not a *block*. My charter's block covers *"Release — for unresolved material vulnerabilities or absent threat modelling"*, and making a code repository public is not a release to users. **So this is a flag with a procedure attached.** The decision to switch is the CEO's (D28).

Because CI scans full history on every push (§5.2), the gate should find nothing new. What the gate adds is **coverage CI does not have**: PR refs on GitHub, a second independent engine, and the non-git surfaces that also become public.

### 9.1 Before scanning

1. **Freeze merges.** Merge or close every open PR. GitHub recommends *"merging or closing all open pull requests"* before any history rewrite [E, [GitHub Docs, Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)].
2. **Review every change ever made to the guard rails:** `git log -p -- .gitleaks.toml .pre-commit-config.yaml .github/workflows/secret-scan.yml .gitignore SECURITY.md`. Any allowlist entry without a recorded CEO approval is a finding in its own right.

### 9.2 The scan (fresh clone, all refs, including PR refs)

```sh
git clone https://github.com/deopea-david/haunts.git haunts-gate && cd haunts-gate
git fetch origin '+refs/pull/*:refs/remotes/origin/pull/*' '+refs/tags/*:refs/tags/*'
git for-each-ref | wc -l        # record the ref count in the gate note

# Engine 1: gitleaks, same pinned version and config as CI, report kept OUTSIDE the repo
gitleaks git . --config .gitleaks.toml --log-opts="--all" --redact \
  --ignore-gitleaks-allow --max-decode-depth=5 --max-archive-depth=2 \
  --report-path "$TMPDIR/gate-gitleaks.json"
# (Correction 1: decode depth 5, as in CI. Binary files are caught only by the filename check below.)

# Engine 2: trufflehog, independent rules, no verification (nothing sent to issuers)
trufflehog git file://. --no-verification --json > "$TMPDIR/gate-trufflehog.json"

# Filenames ever committed, on any ref (same pattern as CI)
git log --all --name-only --format= | sort -u | grep -Ei '<pattern from §5.2>' | grep -Eiv '(^|/)\.env\.example$'

# Blobs over 1 MB, on any ref
git rev-list --objects --all \
  | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
  | awk '$1=="blob" && $3>1048576'
```

- GitHub keeps `refs/pull/*/head` for PRs, and old commits stay reachable *"Through any pull requests that reference them"* and *"Directly via their SHA-1 hashes in cached views on GitHub"* [E, [Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]. So **the scan must include PR refs**, which a plain clone does not fetch [K, high confidence]. The explicit refspec above fetches them.
- **The trufflehog report is not redacted** [K, moderate confidence]. Keep both reports in a temp directory, never in the repo, and delete them after the gate note is written. `.gitignore` blocks accidents (§7).
- Whether trufflehog's `git` source scans every local ref or only the default branch, I have not confirmed [K, uncertain]. Check its `--help` at the pinned version before relying on it, and pass the branch options it documents if needed.

### 9.3 Surfaces `git` does not see

- **Actions runs and logs** become visible to everyone [E, §6]. Check that no run printed a secret. The baseline redacts, but other workflows may be added later. Delete runs and artifacts that should not be public. Deleting logs needs write access and is supported in the UI and API [E, [GitHub Docs, Using workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)].
- **Issues, PR descriptions, review comments** (D27 puts the tickets here). Pipe them through gitleaks' `stdin` mode, one of its three scanning modes [E, README]. For example: `gh issue list --state all --json title,body,comments | gitleaks stdin --redact`, and the same for `gh pr list`.
- **Releases and their assets, packages, wiki.** Review by hand.

### 9.4 If the scan is clean

Record a gate note: tool versions, the ref count, the HEAD SHA, zero findings from each engine, the date, who ran it. Then the CEO decides the switch. Straight after it, in this order: repo push protection on, a ruleset on `main` requiring `secret-scan` and blocking force-pushes, Dependabot alerts on, private vulnerability reporting on. **Watch GitHub's secret-scanning alerts for the first days**, because GitHub's scanner is a third engine [J].

### 9.5 If anything is found: rotate first, then rewrite

**A secret in history is leaked, even while the repo is private.** It has been in every clone, every agent worktree, possibly an agent transcript or a CI log, and within reach of any GitHub App with read access [J]. Scrubbing history hides it from future readers. It does nothing about copies already taken. So the order is fixed:

1. **Do not switch to public.**
2. **Rotate or revoke at the issuer.** App Store Connect key: revoke, which *"can't [be] reinstate[d]"* [E, [Apple, Revoking API keys](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys)]. Upload keystore: request a reset in Play Console, which **Google performs**, so allow for lead time [E, [Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en)]. Expo token: delete it [E, [Expo](https://docs.expo.dev/accounts/programmatic-access/)].
3. **Confirm the old credential is dead**, and check the issuer's activity for use during the exposure window. Record what was found.
4. **Then clean history**, as a human. Use `git-filter-repo` at *"least version 2.47"* with `--sensitive-data-removal`, and `--invert-paths --path <file>` or `--replace-text` [E, [Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]. Then choose one of two routes. **This is a CEO decision at the time, and I give it here only so it is not improvised:**
   - **(a) Keep the repo and ask GitHub Support** to purge cached views and PR refs, providing the affected-PR count and the *"First Changed Commit(s)"* [E, same]. This keeps issues and the board (D27). It depends on Support, which *"will only assist… in cases where we determine that the risk can't be mitigated by rotating affected credentials"* [E, same]. Since we will already have rotated, **Support may decline** [I].
   - **(b) Publish a new repository from the cleaned history** and retire the private one. Nothing can linger in PR refs or cached views, because they never existed on the new repo. The cost: issues, board and PR history need migrating, and deleting the old repo is irreversible [J]. **My lean, if contamination is more than trivial: (b)**, because the repo will still be private and this is the one moment when a clean start is cheap [J].
5. **Rescan the result to zero** with §9.2, then return to §9.4.
6. **Article 3.** The schedule requires *"Prompt disclosure to affected users; public summary after resolution"* for *"Security or data incidents affecting users"* (Constitution Article 3). **Before launch there are no users**, so a pre-launch leak with no misuse triggers no disclosure duty [I, from the clause's words]. I still recommend recording it in the decision record [J]. **After launch**, a leaked signing or update credential that was *used* would be an incident affecting users.

---

## 10. The `candour` history check: done, and clean

**Scope** [E, run 2026-09-26 in this worktree, read-only]:
- **50 commits** reachable from **20 refs**: local branches, agent worktree branches, 5 remote-tracking refs, 7 tags (`v0.1`–`v1.3`) and `refs/stash`.
- I checked the published remote against the local copy with `git ls-remote origin`. Its 4 branch heads and 7 tags all exist locally, including `haunt/requirements` at `e46e9ed`, `main` at `c191922` and `scout/2026-09-candidates` at `ee34eb8`. So the published history is inside what I scanned.
- PR #1's refs were not fetched. PR #1 was merged, and its head is on a branch I scanned [I].

**Method.**
1. `git log -p --all`, with every **added** line tested against **18 patterns**: PEM private-key header, AWS access key ID, GitHub token/PAT, Google API key, Slack, Stripe, OpenAI-style `sk-`, Anthropic `sk-ant-`, npm, Hugging Face, JWT, Mapbox, credentials in URLs, `EXPO_TOKEN=` with a value, npm `_authToken=`, generic `secret/token/password/api_key = <16+ chars>`, long base64-like strings, and 32+ character hex strings. **Values were masked inside the scanner**: only the first 6 characters and the length were ever printed.
2. Every path ever committed on any ref (132 paths) checked against the signing and credential filename pattern in §5.2.
3. A keyword pass for `password`, `api key`, `bearer`, `authorization:`, `token=`, `?key=`, with values redacted before printing.

**Results.**

| Check | Hits | What they are |
|---|---|---|
| Provider-specific tokens, private keys, credential URLs, `EXPO_TOKEN`, `_authToken`, generic secret assignments (16 patterns) | **0** | — |
| Long base64-like strings | 45 | All are fragments of cited URLs (`docs.*`, `gov.uk`, `ons.gov.uk`…) or local file paths quoted in documents. **Not secrets.** |
| Hex strings of 32+ characters | 5, in 4 files | An MD5 checksum of the OS Open Zoomstack file (`products/haunt/map-options-comparison.md`, commit `068a2e1f`); two SHA-256 file hashes (`products/haunt/venue-index-nameseach.md`, `8df29677`); a CEDA catalogue UUID (`proposals/plot/idea-brief.md` and `research/scouts/scout-2026-09-01-everyday-fun.md`, `976a6079`). **Published identifiers, not secrets.** |
| Credential keywords | Prose only | Research text about password managers and backup keys. |
| Signing or credential files ever committed | **0** | The only non-Markdown files ever committed are `.gitignore`, `.gitkeep` files, and the venue-index harness's Python, JSON and text files. **Nothing sensitive was committed and later deleted.** |

**GitHub side** [E, `gh api repos/deopea-david/candour`, GET only]: visibility `public`; `secret_scanning` **enabled**; `secret_scanning_push_protection` **enabled**; non-provider patterns and validity checks disabled; Dependabot security updates disabled (there are no dependencies, so that is moot). `GET .../secret-scanning/alerts` returned **an empty list**.

**Verdict: clean, with stated confidence.** High confidence that no common provider token or private key is anywhere in `candour`'s history. Moderate confidence for unusual formats, because this was 18 patterns without entropy scoring, against gitleaks' 222 rules [J]. It is also backed by GitHub's own scanner having run on the public repo with no alerts [E].

**Two observations. Neither is a secret, and neither is a finding.**
- 100 of the 102 author and committer entries use an address at the founder's own domain [E, domain only printed]. That is already public in `candour`. For `haunts`, using the same address adds nothing. Using a GitHub no-reply address is the CEO's choice to make if he wants to [J].
- Some documents quote absolute local paths that show the macOS username [E, seen in the scan]. Low sensitivity [J].

**Recommendations for `candour` (flags, for the orchestrator or CEO):** (1) Once gitleaks is installed, run `gitleaks git . --log-opts="--all" --redact` on `candour` once, to replace this pattern search with the real engine. It is one command. (2) Consider adding the same `.pre-commit-config.yaml` gitleaks hook to `candour`, where agents commit every day. It is cheap, and GitHub's push protection already covers the server side there.

---

## 11. Setting it up, and the acceptance tests before the first commit

**Order, once the CEO approves** (the repo itself also needs his go-ahead, per STATUS.md):
1. `brew install gitleaks` (Homebrew stable is **8.30.1**, MIT [E, `brew info`]), and put `pre-commit` on the default PATH, via `brew install pre-commit` (**4.6.2** [E]) or by making pyenv 3.14.5 global.
2. Run the tests below in a **throwaway local repo in a scratch directory**. Never in `haunts`, and never pushed anywhere, because test "secrets" in history are exactly what we are preventing. Fake keys are generated at test time, e.g. `openssl genpkey`, and are worthless.
3. Create `haunts`. Write the files from §4, §5, §7 and §8. Run `pre-commit install` and then `pre-commit run --all-files`. **Stage named paths.** Make the first commit, push, and confirm `secret-scan` is green. Then run it once more with `workflow_dispatch`.

| # | Test | Expected |
|---|---|---|
| T1 | Stage a generated PEM private key | Blocked by `gitleaks` **and** `detect-private-key`. |
| T2 | Stage `upload.jks` (random bytes) | Blocked by `forbid-signing-and-credential-files`. **Also record whether gitleaks' path rule fired on the binary**, which answers the open question in §3. |
| T3 | Stage `.env` with `FOO=bar`; separately stage `.env.example` | `.env` blocked; `.env.example` passes. |
| T4 | `EXPO_TOKEN=` + 40 random characters; separately, `EXPO_TOKEN: ${{ secrets.EXPO_TOKEN }}` | First blocked; second passes. Also shows whether keywords are case-insensitive (§4.2). |
| T5 | `storePassword` followed by a quoted random 8-character literal in `build.gradle`; separately, `storePassword System.getenv("X")` | First blocked; second passes. |
| T6 | `MYAPP_UPLOAD_STORE_PASSWORD=` followed by a random 8-character literal in `gradle.properties` | Blocked. |
| T7 | T4's first line plus a `gitleaks:allow` comment | Passes the hook. **Fails** the CI command run locally with `--ignore-gitleaks-allow`. |
| T8 | A `.gitleaksignore` file present | The CI suppression step fails. |
| T9 | A 2 MB file | Blocked by `check-added-large-files`. |
| T10 | A file containing merge-conflict markers | Blocked. |
| T11 | Any blocked secret | Hook output shows it **redacted**, never the value. |
| T12 | Commit a `.p8` with `--no-verify`, delete it in the next commit, then run the CI commands locally (darwin binary, same version) | The filename step **and** gitleaks both fail on the history. |
| T13 | Commit from a git worktree of the test repo | Hooks run (shared hooks directory, §2.2). |
| T14 | First push to `haunts` | `secret-scan` green; ref count and duration noted. If a run takes over ~2 minutes, reconsider §5.2's full-history choice. |
| T15 | Load `.claude/settings.json`; check `/status`; try `cat .env` and `git commit --no-verify` in a Claude Code session | Both denied; `.env.example` readable. |

**Results (Correction 1, 2026-09-26):** T1–T13 pass on the corrected config [E, RESULTS.md]. **T10 failed on this spec's original config** and passes with `--assume-in-merge`. T2 passes via the filename hook only, and gitleaks' path rule did **not** fire on the binary. T14 and T15 are still to run.

**If any test fails, the first commit waits** until the config is fixed and re-tested. A baseline that has never been seen to block anything is a belief, not a control [J].

---

## 12. Disagreements, flags, and what would overturn this

**On the CVO's two points (D29):** both **confirmed**. The first is **strengthened**: while private, CI is the *only* server-side check, not a backstop (§6). The second is **widened** to PR refs, a second engine, and non-git surfaces (§9).

**Where I part from the brief or from a source, stated once:**
1. **I recommend against `gitleaks-action`**, although it is free for this account (§5.1).
2. **I block all `.env` files except `.env.example`**, which is stricter than Expo's guidance (§7).
3. **Framing of D29.** It reads as "pre-commit first". I would put it as **"CI and pre-commit together, in the same first commit"**. The pre-commit hook is the convenience that catches mistakes early. The CI job is the control, because only it cannot be skipped from a laptop. Both are in the baseline, so nothing changes in practice. I record it so that nobody later treats the hooks alone as sufficient.

**Flags (not blocks), with the seat that holds the decision:**
- EAS Update and paid code signing → **CTO**, then **CFO** (§8.4).
- Firebase or Google config ever appearing → **CEO**, Constitution 5.4 (§8.4).
- `no-commit-to-branch`, `forbid-submodules`, native folders committed or generated, `debug.keystore` → **CTO** (§3, §7).
- GitHub Pro for private-repo rulesets → **CEO** (money). I recommend against for now (§6).
- `SECURITY.md` contact address → **CEO** (personal data) (§8.2).
- The gitleaks run and optional hook on `candour` → **orchestrator/CEO** (§10).
- *(Correction 1)* **A binary keystore inside an archive is caught by nothing** [I, from T2]. The fix, if wanted, is to add archive extensions (`zip|tar|tgz|gz|7z|rar`) to both filename patterns, at the cost of blocking legitimate archives. Archives are unusual in a React Native repo [J]. → **CTO** to say whether any are expected. The change would then need a CSO note and CEO approval, like any guard-rail change. It is not a precondition for the first push.
- *(Correction 1)* **Re-run T2 at every gitleaks bump.** If a release starts applying path rules to binaries, the filename controls become a second layer again, and should stay.
- Go-public preconditions: §9 here, plus the CGO licence note and the CEO's written reason, both owed under D28.

**Blocks exercised: none.** My charter's block is release-only, and nothing here is a release.

**What would overturn the tool recommendation, and where I looked.**
- *Evidence that gitleaks misses a class of secret in this stack that trufflehog or detect-secrets catches.* §11's tests and the gate's two-engine comparison would show it. If so, add the second engine to CI.
- *A change to gitleaks' licence away from MIT, or the project going unmaintained.* The last release was 2026-03-21, six months ago [E]. Check at each quarterly bump.
- *pre-commit's Go bootstrap failing in agent sandboxes.* Switch the hook id to `gitleaks-system`, which is defined in the same hooks file [E], with the Homebrew binary pinned by a version check.
- *GitHub making secret scanning available to user-owned private repositories.* CI then becomes a second layer rather than the only one. It still stays.
- **Where I looked:** the gitleaks, gitleaks-action, pre-commit-hooks, trufflehog, detect-secrets, lefthook and actions/checkout repositories at their pinned tags, through the GitHub API; pre-commit.com; GitHub Docs pages on secret scanning, push protection, plans, rulesets, secure use, workflow logs, repository visibility and removing sensitive data; Expo docs on environment variables, EAS environment variables, local credentials, programmatic access and EAS Update code signing, plus Expo's template `.gitignore`; Apple's App Store Connect API key pages; Google's Play App Signing help; Claude Code's settings and permissions docs. **What I could not retrieve:** GitHub Pro's price; whether this account is on Free or Pro; whether Expo robot users need a paid plan.

---

## 13. Sources

All retrieved 2026-09-26.

**Tools, at their pinned tags**
- gitleaks v8.30.1: [release](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1) · [README](https://github.com/gitleaks/gitleaks/blob/v8.30.1/README.md) · [.pre-commit-hooks.yaml](https://github.com/gitleaks/gitleaks/blob/v8.30.1/.pre-commit-hooks.yaml) · [config/gitleaks.toml](https://github.com/gitleaks/gitleaks/blob/v8.30.1/config/gitleaks.toml) · [checksums](https://github.com/gitleaks/gitleaks/releases/download/v8.30.1/gitleaks_8.30.1_checksums.txt)
- gitleaks-action v3.0.0: [README](https://github.com/gitleaks/gitleaks-action/blob/v3.0.0/README.md) · [LICENSE.txt (EULA)](https://github.com/gitleaks/gitleaks-action/blob/v3.0.0/LICENSE.txt)
- pre-commit: [pre-commit.com](https://pre-commit.com/) · [v4.6.2 release](https://github.com/pre-commit/pre-commit/releases/tag/v4.6.2)
- pre-commit-hooks v6.0.0: [release](https://github.com/pre-commit/pre-commit-hooks/releases/tag/v6.0.0) · [README](https://github.com/pre-commit/pre-commit-hooks/blob/v6.0.0/README.md)
- trufflehog v3.97.9: [release](https://github.com/trufflesecurity/trufflehog/releases/tag/v3.97.9) · [README](https://github.com/trufflesecurity/trufflehog/blob/v3.97.9/README.md)
- detect-secrets v1.5.0: [release](https://github.com/Yelp/detect-secrets/releases/tag/v1.5.0)
- lefthook v2.1.14: [release](https://github.com/evilmartians/lefthook/releases/tag/v2.1.14)
- actions/checkout v7.0.1: [release](https://github.com/actions/checkout/releases/tag/v7.0.1) · [README](https://github.com/actions/checkout/blob/v7.0.1/README.md)
- Licences, commit SHAs for tags, release asset digests: GitHub REST API (`gh api`), read directly.

**GitHub**
- [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)
- [Push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection)
- [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) · [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Secure use reference (Actions)](https://docs.github.com/en/actions/reference/security/secure-use)
- [Using workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)
- [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Pricing](https://github.com/pricing)

**Expo**
- [Environment variables](https://docs.expo.dev/guides/environment-variables/) · [EAS environment variables](https://docs.expo.dev/eas/environment-variables/) · [Local app credentials](https://docs.expo.dev/app-signing/local-credentials/) · [Programmatic access](https://docs.expo.dev/accounts/programmatic-access/) · [EAS Update code signing](https://docs.expo.dev/eas-update/code-signing/) · [Template .gitignore](https://github.com/expo/expo/blob/main/templates/expo-template-default/gitignore)

**Apple and Google**
- [Creating API keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api) · [Revoking API keys](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys)
- [Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en)

**Claude Code**
- [Settings](https://code.claude.com/docs/en/settings) · [Permissions](https://code.claude.com/docs/en/permissions)

**Local, read-only, 2026-09-26:** `git log -p --all`, `git ls-remote origin`, `git rev-parse --git-path hooks` (in a `candour` worktree); `gh api repos/deopea-david/candour` and `.../secret-scanning/alerts`; `gh api user`; `brew info gitleaks pre-commit`; `which go`; `pre-commit --version`.

