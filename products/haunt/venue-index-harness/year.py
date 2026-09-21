"""year.py - the same identity metric over a realistic number of visits per venue,
because 'a year of use' is a few visits to most venues and many to your local."""
import statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from identity import simulate
CFG = {"as specified":       ("A", False, 0.0, False, 5,  False),
       "remediated (full)":  ("B", True,  4.0, True,  20, True)}
for sigma in (25.0,):
    for label, (sc, cl, beta, dd, L, ns) in CFG.items():
        print(f"\n=== {label} — sigma {sigma:.0f} m — % of venues keeping ONE identity ===")
        print(f"{'visits/venue':<14}" + "".join(f"{a:>14}" for a in ("manchester","chorlton","ludlow")))
        for v in (3, 6, 12, 20, 40):
            r = simulate(sc, sigma, cl, beta, dd, L, namesearch=ns, visits=v)
            print(f"{v:<14}" + "".join(
                f"{100*sum(x['single'] for x in r[a])/len(r[a]):>13.1f}%" for a in ("manchester","chorlton","ludlow")))
