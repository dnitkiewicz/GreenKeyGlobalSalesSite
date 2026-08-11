# CLAUDE.md — Project Rules for the Green Key Global Sales Site

This file is read automatically by Claude Code at the start of every session. Follow these rules on every edit to this repository without being reminded.

## What this project is
A static marketing and education microsite making the case for Green Key Global's Eco-Rating certification, aimed at hotel GMs, Directors of Operations at management companies, owners, and hotel department heads. It is published via GitHub Pages. The full content, data, and design source of truth is `assets/greenkey-website-spec.md`. When in doubt about content, wording, numbers, or layout, read that spec before acting.

## Non-negotiable content rules
1. **No em dashes ("—") or en dashes ("–") anywhere** in any file that produces visible text. Use commas, colons, parentheses, or the word "to" in ranges (for example "1 to 5 Keys", "40 to 60%").
2. **Every statistic must show its named source** on the page where it appears (for example "Alo Index, 2025" or "Expedia Group, 2022"). Never display a number from the data registry without its source line. Sources are listed in section 6.1 of the spec.
3. **Never state or imply a specific partnership discount percentage.** The correct phrasing is "portfolio agreements improve on list pricing." Discounts are set in a term sheet, never on the website.
4. **Do not invent facts, statistics, pricing, or claims.** Use only what is in `assets/greenkey-website-spec.md`. If a number is not in the spec or the existing site, do not add it; ask first.
5. **Any Key rating (1 through 5) is described as "full certification."** Higher Keys reflect a higher share of points, earned over time.
6. Keep the first-person Green Key Global voice ("we certify operations, not construction").
7. Frame the case on business outcomes (revenue, cost, operations, risk, marketing), never on ideology or politics.

## Brand system (use these exact values)
Colors (CSS variables already defined in styles.css):
- `--gk-deep` `#196B24` — primary green: buttons, chart bars, heading accents
- `--gk-bright` `#92D050` — accent green: numerals, highlights (never as body text on white; contrast is too low)
- `--gk-band` `#8CC642` — footer band / dividers
- `--gk-dark` `#14402A` — dark surfaces, deepest chart shade
- `--gk-pale` `#F2F8EC` — card and section tint backgrounds
- `--gk-ink` `#1A1A1A` — heading text
- `--gk-body` `#222222` — body text
- `--gk-grey` `#595959` — captions and source lines

Fonts: Montserrat for headings (bold, sometimes ALL CAPS), Helvetica/Arial for body. Charts are flat: no gridlines, value labels on the bars, source caption beneath in grey italic.

## Pricing (published, July 2026 — do not alter without being asked)
- US membership $750/year per property; Canada $950 CAD/year
- Virtual audit $500 once per 3-year cycle; on-site audit $2,500 (travel dependent); additional audits $500
- Full 3-year US cycle $2,750, which is under $80/month
Always keep the footer disclaimer that pricing and program details should be confirmed at greenkeyglobal.com.

## The ROI calculator (pricing.html + site.js)
The calculation logic is correct and matches spec section 5.5. **Do not change the formulas or default values** unless explicitly asked. Defaults must keep producing: cost per property per year $916.67, cohort per year $4,583.33, under $80/month, break-even about 6.3 room nights, conservative net benefit about $31,239. If you touch this file, re-verify these numbers before finishing.

## Working style in this repo
- Before editing, read the relevant file and `assets/greenkey-website-spec.md`.
- Make small, focused changes and show diffs before writing.
- After any visual change, render the affected page headlessly and confirm it looks right before saying it is done.
- Preserve all existing source-note lines and citations; never delete a source.
- After a change is approved and verified, offer to commit and push with a clear message.

## QA checklist before committing
- [ ] No em dashes or en dashes in changed files (grep for "—" and "–")
- [ ] Every stat still shows its source
- [ ] No discount percentage stated anywhere
- [ ] Pricing table and calculator defaults unchanged (unless the change was requested)
- [ ] Affected pages render correctly (charts show as bars, calculator responds)
- [ ] Footer keeps the "confirm at greenkeyglobal.com" note
---

