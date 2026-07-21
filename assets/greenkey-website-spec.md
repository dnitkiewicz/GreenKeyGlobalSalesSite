# Green Key Global: Eco-Rating Certification Website Spec

This file is the single source of truth for building a marketing/education website from the Green Key Global sales kit. It contains the complete content, data, brand system, and build guidance. Everything a coding agent needs is in this file; do not invent statistics, pricing, or claims beyond what is written here.

**Working title:** A Hotel's Roadmap to Eco-Rating Certification
**Audience:** Hotel GMs, Directors of Operations at management companies, owners, and hotel department heads
**Goal:** Make the case for Green Key Eco-Rating certification and convert visitors to (a) a contact/demo request, (b) an ROI calculation, or (c) a pilot conversation

---

## 1. How to Use This File (instructions for Claude Code)

1. Build a static, fast, accessible multi-page site (Astro, Next.js static export, or plain HTML/CSS/JS all acceptable; prefer whatever produces the smallest, fastest output).
2. Use the content blocks in Section 5 verbatim or lightly adapted; use the data registry in Section 6 for every number.
3. Follow the brand system in Section 3 exactly.
4. Every statistic rendered on any page must display its source, either inline in small text or as a footnote at the bottom of the section. Sources are listed with each stat in Section 6.1.
5. Respect the hard writing rules in Section 3.4 (notably: no em dashes anywhere).
6. Build the interactive ROI calculator per the formulas in Section 5.5. All math is defined; do not change the formulas or defaults.
7. Include a "last updated July 2026" note in the footer and a disclaimer that pricing and program details should be confirmed at greenkeyglobal.com.

---

## 2. Positioning Summary

- Tagline (use as the site subtitle): **"The Leading North American Standard in Sustainable Hospitality Certification"**
- Voice: Green Key Global speaking in first person plural ("we certify operations, not construction").
- Core narrative: every hotel is being asked to prove, credibly, how it operates. Certification is that proof. It was built by hoteliers for hoteliers, requires no capital spend, is independently audited, is priced for every market tier, and demonstrably drives corporate business.
- Political neutrality: the case is framed on business outcomes (revenue, cost, operations, risk, marketing), never ideology. A property can lead with the environmental story or the cost-discipline story; both describe the same certification honestly.

---

## 3. Brand System

### 3.1 Colors
| Token | Hex | Use |
|---|---|---|
| `--gk-deep` | `#196B24` | Primary green: buttons, headings accents, solid blocks, chart primary |
| `--gk-bright` | `#92D050` | Accent green: numerals, highlights, hover states |
| `--gk-band` | `#8CC642` | Footer band / section dividers |
| `--gk-dark` | `#14402A` | Dark surfaces, hero backgrounds, deepest chart shade |
| `--gk-pantone356` | `#007A33` | Alternate brand green (links, secondary accents) |
| `--gk-pale` | `#F2F8EC` | Card and section tint backgrounds |
| `--gk-ink` | `#1A1A1A` | Headings text |
| `--gk-body` | `#222222` | Body text |
| `--gk-grey` | `#595959` | Captions, source lines |

### 3.2 Typography
- Headings: **Montserrat** (bold; section titles may be ALL CAPS per the deck style)
- Body: **Helvetica, Arial, sans-serif** (brand web-friendly font)
- Footer wordmark line: Montserrat Light, letter-spaced: `GREENKEYGLOBAL.COM`
- Load Montserrat from Google Fonts; Helvetica falls back to Arial.

### 3.3 Visual motifs
- White backgrounds; pale green (`--gk-pale`) rounded cards (radius ~12px) for feature grids
- A light-green full-width footer band (`--gk-band`) with `GREENKEYGLOBAL.COM` right-aligned in white
- Big stat callouts: huge Montserrat bold number in `--gk-deep` over small caption
- Keys ladder: 5 ascending blocks shaded light-to-dark green
- Charts: flat bars, no gridlines, value labels on bars, source line beneath

