# Green Key Global: Eco-Rating Certification Website Spec

This file is the single source of truth for building a marketing and education website from the Green Key Global sales kit. It contains the complete content, data, brand system, and build guidance. Everything a coding agent needs is in this file. Do not invent statistics, pricing, or claims beyond what is written here.

**Working title:** A Hotel's Roadmap to Eco-Rating Certification

**Primary audience:** Hotel owners and capital allocators. Ownership groups, asset managers, CRE investors, private equity, and lenders. General managers and management companies execute certification but do not approve capital, so the primary argument is written for the person who signs the checks.

**Secondary audience:** The general manager and department heads who run the certification process after the owner approves. Served by the Readiness Hub.

**Goal:** Make the case for Green Key Eco-Rating certification and convert visitors to (a) a contact or demo request, (b) an ROI calculation, or (c) a pilot conversation.

---

## 1. How to Use This File (instructions for Claude Code)

1. Build a static, fast, accessible multi-page site (Astro, Next.js static export, or plain HTML, CSS, and JS all acceptable; prefer whatever produces the smallest, fastest output).
2. Use the content blocks in Section 5 verbatim or lightly adapted. Use the data registry in Section 6 for every number.
3. Follow the brand system in Section 3 exactly.
4. Every statistic rendered on any page must display its source, either inline in small text or as a footnote at the bottom of the section. Sources are listed with each statistic in Section 6.1.
5. Respect the hard writing rules in Section 3.4. Notably: no em dashes anywhere, and no Eco-Rating point values anywhere (see Section 6.4).
6. Build the interactive ROI calculator per the formulas in Section 5.8. All math is defined there. Do not change the formulas or defaults.
7. Include a "last updated July 2026" note in the footer and a disclaimer that pricing and program details should be confirmed at greenkeyglobal.com.
8. While the site is pending internal review, every page must carry `<meta name="robots" content="noindex, nofollow">` and robots.txt must disallow all crawling.

---

## 2. Positioning Summary

- Tagline (use as the site subtitle): **"The Leading North American Standard in Sustainable Hospitality Certification"**
- Voice: Green Key Global speaking in first person plural ("we certify operations, not construction").
- Core narrative for the owner audience: the capital an owner is already committing to lighting, fixtures, and building systems can earn twice, once in operating savings and once in a verified credential that corporate buyers, booking platforms, lenders, and regulators all accept. Certification is a sequencing layer on an existing capital plan, not a new line item.
- Supporting narrative: every hotel is being asked to prove, credibly, how it operates. Certification is that proof. It was built by hoteliers for hoteliers, requires no capital spend to achieve, is independently audited, is priced for every market tier, and tracks measurably with corporate business.
- Political neutrality: the case is framed on business outcomes (revenue, cost, operations, risk, asset value), never ideology. A property can lead with the environmental story or the cost-discipline story. Both describe the same certification honestly.

---

## 3. Brand System

### 3.1 Colors

| Token | Hex | Use |
|---|---|---|
| `--gk-deep` | `#196B24` | Primary green: buttons, heading accents, solid blocks, chart primary |
| `--gk-bright` | `#92D050` | Accent green: numerals, highlights, hover states |
| `--gk-band` | `#8CC642` | Footer band and section dividers |
| `--gk-dark` | `#14402A` | Dark surfaces, hero backgrounds, deepest chart shade |
| `--gk-pantone356` | `#007A33` | Alternate brand green (links, secondary accents) |
| `--gk-pale` | `#F2F8EC` | Card and section tint backgrounds |
| `--gk-ink` | `#1A1A1A` | Headings text |
| `--gk-body` | `#222222` | Body text |
| `--gk-grey` | `#595959` | Captions, source lines |

### 3.2 Typography

- Headings: **Montserrat** (bold; section titles may be all caps per the deck style)
- Body: **Helvetica, Arial, sans-serif**
- Footer wordmark line: Montserrat Light, letter-spaced: `GREENKEYGLOBAL.COM`
- Load Montserrat from Google Fonts. Helvetica falls back to Arial.

### 3.3 Visual motifs

- White backgrounds. Pale green (`--gk-pale`) rounded cards (radius approximately 12px) for feature grids.
- A light-green full-width footer band (`--gk-band`) with `GREENKEYGLOBAL.COM` right-aligned in white.
- Big stat callouts: large Montserrat bold number in `--gk-deep` over a small caption.
- Keys ladder: five ascending blocks shaded light to dark green. **Label rungs by Key level only. Never label with score ranges or point totals.**
- Charts: flat bars, no gridlines, value labels on bars, source line beneath.
- Owner-track pages and Readiness Hub pages should be visually distinguishable. Suggested approach: owner pages use the dark hero treatment, hub pages use a lighter, more utilitarian header.

### 3.4 Hard writing rules

- **No em dashes or en dashes anywhere.** Use commas, colons, parentheses, or "to" in ranges.
- **No Eco-Rating point values anywhere.** See Section 6.4 for the full confidentiality rule.
- Third-party facts always carry their named source (see 6.1). Program facts may be labeled "Green Key Global program data, July 2026."
- Never state or imply a specific partnership discount percentage. Say "portfolio agreements improve on list pricing."
- Do not reproduce content from other organizations beyond the short attributed statistics listed here.
- Any rating from 1 to 5 Keys is described as "full certification."
- Plain business English. Lead with operational and financial impact. Short scannable sections with bolded lead-ins.

---

## 4. Site Architecture

```
/                            Home (the owner case at a glance)
/why-certify                 The Business Case (demand, operating cost, asset value, risk)
/capital-map                 The Capital Map (where to deploy capital, and in what order)
/stewardship                 Stewardship (operating discipline, people, place, resilience)
/pricing                     Published pricing and ROI calculator
/partners                    For brands and management companies
/about                       Who we are, recognitions, SDG alignment, glossary
/readiness                   Readiness Hub landing page
/get-started                 90-day roadmap and role entry points (hub entry point)
/how-it-works                Assessment, Core Criteria, process, ratings
/pitfalls                    Common pitfalls
/documentation-checklist     The nine required uploads
/core-criteria-explorer      Interactive Core Criteria reference
/readiness-check             Interactive readiness self-check
/faq                         Objections answered, plus the member track
```

**Global nav (Track A):** The Business Case, The Capital Map, Stewardship, Pricing, Partners, About, Readiness Hub

**Global CTA button** (persistent, `--gk-deep`): **"Start the Conversation"**, linking to mailto:Sales@greenkeyglobal.com

**Readiness Hub sub-pages** are navigated from within the hub, not from the main nav. Get Started is the hub's entry point.

**Footer:** band graphic, GREENKEYGLOBAL.COM, contact email, "Pricing and program details current as of July 2026; confirm at greenkeyglobal.com," and a link list of third-party sources.

---

## 5. Page Content

### 5.0 Two-track structure

**Track A, the owner case.** Home, The Business Case, The Capital Map, Stewardship, Pricing and ROI, Partners, About. Written for ownership groups, asset managers, investors, and lenders.

**Track B, the Readiness Hub.** Get Started, How It Works, Common Pitfalls, Documentation Checklist, Core Criteria Explorer, Readiness Self-Check, FAQ. Written for the GM and department heads who execute after the owner approves.

Navigation shows the seven Track A pages plus a single "Readiness Hub" entry.

---

### 5.1 Home `/`

**Eyebrow:** The Leading North American Standard in Sustainable Hospitality Certification

**H1:** The capital you are already deploying can earn twice

**Lede:** Every hotel replaces lighting, water fixtures, HVAC, and building systems eventually. Green Key Global Eco-Rating certification is what turns that committed capital into a verified credential that corporate buyers, booking platforms, lenders, and regulators all accept, without requiring a capital project of its own.

