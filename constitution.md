# The Candour Constitution

**Version:** 1.3 · **Status:** Unincorporated brand — this document is a public pledge, not yet a legal instrument · **Change log:** all amendments are recorded per Article 11 in `CHANGELOG.md`

---

## Preamble

Candour exists to build software that is genuinely useful to everyday people and businesses, priced honestly, and run transparently enough that trust never has to be taken on faith.

This constitution is the company's highest authority. Every product, decision, role, and agent operates under it. Where any plan conflicts with this document, the plan changes or the document is amended publicly — never quietly.

The company is currently a brand operated by its founder, not a registered legal entity. Nothing here is legally enforceable yet. Its force comes from being published, versioned, and written _before_ any money was at stake: breaking these rules later is visible rule-breaking, on the record. When the company incorporates, this constitution becomes the basis of its legal governing documents.

---

## Definitions

These terms mean the same thing everywhere in this constitution and in every Candour document. Per Article 9, they may only change by public amendment.

- **Cost:** everything it takes to run a product or the company, itemised — hosting, tooling, support, third-party services, and labour valued at a published market benchmark whether or not it is actually paid. **One-off build labour is capital, amortised straight-line over the standard amortisation period**, rather than charged wholly to its first year; maintenance and support are operating costs. Labour spent on work that does not ship is not capital: it is an operating cost in the year it is incurred, and where a product is abandoned before release the whole of its build labour is written off publicly in that year.
- **Standard amortisation period:** **three years (36 months)**, straight-line, in equal monthly amounts. It is **the same for every Candour product**, and no product sets its own. It is **an accounting convention and nothing more**: it is not a promise that a product will be supported, maintained or available for that period, **no customer-facing commitment of any kind attaches to it or is implied by it**, and it is never published as, or in place of, the support statement Article 4 requires. What Candour owes a customer when a product ends is fixed by Article 7.2 and does not depend on how much of the build remains unrecovered. Four conditions bind the treatment: the clock starts on the **earlier of a product's first sale and its public release**, published on its first cost sheet and never restated; **each capitalised increment runs its own clock from the date it ships**, so a later increment never extends, restarts or re-bases an earlier one; any unamortised remainder is **written off publicly on discontinuation** (7.2); and every cost sheet publishes the schedule required by 2.1. The period changes only by public amendment to this document (Article 11), never for one product, and **a change applies only to increments capitalised after it takes effect** — increments already running finish on the period they began under.
- **Profit:** income minus cost over a period.
- **Reserve:** funds held back to keep the company running without income — the target is 6–12 months of operating costs.
- **Surplus:** profit remaining after the reserve has been topped up to target.
- **Distribution:** any value taken out of the company by its owner(s) beyond published, benchmarked pay — dividends and their equivalents in any form.
- **Net proceeds** (of a sale): all consideration received in any form — cash, shares, earn-outs, and any side arrangement attributable to the sale, including consultancy or employment deals routed to the founder — minus direct transaction costs and tax. Consideration is itemised in the published sale assessment (Article 7).

---

## Article 1 — Mission and principles

1. **Genuinely helpful.** We build things people and businesses actually need, judged by whether they would recommend it unprompted — not by engagement metrics.
2. **No exploitation.** We do not profit from confusion, lock-in, addiction, or information asymmetry.
3. **Honest by default.** Pricing, capability, and limitations are stated plainly. We say what a product cannot do.
4. **Transparent to everyone.** Our numbers are public — to customers and to the general public alike (Article 3).
5. **Cheap to run, cheap to buy.** Operating cost discipline is an ethical obligation, because our customers pay our costs.
6. **Dissent is an institution.** No significant decision proceeds without a documented counter-argument (Article 5).

---

## Article 2 — Money rules

### 2.1 Transparent pricing