### 3.4 Hard writing rules
- **No em dashes ("—") or en dashes ("–") anywhere.** Use commas, colons, parentheses, or "to" in ranges.
- Third-party facts always carry their named source (see 6.1). Program facts may be labeled "Green Key Global program data, 2026."
- Never state or imply a specific partnership discount percentage; say "portfolio agreements improve on list pricing."
- Do not reproduce content from other organizations beyond the short attributed stats listed here.
- Any rating from 1 to 5 Keys is described as "full certification."

---

## 4. Site Architecture

```
/                     Home (the case at a glance)
/why-certify          The business case (demand, Alo evidence, cost/risk/asset value)
/how-it-works         Assessment, Core Criteria, process, ratings
/pricing              Published pricing + ROI calculator
/partners             For brands & management companies (portfolio partnership)
/get-started          90-day roadmap + department guide + CTA
/faq                  Objections answered
/about                Who we are + recognitions + SDG alignment (appendix content)
```

Global nav: Why Certify · How It Works · Pricing · Partners · Get Started · FAQ
Global CTA button (persistent, `--gk-deep`): **"Start the Conversation"** -> mailto:info@greenkeyglobal.com (or a contact form)
Footer: band graphic, GREENKEYGLOBAL.COM, contact email, "Pricing and program details current as of July 2026; confirm at greenkeyglobal.com," and a link list of third-party sources.

---

## 5. Page Content

### 5.1 Home `/`

**Hero (dark `--gk-dark` background, white text):**
- H1: `A Hotel's Roadmap to Eco-Rating Certification`
- Subtitle (italic, `--gk-bright`): `The Leading North American Standard in Sustainable Hospitality Certification`
- Supporting line: `Why certification matters, how our program works, and how any property can get there.`
- CTA buttons: `Start the Conversation` (primary), `See How It Works` (ghost, links /how-it-works)

**Section: The question every hotel gets asked** (4 cards on pale tint):
1. **Corporate RFPs** - Travel buyers ask for recognized certification before shortlisting your property
2. **Booking platforms** - OTAs ask for third-party verification before showing a sustainability badge
3. **Brand standards** - Flags are adding certification to brand requirements
4. **The utility line** - Owners ask why energy, water, and waste costs keep climbing

Closing line: `It is always the same question underneath: ` **`can this hotel prove, credibly, how it operates?`**

**Section: Stat band** (4 big-number cards):
- `3,000+` certified properties across North America
- `3x` the corporate room nights at certified hotels *(source: Alo Index, see 6.1)*
- `~11 days` average to complete the Core Criteria assessment
- `<$80/mo` published U.S. cost across a 3-year cycle
Caption: "Corporate room-night figure: Alo Index, analysis of 5,082 assessed hotels, 2025 full year. Other figures: Green Key Global program data and published pricing, July 2026."

**Section: Why this program, in five points** (checklist card):
1. **Built by the industry.** Founded in 1993 and jointly owned by the American Hotel & Lodging Association and Hotels Canada.
2. **No capital spend required to certify.** The assessment scores what a property already does and recommends improvement over time.
3. **A trusted benchmark.** Aligned with all 17 UN Sustainable Development Goals, GSTC-Recognized, recognized by Travalyst, and verified by an independent third-party auditor.
4. **A clear front door.** The 2026 Core Criteria define 37 mandatory questions as the path to a first Key, cutting average completion from about 80 days to about 11.
5. **Priced for every tier.** Published U.S. pricing works out to under $80 per month across a full three-year cycle.

**Section: teaser row** linking to /why-certify, /how-it-works, /partners.

### 5.2 Why Certify `/why-certify`

**Intro:** We built this program around business outcomes: revenue, cost, operations, risk, and marketing. The math is plain: for most properties, three extra bookings in a year covers the cost of certification; every booking after that is positive return.