**Hero styling:** dark `--gk-dark` background, white text.

**Primary CTA:** Start the Conversation (mailto Sales@greenkeyglobal.com)

**Secondary CTA:** See the Capital Map

#### Two paths block (immediately below the hero)

Two cards, equal weight.

- **I am evaluating the investment.** The demand evidence, the operating cost case, and what certification does to asset value. Links to The Business Case.
- **My team is preparing to certify.** The documents to gather, the people to involve, the mistakes that cost properties time. Links to the Readiness Hub.

#### The question every hotel gets asked

Four cards on pale tint.

1. **Corporate RFPs.** Travel buyers ask for recognized certification before shortlisting your property.
2. **Booking platforms.** OTAs ask for third-party verification before showing a sustainability badge.
3. **Brand standards.** Flags are adding certification to brand requirements.
4. **The utility line.** Owners ask why energy, water, and waste costs keep climbing.

Closing line: "It is always the same question underneath: **can this hotel prove, credibly, how it operates?**"

#### Three lenses

Three cards summarizing the owner argument. Each links to the relevant section of The Business Case.

- **Revenue.** Corporate and group demand is consolidating around properties that can prove how they operate. Certified hotels are winning measurably more of it.
- **Operating cost.** The assessment rewards metering, preventative maintenance, and right-sized purchasing. The same disciplines that earn certification reduce utility and supply spend.
- **Asset value.** Operating savings flow to NOI, and NOI capitalizes into value. Certification also supports sustainability-linked financing conversations and reduces exposure to tightening disclosure rules.

#### Evidence tiles

Four big-number cards. Every figure carries its source beneath the block. Use only figures from Section 6.1.

- `3,000+` certified properties across North America
- `3x` the corporate room nights at certified hotels
- `~11 days` average to complete the Core Criteria assessment
- `<$80/mo` published U.S. cost across a full three-year cycle

Caption: "Corporate room-night figure: Alo Index, analysis of 5,082 assessed hotels, 2025 full year. Other figures: Green Key Global program data and published pricing, July 2026."

#### Why this program stands apart

Six short items, two columns.

- **Built by the industry.** Founded in 1993 and jointly owned by the American Hotel and Lodging Association and Hotels Canada.
- **It certifies operations, not construction.** The assessment covers how a property is run, so an older asset and a new build compete on the same terms.
- **No capital spend required to certify.** Certification begins with governance, documentation, and measurement.
- **Independently audited.** Verification is carried out by Control Union, an accredited third-party Certification Body.
- **A trusted benchmark.** Aligned with all 17 UN Sustainable Development Goals, GSTC-Recognized, and recognized by Travalyst, the coalition behind sustainability labels on major booking platforms.
- **A clear front door.** The 2026 Core Criteria define 37 mandatory questions as the path to a first Key. Every rating from 1 to 5 Keys is full certification.

#### Closing CTA

Two buttons: Start the Conversation (Sales@greenkeyglobal.com) and See the Capital Map.

---

### 5.2 The Business Case `/why-certify`

Replaces the previous Why Certify page. File name stays why-certify.html so existing links do not break. Update the page title, H1, and nav label to "The Business Case".

**H1:** The business case for certification

**Intro:** Certification is usually presented as a sustainability decision. For an owner it is three separate business decisions that happen to share one credential: a demand decision, an operating cost decision, and an asset value decision. The math is plain: for most properties, three extra bookings in a year covers the cost of certification, and every booking after that is positive return.

#### 1. Revenue and demand

**Chart 1: "The demand for certified sustainability is measurable"** (horizontal bars, values labeled with percentages):

| Value | Label | Source tag on bar |
|---|---|---|
| 90 | Consumers who look for sustainable options when traveling | Expedia Group, 2022 |
| 85 | Travelers who say sustainable travel is important or very important | Booking.com, 2026 |
| 76 | Travel buyers adding sustainability clauses to supplier contracts | GBTA Foundation, 2023 |

**Chart 2: "Certified hotels win more corporate business"** (column chart plus two callout cards):

- Columns: average corporate room nights per hotel by Alo score band (2025). Score 0 = 126, Score 1 to 60 = 134, Score 61 to 80 = 484, Score 81 to 100 = 1,189. Shade the top two bands bright and deep green, the others muted grey `#C9CFCB`.
- Callout card A: **3x** the corporate room nights at certified hotels, 622 per year versus 202 at non-certified.
- Callout card B (dark): **97% vs 70%**, certified hotels that won corporate business versus non-certified.
- Source line: "Source: Alo Index, analysis of 5,082 assessed hotels, 2025 full year. Green Key Global partnered with the Alo Index in 2026."
- Note that these are Alo Index scores, not Green Key Eco-Rating scores. Do not imply they are the same measure.

**Supporting copy:**

- Booking platform visibility. Travelers booked more than 100 million room nights at accommodation partners with third-party sustainability certification on Booking.com in 2025.
- Kill the generational objection explicitly. Roughly a third of travelers in every generation, Boomers through Gen Z, plan to stay at certified accommodation in the coming year. This is not a young-traveler preference, it is a market-wide expectation.
- Corporate buyers are measuring. Sophisticated travel programs track and report business-travel emissions, and some price carbon internally. A certified property is a lower-friction line item in that ledger. Cite GBTA Foundation research and state the sample size as directional.
- Expedia research has also linked certification to guest satisfaction, reporting a 15% increase in positive guest reviews at certified luxury properties (Expedia Group, 2022).
- Frame the takeaway in revenue-quality terms: corporate and group business books further out and is stickier than transient, so mix improvement compounds.

#### 2. Operating cost

- The practices the assessment rewards are the same practices that cut spend: metering utilities, preventative maintenance, sealing the building envelope, efficient lighting, water-wise housekeeping, right-sized food purchasing, waste diversion. The assessment is largely not asking a hotel to spend money on sustainability. It is asking it to stop spending money on waste.
- Measurement is the entry point by design. The mandatory Engineering requirements are about tracking annual use and cost of electricity, natural gas, and water, because a property cannot manage or fund what it does not meter.
- Note the free tooling: the EPA ENERGY STAR Portfolio Manager benchmarks energy, water, waste, and emissions at no cost, and produces the kind of records the tracking requirements expect.
- Do not quantify certification return. Quantify only utility and operating logic, and only in the owner's own terms.

#### 3. Asset value

- The arithmetic an owner already uses: operating savings flow to NOI, and NOI divided by the going-in cap rate is value. A recurring reduction in utility and supply cost therefore capitalizes into a multiple of itself at sale.
- Present this as an illustrative frame with the owner's own inputs, not as a Green Key claim. Do not publish a savings estimate.
- JLL's analysis of existing hotel assets reaches the same conclusion from the owner's chair: hotels that embed sustainability into capital planning see reduced operating costs, improved access to green financing, enhanced brand equity, and lower regulatory and reputational exposure (JLL, November 2025).
- Financing. Sustainability-linked lending and lender ESG diligence increasingly ask for independent verification rather than self-reported claims.
- Exit. A verified operating credential is a diligence asset. It answers, with third-party evidence, a question a buyer will otherwise ask the seller to answer with a spreadsheet.

#### 4. Risk and regulation

**Where the industry is heading** (three cards, middle one dark):

1. **WTTC.** Elevating Hotel Sustainability Basics, adopted by 8,000+ hotels in 85 countries, into an independent third-party certification scheme (WTTC, 25 June 2026).
2. **EU regulation.** The Empowering Consumers for the Green Transition Directive takes force September 2026. Sustainability labels shown to EU travelers require independent verification (Directive (EU) 2024/825).
3. **Owners' advisors.** JLL: embedded sustainability now means lower operating costs, green financing access, brand equity, and lower regulatory risk (JLL, November 2025).

