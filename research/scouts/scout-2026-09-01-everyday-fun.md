# Scout — 2026-09-01 (round 2: "creative, new and fun, for everyday people")

**This is a second, separate scouting round on the same date.** Round 1 (a different commission, nine candidates, no promotion recommended) is in [`scout-2026-09-01.md`](scout-2026-09-01.md).

**Status:** PRE-pipeline. Nothing in this document has entered the pipeline. No Article 5.2 anti-drift clock is running on any candidate. Promotion happens only when the CEO says so, via `/idea`.

**Commissioned by:** CEO · **Run by:** CVO (agent half) · **Validation:** Research Analyst ×2 · **Cull:** The Skeptic (cold read, file paths only)

**CEO brief:** "a creative, new and fun idea for everyday people" — something the CEO is genuinely interested in.

**CEO's stated preferences (asked before generation):**

- **Interest areas:** home/food/making; play/culture/creativity; body/outdoors/place. Explicitly *not* money/admin/bureaucracy.
- **Kind of fun:** a joyful toy; a boring problem handled delightfully; something you keep. Explicitly *not* social/shared — so no network-effect-dependent ideas were generated.
- **Money model:** unconstrained — score on merit, state the economics honestly.
- **Build size:** unconstrained — effort follows the idea.

**Evidence posture (per `pipeline/evidence-standard.md`):** everything below is secondary evidence — published pricing, licence texts, public forums, and a handful of live data-API queries the analysts ran themselves. Candour has no industry contacts, so there is **no primary user research behind any candidate**. Nothing here is demand validation. Several incumbent sites (Etsy, Grafomap, Samsung Food, Copy Me That, plotaroute, Royal Mail, Blurb) blocked automated fetching; those gaps are recorded as "could not verify" rather than filled from memory.

---

## Recommendation

**Promote one: Plot.** It is the only candidate whose blocker turned out to be answerable, whose running cost is genuinely near zero, and whose remaining risk can be tested by the CEO alone in an afternoon with free data and no insider access.

**Almanac is a conditional second** — do not promote it yet. It has a free, fast test that can kill it before anything is committed (below). If that test passes, promote it; if it fails, it dies without ever starting a clock.

Six candidates died. One of the deaths — Postcard — is a judgment call that belongs to the CEO, not to the agents, and is flagged as such.

---

## Survivors

### 1. Plot — the grow-your-own year, worked out for where you actually live

**Pitch:** Tell it your postcode and what you want to grow; it computes your local frost dates from 1 km gridded UK observations and gives you a sowing, planting and succession plan for the year — as a wall chart you print once and stick in the shed. The free advice that exists today is national or vaguely regional ("in the south of England…"); this one is arithmetic done against your own square kilometre.

**Why it is here:** the only one of the eight with **no per-user variable cost at all** — frost normals are computed once and cached, no API call per customer, a static lookup plus a PDF renderer on a few pounds a month of hosting. Best fit to Constitution 1.5 of anything scouted. The artefact *is* the data export, so Article 4's export duty is free.

**Strongest reason against:** *the differentiator may be a claim we cannot substantiate.* The entire wedge over free RHS content is "postcode-aware." If last-frost dates vary by less than a week within a region, postcode resolution is precision that changes nothing a gardener does — and selling it as the reason to pay engages Article 1.3 and Article 4's honest-marketing clause. Secondary: a wall chart printed once is **a one-off purchase wearing a subscription's clothes**; dressing that as auto-renewal is exactly the pattern the Constitution polices.

**What a full research brief must prove:**

1. **The frost-spread test — do this first, it is an afternoon and it costs nothing.** Compute last-spring-air-frost from HadUK-Grid `tasmin` for ~30 postcodes chosen both *across* and *within* regions. The differentiator survives only if the median **within-region** spread is ≥2 weeks *and* the sowing table actually changes at that spread. Under a week, and Plot needs a different reason to exist.
2. Any retrieved evidence of people **paying** for UK sowing timing specifically — GrowVeg subscriber numbers, unit sales of a printed garden planner on a retrievable storefront, filings for a UK garden-planning tool. The two figures we have measure population, not willingness to pay; absent this, the honest entry is "unsized."
3. CEDA account eligibility for a **non-academic commercial** user (open friction — the Met Office also publishes provisional HadUK-Grid directly).
4. A cost sheet at one-off pricing with zero renewals. If it works as a one-off, the renewal objection dissolves by repricing rather than by argument.
5. Scope of the tagged-PDF-plus-HTML path for WCAG 2.1 AA — a decorative PDF wall chart needs a real accessible alternative.

