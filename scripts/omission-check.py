#!/usr/bin/env python3
"""Omission check (M2) and view screen (M8) for the Coordinator seat.

Owner: the CGO. roles/coordinator.md, Annex E: "The CGO owns and maintains the
script", so the Coordinator runs it and never edits it. Changes to this file,
to ALLOWLIST and to VIEW_PHRASES are drafted by the CGO.
Provenance: written by a CGO subagent (opus), not by the main session.
Section 11 item 18 of pipeline/amendment-draft-coordinator.md had named the
Engineer for the script; the CGO wrote it, a departure that is the CEO's to
accept. Exception (iii) to the role rule (D4a) is replaced by D16 (2026-10-04,
decisions/2026-10-02-coordinator-seat.md): any seat but the Skeptic, only in
a fresh session the CEO asks for. The CGO remains the owner.
Spec: section 11 item 18 of the amendment draft, and Annex E of
roles/coordinator.md (M2 (i)-(iii), M8). Template markers still owed:
pipeline/omission-check-markers.md.

  python3 scripts/omission-check.py report REPORT [SOURCE ...] [options]
  python3 scripts/omission-check.py transcript PATH [PATH ...]

report      Runs M2 over one report (a file, or - for stdin) against the source
            artifacts it covers. Attach the output under Annex A item 5.
            HTML comments and link-reference or footnote definitions are
            removed first, and struck-through text in item 2 is ignored: what
            the CEO cannot see, or sees withdrawn, does not count.
              (i)   every fatal or serious objection headline, every 5.2 date
                    under 7 days, and every marked block and failed QA limb in
                    the sources appears verbatim in item 2 ("What you may not
                    want to hear"), not merely somewhere in the report. Every
                    gate pack, dissent memo, review pack, decision record,
                    research brief or idea brief the report cites, and every
                    dissent memo in a proposals/<slug>/ that the report cites or
                    a source sits in, must be a source
              (ii)  every "Work I started without asking" authority resolves to
                    an allowlisted file and line on main, the CEO's recorded
                    words, or a seat's recommendation or next-steps section in
                    a file git tracks (never the report itself, nor memory)
              (iii) item 3 carries "No view offered." or a "My view - trigger:"
                    line naming a listed trigger, with the kind of reference
                    honest-broker rule 3 requires. A "My view" line outside
                    item 3 fails
            Options:
              --ceo-words PATH  the CEO's recorded words. Repeatable. Either a
                                session transcript (.jsonl), of which only the
                                entries the harness marks origin.kind "human"
                                are read (never tool results, task
                                notifications, peer messages or shell output),
                                or a decision record (decisions/*.md, read as
                                merged to main), of which only blockquoted
                                italic quotes ('> *"..."*') are read. Only a
                                transcript turn before any widget call can
                                PASS; a match in a decision record, or after a
                                widget call, is a GAP
              --today DATE      ISO date for the 5.2 arithmetic (default: today)
              --main-ref REF    for tests: any ref that is not the default main
                                (origin/main, else main) makes the integrity
                                line FAIL, so a run against it is not evidence
              --repo DIR        repository root (default: the git top level)

transcript  Runs M8 over main-session transcript files (.jsonl, text or
            markdown files, or directories holding .jsonl), at a phase review:
              (a) reports (messages carrying Annex A item 2, 3 or 4) whose item
                  3 fails M2(iii); references are checked for form only, and an
                  "asked" quote against the CEO's earlier turns in the same
                  transcript
              (b) view phrases outside a "My view" block in item 3 that names a
                  listed trigger. A lexical
                  screen with false positives and false negatives. Its hits are
                  raw: the CGO samples them and reports confirmed counts.
            Options:
              --since WHEN  count only messages stamped from then on (for
                            example, from D12 coming into force); unstamped
                            messages are then left out

Quotes: every fragment of a quote (split at an ellipsis) must sit in one CEO
turn, or one recorded quote, in order. A quote that is found but has a
fragment under MIN_QUOTE_WORDS words is a GAP, never a PASS.

Output is plain text, one line per check:
  PASS  the check was made and passed
  FAIL  the check was made and failed, or could not be made from what was given
  GAP   a check the script cannot make; never read it as a pass
  HIT   an M8(b) screen hit, unconfirmed
  INFO  what was read: each source, and what was extracted from it
The last line is RESULT: FAIL, PASS-WITH-GAPS or PASS.
Exit status: 1 if any line is FAIL; 2 on a usage or input error; 3 if nothing
fails but a GAP line is present; else 0.

Residuals, stated rather than fixed: a local origin/main can be moved with
git update-ref; a seat could hand over a forged .jsonl; that a human-marked
turn is typed by the CEO is an inference (a widget can send text as if he
typed it), so turns after a widget call are GAPs, but a widget rendered in an
earlier transcript file (a resumed or forked session) is not seen; other
constructs that render as nothing depend on the renderer (raw HTML with a
hidden attribute, for example) and are not removed.
Python 3 standard library only.
"""

import argparse
import datetime as dt
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path

VERSION = "1.2"
SCRIPT_PATH = "scripts/omission-check.py"

# Annex D, case (a): the files whose text, as merged to main, is authority.
# "A file the CEO adds by decision" joins this list by a CGO edit, never by a
# flag, so the seat being checked cannot widen its own allowlist.
ALLOWLIST = (
    "constitution.md",
    "CLAUDE.md",
    "pipeline/agentic-agile.md",
    "pipeline/model-selection.md",
    "pipeline/evidence-standard.md",
    ".claude/commands/*.md",
    "decisions/*.md",
)

# Annex D, "Not authority": state, never authority, even under case (b).
NOT_AUTHORITY = ("STATUS.md", "*/STATUS.md", "*standup*", "*commission*",
                 "MEMORY.md", "*/MEMORY.md", "memory/*", "*/memory/*",
                 ".claude/projects/*")

# Honest-broker rule 3: the only four triggers.
TRIGGERS = ("asked", "seat error", "seat conflict", "process broken")

# M8(b) phrase list. Owned by the CGO (Annex E, M8: "the list is the CGO's").
# The charter's own examples come first. Matching ignores case.
VIEW_PHRASES = (
    # The charter's examples
    "I recommend", "I'd", "I think", "my recommendation",
    # First-person recommendation or advice
    "I'd recommend", "I would recommend", "I suggest", "I'd suggest",
    "I would suggest", "my suggestion", "I advise", "I'd advise", "my advice",
    # First-person opinion
    "I believe", "I feel", "I would", "I reckon", "in my view",
    "in my opinion", "my view is", "my take", "my sense is", "I prefer",
    "I'd prefer", "my preference", "I favour", "I favor", "I lean",
    "I'm inclined", "I am inclined", "if I were you", "I agree", "I disagree",
    # Directive or verdict
    "you should", "we should", "the right call", "the best option",
    "the better option", "the obvious choice", "the right answer",
    # Grading a seat's work (rule 3: "an adjective that grades a seat's work,
    # is a view")
    "excellent", "compelling", "convincing", "unconvincing", "persuasive",
    "well-argued", "well argued", "solid work", "sloppy", "thorough work",
    "weak case", "strong case",
)

# Set to True by the CGO once pipeline/omission-check-markers.md is adopted in
# the templates. Until then every report run carries a GAP line for blocks and
# failed QA limbs written in prose.
MARKERS_IN_TEMPLATES = False

PASS, FAIL, GAP, HIT, INFO = "PASS", "FAIL", "GAP", "HIT", "INFO"

# A quote fragment shorter than this is too common to show the words are his.
MIN_QUOTE_WORDS = 4