**Supporting copy:**

- Further EU rules are in development, including a proposed Green Claims Directive and the EU's first comprehensive Sustainable Tourism Strategy. Neither is in force. Do not present either as law.
- Physical risk. Accommodation providers are already reporting operational disruption from extreme weather and adjusting operations in response (Booking.com partner survey, 2026).
- The framing for an owner: self-reported sustainability claims are becoming a liability, and independent certification is the cheapest available form of substantiation.

Closing line: "Eco-Rating is this model, built for North America, with a two-decade head start with the buyers who matter here."

**Comparison table (Eco-Rating vs WTTC Basics)**, with the note: "The two programs are complementary rather than competing. Basics defines a global floor, while Eco-Rating provides the comprehensive, North America-focused certification a property can grow with."

| | Green Key Eco-Rating | WTTC Hotel Sustainability Basics |
|---|---|---|
| Scope | Comprehensive: 200+ operational questions across five hotel departments | Entry-level: 12 fundamental actions |
| Depth of rating | Graduated 1 to 5 Keys, room to grow for a decade | Verified baseline (phased over 3 years) |
| Market focus | North America; OTA, RFP, and brand integration here | Global framework |
| Governance | Owned by AHLA and Hotels Canada; independent audit by Control Union | WTTC initiative; certification transition underway |
| Recognition | GSTC-Recognized standard; Travalyst; SDG-aligned | Aligning to GSTC Accreditation Framework and EU rules |

---

### 5.3 The Capital Map `/capital-map` (flagship page)

This is the page an owner forwards to their asset manager. It answers one question: given that we are going to spend money on this building anyway, in what order should we spend it, and what does certification change about that order.

**H1:** Where to deploy capital, and in what order

**Lede:** Certification does not ask an owner to fund a new project. It asks an owner to sequence projects that are already on the plan, and to finish the ones that are already started.

#### Section A. Start with what is already committed

Every hotel replaces lighting, water fixtures, roofs, windows, boilers, and HVAC on a cycle. That capital is committed regardless of certification. The question is only whether each dollar also produces verified evidence of how the property operates. Certification is a sequencing layer on an existing capital plan, not a new line item.

#### Section B. Where the work concentrates

Describe qualitatively. No point values and no section weights.

- **Corporate Environmental Management** is the governance backbone: written and endorsed policy, a management action plan, a responsible purchasing policy, and a functioning Green Team. It holds more of the mandatory Core Criteria than any other section and requires essentially no capital.
- **Engineering and Maintenance** is the largest section of the assessment and the one that maps onto a capital plan: metering and sub-metering, preventative maintenance, lighting, water fixtures, building envelope, HVAC and heat recovery, renewables, waste infrastructure.
- **Housekeeping** is training, procedure, and product choice. Low capital.
- **Conference and Meeting Services** and **Food and Beverage** are optional. A property without meeting space or a full-service restaurant opts out and the scoring rescales, so a select-service property is not disadvantaged.

Takeaway for an owner: the certification gate is governance, and the rating ceiling is engineering. Those are two different budgets and two different owners inside the organization.

#### Section C. Finish what you fund

The single most useful thing an owner can know about this assessment.

**The questions are assessed by area, not by project.** Lighting coverage is assessed separately for guest rooms, for public areas, and for back of house. Water fixture coverage is assessed by how much of the property is converted. A retrofit package scoped to guest rooms only leaves the rest of the building unanswered.

**Graduated questions reward completion.** Partial coverage earns partial credit and full coverage earns the most credit. Stopping a conversion program at three quarters leaves the strongest part of the return on the table.

**And the operating case points the same direction.** Back of house runs 24 hours a day. Corridors, stairwells, kitchens, laundry, and parking never go dark. The utility payback on completing those areas is stronger than on guest rooms, independent of certification entirely.

**The instruction to an owner:** do not approve a guest-room-only package. Scope conversions building-wide, and finish them. The last stage of a retrofit is where both the utility return and the certification return concentrate.

#### Section D. Three phases

- **Phase one, the baseline. Roughly one quarter, near zero capital.** Stand up the Green Team, sign the policies, launch the linen and towel reuse program, standardize thermostat set points, put preventative maintenance in writing, and pull twelve months of utility invoices. This satisfies the mandatory Core Criteria and secures certification, which immediately unlocks the marketing toolkit, OTA and RFP visibility, and a verified answer for corporate buyers.
- **Phase two, operating budget retrofits.** Sensors and controls, completing LED conversion building-wide, aerators and low-flow fixtures, bulk dispensers, recycling infrastructure. These carry their own utility and supply-cost payback and lift the assessment across Housekeeping, Food and Beverage, and Engineering at the same time.
- **Phase three, the capital plan.** HVAC, boilers, sub-metering, envelope, renewables, EV charging, and waste infrastructure, evaluated the way ownership already evaluates capex, on payback and asset value, with a higher Key rating as the compounding return.

Reassessment runs on a three-year cycle, which matches a staged capital plan. Each cycle, the projects funded convert into a visibly higher rating.

#### Section E. Priority by capital intensity

Three grouped lists. Ranked order only. **No point values, no scores, no numbers of any kind.**

**Zero capital: policy, program, and people**

Written management action plan addressing policy commitments. A Green Team drawn from every department including management. External reporting on sustainability performance. A policy to consolidate occupied guestrooms and close floors during low occupancy. Employee wage, health care, and benefit coverage. Training and development programs.

Note for the owner: the employee items are operating cost decisions rather than projects, and they carry real weight in the assessment. How a property treats the people who run it is part of the rating.

**Low capital: graduated retrofits with utility payback**

High-efficiency lighting completed across guest rooms, public areas, and back of house. Low-flow toilets, showerheads, and tap aerators across the guestroom count. High-efficiency lighting controls in general areas. High-efficiency windows. Eco-certified cleaning products. Reusable service ware in food and beverage.

**Capital and systems projects**

Energy, water, waste, and greenhouse gas performance audits. Energy sub-metering across hotel areas. Grey water recovery and reuse. Waste diversion infrastructure toward a zero-waste rate. Renewable energy procurement.

Closing note: nearly every item in the second and third groups carries a direct utility, supply, or waste-hauling payback that exists with or without certification. Certification is the compounding return on investments that already clear an ownership hurdle rate on their own.

#### Section F. The two documents that build your capital plan

The assessment asks whether energy, water, waste, and greenhouse gas performance audits have been carried out. Those audits exist precisely to price the payback for a specific property. Certified properties also receive a Property Performance Report alongside their rating, identifying accomplishments and specific recommendations for improvement.

Used together, these two documents convert "invest in sustainability" into a ranked, priced project list with both a savings case and a certification case per line item. That is a document an asset manager can take to an investment committee.

**CTA:** Start the Conversation (Sales@greenkeyglobal.com)

---

### 5.4 Stewardship `/stewardship`

Short page. Confident, not preachy. This is the ethos of the program stated in operating terms.

**H1:** A well-run house

**Lede:** Waste is unmanaged money. Energy that leaves through an unsealed door, water that runs through a worn valve, food ordered past what the covers require, linen replaced before its service life ends. A hotel that does not waste is not making a statement. It is running well.

#### The assessment is an audit of operating discipline

Strip away the vocabulary and the questions are about metering, preventative maintenance, trained staff, documented procedure, and evidence. Those are the same disciplines that protect an asset between renovation cycles, and the same ones that keep an operating statement honest.

#### The people who run the building are part of the standard

The assessment covers wage coverage, health care access, training and advancement, workplace health and wellbeing, diversity and inclusion, and community engagement. This is not the program straying outside its lane. Decent work is part of the international definition of a sustainable hotel: the GSTC Industry Criteria for Hotels, the global baseline against which certification schemes are recognized, include criteria on living wage, training records, employee contracts, grievance mechanisms, and equal opportunity.