**Chart 1: "The demand for certified sustainability is measurable"** (horizontal bars, values labeled with %):
| Value | Label | Source tag on bar |
|---|---|---|
| 90 | Consumers who look for sustainable options when traveling | Expedia Group, 2022 |
| 83 | Global travelers who say sustainable travel is vital | Booking.com, 2021 |
| 76 | Travel buyers adding sustainability clauses to supplier contracts | GBTA Foundation, 2023 |

**Chart 2: "Certified hotels win more corporate business"** (column chart + 2 callout cards):
- Columns: average corporate room nights per hotel by Alo score band (2025): Score 0 = 126, Score 1-60 = 134, Score 61-80 = 484, Score 81-100 = 1,189. Shade the top two bands bright/deep green, others grey `#C9CFCB`.
- Callout card A: **3x** the corporate room nights at certified hotels: 622 per year versus 202 at non-certified
- Callout card B (dark): **97% vs 70%** certified hotels that won corporate business, versus non-certified
- Source line: `Source: Alo Index, analysis of 5,082 assessed hotels, 2025 full year. Green Key Global partnered with the Alo Index in 2026.`
- Copy note: Expedia's research has also linked certification to guest satisfaction, reporting a 15% increase in positive guest reviews at certified luxury properties (Expedia Group, 2022).

**Section: Cost, risk, and asset value:**
- The practices the assessment rewards are the same practices that cut spend: metering utilities, preventative maintenance, sealing the building envelope, efficient lighting, water-wise housekeeping, right-sized food purchasing. The assessment is largely not asking a hotel to spend money on sustainability; it is asking it to stop spending money on waste.
- JLL's analysis of existing hotel assets reaches the same conclusion from the owner's chair: hotels that embed sustainability into capital planning see reduced operating costs, improved access to green financing, enhanced brand equity, and lower regulatory and reputational exposure (JLL, November 2025).

**Section: Where the industry is heading** (3 cards, middle one dark):
1. **WTTC**: elevating Hotel Sustainability Basics, adopted by 8,000+ hotels in 85 countries, into an independent third-party certification scheme (WTTC, 25 June 2026)
2. **EU regulation**: the Empowering Consumers for the Green Transition Directive takes force September 2026: sustainability labels shown to EU travelers require independent verification (Directive (EU) 2024/825)
3. **Owners' advisors**: JLL: embedded sustainability now means lower operating costs, green financing access, brand equity, and lower regulatory risk (JLL, November 2025)
Closing line: `Eco-Rating is this model, built for North America, with a two-decade head start with the buyers who matter here.`

**Comparison table (Eco-Rating vs WTTC Basics)** with note: "The two programs are complementary rather than competing: Basics defines a global floor, while Eco-Rating provides the comprehensive, North America-focused certification a property can grow with."
| | Green Key Eco-Rating | WTTC Hotel Sustainability Basics |
|---|---|---|
| Scope | Comprehensive: 200+ operational questions across five hotel departments | Entry-level: 12 fundamental actions |
| Depth of rating | Graduated 1 to 5 Keys, room to grow for a decade | Verified baseline (phased over 3 years) |
| Market focus | North America; OTA, RFP, and brand integration here | Global framework |
| Governance | Owned by AHLA and Hotels Canada; independent audit by Control Union | WTTC initiative; certification transition underway |
| Recognition | GSTC-Recognized standard; Travalyst; SDG-aligned | Aligning to GSTC Accreditation Framework and EU rules |

### 5.3 How It Works `/how-it-works`

**Section: Inside the assessment (Five Key Performance Areas)** (5 cards):
| KPA | Covers | Applies to |
|---|---|---|
| Corporate Environmental Management | Policy, action plan, responsible purchasing, Green Team, staff and guest engagement, community involvement | All properties |
| Housekeeping | Linen reuse, cleaning products, energy- and water-conscious room routines, training | All properties |
| Engineering | Utility tracking, preventative maintenance, HVAC, insulation, lighting, fixtures, waste, renewables | All properties |
| Food & Beverage | Purchasing, food waste reduction, refrigeration monitoring, service practices | Optional; opt out if not applicable |
| Conference & Meetings | Event-space sustainability practices | Optional; opt out if not applicable |

