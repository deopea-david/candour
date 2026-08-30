# The Candour Constitution

**Version:** 0.1 (draft) · **Status:** Unincorporated brand — this document is a public pledge, not yet a legal instrument · **Change log:** all amendments are recorded in Article 11

---

## Preamble

Candour exists to build software that is genuinely useful to everyday people and businesses, priced honestly, and run transparently enough that trust never has to be taken on faith.

This constitution is the company's highest authority. Every product, decision, role, and agent operates under it. Where any plan conflicts with this document, the plan changes or the document is amended publicly — never quietly.

The company is currently a brand operated by its founder, not a registered legal entity. Nothing here is legally enforceable yet. Its force comes from being published, versioned, and written *before* any money was at stake: breaking these rules later is visible rule-breaking, on the record. When the company incorporates, this constitution becomes the basis of its legal governing documents.

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
- All founder/owner compensation (salary, dividends, benefits) is **published**, with the benchmark it is set against (default: the median UK software developer salary, adjusted for hours actually worked).
- Distributions (dividends or equivalents) may not exceed **[35]% of annual surplus** — deliberately mirroring the UK Community Interest Company cap, so conversion to a CIC later requires no weakening.

### 2.3 Reserves and surplus
- The company maintains a reserve of **6–12 months of operating costs**. Building this reserve is a legitimate use of margin.
- Surplus beyond the reserve is deployed in this order of preference:
  1. Price reductions for existing customers
  2. Funding new products under this constitution
  3. Donations to asset-locked bodies (charities/CICs) aligned with the mission
- The allocation of surplus is published annually.

---

## Article 3 — Transparency schedule

The following are public, permanently, for anyone to inspect:

| What | When |
|---|---|
| Product cost sheets and margins | At launch, at every price change, and at least annually |
| Founder/owner compensation and its benchmark | Annually, from the first pound drawn |
| Surplus allocation (2.3) | Annually |
| This constitution and its full change history | Continuously |
| Decision records for kill/proceed gates (Article 5) | Within 30 days of the decision |
| Security or data incidents affecting users | Prompt disclosure to affected users; public summary after resolution |

What is *not* published: individual customer data, security-sensitive implementation details, and third parties' confidential terms. The boundary is drawn here, in advance, so it is never improvised under pressure.

---

## Article 4 — Product ethics

Every product must, without exception:

- Use plain-language pricing with no hidden fees, forced bundles, or drip pricing.
- Make cancellation as easy as signup.
- Employ **no dark patterns**: no false urgency, no confirm-shaming, no pre-ticked boxes, no deliberately buried settings, no engagement mechanics designed to exploit compulsion.
- Collect the minimum data necessary, state why, and delete it when no longer needed.
- Meet accessibility standards (WCAG 2.1 AA as the working baseline).
- Remain honest in marketing: claims we cannot substantiate are claims we do not make.

---

## Article 5 — Governance and decision gates

### 5.1 The pipeline
Ideas move through fixed stages: **spark → research brief → proposal → gate → discovery → build → release**. Each stage produces a written artifact stored in the company repository.

### 5.2 The anti-drift rule
Every idea entering the pipeline receives a **kill / proceed / park decision within [4] weeks** of its research brief. "Park" requires a written reason and a revisit date. This rule exists to force building over perpetual planning, and it binds the founder above all.

### 5.3 Mandatory dissent
No proposal passes a gate without a **Skeptic memo** attached: the strongest counter-argument, plausible failure modes, and who could be harmed. Approving a proposal requires responding to the dissent in writing, not merely outvoting it.

### 5.4 Human decision points
The following are never automated: kill/proceed decisions, spending real money, pricing changes, anything affecting user data policy, and release to real users. Agents prepare; the founder decides.

### 5.5 Reviews and demos
Every pipeline phase concludes with a **review pack and demo** presented to the CEO in the boardroom, compiled by the Chief Governance Officer. Work is not "done" until it has been reviewed.

---

## Article 6 — Roles

The company is operated by its founder (CEO, and part of the CVO function) together with AI agents holding the seats below. Each seat has a one-page charter (kept in `roles/`) defining its mandate, the questions it must ask, and what it can block.

**Active seats**

