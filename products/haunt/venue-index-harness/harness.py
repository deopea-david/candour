"""harness.py - the venue-index measurement harness, rebuilt.

Provides: the index in memory per scope, great-circle distance, a name matcher,
offline near-duplicate clustering, and the rankers compared in the spike.
Re-runnable: see README_RERUN.md.
"""
import hashlib, json, math, os, random, re, unicodedata
from difflib import SequenceMatcher
import duckdb

SP = os.path.dirname(os.path.abspath(__file__))
R_EARTH = 6371000.0

def hav(alat, alon, blat, blon):
    p = math.pi / 180.0
    return 2 * R_EARTH * math.asin(math.sqrt(
        math.sin((blat - alat) * p / 2) ** 2 +
        math.cos(alat * p) * math.cos(blat * p) * math.sin((blon - alon) * p / 2) ** 2))

# ---------------------------------------------------------------- name matching
_GENERIC = {"the","ltd","limited","plc","llp","uk","co","company","inc","and","at","of",
         "bar","restaurant","cafe","pub","inn","lounge","kitchen","house","grill","tavern",
         "coffee","bistro","brasserie","takeaway","food","eatery","hotel","club","shop",
         "manchester","chorlton","ludlow","didsbury","salford","street","road","centre","center"}
_TRADING = re.compile(r"\b(t/?as?|trading as|t/a)\b", re.I)

def norm(s):
    if not s: return ""
    s = _TRADING.split(s)[-1]
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.lower().replace("&", " and ")
    s = s.replace("'", "").replace("\u2019", "")   # Nando's -> nandos, not nando s
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def toks(s):
    """Distinctive content tokens: generic trade words and locality names removed."""
    return [t for t in norm(s).split() if t not in _GENERIC and len(t) > 1]

def name_sim(a, b):
    """0..1 similarity used to decide 'these two names denote the same venue'.

    Deliberately conservative. Whole-string ratio, token Jaccard, and a
    containment term that is credited ONLY when the shorter name carries at
    least two distinctive tokens, or one distinctive token of >= 6 characters.
    Without that guard, 'Tops Restaurant' matches 'Tops Buffet City' at 1.0.
    """
    na, nb = norm(a), norm(b)
    if not na or not nb: return 0.0
    ratio = SequenceMatcher(None, na, nb).ratio()
    ta, tb = set(toks(a)), set(toks(b))
    if not ta or not tb:
        return ratio
    inter = ta & tb
    jac = len(inter) / len(ta | tb)
    short = ta if len(ta) <= len(tb) else tb
    cont = 0.0
    if inter >= short:                       # shorter name fully contained
        if len(short) >= 2 or (len(short) == 1 and len(next(iter(short))) >= 6):
            cont = 0.95
    return max(ratio, jac, cont)

# ---------------------------------------------------------------- the index
class Index:
    def __init__(self, scope):
        con = duckdb.connect(os.path.join(SP, "ovt.duckdb"), read_only=True)
        col = {"A": "in_a", "B": "in_b", "C": "in_c"}[scope]
        self.rows = [dict(id=r[0], name=r[1], conf=r[2], cat=r[3] or r[4], lat=r[5], lon=r[6])
                     for r in con.execute(
                         "SELECT id,name,confidence,basic_category,cat_primary,lat,lon "
                         "FROM work WHERE " + col).fetchall()]
        con.close()
        self.scope = scope
        self.by_id = {r["id"]: r for r in self.rows}
        self.cluster = {r["id"]: r["id"] for r in self.rows}   # identity until clustered

    def near(self, lat, lon, radius):
        dl = radius / 111320.0
        dn = radius / (111320.0 * math.cos(lat * math.pi / 180))
        out = []
        for r in self.rows:
            if abs(r["lat"] - lat) > dl or abs(r["lon"] - lon) > dn: continue
            d = hav(lat, lon, r["lat"], r["lon"])
            if d <= radius: out.append((d, r))
        out.sort(key=lambda t: t[0])
        return out

    # ------------------------------------------------ offline near-dup clustering
    def build_clusters(self, max_m=60.0, min_sim=0.70):
        """Union rows that are within max_m AND name-similar >= min_sim.
        Runs once at index build time; ships as a cluster_id column."""
        parent = {r["id"]: r["id"] for r in self.rows}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb: parent[max(ra, rb)] = min(ra, rb)
        cell = {}
        g = max_m / 111320.0
        for r in self.rows:
            cell.setdefault((int(r["lat"] / g), int(r["lon"] / (g * 1.5))), []).append(r)
        for (cy, cx), _ in list(cell.items()):
            bucket = []
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    bucket += cell.get((cy + dy, cx + dx), [])
            here = cell[(cy, cx)]
            for a in here:
                for b in bucket:
                    if a["id"] >= b["id"]: continue
                    if hav(a["lat"], a["lon"], b["lat"], b["lon"]) > max_m: continue
                    if name_sim(a["name"], b["name"]) >= min_sim: union(a["id"], b["id"])
        self.cluster = {r["id"]: find(r["id"]) for r in self.rows}
        n = len(set(self.cluster.values()))
        return len(self.rows), n

def stable_seed(*parts):
    """A seed that does not move between processes. Python's built-in hash() is
    salted per process (PYTHONHASHSEED), which silently made an earlier version
    of this harness irreproducible run to run."""
    return int(hashlib.md5("\x1f".join(str(p) for p in parts).encode()).hexdigest()[:8], 16)

def jitter(lat, lon, sigma, rng):
    """Isotropic Gaussian offset of sigma metres on the query point."""
    dn = rng.gauss(0, sigma); de = rng.gauss(0, sigma)
    return (lat + dn / 111320.0, lon + de / (111320.0 * math.cos(lat * math.pi / 180)))