Copy: 200+ questions, multiple users, save as you go, templates for every required document, and evidence uploaded against each mandatory answer so the audit verifies proof, not promises. Opted-out sections rescale the score with no penalty.

**Section: The 37 Core Criteria** (donut graphic: 37 of 213 highlighted; bar mini-chart: Corporate 15, Housekeeping 10, Engineering 12):
- In early 2026 we defined the program's baseline: 37 mandatory questions constitute the minimum for a 1-Key certification. A "Display Core Criteria Only" filter isolates them in the portal.
- Speed stats: average completion fell from about 80 days to about 11; the focused assessment itself takes roughly 4 to 6 hours of work. (Green Key Global program data, 2026)
- The plain-terms summary (6 items): **Govern it** (signed policy, named accountable manager, action plan reviewed within the year) · **Buy responsibly** (written purchasing policy: local, recycled, eco-certified priorities) · **Staff it** (Green Team with written mandate, quarterly meetings) · **Train for it** (linen reuse program; thermostat set-points; housekeeping routines; safe handling of cleaning and medical waste) · **Measure it** (12 months of utility data; written preventative maintenance; HVAC checks; fixture coverage reporting) · **Prove it** (evidence uploaded for every mandatory answer; templates provided).
- Kicker: Under ISO/IEC 17065, a credible certification cannot rest on a hotel's word alone; it has to show its work.

**Section: The process** (5-step flow; step 3 visually emphasized dark):
1. **Assess** - online self-assessment, multiple users, save as you go
2. **Evaluate** - preliminary rating and gap scorecard; retake freely (the preliminary rating may not be represented publicly as certification)
3. **Audit** - independent verification by Control Union
4. **Certify** - 1 to 5 Keys, valid three years, Property Performance Report
5. **Market** - toolkit, OTA badges, RFP content, plaque

**Impartial by design box:** We set the standard but never audit our own members. Audits are conducted by Control Union, an independent global inspection firm, and the certification decision rests with an independent Certification Body, per ISO/IEC 17065. Audits typically commence within ~90 days of request. Rescheduling requires three business days' notice (virtual) or twenty (on-site). A property that stops meeting requirements is subject to corrective action, suspension, or revocation: a label that can never be withdrawn is not a certification.

**Section: The rating** (ascending 5-block ladder):
| Rating | Share of available points |
|---|---|
| 1 Key | 1% to 19% (all 37 Core Criteria met) |
| 2 Keys | 20% to 39.9% |
| 3 Keys | 40% to 59.9% |
| 4 Keys | 60% to 79.9% |
| 5 Keys | 80% to 100% |
Copy: Any rating is full certification. The audit-issued Property Performance Report shows exactly where the points for the next Key live, turning "improve our rating" into an assignable plan across three-year cycles. Members renew membership annually; at the end of three years the property recertifies against the then-current criteria.

**Section: After you're certified** (4 cards):
1. **Marketing Toolkit** - logos, website copy, in-room and event collateral, RFP response content, staff checklists
2. **Automatic distribution** - certified-property lists shared with OTAs, procurement officers, and RFP platforms
3. **Property Performance Report** - property-specific roadmap showing where the points for the next Key live
4. **Green Vendor Directory** - 75+ vetted sustainability suppliers with exclusive member discounts; strictly vendor-agnostic (we do not certify, endorse, or take referral fees from vendors)
Claims note: certified members may use the Green Key name and rating only while current and in scope.

### 5.4 Pricing `/pricing`

**Published pricing table (July 2026):**
| Item | United States | Canada |
|---|---|---|
| Annual membership, per property | $750 / year | $950 CAD / year |
| Virtual audit, once per 3-year cycle | $500 | $500 |
| On-site audit (optional alternative) | $2,500* | $2,500* |
| Additional audits (if required) | $500 | $500 |

