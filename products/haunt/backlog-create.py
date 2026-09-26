#!/usr/bin/env python3
"""Create the Haunts backlog on GitHub from backlog-tickets.py output (D27-D34).

Resumable: progress is written to products/haunt/backlog-issues.csv after every
step, and a rerun skips whatever is already done. Writes nothing without --apply.

Usage:
  python3 products/haunt/backlog-tickets.py . <sha> > tickets.json
  python3 products/haunt/backlog-create.py tickets.json            # dry run
  python3 products/haunt/backlog-create.py tickets.json --apply    # create
"""
import csv, json, os, subprocess, sys, time

OWNER, REPO, PROJECT_NO = "deopea-david", "haunts", 1
MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backlog-issues.csv")
APPLY = "--apply" in sys.argv
tickets = json.load(open(sys.argv[1]))

EXTRA_LABELS = ["level:story", "spec-defect", "escaped", "blocked"]
COLOURS = {"level": "5319e7", "prio": "b60205", "platform": "0e8a16", "seat": "1d76db", "area": "c5def5"}
SPECIAL = {"promise-line": "d93f0b", "standing-condition": "fbca04", "mixed-priority": "fef2c0",
           "needs:cso-review": "e99695", "needs:ceo": "000000", "level:story": "5319e7",
           "spec-defect": "f9d0c4", "escaped": "b60205", "blocked": "d73a4a"}
SELECTS = {
    "Level": ["epic", "feature", "task", "spike", "story"],
    "Priority": ["BLOCKING", "MUST", "CUT-LINE", "PENDING-ESTIMATE"],
    "Platform": ["ios", "android", "both", "none"],
    "Owner seat": ["engineer", "qa", "cto", "cso", "cfo", "cgo", "ux-lead", "pm-ba", "ceo"],
    "Phase": ["M0", "M1", "M2", "M3", "M4", "M5"],
    "Estimate basis": ["In 2,090 h", "Added after the estimate — unsized", "Pending estimate", "n/a"],
}
TEXTS = ["Key", "Requirement ID", "Section", "Blocked by", "Wave", "Verified against"]
NUMBERS = ["QA attempts"]  # the board's existing "Estimate" number field carries the CTO's hours


