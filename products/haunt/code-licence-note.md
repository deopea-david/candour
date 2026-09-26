# Code licence note — Haunts (`deopea-david/haunts`)

**Seat:** Chief Governance Officer · **Date:** 2026-09-26 · **Commissioned by:** the main session, on the CEO's referral in **D28** (`decisions/2026-09-16-haunt-gate.md`, CEO decisions log)
**Slug:** `haunt` · **Reads with:** D27, D28; `LICENSE.md`; `constitution.md` v1.3; `requirements.md` §13 (LIC) and §16 (PLAT); `compliance-note.md` §2; `android-and-stack-note.md`; `map-options-comparison.md`
**Status:** Prepared for the CEO. **This is not a legal opinion and is not assurance** (Constitution 6.1: agent reviews *"prepare and flag; they do not certify"*). Where I write "compatible" or "permitted", read "I found nothing in the retrieved text that forbids it, and the text is quoted so you can check me".

> **Template note.** `pipeline/templates/` holds no licence-note or compliance-note template. This note follows the shape the commission asked for (seven questions), plus a decision list and an evidence register. I have not created a template.

> **Retrieval.** Every [E] below was retrieved on **2026-09-26** during this session, by direct download of the page (curl) and reading of the text, unless marked otherwise. Nothing is cited from memory. [K] marks model knowledge I did not verify this session.

---

## 0. The answer on one page

**Recommended licence: PolyForm Noncommercial License 1.0.0** (SPDX `PolyForm-Noncommercial-1.0.0`), applied to **Candour's own code only**, with every third-party component and dataset keeping its own terms.

**The one-sentence reason:** it is the only candidate that is written for software by licensing lawyers, is standardised and recognised (SPDX-listed), grants personal use, study, modification and noncommercial sharing in plain words, and bars everyone except the licensor from commercial use, which is what D28 asks for.

**What the CEO needs to know before accepting it, in order of weight:**

1. **It is not open source, and says so itself.** The PolyForm Project states it is *"Not… open source or free software"* [E]; the Open Source Definition bars restricting use *"in a business"* (criterion 6) [E]; SPDX records it as not OSI-approved [E]. So **`LICENSE.md`'s presumption in favour of open source is displaced only by a written reason in the decision record, and that reason is the CEO's to give** (§5). A neutral scaffold is drafted at §5.3 with the reason left blank.
2. **"Personal use yes" includes building it for free.** Anyone may compile Haunts from the public source and run it without paying, and may **share** builds (modified or not) for noncommercial purposes. That is what the licence permits and what "personal use" means once the source is public. If the CEO wants personal use **without** free redistribution, the alternative is **PolyForm Strict** (use only; no sharing, no modification) (§3.4). This is Decision 1.
3. **Charities and public bodies may use it for any purpose.** PolyForm Noncommercial permits use by *"any charitable organization… or government institution… regardless of the source of funding"* [E]. On the plain text that is not limited to noncommercial activity (§3.3).
4. **It does not satisfy Article 7.2 at shutdown on my reading, and D28's framing understates this.** Article 7.2 requires the code to be *"open-sourced where third-party rights allow"*. A licence that its own authors say is not open source is not "open-sourced" in the ordinary meaning of the word [J, with reasons at §6]. **Candour should commit now to relicensing under an OSI-approved licence on discontinuation**, and I recommend making that commitment **self-executing** so it survives the founder's absence under Article 7.3 (§6.3). This is not a weakening under Article 11; a product-level commitment is not an amendment at all, and a constitutional clarification would be a strengthening (§6.4).
5. **Outside code contributions cannot be accepted on the default terms.** GitHub's terms make contributions *inbound = outbound* [E], so a contributor's code would reach Candour under the Noncommercial licence too, and Candour could then neither sell it in the app nor relicense it at shutdown. **Recommendation: accept no outside code at v1** (issues and discussion welcome); a DCO does not fix this and a CLA needs a lawyer (§7.3).

**Compatibility with the inbound terms is not a problem** (§4): CDLA-Permissive-2.0, Apache-2.0 (Foursquare NOTICE), OGL v3.0 and the MIT/BSD dependency tree all permit inclusion in a product whose own code is under different terms, provided their notice conditions are met. LIC-1…LIC-6 already require that for the **data**; the **code dependencies'** notices are not yet in the requirements, and I propose a LIC-7 (§7.2). The one thing to guard against is a **copyleft (GPL-family) dependency**, which would conflict (§4.5).

**Constitution and `LICENSE.md` conflicts:** none today. Two obligations become live: `LICENSE.md` requires the written reason **before the code is published under a non-open-source licence**, and Article 7.2 requires the code to be open-sourced **on discontinuation**. A third is an Article 9 commitment I think is triggered: I found a gaming vector not listed there, and Article 9 says *"we commit to adding it rather than using it"* (§6.5).

**Human review (Constitution 6.1):** the clause's licence limb is aimed at third-party licence terms that determine architecture or cost; I do **not** find it clearly triggered by the outbound licence choice, and I say so rather than stretch it (§8). I **recommend**, as my own judgment, that the licence set, the copyright position of AI-generated code, and any CLA or self-executing relicensing grant go into the **L1 legal review** that is already a launch bar. That costs little extra because L1 is being bought anyway.

---

## 1. What our own rules say, quoted

**`LICENSE.md`, "Product code":**
> *"Code for Candour products is **not** covered by this licence. Each product's code licence is decided at its gate and recorded in its decision record, with a stated presumption in favour of open source unless the decision record gives a written reason otherwise."*

Three limbs: (a) decided **at its gate**; (b) **recorded in its decision record**; (c) presumption of open source, displaced only by **a written reason in the decision record**.

- Limb (a): the Haunt gate (2026-09-16) did not decide a code licence; D28 (2026-09-26) is a post-gate entry in the same record. **That is a procedural slip against the words "at its gate", not a substantive breach**: the decision is still being recorded in the decision record, in public, before any code is published. I flag it and do not block on it. [I]
- Limb (b): D28 records the intent (*"a licence permitting personal use but not commercial use"*) but not a licence text. **A further entry naming the licence (SPDX identifier and version) is owed.**
- Limb (c): owed, and the CEO's to state (§5).

**Constitution v1.3, Article 7.2 (Discontinuation):**
> *"The product's code is **open-sourced where third-party rights allow**; where they don't, that is stated publicly with the reason."*

**Article 7.3 (Departure):**
> *"If the founder walks away without a sale — winding down the brand or leaving it dormant — every live product is treated under 7.2."*

**Article 7, closing:**
> *"These conditions may be strengthened by amendment at any time; weakening them once a prospective ending exists is prohibited by Article 11.3."*

**Article 4 (honest marketing):**
> *"Remain honest in marketing: claims we cannot substantiate are claims we do not make."*

**Article 6.1:**
> *"Before launch, anything involving personal data at scale, payments, health information, regulated domains, or **third-party licence terms whose interpretation determines a product's architecture or cost**, receives review by qualified human professionals. The company never represents an AI compliance opinion as assurance."*

**Article 9, closing line:**
> *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."*

**Article 3** lists what is public; **product source code is not on the schedule.** Nothing in the Constitution requires Haunts' code to be public while the product is live. D28's "private now" breaches nothing. [I, from the Article 3 table as read]

**The term "open source" / "open-sourced" is not in the Constitution's Definitions.** I read the Definitions section: it defines Cost, Standard amortisation period, Profit, Reserve, Surplus, Distribution and Net proceeds, and nothing else. [E, `constitution.md` v1.3, read from disk 2026-09-26]

**Customer-facing copy already relies on 7.2.** `requirements.md` §10.1, canonical draft S3: *"If we ever stop supporting Haunts you'll get at least 90 days' notice, your data stays exportable — free, in full, and for 90 days after — **and we open-source what we can.**"* That sentence is a claim Article 4 requires Candour to be able to substantiate (§6.2).

