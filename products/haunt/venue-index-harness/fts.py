"""fts.py - a real SQLite FTS5 name index over the scope-B rows, and the
retrieval policy a shipped implementation would use.

This replaces the ORACLE in identity.py's name-search branch. identity.py
assumes that when the user types a name, any index row that IS their venue is
found -- which is true by construction and is the circularity recorded at
venue-index-remediation.md §6.4 and §8.5.

Here the typed string is matched against the Overture name by FTS5's own
tokeniser and prefix operator. FTS5 knows nothing about name_sim, about the
FSA register, or about which row is the answer.

Retrieval policies
  AND  every query token as a prefix term, ANDed      (headline; strict)
  OR   every query token as a prefix term, ORed       (optimistic sensitivity)

FTS5 is the CTO's own choice: it is already inside row 5 of
android-and-stack-note.md §3.2, and its bundle cost is measured at
venue-index-remediation.md §12.
"""
import os, re, sqlite3
import duckdb

SP = os.path.dirname(os.path.abspath(__file__))
_DB = {}


def _norm(s):
    """Query normalisation. Must match namegen.keyboard()."""
    s = (s or "").lower().replace("’", "").replace("'", "")
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def build(scope="B"):
    """In-memory FTS5 index over the working table for one scope."""
    if scope in _DB:
        return _DB[scope]
    col = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
    con = duckdb.connect(os.path.join(SP, "ovt.duckdb"), read_only=True)
    rows = con.execute(
        "SELECT id, name, lat, lon FROM work WHERE " + col).fetchall()
    con.close()
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE row(rid INTEGER PRIMARY KEY, id TEXT, "
               "name TEXT, lat REAL, lon REAL)")
    db.execute("CREATE VIRTUAL TABLE nm USING fts5(name, content='row', "
               "content_rowid='rid', tokenize=\"unicode61 remove_diacritics 2\")")
    for i, (rid, name, lat, lon) in enumerate(rows, 1):
        # the index stores the name as the dataset supplies it, normalised the
        # same way the query is -- this is index hygiene, not matching
        db.execute("INSERT INTO row VALUES(?,?,?,?,?)", (i, rid, _norm(name), lat, lon))
    db.execute("INSERT INTO nm(nm) VALUES('rebuild')")
    db.commit()
    _DB[scope] = db
    return db


def _expr(q, policy):
    toks = [t for t in _norm(q).split() if t]
    if not toks:
        return None
    join = " AND " if policy == "AND" else " OR "
    return join.join(f'"{t}"*' for t in toks)


def search(q, scope="B", policy="AND", limit=500):
    """Row ids whose Overture name matches the typed string. No distance filter
    -- the caller applies the query radius, exactly as the app would."""
    db = build(scope)
    e = _expr(q, policy)
    if not e:
        return []
    try:
        cur = db.execute(
            "SELECT r.id, r.lat, r.lon FROM nm JOIN row r ON r.rid = nm.rowid "
            "WHERE nm MATCH ? LIMIT ?", (e, limit))
    except sqlite3.OperationalError:
        return []
    return cur.fetchall()


if __name__ == "__main__":
    db = build("B")
    n = db.execute("SELECT count(*) FROM row").fetchone()[0]
    print("scope B rows in the FTS5 index:", n)
    for q in ("the spread eagle", "spread eagle", "eagle", "chur", "wetherspoon"):
        for p in ("AND", "OR"):
            r = search(q, policy=p)
            print(f"  {q!r:<20}{p:<5}{len(r):>5} hits   "
                  + ", ".join(x[0][:0] or "" for x in r[:0]))