# Annex A item 2 is where rule 1's copies go. Reports cite these kinds of
# artifact; each one cited must be among the sources M2(i) reads.
SOURCE_KINDS = (
    ("gate pack", "gate-pack*.md"), ("dissent memo", "*dissent*.md"),
    ("review pack", "review-pack*.md"), ("decision record", "decisions/*.md"),
    ("research brief", "research-brief*.md"), ("research brief", "research/*.md"),
    ("idea brief", "idea-brief*.md"),
)

# ---------------------------------------------------------------- text helpers

_TR = str.maketrans({
    "‘": "'", "’": "'", "“": '"', "”": '"',
    " ": " ", "′": "'",
})


def norm(text):
    """Straight quotes, no markdown emphasis or code ticks, single spaces."""
    text = text.translate(_TR).replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def one_line(text, limit=160):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit - 3] + "..."


_COMMENT = re.compile(r"<!--.*?(?:-->|\Z)", re.S)
# A link-reference or footnote definition, also inside a blockquote or list
# item: "[r0]: <#> (title)" renders as nothing (CommonMark 0.31.2, 4.7), and a
# footnote renders away from item 2 (CTO re-review N1). Any indent is matched:
# stripping too much fails closed.
_LINKDEF = re.compile(r"^\s*(?:(?:>|[-*+]|\d+[.)])\s*)*\[(?:[^\]\\]|\\.)+\]:(?P<rest>.*)$")
_TITLE_OPEN = {'"': '"', "'": "'", "(": ")"}


def _title_tail(rest):
    """For a definition's text after the colon: the closer still awaited on
    later lines ('' if none), and whether the destination is still to come."""
    rest = rest.strip()
    if not rest:
        return "", True
    dest = re.match(r"<[^>]*>|\S+", rest)
    rest = rest[dest.end():].strip()
    if rest[:1] in _TITLE_OPEN:
        close = _TITLE_OPEN[rest[0]]
        return ("" if close in rest[1:] else close), False
    return "", False


def strip_hidden(text):
    """What does not render, removed, line numbers kept: HTML comments, and
    link-reference and footnote definitions with their continuation lines
    (a destination or title on the following lines)."""
    text = _COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    lines, out = text.split("\n"), []
    await_close, await_dest, after_def = "", False, False
    for line in lines:
        s = line.strip()
        if await_close:
            out.append("")
            if not s or await_close in s:
                await_close, after_def = "", False
            continue
        m = _LINKDEF.match(line)
        if m:
            out.append("")
            await_close, await_dest = _title_tail(m.group("rest"))
            after_def = True
            continue
        if after_def and s and (await_dest or s[:1] in _TITLE_OPEN):
            # The destination, or a title, continuing the definition above.
            out.append("")
            if await_dest:
                await_close, await_dest = _title_tail(s)
            else:
                close = _TITLE_OPEN[s[0]]
                await_close = "" if close in s[1:] else close
                after_def = False  # one title per definition
            continue
        after_def = False
        out.append(line)
    return "\n".join(out)


# Strikethrough visibly withdraws a line, so struck text is not copied (N5).
_STRUCK = re.compile(r"(?<![~\w])(~{1,2})(?!~)(?=\S).*?(?<=\S)(?<!~)\1(?![~\w])"
                     r"|<(del|s|strike)\b[^>]*>.*?</\2\s*>", re.S | re.I)


def strip_struck(text):
    return _STRUCK.sub(" ", text)


def section_text(secs, key):
    return "\n".join(l for _, l in secs.get(key, []))


# ------------------------------------------------------- Annex A report shape

LABELS = (
    ("hear", ("what you may not want to hear",)),
    ("item3", ("seats' recommendations", "seat recommendations",
               "seats recommendations")),
    ("item4", ("work i started without asking",)),
    ("item5", ("omission-check output", "omission check output")),
    ("item6", ("links",)),
)
REPORT_LABELS = ("hear", "item3", "item4")
_LEAD = re.compile(r"^(?:[#>\s_\-+]|\d+[.)])*")
_ITEM3_TITLE = re.compile(
    r"then my view or\s*\"?\s*No view offered\.?\s*\"?", re.I)


def label_of(line):
    """The Annex A item a line opens, or None."""
    s = _LEAD.sub("", norm(line).lower())
    for key, texts in LABELS:
        for t in texts:
            if s.startswith(t):
                nxt = s[len(t):len(t) + 1]
                if nxt and nxt.isalnum():
                    continue
                return key
    return None


def sections(text):
    """{item key: [(line number, line), ...]}, each from its label onwards."""
    out, cur = {}, None
    for n, line in enumerate(text.splitlines(), 1):
        key = label_of(line)
        if key:
            cur = key
            if key == "item3":
                # The charter's own title for item 3 contains the marker text;
                # copying the title must not count as carrying the marker.
                line = _ITEM3_TITLE.sub("", line.translate(_TR).replace("*", "")
                                        .replace("`", ""))
        if cur:
            out.setdefault(cur, []).append((n, line))
    return out


# ------------------------------------------------------------------ references

PATH_RE = re.compile(
    r"(?P<path>(?:\.{0,2}/)?(?:[\w.-]+/)*[\w-][\w.-]*"
    r"\.(?:md|py|ya?ml|jsonl|json|csv|txt|sh|toml|ts|js))"
    r"(?::(?P<line>\d+)(?:-\d+)?|#L(?P<line2>\d+)(?:-L?\d+)?|#(?P<anchor>[\w-]+))?")
LINE_AFTER = re.compile(r"^[\s,]*(?:line|l\.|L)\s*(\d+)\b", re.I)
ANCHOR_AFTER = re.compile(r"^[\s,]*(D\d+[a-z]?|Condition \d+)\b")
# A recommendation or next-steps heading, after its number: "7. Recommendation",
# "My recommendation: ...", "The CTO's recommendation", "Recommended next step",
# "Next steps". Not any heading containing the word ("Seats' recommendations").
_HEAD_NUM = re.compile(r"^(?:[A-Z]?\d+(?:\.[\dA-Z]+)*\.?\s+)?")
RECO_HEAD = re.compile(
    r"^(?:(?:my|our|the(?:\s+[\w'-]+)?)\s+)?"
    r"(?:recommendations?|recommended next steps?|next steps?)\b", re.I)


def reco_heading(heading):
    return bool(RECO_HEAD.match(_HEAD_NUM.sub("", norm(heading))))


class Ref:
    def __init__(self, path, line=None, anchor=None):
        self.path, self.line, self.anchor = path, line, anchor

    def __str__(self):
        if self.line:
            return "%s:%d" % (self.path, self.line)
        if self.anchor:
            return "%s %s" % (self.path, self.anchor)
        return self.path


def path_refs(text):
    refs = []
    for m in PATH_RE.finditer(text):
        path = re.sub(r"^\./", "", m.group("path"))
        line = m.group("line") or m.group("line2")
        anchor = m.group("anchor")
        tail = text[m.end():m.end() + 24]
        if not line and not anchor:
            la = LINE_AFTER.match(tail)
            if la:
                line = la.group(1)
            else:
                aa = ANCHOR_AFTER.match(tail)
                if aa:
                    anchor = aa.group(1)
        refs.append(Ref(path, int(line) if line else None, anchor))
    return refs


def allowlisted(path):
    return any(fnmatch.fnmatchcase(path, pat) for pat in ALLOWLIST)


def not_authority(path):
    return any(fnmatch.fnmatchcase(path, pat) for pat in NOT_AUTHORITY)


