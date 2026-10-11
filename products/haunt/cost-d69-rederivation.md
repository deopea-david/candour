# Re-derivation record: CFO addendum E (D69 scope), cost figures

**Seat:** QA Engineer · **Date:** 2026-10-11 · **Slug:** `haunt` · **Authority:** gate Condition 6, `decisions/2026-09-16-haunt-gate.md`: *"Arithmetic … is re-derived in every future pack by a seat other than its author."* Commissioned by the Coordinator.
**Under test:** `products/haunt/cost-sheet-v3-addendum-d69.md` (PR #44, branch `docs/haunt-cost-d69`). **Inputs:** `cap-15-17-sizing.md` §1.1 to §1.3 (PR #42, read from the CTO worktree, commit `c7904f1` per the CFO), and `cost-sheet-v3-addendum-design.md` on `main` for the base (`A` = £51,017.93, `F` = £20,733.14, capitalised £90,854.37) and the formulae (§3.2, §4.2, §5.3; v3 §6, §11.2).
**Method:** I computed every figure with the script below **before opening the CFO's file**, then compared. Hours are [J] (the CTO's); everything here is arithmetic on them, so the tags below are [I] re-derivation, not measurement. **Provenance:** QA · sonnet (Sonnet 5.5) · effort medium · 2026-10-11. This record prepares and flags; it certifies nothing.

## Result

**89 of 105 compared figures match. The 16 mismatches all sit in the Low column and all come from one error: the Low one-off hours total is 55.0, not 55.5.** CTO lines 19.5 + 25 + 10.5 = 55.0. The CTO's sizing memo gives the sum as 55.5 (its "Sums" line) and 56 (its §0 table); the CFO re-adds the three subtotals as "55.5" and marks it ✔ ("The CTO's sums re-derive exactly (§1)"). The Point (80.25) and High (111) columns, the labour at risk, the margin at 4,000 and the D15 step all re-derive. No Point or High figure is affected; 1p differences from rounding are counted as matches.

**Does the Low error matter?** It moves nothing in the decision. Low one-off is £1,799.05, not £1,815.41 (£16.36); Low `A` is £51,764.81, not £51,770.27 (£5.46). Low `N*` is 15,232, not 15,233. It does falsify the sentence "the CTO's sums re-derive exactly", and Condition 6 exists to catch exactly that. **Fix:** CFO corrects the Low column and §0 A ("55.5" becomes "55"); CTO corrects `cap-15-17-sizing.md` §0 ("56", "+2.7%") and its Sums line ("55.5"), where the correct figures are 55 and +2.6%.