- Every product publishes a **cost sheet**: hosting, tooling, support, third-party services, and a fair-market cost for labour (including the founder's, whether or not it is actually drawn). Where build labour is capitalised, the cost sheet publishes an **amortisation schedule** — one line per capitalised increment, with its hours, ship date, period, amount amortised to date and remaining balance — together with capitalised hours as a share of all hours worked on the product that year, and a statement that the period is a company-wide accounting convention and not a statement about how long the product will be supported.
- Prices target a margin of approximately **20% over published costs**. This is a published target, not a rigid formula: deviations are permitted but must be justified in writing on the cost sheet (e.g. building a reserve, absorbing a cost spike). **A deviation in either direction is a deviation** — a margin below target is recorded and justified like any other, never labelled as no deviation. As a hard backstop, **no product's margin may exceed 30%**, regardless of justification.
- Margin is measured **per product, per financial year**. For products sold on a recurring basis it is additionally tested **cumulatively over the customer's lifetime**: a subscriber must not, merely by staying, pay materially more than the 30% ceiling would permit against the cost of serving them. A recurring price whose every individual year is compliant can still breach this document over a decade, and the cumulative test is what catches it. **This test is one-directional: it forbids a long-standing customer's position drifting above a newer customer's. A legacy price that is *lower* is not caught by it, and the notice a customer is owed before such a price rises is in Article 4.**
- Margins are per product, never averaged across the portfolio: each product's customers get that product's honest number, and no customer subsidises another product unknowingly.
- Cost sheets are reviewed and republished at least **annually** and at every price change.
- Labour is always costed at a stated market benchmark, so unpaid effort never fakes a low price and salary inflation never hides a high one.

### 2.2 Extraction rule

- All founder/owner compensation (salary, distributions, benefits) is **published**, with the benchmark pay is set against (default: the median UK software developer salary, adjusted for hours actually worked). Being paid is legitimate; being paid opaquely is not.
- Distributions may not exceed **35% of annual surplus** — deliberately mirroring the UK Community Interest Company cap, so conversion to a CIC later requires no weakening. Distributions are taken only at step 2 of the waterfall below, never outside it.

### 2.3 The profit waterfall

Each year, profit is applied strictly in this order, and the full allocation is published:

1. **Reserve top-up** — until the reserve reaches its 6–12 month target.
2. **Distributions** — optionally, up to 35% of the surplus (2.2), always published.
3. **The remainder**, in this order of preference:
   1. Price reductions for existing customers
   2. Funding new products under this constitution
   3. Donations — first to Candour's own non-profit initiatives (Article 8); if none exist, to external charities or non-profits signed off by the CEO in a published decision record

---

## Article 3 — Transparency schedule

The following are public, permanently, for anyone to inspect:

| What                                                                          | When                                                                 |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Product cost sheets and margins                                               | At launch, at every price change, and at least annually              |
| Founder/owner compensation and its benchmark                                  | Annually, from the first pound drawn                                 |
| The full profit waterfall allocation (2.3)                                    | Annually                                                             |
| This constitution and its full change history                                 | Continuously                                                         |
| Decision records for every gate decision — kill, proceed, or park (Article 5) | Within 30 days of the decision                                       |
| Security or data incidents affecting users                                    | Prompt disclosure to affected users; public summary after resolution |

What is _not_ published: individual customer data, security-sensitive implementation details, and third parties' confidential terms. The boundary is drawn here, in advance, so it is never improvised under pressure.

---

## Article 4 — Product ethics

Every product must, without exception:

- Use plain-language pricing with no hidden fees, forced bundles, or drip pricing.
- State, before first sale and on the product's own pricing page, **either the date until which the product will be supported, or plainly that no support date is committed**. Silence is not an option. A published support date is a term of the customer's contract — Consumer Rights Act 2015, s.36(3) — and is not **unilaterally** changed for customers who have already bought. **A product's standard amortisation period (Definitions) is an accounting convention, is never published as or in place of a support date, and the cost sheet carrying it says so on its face.**
- Make cancellation as easy as signup.
- **Where a price rises for a customer who has already bought, give at least 90 days' notice before the new price applies** — and longer where a customer would need longer to move to an alternative, judged from the export the product actually ships rather than an idealised one. **Each product publishes the notice period it guarantees, in its first cost sheet and on its pricing page, before its first sale; that period may be lengthened, never shortened.** Throughout the notice period the customer may cancel before the new price applies, and may export in full and free under the clause below. Where law or a distribution platform requires the customer's consent to the rise, this duty is **in addition to that requirement and never in place of it**. The 90 days is the same number, for the same reason, as the discontinuation notice in 7.2: time to decide, and time to leave with your data.
- Employ **no dark patterns**: no false urgency, no confirm-shaming, no pre-ticked boxes, no deliberately buried settings, no engagement mechanics designed to exploit compulsion.
- Collect the minimum data necessary, state why, and delete it when no longer needed.
- Let customers leave with their data: export in a usable, machine-readable format, available at any time, at no charge, and **with no penalty or disadvantage imposed for having exported**. This clause governs exit — that the export is complete, free, immediate and without consequence. It is **not** a requirement that an export reproduce the product's own experience, and it says nothing about what a product may or may not gate inside itself.
- Meet accessibility standards (**WCAG 2.2 AA** as the working baseline, read through **WCAG2ICT** where the product is native software rather than a web page, since WCAG is written for the web).
- Remain honest in marketing: claims we cannot substantiate are claims we do not make.

---

## Article 5 — Governance and decision gates

### 5.1 The pipeline

Ideas move through fixed stages: **spark → discovery (research brief, cost model, feasibility) → proposal → gate → build (requirements → architecture → build → verification) → release**. Each stage produces a written artifact stored in the company repository.

### 5.2 The anti-drift rule

Every idea entering the pipeline receives a **kill / proceed / park decision within 4 weeks** of its research brief — measured from the brief's **delivery**, or from its due date if the brief is late, **whichever is earlier**. Delivering a brief early shortens the decision window; it never buys slack. The clock cannot be stalled upstream: research briefs are **due 3 weeks from commissioning** (one extension allowed, with a written reason), and if a brief is overdue, the decision clock starts at its due date regardless. "Park" requires a written reason and a revisit date. This rule exists to force building over perpetual planning, and it binds the founder above all.

### 5.3 Mandatory dissent

No proposal passes a gate without a **Skeptic memo** attached: the strongest counter-argument, plausible failure modes, and who could be harmed. Approving a proposal requires responding to the dissent in writing, not merely outvoting it.

### 5.4 Human decision points

The following are never automated: kill/proceed decisions, spending real money, pricing changes, anything affecting user data policy, and release to real users. Agents prepare; the founder decides.

### 5.5 Reviews and demos

Every pipeline phase concludes with a **review pack and demo** presented to the CEO in the boardroom, compiled by the Chief Governance Officer. Work is not "done" until it has been reviewed.

### 5.6 Blocks and overrules

Certain seats hold blocking powers, defined in their charters: the CGO (gate passage), CTO (build commencement), CSO (release, on security grounds), QA (release, on verification grounds), UX (release, on Article 4 or accessibility grounds), and CFO (unpriced or uncosted launches). A block halts the blocked action. Only the CEO may overrule a block, and every overrule is recorded, with reasons, in the public decision record. The Skeptic holds no block by design: its power is that no gate passes without its dissent answered in writing (5.3).

---

## Article 6 — Roles

The company is operated by its founder (CEO, and part of the CVO function) together with AI agents holding the seats below. Each seat has a one-page charter (kept in `roles/`) defining its mandate, the questions it must ask, and what it can block.

**Active seats**

| Seat                                             | Mandate in one line                                                                                                                   |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **CEO** (human)                                  | Final authority on all human decision points (5.4); owns this constitution's spirit                                                   |
| **Chief Vision Officer** (shared: human + agent) | Originates and develops ideas; commissions discovery; drafts proposals                                                                |
| **Chief Governance Officer**                     | Enforces this constitution; runs gates, cadence and reviews; owns regulatory conformance (incl. UK GDPR, consumer law, accessibility) |
| **Chief Technology Officer**                     | Technical architecture; build-vs-buy; keeps the stack boring and cheap                                                                |
| **Chief Security Officer**                       | Secure design and industry standards (e.g. OWASP), from architecture through release; partners with the CTO                           |
| **Chief Financial Officer**                      | Unit economics, cost sheets, pricing transparency (Article 2–3)                                                                       |
| **The Skeptic**                                  | Institutional dissent (5.3). Deliberately not a C-title: this seat defends nothing and negotiates nothing                             |
| **Product Manager / BA**                         | Turns approved proposals into scoped requirements and acceptance criteria                                                             |
| **UX / Design Lead**                             | Usability for everyday people; polices dark patterns from the design side                                                             |
| **Engineer(s)**                                  | Builds it                                                                                                                             |
| **QA Engineer**                                  | Independent verification against acceptance criteria; edge cases; release readiness                                                   |
| **Research Analyst**                             | Market, user, competitor and feasibility research under CVO commission                                                                |

**Dormant seats** (defined now, activated when reality demands): **COO** (when there are operations), **Chief Legal Officer** (at incorporation or first contract).

### 6.1 Limits of agent authority

Agent reviews **prepare and flag; they do not certify**. Before launch, anything involving personal data at scale, payments, health information, regulated domains, or **third-party licence terms whose interpretation determines a product's architecture or cost**, receives review by qualified human professionals. The company never represents an AI compliance opinion as assurance.

---

## Article 7 — Endings

A product's ending — sale, discontinuation, or the founder's departure — is where trust promises are cheapest to break. So the rules for endings are fixed here, in advance, while no ending is on the table.

### 7.1 Sale

The company (or any product) may be sold — each transaction, however small, triggering all of the following:

1. The buyer **publicly adopts this constitution** as a condition of sale, locked for the same **3-year** term as condition 2; during that term, amendments weakening rules facing acquired customers are prohibited.
2. Existing customers' pricing rules (Article 2.1) are **contractually locked for 3 years** post-sale.
3. The transparency schedule (Article 3) continues post-sale for the same term.
4. **20% of net proceeds** (as defined) go first to Candour's own non-profit initiatives (Article 8); if none exist, to an external asset-locked charity or non-profit signed off in a published decision record.
5. The sale agreement **names the condition-4 recipient as entitled to enforce conditions 2 and 3** against the buyer, under the Contracts (Rights of Third Parties) Act 1999 — so someone with standing and motive can collect on these promises after the founder has been paid and gone.
6. The founder publishes, at the time of sale, an assessment of the buyer against these conditions — itemising all consideration received (see net proceeds) and stating the date of first contact (11.3). The judgment is made against this checklist, not against feelings.

### 7.2 Discontinuation

Shutting a product down is an ending too, and triggers:

- At least **90 days' notice** to every customer.
- Full data export (Article 4) available throughout the notice period and for **90 days** after shutdown, free.
- The product's code is **open-sourced where third-party rights allow**; where they don't, that is stated publicly with the reason.
- A published closing cost sheet for the product's final period, **stating the build labour capitalised, the amount recovered from customers to date, and the unamortised remainder written off.**

### 7.3 Departure

If the founder walks away without a sale — winding down the brand or leaving it dormant — every live product is treated under 7.2. Joining another company while abandoning Candour's products does not bypass these rules: the products' endings are still discontinuations, with everything that entails.

These conditions may be strengthened by amendment at any time; weakening them once a prospective ending exists is prohibited by Article 11.3.

---

## Article 8 — Non-profit initiatives

The CEO may designate any product a **non-profit initiative**, in a published decision record. Designation is permanent for that product and binds it to this annex on top of the rest of the constitution:

- **Zero distribution:** no profit is ever extracted from it, by anyone, at any time.
- Costs are limited to realistic infrastructure, support and management, all published.
- It can never be **sold**: it may only be transferred to an asset-locked body (a charity or CIC), and Article 7.2 governs any shutdown.
- Stated intent: when it becomes operationally real, it spins out into its own asset-locked entity, sharing this constitution's values but legally independent — as charity or sector governance may require.
- Open-source and self-hostable design is **encouraged wherever possible**, decided per initiative at its gate and recorded with reasons.

Non-profit initiatives are also the first-preference recipients of the waterfall's donations (2.3) and of sale proceeds (7.1).

---

## Article 9 — How to game this document

We name our own loopholes, and publish the numbers that expose each one:

| Loophole                                                   | The number that exposes it                                                              |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Inflating costs to raise the allowable price (2.1)         | Itemised cost sheets with third-party costs identifiable and labour benchmarked         |
| Salary creep around the distribution cap (2.2)             | Published compensation against a published benchmark                                    |
| Related-party payments disguised as costs                  | Any payment to the founder, family, or affiliated entities is separately disclosed      |
| Redefining "cost," "surplus," "reserve," "net proceeds," or the standard amortisation period | Definitions may only change by public amendment (Article 11), and a change to the period publishes its effect on every live product |
| Quietly weakening the rules                                | Full public change history; weakening amendments flagged as such (11.2)                 |
| Shrinking "net proceeds" via side deals                    | The definition includes all consideration in any form; the sale assessment itemises it  |
| Selling out and blaming the buyer                          | Article 7's pre-committed conditions, third-party enforcement, and published assessment |
| Setting or amending the standard amortisation period to suit whichever product is being priced at the time | Fixed company-wide; changes only by public amendment and **only prospectively**. Every change publishes, for every live product, the build labour still unrecovered and the price effect on each |
| Inflating capitalised build hours, or capitalising work that is really maintenance | Capitalised hours per product against the gate estimate **and** hours actually recorded, restated annually; plus capitalised hours as a share of all hours worked on the product that year, which trends to zero in steady state |
| Restarting the clock with a "v2" — re-badging maintenance as a new build to open a fresh layer | The published amortisation schedule: hours, ship date, period, amortised to date, balance. A real increment has a shipped change behind it; a fake one is a layer with no release note |
| The price never falls when the build leaves the cost base — by inaction, or by opening a new layer to offset every expiry | The counterfactual price at every republication: what the price would be if no layer had opened since the last expired. Plus the annual margin at the first republication after an expiry, against 2.1's cap |
| Deferring the amortisation start date, because "launch" is a soft enough word to move | The start date is the earlier of first sale and public release, published on the first cost sheet and never restated, **with the date of the first pound of revenue published beside it** |
| A one-off or pay-once tier escaping the cumulative lifetime margin test (2.1), which constrains only what a subscriber pays *by staying* | The **annual** margin on every tier including one-off tiers, at every republication, with one-off revenue recognised over the amortisation period rather than in the year of receipt |
| Recovering the build quickly and then discontinuing once it is recovered | The closing cost sheet's unamortised remainder written off (7.2), against the published amortisation start date. **An early discontinuation showing a write-off of zero is a product whose customers paid for the whole build and did not get the product** |

If a reader finds a gaming vector not listed here, we commit to adding it rather than using it.

---

## Article 10 — Honesty of this document itself

- This constitution currently binds through publicity, not law. We say so plainly rather than implying legal force we don't have.
- Where we have not yet done a thing (published a cost sheet, drawn a salary), the relevant rules are commitments about the future, and are marked as such by context.
- The Article 11.3 freeze relies on the founder truthfully reporting when ending conversations began. The trigger is defined objectively (any written expression of interest, sent or received) and the date must be published in the sale assessment — but a determined liar could misstate it. We admit this residual gap rather than pretend the clause is watertight; what the rule guarantees is that dodging it requires an affirmative false statement on the public record, not a definitional shrug.
- **This document does not cover everything, and one gap is named here deliberately rather than left to be discovered.** It says nothing about a product limiting a customer's access to content that customer authored and holds on their own device. In September 2026, three seats asked whether such a limit was permitted filled that silence by over-reading the export clause in Article 4, and reported a prohibition that does not exist; the error was caught by the founder, not by any agent, and is recorded in full in `decisions/2026-09-16-haunt-gate.md`. **The gap is left open deliberately** — legislating it in haste, around a single product's pricing question, is how a constitution acquires rules it cannot defend. What binds meanwhile is everything that already does: pricing stated plainly and in advance (1.3, Article 4), no profiting from lock-in or confusion (1.2), no dark patterns, and the export clause read for what it says. Naming a gap is a commitment to argue about it in the open when it next matters.
- **The standard amortisation period is one number applied to every product, chosen because a period chosen per product is a period chosen to suit a price.** It is therefore, for any particular product, an approximation of nothing in particular — it does not claim to track how long that product will live or be supported. We say so here because a cost sheet showing a build cost spread over a fixed term invites exactly the opposite reading, and because the alternative — a period tuned per product — is the loophole this convention exists to close. What a customer is owed when a product ends is in Article 7.2, and does not move with this number.
- Candour is operated by its founder together with **AI agents** holding the seats in Article 6, working under written charters. We disclose this because transparency includes how we work — and because it sets honest expectations: agent output is reviewed under this constitution's gates, and agent reviews prepare rather than certify (6.1).

---

## Article 11 — Amendments

1. Any change to this document is recorded in a public change log with date, diff, and rationale.
2. Amendments that **weaken** a customer-facing or transparency rule must be explicitly labelled "WEAKENING" in the change log and include the reason.
3. No amendment to Article 7 (endings) is permitted from the moment any written expression of interest in a sale — sent or received — exists, until the matter concludes. The date of first contact is published in the sale assessment (7.1.6).
4. Version 1.0 was declared when all bracketed placeholders were resolved (see CHANGELOG, v1.0). Amendments continue under this article.

---

_Founded by David, 2026. Built with candour._