def quotes_in(text):
    text = text.translate(_TR).replace("*", "")
    return [q for q in re.findall(r'"([^"]+)"', text) if re.search(r"\w", q)]


def quote_status(quote, texts):
    """PASS if every fragment (split at an ellipsis) is in one text, in order,
    and each has MIN_QUOTE_WORDS words; GAP if found but a fragment is shorter;
    FAIL if no single text holds them all in order."""
    frags = re.split(r"\[?(?:…|\.\.\.)\]?", norm(quote))
    frags = [f.strip(" .,;:!?").casefold() for f in frags]
    frags = [f for f in frags if re.search(r"\w", f)]
    if not frags:
        return FAIL
    for t in texts:
        at = 0
        for f in frags:
            i = t.find(f, at)
            if i < 0:
                break
            at = i + len(f)
        else:
            short = any(len(re.findall(r"\w+(?:'\w+)?", f)) < MIN_QUOTE_WORDS for f in frags)
            return GAP if short else PASS
    return FAIL


# Where a recorded text came from, when that alone keeps it from a PASS.
DR_WHY = "decision record"
WIDGET_WHY = "widget"


def ceo_match(qs, ceo):
    """(status, first quote at that status, why) for quotes against the CEO's
    words, a list of (text, why). Only a text with no why can give a PASS: a
    quote found only in a decision record (which does not mark who is quoted,
    CTO re-review N3), or only in a turn at or after a widget call (CTO
    re-review, section 5), is a GAP. A fragment too short is a GAP too."""
    trusted = [t for t, why in ceo if not why]
    worst = (PASS, None, None)
    for q in qs:
        st = quote_status(q, trusted)
        if st == PASS:
            continue
        if st == GAP:
            if worst[0] == PASS:
                worst = (GAP, q, "short")
            continue
        for t, why in ceo:
            if why and quote_status(q, [t]) != FAIL:
                if worst[0] == PASS:
                    worst = (GAP, q, why)
                break
        else:
            return FAIL, q, None
    return worst


def gap_reason(q, why):
    q = one_line(q, 80)
    if why == DR_WHY:
        return "\"%s\" is found only in a decision record, which does not mark who is " \
               "quoted, so it may be another seat's words; confirm by hand that the CEO " \
               "said it" % q
    if why == WIDGET_WHY:
        return "\"%s\" is found only in a turn at or after a widget call in the same " \
               "transcript; a widget can send text as if the CEO typed it, so confirm by " \
               "hand that he did" % q
    return "quote found, but \"%s\" has a fragment under %d words, too short to show " \
           "the words are his; check it by hand" % (q, MIN_QUOTE_WORDS)


def slug(heading):
    s = norm(heading).lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s.strip())


# ------------------------------------------------------------------- git, main

def git(repo, *args):
    try:
        p = subprocess.run(["git", "-C", str(repo)] + list(args),
                           capture_output=True, text=True)
    except OSError:
        return None
    return p.stdout if p.returncode == 0 else None


class Main:
    """Read files as merged to main (Annex D: "as merged to main")."""

    DEFAULT = ("origin/main", "main")

    def __init__(self, repo, ref=None):
        self.repo, self.name, self.sha, self.cache = repo, None, None, {}
        self.default_name, self.default_sha = self._first(self.DEFAULT)
        self.tried = [ref] if ref else list(self.DEFAULT)
        self.name, self.sha = self._first(self.tried)
        # --main-ref may not choose its own "main" (CTO review F9): a ref that
        # is not the default main is recorded here and fails the integrity line.
        self.overridden = bool(ref) and (self.sha is None or self.sha != self.default_sha)

    def _first(self, cands):
        for cand in cands:
            out = git(self.repo, "rev-parse", "--verify", "--quiet", cand + "^{commit}")
            if out and out.strip():
                return cand, out.strip()
        return None, None

    def read(self, path):
        if not self.sha:
            return None
        if path not in self.cache:
            self.cache[path] = git(self.repo, "show", "%s:%s" % (self.sha, path))
        return self.cache[path]

    def blob(self, path):
        if not self.sha:
            return None
        out = git(self.repo, "rev-parse", "--verify", "--quiet",
                  "%s:%s" % (self.sha, path))
        return out.strip() if out else None

    def describe(self):
        if not self.sha:
            return "none (tried %s)" % ", ".join(self.tried)
        return "%s@%s" % (self.name, self.sha[:7])


class Ctx:
    def __init__(self, repo, main, ceo, today, form_only=False, report_path=None):
        self.repo, self.main, self.ceo = repo, main, ceo
        self.today, self.form_only = today, form_only
        self.report_path = report_path


def in_repo(ctx, path):
    """The repository-relative path, or None if it lies outside the repository."""
    try:
        return (ctx.repo / path).resolve().relative_to(ctx.repo.resolve()).as_posix()
    except ValueError:
        return None


def tracked(ctx, rel):
    return git(ctx.repo, "ls-files", "--error-unmatch", "--", rel) is not None


def read_tree(ctx, path):
    p = ctx.repo / path
    try:
        return p.read_text(encoding="utf-8") if p.is_file() else None
    except (OSError, UnicodeDecodeError):
        return None


def resolve_allowlisted(ref, ctx, require_line):
    """Annex D case (a): an allowlisted file, as merged to main."""
    if not allowlisted(ref.path):
        return False, "%s is not on the Annex D allowlist" % ref.path
    if not ctx.main.sha:
        return False, "no main ref to read %s from (tried %s)" % (
            ref.path, ", ".join(ctx.main.tried))
    text = ctx.main.read(ref.path)
    if text is None:
        return False, "%s is not on %s" % (ref.path, ctx.main.name)
    lines = text.splitlines()
    if ref.line:
        if not 1 <= ref.line <= len(lines):
            return False, "%s has %d lines on %s; line %d does not exist" % (
                ref.path, len(lines), ctx.main.name, ref.line)
        if not lines[ref.line - 1].strip():
            return False, "%s:%d is blank on %s" % (ref.path, ref.line, ctx.main.name)
        # Print what the cited line says, so a reader sees what the authority is.
        return True, "%s on %s, which reads: \"%s\"" % (
            ref, ctx.main.name, one_line(lines[ref.line - 1], 120))
    if ref.anchor:
        if re.search(r"\b%s\b" % re.escape(ref.anchor), text):
            return True, "%s on %s" % (ref, ctx.main.name)
        return False, "%s does not contain %s on %s" % (
            ref.path, ref.anchor, ctx.main.name)
    if require_line:
        return False, "%s is cited without a line (Annex A item 4: 'file and line')" % ref.path
    return True, "%s on %s" % (ref.path, ctx.main.name)


