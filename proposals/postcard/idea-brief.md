# Idea brief — Postcard

**Date:** 2026-09-01 · **Origin:** CEO spark via `/scout` (round 2 — Skeptic's stated falsifier fired) · **Status:** spark → awaiting research

## The idea in two sentences

Upload a photo, write a message, and a real postcard is printed and posted to a real UK address — with the print cost, the postage and Candour's 20% itemised on the checkout page. No credits, no expiry, no subscription, no bundles: the honest price *is* the product.

## Who it's for, and what they do today instead

People who send physical postcards — holidaymakers, grandparents, people marking occasions. There is unambiguous evidence they pay for this today, which makes it the best-evidenced candidate of the eight scouted.

- **Touchnote:** £3.69 per card, "from £2.17" via credit packs, postage included [E] (https://touchnote.com/uk/info/postcard/) — and **credits expire after 12 months** [E] (https://touchnote.com/uk/credits/). A MoneySavingExpert thread records expiry with no refund or extension, subscription tiers framing paid cards as "free", an automatic £38 annual charge after a free trial, and a multi-step cancellation flow [E, user-generated forum content — indicative, not authoritative] (https://forums.moneysavingexpert.com/discussion/6007141/warning-for-touchnote-customers).
- **PostSnap:** £4.00 standard, £4.99 large, free UK postage, and describes itself as pay-as-you-go with no subscription and no minimums [E] (https://www.postsnap.com/postcards) — the ethically clean incumbent, and the one to beat on price.
- **MyPostcard:** $3.49 worldwide including postage [E] (https://www.mypostcard.com/en/prices).

## Why this fits Candour (which principles it serves)

- **Article 4 — no dark patterns.** Expiring prepaid credits and hard cancellation are named prohibitions. The market leader's documented behaviour is the exact thing the Constitution forbids, which makes an honest competitor a real product rather than a posture.
- **2.1 — transparent pricing.** Direct cost is ~£0.88 ex VAT print-and-post [E] (https://www.stannp.com/uk/direct-mail-api/postcards) plus Stripe at 1.5% + 20p [E] (https://stripe.com/gb/pricing). An honest ~£2.40 card undercuts PostSnap's £4.00 by roughly 40%.
- **1.2 — no exploitation.** Nothing here profits from confusion; the whole pitch is the removal of it.

**Scope decision at spark:** **UK domestic only.** International is dead on arithmetic — Royal Mail international starts at £3.60 [E, third-party reseller page; royalmail.com 403'd] (https://www.mailcoms.co.uk/current-royal-mail-postage-rates/) while MyPostcard retails worldwide at $3.49, so an honest UK-posted international price would *exceed* the incumbent's retail price. Incumbents almost certainly print in-destination through networks a solo UK operator cannot access [I, medium confidence].

## What would make this NOT worth doing

The scout's kill was withdrawn only on the axis the Skeptic named in advance (CEO appetite for running a fulfilment operation). **Every other objection stands and belongs in the research brief:**

1. **The honest cost sheet may not undercut £2.17.** Direct cost £1.10, plus benchmarked founder labour at even two minutes a card (~£0.80–£1.00), gives £1.90–£2.10 → £2.28–£2.52 retail, before any failure allowance and worse on the VAT-inclusive print figure. That beats PostSnap's £4.00 comfortably but **does not beat Touchnote's credit price**, and the honest comparison has to be made against both.
2. **No software leverage.** This is 1:1 physical goods: support burden scales linearly with revenue forever — wrong addresses, misprints, non-delivery. It never gets cheaper per unit the way software does.
3. **Cold start against app-store brands**, with a 20% margin that cannot fund paid acquisition.
4. **Recipient personal data.** It processes postal addresses of people who are not customers and never consented. Constitution 6.1 requires qualified human review before launch — this qualifies, and it is not an agent's call.
5. **Unlimited personal liability** on fulfilment failures while the brand is unincorporated.

## Commissioned discovery

- [ ] **Cost model** (CFO) — **decisive, and commissioned first.** An honest per-card cost sheet with benchmarked labour and a per-card failure allowance, priced at +20%, compared against *both* Touchnote's £2.17 credit price and PostSnap's £4.00. Model at realistic solo-operator volume, not the wholesale volume floor.
- [ ] **Research brief** (Research Analyst) — commissioned 2026-09-01, **due 2026-09-22**. Must close: Stannp's true small-volume rate and any minimum commitment; whether the Touchnote complaint pattern is substantiated beyond one forum thread; how the category is discovered by buyers, given no organic search position and no acquisition budget.
- [ ] **Feasibility note (CTO)** — warranted: fulfilment API integration, address validation, and failure/reprint handling are the technical substance of this product.

**Anti-drift:** kill/proceed/park decision due **2026-10-20**. If the brief is late, the clock starts from 2026-09-22 regardless (Constitution 5.2).