| Seat | Mandate in one line |
|---|---|
| **CEO** (human) | Final authority on all human decision points (5.4); owns this constitution's spirit |
| **Chief Vision Officer** (shared: human + agent) | Originates and develops ideas; commissions discovery; drafts proposals |
| **Chief Governance Officer** | Enforces this constitution; runs gates, cadence and reviews; owns regulatory conformance (incl. UK GDPR, consumer law, accessibility) |
| **Chief Technology Officer** | Technical architecture; build-vs-buy; keeps the stack boring and cheap |
| **Chief Security Officer** | Secure design and industry standards (e.g. OWASP), from architecture through release; partners with the CTO |
| **Chief Financial Officer** | Unit economics, cost sheets, pricing transparency (Article 2–3) |
| **The Skeptic** | Institutional dissent (5.3). Deliberately not a C-title: this seat defends nothing and negotiates nothing |
| **Product Manager / BA** | Turns approved proposals into scoped requirements and acceptance criteria |
| **UX / Design Lead** | Usability for everyday people; polices dark patterns from the design side |
| **Engineer(s)** | Builds it |
| **QA Engineer** | Independent verification against acceptance criteria; edge cases; release readiness |
| **Research Analyst** | Market, user, competitor and feasibility research under CVO commission |

**Dormant seats** (defined now, activated when reality demands): **COO** (when there are operations), **Chief Legal Officer** (at incorporation or first contract).

### 6.1 Limits of agent authority
Agent reviews **prepare and flag; they do not certify**. Before launch, anything involving personal data at scale, payments, health information, or regulated domains receives review by qualified human professionals. The company never represents an AI compliance opinion as assurance.

---

## Article 7 — Sale and succession

The company (or any product) may be sold, but only under conditions fixed here, in advance, while no sale is on the table:

1. The buyer **publicly adopts this constitution** as a condition of sale.
2. Existing customers' pricing rules (Article 2.1) are **contractually locked for [3] years** post-sale.
3. The transparency schedule (Article 3) continues post-sale, or the sale terms are breached.
4. **[10–25]% of net sale proceeds** go to an asset-locked destination (a charity or CIC aligned with the mission; if the NHS project exists as an entity, it is the default recipient).
5. The founder publishes, at the time of sale, an assessment of the buyer against these conditions — the judgment is made against this checklist, not against feelings.

These conditions may be strengthened by amendment at any time; weakening them once a prospective sale exists is prohibited by Article 11.3.

---

## Article 8 — The NHS project annex

The NHS platform initiative operates under this constitution **plus** a stricter annex:

- **Zero distribution:** no profit is ever extracted from it, by anyone.
- Costs are limited to realistic infrastructure, support and management, all published.
- It is open-source and self-hostable by design.
- Stated intent: when it becomes operationally real, it spins out into its own asset-locked entity (charity or CIC), sharing this constitution's values but legally independent — as charity and healthcare governance will require.

---

## Article 9 — How to game this document

We name our own loopholes, and publish the numbers that expose each one:

| Loophole | The number that exposes it |
|---|---|
| Inflating costs to raise the allowable price (2.1) | Itemised cost sheets with third-party costs identifiable and labour benchmarked |
| Salary creep around the distribution cap (2.2) | Published compensation against a published benchmark |
| Related-party payments disguised as costs | Any payment to the founder, family, or affiliated entities is separately disclosed |
| Redefining "cost," "surplus," or "reserve" | Definitions may only change by public amendment (Article 11) |
| Quietly weakening the rules | Full public change history; weakening amendments flagged as such (11.2) |
| Selling out and blaming the buyer | Article 7's pre-committed conditions and published assessment |

If a reader finds a gaming vector not listed here, we commit to adding it rather than using it.

---

## Article 10 — Honesty of this document itself

- This constitution currently binds through publicity, not law. We say so plainly rather than implying legal force we don't have.
- Where we have not yet done a thing (published a cost sheet, drawn a salary), the relevant rules are commitments about the future, and are marked as such by context.
- Placeholder values in **[brackets]** are decisions still open; they will be fixed before version 1.0.

---

## Article 11 — Amendments

1. Any change to this document is recorded in a public change log with date, diff, and rationale.
2. Amendments that **weaken** a customer-facing or transparency rule must be explicitly labelled "WEAKENING" in the change log and include the reason.
3. No amendment to Article 7 (sale) is permitted from the moment a specific sale conversation begins until it concludes.
4. Version 1.0 is declared when all bracketed placeholders are resolved; until then this is a working draft.

---

*Founded by David, [year]. Built with candour.*