---

## 2. Candidate licences, retrieved at source

### 2.1 Summary table

| Candidate | Personal use | Modify | Share (noncommercial) | Commercial use by others | Written for software? | Patent grant | Standardised / recognised | Verdict |
|---|---|---|---|---|---|---|---|---|
| **PolyForm Noncommercial 1.0.0** | Yes | Yes | Yes | **No** | **Yes** | Yes | SPDX-listed; plain-language; lawyer-drafted | **Recommended** |
| **PolyForm Strict 1.0.0** | Yes | **No** | **No** | **No** | Yes | Yes | SPDX-listed [K for SPDX listing of Strict; not retrieved] | **The alternative** if free redistribution is unwanted |
| **PolyForm Small Business 1.0.0** | Yes | Yes | Yes | **Yes, for small businesses** | Yes | Yes | Standardised | **Rejected**: permits the commercial use D28 forbids |
| **CC BY-NC-SA 4.0** | Yes | Yes | Yes, share-alike | No | **No** — CC advises against it for software | **No** | Very widely known | **Rejected** on CC's own advice |
| **Custom "all rights reserved, personal use permitted"** | As drafted | As drafted | As drafted | As drafted | Only if a lawyer drafts it | As drafted | **None** | **Rejected** unless lawyered; cost and ambiguity |
| BSL 1.1 (for comparison) | **Non-production use only** | Yes | Yes | Only via "Additional Use Grant" | Yes | — | Widely used | Not a fit: bars production use, which would bar personal use of the app itself |
| PolyForm Shield / Perimeter (for comparison) | Yes | Yes | Yes | **Yes, unless competing** | Yes | Yes | Standardised | Different intent: fits "no competitors", not "no commercial use" |

### 2.2 PolyForm Noncommercial 1.0.0

Retrieved in full at [polyformproject.org/licenses/noncommercial/1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0) and corroborated at [SPDX, PolyForm-Noncommercial-1.0.0](https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.html) (SPDX notes it was *"released on July 9, 2019"*). [E]

The clauses that do the work, verbatim:

- **Copyright licence:** *"The licensor grants you a copyright license for the software to do everything you might do with the software that would otherwise infringe the licensor's copyright in it for any permitted purpose."*
- **Distribution:** *"The licensor grants you an additional copyright license to distribute copies of the software."*
- **Notices:** *"You must ensure that anyone who gets a copy of any part of the software from you also gets a copy of these terms or the URL for them above, as well as copies of any plain-text lines beginning with `Required Notice:` that the licensor provided with the software."*
- **Changes:** *"The licensor grants you an additional copyright license to make changes and new works based on the software for any permitted purpose."*
- **Patent licence:** granted, with a patent-defence termination.
- **Noncommercial Purposes:** *"Any noncommercial purpose is a permitted purpose."*
- **Personal Uses:** *"Personal use for research, experiment, and testing for the benefit of public knowledge, personal study, private entertainment, hobby projects, amateur pursuits, or religious observance, without any anticipated commercial application, is use for a permitted purpose."*
- **Noncommercial Organizations:** *"Use by any charitable organization, educational institution, public research organization, public safety or health organization, environmental protection organization, or government institution is use for a permitted purpose regardless of the source of funding or obligations resulting from the funding."*
- **No Other Rights:** *"These terms do not allow you to sublicense or transfer any of your licenses to anyone else, or prevent the licensor from granting licenses to anyone else. These terms do not imply any other licenses."*
- **Violations:** a 32-day cure period after first written notice.

**What the licensor keeps:** everything not granted. The licence restricts the licensee, not Candour; "No Other Rights" expressly preserves the licensor's freedom to license others (including Apple's and Google's end users) on different terms. [E, clause above]