def gh(*args, input=None, retries=6):
    for attempt in range(retries):
        p = subprocess.run(["gh", *args], input=input, capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout
        err = p.stderr + p.stdout
        if "rate limit" in err.lower() or "abuse" in err.lower() or "502" in err or "503" in err:
            wait = 60 * (attempt + 1)
            print(f"  rate-limited; waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
            continue
        raise SystemExit(f"gh {' '.join(args[:3])} failed: {err.strip()[:500]}")
    raise SystemExit("gave up after retries")


def graphql(query, **vars):
    args = ["api", "graphql", "-f", f"query={query}"]
    for k, v in vars.items():
        args += ["-F" if isinstance(v, int) else "-f", f"{k}={v}"]
    return json.loads(gh(*args))


def load_map():
    if not os.path.exists(MAP):
        return {}
    return {r["key"]: r for r in csv.DictReader(open(MAP))}


def save_map(m):
    cols = ["key", "number", "id", "node_id", "item_id", "linked", "fields"]
    with open(MAP, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for t in tickets:
            if t["key"] in m:
                w.writerow({c: m[t["key"]].get(c, "") for c in cols})


# ---- plan -------------------------------------------------------------------
labels = sorted({l for t in tickets for l in t["labels"]} | set(EXTRA_LABELS))
existing_labels = {x["name"] for x in json.loads(gh("label", "list", "-R", f"{OWNER}/{REPO}", "--limit", "200", "--json", "name"))}
proj = graphql("""query($o:String!,$n:Int!){user(login:$o){projectV2(number:$n){id fields(first:50){nodes{
  ... on ProjectV2Field{id name dataType}
  ... on ProjectV2SingleSelectField{id name dataType options{id name}}}}}}}""", o=OWNER, n=PROJECT_NO)["data"]["user"]["projectV2"]
PID = proj["id"]
fields = {f["name"]: f for f in proj["fields"]["nodes"] if f}
m = load_map()
todo = [t for t in tickets if t["key"] not in m]
print(f"labels to create: {len([l for l in labels if l not in existing_labels])}")
print(f"fields to create or reset: {[n for n in list(SELECTS) + TEXTS + NUMBERS if n not in fields or (n in SELECTS and {o['name'] for o in fields[n].get('options', [])} != set(SELECTS[n]))]}")
print(f"issues to create: {len(todo)} of {len(tickets)}; already mapped: {len(m)}")
if not APPLY:
    sys.exit("dry run only; pass --apply to create")

# ---- labels -----------------------------------------------------------------
for l in labels:
    if l in existing_labels:
        continue
    colour = SPECIAL.get(l) or COLOURS.get(l.split(":")[0], "ededed")
    gh("label", "create", l, "-R", f"{OWNER}/{REPO}", "--color", colour, "--force")
print("labels ok")

# ---- fields -----------------------------------------------------------------
for name, opts in SELECTS.items():
    f = fields.get(name)
    want = [{"name": o, "color": "GRAY", "description": ""} for o in opts]
    if f and {o["name"] for o in f.get("options", [])} == set(opts):
        continue
    if f and f["dataType"] == "SINGLE_SELECT":  # e.g. the template's own Priority field: reset its options
        q = "mutation($f:ID!,$o:[ProjectV2SingleSelectFieldOptionInput!]!){updateProjectV2Field(input:{fieldId:$f,singleSelectOptions:$o}){projectV2Field{... on ProjectV2SingleSelectField{id}}}}"
        gh("api", "graphql", "--input", "-", input=json.dumps({"query": q, "variables": {"f": f["id"], "o": want}}))
    else:
        q = "mutation($p:ID!,$n:String!,$o:[ProjectV2SingleSelectFieldOptionInput!]!){createProjectV2Field(input:{projectId:$p,dataType:SINGLE_SELECT,name:$n,singleSelectOptions:$o}){projectV2Field{... on ProjectV2SingleSelectField{id}}}}"
        gh("api", "graphql", "--input", "-", input=json.dumps({"query": q, "variables": {"p": PID, "n": name, "o": want}}))
for name, dtype in [(n, "TEXT") for n in TEXTS] + [(n, "NUMBER") for n in NUMBERS]:
    if name not in fields:
        q = "mutation($p:ID!,$n:String!,$d:ProjectV2CustomFieldType!){createProjectV2Field(input:{projectId:$p,dataType:$d,name:$n}){projectV2Field{... on ProjectV2Field{id}}}}"
        gh("api", "graphql", "--input", "-", input=json.dumps({"query": q, "variables": {"p": PID, "n": name, "d": dtype}}))
proj = graphql("""query($o:String!,$n:Int!){user(login:$o){projectV2(number:$n){fields(first:50){nodes{
  ... on ProjectV2Field{id name dataType}
  ... on ProjectV2SingleSelectField{id name dataType options{id name}}}}}}}""", o=OWNER, n=PROJECT_NO)["data"]["user"]["projectV2"]
fields = {f["name"]: f for f in proj["fields"]["nodes"] if f}
status_backlog = next(o["id"] for o in fields["Status"]["options"] if o["name"] == "Backlog")
print("fields ok")

# ---- issues, sub-issues, board items, field values ---------------------------
for i, t in enumerate(tickets, 1):
    k = t["key"]
    row = m.get(k, {"key": k})
    if not row.get("number"):
        out = json.loads(gh("api", f"repos/{OWNER}/{REPO}/issues", "--method", "POST", "--input", "-",
                            input=json.dumps({"title": t["title"], "body": t["body"], "labels": t["labels"]})))
        row.update(number=str(out["number"]), id=str(out["id"]), node_id=out["node_id"])
        m[k] = row; save_map(m)
        time.sleep(1.5)
    if t["parent"] and not row.get("linked"):
        parent = m[t["parent"]]
        gh("api", f"repos/{OWNER}/{REPO}/issues/{parent['number']}/sub_issues", "--method", "POST",
           "-F", f"sub_issue_id={row['id']}")
        row["linked"] = "1"; save_map(m)
    if not row.get("item_id"):
        r = graphql("mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}",
                    p=PID, c=row["node_id"])
        row["item_id"] = r["data"]["addProjectV2ItemById"]["item"]["id"]; save_map(m)
    if not row.get("fields"):
        sets = [("Status", {"singleSelectOptionId": status_backlog})]
        for name, val in t["fields"].items():
            if val in ("", None):
                continue
            f = fields[name]
            if f["dataType"] == "SINGLE_SELECT":
                sets.append((name, {"singleSelectOptionId": next(o["id"] for o in f["options"] if o["name"] == val)}))
            elif f["dataType"] == "NUMBER":
                sets.append((name, {"number": float(val)}))
            else:
                sets.append((name, {"text": str(val)}))
        parts = []
        for j, (name, value) in enumerate(sets):
            v = json.dumps(value).replace('"singleSelectOptionId"', "singleSelectOptionId").replace('"number"', "number").replace('"text"', "text")
            parts.append(f'f{j}: updateProjectV2ItemFieldValue(input:{{projectId:"{PID}",itemId:"{row["item_id"]}",fieldId:"{fields[name]["id"]}",value:{v}}}){{clientMutationId}}')
        gh("api", "graphql", "-f", "query=mutation{" + " ".join(parts) + "}")
        row["fields"] = "1"; save_map(m)
    if i % 25 == 0:
        print(f"{i}/{len(tickets)}", flush=True)

print(f"done: {len(m)} tickets mapped in {MAP}")