def resolve_seat_section(ref, ctx):
    """Annex D case (b): a seat's own recommendation or next-steps section."""
    rel = in_repo(ctx, ref.path)
    if rel is None:
        return False, "%s lies outside the repository; case (b) needs a seat's " \
                      "artifact in it" % ref.path
    if not_authority(rel):
        return False, "%s is state, not authority (Annex D, 'Not authority')" % ref.path
    if ctx.report_path is not None and (ctx.repo / rel).resolve() == ctx.report_path:
        return False, "%s is this report; a report cannot authorise its own work" % ref.path
    if not tracked(ctx, rel):
        return False, "%s is not tracked by git; case (b) needs a seat's committed " \
                      "artifact" % ref.path
    text = read_tree(ctx, rel)
    if text is None:
        return False, "%s not found" % ref.path
    lines = text.splitlines()
    headings = [(i, l.lstrip("#").strip()) for i, l in enumerate(lines, 1)
                if re.match(r"^#{1,6}\s", l)]
    if ref.line:
        if not 1 <= ref.line <= len(lines):
            return False, "%s has %d lines; line %d does not exist" % (
                ref.path, len(lines), ref.line)
        above = [h for i, h in headings if i <= ref.line]
        if not above:
            return False, "%s:%d is under no heading" % (ref.path, ref.line)
        if reco_heading(above[-1]):
            return True, "case (b): %s, under '%s'" % (ref, one_line(above[-1], 60))
        return False, "%s:%d sits under '%s', not a recommendation or next-steps section" % (
            ref.path, ref.line, one_line(above[-1], 60))
    if ref.anchor:
        for _, h in headings:
            if slug(h) == ref.anchor.lower():
                if reco_heading(h):
                    return True, "case (b): %s#%s" % (ref.path, ref.anchor)
                return False, "%s#%s is not a recommendation or next-steps section" % (
                    ref.path, ref.anchor)
        return False, "%s has no heading #%s" % (ref.path, ref.anchor)
    return False, "%s is cited without a line or section anchor" % ref.path


# ---------------------------------------------------------------------- M2(iii)

VIEW_RE = re.compile(r"My view\s*(?:—|–|--?)\s*trigger\s*:(?P<rest>.*)", re.I)
REF_SPLIT = re.compile(r"(?:—|–|--?)\s*reference\s*:", re.I)
NO_VIEW = "no view offered."


def check_item3(text, ctx, check="M2(iii)"):
    secs = sections(text)
    if "item3" not in secs:
        return [(FAIL, check, "item 3 (\"Seats' recommendations\") not found, "
                 "so neither marker can be checked")]
    lines = secs["item3"]
    in3 = set(n for n, _ in lines)
    # Rule 3: "a recommendation in item 1 ... is a view". A My view line has
    # one home, item 3 (CTO review F10).
    stray = [n for n, l in enumerate(text.splitlines(), 1)
             if n not in in3 and VIEW_RE.search(norm(l))]
    if stray:
        return [(FAIL, check, "a 'My view' line sits outside item 3 (line %s); rule 3 "
                 "gives a view one place, item 3" % ", ".join(str(n) for n in stray))]
    no_view = [n for n, l in lines if NO_VIEW in norm(l).lower()]
    views = [(n, VIEW_RE.search(norm(l))) for n, l in lines]
    views = [(n, m) for n, m in views if m]
    if not no_view and not views:
        return [(FAIL, check, "item 3 carries neither 'No view offered.' nor a "
                 "'My view — trigger:' line")]
    if no_view and views:
        return [(FAIL, check, "item 3 carries both 'No view offered.' (line %d) and "
                 "a 'My view' line (line %d); Annex A allows exactly one"
                 % (no_view[0], views[0][0]))]
    if no_view:
        return [(PASS, check, "item 3, line %d: No view offered." % no_view[0])]
    out = []
    for n, m in views:
        out.extend(check_view_line(n, m.group("rest"), ctx, check))
    return out


def parse_view(rest):
    """(trigger names, reference, problem or None) for a My view line's text
    after "trigger:". The problem is set when the trigger itself is invalid."""
    parts = REF_SPLIT.split(rest, maxsplit=1)
    ref = parts[1].strip() if len(parts) == 2 else ""
    names = [t.strip(" .").lower()
             for t in re.split(r"[,|/;+&]|\band\b", parts[0])]
    names = [t for t in names if t]
    if not names:
        return names, ref, "'My view' names no trigger"
    bad = [t for t in names if t not in TRIGGERS]
    if bad:
        return names, ref, "trigger not on rule 3's list: %s (listed: %s)" % (
            ", ".join(repr(b) for b in bad), ", ".join(TRIGGERS))
    if not ref:
        return names, ref, "no '— reference:' part"
    return names, ref, None


def check_view_line(n, rest, ctx, check):
    where = "item 3, line %d" % n
    names, ref, problem = parse_view(rest)
    if problem:
        return [(FAIL, check, "%s: %s" % (where, problem))]
    out = []
    for t in names:
        ok, msg = REFERENCE_CHECKS[t](ref, ctx)
        status = ok if ok in (PASS, FAIL, GAP) else (PASS if ok else FAIL)
        out.append((status, check, "%s: trigger '%s': %s" % (where, t, msg)))
    return out


def ref_asked(ref, ctx):
    qs = quotes_in(ref)
    if not qs:
        return FAIL, "needs the CEO's words, quoted (rule 3)"
    if not ctx.ceo:
        # As M2(ii) does: an unchecked CEO quote is the case this check is for.
        return FAIL, "quotes the CEO, but no record of his words was given to check " \
                     "it against (pass --ceo-words)"
    st, q, why = ceo_match(qs, ctx.ceo)
    if st == FAIL:
        return FAIL, "quote not found in the CEO's recorded words: \"%s\"" % one_line(q, 80)
    if st == GAP:
        return GAP, gap_reason(q, why)
    return PASS, "quote found in the CEO's recorded words"


def ref_seat_error(ref, ctx):
    refs = [r for r in path_refs(norm(ref)) if r.line]
    if not refs:
        return False, "needs the artifact's path and line (rule 3)"
    if ctx.form_only:
        return True, "path and line given: %s (form only)" % refs[0]
    for r in refs:
        text = read_tree(ctx, r.path)
        if text is not None and 1 <= r.line <= len(text.splitlines()):
            return True, "%s exists" % r
    return False, "no cited path and line exists: %s" % ", ".join(str(r) for r in refs)


def ref_seat_conflict(ref, ctx):
    paths = []
    for r in path_refs(norm(ref)):
        if r.path not in paths:
            paths.append(r.path)
    if len(paths) < 2:
        return False, "needs both artifacts' paths (rule 3); found %d" % len(paths)
    if ctx.form_only:
        return True, "two paths given (form only)"
    missing = [p for p in paths if read_tree(ctx, p) is None]
    if len(paths) - len(missing) < 2:
        return False, "fewer than two cited paths exist (missing: %s)" % ", ".join(missing)
    return True, "both paths exist: %s" % ", ".join(p for p in paths if p not in missing)


def ref_process_broken(ref, ctx):
    refs = [r for r in path_refs(norm(ref)) if allowlisted(r.path)]
    if not refs:
        return False, "needs the file that requires the step: an Annex D allowlisted " \
                      "file or a decision record (rule 3)"
    if ctx.form_only:
        return True, "allowlisted file given: %s (form only)" % refs[0]
    reasons = []
    for r in refs:
        ok, msg = resolve_allowlisted(r, ctx, require_line=False)
        if ok:
            return True, msg
        reasons.append(msg)
    return False, "; ".join(reasons)


REFERENCE_CHECKS = {
    "asked": ref_asked,
    "seat error": ref_seat_error,
    "seat conflict": ref_seat_conflict,
    "process broken": ref_process_broken,
}

# ----------------------------------------------------------------------- M2(ii)

AUTH_RE = re.compile(r"\bauthority\s*:\s*(?P<v>.*)", re.I)
SEAT_FIELD = re.compile(r"^(?:[-*+]\s+|\d+[.)]\s+)?(?:the\s+)?seat\s*:", re.I)