**Where PolyForm places itself**, from its own "About" page: *"PolyForm is not… Open source or free software. There are plenty of existing open source licenses. PolyForm is not a substitute for them, but an alternative for those who want to license source code under limited rights."* It also says it is *"Not… A substitute for legal counsel."* [E, [polyformproject.org/about](https://polyformproject.org/about)]

### 2.3 PolyForm Strict 1.0.0

Retrieved at [polyformproject.org/licenses/strict/1.0.0](https://polyformproject.org/licenses/strict/1.0.0). [E] It is the Noncommercial licence with the distribution and changes grants removed:

> *"The licensor grants you a copyright license for the software to do everything you might do with the software that would otherwise infringe the licensor's copyright in it for any permitted purpose, **other than distributing the software or making changes or new works based on the software**."*

Its Personal Uses and Noncommercial Organizations clauses are word-for-word the same as Noncommercial's. PolyForm's own summary: *"PolyForm Strict removes permission to distribute copies and make changes, leaving only permission to use for noncommercial purposes."* [E, [polyformproject.org/licenses](https://polyformproject.org/licenses)]

**Consequence:** a person may read, build and run Haunts for personal use, but may not change it (not even locally, to test a fix) and may not hand a build to anyone. A security researcher could inspect and run it, but not patch it to test a hypothesis. [I]

### 2.4 PolyForm Small Business 1.0.0

Retrieved at [polyformproject.org/licenses/small-business/1.0.0](https://polyformproject.org/licenses/small-business/1.0.0). [E] It adds:

> *"Use of the software for the benefit of your company is use for a permitted purpose if your company has fewer than 100 total individuals working as employees and independent contractors, and less than 1,000,000 USD (2019) total revenue in the prior tax year."*

**Rejected:** it **permits commercial use** by exactly the kind of small operator who could re-skin Haunts and sell it. It contradicts D28's *"not commercial use"* on its face. [I]

### 2.5 CC BY-NC-SA 4.0, and Creative Commons' own advice

Legal code retrieved at [creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en). NonCommercial is defined as *"not primarily intended for or directed towards commercial advantage or monetary compensation."* [E]

**Creative Commons advises against using its licences for software.** From the [CC FAQ](https://creativecommons.org/faq/), under "Can I apply a Creative Commons license to software?" [E]:

> *"We recommend against using Creative Commons licenses for software. Instead, we strongly encourage you to use one of the very good software licenses which are already available."*

It gives three reasons: CC licences *"do not contain specific terms about the distribution of source code"*; they do not address patents; and *"our licenses are currently not compatible with the major software licenses"*. [E, same page]

CC's own NonCommercial interpretation page adds two points that matter here [E, [CC wiki, NonCommercial interpretation](https://wiki.creativecommons.org/wiki/NonCommercial_interpretation), oldid 116467]:
- *"NonCommercial turns on the use, not the identity of the reuser."* (This is **better** than PolyForm on the charity question: a charity's commercial use is still commercial under CC NC.)
- The NC licences *"do not qualify as 'open licenses' under the Open Definition"*.

**Rejected.** The steward of the licence tells software authors not to use it, and it has no patent grant and no source-code terms. Choosing it against that advice is the kind of choice a stranger auditing the record would ask about, and the answer would be weak. [J] **Its one advantage (use-based NC, so charities cannot sell forks) is noted in §3.3.**

### 2.6 A custom "all rights reserved, personal use permitted" grant

No text exists to retrieve; this would be drafted. Two retrieved facts shape it:

- **Without any licence, others get nothing beyond what GitHub's terms give them.** GitHub: *"without a license, the default copyright laws apply, meaning that you retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work."* [E, [GitHub Docs, Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)]
- **But a public GitHub repository always carries GitHub's own view-and-fork licence**, whatever file sits in the repo: *"By making a repository public, you grant other Users a nonexclusive, worldwide license to use, display, perform and reproduce (by forking) Your Content through the Service as permitted by GitHub's functionality."* [E, [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) §D.5, effective 2026-04-27]

**Rejected**, unless a qualified lawyer drafts it. A home-made grant is precisely where "personal", "commercial" and "use" become arguable, and it has none of the recognition that lets a reader understand PolyForm at a glance (SPDX identifier, published text, drafting by specialists). Paying a lawyer to draft what PolyForm already publishes free breaches the spirit of Constitution 1.5 (*"Cheap to run, cheap to buy"*). [J]

### 2.7 For comparison only

- **Business Source License 1.1** grants the right to *"copy, modify, create derivative works, redistribute, and make **non-production use**"*, with a **Change Date** on which the code converts to an open-source "Change License" [E, [mariadb.com/bsl11](https://mariadb.com/bsl11/)]. A person running Haunts on their own phone to journal their life is using it in production [I], so BSL would bar the very personal use D28 wants. **Not a fit.** Its Change Date mechanism is relevant to §6.3.
- **PolyForm Shield / Perimeter** permit commercial use other than competing with the provider or the software [E, [polyformproject.org/licenses](https://polyformproject.org/licenses)]. If the CEO's real concern is "no one should sell a competing copy" rather than "no commercial use at all", Shield is the better fit. **I note it and do not recommend it**, because D28 says "not commercial use", and the record should implement what was decided rather than what a seat thinks might have been meant. [J]

---

## 3. Recommendation, and what "non-commercial" leaves open

### 3.1 Recommendation

**PolyForm Noncommercial License 1.0.0, unmodified, for Candour's own code in `deopea-david/haunts`.** Reasons, in order of weight:

1. **It implements D28 as written.** Personal use, study and tinkering are granted in plain words; commercial use by anyone but the licensor is not. [E, §2.2 clauses]
2. **It is made for software.** It covers source distribution, changes and patents. CC BY-NC-SA does none of these, and CC tells software authors not to use it. [E, §2.5]
3. **It is standard and cheap.** It has a published text, an SPDX identifier, and lawyer drafting, at a cost of £0. A stranger can look it up. Constitution 1.5 favours it over a bespoke grant. [J]
4. **It serves the reason the code is worth publishing at all.** Haunts is sold on a privacy claim: *"nothing about the user leaves the device"* (D22), backed by PRIV-8's no-network rule. Public source lets anyone check that claim. PolyForm expressly permits *"research, experiment, and testing for the benefit of public knowledge"*, and also lets a researcher patch and rebuild to test a hypothesis, which Strict does not. [E for the clause; J for the value]
5. **It leaves the licensor free.** Candour can sell the app under store terms, and can later grant an OSI licence (§6), because *"These terms do not… prevent the licensor from granting licenses to anyone else."* [E]

**Use it unmodified.** Much of PolyForm's value is that it is a known text. An edited PolyForm is a custom licence with a borrowed name. Clarifications belong in a separate, plainly non-binding FAQ, or in `Required Notice:` lines, not in edits to the licence. [J]

### 3.2 Most questions about "non-commercial" do not arise, because app users are not licensed by the repo

**The repository licence governs people who take the source code. People who buy Haunts from a store are licensed by the store terms, not by PolyForm.** [I, from the two sets of terms quoted at §7.5] So "can a freelancer use Haunts for work?" is mostly a store-terms question, not a PolyForm question. The PolyForm question arises only for someone who builds from source.

### 3.3 The ambiguous cases, and how the recommended text handles them

| Case | Under PolyForm Noncommercial | Confidence |
|---|---|---|
| A person builds Haunts from source and journals their own life | **Permitted.** *"private entertainment, hobby projects"*; *"Any noncommercial purpose"* | High [I] |
| A **freelancer** builds it and journals their own life | **Permitted**, same as above. Being self-employed does not make private journalling commercial | High [I] |
| A freelancer builds it and uses it to **log client site visits for invoicing or mileage claims** | **Probably not permitted.** Personal Uses requires *"without any anticipated commercial application"*, and logging work visits for billing has one. The general *"Any noncommercial purpose"* clause does not define the word, so this is the grey zone. **Practical answer: buy the app from the store** (§7.5), where the repo licence does not apply | Medium [I] |
| An employee at a company **reads** the source on GitHub | **No licence needed** to read; GitHub's §D.5 grant covers viewing [E]. Ideas and techniques learned are not restricted by copyright [K, high confidence] | High |
| A company copies a module (e.g. the grid-cell venue query) into its commercial product | **Not permitted.** Commercial use of the code | High [I] |
| A **security researcher** clones, patches and runs it to test the privacy claim, and publishes findings | **Permitted.** *"research, experiment, and testing for the benefit of public knowledge"* | High [I] |
| A school or university uses it in teaching | **Permitted.** *"educational institution"* | High [E] |
| A **charity** uses it internally, e.g. a history society logging site visits | **Permitted.** *"Use by any charitable organization… is use for a permitted purpose"* | High [E] |
| A charity **distributes a modified build, or charges for one** | **On the plain text, arguably permitted.** The Noncommercial Organizations clause makes use by a charity a permitted purpose with no qualification on the kind of use, and "use" is defined as *"anything you do with the software requiring one of your licenses"*, which includes distribution. **This is looser than D28's words.** CC's NC definition would catch it (*"turns on the use, not the identity"*), but CC is unsuitable for software (§2.5). **I recommend accepting it** as low-probability and in keeping with Article 8's regard for non-profits, and I record it so it is a known cost rather than a discovery | Medium [I]; the acceptance is [J] |
| Someone publishes **free builds** (APK, or modified "Haunts-lite") on their own site | **Permitted**, if noncommercial. That is the Distribution and Changes grant. They must pass on the licence terms and `Required Notice:` lines. **They get no right to the name** (*"These terms do not imply any other licenses"*), and the name is unprotected until PLAT-6's trademark check passes | High [I] |
| Someone publishes the same build on a store for a **price, or with ads** | **Not permitted.** Commercial | High [I] |

**The row the CEO should weigh most is the free-build row.** "Personal use yes" plus public source means a person who can compile Haunts can run it without buying it, and can share that build without charging. **That is inherent in the intent, not a flaw in the licence.** Its likely revenue effect is small, because very few buyers of a consumer journal app build from source [J, low-to-medium confidence; no evidence retrieved on this]. But the cost sheet's break-even (~2,400–2,700 sales over three years, per the gate record) is tight enough that the CEO should choose it knowingly. On iOS, running a self-built app needs Xcode and a developer account [K]; on Android, installing a shared APK is easy [K]. So the leak, if any, is mostly on Android.

### 3.4 If free redistribution is unwanted: PolyForm Strict

**Strict keeps "personal use yes, commercial no" and removes sharing and modification** (§2.3). It shuts the free-build row and the charity-fork row. It costs the patch-and-test value in reason 4 above, and it makes the repository "look and run, don't touch". **My recommendation stays Noncommercial** because the verification value is the best reason to publish at all, and the leak is probably small [J]. But this is a genuine trade-off between two defensible choices, and it is **Decision 1** (§9).

---

## 4. Compatibility with the inbound terms

### 4.1 The principle: the outbound licence covers Candour's own code only

**PolyForm Noncommercial will apply only to code Candour wrote (or holds the rights to). Every third-party library, dataset and asset keeps its own licence, and the repository must say so on its face.** Candour cannot relicense what it does not own, and must not appear to try. [I] The mechanism is in §7.1–7.2: a `LICENSE` that scopes itself to Candour's code, and a `THIRD_PARTY_NOTICES` file (plus per-directory licence files for any data in the repo) that lists everything else under its own terms.

The question for each inbound licence is therefore narrow: **does it permit its material to be distributed inside, or alongside, a product whose own code is under different, more restrictive terms, and on what conditions?**

### 4.2 Data: CDLA-Permissive-2.0 (Overture Places)

- §2.1: *"A Data Recipient may share Data, with or without modifications, so long as the Data Recipient makes available the text of this agreement with the shared Data."* [E, [cdla.dev/permissive-2-0](https://cdla.dev/permissive-2-0/)]
- §3.1: *"This agreement does not impose any restriction or obligations with respect to the use, modification, or sharing of Results."* [E, same]

**Compatible.** Its only condition is that the text travels with the data; nothing restricts the terms of the surrounding software. Already required by LIC-1/LIC-2. **The data itself stays under CDLA-Permissive-2.0; it is not relicensed under PolyForm.** [I]

### 4.3 Data: Apache-2.0, and the Foursquare OS Places NOTICE

- Apache-2.0 §4, closing paragraph: *"You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License."* [E, [apache.org/licenses/LICENSE-2.0.txt](https://www.apache.org/licenses/LICENSE-2.0.txt)]
- Apache-2.0 §1, "Derivative Works" *"shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof."* [E, same]
- Foursquare OS Places Notice: the recipient must *"provide recipients with a copy of the License"*, *"include prominent notices to the extent you've changed the Data"*, and *"preserve attribution to Foursquare, including preserving the full content of this NOTICE.txt file"*; for flat-file distribution, Foursquare recommends including NOTICE.txt itself. [E, [opensource.foursquare.com/places-notice-txt](https://opensource.foursquare.com/places-notice-txt/)] (Re-retrieved today; it matches `compliance-note.md` §2.2.)

**Compatible.** Apache-2.0 expressly allows different terms for the surrounding work, provided the Apache conditions are met for the Apache material. Candour's app code is separable from the venue data, so it is not a Derivative Work of it [I]. **Recommendation: do not place the Foursquare-derived index under PolyForm at all.** Keep it (and any committed copy of it) under its upstream terms, with NOTICE.txt and the modification notice beside it. Relicensing the data would be both unnecessary and, for the unmodified parts, ineffective, since anyone can obtain them from Foursquare under Apache-2.0. [I]

### 4.4 Data: OGL v3.0 (OS Open Zoomstack, per D22)

- Grant: *"copy, publish, distribute and transmit the Information; adapt the Information; exploit the Information commercially and non-commercially for example, by combining it with other Information, or by including it in your own product or application."* [E, [OGL v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)]
- Condition: *"acknowledge the source of the Information in your product or application by including or linking to any attribution statement specified by the Information Provider(s) and, where possible, provide a link to this licence"*. [E, same]
- **The OS attribution statement, now retrieved at primary:** *"Contains OS data © Crown copyright [and database right] [year]."* OS adds that the same acknowledgement *"should be incorporated into any sub-licences you grant others"*. [E, [Ordnance Survey, Copyright acknowledgments](https://www.ordnancesurvey.co.uk/customers/public-sector/public-sector-licensing/copyright-acknowledgments), read through a page-summarising fetch rather than a raw download; **single source, but it is the Information Provider's own page, which is the authoritative source for its own statement**. The CTO or the Skeptic should confirm the exact punctuation on a direct read before the string is fixed in code.]

**Compatible.** OGL is attribution-only with no share-alike, and expressly contemplates inclusion in *"your own product or application"*. **This also advances LIC-6**, whose attribution string was marked [K] and "not yet confirmed at primary": the string above is the primary form, and LIC-6(a) can now be written against it, subject to the punctuation check. The Zoomstack file is too large for the repo and is delivered as a store asset pack (D22), so it is not in `haunts`; **the tile-building pipeline code is Candour's and goes under PolyForm; any committed Zoomstack-derived tiles or samples stay under OGL.** [I]

### 4.5 The React Native / Expo dependency tree

**Retrieved from the npm registry today** (`registry.npmjs.org/<package>/latest`, `license` field) [E]:

| Package | Version | Licence |
|---|---|---|
| `react-native` | 0.87.1 | MIT |
| `react` | 19.3.0 | MIT |
| `expo` | 57.0.25 | MIT |
| `expo-modules-core` | 57.0.19 | MIT |
| `expo-location` | 57.0.20 | MIT |
| `expo-sqlite` | 57.0.3 | MIT |
| `expo-crypto` | 57.0.3 | MIT |
| `@maplibre/maplibre-react-native` | 11.4.0 | MIT |
| MapLibre Native (the renderer) | — | BSD-2-Clause [E, via `map-options-comparison.md` §2, retrieved by the CTO from the GitHub API; **not re-retrieved by me**] |

- **MIT** permits anyone *"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies"*, subject to *"The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."* [E, [OSI, MIT](https://opensource.org/license/mit)]
- **BSD-2-Clause:** *"Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution."* [E, [OSI, BSD-2-Clause](https://opensource.org/license/bsd-2-clause)]

**Compatible**, on condition that the notices are reproduced, **in the app** (for binary distribution) as well as in the repo. LIC-1 covers the data licences but **not the code dependencies**; see §7.2.

**What I could not check:** the full transitive tree. The `haunts` repository is private and has, as far as the governance record shows, no lockfile yet, and I was told not to touch GitHub. The typical React Native / Expo tree is overwhelmingly MIT, BSD, ISC and Apache-2.0 [K, medium-high confidence], all of which are permissive and compatible on the same notice-preserving basis.

**The one real incompatibility to guard against is copyleft.** GPLv3 §10: *"You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License."* [E, [SPDX, GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html)] A GPL component compiled into the app would require the combined work to be offered on GPL terms, which a noncommercial restriction contradicts [I]. (It would also be a problem on the App Store [K].) `map-options-comparison.md` already notes OsmAnd is GPLv3 and excluded. **Recommendation: a licence allow-list in CI** (MIT, BSD-2/3, ISC, Apache-2.0, 0BSD, CC0, Unlicense; MPL-2.0 by review; GPL/LGPL/AGPL/SSPL blocked), owned by the **CSO** under its dependency-hygiene mandate. [J]

**Fonts:** the MapLibre style must bundle its glyphs locally (`map-tiles-note.md` §5.5). Whatever font is chosen carries its own licence (commonly SIL OFL for open fonts [K]) and joins the third-party notices. **Not yet chosen; flagged.**

---

## 5. Is a non-commercial licence "open source"? And what `LICENSE.md` then requires

### 5.1 No, on three independent sources

1. **The Open Source Definition**, criterion 6, *"No Discrimination Against Fields of Endeavor"*: *"The license must not restrict anyone from making use of the program in a specific field of endeavor. For example, it may not restrict the program from being used in a business, or from being used for genetic research."* [E, [OSI, The Open Source Definition](https://opensource.org/osd), v1.9, last modified 2007-03-22] Criterion 1 (Free Redistribution) also requires that the licence *"shall not restrict any party from selling or giving away the software"*. [E, same]
2. **The PolyForm Project itself:** *"PolyForm is not… Open source or free software."* [E, [polyformproject.org/about](https://polyformproject.org/about)]
3. **SPDX** records `PolyForm-Noncommercial-1.0.0` with `isOsiApproved: false`. [E, [SPDX](https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.html), page metadata]

These have separate origins (OSI, PolyForm, the Linux Foundation's SPDX project), so this is **not** single-sourced. **D28's [K] tag on this point can now be upgraded to [E].**

The accurate term for PolyForm-licensed code is **"source-available"**. [J, on terminology; it is common usage but I did not retrieve a definition]

### 5.2 Consequences for `LICENSE.md`

`LICENSE.md` presumes open source *"unless the decision record gives a written reason otherwise"*. **So before the `haunts` repository is made public under PolyForm, the decision record must carry: (a) the licence named precisely, and (b) the CEO's written reason for departing from the presumption.** Neither is there yet.

It follows, under Article 4 (*"claims we cannot substantiate are claims we do not make"*) and Article 1.3, that **no Candour material (store listing, website, README, social posts) may call Haunts' code "open source" while it is under PolyForm.** "Source-available" or "the source is public" is accurate. I recommend this become a QA-checkable acceptance criterion alongside the D21 word search (§7.6). [J on the mechanism; the obligation is Article 4]

### 5.3 Neutral wording for the decision record, with the reason left to the CEO

I have not supplied a reason. The factual parts below are verifiable; the bracketed part is his.

> **D[nn] — The `haunts` code licence: PolyForm Noncommercial License 1.0.0.** *CEO, [date].* Candour's own code in `deopea-david/haunts` is licensed under the **PolyForm Noncommercial License 1.0.0** (SPDX `PolyForm-Noncommercial-1.0.0`) when the repository is made public. Third-party code, data and assets in the repository keep their own licences, listed in `THIRD_PARTY_NOTICES`.
>
> **This is not an open-source licence.** It forbids commercial use by anyone other than Candour, which the Open Source Definition does not allow (criterion 6), and its authors say it is not open source. `LICENSE.md` presumes open source for product code unless this record gives a written reason. **The CEO's reason:** *[in his own words]*.
>
> **What this permits:** anyone may read, build, run, study, modify and share the code for noncommercial purposes, including charities, schools and public bodies. **What it forbids:** commercial use by anyone but Candour. **What it means for customers when Haunts ends:** *[the Article 7.2 commitment, as decided under Decision 3]*.

---

## 6. Article 7.2 at discontinuation

### 6.1 Does a non-commercial licence satisfy "open-sourced"? On my reading, no

Article 7.2: *"The product's code is **open-sourced** where third-party rights allow; where they don't, that is stated publicly with the reason."*

The Constitution does not define the word (§1). **Its ordinary meaning, in software, is the Open Source Definition's**, and on that meaning a PolyForm-licensed codebase has been published but not open-sourced (§5.1). Three further pointers inside our own documents read the same way [I]:
- `LICENSE.md` sets "open source" against a licence given *"a written reason otherwise"*. That contrast makes no sense unless some licences are not open source.
- Article 8 speaks of *"Open-source and self-hostable design"* as something to encourage, which again treats "open source" as a category with edges.
- The gate record says the CGO found *"Article 7.2's open-sourcing promise is deliverable in full"* on the offline architecture. That finding was made about third-party rights, and it assumed Candour would actually open-source the code.

**The standing of this reading.** It is an interpretation of a constitutional term, and `pipeline/evidence-standard.md` records that agent interpretation of Article 4 failed four times in September 2026 and the founder caught it. **So I give it as [J], with its reasons shown, and the CEO should settle it, not a second agent pass.** What makes the call easy is the asymmetry: honouring the strong reading costs one relicensing act at the end of the product's life, while the weak reading opens a loophole (§6.5).

**Are there third-party rights that would stop open-sourcing?** On what I have seen: **no.** MIT, BSD-2 and Apache-2.0 code, and CDLA, Apache and OGL data, all permit redistribution under open terms with notices [E, §4]. So 7.2's "where they don't" carve-out is not available as an excuse for Haunts. [I] The unknowns that could change this are a future non-permissive dependency (§4.5), and code whose ownership Candour cannot show (§7.3, §8).

### 6.2 A written disagreement with D28's framing

D28 says: *"A non-commercial licence during the product's life does not conflict with that, but whether it satisfies it at shutdown is not settled. If it does not, the code is relicensed at discontinuation."*

**I agree with the first sentence and disagree with the second, on two grounds.**

1. **"Not settled" understates it.** On the ordinary meaning, and on the three pointers above, a PolyForm codebase is not "open-sourced". Leaving the question open lets a future shutdown answer it in the direction that is cheapest at the time, and that is the situation Article 7's preamble exists to prevent: *"the rules for endings are fixed here, in advance, while no ending is on the table."*
2. **"The code is relicensed at discontinuation" needs someone to do it, and Article 7.3 is the case where nobody is there.** If the founder walks away, 7.3 says every product is treated under 7.2, but a relicensing act that requires the copyright holder to act will not happen if the copyright holder has gone. The Constitution is candid that it *"currently binds through publicity, not law"* (Article 10). **A promise that the one person able to keep it must actively perform, in the one scenario where he is absent, is weaker than it looks.**

**Customer copy depends on this.** PRICE S3 already tells buyers *"we open-source what we can"*. Under Article 4 that is only honest if the commitment behind it is firm (§1).

### 6.3 What Candour should commit to now

**Three options, which stack:**

| Option | What it is | Survives the founder's absence (7.3)? | Survives a sale (7.1)? | Cost |
|---|---|---|---|---|
| **A. Product commitment** in the decision record | *"On discontinuation of Haunts, or under Article 7.3, Candour's code in `haunts` is relicensed under [Apache-2.0 / MIT], an OSI-approved licence."* | **No.** It needs the copyright holder to act | Only through 7.1.1's 3-year adoption of the Constitution, and only if the commitment is in the Constitution rather than in a product record [I] | £0 |
| **B. A self-executing grant in the licence itself** | A **PolyForm Countdown** grant, or equivalent, on each release: that release **automatically** becomes available under an OSI licence on a stated future date | **Yes.** PolyForm: *"Legally, this is a present grant of a license on the date of release, not a contract promise to grant the license later"*; *"No contributor can revoke the new license before it starts."* [E, [PolyForm Countdown 1.0.0](https://polyformproject.org/licenses/countdown/1.0.0)] | **Yes**, since the grant has already been made [I] | £0 in text; **erodes the noncommercial restriction for old releases** after the chosen period |
| **C. Constitutional clarification** | Amend 7.2 so "open-sourced" means *"licensed under a licence approved by the Open Source Initiative"*, company-wide | No, on its own | **Yes** for the 7.1.1 term, because the buyer adopts the Constitution | £0 plus an Article 11 change-log entry |

**My recommendation: A now, and B for each release, with the period chosen by the CEO. C is optional.** [J]

- **A** is the minimum. It closes the "not settled" question and makes PRICE S3 substantiable.
- **B** is the only option that works when nobody is left to act. It is modelled on a known instrument: BSL's Change Date does the same, *"Effective on the Change Date… the Licensor hereby grants you rights under the terms of the Change License"* [E, [BSL 1.1](https://mariadb.com/bsl11/)], and PolyForm publishes Countdown for exactly this job. **The price is that each release eventually becomes commercially usable by anyone.** A long period protects the CEO's intent during the product's life and still guarantees the ending [J]. The period is the CEO's to set; it is not a number a seat should pick for him. **B involves drafting choices (trigger, period, target licence, how it sits beside PolyForm), so I recommend it goes to the L1 legal review before first publication** (§8).
- **C** is worth doing because it closes the loophole for every future product, not only Haunts. It is not needed to make Haunts compliant.

**Which OSI licence at the end?** **Apache-2.0** is my preference [J]: it carries an express patent grant (as PolyForm does, so nothing is lost at the switch), and its NOTICE mechanism matches the one the Foursquare data already uses. **MIT** is simpler and matches the React Native ecosystem. Both are OSI-approved [E, [OSI, Apache-2.0](https://opensource.org/license/apache-2.0); [OSI, MIT](https://opensource.org/license/mit)]. Either satisfies 7.2.

**A precondition for every option:** Candour must hold the rights to relicense **all** the code in the repository. That rules out accepting outside contributions on default terms (§7.3).

### 6.4 Is the commitment a strengthening under Article 11?

- **Option A is not an amendment.** It is a product commitment recorded in a decision record, like D4 or D22. Article 11 does not engage. [I]
- **Option B is not an amendment** either. It is a licence term. [I]
- **Option C is an amendment and must go through Article 11.1**: *"Any change to this document is recorded in a public change log with date, diff, and rationale."* Is it a strengthening? **If the ordinary reading (§6.1) is right, C changes nothing in substance and is a clarification. If a looser reading were right, C narrows Candour's discretion at a customer-facing ending and is a strengthening.** **On neither reading is it a weakening**, so the Article 11.2 "WEAKENING" label does not apply, and Article 7's closing line permits it: *"These conditions may be strengthened by amendment at any time"*. [I] **Article 11.3's freeze** (*"No amendment to Article 7… from the moment any written expression of interest in a sale… exists"*) would block C if any sale interest existed. **I found none in the repository**, but I searched only the files named in this note and the decision record, and the founder is the only person who can say whether any such written expression exists (Article 10 names this reliance). [I, with that limit]

### 6.5 An Article 9 gaming vector, which Article 9 says we add rather than use

**The vector:** *publish a product's code under a source-available licence that forbids commercial use, and at discontinuation call that "open-sourced", so 7.2 is met in name while no one can in practice take over, fork or commercially maintain the product for its stranded customers.*

Article 9: *"If a reader finds a gaming vector not listed here, we commit to adding it rather than using it."* I am a reader, and I have found one. **Draft row for the CEO to accept or rewrite:**

| Loophole | The number that exposes it |
|---|---|
| Reading "open-sourced" (7.2) to include a source-available licence that restricts commercial use, so a discontinued product's code cannot in practice be maintained by anyone else | Each product's decision record names its code licence by SPDX identifier and states whether it is OSI-approved; the closing cost sheet (7.2) names the licence the code was released under at discontinuation |

Adding a row to Article 9 is an amendment under Article 11.1 (change log, date, diff, rationale). It is not a weakening. [I]

---

## 7. Practical items for the repository

### 7.1 The `LICENSE` file, and the scope statement

1. **`LICENSE`** at the repo root: the **verbatim, unmodified** PolyForm Noncommercial 1.0.0 text, including its URL line. Nothing else in the file, so that tooling and readers recognise it. [J]
2. **A `Required Notice:` line** at the end of `LICENSE`, which the licence obliges every redistributor to pass on (*"copies of any plain-text lines beginning with `Required Notice:` that the licensor provided"* [E, §2.2]). Suggested: `Required Notice: Copyright (c) 2026 David Parrish, trading as Candour.` **The licensor is the founder personally, not "Candour"**, because the Constitution states *"The company is currently a brand operated by its founder, not a registered legal entity"* (Preamble) [E]. An unincorporated brand cannot hold copyright or grant a licence [K, high confidence]. **At incorporation, the copyright should be assigned to the company in writing** [K; for L1].
3. **A "Licence" section in `README.md`** saying, in plain words: this is **source-available, not open source**; PolyForm Noncommercial applies to **code written by Candour**; listed paths (vendored code, `data/`, fonts, any tile samples) are **third-party and under their own licences**, see `THIRD_PARTY_NOTICES`; and the **Article 7.2 commitment** as decided (Decision 3). [J]
4. **SPDX headers** in Candour's source files (`// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0`) so the scope is visible file by file and third-party files are distinguishable at a glance. Cheap and optional. [J]
5. **If Option B is taken:** a per-release Countdown grant file shipped with each tagged release, with its start date. Drafting to go through L1 first (§8).

### 7.2 NOTICE and third-party notices

1. **`THIRD_PARTY_NOTICES`** (or `NOTICE`) in the repo root, listing every third-party component with its licence and the copyright notices its licence requires. **Generate it from the lockfile** rather than writing it by hand, and regenerate on every dependency change, because MIT and BSD notices must accompany *"all copies or substantial portions"* and binary redistributions [E, §4.5]. [J on the method]
2. **Data directories carry their own licence files:** the CDLA-Permissive-2.0 text, the Apache-2.0 text, the **unaltered** Foursquare NOTICE.txt and Candour's modification notice beside any committed venue-index artefact; the OGL link and the OS attribution statement beside any committed Zoomstack-derived material. [E for the obligations, §4.2–4.4]
3. **A gap in the requirements, for the PM/BA.** LIC-1 puts the **data** licences on the in-app "Data sources and licences" screen but says nothing about the **code dependencies**. MIT requires the notice in *"all copies or substantial portions of the Software"*, and BSD-2 requires binary redistributions to reproduce the notice *"in the documentation and/or other materials provided with the distribution"* [E, §4.5]. An app binary is a binary redistribution. **Proposed LIC-7:** *"The licences screen also lists every third-party code dependency shipped in the binary, with its licence text and copyright notice, generated from the lockfile at build time; QA asserts the list matches the shipped lockfile."* [I for the obligation; J for the wording] The export README (LIC-2) does not need these, because the export contains data, not code [I].

### 7.3 Contributions: why the default does not work, and what to do

**GitHub's default is inbound = outbound.** GitHub Terms §D.6: *"Whenever you add Content to a repository containing notice of a license, you license that Content under the same terms… If you have a separate agreement to license that Content under different terms, such as a contributor license agreement, that agreement will supersede."* [E, [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)]

**Under PolyForm, that means a contributor's code reaches Candour under PolyForm Noncommercial, and Candour's own use of it is then limited to noncommercial purposes.** Selling the app with that code in it is commercial use. **Candour could not ship an outside contribution in the paid app, and could not relicense it at discontinuation (§6.3).** [I, from §D.6 and the PolyForm grant]

**A DCO does not fix this.** DCO 1.1 has the contributor certify that *"I have the right to submit it under the open source license indicated in the file"* [E, [developercertificate.org](https://developercertificate.org/)]. It is a certification of provenance, not a grant of extra rights, and it assumes an **open-source** licence, which PolyForm is not. [I]

**Options:**

| Option | Effect | Cost | Honesty point |
|---|---|---|---|
| **(i) Accept no outside code at v1** *(recommended)* | Bug reports, security reports, discussion and ideas welcome; **pull requests not accepted**. Stated in `CONTRIBUTING.md`, and pull requests turned off if the repo settings allow it | £0 | Plain and symmetric: nobody gives Candour rights Candour does not give them |
| **(ii) A CLA** | Each contributor grants Candour a broad licence (including commercial use and relicensing, so that the app can include the code and 7.2 can be honoured) | **Needs a lawyer to draft or adapt it** (a CLA is a contract); admin per contributor | **Asymmetric**: the contributor gives Candour the commercial rights the licence denies the contributor. Articles 1.2 and 1.3 require saying that plainly on the CONTRIBUTING page, not in the CLA's small print [J] |
| (iii) Copyright assignment | As (ii), stronger | As (ii), and more off-putting | As (ii) |

The Apache Software Foundation publishes an Individual CLA as a model [E, the page exists: [apache.org/licenses/contributor-agreements](https://www.apache.org/licenses/contributor-agreements.html); **I did not retrieve or read the ICLA's grant text**, so I make no claim about its terms].

**Recommendation: (i) now; revisit only if outside contributors actually appear.** It is cheapest, most honest, and keeps the 7.2 relicensing within the founder's sole power. **This is Decision 4.** [J]

**Agent-written code is not an "outside contribution", but it has its own chain-of-title question**, covered in §8.

### 7.4 AI-written code and who owns it

Much of Haunts will be written by Candour's agent seats. Two retrieved facts and one open question:

- **Anthropic's terms assign outputs to the user, "if any".** Consumer Terms: *"Subject to your compliance with our Terms, we assign to you all our right, title, and interest (if any) in Outputs."* [E, [Anthropic Consumer Terms](https://www.anthropic.com/legal/consumer-terms), effective 8 October 2025 as displayed]. The Commercial Terms say the Customer *"owns its Outputs"* and assign Anthropic's *"right, title and interest (if any)"* [E, [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms), effective 17 June 2025 as displayed]. **Which set governs Candour's use depends on the account the founder uses; I do not know which** [flag].
- **UK law has a specific rule for computer-generated works.** CDPA 1988 s.9(3): *"In the case of a literary, dramatic, musical or artistic work which is computer-generated, the author shall be taken to be the person by whom the arrangements necessary for the creation of the work are undertaken."* s.178: *"'computer-generated', in relation to a work, means that the work is generated by computer in circumstances such that there is no human author of the work"*. [E, [legislation.gov.uk s.9](https://www.legislation.gov.uk/ukpga/1988/48/section/9); [s.178](https://www.legislation.gov.uk/ukpga/1988/48/section/178)]
- **Open question:** whether agent-written code directed and reviewed by the founder has him as human author, or is "computer-generated" with him as the s.9(3) author, or (for some fragments) lacks the originality for copyright to subsist at all. **On either of the first two readings the rights appear to sit with the founder** [I], which is what the licence and the store EULAs need. The third reading does not void the licence; it means some parts may be freely copyable whatever the licence says, so **the noncommercial restriction may be weaker in practice than it reads** [I]. **I cannot resolve this and it is a question for a qualified lawyer (§8).** [J]

A hygiene rule follows, for the CTO and CSO: **no code copied from the web into `haunts` without its source and licence recorded.** An agent pasting a Stack Overflow answer imports that answer's licence [K: Stack Overflow content is CC BY-SA; not retrieved], and CC BY-SA content cannot be relicensed under PolyForm. [I]

### 7.5 App Store and Play Store: the store terms and the repo licence sit side by side

**Apple's Standard EULA** [E, [apple.com/legal/…/stdeula](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)]:
- *"Apps made available through the App Store are licensed, not sold, to you."*
- Scope: *"Licensor grants to you a nontransferable license to use the Licensed Application on any Apple-branded products that you own or control and as permitted by the Usage Rules."*
- Restriction: *"You may not copy…, reverse-engineer, disassemble, attempt to derive the source code of, modify, or create derivative works of the Licensed Application… (except as and only to the extent that any foregoing restriction is prohibited by applicable law or to the extent as may be permitted by the licensing terms governing use of any open-sourced components included with the Licensed Application)."*
- For a Third Party App, the licence *"is granted by the Application Provider of that Third Party App"*, i.e. by Candour (the founder).

**Google Play Terms of Service** [E, [play.google.com/about/play-terms](https://play.google.com/about/play-terms/index.html)]:
- *"you will have the non-exclusive right… to store, access, view, use, and display copies of the applicable Content on your Devices or as otherwise authorized for your personal, non-commercial use only… Your use of apps and games may be governed by the additional terms and conditions of the end user license agreement between you and the Provider."*

**How they fit together** [I throughout]:
1. **Two routes, two licences, one licensor.** A buyer gets the **binary** under the store's terms. Anyone gets the **source** under PolyForm. The same copyright holder can license the same work on different terms to different people, and PolyForm expressly preserves that (*"or prevent the licensor from granting licenses to anyone else"*). Nothing in either store's terms requires the source to be closed.
2. **No conflict with Apple's anti-reverse-engineering clause.** A buyer who wants the source does not need to decompile the binary; they can take it from the repository under PolyForm, a separate grant. Apple's clause restricts what the buyer may do *to the Licensed Application*, not what Candour may publish.
3. **The asymmetry to know about.** Apple's Standard EULA contains **no noncommercial restriction** on using the app. Google Play's default terms say **"personal, non-commercial use only"**. So on Android, a freelancer using Haunts for work mileage is arguably outside Play's default licence unless Candour offers its own EULA saying otherwise. **Minor, but it belongs in L1**, together with whether Candour needs its own customer terms at all (§8).
4. **One Apple EULA clause sits awkwardly with the product's promise.** Standard EULA clause (b), *"Consent to Use of Data"*, says the licensor *"may collect and use technical data"*. It is a permission, not an obligation, so there is no breach in Haunts collecting nothing. But a customer reading it beside "nothing leaves the device" could reasonably be confused. **Flag for L1 and UX:** whether a short Custom EULA is worth its cost. I do not recommend one on this ground alone. [J]
5. **The repo licence must not be presented as the app's terms.** The store listing, and the licences screen, should say the app is licensed under the store's terms, and that the source is available separately under PolyForm Noncommercial. [J]

### 7.6 Before the repository is made public: a checklist

| # | Item | Owner | Source of the duty |
|---|---|---|---|
| 1 | Decision-record entry naming the licence (SPDX ID and version) | CEO | `LICENSE.md` limb (b) |
| 2 | The CEO's written reason for not using an open-source licence | CEO | `LICENSE.md` limb (c) |
| 3 | The Article 7.2 commitment decided (Option A at minimum) | CEO | Article 7.2; PRICE S3 under Article 4 |
| 4 | `LICENSE` (verbatim) + `Required Notice:` line naming the founder | CGO drafts, CEO approves | PolyForm Notices clause |
| 5 | `THIRD_PARTY_NOTICES` generated from the lockfile; data licence files in place | Engineer; CGO checks | MIT, BSD-2, Apache §4, CDLA §2.1, OGL |
| 6 | `CONTRIBUTING.md` stating the contribution policy | CGO drafts, CEO approves | §7.3 |
| 7 | CI licence allow-list, copyleft blocked | CSO | §4.5 |
| 8 | **Full git history scanned for secrets and anything not meant to be public**, because the whole history becomes visible, and **making the repo private again does not recall it**: *"When you change the visibility of a repository to private, existing forks or local copies created by other users will still exist."* [E, [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)] | CSO | D28's own reasoning |
| 9 | CSO review of security code | CSO | D28's own reasoning |
| 10 | PLAT-6's three name checks passed, since the repo is named `haunts` | CGO (trademark), CEO | D27, D28, PLAT-6 |
| 11 | **No material calls the code "open source"** while it is under PolyForm | QA, as a word search alongside D21's | Article 4 honest marketing; §5.2 |
| 12 | OS attribution string confirmed by direct read, punctuation included | CTO or Skeptic | LIC-6; §4.4 |

---

## 8. What needs qualified human review (Constitution 6.1)

**What the clause says:** *"Before launch, anything involving personal data at scale, payments, health information, regulated domains, or **third-party licence terms whose interpretation determines a product's architecture or cost**, receives review by qualified human professionals."*

**What it requires here, read strictly** [I]:
- The **outbound** licence is Candour's own term, not a *third-party* licence term. The clause does not, on its words, reach it.
- The **inbound** terms (CDLA, Apache/Foursquare, OGL, MIT/BSD) are third-party terms. But their interpretation no longer determines Haunts' architecture or cost: they all permit what Haunts does with notices, and the notices are a static screen (`compliance-note.md` §2.4: *"Cost impact: none worth modelling"*). So I do not find this limb triggered by anything in this note.
- The clause bites *"before launch"*. The repo may go public before or after launch.

**So I do not claim 6.1 mandates a review of the licence choice.** A seat's recommendation is not an article (`pipeline/evidence-standard.md`), and I am not going to dress one as the other.

**What I recommend anyway, as this seat's judgment [J], and why it is cheap:** **L1**, a qualified human legal review, is **already a launch bar** (Condition 9.6; `requirements.md` §0). Adding these questions to its brief costs a marginal amount, not a second engagement:

1. **The licence set as a whole:** PolyForm Noncommercial for code, the store terms for the binary, and the third-party notices, checked together for gaps.
2. **Any self-executing relicensing grant (Option B)** before the first public release carries one: the trigger or date, the target licence, and how it sits beside PolyForm.
3. **A CLA**, only if Decision 4 goes that way.
4. **Chain of title:** who owns agent-written code under CDPA s.9(3) and the Anthropic terms that actually apply, and what to do at incorporation (§7.4).
5. **Customer terms on the stores:** whether Candour needs its own EULA on Google Play (the "non-commercial use only" default) and whether Apple's Standard EULA sits well with Haunts' privacy promise (§7.5).
6. **The charity reading** of PolyForm's Noncommercial Organizations clause (§3.3), if the CEO wants certainty before accepting it.

**What would make 6.1 mandatory rather than advisable:** a dependency or dataset whose licence terms began to decide a feature or a cost, for example a GPL component needed for a core function (§4.5), or a map or font source with restrictive terms. **L1's cost is not yet on the cost sheet; flagged to the CFO**, as the other L1 items already are.

---

## 9. Decisions for the CEO, one at a time

Each depends on the one before, so they are in order. None is urgent until the repository is about to go public.

1. **Which licence text?** **PolyForm Noncommercial 1.0.0** (recommended: personal use, modification and free noncommercial sharing) **or PolyForm Strict 1.0.0** (personal use only; no sharing, no changes). The difference is the free-build row in §3.3.
2. **The written reason**, in your own words, for not using an open-source licence (`LICENSE.md`). Scaffold at §5.3.
3. **The Article 7.2 commitment.** Recommended: **commit now** to relicensing under **Apache-2.0** (or MIT) on discontinuation or under 7.3 (Option A), **and** make each release convert automatically after a period you choose (Option B), subject to L1. Option C, a constitutional clarification, is optional.
4. **Outside code contributions:** **none at v1** (recommended) or a lawyer-drafted CLA.
5. **The Article 9 row** (§6.5), which Article 9 says Candour adds when a reader finds an unlisted vector. It is an Article 11 amendment, and not a weakening.

**No block.** This is not a gate, and I hold no power over repository visibility. If the repository were made public before items 1–2 are recorded, that would depart from `LICENSE.md`, and I would flag it to the CEO. The decision stays his.

**Hand-offs to other seats, recorded here so they are not lost:**
- **PM/BA:** proposed **LIC-7** (code-dependency notices in the app, §7.2) and **LIC-8** (no "open source" claims while under PolyForm, §5.2). LIC-6's attribution string can now be written against the OS primary form (§4.4).
- **CSO:** CI licence allow-list (§4.5); history secret scan before the flip (§7.6 item 8).
- **CTO / Skeptic:** confirm the OS attribution string's exact punctuation on a direct read (§4.4); re-retrieve MapLibre Native's licence (I relied on the CTO's retrieval).
- **CFO:** L1's scope grows slightly (§8); still unpriced.

---

## 10. Negative findings: where I looked, and what would overturn them

| Finding | Where I looked | What would overturn it |
|---|---|---|
| PolyForm Noncommercial is not open source | OSI OSD (criteria 1 and 6); PolyForm "About"; SPDX metadata | OSI approving it, which its own authors disclaim; or the CEO adopting, in writing, a meaning of "open source" for Candour that departs from the industry's |
| A PolyForm codebase does not satisfy Article 7.2's "open-sourced" | Constitution Definitions (term absent), 7.2, 7.3, Article 8, `LICENSE.md`, gate record, PRICE S3 | The CEO settling the meaning of the word the other way, in writing; that is his call, not a second agent's (§6.1) |
| CC BY-NC-SA is unsuitable for software | CC FAQ; CC NonCommercial interpretation page | Creative Commons withdrawing its advice |
| PolyForm Small Business does not deliver D28 | Its text (Small Business clause) | The CEO clarifying that his intent is "no large-company use" rather than "no commercial use" |
| DCO and GitHub's default do not give Candour commercial rights in contributions | DCO 1.1 text; GitHub Terms §D.6; PolyForm grant | A contributor agreement granting more; or Candour choosing not to sell code containing contributions |
| A GPL-family dependency would conflict | GPLv3 §10 via SPDX | None needed; it is a guard, not a finding about the current tree |
| The transitive dependency tree is compatible | **Could not look**: repo private, no lockfile in the record, and GitHub off-limits for this commission | A licence scan of the real lockfile, which item 7 of §7.6 provides |
| No sale interest exists (relevant to 11.3 and Option C) | This repository's governance files only | Any written expression of interest in a sale, which only the founder can confirm |

---

## 11. Evidence register

All retrieved **2026-09-26** unless stated.

**Licences and definitions**
- [PolyForm Noncommercial 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0) — full text read. (The same path with a trailing slash returned 404; the canonical URL above returned the text.)
- [SPDX — PolyForm-Noncommercial-1.0.0](https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.html) — text; `isOsiApproved: false`; released 9 July 2019
- [PolyForm Strict 1.0.0](https://polyformproject.org/licenses/strict/1.0.0) — full text read
- [PolyForm Small Business 1.0.0](https://polyformproject.org/licenses/small-business/1.0.0) — full text read
- [PolyForm Countdown 1.0.0](https://polyformproject.org/licenses/countdown/1.0.0) — full text read
- [PolyForm — Licenses](https://polyformproject.org/licenses) and [About](https://polyformproject.org/about) — suite summary; *"not… open source"*
- [OSI — The Open Source Definition](https://opensource.org/osd) — v1.9, criteria 1–10 read
- [OSI — Apache-2.0](https://opensource.org/license/apache-2.0), [MIT](https://opensource.org/license/mit), [BSD-2-Clause](https://opensource.org/license/bsd-2-clause)
- [CC BY-NC-SA 4.0 legal code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en) — NonCommercial definition
- [Creative Commons FAQ](https://creativecommons.org/faq/) — "Can I apply a Creative Commons license to software?"
- [CC wiki — NonCommercial interpretation](https://wiki.creativecommons.org/wiki/NonCommercial_interpretation) — oldid 116467
- [Business Source License 1.1](https://mariadb.com/bsl11/) — grant and Change Date clauses
- [SPDX — GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html) — §10 (gnu.org refused the automated request with 403)
- [Developer Certificate of Origin 1.1](https://developercertificate.org/) — full text

**Inbound terms**
- [Apache License 2.0 (text)](https://www.apache.org/licenses/LICENSE-2.0.txt) — §1 Derivative Works; §4 closing paragraph
- [Foursquare OS Places Notice](https://opensource.foursquare.com/places-notice-txt/) — full notice
- [CDLA-Permissive-2.0](https://cdla.dev/permissive-2-0/) — §2.1, §3.1, §5.4
- [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) — grant, conditions, exemptions
- [Ordnance Survey — Copyright acknowledgments](https://www.ordnancesurvey.co.uk/customers/public-sector/public-sector-licensing/copyright-acknowledgments) — attribution statement, **read through a summarising fetch; single source (the provider's own page)**
- [Ordnance Survey — OS Open Zoomstack](https://www.ordnancesurvey.co.uk/products/os-open-zoomstack) — product page (states no licence or attribution itself)
- npm registry, `license` field for `react-native`, `react`, `expo`, `expo-modules-core`, `expo-location`, `expo-sqlite`, `expo-crypto`, `@maplibre/maplibre-react-native` (`https://registry.npmjs.org/<name>/latest`)

**Platforms and ownership**
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) — §D.5, §D.6; effective 2026-04-27
- [GitHub Docs — Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [Apple — Licensed Application EULA (Standard EULA)](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)
- [Google Play Terms of Service](https://play.google.com/about/play-terms/index.html) — "License to Use Content"
- [Apache — Contributor agreements](https://www.apache.org/licenses/contributor-agreements.html) — page only; ICLA text **not** read
- [Anthropic Consumer Terms](https://www.anthropic.com/legal/consumer-terms) and [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) — outputs clauses
- [CDPA 1988 s.9](https://www.legislation.gov.uk/ukpga/1988/48/section/9) and [s.178](https://www.legislation.gov.uk/ukpga/1988/48/section/178)

**Relied on from other seats, not re-retrieved by me:** MapLibre Native BSD-2-Clause (`map-options-comparison.md`, CTO); Overture theme licences (`compliance-note.md` §2.5, my own earlier note).

**Internal, read from disk:** `constitution.md` v1.3 (Preamble, Definitions, Articles 1, 3, 4, 6.1, 7, 8, 9, 10, 11); `LICENSE.md`; `decisions/2026-09-16-haunt-gate.md` (gate record, Conditions, D4, D22, D27, D28); `products/haunt/requirements.md` §0, §10.1, §13, §16; `products/haunt/compliance-note.md` §2; `products/haunt/android-and-stack-note.md`; `products/haunt/map-options-comparison.md`; `roles/cgo.md`; `pipeline/evidence-standard.md`.

---

## Change log

- **2026-09-26** — First version (CGO), on the D28 referral.