**Assumptions I had to make, because the formulae do not fix them (the CFO states the same ones):**
1. Each case pairs its one-off hours with its ongoing hours and adds both to the **point** base (addendum D), not to addendum D's low or high base.
2. Ongoing: low 0.75 × 6, point 1.125 × 8 (the midpoint; the CTO gives none), high 1.5 × 10.
3. Margin uses annual net proceeds 0.85 × 9.90 = £8.415 at 99p (the figure v3 uses); I calibrated this by reproducing addendum D's −44.5% at 4,000 before applying it (the script's base check).
4. Labour at risk: Android capture layer at 5, 6 and 7 weeks × 37.5 h (from the CFO's cited `android-and-stack-note.md`, which I did not open; I re-derived only the arithmetic on the stated weeks).

**Not re-derived:** post-cliff monthly (70.4p, 69p) and yearly (6.411, £6.39) D15 figures, because the formulae for them are not stated in the files I was given; the 5 to 7 weeks and the rate £32.71 (inputs, [J] and single-source per v3). The 1p ties: three-year point cost £156,561.94 (mine) against £156,561.93 (CFO; I triple the unrounded `A`); thresholds point £62,319.57 against £62,319.56.

## The D15 step point

Post-cliff pay-once honest price at the point: **£18.679** (mine) against £18.679 (CFO). Nearest of £18.49 and £18.90 is £18.49 (midpoint £18.695): **the switch is confirmed**. Sensitivity the CFO did not state: it is **fragile to the ongoing-hours assumption.** With point one-off hours and ongoing hours of 12 the honest price is £18.699, above the midpoint, so the point stays at £18.90; at 9 h (CFO) it is £18.679; at 15 h £18.718. The crossover is near 11.5 h a year. The CFO's flag (E-F6, do not freeze before v4) already covers this; I add that the ongoing point is the CFO's own midpoint [J, CFO], and the CTO gave none.

## Table

Cells are Low / Point / High. "Match" means to the penny, or to 1p from rounding.

| # | Figure | CFO | QA | Result |
|---|---|---|---|---|
| 1 | CAP-15 hours | 19.5 / 29 / 39 | 19.5 / 29 / 39 | match (3) |
| 2 | CAP-16 hours | 25 / 36 / 51 | 25 / 36 / 51 | match (3) |
| 3 | CAP-17 hours | 10.5 / 15.25 / 21 | 10.5 / 15.25 / 21 | match (3) |
| 4 | **Total one-off hours** | 55.5 / 80.25 / 111 | **55.0** / 80.25 / 111 | **Low MISMATCH**, others match |
| 5 | % of 2,090 h | 2.66 / 3.84 / 5.31 | **2.63** / 3.84 / 5.31 | **Low MISMATCH** |
| 6 | One-off at £32.71 | £1,815.41 / £2,624.98 / £3,630.81 | **£1,799.05** / £2,624.98 / £3,630.81 | **Low MISMATCH** |
| 7 | Ongoing hours a year | 4.5 / 9 / 15 | 4.5 / 9 / 15 | match (3) |
| 8 | Ongoing £ a year | £147.20 / £294.39 / £490.65 | same | match (3) |
| 9 | Ongoing vs 360 h | +1.3 / 2.5 / 4.2% | 1.2 / 2.5 / 4.2% | match (3; Low 1.25 rounds both ways) |
| 10 | Amortised a year | £605.14 / £874.99 / £1,210.27 | **£599.68** / £874.99 / £1,210.27 | **Low MISMATCH** |
| 11 | Amortised a month | £50.43 / £72.92 / £100.86 | **£49.97** / £72.92 / £100.86 | **Low MISMATCH** |
| 12 | Capitalised hours | 2,832.5 / 2,857.25 / 2,888 | **2,832** / 2,857.25 / 2,888 | **Low MISMATCH** |
| 13 | Capitalised £ | £92,669.78 / £93,479.35 / £94,485.18 | **£92,653.42** / £93,479.35 / £94,485.18 | **Low MISMATCH** |
| 14 | `B` | £30,889.93 / £31,159.78 / £31,495.06 | **£30,884.47** / £31,159.78 / £31,495.06 | **Low MISMATCH** |
| 15 | `F` | £20,880.34 / £21,027.53 / £21,223.79 | same | match (3) |
| 16 | **`A`** | £51,770.27 / £52,187.31 / £52,718.85 | **£51,764.81** / £52,187.31 / £52,718.85 | **Low MISMATCH** |
| 17 | Change in `A` | +752.34 (1.5%) / +1,169.38 (2.3%) / +1,700.92 (3.3%) | **+746.88** (1.5%) / same / same | **Low MISMATCH** (£) |
| 18 | Three-year cost | £155,310.81 / £156,561.93 / £158,156.55 | **£155,294.43** / £156,561.94 / £158,156.55 | **Low MISMATCH**; Point 1p rounding |
| 19 | Fixed labour h/yr | 606.75 / 611.25 / 617.25 | same | match (3) |
| 20 | **`N*`** | 15,233 / 15,356 / 15,512 | **15,232** / 15,356 / 15,512 | **Low MISMATCH** |
| 21 | 99p covers cost | 10,783 / 10,870 / 10,981 | **10,782** / 10,870 / 10,981 | **Low MISMATCH** |
| 22 | Pay-once covers cost | 11,406 / 11,498 / 11,615 | **11,404** / 11,498 / 11,615 | **Low MISMATCH** |
| 23 | Monthly 99p at 30% cap | 20,573 / 20,739 / 20,950 | **20,571** / 20,739 / 20,950 | **Low MISMATCH** |
| 24 | Pay-once buyers a month | 317 / 319 / 323 | 317 / 319 / 323 | match (3) |
| 25 | **Margin at 99p, 4,000** | −45.1 / −45.4 / −45.8% | −45.1 / −45.4 / −45.8% | match (3) |
| 26 | Honest monthly, 4,000 | £2.34 / £2.35 / £2.37 | £2.337 / £2.352 / £2.371 | match (3) |
| 27 | D15 M1, honest | 25.553 to 25.557 (pt 25.555) | 25.553 / 25.555 / 25.557 | match (3) |
| 28 | D15 M2, honest | 22.113 to 22.122 (pt 22.117) | 22.113 / 22.117 / 22.122 | match (3) |
| 29 | **D15 post-cliff, honest** | 18.674 to 18.686 (pt 18.679) | 18.674 / 18.679 / 18.687 | match (3; High 18.686 v 18.687, rounding) |
| 30 | **D15 step £18.90 to £18.49** | moves to £18.49 | moves to £18.49 (midpoint £18.695) | match (3 nearest points: M1 £25.49, M2 £22.00, post-cliff £18.49) |
| 31 | D15 thresholds, point | £31,159.78 / £62,319.56 | £31,159.78 / £62,319.57 | match (2; 1p) |
| 32 | **Labour at risk, hours** | 223 / 276.25 / 334.5 | 223 / 276.25 / 334.5 | match (3) |
| 33 | **Labour at risk, £** | £7,294.33 / £9,036.14 / £10,941.50 | same | match (3) |
| 34 | Extras: CAP-15 £948.59; with 75 h spike £11,489.39; 9.7% of build; `B` fall £3,012.05 | as stated | same | match (4) |

## Script

Run as `python3 -I final.py`. Output from the run is summarised by the table above.

```python
# QA re-derivation of CFO addendum E (D69). Run: python3 -I final.py
R=32.71; K=1.694118; SP=2.306; S=3.614; AN=3.3985
CAP_LO, CAP_HI = 0.0, 0.0
# CTO lines (cap-15-17-sizing.md c7904f1 section 1.1-1.3): (low, point, high)
c15=[(1.5,2,3),(3,4.5,6),(4,6,8),(2,3,4),(3,4.5,6),(6,9,12)]
c16=[(3,4.5,6),(2,3,4),(5,7.5,10),(3,5,8),(4,6,8),(8,10,15)]
c17=[(0.5,.75,1),(1,1.5,2),(1.5,2,3),(6,9,12),(1.5,2,3)]
col=lambda L,i:sum(x[i] for x in L)
H=[[col(L,i) for i in range(3)] for L in (c15,c16,c17)]
tot=[sum(h[i] for h in H) for i in range(3)]
print("CAP15/16/17 sums",H,"TOTAL",tot)
print("pct of 2090",[round(t/2090*100,2) for t in tot],"of 2777",[round(t/2777*100,1) for t in tot])
g=lambda x:round(x+1e-9,2)
print("one-off GBP",[g(t*R) for t in tot])
og=[0.75*6,1.125*8,1.5*10]
print("ongoing h",og,"GBP",[g(x*R) for x in og],"vs 360h",[round(x/360*100,1) for x in og])
print("amortised yr",[g(t*R/3) for t in tot],"month",[g(t*R/36) for t in tot])
# base: addendum D point (CFO pairs each case with the POINT base)
CAP0,F0,A0=90854.37,20733.14,51017.93
print("base A check",g(CAP0/3+F0))
rows={}
for n,i in (("low",0),("point",1),("high",2)):
    cap=CAP0+tot[i]*R; B=cap/3; F=F0+og[i]*R; A=B+F; N=A/AN
    m=lambda n_:(8.415-(A/n_+S))/((A/n_+S)+1.485)
    pc=lambda k:(3*(F/N+SP)+k*B/N)*K
    print(n,"hrs",2777+tot[i],"cap",g(cap),"B",g(B),"F",g(F),"A",g(A),"dA",g(A-A0),round((A/A0-1)*100,1),
      "3yr",g(3*A),"fixed lab h",602.25+og[i])
    print("   N*",round(N),"cover99",round(A/4.801),"payonce",round(3*A/13.617),"cap30",round(20274*A/A0),"buyers/mo",round(3*A/13.617/36),
      "m4000 %.1f%%"%(m(4000)*100),"honest4000 %.3f"%((A/4000+S)*K/12),
      "M1 %.3f M2 %.3f post %.3f"%(pc(2),pc(1),pc(0)),"thr",g(cap/3),g(2*cap/3), "mid(18.49,18.90)=18.695")
# labour at risk
android=[5*37.5,6*37.5,7*37.5]
risk=[android[i]+H[1][i]+H[2][i] for i in range(3)]
print("android",android,"risk h",risk,"GBP",[g(r*R) for r in risk],"with spike",g((risk[1]+75)*R),"pct of cap",round(risk[1]/(2777+tot[1])*100,1))
print("CAP15 GBP",g(H[0][1]*R),"B fall",g(risk[1]*R/3), "CFO-uses 2857.25 h:", round(risk[1]/2857.25*100,1))
# D15 sensitivity: ongoing hours at which post-cliff crosses 18.695
for ongoing in (4.5,9,10,12,15):
    cap=CAP0+tot[1]*R; B=cap/3; F=F0+ongoing*R; A=B+F; N=A/AN
    print("ongoing",ongoing,"post %.3f"%((3*(F/N+SP))*K))
# CFO's low column as stated hours 55.5 vs mine 55
cap=CAP0+55.5*R; print("CFO-low-hours cap",g(cap))
```

## Disagreement, once

The CFO's §1 says the CTO's sums "re-derive exactly" and ticks the 55.5. They do not for Low. A check that reads the subtotals and does not re-add them will pass a wrong total; the re-addition is the control. This is a flag to the CFO and CTO, not a block; it affects no price and no decision. **What would overturn this finding:** a CTO line figure I mis-transcribed (I read `cap-15-17-sizing.md` §1.1 to §1.3; Low column lines 1.5, 3, 4, 2, 3, 6 / 3, 2, 5, 3, 4, 8 / 0.5, 1, 1.5, 6, 1.5). **Where I did not look:** the CFO's §6 to §9 text beyond the figures compared, and the changes the CTO may have made to PR #42 after `c7904f1`.
