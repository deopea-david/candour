# Idea brief — Plot

**Date:** 2026-09-01 · **Origin:** CEO spark via `/scout` (round 2, ranked 1st) · **Status:** spark → awaiting research

## The idea in two sentences

Tell it your postcode and what you want to grow, and it computes your local frost dates from 1 km gridded UK observations and returns a sowing, planting and succession plan for the year — delivered as a wall chart you print once and keep in the shed. The free advice that exists today is national or loosely regional ("in the south of England…"); this is the same arithmetic done against your own square kilometre.

## Who it's for, and what they do today instead

UK home food growers and allotment holders. 36% of UK adults grow vegetables, fruit or herbs [E, search-snippet only, single source, ageing] (https://horticulture.co.uk/gardening/statistics); 108,958 people sit on allotment waiting lists across 175 responding councils, average wait 4 years [E, single source, commercially motivated, FOI method stated and checkable] (https://www.dino.co.uk/uks-growing-allotment-waiting-lists/).

Today they use: free RHS month-by-month grow-your-own advice, which is genuinely good and already regionally varied [E] (https://www.rhs.org.uk/advice/grow-your-own/in-month); the sowing calendar printed on the seed packet; GrowVeg at $35/yr auto-recurring, whose own subscribe page does **not** name frost dates, succession planting or printing as features [E] (https://www.growveg.com/subscribeinfo.aspx); or their own memory and last year's mistakes.

## Why this fits Candour (which principles it serves)

- **1.5 / 2.1 — cheap to run.** The only candidate of eight with *no per-user variable cost at all*: frost normals are computed once from a licensed historical series, cached, and never queried per customer. A static lookup, a rules table and a PDF renderer on a few pounds a month. The cost sheet is honest without effort.
- **4 — data export.** Trivially satisfied: the artefact *is* the export.
- **1.1 — genuinely helpful.** It answers a question people actually get wrong every spring, using public data they cannot practically compute themselves.

The data licence question that the scout called decisive is answered: HadUK-Grid, 1 km gridded UK observations 1836–2025 including minimum air temperature and days of air frost, is published under **Open Government Licence v3 with commercial reuse permitted** [E] (https://catalogue.ceda.ac.uk/uuid/789b3065d74a4c948ab05d33556c86d0/).

## What would make this NOT worth doing

Written honestly at spark stage; the Skeptic will check this was not sandbagged.

1. **The differentiator may be noise.** The entire wedge over free RHS content is "postcode-aware." If last-frost dates vary by less than a week *within* a region, postcode resolution is precision that changes nothing a gardener does — and selling it as the reason to pay engages Article 1.3 and Article 4's honest-marketing clause. This is the single thing that decides the idea and it is testable in an afternoon for £0.
2. **It is a one-off purchase wearing a subscription's clothes.** A wall chart is printed once and frost normals barely move year to year, so renewal is near-zero and the business is annual re-acquisition. Dressing that as auto-renewal is precisely the pattern Article 4 polices.
3. **The demand evidence measures population, not willingness to pay.** 36% of adults growing herbs is not 36% of adults buying a planner, and both figures are single-source. There is currently *no* retrieved evidence of anyone paying for UK sowing timing specifically.
4. The free competitor (RHS) is good, not bad. A paid product has to beat free-and-good.

## Commissioned discovery

- [ ] **Research brief** (Research Analyst) — commissioned 2026-09-01, **due 2026-09-22**. Starts the 4-week anti-drift clock at delivery.
- [ ] **Cost model** (CFO) — after the research brief; must model one-off pricing with zero renewals as the base case.
- [ ] Feasibility note (CTO) — not warranted; nothing here is technically novel.

**Anti-drift:** kill/proceed/park decision due **2026-10-20** (brief due date + 4 weeks). If the brief is late, the decision clock starts from 2026-09-22 regardless (Constitution 5.2).
