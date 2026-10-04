#!/usr/bin/env python3
"""Omission check (M2) and view screen (M8) for the Coordinator seat.

Owner: the CGO. roles/coordinator.md, Annex E: "The CGO owns and maintains the
script", so the Coordinator runs it and never edits it (exception (iii), D4a).
Changes to this file, to ALLOWLIST and to VIEW_PHRASES are drafted by the CGO.
Spec: pipeline/amendment-draft-coordinator.md section 11 item 18, and Annex E
of roles/coordinator.md (M2 (i)-(iii), M8). Template markers still owed:
pipeline/omission-check-markers.md.

  python3 scripts/omission-check.py report REPORT [SOURCE ...] [options]
  python3 scripts/omission-check.py transcript PATH [PATH ...]

report      Runs M2 over one report (a file, or - for stdin) against the source
            artifacts it covers. Attach the output under Annex A item 5.
              (i)   every fatal or serious objection headline, every 5.2 date
                    under 7 days, and every marked block and failed QA limb in
                    the sources appears verbatim in the report
              (ii)  every "Work I started without asking" authority resolves to
                    an allowlisted file and line on main, the CEO's recorded
                    words, or a seat's recommendation or next-steps section
              (iii) item 3 carries "No view offered." or a "My view - trigger:"
                    line naming a listed trigger, with the kind of reference
                    honest-broker rule 3 requires
            Options:
              --ceo-words PATH  the CEO's recorded words: a session transcript
                                (.jsonl; only his own messages are read) or a
                                text file such as a decision record. Repeatable.
              --today DATE      ISO date for the 5.2 arithmetic (default: today)
              --main-ref REF    the ref that stands for main (default: origin/main,
                                else main)
              --repo DIR        repository root (default: the git top level)

transcript  Runs M8 over main-session transcript files (.jsonl, text or
            markdown files, or directories holding .jsonl), at a phase review:
              (a) reports whose item 3 fails M2(iii); references are checked for
                  form only, and an "asked" quote against the CEO's earlier
                  messages in the same transcript
              (b) view phrases outside a "My view" block. A lexical screen with
                  false positives and false negatives. Its hits are raw: the CGO
                  samples them and reports confirmed counts, never raw ones.
            Options:
              --since WHEN  count only messages stamped from then on (for
                            example, from D12 coming into force); unstamped
                            messages are then left out

Output is plain text, one line per check:
  PASS  the check was made and passed
  FAIL  the check was made and failed, or could not be made from what was given
  GAP   a check the script cannot make; never read it as a pass
  HIT   an M8(b) screen hit, unconfirmed
Exit status: 1 if any line is FAIL, 2 on a usage or input error, else 0.
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

VERSION = "1.0"
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
NOT_AUTHORITY = ("STATUS.md", "*/STATUS.md", "*standup*", "*commission*")

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

PASS, FAIL, GAP, HIT = "PASS", "FAIL", "GAP", "HIT"

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


# ------------------------------------------------------- Annex A report shape

LABELS = (
    ("hear", ("what you may not want to hear",)),
    ("item3", ("seats' recommendations", "seat recommendations",
               "seats recommendations")),
    ("item4", ("work i started without asking",)),
    ("item5", ("omission-check output", "omission check output")),
    ("item6", ("links",)),
)
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
RECO = re.compile(r"recommend|next[- ]steps?", re.I)


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


def quote_found(quote, texts):
    """Every fragment of the quote (split at an ellipsis) is in one text."""
    frags = re.split(r"\[?(?:…|\.\.\.)\]?", norm(quote))
    frags = [f.strip(" .,;:!?").casefold() for f in frags]
    frags = [f for f in frags if re.search(r"\w", f)]
    return bool(frags) and all(any(f in t for t in texts) for f in frags)


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

    def __init__(self, repo, ref=None):
        self.repo, self.name, self.sha, self.cache = repo, None, None, {}
        self.tried = [ref] if ref else ["origin/main", "main"]
        for cand in self.tried:
            out = git(repo, "rev-parse", "--verify", "--quiet", cand + "^{commit}")
            if out and out.strip():
                self.name, self.sha = cand, out.strip()
                break

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
    def __init__(self, repo, main, ceo, today, form_only=False):
        self.repo, self.main, self.ceo = repo, main, ceo
        self.today, self.form_only = today, form_only


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
        return True, "%s on %s" % (ref, ctx.main.name)
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
    if not_authority(ref.path):
        return False, "%s is state, not authority (Annex D, 'Not authority')" % ref.path
    text = read_tree(ctx, ref.path)
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
        if RECO.search(above[-1]):
            return True, "case (b): %s, under '%s'" % (ref, one_line(above[-1], 60))
        return False, "%s:%d sits under '%s', not a recommendation or next-steps section" % (
            ref.path, ref.line, one_line(above[-1], 60))
    if ref.anchor:
        for _, h in headings:
            if slug(h) == ref.anchor.lower():
                if RECO.search(h):
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


def check_view_line(n, rest, ctx, check):
    where = "item 3, line %d" % n
    parts = REF_SPLIT.split(rest, maxsplit=1)
    ref = parts[1].strip() if len(parts) == 2 else ""
    names = [t.strip(" .").lower()
             for t in re.split(r"[,|/;+&]|\band\b", parts[0])]
    names = [t for t in names if t]
    if not names:
        return [(FAIL, check, "%s: 'My view' names no trigger" % where)]
    bad = [t for t in names if t not in TRIGGERS]
    if bad:
        return [(FAIL, check, "%s: trigger not on rule 3's list: %s (listed: %s)"
                 % (where, ", ".join(repr(b) for b in bad), ", ".join(TRIGGERS)))]
    if not ref:
        return [(FAIL, check, "%s: no '— reference:' part" % where)]
    out = []
    for t in names:
        ok, msg = REFERENCE_CHECKS[t](ref, ctx)
        out.append((PASS if ok else FAIL, check,
                    "%s: trigger '%s': %s" % (where, t, msg)))
    return out


def ref_asked(ref, ctx):
    qs = quotes_in(ref)
    if not qs:
        return False, "needs the CEO's words, quoted (rule 3)"
    if ctx.ceo is None:
        return True, "quote present (form only: not checked against a record; " \
                     "pass --ceo-words to check it)"
    missing = [q for q in qs if not quote_found(q, ctx.ceo)]
    if missing:
        return False, "quote not found in the CEO's recorded words: \"%s\"" % one_line(missing[0], 80)
    return True, "quote found in the CEO's recorded words"


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
        ok, msg = resolve_authority(v, ctx)
        out.append((PASS if ok else FAIL, check, "item 4, line %d: %s" % (n, msg)))
    return out


def resolve_authority(v, ctx):
    reasons = []
    refs = path_refs(norm(v))
    for r in refs:
        if allowlisted(r.path):
            ok, msg = resolve_allowlisted(r, ctx, require_line=True)
            if ok:
                return True, "case (a): " + msg
            reasons.append(msg)
    qs = quotes_in(v)
    if qs:
        if ctx.ceo is None:
            reasons.append("quotes the CEO, but no --ceo-words record was given to "
                           "resolve it against")
        else:
            missing = [q for q in qs if not quote_found(q, ctx.ceo)]
            if not missing:
                return True, "the CEO's recorded words"
            reasons.append("quote not found in the CEO's recorded words: \"%s\""
                           % one_line(missing[0], 80))
    for r in refs:
        if not allowlisted(r.path):
            ok, msg = resolve_seat_section(r, ctx)
            if ok:
                return True, msg
            reasons.append(msg)
    if not refs and not qs:
        reasons.append("cites no file and quotes no words")
    return False, "authority does not resolve: " + "; ".join(reasons)


# ------------------------------------------------------------------------ M2(i)

TIER = re.compile(r"\[(FATAL|SERIOUS)\b[^\]]*\]")
OID = re.compile(r"^(?P<id>[A-Z]{1,3}\d+(?:-[A-Z]{1,3}\d+)*)(?=[\s.:—–-]|$)\.?")
BOLD_LEAD = re.compile(r"^(?:[-*+]\s+)?\*\*(?P<b>.+?)\*\*")
LIST_TAG = re.compile(r"^[-*+]\s+\[(?:FATAL|SERIOUS)")
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


def objections_in(path, text):
    heads, rows = [], []
    for n, raw in enumerate(text.splitlines(), 1):
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
        if s.startswith("#"):
            body, whole = s.lstrip("#").strip(), False
        else:
            m = BOLD_LEAD.match(s)
            if m and TIER.search(m.group("b")):
                body, whole = m.group("b"), False
            elif LIST_TAG.match(s):
                body, whole = s[1:].strip(), True
            else:
                continue
        t = TIER.search(body)
        if not t:
            continue
        title = norm(body[:t.start()] + " " + body[t.end():])
        idm = OID.match(title)
        oid = idm.group("id") if idm else None
        if idm and not whole:
            title = title[idm.end():]
        title = title.lstrip(" .:—–-").strip()
        if whole:
            # A tagged list item has no delimited headline: require the line.
            title = norm(body[:t.start()] + body[t.end():]).strip()
        if title:
            heads.append(Objection(t.group(1), oid, title, path, n,
                                   "list" if whole else "heading"))
    return heads, rows


def check_sources(report, sources, ctx, check="M2(i)"):
    out = []
    if not sources:
        return [(FAIL, check, "no source artifacts given, so M2(i) cannot run; name "
                 "the artifacts this report covers")]
    report_n = norm(report)
    heads, rows, texts = [], [], []
    for src in sources:
        p = Path(src)
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            out.append((FAIL, check, "source %s cannot be read (%s)" % (src, e.__class__.__name__)))
            continue
        texts.append((src, text))
        h, r = objections_in(src, text)
        heads.extend(h)
        rows.extend(r)
    seen = set(o.oid for o in heads if o.oid)
    objs = heads + [o for o in rows if not (o.oid and o.oid in seen)]
    for o in objs:
        where = "%s %s%s:%d" % (o.tier, (o.oid + " ") if o.oid else "", o.path, o.line)
        if norm(o.headline) in report_n:
            out.append((PASS, check, "objection %s: headline copied verbatim" % where))
        else:
            out.append((FAIL, check, "objection %s: headline not in the report verbatim: \"%s\""
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
                elif iso in report:
                    out.append((PASS, check, "5.2 date %s at %s:%d (%d days): copied"
                                % (iso, src, n, days)))
                else:
                    out.append((FAIL, check, "5.2 date %s at %s:%d is %s and not in the report"
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
    return (FAIL, check, "%s not in the report verbatim: \"%s\"" % (where, one_line(text, 1000)))


# ------------------------------------------------------------------- integrity

def check_integrity(ctx):
    check = "script"
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

_STRIP_TAGS = re.compile(
    r"<(system-reminder|local-command-stdout|local-command-stderr)>.*?</\1>", re.S)


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


def user_texts(e):
    """The CEO's own words in a transcript entry: no tool results, no injections."""
    if e.get("type") != "user" or e.get("isMeta") or e.get("isSidechain"):
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


