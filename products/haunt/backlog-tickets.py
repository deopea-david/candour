#!/usr/bin/env python3
"""Generate the Haunts ticket set (title, body, labels, fields) from backlog.csv
and requirements.md.

Governing decisions (decisions/2026-09-16-haunt-gate.md):
  D27 as amended by D31 - tickets carry a copy of the requirement and its
      acceptance criteria, stamped with the requirements.md commit they were
      copied from. requirements.md stays the source of truth.
  D33 - requirement tickets carry the files sections, marked TBD until the
      CTO has designed the architecture.
  D34 - the ticket format of products/haunt/agentic-agile-adoption.md §3.3:
      a GENERATED region (replaced whole on regeneration) and a CTO-MAINTAINED
      region (Files / Interfaces / File ownership) that regeneration never touches.

Usage:
  python3 products/haunt/backlog-tickets.py <repo-root> <requirements-sha> > tickets.json
  python3 products/haunt/backlog-tickets.py <repo-root> <requirements-sha> --self-test

Regenerating a ticket later (after a §24 scope-change row changes a requirement):
  1. Run this script at the new requirements.md commit to get the fresh body.
  2. Fetch the ticket's CURRENT body from GitHub.
  3. new_body = regenerate_body(current_body, fresh_body)
     This replaces only the text between GEN_BEGIN (matched by prefix, since it
     carries the old SHA) and GEN_END, and keeps everything after GEN_END - the
     CTO-maintained region - exactly as it is. It raises (fails loudly) if either
     marker is missing, duplicated or out of order in either body; it never guesses.
  4. Write new_body back to the issue. (The GitHub update code is not written yet.)
--self-test checks that round trip on every generated ticket.
"""
import csv, json, re, subprocess, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
SELF_TEST = "--self-test" in sys.argv[1:]
ROOT, SHA = args[0], args[1]
REQ_PATH = "products/haunt/requirements.md"
PLAN_PATH = "products/haunt/backlog-plan.md"
DEC_PATH = "decisions/2026-09-16-haunt-gate.md"
BLOB = "https://github.com/deopea-david/candour/blob"

GEN_BEGIN_PREFIX = "<!-- generated:begin"
GEN_BEGIN = f"{GEN_BEGIN_PREFIX} requirements.md@{SHA[:7]}: replaced on regeneration; do not edit by hand -->"
GEN_BEGIN_SPIKE = f"{GEN_BEGIN_PREFIX} backlog-plan.md §5: replaced on regeneration; do not edit by hand -->"
GEN_END = "<!-- generated:end -->"
CTO_MARK = "<!-- cto-maintained: regeneration never overwrites below this line -->"

req_text = subprocess.check_output(["git", "-C", ROOT, "show", f"{SHA}:{REQ_PATH}"], text=True)
plan_text = open(f"{ROOT}/{PLAN_PATH}").read()
rows = list(csv.DictReader(open(f"{ROOT}/products/haunt/backlog.csv")))


def split_cells(line):
    # Split a markdown table row on pipes that are not inside backticks or escaped.
    cells, cur, tick = [], "", False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur += "|"; i += 2; continue
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick:
            cells.append(cur.strip()); cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells[1:-1]


def anchor(heading):
    h = heading.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


# Section number -> heading anchor (##, ### and ####).
anchors = {}
for line in req_text.split("\n"):
    m = re.match(r"^#{2,4} (\d+(?:\.\d+)*)\.? (.*)$", line)
    if m:
        anchors.setdefault(m.group(1), anchor(f"{m.group(1)}{'.' if line.startswith('## ') else ''} {m.group(2)}"))

# Requirement ID -> (requirement, acceptance, priority, source)
reqs = {}
for line in req_text.split("\n"):
    m = re.match(r"^\| \*\*([A-Z0-9]+-\d+[a-z]?)\*\*", line)
    if not m:
        continue
    cells = split_cells(line)
    if len(cells) != 5:
        continue
    rid = m.group(1)
    if rid in reqs:
        sys.exit(f"duplicate requirement row {rid}")
    reqs[rid] = cells[1:]

# Spike rows from plan §5.
spikes = {}
for line in plan_text.split("\n"):
    m = re.match(r"^\| \*\*(SPK-\d+)\*\* \|", line)
    if m:
        c = split_cells(line)
        spikes[m.group(1)] = dict(what=c[1], owner=c[2], unblocks=c[3], source=c[4])