## Audience and purpose

This site makes the case for Green Key Global Eco-Rating certification to **hotel owners and
capital allocators**: ownership groups, asset managers, CRE investors, private equity, and lenders.
General managers and management companies execute certification but do not approve capital, so the
primary argument must be written for the person who signs the checks.

A secondary track (the Readiness Hub) serves the operator who has to run the process after the
owner says yes. Keep the two tracks visually and structurally distinct.

## Contact and calls to action

- Every CTA, mailto link, nav button, and footer contact uses **Sales@greenkeyglobal.com**.
- Never use info@greenkeyglobal.com anywhere on this site.
- Readiness Hub pages may additionally direct existing members to the Members Area and to
  Green Key Global member services, but the sales CTA remains Sales@greenkeyglobal.com.

## Scoring confidentiality (hard rule)

The Eco-Rating point structure is proprietary. Nothing derived from the point table may appear
on this site.

Never publish:
- Point values for any question or answer option
- Section point totals or the total points available
- Percentages, ratios, or shares derived from the point table
- The percentage score ranges behind each Key level
- Any arithmetic that would let a reader reconstruct scoring weights

Permitted, because these describe structure and mechanics rather than values:
- The five Key Performance Areas by name
- That Conference and Meeting Services and Food and Beverage are optional, and that opting out
  does not disadvantage a property
- That graduated questions award partial credit for partial coverage and the most credit for
  full coverage
- That certain questions are scored separately by area (for example, lighting coverage in
  guest rooms, public areas, and back of house)
- That N/A options remove a question from scoring rather than penalizing the property
- That there are 37 mandatory Core Criteria, and how they are distributed across Corporate,
  Housekeeping, and Engineering by name
- That every rating from 1 to 5 Keys is full certification

QA test: search built pages for "point" and "%" . Every match must be either a sourced
third-party statistic or a structural statement with no number attached to scoring.

## Sourcing

- Every statistic on a page must show its source on that page, inline or as a footnote.
- Use only statistics listed in Section 6.1 of greenkey-website-spec.md. Do not introduce new
  figures, do not estimate, do not round from memory.
- Link third-party research to the original publisher URL. Do not host third-party PDFs in
  this repo.

## Regulatory accuracy

- The EU Empowering Consumers for the Green Transition Directive is **Directive (EU) 2024/825**,
  in force **27 September 2026**. This is the directive to cite as a compliance date.
- The **Green Claims Directive (COM 2023/166)** is a separate legislative proposal and is not
  law. Reference it only as further EU rules in development, never as an in-force requirement.
- Never merge the two into a single claim.

## Content boundaries

- No hotel brand names, management company names, or destination organization names.
- No discount percentages, negotiated rates, or internal commercial strategy. Portfolio pricing
  is described only as "portfolio agreements improve on list pricing."
- No internal targets, revenue goals, or pipeline information.
- greenkeyglobal.com is cited as the source of record for anything subject to change.

## Draft status

While the site is pending internal review, every page must carry
`<meta name="robots" content="noindex, nofollow">` in the head, and robots.txt must contain
`User-agent: *` and `Disallow: /`. Do not remove these without an explicit instruction.

## Writing style

- Plain business English. Lead with operational and financial impact.
- Short scannable sections with bolded lead-ins. Avoid dense paragraphs.
- **No em dashes and no en dashes** anywhere in output. Use commas, colons, or periods.
- Do not use sustainability language where operating language will do. Say operating cost,
  NOI, asset value, corporate mix, and risk.

## Technical

- Static HTML, one small shared CSS file, no build step, no CMS.
- Match the existing nav, footer, and CSS class structure of the current pages exactly.
- No blocking scripts except the ROI calculator.
- Target Lighthouse 90+ on performance, accessibility, best practices, and SEO.