*Travel dependent. Fees are non-refundable except in exceptional circumstances. Fees reviewed periodically; current pricing at greenkeyglobal.com.

**Callout cards:** `<$80/month` (full 3-year U.S. cycle: $2,750 all-in with a virtual audit) · `3 bookings` (in a year covers the cost of certification; the rest is return)

**Partnership note:** List pricing is the ceiling, not the expectation, for groups. Portfolio agreements (MSAs for brands, MOUs for management companies) carry negotiated per-property rates, coordinated onboarding, and fast-track pathways. Link to /partners.

### 5.5 ROI Calculator (interactive component on /pricing)

Inputs (with defaults; all editable):
| Input | Default | Notes shown to user |
|---|---|---|
| `props` Number of properties | 5 | Start with a pilot cohort |
| `adr` Average daily rate | $145 | Blended across the cohort |
| `rn` Current corporate room nights per property per year | 202 | Default = Alo Index average for non-certified hotels (2025); replace with your own |
| `util` Annual utility spend per property | $190,000 | From your P&L |
| `member` Annual membership per property | $750 | Published list, US$ |
| `audit` Virtual audit per property per 3-year cycle | $500 | Published list |
| `disc` Partnership discount | 0% | Leave 0% until a term sheet exists |
| `liftC` Conservative lift | 5% | Far below the Alo-observed gap |
| `liftM` Moderate lift | 15% | Assumes badges live and RFP usage |
| `liftS` Strong lift | 40% | Still well under the 3x (200%) observed gap; correlation, not a promise |
| `save` Utility savings | 3% | Low-single-digit O&M savings; adjust to experience |

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
Render results for Conservative / Moderate / Strong side by side, plus break-even RNs and cost per month. Required disclaimers under the calculator: "Illustrative planning tool, not a forecast or commitment. Revenue figures are room revenue, not profit; apply your own flow-through." Show sources: Alo Index (5,082 hotels, 2025); greenkeyglobal.com pricing (July 2026).

### 5.6 Partners `/partners`

**Intro:** For brands and management companies, certification is structured as a partnership: a formal membership commitment across your portfolio in exchange for preferred pricing and dedicated support.

**What a formal partnership includes** (6 cards):
1. **Preferred pricing** - a membership commitment across your portfolio in exchange for discounted certification fees under an MSA or MOU
2. **Dedicated Account Manager** - a named owner of your partnership from activation onward: rollout support, troubleshooting, best-practice guidance
3. **Structured activation** - a joint kickoff with your team, a year-one engagement plan, promo codes, and enrollment workflows configured for your properties
4. **Co-marketing launch** - a joint launch plan with agreed messaging across PR, web, social, and email, supported by our templates
5. **Quarterly reporting** - partnership progress reports tracking certification, participation, and impact against agreed targets
6. **Fast-track equivalencies** - where a brand program equivalency exists, work your properties have already done is credited toward certification

**The partnership journey** (4 numbered phases, big bright-green numerals):
1. **Explore & Agree** - discovery of your portfolio goals and timelines; tailored proposal and term sheet; MSA or MOU with negotiated rates
2. **Onboard** - activation meeting with your team; dedicated Account Manager assigned; promo codes, workflows, co-marketing launch
3. **Execute** - property rollout and certification support; best-practice guidance on demand; quarterly and annual progress reports
4. **Grow & Renew** - annual review against agreed targets; expansion across the portfolio; renewal on proven results

Closing: If your flags or group already hold an agreement with us, your properties may have simplified enrollment waiting. Ask before enrolling individually.

### 5.7 Get Started `/get-started`