def ceo_record(paths):
    texts = []
    for p in paths:
        p = Path(p)
        if p.suffix == ".jsonl":
            for e in jsonl_entries(p):
                texts.extend(user_texts(e))
        else:
            texts.append(norm(p.read_text(encoding="utf-8")).casefold())
    return texts


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
    users, order, msgs = [], [], {}
    for k, e in enumerate(jsonl_entries(path)):
        users.extend(user_texts(e))
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
    """M8(b): view phrases outside a My view block, quotes, blockquotes and code."""
    hits, in_fence, in_view = [], False, False
    for n, raw in enumerate(text.splitlines(), 1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = raw.translate(_TR)
        if VIEW_RE.search(norm(s)):
            in_view = True
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
            if any(label_of(l) == "hear" for l in text.splitlines()):
                reports += 1
                ctx = Ctx(repo, None, ceo if ceo else None, None, form_only=True)
                bad = [r for r in check_item3(text, ctx, "M8(a)") if r[0] == FAIL]
                if bad:
                    failing += 1
                    out.append((FAIL, "M8(a)", "%s: %s" % (label, bad[0][2])))
            hits = screen(text)
            if hits:
                hit_units += 1
                hits_total += len(hits)
                for n, phrase, snip in hits:
                    out.append((HIT, "M8(b)", "%s line %d '%s': %s" % (label, n, phrase, snip)))
    out.append((FAIL if failing else PASS, "M8(a)",
                "%d of %d reports fail M2(iii) (reports are messages carrying "
                "'What you may not want to hear')" % (failing, reports)))
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
    verdict = FAIL if counts[FAIL] else PASS
    tail = ", ".join("%d %s" % (counts[s], s.lower()) for s in (FAIL, PASS, GAP, HIT) if counts[s])
    note = " (a gap is never a pass)" if counts[GAP] and verdict == PASS else ""
    print("RESULT: %s (%s)%s" % (verdict, tail or "no checks", note))
    return 1 if counts[FAIL] else 0


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
    try:
        if a.report == "-":
            report, name = sys.stdin.read(), "stdin"
        else:
            report, name = Path(a.report).read_text(encoding="utf-8"), a.report
        ceo = ceo_record(a.ceo_words) if a.ceo_words else None
    except (OSError, UnicodeDecodeError) as e:
        print("omission-check: cannot read input: %s" % e, file=sys.stderr)
        return 2
    main_ref = Main(repo, a.main_ref)
    ctx = Ctx(repo, main_ref, ceo, today)
    results = [check_integrity(ctx)]
    results += check_item3(report, ctx)
    results += check_item4(report, ctx)
    results += check_sources(report, a.sources, ctx)
    header = "omission-check %s report · %s · sources: %d · main: %s · today: %s · CEO words: %s" % (
        VERSION, name, len(a.sources), main_ref.describe(), today.isoformat(),
        "%d file(s)" % len(a.ceo_words) if a.ceo_words else "none given")
    return emit(header, results)


if __name__ == "__main__":
    sys.exit(main())