def check_item4(text, ctx, check="M2(ii)"):
    secs = sections(text)
    if "item4" not in secs:
        return [(FAIL, check, "item 4 (\"Work I started without asking\") not found")]
    lines = secs["item4"]
    first = re.sub(r"(?i)^.*?work i started without asking[.:]?", "", norm(lines[0][1]))
    content = " ".join([first] + [norm(l) for _, l in lines[1:]]).strip(" :.-")
    auths = []
    for i, (n, l) in enumerate(lines):
        m = AUTH_RE.search(norm(l))
        if m:
            v = m.group("v").strip()
            j = i + 1
            while not v and j < len(lines):
                v = norm(lines[j][1]).lstrip("-*+ ").strip()
                j += 1
            auths.append((n, v))
    if not auths:
        if re.match(r"(?i)none\b", content):
            return [(PASS, check, "item 4: none")]
        if not content:
            return [(FAIL, check, "item 4 is empty; Annex A says to write 'none'")]
        return [(FAIL, check, "item 4 lists work but no 'authority:' field")]
    out = []
    seats = sum(1 for _, l in lines if SEAT_FIELD.match(norm(l)))
    if seats and seats != len(auths):
        out.append((FAIL, check, "item 4 names %d seats but gives %d authorities"
                    % (seats, len(auths))))
    for n, v in auths:
        status, msg = resolve_authority(v, ctx)
        out.append((status, check, "item 4, line %d: %s" % (n, msg)))
    return out


def resolve_authority(v, ctx):
    reasons, gap = [], None
    refs = path_refs(norm(v))
    for r in refs:
        if allowlisted(r.path):
            ok, msg = resolve_allowlisted(r, ctx, require_line=True)
            if ok:
                return PASS, "case (a): " + msg
            reasons.append(msg)
    qs = quotes_in(v)
    if qs:
        if not ctx.ceo:
            reasons.append("quotes the CEO, but no --ceo-words record was given to "
                           "resolve it against")
        else:
            st, q, why = ceo_match(qs, ctx.ceo)
            if st == PASS:
                return PASS, "the CEO's recorded words"
            if st == GAP:
                gap = gap_reason(q, why)
            else:
                reasons.append("quote not found in the CEO's recorded words: \"%s\""
                               % one_line(q, 80))
    for r in refs:
        if not allowlisted(r.path):
            ok, msg = resolve_seat_section(r, ctx)
            if ok:
                return PASS, msg
            reasons.append(msg)
    if gap:
        return GAP, gap
    if not refs and not qs:
        reasons.append("cites no file and quotes no words")
    return FAIL, "authority does not resolve: " + "; ".join(reasons)


# ------------------------------------------------------------------------ M2(i)

# The template requires a tier tag, not a line shape (CTO review F3), so a tag
# is looked for in any case, and an upper-case tier word without brackets
# counts where it leads a heading, list item or bold lead.
TIER = re.compile(r"\[(FATAL|SERIOUS)\b[^\]]*\]", re.I)
BARE_TIER = re.compile(r"(?<![\w\[])(FATAL|SERIOUS)(?![\w\]])")
FRICTION_TAG = re.compile(r"\[FRICTION\b", re.I)
OID = re.compile(r"^(?P<id>[A-Z]{1,3}\d+(?:-[A-Z]{1,3}\d+)*)(?=[\s.:—–-]|$)\.?")
LIST_LEAD = re.compile(r"^(?:[-*+]|\d+[.)])\s+")
BOLD_SPLIT = re.compile(r"^\*\*(?P<b>.+?)\*\*(?P<after>.*)$")
DELIMS = " .:—–-"
TIER_CELL = re.compile(r"^\[?(FATAL|SERIOUS)\b")
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
DUE_MARKERS = (
    re.compile(r"decision due\s*:", re.I),            # gate-pack.md
    re.compile(r"anti-drift clock\s*:", re.I),        # research-brief.md
    re.compile(r"^[-*+]\s*\[ \]\s*research brief\b.*?\bdue\b", re.I),  # idea-brief.md
    re.compile(r"\b5\.2 DUE\s*:"),                    # proposed marker
)
MARK_LEAD = re.compile(r"^(?:>\s*|[-*+]\s+)*")
BLOCK_M = re.compile(r"^BLOCK\s*\((?P<seat>[^)]+)\)\s*:\s*(?P<ground>\S.*)$")
LIFT_M = re.compile(r"^LIFTS WHEN\s*:\s*(?P<lift>\S.*)$")
QA_M = re.compile(r"^QA FAIL\s*\((?P<id>[^)]+)\)\s*:\s*(?P<text>\S.*)$")


class Objection:
    def __init__(self, tier, oid, headline, path, line, form):
        self.tier, self.oid, self.headline = tier, oid, headline
        self.path, self.line, self.form = path, line, form


def _strip_id(title):
    """(objection id or None, the title without it)."""
    idm = OID.match(title)
    if not idm:
        return None, title
    return idm.group("id"), title[idm.end():]


def objections_in(path, text):
    """(headed objections, table rows, problems). A problem is (line, kind):
    "unextracted" for a leading tag with no headline found, which fails closed,
    and "prose" for a bracketed tag mid-sentence, which is a GAP."""
    heads, rows, problems = [], [], []
    lines = text.splitlines()
    for n, raw in enumerate(lines, 1):
        s = raw.strip()
        if s.startswith("|"):
            cells = [norm(c) for c in s.strip("|").split("|")]
            for i, c in enumerate(cells):
                m = TIER_CELL.match(c)
                if m and len(c) <= 60 and i + 1 < len(cells) and cells[i + 1]:
                    oid = cells[i - 1] if i > 0 and OID.fullmatch(cells[i - 1]) else None
                    rows.append(Objection(m.group(1), oid, cells[i + 1], path, n, "table"))
                    break
            continue
        s = re.sub(r"^(?:>\s*)+", "", s)
        heading = s.startswith("#")
        listed = bool(LIST_LEAD.match(s))
        body = s.lstrip("#").strip() if heading else LIST_LEAD.sub("", s, count=1)
        bold = BOLD_SPLIT.match(body)
        t = TIER.search(body)
        if not t and (heading or listed or bold):
            t = BARE_TIER.search(body)
        if not t:
            continue
        tier = t.group(1).upper()
        lead = norm(body[:t.start()]).strip(DELIMS)
        if lead and not OID.fullmatch(lead):
            # Mid-sentence. The template's tier legend ("[FATAL] / [SERIOUS] /
            # [FRICTION]") is the one expected case; any other is for a human.
            if t.re is TIER and not FRICTION_TAG.search(body):
                problems.append((n, "prose"))
            continue
        if bold and t.start() < bold.end("b"):
            inner = body[:t.start()] + " " + body[t.end():bold.end("b")]
            oid, title = _strip_id(norm(inner))
            title, form = title.lstrip(DELIMS).strip(), "bold"
            if not title:
                title, form = norm(bold.group("after")).lstrip(DELIMS).strip(), "bold, after"
        elif heading:
            oid, title = _strip_id(norm(body[:t.start()] + " " + body[t.end():]))
            title, form = title.lstrip(DELIMS).strip(), "heading"
            if not title:
                nxt = next((l.strip() for l in lines[n:n + 3] if l.strip()), "")
                # Another heading or a table is not this objection's headline.
                if nxt.startswith(("#", "|")):
                    nxt = ""
                title = norm(LIST_LEAD.sub("", nxt.lstrip(">").strip())).lstrip(DELIMS).strip()
                form = "heading, next line"
        else:
            # A tagged list item or paragraph has no delimited headline:
            # require the whole line.
            whole = norm(body[:t.start()] + " " + body[t.end():]).lstrip(DELIMS).strip()
            oid, _ = _strip_id(whole)
            title, form = whole, "list"
        if title:
            heads.append(Objection(tier, oid, title, path, n, form))
        else:
            problems.append((n, "unextracted"))
    return heads, rows, problems