For an owner the connection is direct. Turnover is expensive, service scores follow tenure, and a property that cannot hold a housekeeping team cannot hold a rating either.

#### Place

The assessment credits sourcing locally, supporting local entrepreneurs, interpreting the natural and cultural surroundings for guests, protecting biodiversity, and engaging with the community the hotel sits inside. A hotel is a permanent structure in someone else's neighborhood. Behaving like a good neighbor is both the right posture and a durable commercial one.

#### Resilience

Extreme weather is already an operating variable. Accommodation providers report disruption from heat, storms, and flooding, and many have adjusted operations in response (Booking.com partner survey, 2026). The disciplines this assessment builds, metering, maintenance, documented procedure, trained staff, are the same ones a property relies on when conditions turn.

#### Closing

Certification is not a claim about intentions. It is independent evidence that a building is run carefully, by people who are treated well, in a place it is trying not to damage. That is worth having on its own terms. It also happens to be what the market is now asking properties to prove.

---

### 5.5 Get Started `/get-started`

Entry point to the Readiness Hub.

#### Role entry points

Three cards at the top of the page, each linking into the Readiness Hub.

- **I am the General Manager.** Governance, policy, the Green Team, and the documents that need a senior signature.
- **I run Housekeeping.** Guestroom procedure, the linen and towel reuse program, training confirmation, cleaning product and waste handling policy.
- **I run Engineering.** Utility tracking, preventative maintenance documentation, fixture and lighting coverage, building systems.

#### The 90-day path

Three phase cards.

- **Days 1 to 30: Foundation.** Name the accountable senior officer. Form the Green Team with a written mandate and quarterly meetings on the calendar. Request 12 months of utility invoices (electricity, gas, water). Download our templates for the sustainability policy, action plan, purchasing policy, and Green Team mandate.
- **Days 31 to 60: Close the gaps.** Launch the linen and towel reuse program. Put the preventative maintenance program in writing. Standardize thermostat set points and add the trained behaviors to housekeeping checklists. Finalize and sign the purchasing policy. Document fixture coverage and any F&B monitoring logs.
- **Days 61 to 90: Assess and request audit.** Complete the self-assessment using the Core Criteria filter first. Upload every required document. Run a cross-department consistency check (the assessment locks once the audit is requested). Choose virtual or on-site audit and request it through the Members Area.

#### What each department will be asked to do

Nothing in this table requires a budget line to start.

| Team | Day-to-day contribution |
|---|---|
| Housekeeping | Run the linen reuse program. Clean by natural light where possible, manage blinds with heating and cooling needs, keep windows and doors closed while systems run, switch off lights and TVs in empty rooms, minimize water while cleaning, report faulty equipment right away. |
| Engineering and Maintenance | Keep utility bills organized and tracked. Follow the written preventative maintenance schedule for HVAC, ventilation, plumbing, and lighting. Log fixture coverage and efficiency upgrades. |
| Front Office and Admin | Email guest folios instead of printing. Default to double-sided printing. Help communicate the sustainability policy to staff and guests. |
| Food and Beverage (if applicable) | Keep freezer and thawing logs. Practice first-in-first-out and right-sized ordering. Separate organics where service exists, log surplus food donations. |
| General Manager | Sign and endorse the policy, sponsor the Green Team, keep the quarterly meeting cadence real. The audit checks for evidence of meetings, not just a signed document. |

#### What happens when you request the audit

Owners and GMs both get surprised by this sequence, so state it plainly.

- The self-assessment can be saved, revisited, and retaken as many times as needed before an audit is requested.
- Requesting the audit and paying the audit fee **locks the assessment**. Complete a cross-department consistency review first.
- Green Key Global uses commercially reasonable efforts to begin the audit process within approximately ninety days of receiving the audit request and fees.
- Applicants receive at least one week's notice of any on-site inspection unless a shorter period is agreed. Rescheduling requires three business days' notice for a virtual audit, twenty for an on-site audit.
- Control Union, as the independent Certification Body, is prohibited under ISO 17065 from providing consulting support. Preparation help comes from Green Key Global templates, tips text, and member services.

#### Closing block and CTA

We never ask a property to be something it is not. We ask a hotel to run well, prove it, and be recognized for it: by a standard hoteliers built, anchored to goals the whole world has agreed on, verified by an auditor no one can lean on, at a price every tier of the market can carry.

**CTA:** Start the Conversation (Sales@greenkeyglobal.com). Existing members should contact Green Key Global member services through the Members Area.

---

### 5.6 Readiness Hub `/readiness`

Hub landing page with cards linking to each sub-page below.

#### 5.6.1 Common Pitfalls `/pitfalls`

Seven items, each a short bolded lead-in plus one or two sentences.

- Waiting until the property feels ready before starting the self-assessment. Progress saves, and starting early surfaces documentation gaps while there is still time to close them.
- Treating the Green Team mandate as paperwork. The audit looks for evidence of actual quarterly meetings, not only a signed document.
- Underestimating how long it takes to gather twelve months of utility invoices, especially across multiple fuel types or where billing is not centralized. Start this first.
- Assuming that opting out of Food and Beverage or Conference sections will hurt the result. It does not. The scoring rescales.
- Expecting hands-on consulting from the auditor. Control Union is prohibited under ISO 17065 from providing consulting support.
- Not documenting practices the property already runs. Many properties already recycle or have fixtures installed but never wrote the practice down or kept evidence.
- Requesting the audit before an internal cross-department review. The assessment locks on request.

#### 5.6.2 Documentation Checklist `/documentation-checklist`

Table of the nine questions that require a document upload, with the department that owns each. Templates and examples are provided by Green Key Global inside the Members Area.

| Section | Question | Document to upload | Owner |
| --- | --- | --- | --- |
| Corporate | Q1 | Sustainability Policy, signed by a senior officer | GM and senior leadership |
| Corporate | Q2 | Management Action Plan, reviewed within 12 months | GM and Green Team |
| Corporate | Q3 | Responsible Purchasing Policy | GM and Purchasing |
| Corporate | Q9b | Green Team written mandate | Green Team lead |
| Housekeeping | Q19 | Cleaning supplies and medical waste disposal policy | Executive Housekeeper |
| Engineering | Q4 | Electricity use and cost records | Chief Engineer |
| Engineering | Q5 | Natural gas use and cost records | Chief Engineer |
| Engineering | Q11 | Water use and cost records | Chief Engineer |
| Engineering | Q15 | Preventative maintenance program | Chief Engineer |

Add a practical note: the EPA ENERGY STAR Portfolio Manager is a free tool for tracking energy, water, waste, and emissions, and it produces the kind of records the utility tracking questions ask for. Link to energystar.gov/benchmark.

Also gather: waste hauling and disposal records including any diversion data, and a current vendor and supplier list for mapping against purchasing criteria.

#### 5.6.3 Core Criteria Explorer `/core-criteria-explorer`

Interactive, client-side, no backend. Reads its content from `data/core-criteria.json` rather than hardcoded markup, so the question set can be updated without touching code.

Filter the 37 mandatory Core Criteria by department (Corporate, Housekeeping, Engineering) and by whether a document upload is required. Show question text, department owner, and upload requirement. **Show no point values and no answer scoring.**

#### 5.6.4 Readiness Self-Check `/readiness-check`

Interactive checklist built from the preparation checklist: documents to gather, policies to have in place, people to involve. Output is a readiness summary and the next three actions. Client-side only, no data stored, no backend, no browser storage.

#### 5.6.5 FAQ, member track