**The 90-day path** (3 phase cards):
- **Days 1-30: Foundation** - Name the accountable senior officer. Form the Green Team with a written mandate and quarterly meetings on the calendar. Request 12 months of utility invoices (electricity, gas, water). Download our templates for the sustainability policy, action plan, purchasing policy, and Green Team mandate.
- **Days 31-60: Close the gaps** - Launch the linen and towel reuse program. Put the preventative maintenance program in writing. Standardize thermostat set-points and add the trained behaviors to housekeeping checklists. Finalize and sign the purchasing policy. Document fixture coverage and any F&B monitoring logs.
- **Days 61-90: Assess and request audit** - Complete the self-assessment using the Core Criteria filter first. Upload every required document. Run a cross-department consistency check (the assessment locks once the audit is requested). Choose virtual or on-site audit and request it through the Members Area.

**What each department will be asked to do** (table; nothing requires a budget line to start):
| Team | Day-to-day contribution |
|---|---|
| Housekeeping | Run the linen reuse program. Clean by natural light where possible, manage blinds with heating and cooling needs, keep windows and doors closed while systems run, switch off lights and TVs in empty rooms, minimize water while cleaning, report faulty equipment right away. |
| Engineering / Maintenance | Keep utility bills organized and tracked. Follow the written preventative maintenance schedule for HVAC, ventilation, plumbing, and lighting. Log fixture coverage and efficiency upgrades. |
| Front Office / Admin | Email guest folios instead of printing. Default to double-sided printing. Help communicate the sustainability policy to staff and guests. |
| Food & Beverage (if applicable) | Keep freezer and thawing logs. Practice first-in-first-out and right-sized ordering. Separate organics where service exists; log surplus food donations. |
| General Manager | Sign and endorse the policy, sponsor the Green Team, keep the quarterly meeting cadence real: the audit checks for evidence of meetings, not just a signed document. |

**Closing block + CTA:** We never ask a property to be something it is not. We ask a hotel to run well, prove it, and be recognized for it: by a standard hoteliers built, anchored to goals the whole world has agreed on, verified by an auditor no one can lean on, at a price every tier of the market can carry. → `Start the Conversation` (info@greenkeyglobal.com | greenkeyglobal.com)

### 5.8 FAQ `/faq` (accordion; adapted from objection handling)

1. **Is there a budget case for this?** Under $80 a month per property at list, less under a portfolio agreement, and no capital spend is required to certify. Three extra bookings a year covers it, and the practices it rewards cut the utility line.
2. **Sustainability doesn't sell in our market. Why certify?** Then lead with operations and revenue: corporate RFP eligibility, OTA badges, and a 3x corporate room-night gap (Alo Index) are market-neutral. The certification works whether a property leads with the environmental story or the cost-discipline story.
3. **We don't have a sustainability person.** The assessment is organized by department; the GM, executive housekeeper, and chief engineer already own the answers. The Core Criteria take 4 to 6 hours of focused work, with templates for every required document.
4. **We're already in a brand program.** AHLA co-owns Green Key, and brand programs feed in: where an equivalency exists, work already done is credited. Ask before assuming you start from zero.
5. **What if we fail the audit?** You cannot be surprised by it. The self-assessment produces a preliminary rating and gap scorecard first and can be retaken freely; nothing locks until you request the audit.
6. **Is this just a badge?** We never audit our own members. Control Union verifies evidence independently, the decision sits with an independent Certification Body under ISO/IEC 17065, and certification can be suspended or revoked.
7. **Our owners only care about NOI.** JLL's guidance to owners: embedded sustainability means lower operating costs, better access to green financing, and lower regulatory exposure. Add utility savings and this is an NOI conversation.
8. **We looked at LEED; too expensive.** Different animal. LEED certifies how a building was constructed; we certify how a hotel operates. No construction, no retrofit requirement, no capital gate.
9. **Timing is bad.** Average completion is about 11 days, the focused work is hours not weeks, and the portal saves progress across multiple users. A pilot cohort fits inside one quarter.
10. **Which properties qualify?** All of them. Select-service properties opt out of F&B and conference sections with no scoring penalty, and any rating from 1 to 5 Keys is full certification.
11. **Hidden costs at renewal?** None to hide: flat published fees, membership renewed annually, one audit per three-year cycle, recertification on the same terms.

