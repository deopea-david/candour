# The Candour Constitution

**Version:** 0.2 (draft) · **Status:** Unincorporated brand — this document is a public pledge, not yet a legal instrument · **Change log:** all amendments are recorded per Article 11 in `CHANGELOG.md`

---

## Preamble

Candour exists to build software that is genuinely useful to everyday people and businesses, priced honestly, and run transparently enough that trust never has to be taken on faith.

This constitution is the company's highest authority. Every product, decision, role, and agent operates under it. Where any plan conflicts with this document, the plan changes or the document is amended publicly — never quietly.

The company is currently a brand operated by its founder, not a registered legal entity. Nothing here is legally enforceable yet. Its force comes from being published, versioned, and written _before_ any money was at stake: breaking these rules later is visible rule-breaking, on the record. When the company incorporates, this constitution becomes the basis of its legal governing documents.

---

## Definitions

These terms mean the same thing everywhere in this constitution and in every Candour document. Per Article 9, they may only change by public amendment.

- **Cost:** everything it takes to run a product or the company, itemised — hosting, tooling, support, third-party services, and labour valued at a published market benchmark whether or not it is actually paid.
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

- Every product publishes a **cost sheet**: hosting, tooling, support, third-party services, and a fair-market cost for labour (including the founder's, whether or not it is actually drawn).
- Prices target a margin of approximately **20% over published costs**. This is a published target, not a rigid formula: deviations are permitted but must be justified in writing on the cost sheet (e.g. building a reserve, absorbing a cost spike).
- Cost sheets are reviewed and republished at least **annually** and at every price change.
- Labour is always costed at a stated market benchmark, so unpaid effort never fakes a low price and salary inflation never hides a high one.

### 2.2 Extraction rule

- All founder/owner compensation (salary, distributions, benefits) is **published**, with the benchmark pay is set against (default: the median UK software developer salary, adjusted for hours actually worked). Being paid is legitimate; being paid opaquely is not.
- Distributions may not exceed **[35]% of annual surplus** — deliberately mirroring the UK Community Interest Company cap, so conversion to a CIC later requires no weakening. Distributions are taken only at step 2 of the waterfall below, never outside it.

### 2.3 The profit waterfall

Each year, profit is applied strictly in this order, and the full allocation is published:

1. **Reserve top-up** — until the reserve reaches its 6–12 month target.
2. **Distributions** — optionally, up to [35]% of the surplus (2.2), always published.
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
- Make cancellation as easy as signup.
- Employ **no dark patterns**: no false urgency, no confirm-shaming, no pre-ticked boxes, no deliberately buried settings, no engagement mechanics designed to exploit compulsion.
- Collect the minimum data necessary, state why, and delete it when no longer needed.
- Let customers leave with their data: export in a usable, machine-readable format, available at any time, at no charge and with no penalty.
- Meet accessibility standards (WCAG 2.1 AA as the working baseline).
- Remain honest in marketing: claims we cannot substantiate are claims we do not make.

---

## Article 5 — Governance and decision gates

### 5.1 The pipeline

Ideas move through fixed stages: **spark → discovery (research brief, cost model, feasibility) → proposal → gate → build (requirements → architecture → build → verification) → release**. Each stage produces a written artifact stored in the company repository.

### 5.2 The anti-drift rule

Every idea entering the pipeline receives a **kill / proceed / park decision within [4] weeks** of its research brief. The clock cannot be stalled upstream: research briefs are **due [3] weeks from commissioning** (one extension allowed, with a written reason), and if a brief is overdue, the decision clock starts at its due date regardless. "Park" requires a written reason and a revisit date. This rule exists to force building over perpetual planning, and it binds the founder above all.

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

Agent reviews **prepare and flag; they do not certify**. Before launch, anything involving personal data at scale, payments, health information, or regulated domains receives review by qualified human professionals. The company never represents an AI compliance opinion as assurance.

---

## Article 7 — Endings

A product's ending — sale, discontinuation, or the founder's departure — is where trust promises are cheapest to break. So the rules for endings are fixed here, in advance, while no ending is on the table.

### 7.1 Sale

The company (or any product) may be sold — each transaction, however small, triggering all of the following:

1. The buyer **publicly adopts this constitution** as a condition of sale, locked for the same **[3]-year** term as condition 2; during that term, amendments weakening rules facing acquired customers are prohibited.
2. Existing customers' pricing rules (Article 2.1) are **contractually locked for [3] years** post-sale.
3. The transparency schedule (Article 3) continues post-sale for the same term.
4. **[10–25]% of net proceeds** (as defined) go first to Candour's own non-profit initiatives (Article 8); if none exist, to an external asset-locked charity or non-profit signed off in a published decision record.
5. The sale agreement **names the condition-4 recipient as entitled to enforce conditions 2 and 3** against the buyer, under the Contracts (Rights of Third Parties) Act 1999 — so someone with standing and motive can collect on these promises after the founder has been paid and gone.
6. The founder publishes, at the time of sale, an assessment of the buyer against these conditions — itemising all consideration received (see net proceeds) and stating the date of first contact (11.3). The judgment is made against this checklist, not against feelings.

### 7.2 Discontinuation

Shutting a product down is an ending too, and triggers:

- At least **[90] days' notice** to every customer.
- Full data export (Article 4) available throughout the notice period and for **[90] days** after shutdown, free.
- The product's code is **open-sourced where third-party rights allow**; where they don't, that is stated publicly with the reason.
- A published closing cost sheet for the product's final period.

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
| Redefining "cost," "surplus," "reserve," or "net proceeds" | Definitions may only change by public amendment (Article 11)                            |
| Quietly weakening the rules                                | Full public change history; weakening amendments flagged as such (11.2)                 |
| Shrinking "net proceeds" via side deals                    | The definition includes all consideration in any form; the sale assessment itemises it  |
| Selling out and blaming the buyer                          | Article 7's pre-committed conditions, third-party enforcement, and published assessment |

If a reader finds a gaming vector not listed here, we commit to adding it rather than using it.

---

## Article 10 — Honesty of this document itself

- This constitution currently binds through publicity, not law. We say so plainly rather than implying legal force we don't have.
- Where we have not yet done a thing (published a cost sheet, drawn a salary), the relevant rules are commitments about the future, and are marked as such by context.
- The Article 11.3 freeze relies on the founder truthfully reporting when ending conversations began. The trigger is defined objectively (any written expression of interest, sent or received) and the date must be published in the sale assessment — but a determined liar could misstate it. We admit this residual gap rather than pretend the clause is watertight; what the rule guarantees is that dodging it requires an affirmative false statement on the public record, not a definitional shrug.
- Candour is operated by its founder together with **AI agents** holding the seats in Article 6, working under written charters. We disclose this because transparency includes how we work — and because it sets honest expectations: agent output is reviewed under this constitution's gates, and agent reviews prepare rather than certify (6.1).
- Placeholder values in **[brackets]** are decisions still open; they will be fixed before version 1.0.

---

## Article 11 — Amendments

1. Any change to this document is recorded in a public change log with date, diff, and rationale.
2. Amendments that **weaken** a customer-facing or transparency rule must be explicitly labelled "WEAKENING" in the change log and include the reason.
3. No amendment to Article 7 (endings) is permitted from the moment any written expression of interest in a sale — sent or received — exists, until the matter concludes. The date of first contact is published in the sale assessment (7.1.6).
4. Version 1.0 is declared when all bracketed placeholders are resolved; until then this is a working draft.

---

_Founded by David, 2026. Built with candour._
