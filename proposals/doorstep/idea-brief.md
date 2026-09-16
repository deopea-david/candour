# Idea brief — Doorstep

**Date:** 2026-09-01 · **Origin:** CEO spark via `/scout` (round 2 — new hypothesis, not a revival) · **Status:** spark → awaiting research

## The idea in two sentences

Good walks in cities, towns and built-up areas — the places the walking apps treat as the bit you drive through on the way to the countryside. **The product's shape is deliberately unresolved at spark stage**: the research brief's first job is to determine which of three candidate products has an actual gap.

## The three framings the research must choose between

1. **Walks worth taking (curation).** The scarce thing in a town is not routing — it is knowing which streets are interesting: architecture, history, plaques, street art, cut-throughs, the good bits. Competitor set is Go Jauntly, self-guided tour apps and city listicles. Cost base is curation labour, which Article 2.1 puts on the cost sheet at benchmark.
2. **Practical urban loops (routing).** A loop of the minutes you have, from your door, away from main roads, weighted to quiet streets and green space. Cheap to run and fully automatable — but this is the version the original scout kill was aimed at, and it must beat free.
3. **A keepsake for a place.** A printed walk card or booklet for a specific town — a thing you keep or give, priced as a one-off. Fits the CEO's stated preference for things you keep; curation cost per town is high and it does not scale.

## Who it's for, and what they do today instead

People who want a decent walk from where they already are, in a built-up area. Today: Komoot, whose loop planning remains free in-app (its Feb 2025 paywall is on device sync) [E] (https://www.komoot.com/product); Strava's subscriber route builder [E] (https://www.strava.com/pricing); OS Maps at £35.99/yr [E, gift-card listing; flagged]; free tools including plotaroute's "Make Me a Route" [E, search-snippet only — the site 403'd to two separate attempts and remains **unverified**]; or a search for "nice walks in [town]" and a listicle.

## Why this fits Candour (which principles it serves)

- **1.1 — genuinely helpful** to a group the incumbents underserve, *if* the CEO's hypothesis holds.
- **1.5 — cheap to run**, in framing 2 at least: OSM is ODbL and OS Open Greenspace is free for commercial use with attribution [E] (https://www.ordnancesurvey.co.uk/products/os-open-greenspace). Self-hosted routing was estimated at £15–30/mo [J, needs a measured import].

## What would make this NOT worth doing

Written honestly at spark stage. **The original candidate was killed, and the kill has not been overturned — only re-aimed.** The reason it died was that incumbents bundle loop planning free, and *"20% over cost cannot beat zero."*

1. **The hypothesis may simply be wrong.** "Komoot is nature-focused" is currently the CEO's observation, untested. Komoot routes through towns perfectly well. If urban loops are adequately served and free, framing 2 dies exactly as the original did.
2. **If the answer is curation (framing 1 or 3), the economics invert.** Curation is labour that scales with *places*, not customers — software's economics upside down, the same structural problem that pushed Almanac down the ranking. A per-town cost base under a 20% margin needs a very large number of towns or a very small number of them done very well.
3. **The keepsake framing does not scale** and competes with £3 Etsy printables and free council walking leaflets.
4. Nobody has yet verified plotaroute, which may already be framing 2, for free.

## Commissioned discovery

- [ ] **Research brief** (Research Analyst) — commissioned 2026-09-01, **due 2026-09-22**. **Primary question: which of the three framings has a real gap?** Must test the CEO's hypothesis directly — does Komoot/Strava/OS actually underserve urban walking, or is that an impression from marketing imagery? Must verify plotaroute by hand. Must establish who curates urban walks today and at what price.
- [ ] **Cost model** (CFO) — after the framing is chosen; the cost base differs by an order of magnitude between routing and curation.
- [ ] Feasibility note (CTO) — only if framing 2 survives; a measured GB routing import replaces the £15–30/mo estimate.

**Anti-drift:** kill/proceed/park decision due **2026-10-20**. If the brief is late, the clock starts from 2026-09-22 regardless (Constitution 5.2).