def cited_sources(report, sources, ctx, check):
    """CTO review F2: every gate pack, dissent memo, review pack, decision
    record, research brief or idea brief the report cites, and every dissent
    memo in a proposals/<slug>/ that the report cites or that a source sits in
    (CTO re-review N4), must be among the sources."""
    out, have = [], set()
    for src in sources:
        try:
            have.add(Path(src).resolve())
        except OSError:
            pass
    need = {}

    def memos_beside(rel, kind):
        parts = rel.split("/")
        if len(parts) >= 2 and parts[0] == "proposals":
            for memo in sorted((ctx.repo / "proposals" / parts[1]).glob("*dissent*.md")):
                need.setdefault("proposals/%s/%s" % (parts[1], memo.name), kind)

    for r in path_refs(norm(report)):
        rel = in_repo(ctx, r.path)
        if rel is None or rel.startswith("pipeline/templates/"):
            continue
        for kind, pat in SOURCE_KINDS:
            target = rel if "/" in pat else rel.rsplit("/", 1)[-1]
            if fnmatch.fnmatchcase(target, pat):
                need.setdefault(rel, kind)
                break
        memos_beside(rel, "dissent memo in a cited proposal")
    for p in have:
        try:
            rel = p.relative_to(ctx.repo.resolve()).as_posix()
        except ValueError:
            continue
        memos_beside(rel, "dissent memo in the same proposal as a source")
    for rel, kind in sorted(need.items()):
        p = (ctx.repo / rel).resolve()
        if not p.is_file():
            out.append((GAP, check, "the report cites %s (%s), which is not in the "
                        "repository; find it and check it by hand" % (rel, kind)))
        elif p not in have:
            out.append((FAIL, check, "%s (%s) is not among the sources, so its "
                        "objections, blocks and dates were not checked; re-run with it"
                        % (rel, kind)))
    return out


def check_sources(report, sources, ctx, check="M2(i)"):
    out = []
    if not sources:
        return [(FAIL, check, "no source artifacts given, so M2(i) cannot run; name "
                 "the artifacts this report covers")]
    out.extend(cited_sources(report, sources, ctx, check))
    # Rule 1's copies go under item 2 (Annex A). Text elsewhere, or in an HTML
    # comment (already removed), is not copied there (CTO review F1).
    secs = sections(report)
    if "hear" not in secs:
        out.append((FAIL, check, "item 2 (\"What you may not want to hear\") not found, "
                    "so nothing counts as copied under rule 1"))
    # Struck-through text is visibly withdrawn, so it is not copied (N5).
    hear = strip_struck(section_text(secs, "hear"))
    report_n = norm(hear)
    heads, rows, texts = [], [], []
    for src in sources:
        p = Path(src)
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            out.append((FAIL, check, "source %s cannot be read (%s)" % (src, e.__class__.__name__)))
            continue
        texts.append((src, text))
        h, r, problems = objections_in(src, text)
        seen_here = set(o.oid for o in h if o.oid)
        mine = h + [o for o in r if not (o.oid and o.oid in seen_here)]
        out.append((INFO, check, "source %s: %d fatal, %d serious objections extracted; "
                    "check against the memo's own count" % (
                        src, sum(o.tier == "FATAL" for o in mine),
                        sum(o.tier == "SERIOUS" for o in mine))))
        for n, kind in problems:
            if kind == "unextracted":
                out.append((FAIL, check, "objection tag at %s:%d: tag found, headline not "
                            "extracted; read it and copy its headline by hand" % (src, n)))
            else:
                out.append((GAP, check, "tier tag mid-sentence at %s:%d, read as prose, not "
                            "an objection; check it by hand" % (src, n)))
        heads.extend(h)
        rows.extend(r)
    seen = set((o.path, o.oid) for o in heads if o.oid)
    objs = heads + [o for o in rows if not (o.oid and (o.path, o.oid) in seen)]
    for o in objs:
        where = "%s %s%s:%d" % (o.tier, (o.oid + " ") if o.oid else "", o.path, o.line)
        if norm(o.headline) in report_n:
            out.append((PASS, check, "objection %s: headline copied verbatim in item 2" % where))
        else:
            out.append((FAIL, check, "objection %s: headline not in item 2 verbatim: \"%s\""
                        % (where, one_line(o.headline, 1000))))
    marked = 0
    for src, text in texts:
        lines = text.splitlines()
        for n, raw in enumerate(lines, 1):
            s = norm(raw)
            for rx in DUE_MARKERS:
                m = rx.search(s)
                if not m:
                    continue
                d = DATE.search(s, m.end())
                if not d:
                    out.append((GAP, check, "5.2 line %s:%d has no ISO date, so the script "
                                "cannot tell whether it is under 7 days; check it by hand"
                                % (src, n)))
                    break
                iso = d.group(1)
                try:
                    days = (dt.date.fromisoformat(iso) - ctx.today).days
                except ValueError:
                    out.append((GAP, check, "5.2 line %s:%d: %s is not a valid date" % (src, n, iso)))
                    break
                if days >= 7:
                    out.append((PASS, check, "5.2 date %s at %s:%d: %d days away, not under 7"
                                % (iso, src, n, days)))
                elif iso in hear:
                    out.append((PASS, check, "5.2 date %s at %s:%d (%d days): copied"
                                % (iso, src, n, days)))
                else:
                    out.append((FAIL, check, "5.2 date %s at %s:%d is %s and not in item 2"
                                % (iso, src, n, "%d days away" % days if days >= 0
                                   else "%d days past" % -days)))
                break
            s2 = MARK_LEAD.sub("", s)
            b = BLOCK_M.match(s2)
            if b:
                marked += 1
                where = "block (%s) at %s:%d" % (b.group("seat").strip(), src, n)
                out.append(copied(check, where + ": ground", b.group("ground"), report_n))
                lift = None
                for later in lines[n:n + 4]:
                    lm = LIFT_M.match(MARK_LEAD.sub("", norm(later)))
                    if lm:
                        lift = lm.group("lift")
                        break
                if lift is None:
                    out.append((FAIL, check, "%s has no 'LIFTS WHEN:' line within 3 lines; "
                                "every block states what lifts it" % where))
                else:
                    out.append(copied(check, where + ": lifting condition", lift, report_n))
            q = QA_M.match(s2)
            if q:
                marked += 1
                where = "failed QA limb (%s) at %s:%d" % (q.group("id").strip(), src, n)
                out.append(copied(check, where, q.group("text"), report_n))
    if not MARKERS_IN_TEMPLATES:
        out.append((GAP, check, "blocks and failed QA limbs: only lines marked 'BLOCK (seat):' "
                    "/ 'LIFTS WHEN:' / 'QA FAIL (id):' are checked (%d found). No template "
                    "carries these markers yet (pipeline/omission-check-markers.md), so a block "
                    "or failed limb written in prose is invisible to this script. Read the "
                    "sources for them yourself." % marked))
    return out


def copied(check, where, text, report_n):
    if norm(text) in report_n:
        return (PASS, check, "%s copied verbatim" % where)
    return (FAIL, check, "%s not in item 2 verbatim: \"%s\"" % (where, one_line(text, 1000)))


# ------------------------------------------------------------------- integrity