**Load-bearing evidence:**

- HadUK-Grid, 1 km gridded UK observations 1836–2025 including minimum air temperature and days of air frost, **Open Government Licence v3, commercial reuse permitted** [E] (https://catalogue.ceda.ac.uk/uuid/789b3065d74a4c948ab05d33556c86d0/) — retrieved by the Skeptic; **this dissolves the blocker the research pass called decisive.**
- GrowVeg: $35/yr auto-recurring, $50 one year, $85 two years; that page does **not** name frost dates, succession planting or printing as features [E] (https://www.growveg.com/subscribeinfo.aspx).
- RHS month-by-month grow-your-own advice, free, already regionally varied [E] (https://www.rhs.org.uk/advice/grow-your-own/in-month) — **the serious competitor is free and good.**
- Open-Meteo free tier excludes commercial use: "A subscription grants a commercial use licence" [E] (https://open-meteo.com/en/pricing).
- 108,958 people on UK allotment waiting lists, 175 responding councils, average wait 4 years, May 2025 [E] (https://www.dino.co.uk/uks-growing-allotment-waiting-lists/) — **single source, commercially motivated (a decking retailer's content marketing), method (FOI) stated and checkable.**
- 36% of UK adults grow vegetables, fruit or herbs, YouGov for the HTA, Oct 2022 [E, search-snippet only, single source, ageing] (https://horticulture.co.uk/gardening/statistics).

### 2. Almanac — one printable page a month, for your postcode

**Pitch:** A single page for where you live, every month: what's in season, what's flowering and migrating, sunrise and the shape of the daylight, moon phases, the night sky — and tides if you're coastal. People pin it up; it is a keepsake with a date on it.

**Why it is here:** the only candidate with a defensible keepsake moat, and real evidence that people buy the *national* version of this. The non-tidal data stack is clean — ephemeris is pure computation, no licence, no vendor.

**Strongest reason against:** *the licensed component and the localised component are the same component.* UKHO's free-licence criteria cover one port for up to a year, **or** ten ports for one month, **or** any number of ports for seven days — or total commercial value under £10,000/yr. Read plainly, **the free licence covers a product that is not a business.** Strip tides out and postcode localisation collapses toward sunrise/sunset: free, and thin. So Almanac has two shapes — licensed-and-blocked, or unlicensed-and-thin — and the appealing coastal version is the blocked one. Underneath that: **editorial labour is the entire cost base, it scales with regions rather than customers**, and Article 2.1 forces it onto the public cost sheet at market benchmark. That is software's economics inverted.

**What a full research brief must prove — in this order:**

1. **The editorial break-even model, first, because it is free and can kill this without waiting on anyone.** 12 months × N regions of benchmarked writing against a £15–25/yr price. If break-even needs more subscribers than the analyst's own upper bound of "low thousands," Almanac is dead and no licence letter changes that.
2. Only if (1) survives: a **written UKHO position** on per-postcode monthly reproduction of tidal predictions, at a price the product can carry. API access is not a reproduction licence — the redistribution terms could not be verified.
3. Failing tides: that a Cumbria page and a Kent page differ enough on **non-tidal** content that a reader would call them different products.
4. Whether localisation has been **tried and abandoned** in a comparable market — regional or climate-zone almanac editions anywhere. A category this mature having not localised is mildly adverse evidence, not neutral.
5. The same WCAG 2.1 AA obligation as Plot.

**Load-bearing evidence:**

- UKHO: any reproduction of tidal predictions requires an official copyright licence [E] (https://developer.admiralty.co.uk/faqs); free-licence qualifying criteria — one port/one year, or 10 ports/one month, or any ports/seven days, or commercial value under £10,000/yr [E] (https://copyright.ukho.gov.uk/QualifyingCriteria.aspx) — **verified independently by the Skeptic.**
- Tidal API Foundation tier £120/yr ex VAT, 20,000 calls/month [E] (https://api.gov.uk/ukho/tidal-api-foundation) — **access, not a reproduction licence.**
- Lia Leendertz, *The Almanac: A Seasonal Guide to 2026*, Hachette, **£12.99 RRP**, pub. 28 Aug 2025, several annual editions [E] (https://www.hachette.co.uk/titles/lia-leendertz/the-almanac-a-seasonal-guide-to-2026/9781856755504/) — **evidence that people buy the *national* version. The localised variant has no evidenced buyer.**
- ADMIRALTY EasyTide: free, 7-day predictions, 600+ British Isles ports [E] (https://www.admiralty.co.uk/access-data/tidal-data/easy-tide). Woodland Trust Nature's Calendar: free [E] (https://naturescalendar.woodlandtrust.org.uk/). **The information is free; the product would compete on the artefact.**
- Met Office site-specific forecasts free to 360 calls/day, £9/mo for 900/day [E] (https://datahub.metoffice.gov.uk/pricing/site-specific) — optional, not required.

---

## The six that died

| # | Candidate | Why it died |
|---|---|---|
| 4 | **Cookbook** | Its defining mechanic reproduces the one part of a recipe UK copyright protects. Ingredients and quantities are functional and safe; "the particular literary expression used to describe the method steps" is protected [E] (https://www.mathys-squire.com/insights-and-events/news/the-recipe-for-success-a-platter-of-ip-rights-to-protect-your-food-and-drink-products/), corroborated by a second UK legal source. Printing and binding a book of harvested method prose is reproduction, not a grey area. The premise also failed: Paprika is still a **£29.99 one-off** [E] (https://apps.apple.com/gb/app/paprika-recipe-manager-3/id1303222628), so there is no price-hike refugee to catch, and against AnyList at **$9.99/yr** [E] (https://www.anylist.com/complete) there is no price headroom a 20% cap could use. |
| 6 | **Hunt** | Fails silently *after* payment in exactly the residential postcodes it is sold for. Live Overpass counts of taggable features within 800 m [E, analyst's own retrieval, ODbL]: Cambridge 975, Liverpool 754, outer London 271 — but **Bishop's Castle 36, Leicester suburb 22, south Manchester 15**. You cannot build eight checkable clues from 15 features, and you cannot warn the customer in advance. Plus: directing children to algorithmically-chosen outdoor locations while the founder carries **unlimited personal liability as an unincorporated brand**. Actionbound is free for private use [E] (https://en.actionbound.com/pricing). |
| 7 | **Doorstep** | The payable audience is approximately zero. Komoot's loop planning remains free in-app (the Feb 2025 paywall is on *device sync*, which this product doesn't need) [E] (https://www.komoot.com/product); Strava's subscriber route builder does circular routes [E] (https://www.strava.com/pricing). The capability is bundled inside subscriptions the target user already holds, and **20% over cost cannot beat free**. Cheapest and most legally clean of the eight, and the one nobody needs to buy. *Do not spend an afternoon verifying plotaroute to confirm a kill that already holds.* |
| 1 | **Trace** | Three incumbents already ship it — My Adventure Maps sells finished posters from GPX/Strava/FIT at €24.95–€44.95 with a €7.95 digital download [E] (https://myadventuremaps.com/en/index.html); Maprides compiles Strava activities into a print [E] (https://mapridesshop.com/). A one-off seasonal gift purchase with no repeat revenue, and cost+20% on a physical print (Prodigi budget poster from £3.00 wholesale ex-VAT ex-shipping [E]) leaves nothing for reprints, returns or card fees. The digital variant that *does* fit Article 2.1 lands near an incumbent's €7.95 without an incumbent's brand. **Correction for the record:** the Strava API dependency is *not* the reason. It dissolves the moment you accept a user-exported GPX and never touch the API — Apple Health exports contain `workout-routes/*.gpx`. A wrong reason invites a wrong revival. |
| 3 | **Quizmaster** | Two independent legs, both unsupported. The analyst went looking for evidence that quiz buyers care about sourced answers and **found none** — no host complaints, no trade coverage, nothing. And the per-pack verification cost ([J] £1.50–£6 for 60 sourced answers plus a human spot-check to make the claim honest under Article 4) plausibly exceeds a market that clears at **£2.00–£4.50** — Instant Quizzes £4.50/pack, subscription from £21 [E] (https://www.instant-quizzes.co.uk/collections/quiz-night); Quiz On Demand from £2.00 [E] (https://quizondemand.co.uk/pub-quiz-subscription-packages/) — before the margin cap even binds. At least six UK sites give the same thing away free. A product needs one of those legs to hold. |
| 8 | **Postcard** | **See below — this death is the CEO's call, not the agents'.** |

---

## One open decision for the CEO — Postcard

The agents disagreed, and the disagreement resolves on a fact only the CEO holds.

The **ethical wedge is real and documented.** Touchnote sells at £3.69, or "from £2.17" via credits — and **those credits expire after 12 months** [E] (https://touchnote.com/uk/info/postcard/, https://touchnote.com/uk/credits/), with a MoneySavingExpert thread recording expiry with no refund, subscription tiers framing paid cards as "free", an automatic £38 annual charge after a free trial, and a multi-step cancellation flow [E, user-generated forum content, indicative not authoritative] (https://forums.moneysavingexpert.com/discussion/6007141/warning-for-touchnote-customers). Expiring prepaid credits and hard cancellation are precisely what Article 4 forbids. An honest card at roughly £2.40 — Stannp's real API rate of £0.88 ex VAT [E] (https://www.stannp.com/uk/direct-mail-api/postcards) plus Stripe's 1.5% + 20p [E] (https://stripe.com/gb/pricing) plus benchmarked labour — **undercuts PostSnap's ethically-clean £4.00 by about 40%** [E] (https://www.postsnap.com/postcards). It is the best-evidenced paying demand of all eight candidates.

It dies here anyway, on **shape**: no software leverage, so support burden scales linearly with revenue forever; a cold start against app-store brands that a 20% margin cannot fund acquisition against; postal data on **recipients who never consented**, requiring qualified human review under Constitution 6.1; physical fulfilment failures landing on unlimited personal liability; and — the decisive one — it sits in none of the three interest areas the CEO named, against a brief that explicitly asked for something he is genuinely interested in. The international proposition is dead outright: Royal Mail international starts at £3.60 [E, third-party reseller page, royalmail.com 403'd] (https://www.mailcoms.co.uk/current-royal-mail-postage-rates/) while MyPostcard retails worldwide at $3.49 [E] (https://www.mypostcard.com/en/prices), so an honest UK-posted price would *exceed* the incumbent's retail price.

**The falsifier, stated by the Skeptic and put to the CEO:** if David would genuinely enjoy running a small physical fulfilment operation, then "CEO pull = 2" was simply wrong, and **Postcard becomes the best-evidenced candidate of the eight and should displace Almanac.** That is a Constitution 5.4 judgment; the agents cannot make it.

---

## Corrections found during this scout

Recorded because they change what a future reader should believe, not to tidy the record.

1. **The research pass missed the dataset that dissolves Plot's blocker.** It checked Met Office DataHub and Open-Meteo and concluded the frost-date licence question "decides this candidate." HadUK-Grid on CEDA — OGL v3, commercial reuse permitted — answers it, and the answer is yes.
2. **The CVO's scoring rubric had a real bug: it added where three of its axes should gate.** "Payable audience ≈ zero", "the core mechanic reproduces protected work" and "we cannot tell the customer before payment whether it will work" are disqualifiers, not one-out-of-five weaknesses. Under the additive version, Doorstep scored level with Almanac while carrying the niche score the analyst described as "not a business." **Adopted for future scouts:** gate first (any axis at 1 kills; any two at 2 kills), then score survivors for ordering only.
3. **"Validatable" was measuring the cost of finding out, not the probability of success — and paying up to 5 points either way.** Being cheap to investigate is not merit. It should drive research *sequencing*, not rank. This was the specific bug behind both anomalies in the table.
4. **CEO pull must not be additive.** It is the only axis with no evidence behind it and the one most predictive of abandonment. Demoted to a tiebreaker.
5. **Trace's platform dependency was misdiagnosed as structural.** See the kill table.

**Skeptic's limitation, recorded rather than buried:** four of the six kills — Cookbook, Hunt, Trace, Quizmaster — rest on the analyst's evidence as reported, which the Skeptic did not independently retrieve. At a gate that would be unacceptable; pre-pipeline it is proportionate, because no clock is running and a kill here costs nothing and is freely reversible. **If the CEO wants any of those four reconsidered, the Skeptic will verify that candidate properly before it dies.**

**Steering noted, per the Skeptic's clean-invocation clause:** the task was framed as "a cull," which presupposes deaths. The Skeptic checked whether "kill nothing" was defensible and concluded it was not — under Article 5.2 each survivor consumes a research brief due in 3 weeks and a decision 4 weeks after that, which a solo founder cannot run five times in parallel. The framing pointed the same way the evidence did.

---

## If the CEO promotes Plot, the order of work is

1. The **within-region frost-spread test** — one afternoon, free data, and it either confirms or destroys Plot's reason to exist. Do this before anything else; it is cheaper to be wrong now.
2. Then, and only then, `/idea plot` — which commissions the research brief and **starts the Article 5.2 clock**: brief due 3 weeks from commissioning, kill/proceed/park due 4 weeks after that.

Nothing in this document is promoted. That is the CEO's call.

---

## CEO decision — 2026-09-01

Recorded by the CVO. This is a promotion decision, not a gate decision, so it does not produce a decision record under Article 3; it is recorded here because the scout's kills are being partly overruled and the record should say so plainly.

**Taken forward:** Plot, Quizmaster, Postcard, and Doorstep under a changed hypothesis.
**Not taken forward:** Almanac, Trace, Cookbook, Hunt.

**Postcard — the Skeptic's falsifier fired.** The kill rested on the CVO scoring CEO pull at 2/5. The CEO has corrected that score. Per the Skeptic's own stated condition — "if he says he would genuinely enjoy running a small fulfilment operation, then pull=2 was simply wrong, and Postcard becomes the best-evidenced of all eight candidates" — the kill is withdrawn on the grounds the Skeptic specified in advance. Nothing else about Postcard changed: the shape objections (linear support burden, cold start, recipient data under 6.1, unlimited personal liability on fulfilment failures) all stand and belong in its research brief. International remains dead on postage arithmetic.

**Quizmaster — overruled, and the reason it died has not been answered.** Both legs the Skeptic killed it on are still unsupported: no evidence retrieved that quiz buyers care about sourced answers, and a per-pack verification cost that plausibly exceeds a £2.00–£4.50 market. Neither is settled by wanting the idea to work. The CVO's position, in writing once per charter: **cost a verified 60-question pack before commissioning a research brief.** That is hours of work, it produces a single number, and if the number exceeds ~£2.50 the 30% cap kills Quizmaster regardless of what any brief finds. Spending a 3-week brief and a 4-week clock to arrive at an arithmetic result available today would be the anti-drift rule working against itself.

**Doorstep — a new spark, not a revival.** The original was killed because Komoot and Strava bundle loop planning for free. The CEO's hypothesis is different: those incumbents are oriented toward nature and countryside walking, and **walks in cities, towns and built-up areas are the underserved case.** The CVO's read is that this changes the product's category, not just its setting — the scarce thing in a town is not routing, it is knowing which streets are *worth walking*. That moves the competitor set away from Komoot/Strava/OS and toward curated urban walking products, and moves the cost base from routing infrastructure to curation. It also moves the Article 1.5 risk: routing is cheap and automatable, curation is labour that Article 2.1 puts on the cost sheet at benchmark. This should be scouted as a fresh candidate with its own validation pass, not promoted on the strength of the original.

**CVO concern, stated once and then set aside (Constitution 5.2).** Four promotions means four research briefs due 3 weeks from commissioning and four kill/proceed/park decisions due 4 weeks after each brief. The Skeptic already flagged that a solo founder cannot run this many in parallel, and the anti-drift rule explicitly "binds the founder above all." The CVO's recommendation is to stagger commissioning rather than start four clocks on one day, and to run the cheap pre-tests (Plot's frost spread, Quizmaster's pack cost) before their clocks start rather than inside them. The decision is the CEO's.

**CEO's sequencing decision:** all four commissioned on 2026-09-01. The CVO's recommendation to stagger was not taken; the concern above is recorded, not re-argued. **Four research briefs are due 2026-09-22 and four kill/proceed/park decisions are due 2026-10-20.** If any brief is late, that idea's decision clock starts from 2026-09-22 regardless (Constitution 5.2).

**Doorstep's shape:** left open by CEO decision. The research brief's primary job is to choose between the three framings, or to recommend killing.

**Scout round 2 closed.** Idea briefs: `proposals/plot/`, `proposals/quizmaster/`, `proposals/postcard/`, `proposals/doorstep/`.
