"""Generate the remaining pages from shared partials so nav and footer stay in sync."""
from _partials import NAV, FOOT, CREDS

NAV_KEYS = ["why", "how", "prop", "port", "q", "read"]


def nav(active=None):
    subs = {}
    for k in NAV_KEYS:
        subs["C_" + k] = ' aria-current="page"' if k == active else ""
    return NAV.format(**subs)


def page(slug, title, desc, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

{nav(active)}

<main id="main">
{body}
</main>

{FOOT}
<script src="assets/site.js"></script>
</body>
</html>
"""


LADDER = """  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">However you want to move</p>
        <h2>Three ways forward, in order of commitment</h2>
      </div>
      <div class="ladder-cta">
        <div class="rung">
          <span class="step">Lowest commitment</span>
          <h3>Read the questions</h3>
          <p>All 213 assessment questions, filterable, with the mandatory ones flagged.</p>
          <p><a class="btn btn--ghost" href="questions.html">Open the library</a></p>
        </div>
        <div class="rung">
          <span class="step">Ten minutes</span>
          <h3>Check your readiness</h3>
          <p>Work through the Core Criteria in plain terms. Runs in your browser, stores nothing.</p>
          <p><a class="btn btn--ghost" href="readiness.html">Start the checklist</a></p>
        </div>
        <div class="rung rung--last">
          <span class="step">When you are ready</span>
          <h3>Talk to us</h3>
          <p>We will walk the assessment with you before anything is signed.</p>
          <p><a class="btn" href="mailto:Sales@greenkeyglobal.com">Sales@greenkeyglobal.com</a></p>
        </div>
      </div>
    </div>
  </section>"""


# ---------------------------------------------------------------- properties
properties = f"""  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">For general managers and operations leaders</p>
      <h1>Four to six hours, spread across people who already know the answers</h1>
      <p class="lede">No single person completes this assessment. It splits along the lines your org chart already runs on, and each contributor answers questions about their own department in their own language.</p>
      <div class="btn-row">
        <a class="btn" href="readiness.html">Check your readiness</a>
        <a class="btn btn--ghost" href="questions.html">Read the questions</a>
      </div>
    </div>
  </section>

{CREDS}

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Who does the work</p>
        <h2>Five people, an hour or so each</h2>
      </div>
      <table class="roles">
        <caption>Contributors and what each supplies</caption>
        <thead><tr><th scope="col">Role</th><th scope="col">What they supply</th></tr></thead>
        <tbody>
          <tr><td data-l="Role" class="who">General Manager</td><td data-l="Supplies">Signs the sustainability policy and names the accountable manager</td></tr>
          <tr><td data-l="Role" class="who">Chief Engineer</td><td data-l="Supplies">Twelve months of utility data, maintenance logs, equipment inventory</td></tr>
          <tr><td data-l="Role" class="who">Executive Housekeeper</td><td data-l="Supplies">Linen reuse program, cleaning products, room routines, training records</td></tr>
          <tr><td data-l="Role" class="who">F&amp;B Lead</td><td data-l="Supplies">Purchasing practice, waste reduction, refrigeration</td></tr>
          <tr><td data-l="Role" class="who">Green Team Lead</td><td data-l="Supplies">Coordinates the team, uploads evidence, tracks completion</td></tr>
        </tbody>
        <tfoot><tr><td data-l="Total" colspan="2">Roughly four to six hours of focused work across the team</td></tr></tfoot>
      </table>
      <span class="src">Green Key Global program data &middot; 2026. Per-role estimates are illustrative; the four to six hour total is the measured figure.</span>

      <div class="callout" style="margin-top:2rem">
        <h3>If you are an independent property</h3>
        <p>No corporate sustainability team, no brand standard forcing the issue, no procurement department. That is the common case, and it is the case the redesigned assessment was built for. A property does not need a dedicated sustainability function to certify. It needs someone accountable and a few hours from people who already know the answers.</p>
      </div>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">The question nobody asks out loud</p>
        <h2>There is no failing grade</h2>
        <p>Any rating is full certification. A property that certifies at one Key is certified. What the audit produces alongside the rating is a Property Performance Report showing exactly where the next Key's points live, which turns improvement into an assignable plan across a three year cycle.</p>
      </div>
      <div class="ladder" role="img" aria-label="Five ascending steps labelled one Key through five Keys. Every step is full certification.">
        <div>1 Key</div><div>2 Keys</div><div>3 Keys</div><div>4 Keys</div><div>5 Keys</div>
      </div>
      <p class="ladder-note">Every step above is full certification.</p>
      <p>The rating is not a public verdict on how the hotel is run. It is a starting position with a documented route out of it.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">What the assessment asks</p>
        <h2>213 questions, five sections, two of them optional</h2>
        <p>Rather than describe them, we publish them. Every question is listed with the mandatory ones flagged and the documentation requirement shown.</p>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Corporate management</h3><p>Policy, action plan, responsible purchasing, staff and guest engagement, community involvement.</p></div>
        <div class="card"><h3>Engineering &amp; maintenance</h3><p>Utility tracking, preventative maintenance, HVAC, insulation, lighting, fixtures, waste, renewables.</p></div>
        <div class="card"><h3>Housekeeping</h3><p>Linen reuse, cleaning products, energy and water conscious room routines, training.</p></div>
        <div class="card"><h3>Food &amp; beverage <em>(optional)</em></h3><p>Purchasing, waste reduction, refrigeration, service practices.</p></div>
        <div class="card"><h3>Conference &amp; meetings <em>(optional)</em></h3><p>Event space sustainability practices for properties with meeting space.</p></div>
        <div class="card" style="background:var(--surface)"><h3>Read them yourself</h3><p>All 213, filterable by section, no login.</p><p><a href="questions.html">Open the question library &rarr;</a></p></div>
      </div>
      <p style="margin-top:1.25rem"><span class="src">Optional sections rescale the score without penalty, so a property with no meeting space is not scored against one that has it.</span></p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">The operating line</p>
        <p class="pull">The assessment is not asking a hotel to spend money on sustainability. It is asking it to stop spending money on waste.</p>
        <p>Metering utilities. Preventative maintenance. Sealing the building envelope. Lighting upgrades. Water-conscious housekeeping routines. Right-sized food purchasing. None of that is a sustainability program. It is operating discipline that happens to score.</p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">For your sales team</p>
        <h2>A verifiable answer in an RFP</h2>
        <p>Corporate travel buyers increasingly require recognized certification before shortlisting a hotel. Booking platforms look for third-party verification before displaying a sustainability badge. Certification gives a director of sales something checkable instead of a description of good intentions.</p>
      </div>
      <div class="grid grid--2">
        <div class="stat">
          <span class="fig">89%</span>
          <p class="lab">Of business travel professionals say sustainability is a priority for their organization.</p>
          <span class="src">GBTA Business Travel Industry Outlook &middot; 2025</span>
        </div>
        <div class="stat">
          <span class="fig">100M</span>
          <p class="lab">Nights booked at properties holding a third-party certification on Booking.com in 2025.</p>
          <span class="src">Booking.com &middot; 2026</span>
        </div>
      </div>
      <p style="margin-top:1.5rem"><a href="why-certify.html">See the full business case &rarr;</a></p>
    </div>
  </section>

{LADDER}"""


# ---------------------------------------------------------------- portfolios
portfolios = f"""  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">For management companies, brands and collections</p>
      <h1>One standard, applied the same way at every property</h1>
      <p class="lede">A portfolio rollout is not twenty separate certifications. It is one set of corporate policies written once, plus property-level evidence gathered locally. The corporate work does not repeat.</p>
      <div class="btn-row">
        <a class="btn" href="mailto:Sales@greenkeyglobal.com">Scope a portfolio rollout</a>
        <a class="btn btn--ghost" href="questions.html">Read the questions</a>
      </div>
    </div>
  </section>

{CREDS}

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">The mechanic</p>
        <h2>What repeats, and what does not</h2>
      </div>
      <div class="split">
        <div class="card">
          <h3>Written once at corporate</h3>
          <ul>
            <li>Environmental policy and signature</li>
            <li>Responsible purchasing policy</li>
            <li>Green Team mandate and structure</li>
            <li>Training standards</li>
            <li>Reporting cadence</li>
          </ul>
        </div>
        <div class="card">
          <h3>Gathered at each property</h3>
          <ul>
            <li>Twelve months of utility data</li>
            <li>Maintenance logs</li>
            <li>Housekeeping routines</li>
            <li>F&amp;B purchasing practice</li>
            <li>Property-specific evidence uploads</li>
          </ul>
        </div>
      </div>
      <p style="margin-top:1.5rem">This is what makes portfolio rollout tractable. The heaviest lift, corporate governance, is a single exercise. What scales per property is evidence collection, which is local by nature and cannot be centralized anyway.</p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Pricing and reporting at portfolio level</p>
        <h2>Structured to the portfolio, not sold from a rate card</h2>
      </div>
      <p>Portfolio-level pricing and consolidated reporting are available and are built around the portfolio rather than offered as a fixed package. Data can be pulled by portfolio, which gives corporate a comparable view of operating gaps scored on the same criteria at every property.</p>
      <p>What that looks like in practice depends on portfolio size, brand structure, and what corporate needs to report and to whom. It is scoped in conversation.</p>
      <div class="callout">
        <p>This is the one place on this site where the answer is genuinely "let us talk". Everything else here, including the full question set, is published and open.</p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Sequencing</p>
        <h2>Most portfolios do not start everywhere at once</h2>
      </div>
      <p>A common pattern is a pilot cohort of properties that already have utility metering and maintenance discipline in place. That cohort produces a working template and an internal reference case before the wider rollout begins.</p>
      <p>Because the corporate-level policies are written once, the second property is materially faster than the first, and the twentieth is faster again.</p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Why owners ask about this</p>
        <h2>Certification evidences operating discipline rather than asserting it</h2>
      </div>
      <p>Hotel owners and operators are increasingly aligning on ESG metrics inside management agreements, with sustainability treated as an investment and performance metric rather than a reporting exercise. For a management company, certification is a way to show that discipline to an owner in a form a third party has verified.</p>
      <span class="src">JLL, on hotel owner and operator ESG alignment &middot; 2025</span>

      <div class="sec-head" style="margin-top:3rem">
        <p class="eyebrow">Regulatory horizon</p>
        <h2>Independent verification becomes a requirement, not a differentiator</h2>
      </div>
      <p>The EU's Empowering Consumers for the Green Transition Directive applies from 27 September 2026. It prohibits displaying sustainability labels that are not based on a certification scheme, and requires those schemes to meet minimum conditions of transparency and credibility with independent third-party monitoring.</p>
      <p>Portfolios marketing to European source markets will need third-party verification behind any environmental claim they display.</p>
      <span class="src">Directive (EU) 2024/825 &middot; applies 27 September 2026</span>
    </div>
  </section>

{LADDER}"""


# ---------------------------------------------------------------- partners
partners = f"""  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">For organizations that support the industry</p>
      <h1>Three ways to work with Green Key without certifying</h1>
      <p class="lede">Destination organizations, associations and suppliers are not certification buyers. They are how certification reaches the properties that are.</p>
    </div>
  </section>

{CREDS}

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">DMOs and CVBs</p>
        <h2>Give your destination a verifiable sustainability story</h2>
      </div>
      <p>Meeting planners and corporate buyers increasingly evaluate destinations on the certified inventory available in them, not on destination-level marketing claims. Certified properties appear in Green Key's distributed property lists and on booking platforms that verify certification.</p>
      <p><a class="btn btn--ghost" href="mailto:Sales@greenkeyglobal.com">Talk about destination partnership</a></p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Membership associations</p>
        <h2>Bring a recognized certification to your membership</h2>
      </div>
      <p>Green Key Global is jointly owned by AHLA and Hotels Canada, so association partnership is core to how the program reaches properties rather than an add-on to it. Associations extend a certification pathway to members without building or maintaining a standard themselves.</p>
      <p><strong>What partnering looks like:</strong> member communication, event presence, and educational content on what certification asks of a property.</p>
      <p><a class="btn btn--ghost" href="mailto:Sales@greenkeyglobal.com">Talk about association partnership</a></p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Vendors and suppliers</p>
        <h2>Reach certified properties through the Green Vendor Directory</h2>
      </div>
      <p>Certified members receive access to a Green Vendor Directory. For a supplier whose products help properties score, that is direct access to an audience actively working through an assessment.</p>
      <p>The vendor program and application form are on the main Green Key Global site.</p>
      <p><a class="btn btn--ghost" href="https://greenkeyglobal.com/vendor-program/">Open the vendor program</a></p>
    </div>
  </section>"""


# ---------------------------------------------------------------- how it works
how = f"""  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">How the program works</p>
      <h1>Assessment, evidence, audit and certification in one path</h1>
      <p class="lede">A property completes the self-assessment with multiple users, uploads evidence for each mandatory answer, and moves to audit with a preliminary rating already in hand.</p>
    </div>
  </section>

{CREDS}

  <section class="sec">
    <div class="wrap">
      <div class="sec-head"><h2>The five stages</h2></div>
      <ol class="steps">
        <li><div><h3>Assess</h3><p>Online self-assessment with multiple users and progress saved as you go. Evidence is uploaded against each mandatory answer.</p><span class="when">About 4 to 6 hours of focused work &middot; recent average 11 days elapsed</span></div></li>
        <li><div><h3>Evaluate</h3><p>Preliminary rating and gap scorecard. Retake freely before the audit is requested.</p><span class="when">Immediate</span></div></li>
        <li><div><h3>Audit</h3><p>Independent verification, then a certification decision made by an independent certification body.</p><span class="when">Commences within about 90 days of request</span></div></li>
        <li><div><h3>Certify</h3><p>A rating of 1 to 5 Keys, supported by a Property Performance Report.</p><span class="when">Valid three years</span></div></li>
        <li><div><h3>Market</h3><p>Marketing toolkit, OTA badges, RFP content, plaque, and distribution of your property listing.</p><span class="when">Ongoing</span></div></li>
      </ol>
      <p style="margin-top:1rem"><span class="src">Rescheduling an audit requires three business days notice for virtual audits, or 20 for on-site audits.</span></p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">The gate</p>
        <h2>The 37 Core Criteria</h2>
        <p>Thirty-seven questions across Corporate, Housekeeping and Engineering are mandatory. A property cannot certify at any level without them. Nearly all are governance, training and tracking requirements rather than capital projects.</p>
      </div>
      <div class="grid grid--3">
        <div class="card"><h3>Govern it</h3><p>A signed sustainability policy and a named accountable manager.</p></div>
        <div class="card"><h3>Buy responsibly</h3><p>A written responsible purchasing policy.</p></div>
        <div class="card"><h3>Staff it</h3><p>A Green Team with a written mandate.</p></div>
        <div class="card"><h3>Train for it</h3><p>Documented housekeeping and operating routines.</p></div>
        <div class="card"><h3>Measure it</h3><p>Twelve months of utility data and maintenance logs.</p></div>
        <div class="card"><h3>Prove it</h3><p>Documented evidence for every mandatory answer.</p></div>
      </div>
      <p style="margin-top:1.5rem"><a href="questions.html">See all 37 Core Criteria as the assessment asks them &rarr;</a></p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">The rating</p>
        <h2>Any rating is full certification</h2>
        <p>A property that certifies at one Key is certified. The Property Performance Report issued at audit shows exactly where the next Key's points live, which turns improvement into an assignable plan across three year cycles.</p>
      </div>
      <div class="ladder" role="img" aria-label="Five ascending steps labelled one Key through five Keys. Every step is full certification.">
        <div>1 Key</div><div>2 Keys</div><div>3 Keys</div><div>4 Keys</div><div>5 Keys</div>
      </div>
      <p class="ladder-note">Every step above is full certification.</p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Impartiality</p>
        <h2>We set the standard. We never audit our own members.</h2>
      </div>
      <p>Audits are conducted by an independent global inspection firm, and the certification decision rests with an independent certification body, in line with ISO/IEC 17065. Green Key Global does not decide whether a property it enrolled passes.</p>
      <p>Membership renews annually, and a property recertifies every three years against the criteria current at that time.</p>
    </div>
  </section>

{LADDER}"""


# ---------------------------------------------------------------- why certify
why = f"""  <section class="hero">
    <div class="wrap">
      <p class="eyebrow">The evidence</p>
      <h1>The business case, with its sources shown</h1>
      <p class="lede">Every figure on this page carries a named source and a date. Where certified properties outperform others, that is an observed association rather than a demonstrated cause, and it is worded that way.</p>
    </div>
  </section>

{CREDS}

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Operating cost</p>
        <p class="pull">The assessment is not asking a hotel to spend money on sustainability. It is asking it to stop spending money on waste.</p>
        <p>The practices the assessment rewards are the practices that reduce spend. Metering utilities. Preventative maintenance. Sealing the building envelope. Lighting upgrades. Water-conscious housekeeping routines. Right-sized food purchasing.</p>
        <p>None of that is a sustainability program. It is operating discipline that happens to score, which is why the assessment tends to pay for itself before the certificate arrives.</p>
      </div>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Demand</p>
        <h2>Certification is increasingly a filter, not a differentiator</h2>
      </div>
      <div class="grid grid--2">
        <div class="stat">
          <span class="fig">100M</span>
          <p class="lab">Nights booked at properties holding a third-party certification on Booking.com in 2025.</p>
          <span class="src">Booking.com &middot; 2026</span>
        </div>
        <div class="stat">
          <span class="fig">89%</span>
          <p class="lab">Of business travel professionals say sustainability is a priority for their organization.</p>
          <span class="src">GBTA Business Travel Industry Outlook &middot; 2025</span>
        </div>
        <div class="stat">
          <span class="fig">85%</span>
          <p class="lab">Of travelers say more sustainable travel is important or very important to them.</p>
          <span class="src">Booking.com &middot; 2026</span>
        </div>
        <div class="stat">
          <span class="fig">36%</span>
          <p class="lab">Of travelers plan to choose accommodation with a sustainability certification in 2026.</p>
          <span class="src">Booking.com &middot; 2026</span>
        </div>
      </div>
      <p style="margin-top:1.75rem">The booking figure is the one worth weighting most heavily. It measures behaviour rather than stated intent, which is the usual weakness of sustainability survey data.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Regulation</p>
        <h2>Verification requirements are arriving on a fixed date</h2>
      </div>
      <p>The EU's Empowering Consumers for the Green Transition Directive applies from <strong>27 September 2026</strong>. It prohibits displaying sustainability labels that are not based on a certification scheme, and requires such schemes to meet minimum conditions of transparency and credibility with independent third-party monitoring.</p>
      <p>A property showing an unverified environmental claim to EU travelers after that date is exposed. A property holding an independently audited certification is not.</p>
      <span class="src">Directive (EU) 2024/825 &middot; applies 27 September 2026</span>
      <p style="margin-top:1.5rem"><span class="src">This is distinct from the proposed Green Claims Directive, COM 2023/166, which is not law.</span></p>
    </div>
  </section>

  <section class="sec sec--tint">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Owners and lenders</p>
        <h2>Sustainability is becoming a term in the management agreement</h2>
      </div>
      <p>Hotel owners and operators are increasingly aligning on ESG metrics inside management agreements, with sustainability treated as an investment and performance metric rather than a reporting exercise. Certification is a way to evidence that discipline to an owner rather than assert it.</p>
      <span class="src">JLL, on hotel owner and operator ESG alignment &middot; 2025</span>
    </div>
  </section>

{LADDER}"""


PAGES = [
    ("for-properties.html", "Certify one property | Green Key Global",
     "What the Green Key Eco-Rating asks of a single hotel: hours, roles, the rating, and what certification gives a sales team.",
     "prop", properties),
    ("for-portfolios.html", "Certify a portfolio | Green Key Global",
     "How a Green Key Eco-Rating rollout sequences across a management company, brand or collection.",
     "port", portfolios),
    ("for-partners.html", "Partner with Green Key | Green Key Global",
     "For DMOs, CVBs, membership associations, vendors and suppliers who reach hotels rather than certify them.",
     None, partners),
    ("how-it-works.html", "How Eco-Rating certification works | Green Key Global",
     "The Green Key Eco-Rating assessment, Core Criteria, independent audit and rating, stage by stage.",
     "how", how),
    ("why-certify.html", "The business case for certification | Green Key Global",
     "Operating cost, demand, regulation and owner perspective, with every figure sourced and dated.",
     "why", why),
]

for slug, title, desc, active, body in PAGES:
    with open(slug, "w", encoding="utf-8") as f:
        f.write(page(slug, title, desc, active, body))
    print("wrote", slug)