See Section 5.11. The member track is a second accordion group on the same FAQ page.

---

### 5.7 How It Works `/how-it-works`

#### Inside the assessment: five Key Performance Areas

| KPA | Covers | Applies to |
|---|---|---|
| Corporate Environmental Management | Policy, action plan, responsible purchasing, Green Team, staff and guest engagement, community involvement | All properties |
| Housekeeping | Linen reuse, cleaning products, energy and water conscious room routines, training | All properties |
| Engineering | Utility tracking, preventative maintenance, HVAC, insulation, lighting, fixtures, waste, renewables | All properties |
| Food and Beverage | Purchasing, food waste reduction, refrigeration monitoring, service practices | Optional, opt out if not applicable |
| Conference and Meetings | Event-space sustainability practices | Optional, opt out if not applicable |

Copy: 200+ questions, multiple users, save as you go, templates for every required document, and evidence uploaded against each mandatory answer so the audit verifies proof, not promises. Opted-out sections rescale the score with no penalty.

#### The 37 Core Criteria

Supporting graphic: a bar mini-chart showing the distribution by section, Corporate 15, Housekeeping 10, Engineering 12. **Do not show the Core Criteria as a share of a total question count.**

- In early 2026 we defined the program's baseline: 37 mandatory questions constitute the minimum for a 1-Key certification. A "Display Core Criteria Only" filter isolates them in the portal.
- Speed: average completion fell from about 80 days to about 11, and the focused assessment itself takes roughly 4 to 6 hours of work (Green Key Global program data, 2026).
- The plain-terms summary, six items:
  - **Govern it.** Signed policy, named accountable manager, action plan reviewed within the year.
  - **Buy responsibly.** Written purchasing policy with local, recycled, and eco-certified priorities.
  - **Staff it.** Green Team with a written mandate and quarterly meetings.
  - **Train for it.** Linen reuse program, thermostat set points, housekeeping routines, safe handling of cleaning and medical waste.
  - **Measure it.** Twelve months of utility data, written preventative maintenance, HVAC checks, fixture coverage reporting.
  - **Prove it.** Evidence uploaded for every mandatory answer, templates provided.
- Kicker: under ISO/IEC 17065, a credible certification cannot rest on a hotel's word alone. It has to show its work.

Link out to the Core Criteria Explorer for the full question-by-question view.

#### The process

Five-step flow, step 3 visually emphasized dark.

1. **Assess.** Online self-assessment, multiple users, save as you go.
2. **Evaluate.** Preliminary rating and gap scorecard, retake freely. The preliminary rating may not be represented publicly as certification.
3. **Audit.** Independent verification by Control Union.
4. **Certify.** 1 to 5 Keys, valid three years, Property Performance Report issued.
5. **Market.** Toolkit, OTA badges, RFP content, plaque.

#### Impartial by design (callout box)

We set the standard but never audit our own members. Audits are conducted by Control Union, an independent global inspection firm, and the certification decision rests with an independent Certification Body, per ISO/IEC 17065. Audits typically commence within approximately ninety days of request. Rescheduling requires three business days' notice for a virtual audit, twenty for an on-site audit. A property that stops meeting requirements is subject to corrective action, suspension, or revocation. A label that can never be withdrawn is not a certification.

#### The rating

Ascending five-block Keys ladder, labeled by Key level only.

| Rating | What it means |
|---|---|
| 1 Key | Full certification. All 37 mandatory Core Criteria met. |
| 2 Keys | Full certification, with stronger performance across the assessment. |
| 3 Keys | Full certification, with stronger performance again. |
| 4 Keys | Full certification, approaching the top of the scale. |
| 5 Keys | Full certification at the highest level of the scale. |

**Do not publish the score ranges behind each Key level.**

Copy: Any rating is full certification. The audit-issued Property Performance Report shows exactly where the next Key is won, turning "improve our rating" into an assignable plan across three-year cycles. Members renew membership annually. At the end of three years the property recertifies against the then-current criteria.

#### After you are certified

Four cards.

1. **Marketing Toolkit.** Logos, website copy, in-room and event collateral, RFP response content, staff checklists.
2. **Automatic distribution.** Certified-property lists shared with OTAs, procurement officers, and RFP platforms.
3. **Property Performance Report.** A property-specific roadmap showing where the next Key is won.
4. **Green Vendor Directory.** Vetted sustainability suppliers with member discounts. Strictly vendor-agnostic: we do not certify, endorse, or take referral fees from vendors.

Claims note: certified members may use the Green Key name and rating only while current and in scope.

---

### 5.8 Pricing and ROI `/pricing`

#### Published pricing table (July 2026)

| Item | United States | Canada |
|---|---|---|
| Annual membership, per property | $750 / year | $950 CAD / year |
| Virtual audit, once per 3-year cycle | $500 | $500 |
| On-site audit (optional alternative) | $2,500* | $2,500* |
| Additional audits (if required) | $500 | $500 |

*Travel dependent. Fees are non-refundable except in exceptional circumstances. Fees are reviewed periodically. Current pricing at greenkeyglobal.com.

**Callout cards:**

- `<$80/month`. Full three-year U.S. cycle: $2,750 all-in with a virtual audit.
- `3 bookings`. Three extra bookings in a year covers the cost of certification. The rest is return.

**Partnership note:** List pricing is the ceiling, not the expectation, for groups. Portfolio agreements (MSAs for brands, MOUs for management companies) carry negotiated per-property rates, coordinated onboarding, and fast-track pathways. Link to /partners. **Never state a discount percentage.**

#### ROI Calculator (interactive component on this page)

Inputs, with defaults. All editable.

| Input | Default | Notes shown to user |
|---|---|---|
| `props` Number of properties | 5 | Start with a pilot cohort |
| `adr` Average daily rate | $145 | Blended across the cohort |
| `rn` Current corporate room nights per property per year | 202 | Default is the Alo Index average for non-certified hotels (2025). Replace with your own |
| `util` Annual utility spend per property | $190,000 | From your P&L |
| `member` Annual membership per property | $750 | Published list, US$ |
| `audit` Virtual audit per property per 3-year cycle | $500 | Published list |
| `disc` Partnership discount | 0% | Leave at 0% until a term sheet exists |
| `liftC` Conservative lift | 5% | Far below the Alo-observed gap |
| `liftM` Moderate lift | 15% | Assumes badges live and RFP usage |
| `liftS` Strong lift | 40% | Still well under the 3x observed gap. Correlation, not a promise |
| `save` Utility savings | 3% | Low single-digit operating savings. Adjust to experience |

Formulas:

```
memberNet   = member * (1 - disc)
auditAnnual = audit * (1 - disc) / 3
costPerProp = memberNet + auditAnnual           // per property per year
costCohort  = costPerProp * props               // per year
costMonthly = costPerProp / 12
breakevenRN = adr > 0 ? costPerProp / adr : 0   // room nights per property per year
addedRN(l)  = rn * l                            // per property
addedRev(l) = addedRN(l) * adr                  // per property per year
cohortRev(l)= addedRev(l) * props
utilSaveProp   = util * save
utilSaveCohort = utilSaveProp * props
netBenefit(l)  = cohortRev(l) + utilSaveCohort - costCohort
returnX(l)     = costCohort > 0 ? (cohortRev(l) + utilSaveCohort) / costCohort : 0
```

Render results for Conservative, Moderate, and Strong side by side, plus break-even room nights and cost per month.

Required disclaimers under the calculator: "Illustrative planning tool, not a forecast or commitment. Revenue figures are room revenue, not profit. Apply your own flow-through."

Show sources: Alo Index (5,082 hotels, 2025), greenkeyglobal.com pricing (July 2026).

---

### 5.9 Partners `/partners`