def limbs(ac):
    """Split '(a) ... (b) ...' into checklist limbs when the letters run a, b, c... in order."""
    # A limb starts at the beginning, or after '. ', '; ', ': ', or '* ' (closing bold or italic,
    # e.g. a quoted string ending *"...here."* before "(b)", as in CAP-4 and CAP-5).
    parts = re.split(r"(?:(?<=^)|(?<=[.;:] )|(?<=\* ))\(([a-z])\)\s", ac)
    if len(parts) < 3:
        return None
    head, letters, bodies = parts[0].strip(), parts[1::2], parts[2::2]
    if letters != [chr(ord("a") + i) for i in range(len(letters))]:
        return None
    out = [head] if head else []
    out += [f"- [ ] **({l})** {b.strip()}" for l, b in zip(letters, bodies)]
    return "\n".join(out)


def sec(s):
    a = anchors.get(s)
    return f"[§{s}]({BLOB}/{SHA}/{REQ_PATH}" + (f"#{a})" if a else ")")


def sec_links(section):
    return ", ".join(sec(s) for s in section.split(";") if s)


def first_sentence(text):
    t = re.sub(r"\s+", " ", text).strip()
    # A sentence may end inside bold, italics or quotes: '.**', '."*', '.)'.
    m = re.match(r"^(.+?[.!?][*\"”’)]*)(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) <= 220 else s[:217].rstrip() + "…"


ID_PATTERN = re.compile(r"\b([A-Z][A-Z0-9]{1,5}-\d+[a-z]?)\b")


def mentions(rid, *texts):
    seen = []
    for t in texts:
        for m in ID_PATTERN.findall(t):
            if m in reqs and m != rid and m not in seen:
                seen.append(m)
    return seen


PROMISE = {"DATA-4", "VEN-7", "VEN-8", "VEN-9", "VEN-10", "VEN-11", "VEN-12", "CONF-3", "SESS-1", "PRIV-1", "PRIV-8", "CAP-4", "VEN-21"}
STANDING = {"VEN-24", "CONF-9", "VEN-14", "VEN-15", "VEN-21", "VPAGE-5"}
MIXED = {"HEAD-4", "HEAD-5", "HEAD-9", "HEAD-13", "HEAD-14", "HEAD-15", "PHOTO-9"}
CSO = {f"DATA-{n}" for n in range(6, 14)} | {"DATA-15", "ENT-11", "PRIV-8", "PHOTO-11", "CAP-1", "SPK-06"}
NEEDS_CEO = {"PLAT-5", "PLAT-7"}
BLOCKED_BY = {"VEN-24": "CAP-10", "CAP-10": "SPK-02", "HEAD-10": "SPK-05", "NOT-3": "SPK-07", "NOT-5": "SPK-07",
              "ENT-10": "SPK-10", "ENT-8": "SPK-14", "DATA-6": "SPK-06", "DATA-7": "SPK-06", "DATA-8": "SPK-06",
              "DATA-12": "SPK-12", "LOOK-2": "SPK-04", "DATA-15": "SPK-13", "ONB-3": "SPK-08", "LOOK-5": "PLAT-7"}
for n in range(1, 12):
    BLOCKED_BY[f"PHOTO-{n}"] = "SPK-11"

byk = {r["key"]: r for r in rows}
children = {}
for r in rows:
    children.setdefault(r["parent_key"], []).append(r)


def epic_of(r):
    while r["level"] != "epic":
        r = byk[r["parent_key"]]
    return r["key"]


for r in rows:
    if r["level"] == "task" and not r["key"].startswith("SPK"):
        if epic_of(r) == "EP-VEN" or r["parent_key"] in ("FT-CONF-2", "FT-CONF-3"):
            BLOCKED_BY.setdefault(r["key"], "SPK-01")

REQ_LINK = f"[`{REQ_PATH}`]({BLOB}/{SHA}/{REQ_PATH})"
DEC_LINK = f"[decision record]({BLOB}/{SHA}/{DEC_PATH})"

STAMP = (f"<sub>Copied from `{REQ_PATH}` at [`{SHA[:7]}`]({BLOB}/{SHA}/{REQ_PATH}) by `backlog-tickets.py`. "
         "**The requirements document is the source of truth; if this ticket and the document differ, the document wins.** "
         "A change to the requirement is a §24 scope-change row, and the ticket copy is regenerated from the new commit.</sub>")

SPK_STAMP = (f"<sub>Copied from `{PLAN_PATH}` §5 by `backlog-tickets.py`. "
             "**The backlog plan is the source of truth; if this ticket and the plan differ, the plan wins.**</sub>")

# Product-wide invariants (agentic-agile-adoption.md §3.3 row 5a). One-line summaries; the linked requirement governs.
PRODUCT_WIDE = [
    f"- **MEM-1** ({sec('3.1')}): Haunts never encourages drinking, and never rewards the frequency or volume of visits; "
    "*\"a count may appear only as a plain fact.\"*",
    f"- **DFLT-1** ({sec('3.2')}): where a setting has a more and a less protective value, the default is the protective one, "
    "the user can change it, and every setting is in the settings register.",
    f"- **PRIV-8** ({sec('14')}): no analytics, no telemetry SDK, no bundled measurement of any kind; "
    "no outbound call site outside the backup module.",
    f"- **PRIV-1** ({sec('14')}), as narrowed by D12 ({sec('12.2.8')}): Candour receives nothing, and the user's data "
    "goes nowhere but their own cloud.",
]
PW_NOTE = "*Summaries only; each linked requirement governs.*"

TBD_LINE = ("**TBD** — set by the CTO once the architecture ADR exists, at wave planning (D33). "
            "This ticket cannot enter Ready while this says TBD.")


def cto_region():
    return [CTO_MARK, "",
            "### Files to create or modify", TBD_LINE, "",
            "### Interfaces to implement", TBD_LINE, "",
            "### File ownership", "Wave: TBD", "",
            "| File | Owned by this ticket in wave | Notes |", "|---|---|---|", "| TBD | | |"]


def specific_invariants(key):
    out = []
    if key in PROMISE:
        out.append(f"- **On the promise line** ({sec('20.1')}). Cutting or weakening it is an overrule or an amendment, not a scope change.")
    if key in STANDING:
        out.append(f"- **A standing condition of Block 4** ({sec('7.7.5')}). A change here re-engages the CTO's block.")
    if key in MIXED:
        out.append("- **Mixed priority:** limbs carry different priorities; read them in the document.")
    if key in CSO:
        out.append("- **Security-relevant:** the CSO reviews the PR (`needs:cso-review`).")
    return out


def parent_line(r):
    p = byk.get(r["parent_key"])
    return f"Parent: {p['key']} — {p['title']}" if p else "Parent: none"


def regenerate_body(current, fresh):
    """Return `current` with its generated region replaced by `fresh`'s.

    Keeps everything outside the generated region (the CTO-maintained region)
    byte for byte. Raises ValueError if either body lacks exactly one begin
    marker followed by exactly one end marker.
    """
    def split(body, name):
        begins = [m.start() for m in re.finditer(re.escape(GEN_BEGIN_PREFIX), body)]
        ends = [m.start() for m in re.finditer(re.escape(GEN_END), body)]
        if len(begins) != 1 or len(ends) != 1 or begins[0] > ends[0]:
            raise ValueError(f"{name}: expected one '{GEN_BEGIN_PREFIX}' before one '{GEN_END}', "
                             f"found {len(begins)} begin and {len(ends)} end marker(s)")
        e = ends[0] + len(GEN_END)
        return body[:begins[0]], body[begins[0]:e], body[e:]
    pre, _, post = split(current, "current body")
    _, gen, _ = split(fresh, "fresh body")
    return pre + gen + post


tickets, missing = [], []
for r in rows:
    key, lvl = r["key"], r["level"]
    is_spike = key.startswith("SPK-")
    labels = [f"level:{'spike' if is_spike else lvl}", f"area:{epic_of(r)[3:].lower()}"]
    if r["owner_seat"]:
        labels.append(f"seat:{r['owner_seat']}")
    if r["priority"]:
        labels.append(f"prio:{r['priority'].lower()}")
    if r["platform"]:
        labels.append(f"platform:{r['platform']}")
    for s, lab in ((PROMISE, "promise-line"), (STANDING, "standing-condition"), (MIXED, "mixed-priority"),
                   (CSO, "needs:cso-review"), (NEEDS_CEO, "needs:ceo")):
        if key in s:
            labels.append(lab)

    if lvl in ("epic", "feature"):
        # Epics and features: content unchanged (adoption note §3.3); wrapped in markers so they regenerate cleanly.
        kids = children.get(key, [])
        lines = [GEN_BEGIN, f"**{'Epic' if lvl == 'epic' else 'Feature'} {key}** — {r['title']}",
                 f"Requirements: {sec_links(r['section'])} · accountable seat: {r['owner_seat']}", ""]
        if lvl == "epic":
            lines += ["| Feature | Title | Tasks |", "|---|---|---|"]
            for k in kids:
                tk = ", ".join(t["key"] for t in children.get(k["key"], []))
                lines.append(f"| {k['key']} | {k['title']} | {tk} |")
        else:
            lines += ["| Task | Priority | Platform | What it requires |", "|---|---|---|---|"]
            for t in kids:
                what = first_sentence(reqs[t["requirement_id"]][0]) if t["requirement_id"] in reqs else (
                    first_sentence(spikes[t["key"]]["what"]) if t["key"] in spikes else t["title"])
                lines.append(f"| {t['key']} | {t['priority']} | {t['platform']} | {what.replace('|', '/')} |")
        lines += ["", "Progress rolls up from the sub-issues. Done means every sub-issue is Done (QA-verified)"
                  + (" and the feature has been demonstrated end to end on its platforms." if lvl == "feature" else "."),
                  "", STAMP, GEN_END]
        title = f"[{key}] {r['title']}"
    elif is_spike:
        s = spikes.get(key)
        if not s:
            missing.append(key)
            continue
        lines = [GEN_BEGIN_SPIKE,
                 f"**Planning task {key}** · {r['priority']} · platform: {r['platform']} · owner: {s['owner']}", "",
                 "### Summary", first_sentence(s["what"]), "",
                 "### What", s["what"], "",
                 "### Unblocks", s["unblocks"], "",
                 "### Origin and context", s["source"], "",
                 "### Negative constraints",
                 "- A spike produces a written answer. No product code reaches `main` under a spike ticket; "
                 "prototype code stays on its spike branch. *(Proposed by the PM/BA; the CTO confirms or changes this rule.)*", "",
                 "### Dependencies", parent_line(r), "",
                 "### Done when",
                 f"Its written artifact is committed and the owning seat has recorded the result "
                 f"([backlog plan §5]({BLOB}/main/{PLAN_PATH})). QA does not verify spikes; the seat that consumes the answer confirms it.",
                 "", SPK_STAMP, GEN_END, ""] + cto_region()
        title = f"[{key}] {r['title']}"
    else:
        rid = r["requirement_id"]
        if rid not in reqs:
            missing.append(rid)
            continue
        req, ac, prio, src = reqs[rid]
        ac_md = limbs(ac) or ac
        spec_inv = specific_invariants(key)
        ment = mentions(rid, req, ac)
        deps = [f"- Blocked by: {BLOCKED_BY.get(key, 'nothing recorded')}", f"- {parent_line(r)}"]
        deps.append("- Mentioned in the text (not necessarily a dependency): " + (", ".join(ment) if ment else "none"))
        lines = [GEN_BEGIN,
                 f"**{rid}** · {prio} · platform: {r['platform']} · owner: {r['owner_seat']} · {sec_links(r['section'])}", "",
                 "### Summary", first_sentence(req), "",
                 "### Origin and context", src, "",
                 f"The CEO's words are quoted in the decision entries named here ({DEC_LINK}); they are not copied into tickets.", "",
                 "### Requirement", req, "",
                 "### Acceptance criteria (QA-verifiable)", ac_md, "",
                 "### Invariants to preserve", "**Product-wide, on every ticket:**", *PRODUCT_WIDE, PW_NOTE]
        if spec_inv:
            lines += ["", "**This ticket:**", *spec_inv]
        lines += ["",
                  "### Negative constraints",
                  f"- Nothing listed in {REQ_LINK} {sec('18')} (Explicitly out of scope for v1) is built under this ticket.",
                  "- Story-level constraints: set at wave planning.", "",
                  "### Dependencies", *deps, "",
                  "### Verification",
                  "QA verifies every limb against `requirements.md` at a recorded commit, and records that SHA in "
                  "\"Verified against\" at Done. Only QA moves this ticket to Done (D30, D34).", "",
                  STAMP, GEN_END, ""] + cto_region()
        title = f"[{rid}] {r['title']}"

    body = "\n".join(lines)
    if len(body) > 60000:
        sys.exit(f"{key}: body too long ({len(body)})")
    tickets.append(dict(key=key, level=lvl, parent=r["parent_key"], title=title[:250], body=body, labels=labels,
                        fields={"Level": "spike" if is_spike else lvl, "Key": key, "Requirement ID": r["requirement_id"],
                                "Section": r["section"], "Priority": r["priority"], "Platform": r["platform"],
                                "Owner seat": r["owner_seat"], "Blocked by": BLOCKED_BY.get(key, ""),
                                "Wave": "", "QA attempts": 0}))

if missing:
    sys.exit(f"unmatched keys: {missing}")

if SELF_TEST:
    # Simulate a CTO edit, then regenerate from a changed fresh body; the CTO region must survive untouched.
    failures = 0
    for t in tickets:
        edited = t["body"].replace("| TBD | | |", "| src/x.ts | M1.W1 | CTO edit |")
        fresh = t["body"].replace(GEN_END, "changed line\n" + GEN_END)
        out = regenerate_body(edited, fresh)
        if "changed line" not in out or edited.split(GEN_END, 1)[1] != out.split(GEN_END, 1)[1]:
            failures += 1
            print(f"FAIL {t['key']}", file=sys.stderr)
    for bad in ("no markers here", GEN_END + "\n" + GEN_BEGIN):
        try:
            regenerate_body(bad, tickets[0]["body"])
            failures += 1
            print("FAIL: missing/out-of-order markers not rejected", file=sys.stderr)
        except ValueError:
            pass
    print(f"self-test: {len(tickets)} tickets, {failures} failure(s)", file=sys.stderr)
    sys.exit(1 if failures else 0)

json.dump(tickets, sys.stdout, ensure_ascii=False, indent=1)
print(f"{len(tickets)} tickets", file=sys.stderr)