### 5.9 About `/about`

**Who we are:** Green Key began in 1993, created by the Hotel Association of Canada (now Hotels Canada). In 2024, the American Hotel & Lodging Association and Hotels Canada formed the joint venture that is Green Key Global today: the leading hotel sustainability certification program in North America, with more than 3,000 certified properties. We certify operations, not construction. In partnership with One Tree Planted, a tree is planted for every new member: more than 13,000 trees since 2023.

**Recognitions** (badge row):
- **United Nations SDGs** - aligned with all 17 Sustainable Development Goals
- **GSTC-Recognized** - standard recognized by the Global Sustainable Tourism Council
- **Travalyst** - recognized by the coalition behind sustainability labels on major booking platforms
- **ISO-aligned, EU-ready** - certification structured around ISO/IEC 17065; compliant architecture for Directive (EU) 2024/825 (in force 27 September 2026)

**SDG mapping table** (all 17; how a hotel contributes):
| # | Goal | How a hotel contributes |
|---|---|---|
| 1 | No Poverty | Hotel jobs and local purchasing keep income in the communities where properties operate. |
| 2 | Zero Hunger | Food waste reduction and surplus food donation put edible food to use instead of landfill. |
| 3 | Good Health and Well-Being | Safer cleaning products, air quality, and proper hazardous waste handling protect guests and staff. |
| 4 | Quality Education | Staff sustainability training builds transferable skills across every department. |
| 5 | Gender Equality | Hospitality is a major employer of women; equitable practice turns jobs into careers. |
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

Note under table: Four operational areas do an outsized share of the work: Energy advances SDG 7 and 13; Water advances SDG 6; Food Waste advances SDG 2 and 12; Procurement advances SDG 8 and 12.

**Glossary** (definition list): Core Criteria (the 37 mandatory questions forming the 1-Key baseline) · KPA (one of five assessment sections) · Scheme Owner (Green Key Global: develops the standard, does not audit) · Certification Body (independent decision-maker) · Audit Body / Control Union (independent third-party audit firm) · ISO/IEC 17065 (international standard for certification bodies) · ISO 14001 (environmental management systems standard) · GSTC (Global Sustainable Tourism Council) · Travalyst (sustainable-travel coalition behind booking-platform labels) · Green Team (mandatory cross-department group, written mandate, quarterly meetings) · MSA / MOU (portfolio agreements for brands / management companies) · OTA (online travel agency) · Property Performance Report (audit-issued improvement roadmap) · Sub-metering (separate meters for detailed tracking).

---

## 6. Data Registry (single source of truth for every number)

### 6.1 Third-party statistics (must display source)
| Stat | Value | Source (display exactly) |
|---|---|---|
| Consumers looking for sustainable travel options | 90% | Expedia Group, Sustainable Travel Study (2022) |
| Certified luxury properties, increase in positive guest reviews | 15% | Expedia Group, Sustainable Travel Study (2022) |
| Global travelers who say sustainable travel is vital | 83% | Booking.com, Sustainable Travel Report (2021) |
| Travel buyers adding sustainability clauses to contracts | 76% | GBTA Foundation, The State of Climate Action in Business Travel (2023) |
| Corporate room nights, certified vs non-certified | 622 vs 202 (3x) | Alo Index, analysis of 5,082 assessed hotels, 2025 full year |
| Certified vs non-certified hotels winning corporate business | 97% vs 70% | Alo Index, 2025 (as above) |
| Room nights by Alo score band | 126 / 134 / 484 / 1,189 | Alo Index, 2025 (as above) |
| Hotels in WTTC Basics program | 8,000+ in 85 countries | WTTC, 25 June 2026 press release |
| EU green-claims directive in force | 27 September 2026 | Directive (EU) 2024/825 |
| Owner payoffs of embedded sustainability | qualitative | JLL, "Greener returns," 18 November 2025 |