**Intro:** For brands and management companies, certification is structured as a partnership: a formal membership commitment across your portfolio in exchange for preferred pricing and dedicated support.

#### What a formal partnership includes

Six cards.

1. **Preferred pricing.** A membership commitment across your portfolio in exchange for improved certification fees under an MSA or MOU.
2. **Dedicated Account Manager.** A named owner of your partnership from activation onward: rollout support, troubleshooting, best-practice guidance.
3. **Structured activation.** A joint kickoff with your team, a year-one engagement plan, promo codes, and enrollment workflows configured for your properties.
4. **Co-marketing launch.** A joint launch plan with agreed messaging across PR, web, social, and email, supported by our templates.
5. **Quarterly reporting.** Partnership progress reports tracking certification, participation, and impact against agreed targets.
6. **Fast-track equivalencies.** Where a brand program equivalency exists, work your properties have already done is credited toward certification.

#### The partnership journey

Four numbered phases, large bright-green numerals.

1. **Explore and agree.** Discovery of your portfolio goals and timelines, a tailored proposal and term sheet, an MSA or MOU with negotiated rates.
2. **Onboard.** Activation meeting with your team, dedicated Account Manager assigned, promo codes, workflows, co-marketing launch.
3. **Execute.** Property rollout and certification support, best-practice guidance on demand, quarterly and annual progress reports.
4. **Grow and renew.** Annual review against agreed targets, expansion across the portfolio, renewal on proven results.

Closing: If your flags or group already hold an agreement with us, your properties may have simplified enrollment waiting. Ask before enrolling individually.

---

### 5.10 About `/about`

**Who we are:** Green Key began in 1993, created by the Hotel Association of Canada (now Hotels Canada). In 2024, the American Hotel and Lodging Association and Hotels Canada formed the joint venture that is Green Key Global today: the leading hotel sustainability certification program in North America, with more than 3,000 certified properties. We certify operations, not construction. In partnership with One Tree Planted, a tree is planted for every new member, more than 13,000 trees since 2023.

#### Recognitions

Badge row.

- **United Nations SDGs.** Aligned with all 17 Sustainable Development Goals.
- **GSTC-Recognized.** Standard recognized by the Global Sustainable Tourism Council.
- **Travalyst.** Recognized by the coalition behind sustainability labels on major booking platforms.
- **ISO-aligned, EU-ready.** Certification structured around ISO/IEC 17065. Compliant architecture for Directive (EU) 2024/825, in force 27 September 2026.

#### SDG mapping table

| # | Goal | How a hotel contributes |
|---|---|---|
| 1 | No Poverty | Hotel jobs and local purchasing keep income in the communities where properties operate. |
| 2 | Zero Hunger | Food waste reduction and surplus food donation put edible food to use instead of landfill. |
| 3 | Good Health and Well-Being | Safer cleaning products, air quality, and proper hazardous waste handling protect guests and staff. |
| 4 | Quality Education | Staff sustainability training builds transferable skills across every department. |
| 5 | Gender Equality | Hospitality is a major employer of women. Equitable practice turns jobs into careers. |
| 6 | Clean Water and Sanitation | Guestroom fixtures, laundry programs, and kitchen practice conserve a shared community resource. |
| 7 | Affordable and Clean Energy | Tracking and reducing energy use lowers cost and the emissions tied to it. |
| 8 | Decent Work and Economic Growth | Local sourcing and fair, stable hospitality employment strengthen the tourism economy. |
| 9 | Industry, Innovation and Infrastructure | Efficient building systems modernize a property while cutting resource use. |
| 10 | Reduced Inequalities | Sustainable tourism brings investment and opportunity to overlooked communities. |
| 11 | Sustainable Cities and Communities | Hotels are part of the built fabric of their cities and towns. |
| 12 | Responsible Consumption and Production | Responsible purchasing, eco-friendly products, and waste reduction in daily operation. |
| 13 | Climate Action | Every kWh and therm avoided is a direct, measurable contribution. |
| 14 | Life Below Water | Coastal and island properties depend on the healthy oceans that sustain their tourism. |
| 15 | Life on Land | Conserving resources and supporting biodiversity protects ecosystems on and around property. |
| 16 | Peace, Justice and Strong Institutions | Written policies, accountable officers, and documented plans are governance in practice. |
| 17 | Partnerships for the Goals | Our organization is itself a partnership between AHLA and Hotels Canada. |

Note under the table: four operational areas do an outsized share of the work. Energy advances SDG 7 and 13. Water advances SDG 6. Food waste advances SDG 2 and 12. Procurement advances SDG 8 and 12.

#### Glossary

Definition list.

- **Core Criteria.** The 37 mandatory questions forming the 1-Key baseline.
- **KPA.** One of five assessment sections.
- **Scheme Owner.** Green Key Global. Develops the standard, does not audit.
- **Certification Body.** The independent decision-maker on certification.
- **Audit Body / Control Union.** The independent third-party audit firm.
- **ISO/IEC 17065.** International standard for certification bodies.
- **ISO 14001.** Environmental management systems standard.
- **GSTC.** Global Sustainable Tourism Council.
- **Travalyst.** Sustainable-travel coalition behind booking-platform labels.
- **Green Team.** Mandatory cross-department group with a written mandate and quarterly meetings.
- **MSA / MOU.** Portfolio agreements for brands and management companies.
- **OTA.** Online travel agency.
- **Property Performance Report.** Audit-issued improvement roadmap.
- **Sub-metering.** Separate meters for detailed tracking.

---

### 5.11 FAQ `/faq`

Accordion, in two groups.

#### Group 1: Evaluating certification

1. **Is there a budget case for this?** Under $80 a month per property at list, less under a portfolio agreement, and no capital spend is required to certify. Three extra bookings a year covers it, and the practices it rewards cut the utility line.
2. **Sustainability does not sell in our market. Why certify?** Then lead with operations and revenue. Corporate RFP eligibility, OTA badges, and a 3x corporate room-night gap (Alo Index) are market-neutral. The certification works whether a property leads with the environmental story or the cost-discipline story.
3. **We do not have a sustainability person.** The assessment is organized by department. The GM, executive housekeeper, and chief engineer already own the answers. The Core Criteria take 4 to 6 hours of focused work, with templates for every required document.
4. **We are already in a brand program.** AHLA co-owns Green Key, and brand programs feed in. Where an equivalency exists, work already done is credited. Ask before assuming you start from zero.
5. **What if we fail the audit?** You cannot be surprised by it. The self-assessment produces a preliminary rating and gap scorecard first and can be retaken freely. Nothing locks until you request the audit.
6. **Is this just a badge?** We never audit our own members. Control Union verifies evidence independently, the decision sits with an independent Certification Body under ISO/IEC 17065, and certification can be suspended or revoked.
7. **Our owners only care about NOI.** JLL's guidance to owners: embedded sustainability means lower operating costs, better access to green financing, and lower regulatory exposure. Add utility savings and this is an NOI conversation.
8. **We looked at LEED. Too expensive.** Different animal. LEED certifies how a building was constructed. We certify how a hotel operates. No construction, no retrofit requirement, no capital gate.
9. **Timing is bad.** Average completion is about 11 days, the focused work is hours not weeks, and the portal saves progress across multiple users. A pilot cohort fits inside one quarter.
10. **Which properties qualify?** All of them. Select-service properties opt out of F&B and conference sections with no scoring penalty, and any rating from 1 to 5 Keys is full certification.
11. **Hidden costs at renewal?** None to hide. Flat published fees, membership renewed annually, one audit per three-year cycle, recertification on the same terms.

#### Group 2: For properties already enrolled