def check_integrity(ctx):
    check = "script"
    if ctx.main.overridden:
        return (FAIL, check, "--main-ref %s is not the default main (%s); a seat may not "
                "choose its own main, so this run is not evidence" % (
                    ctx.main.tried[0], "%s@%s" % (ctx.main.default_name, ctx.main.default_sha[:7])
                    if ctx.main.default_sha else "none found"))
    if not ctx.main.sha:
        return (GAP, check, "no main ref, so the script cannot confirm it matches main's copy")
    on_main = ctx.main.blob(SCRIPT_PATH)
    if on_main is None:
        return (GAP, check, "%s is not on %s yet; this run is of an unmerged copy"
                % (SCRIPT_PATH, ctx.main.name))
    mine = git(ctx.repo, "hash-object", str(Path(__file__).resolve()))
    if mine and mine.strip() == on_main:
        return (PASS, check, "this copy matches %s:%s" % (ctx.main.name, SCRIPT_PATH))
    return (FAIL, check, "this copy differs from %s:%s; run main's copy, which only the "
            "CGO changes" % (ctx.main.name, SCRIPT_PATH))


# ---------------------------------------------------------------- transcripts

# Inside a human turn, text the harness wrapped rather than he typed: shell
# commands and their output ("!" mode), slash-command expansions, reminders.
_STRIP_TAGS = re.compile(
    r"<(system-reminder|local-command-stdout|local-command-stderr|local-command-caveat"
    r"|bash-input|bash-stdout|bash-stderr|command-name|command-message"
    r"|task-notification)>.*?</\1>", re.S)


def jsonl_entries(path):
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.strip()
            if not raw:
                continue
            try:
                e = json.loads(raw)
            except ValueError:
                continue
            if isinstance(e, dict):
                yield e


def _content(e):
    msg = e.get("message")
    return msg.get("content") if isinstance(msg, dict) else None


def widget_call(e):
    """Whether an entry calls a widget tool (show_widget and kin). A rendered
    widget can send chat text "as if the user typed it", and the transcript
    does not mark that input path. Any tool named for a widget counts, in any
    entry, sidechains included: erring wide only adds GAP lines."""
    c = _content(e)
    return isinstance(c, list) and any(
        isinstance(b, dict) and str(b.get("type", "")).endswith("tool_use")
        and "widget" in str(b.get("name", "")).lower() for b in c)


def human_turns(path):
    """(text, why) for each of the CEO's turns in a transcript, in order. why is
    WIDGET_WHY for a turn at or after the transcript's first widget call."""
    widget = False
    for e in jsonl_entries(path):
        widget = widget or widget_call(e)
        for t in user_texts(e):
            yield t, (WIDGET_WHY if widget else None)


def user_texts(e):
    """The CEO's own words in a transcript entry.

    Claude Code marks each user-role entry with its origin. Only
    origin.kind == "human" is read; "task-notification" (a background seat's
    result), "peer" (another agent's message) and entries with no origin
    (interruptions, injected context) are not his words, and neither are tool
    results (CTO review F4). An allowlist, not a blocklist.

    That a human-marked turn is one he typed is an inference, not a fact: a
    widget's sendPrompt sends text "as if the user typed it", and nothing in
    the format marks the input path (CTO re-review, section 5). human_turns
    therefore marks every turn at or after a widget call, which cannot PASS.
    """
    if e.get("type") != "user" or e.get("isMeta") or e.get("isSidechain"):
        return []
    origin = e.get("origin")
    if not (isinstance(origin, dict) and origin.get("kind") == "human"):
        return []
    if e.get("isCompactSummary") or e.get("toolUseResult") is not None:
        return []
    c = _content(e)
    if isinstance(c, str):
        parts = [c]
    elif isinstance(c, list):
        if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
            return []
        parts = [b.get("text", "") for b in c
                 if isinstance(b, dict) and b.get("type") == "text"]
    else:
        return []
    out = [norm(_STRIP_TAGS.sub(" ", p)).casefold() for p in parts]
    return [t for t in out if t]


def assistant_texts(e):
    if e.get("type") != "assistant" or e.get("isSidechain"):
        return []
    c = _content(e)
    if isinstance(c, str):
        return [c]
    if isinstance(c, list):
        return [b.get("text", "") for b in c
                if isinstance(b, dict) and b.get("type") == "text"]
    return []


_DR_QUOTE = re.compile(r'^>\s*\*"(?P<q>[^"*][^"]*)"\*')


def ceo_record(paths, ctx):
    """(the CEO's words as (text, why), one per turn or recorded quote; problems).

    A .jsonl transcript gives his human-origin turns, those at or after a
    widget call marked. A decision record (decisions/*.md, read as merged to
    main) gives only its blockquoted italic quotes, never its prose (CTO
    review F5), all marked: the record does not say who is quoted (N3), so a
    match there is a GAP until a "> CEO:" marker exists. Nothing else is
    read."""
    texts, problems = [], []
    for p in paths:
        p = Path(p)
        if ctx.report_path is not None and p.resolve() == ctx.report_path:
            problems.append("--ceo-words %s is the report itself; refused" % p)
            continue
        if p.suffix == ".jsonl":
            got = list(human_turns(p))
            texts.extend(got)
            if not got:
                problems.append("--ceo-words %s has no turn marked origin.kind \"human\", so "
                                "none of it is the CEO's words" % p)
            continue
        rel = None
        try:
            rel = p.resolve().relative_to(ctx.repo.resolve()).as_posix()
        except ValueError:
            pass
        if rel is None or not fnmatch.fnmatchcase(rel, "decisions/*.md"):
            problems.append("--ceo-words %s is neither a session transcript (.jsonl) nor a "
                            "decision record (decisions/*.md); refused" % p)
            continue
        text = ctx.main.read(rel) if ctx.main and ctx.main.sha else None
        if text is None:
            problems.append("--ceo-words %s is not on %s; a decision record counts as "
                            "merged" % (rel, ctx.main.name if ctx.main else "main"))
            continue
        quotes = [norm(m.group("q")).casefold() for m in
                  (_DR_QUOTE.match(l.translate(_TR).strip()) for l in text.splitlines()) if m]
        texts.extend((q, DR_WHY) for q in quotes if q)
    return texts, problems


def parse_when(value):
    """An ISO date or date-time as an aware UTC datetime, or None."""
    if not value:
        return None
    try:
        when = dt.datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=dt.timezone.utc)
    return when


def transcript_units(path, since=None):
    """(label, assistant text, the CEO's words before it or None).

    With since, messages stamped earlier are skipped, and so are unstamped
    ones, which cannot be shown to fall inside the period. The CEO's earlier
    words still count as his record.
    """
    if path.suffix != ".jsonl":
        yield path.name, path.read_text(encoding="utf-8"), None
        return
    users, order, msgs, widget = [], [], {}, False
    for k, e in enumerate(jsonl_entries(path)):
        widget = widget or widget_call(e)
        users.extend((t, WIDGET_WHY if widget else None) for t in user_texts(e))
        texts = assistant_texts(e)
        if not texts:
            continue
        msg = e.get("message") or {}
        mid = msg.get("id") or e.get("uuid") or "entry%d" % k
        if mid not in msgs:
            if since is not None:
                when = parse_when(e.get("timestamp"))
                if when is None or when < since:
                    msgs[mid] = None
                    continue
            msgs[mid] = []
            order.append((mid, len(users)))
        if msgs[mid] is not None:
            msgs[mid].extend(texts)
    for i, (mid, seen) in enumerate(order, 1):
        text = "\n".join(t for t in msgs[mid] if t)
        if text.strip():
            yield "%s#%d" % (path.name, i), text, users[:seen]


def _phrase_rx():
    alts = sorted({p.translate(_TR) for p in VIEW_PHRASES}, key=len, reverse=True)
    return re.compile(r"(?<![\w'])(?:%s)(?![\w'])" % "|".join(re.escape(a) for a in alts), re.I)


PHRASE_RX = _phrase_rx()