### 6.2 Program facts (label "Green Key Global program data" where a source line is shown)
- Founded 1993 (Hotel Association of Canada, now Hotels Canada); 2024 AHLA + Hotels Canada joint venture
- 3,000+ certified properties across North America
- 13,000+ trees planted with One Tree Planted (one per new member, since 2023)
- Assessment: 200+ questions across 5 KPAs; Core Criteria = 37 mandatory (Corporate 15, Housekeeping 10, Engineering 12)
- Completion: ~80 days before Core Criteria redesign, ~11 days after; focused work 4 to 6 hours
- Audit: independent, by Control Union; certification decision by independent Certification Body; ISO/IEC 17065 structure; audits typically commence within ~90 days of request; reschedule notice 3 business days (virtual) / 20 (on-site)
- Rating: 1 to 5 Keys, valid 3 years; bands 1-19 / 20-39.9 / 40-59.9 / 60-79.9 / 80-100% of points; 1 Key also requires all 37 Core Criteria; annual membership renewal; recertification each 3-year cycle
- Pricing (July 2026): US $750/yr membership, $500 virtual audit per cycle, $2,500 on-site (travel dependent), $500 additional audits; Canada $950 CAD/yr membership; 3-yr US cycle $2,750 (<$80/month)
- Vendor Program: 75+ vetted vendors; Approved tier $500/yr, Preferred tier $2,000/yr; explicitly not a certification, vendor-agnostic, no lead generation; member discounts available
- Distribution: certified-property lists shared automatically with OTAs, government procurement officers, RFP platforms

### 6.3 Contact
- Website: greenkeyglobal.com · Email: info@greenkeyglobal.com

---

## 7. Technical & Component Guidance

- **Components to build:** StatCard, ChecklistCard, IconCard grid, HorizontalBarChart, ColumnChart (both pure CSS/SVG, no heavy chart lib needed), DonutStat (37 of 213), KeysLadder, ProcessFlow (5 steps), PhaseCards, PricingTable, ROICalculator (vanilla JS or framework state), FAQAccordion, SDGTable, FooterBand.
- **Charts:** flat design, no gridlines, value labels at bar ends, source caption below in `--gk-grey` italic 12px. Colors: primary `--gk-deep`, highlight `--gk-bright`, muted `#C9CFCB`, darkest `--gk-dark`.
- **Icons:** simple line/solid icons (Lucide or similar) in `--gk-deep` inside white circles with a thin deep-green ring, matching the card motif.
- **Accessibility:** semantic headings per page (one h1), alt text on all decorative-free imagery, color-contrast AA (never `--gk-bright` text on white for body copy; reserve it for large numerals on dark), keyboard-operable accordion and calculator, `prefers-reduced-motion` respected.
- **SEO:** unique titles/descriptions per page; the tagline in the home title; Open Graph tags.
- **Performance:** static output, system-font fallback, single small CSS file, no blocking scripts except the calculator.
- **No CMS needed;** content lives in the repo. Keep copy in easily editable files (markdown/JSON) so future edits are diffs.

## 8. QA Checklist (run before finishing)

- [ ] Zero em dashes and en dashes in rendered output (`grep` the build for `—` and `–`)
- [ ] Every stat from 6.1 shows its source on the page where it appears
- [ ] Calculator matches formulas exactly; defaults produce: cost/prop/yr $916.67, cohort/yr $4,583.33, <$80/mo, break-even ~6.3 RNs, conservative net benefit ~$31,239 at defaults
- [ ] Pricing table matches Section 5.4 exactly; disclaimer present
- [ ] No discount percentages stated anywhere
- [ ] "Any rating is full certification" appears on the ratings section
- [ ] Footer: July 2026 note + confirm-at-greenkeyglobal.com line + source links
- [ ] Lighthouse: 90+ across performance/accessibility/best practices/SEO