1. **Does every hotel need to complete Food and Beverage and Conference sections?** No, both are optional and the scoring adjusts.
2. **Can we retake the self-assessment before requesting an audit?** Yes, as many times as needed. Progress saves. It locks only when an audit is formally requested and paid for.
3. **What if we cannot meet one of the mandatory Core Criteria yet?** There is no deadline forcing an audit request. Use the member toolkit resources for that requirement and contact member services.
4. **Does a lower rating still count as certified?** Yes. Every rating from 1 to 5 Keys is full certification. Higher Key levels reflect stronger performance and can be built toward over subsequent cycles.
5. **Who needs to be present during the audit?** Whoever completed the self-assessment, plus a representative from each area in scope, typically Engineering, Housekeeping, and Food and Beverage if included.
6. **What happens after our three-year certification expires?** A new independent audit is required. Set a reminder roughly ninety days ahead of expiration.
7. **Should we use Green Key Ready instead?** No. It is being phased out as of 2026 and members are migrated into Eco-Rating. Use the Core Criteria filter inside the Eco-Rating self-assessment for the fastest path to entry-level certification.
8. **What if our brand or management company already has an agreement?** Enrollment may already be simplified through that relationship. Check with your corporate sustainability or brand standards team before registering independently.

---

## 6. Data Registry (single source of truth for every number)

### 6.1 Approved statistics and sources

**Rule: no figure may appear anywhere on the site unless it is listed here, with the source shown on the page where it appears.**

#### Green Key Global program data (July 2026)

| Figure | Use |
| --- | --- |
| 3,000+ certified properties across North America | Home, About |
| Founded 1993, jointly owned by AHLA and Hotels Canada | Home, About |
| 200+ questions across five Key Performance Areas | How It Works, Business Case comparison table |
| 37 mandatory Core Criteria questions | Home, How It Works, Readiness Hub |
| Core Criteria by section: Corporate 15, Housekeeping 10, Engineering 12 | How It Works, Core Criteria Explorer |
| Average completion fell from about 80 days to about 11 | Home, How It Works, FAQ |
| Focused Core Criteria work takes roughly 4 to 6 hours | How It Works, FAQ |
| Certification valid for three years | How It Works |
| Every rating from 1 to 5 Keys is full certification | Home, How It Works, FAQ |
| 13,000+ trees planted with One Tree Planted since 2023 | About |
| Audits typically commence within approximately 90 days of request | How It Works, Get Started |

Source line: Green Key Global program data, July 2026.

#### Published pricing (July 2026)

U.S. annual membership $750 per property per year. Canada annual membership $950 CAD per property per year. Virtual audit $500, once per three-year cycle. On-site audit $2,500, travel dependent. Additional audits $500. Full three-year U.S. cycle $2,750, under $80 per month.

Source line: Green Key Global published pricing, July 2026. Confirm current pricing at greenkeyglobal.com. No discount percentages anywhere.

#### Alo Index, 2025 full year, 5,082 assessed hotels

| Figure | Use |
| --- | --- |
| Certified hotels averaged 622 corporate room nights per year, non-certified averaged 202, roughly 3x | Home, Business Case, FAQ |
| 97% of certified hotels won corporate business, versus 70% of non-certified | Home, Business Case |
| Average corporate room nights by Alo score: 126 at score 0, 134 at 1 to 60, 484 at 61 to 80, 1,189 at 81 to 100 | Business Case |

Source line: Alo Index, analysis of 5,082 assessed hotels, 2025 full year. Green Key Global partnered with the Alo Index in 2026. Ranking correlation between Alo score and room-night volume is approximately 0.5.

Note: these are Alo Index scores, not Green Key Eco-Rating scores. Do not imply they are the same measure. The gradient supports the argument that higher assessed performance correlates with higher corporate demand.

#### Booking.com Travel and Sustainability Report 2026

Published 20 April 2026. Traveler research: 32,500 respondents across 35 markets, surveyed January 2026. Partner research: 3,715 accommodation partners across 18 countries, surveyed February 2026.

| Figure | Use |
| --- | --- |
| 85% of travelers say more sustainable travel is important or very important to them | Business Case |
| Travelers booked more than 100 million room nights at accommodation partners with third-party sustainability certification on Booking.com in 2025 | Home, Business Case |
| Roughly a third of every generation plan to stay at certified accommodation in the next 12 months: Boomers 35%, Gen X 35%, Millennials 36%, Gen Z 35% | Business Case |
| 74% of travelers consider extreme weather risk when choosing destination and timing | Stewardship |
| 31% canceled or changed trip plans in the past 12 months due to extreme weather or natural disasters | Stewardship |
| 24% of accommodation partners experienced operational disruptions due to extreme weather in 2025 | Stewardship, Business Case risk section |

Source line: Booking.com Travel and Sustainability Report 2026, published 20 April 2026. Link to news.booking.com.

This 2026 report supersedes the Booking.com Sustainable Travel Report (2021) previously cited. Use the 85% figure rather than the older 83% figure.

> **Verify before publishing:** the partner survey also reports a 40% figure for partners that adjusted operations in response to climate-related risks. The published summary is ambiguous as to whether 40% refers to all partners surveyed or only to the 24% that experienced disruption. Confirm against the full report before using the 40% figure. The 24% figure is unambiguous and can be used now.

#### Expedia Group, Sustainable Travel Study (2022)

| Figure | Use |
| --- | --- |
| 90% of consumers look for sustainable options when traveling | Business Case, Chart 1 |
| 15% increase in positive guest reviews at certified luxury properties | Business Case |

Source line: Expedia Group, Sustainable Travel Study (2022).

#### GBTA Foundation

| Figure | Source | Use |
| --- | --- | --- |
| 76% of travel buyers adding sustainability clauses to supplier contracts | GBTA Foundation, The State of Climate Action in Business Travel (2023) | Business Case, Chart 1 |
| Companies purchasing SAF overwhelmingly track and report Scope 3.6 business-travel emissions | GBTA Foundation, Corporate Behavior on Sustainable Aviation Fuel Purchases (February 2026), 58 organizations | Business Case, demand section |
| 20% of SAF buyers use internal carbon pricing, at an average internal fee of $95 per ton of CO2e | GBTA Foundation, February 2026, 58 organizations | Business Case, demand section |

The SAF findings are based on 58 organizations. Present as a directional signal about sophisticated corporate travel buyers, and state the sample size. Do not present as a market-wide statistic.

#### GBTA European Parliament roundtable, 9 April 2026

The EU is developing a Sustainable Tourism Strategy, described as the first comprehensive policy framework for the tourism ecosystem. Use as evidence of regulatory direction only. Not in force.

#### Regulatory

| Item | Status | Use |
| --- | --- | --- |
| Directive (EU) 2024/825, Empowering Consumers for the Green Transition | In force 27 September 2026 | Business Case risk section, About |
| Green Claims Directive, COM 2023/166 | Legislative proposal, not law | Reference only as rules in development |
| WTTC elevating Hotel Sustainability Basics to an independent global certification scheme, adopted by 8,000+ hotels in 85 countries | Announced 25 June 2026 | Business Case risk section, comparison table |

#### Third-party recognition and standards

- GSTC-Recognized status. GSTC Industry Criteria for Hotels, Version 3. Use for the Stewardship page argument that decent work is part of the international definition of a sustainable hotel. Link to gstcouncil.org.
- Travalyst recognition. Link to travalyst.org/industry.
- Control Union, accredited Certification Body. ISO 17065 prohibits the Certification Body from providing consulting support.
- United Nations Sustainable Development Goals alignment, all 17 goals.

#### Advisory and tooling

- JLL, "Greener returns: A framework for operationalizing sustainability in existing hotel assets," 18 November 2025. Use in the asset value section.
- EPA ENERGY STAR Portfolio Manager. Free benchmarking tool for energy, water, waste, and emissions. Use in the operating cost section and the Readiness Hub. Link to energystar.gov/benchmark.