def screen(text):
    """M8(b): view phrases outside quotes, blockquotes, code, and a My view
    block in item 3. A My view line anywhere else is itself a hit, and what
    follows it is screened (CTO review F10)."""
    hits, in_fence, in_view = [], False, False
    in3 = set(n for n, _ in sections(text).get("item3", []))
    for n, raw in enumerate(text.splitlines(), 1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = raw.translate(_TR)
        vm = VIEW_RE.search(norm(s))
        if vm:
            if n not in in3:
                hits.append((n, "My view (outside item 3)", one_line(s.strip(), 100)))
                in_view = False
                continue
            # A view block is exempt only when its trigger is one rule 3 lists
            # (CTO re-review N2); otherwise what follows it is screened.
            problem = parse_view(vm.group("rest"))[2]
            in_view = problem is None
            if not in_view:
                hits.append((n, "My view (%s)" % problem.split(":")[0], one_line(s.strip(), 100)))
            continue
        if in_view:
            if label_of(s) or s.lstrip().startswith("#"):
                in_view = False
            else:
                continue
        if s.lstrip().startswith(">"):
            continue
        s = re.sub(r"`[^`]*`", " ", s)
        s = re.sub(r'"[^"\n]*"', " ", s)
        for m in PHRASE_RX.finditer(s):
            hits.append((n, m.group(0), one_line(s.strip(), 100)))
    return hits


def run_transcript(paths, repo, since=None):
    out = []
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(p.glob("*.jsonl")))
        elif p.is_file():
            files.append(p)
        else:
            out.append((FAIL, "M8", "transcript %s not found" % p))
    reports = failing = units = hit_units = hits_total = 0
    for f in files:
        try:
            unit_list = list(transcript_units(f, since))
        except (OSError, UnicodeDecodeError) as e:
            out.append((FAIL, "M8", "transcript %s cannot be read (%s)" % (f, e.__class__.__name__)))
            continue
        for label, text, ceo in unit_list:
            units += 1
            # A message is a report if it carries any of Annex A items 2-4, not
            # only item 2, so dropping item 2 does not escape M8(a) (CTO re-review N2).
            if any(label_of(l) in REPORT_LABELS for l in text.splitlines()):
                reports += 1
                ctx = Ctx(repo, None, ceo or [], None, form_only=True)
                res = check_item3(strip_hidden(text), ctx, "M8(a)")
                bad = [r for r in res if r[0] == FAIL]
                if bad:
                    failing += 1
                    out.append((FAIL, "M8(a)", "%s: %s" % (label, bad[0][2])))
                else:
                    # A check not made stays visible here too (a short quote, or
                    # one found only after a widget call).
                    out.extend((GAP, "M8(a)", "%s: %s" % (label, r[2]))
                               for r in res if r[0] == GAP)
            hits = screen(text)
            if hits:
                hit_units += 1
                hits_total += len(hits)
                for n, phrase, snip in hits:
                    out.append((HIT, "M8(b)", "%s line %d '%s': %s" % (label, n, phrase, snip)))
    out.append((FAIL if failing else PASS, "M8(a)",
                "%d of %d reports fail M2(iii) (reports are messages carrying Annex A "
                "item 2, 3 or 4)" % (failing, reports)))
    if hits_total:
        out.append((HIT, "M8(b)", "%d raw hits in %d of %d messages. Unconfirmed: the CGO "
                    "samples them and reports confirmed counts, never raw ones"
                    % (hits_total, hit_units, units)))
    else:
        out.append((PASS, "M8(b)", "no screen hits in %d messages (a screen; it has false "
                    "negatives)" % units))
    return out


# ------------------------------------------------------------------------- main

def emit(header, results):
    print(header)
    for status, check, msg in results:
        print("%-4s %s %s" % (status, check, one_line(msg, 1200)))
    counts = {s: sum(1 for r in results if r[0] == s) for s in (FAIL, PASS, GAP, HIT)}
    # The RESULT line is what gets attached to a decision request, and the exit
    # status is what automation reads. Neither says PASS while a GAP stands.
    if counts[FAIL]:
        verdict, code = FAIL, 1
    elif counts[GAP]:
        verdict, code = "PASS-WITH-GAPS", 3
    else:
        verdict, code = PASS, 0
    tail = ", ".join("%d %s" % (counts[s], s.lower()) for s in (FAIL, PASS, GAP, HIT) if counts[s])
    note = " (each gap is a check not made; read the GAP lines)" if code == 3 else ""
    print("RESULT: %s (%s)%s" % (verdict, tail or "no checks", note))
    return code


def repo_root(arg):
    if arg:
        return Path(arg).resolve()
    out = git(Path.cwd(), "rev-parse", "--show-toplevel")
    return Path(out.strip()) if out and out.strip() else Path.cwd()


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="omission-check.py",
        description="Omission check (M2) and view screen (M8), roles/coordinator.md Annex E.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report", help="M2 over one report")
    r.add_argument("report", help="the report file, or - for stdin")
    r.add_argument("sources", nargs="*", help="the source artifacts the report covers")
    r.add_argument("--ceo-words", action="append", default=[], metavar="PATH")
    r.add_argument("--today", metavar="YYYY-MM-DD")
    r.add_argument("--main-ref", metavar="REF")
    r.add_argument("--repo", metavar="DIR")
    t = sub.add_parser("transcript", help="M8 over transcript files")
    t.add_argument("paths", nargs="+")
    t.add_argument("--repo", metavar="DIR")
    t.add_argument("--since", metavar="WHEN",
                   help="count only messages stamped at or after this ISO date or "
                        "date-time (UTC unless stated), e.g. when D12 came into force")
    a = ap.parse_args(argv)
    repo = repo_root(a.repo)

    if a.cmd == "transcript":
        since = parse_when(a.since)
        if a.since and since is None:
            print("omission-check: --since must be an ISO date or date-time", file=sys.stderr)
            return 2
        results = run_transcript(a.paths, repo, since)
        header = "omission-check %s transcript · files: %d · since: %s" % (
            VERSION, len(a.paths), since.isoformat() if since else "all messages")
        return emit(header, results)

    try:
        today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    except ValueError:
        print("omission-check: --today must be YYYY-MM-DD", file=sys.stderr)
        return 2
    main_ref = Main(repo, a.main_ref)
    report_path = None if a.report == "-" else Path(a.report).resolve()
    ctx = Ctx(repo, main_ref, None, today, report_path=report_path)
    problems = []
    try:
        if a.report == "-":
            report, name = sys.stdin.read(), "stdin"
        else:
            report, name = Path(a.report).read_text(encoding="utf-8"), a.report
        if a.ceo_words:
            ctx.ceo, problems = ceo_record(a.ceo_words, ctx)
    except (OSError, UnicodeDecodeError) as e:
        print("omission-check: cannot read input: %s" % e, file=sys.stderr)
        return 2
    # What the CEO cannot see does not count (CTO review F1).
    report = strip_hidden(report)
    results = [check_integrity(ctx)]
    results += [(FAIL, "CEO words", p) for p in problems]
    results += check_item3(report, ctx)
    results += check_item4(report, ctx)
    results += check_sources(report, a.sources, ctx)
    header = "omission-check %s report · %s · sources: %d · main: %s · today: %s · CEO words: %s" % (
        VERSION, name, len(a.sources), main_ref.describe(), today.isoformat(),
        "%d text(s) from %d file(s)" % (len(ctx.ceo or []), len(a.ceo_words))
        if a.ceo_words else "none given")
    return emit(header, results)


if __name__ == "__main__":
    sys.exit(main())
