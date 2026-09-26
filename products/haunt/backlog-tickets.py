#!/usr/bin/env python3
"""Generate the Haunts ticket set (title, body, labels, fields) from backlog.csv
and requirements.md, per D27 as amended by D31: tickets carry a copy of the
requirement and its acceptance criteria, stamped with the requirements.md
commit they were copied from. requirements.md stays the source of truth.

Usage: python3 products/haunt/backlog-tickets.py <repo-root> <requirements-sha> > tickets.json
"""
import csv, json, re, subprocess, sys

ROOT, SHA = sys.argv[1], sys.argv[2]
REQ_PATH = "products/haunt/requirements.md"
PLAN_PATH = "products/haunt/backlog-plan.md"
BLOB = "https://github.com/deopea-david/candour/blob"

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


# Section number -> heading anchor.
anchors = {}
for line in req_text.split("\n"):
    m = re.match(r"^#{2,3} (\d+(?:\.\d+)*)\.? (.*)$", line)
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
    parts = re.split(r"(?:(?<=^)|(?<=[.;:] )|(?<=\*\* ))\(([a-z])\)\s", ac)
    if len(parts) < 3:
        return None
    head, letters, bodies = parts[0].strip(), parts[1::2], parts[2::2]
    if letters != [chr(ord("a") + i) for i in range(len(letters))]:
        return None
    out = [head] if head else []
    out += [f"- [ ] **({l})** {b.strip()}" for l, b in zip(letters, bodies)]
    return "\n".join(out)


def sec_links(section):
    out = []
    for s in [x for x in section.split(";") if x]:
        a = anchors.get(s)
        out.append(f"[§{s}]({BLOB}/{SHA}/{REQ_PATH}" + (f"#{a})" if a else ")"))
    return ", ".join(out)


def first_sentence(text):
    t = re.sub(r"\s+", " ", text).strip()
    m = re.match(r"^(.+?[.!?])(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) <= 220 else s[:217].rstrip() + "…"


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

STAMP = (f"<sub>Copied from `{REQ_PATH}` at [`{SHA[:7]}`]({BLOB}/{SHA}/{REQ_PATH}) by `backlog-tickets.py`. "
         "**The requirements document is the source of truth; if this ticket and the document differ, the document wins.** "
         "A change to the requirement is a §24 scope-change row, and the ticket copy is regenerated from the new commit.</sub>")

SPK_STAMP = (f"<sub>Copied from `{PLAN_PATH}` §5 by `backlog-tickets.py`. "
             "**The backlog plan is the source of truth; if this ticket and the plan differ, the plan wins.**</sub>")

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
        kids = children.get(key, [])
        lines = [f"**{'Epic' if lvl == 'epic' else 'Feature'} {key}** — {r['title']}",
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
                  "", STAMP]
        title = f"[{key}] {r['title']}"
    elif is_spike:
        s = spikes.get(key)
        if not s:
            missing.append(key)
            continue
        lines = [f"**Planning task {key}** — owner: {s['owner']} · priority: {r['priority']} · platform: {r['platform']}", "",
                 "### What", s["what"], "", "### Unblocks", s["unblocks"], "", "### Source", s["source"], "",
                 f"**Done when** its written artifact is committed and the owning seat has recorded the result "
                 f"([backlog plan §5]({BLOB}/main/{PLAN_PATH})).", "", SPK_STAMP]
        title = f"[{key}] {r['title']}"
    else:
        rid = r["requirement_id"]
        if rid not in reqs:
            missing.append(rid)
            continue
        req, ac, prio, src = reqs[rid]
        ac_md = limbs(ac) or ac
        lines = [f"**{rid}** · {prio} · platform: {r['platform']} · owner: {r['owner_seat']} · {sec_links(r['section'])}", "",
                 "### Requirement", req, "", "### Acceptance criteria (QA-verifiable)", ac_md, "",
                 "### Source", src]
        if key in BLOCKED_BY:
            lines += ["", f"**Blocked by:** {BLOCKED_BY[key]}"]
        lines += ["", "QA verifies against `requirements.md` at a recorded commit, and records that SHA at Done.", "", STAMP]
        title = f"[{rid}] {r['title']}"

    body = "\n".join(lines)
    if len(body) > 60000:
        sys.exit(f"{key}: body too long ({len(body)})")
    tickets.append(dict(key=key, level=lvl, parent=r["parent_key"], title=title[:250], body=body, labels=labels,
                        fields={"Level": "spike" if is_spike else lvl, "Key": key, "Requirement ID": r["requirement_id"],
                                "Section": r["section"], "Priority": r["priority"], "Platform": r["platform"],
                                "Owner seat": r["owner_seat"], "Blocked by": BLOCKED_BY.get(key, "")}))

if missing:
    sys.exit(f"unmatched keys: {missing}")
json.dump(tickets, sys.stdout, ensure_ascii=False, indent=1)
print(f"{len(tickets)} tickets", file=sys.stderr)