#### Optional academic footnote

Peer-reviewed findings on certified-hotel financial performance are mixed. Cornell's Center for Hospitality Research found LEED-certified hotels outperformed comparable properties on ADR and RevPAR in the period following certification, while a larger subsequent study found the RevPAR difference statistically insignificant and found Energy Star labeled properties showed consistently higher occupancy.

Use only as a footnote if a supporting citation is wanted. Never as a headline statistic, and never without the caveat that findings are mixed. The site's quantitative spine is Alo Index, Booking.com, GBTA, JLL, and the EU directive.

#### Prohibited

- Any Eco-Rating point value, section point total, or score percentage range
- Any figure not listed above
- Any estimate, projection, or savings claim attributed to Green Key Global
- Any discount percentage or negotiated rate
- Any named hotel brand, management company, or destination organization

---

### 6.2 Additional program facts

Label these "Green Key Global program data, July 2026" where a source line is shown. These are qualitative context. **Any number used on a page must still appear in Section 6.1.**

- Founded 1993 by the Hotel Association of Canada, now Hotels Canada. Became an AHLA and Hotels Canada joint venture in 2024.
- One tree is planted with One Tree Planted for every new member, a program running since 2023.
- The assessment covers five Key Performance Areas: Corporate Environmental Management, Housekeeping, Conference and Meeting Services, Food and Beverage, and Engineering and Maintenance.
- Conference and Meeting Services and Food and Beverage are optional. Opting out rescales the scoring, so a select-service property is not disadvantaged.
- The Core Criteria are the mandatory baseline and are the requirement for a first Key. The self-assessment portal includes a "Display Core Criteria Only" filter for properties prioritizing the fastest path to entry-level certification.
- Audits are conducted independently by Control Union under an ISO/IEC 17065 structure. Audit findings inform, but do not determine, the certification decision, which is made by the Certification Body.
- Rescheduling an audit requires three business days' notice for a virtual audit and twenty for an on-site audit.
- Certification is valid for three years. Membership renews annually. Recertification requires a new self-assessment, supporting documentation, and a new independent audit under the criteria in effect at that time.
- Certified properties receive a Property Performance Report identifying accomplishments and recommendations for future improvement.
- A Green Vendor Directory of vetted vendors is available to members, with member discounts. It is explicitly not a certification, is vendor-agnostic, and does not provide lead generation or take referral fees.
- Certified-property lists are shared with OTAs, government procurement officers, and RFP platforms.
- Certified members may use the Green Key name and rating only while current and in scope.

### 6.3 Contact

- Website: greenkeyglobal.com
- Sales and new business: Sales@greenkeyglobal.com
- Existing members: Green Key Global member services, through the Members Area

### 6.4 Scoring confidentiality (hard rule)

The Eco-Rating point structure is proprietary. Nothing derived from the point table may appear on this site.

**Never publish:**

- Point values for any question or answer option
- Section point totals or the total points available
- Percentages, ratios, or shares derived from the point table
- The percentage score ranges behind each Key level
- Any arithmetic that would let a reader reconstruct scoring weights

**Permitted, because these describe structure and mechanics rather than values:**

- The five Key Performance Areas by name
- That the assessment contains 200+ questions
- That Conference and Meeting Services and Food and Beverage are optional, and that opting out does not disadvantage a property
- That graduated questions award partial credit for partial coverage and the most credit for full coverage
- That certain questions are assessed separately by area, for example lighting coverage in guest rooms, public areas, and back of house
- That N/A options remove a question from scoring rather than penalizing the property
- That there are 37 mandatory Core Criteria, distributed as Corporate 15, Housekeeping 10, Engineering 12
- That every rating from 1 to 5 Keys is full certification

QA test: search built pages for "point" and "%". Every match must be either a sourced third-party statistic or a structural statement with no number attached to scoring.

---

## 7. Technical and Component Guidance

- **Components to build:** StatCard, ChecklistCard, IconCard grid, HorizontalBarChart, ColumnChart (both pure CSS or SVG, no heavy chart library needed), KeysLadder, ProcessFlow (5 steps), PhaseCards, PricingTable, ROICalculator (vanilla JS or framework state), FAQAccordion, SDGTable, ComparisonTable, FooterBand, CriteriaExplorer, ReadinessCheck.
- **Charts:** flat design, no gridlines, value labels at bar ends, source caption below in `--gk-grey` italic 12px. Colors: primary `--gk-deep`, highlight `--gk-bright`, muted `#C9CFCB`, darkest `--gk-dark`.
- **KeysLadder:** label rungs by Key level only. Do not label with score ranges or point totals.
- **Icons:** simple line or solid icons (Lucide or similar) in `--gk-deep` inside white circles with a thin deep-green ring, matching the card motif.
- **Accessibility:** semantic headings per page (one h1), alt text on all imagery, color contrast AA (never `--gk-bright` text on white for body copy; reserve it for large numerals on dark), keyboard-operable accordion, calculator, and explorer, `prefers-reduced-motion` respected.
- **SEO:** unique titles and descriptions per page, the tagline in the home title, Open Graph tags. Note that noindex is in force while the site is in draft review.
- **Performance:** static output, system-font fallback, single small CSS file, no blocking scripts except the calculator and the interactive tools.
- **No CMS needed.** Content lives in the repo. Keep copy in easily editable files (markdown or JSON) so future edits are diffs. The Core Criteria Explorer reads from `data/core-criteria.json`.
- **Interactive tools** must be client-side only. No backend, no data persistence, no browser storage.

---

## 8. QA Checklist (run before finishing)

**Content and accuracy**

- [ ] Zero em dashes and en dashes in rendered output (grep the build for the characters)
- [ ] Every statistic shows its source on the page where it appears
- [ ] Every figure on every page appears in Section 6.1
- [ ] Calculator matches the Section 5.8 formulas exactly. Defaults produce: cost per property per year $916.67, cohort per year $4,583.33, under $80 per month, break-even approximately 6.3 room nights, conservative net benefit approximately $31,239
- [ ] Pricing table matches Section 5.8 exactly, disclaimer present
- [ ] No discount percentages stated anywhere
- [ ] "Any rating is full certification" appears in the ratings section
- [ ] ECGT accuracy: Directive (EU) 2024/825 cited with the 27 September 2026 date. The Green Claims proposal, if mentioned, is clearly identified as not law
- [ ] Third-party research is linked to the original publisher, not hosted in the repo
- [ ] No hotel brand names, management company names, or destination organization names anywhere

**Scoring confidentiality**

- [ ] Grep built output for "point", "points", "pts". Every match is a structural statement with no number attached to scoring
- [ ] Grep for "%". Every match is a sourced third-party statistic, never a section weight, tier value, or Key rating band
- [ ] The percentage ranges behind each Key level appear nowhere
- [ ] The KeysLadder component labels rungs by Key level only
- [ ] No graphic or caption expresses the Core Criteria as a share of a total question count

**Contact and draft protection**

- [ ] Grep for "info@". Zero matches. Every mailto is Sales@greenkeyglobal.com
- [ ] Every page has `<meta name="robots" content="noindex, nofollow">`
- [ ] robots.txt disallows all crawling

**Structure**

- [ ] Every nav and footer link resolves. No orphan pages
- [ ] Owner pages and Readiness Hub pages are visually distinct and correctly cross-linked
- [ ] Self-Check and Core Criteria Explorer are client-side only, store no data, and use no browser storage
- [ ] Footer carries the July 2026 note, the confirm-at-greenkeyglobal.com line, and source links
- [ ] Lighthouse 90+ across performance, accessibility, best practices, and SEO
