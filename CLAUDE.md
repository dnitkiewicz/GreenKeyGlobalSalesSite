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
