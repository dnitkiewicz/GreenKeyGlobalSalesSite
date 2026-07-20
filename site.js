document.addEventListener('DOMContentLoaded', () => {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
  }

  document.querySelectorAll('.faq-item').forEach((item) => {
    item.querySelector('.faq-question').addEventListener('click', () => {
      const active = item.classList.contains('active');
      document.querySelectorAll('.faq-item').forEach((entry) => entry.classList.remove('active'));
      if (!active) item.classList.add('active');
    });
  });

  const calculatorForm = document.getElementById('roi-form');
  const outputs = {
    conservative: document.getElementById('conservative-output'),
    moderate: document.getElementById('moderate-output'),
    strong: document.getElementById('strong-output'),
    breakEven: document.getElementById('breakeven-output'),
    monthly: document.getElementById('monthly-output')
  };

  if (calculatorForm && outputs.conservative) {
    const formatCurrency = (value) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }).format(value);
    const formatNumber = (value) => new Intl.NumberFormat('en-US', { maximumFractionDigits: 1 }).format(value);

    const calculate = () => {
      const props = Number(document.getElementById('props').value || 0);
      const adr = Number(document.getElementById('adr').value || 0);
      const rn = Number(document.getElementById('rn').value || 0);
      const util = Number(document.getElementById('util').value || 0);
      const member = Number(document.getElementById('member').value || 0);
      const audit = Number(document.getElementById('audit').value || 0);
      const disc = Number(document.getElementById('disc').value || 0) / 100;
      const liftC = Number(document.getElementById('liftC').value || 0) / 100;
      const liftM = Number(document.getElementById('liftM').value || 0) / 100;
      const liftS = Number(document.getElementById('liftS').value || 0) / 100;
      const save = Number(document.getElementById('save').value || 0) / 100;

      const memberNet = member * (1 - disc);
      const auditAnnual = audit * (1 - disc) / 3;
      const costPerProp = memberNet + auditAnnual;
      const costCohort = costPerProp * props;
      const costMonthly = costPerProp / 12;
      const breakEven = adr > 0 ? costPerProp / adr : 0;

      const addedRN = (lift) => rn * lift;
      const addedRev = (lift) => addedRN(lift) * adr;
      const cohortRev = (lift) => addedRev(lift) * props;
      const utilSaveProp = util * save;
      const utilSaveCohort = utilSaveProp * props;
      const netBenefit = (lift) => cohortRev(lift) + utilSaveCohort - costCohort;
      const returnX = (lift) => costCohort > 0 ? (cohortRev(lift) + utilSaveCohort) / costCohort : 0;

      outputs.conservative.innerHTML = `<div class="big">${formatCurrency(netBenefit(liftC))}</div><p>Net benefit at conservative lift</p><p>Return multiple: ${formatNumber(returnX(liftC))}x</p>`;
      outputs.moderate.innerHTML = `<div class="big">${formatCurrency(netBenefit(liftM))}</div><p>Net benefit at moderate lift</p><p>Return multiple: ${formatNumber(returnX(liftM))}x</p>`;
      outputs.strong.innerHTML = `<div class="big">${formatCurrency(netBenefit(liftS))}</div><p>Net benefit at strong lift</p><p>Return multiple: ${formatNumber(returnX(liftS))}x</p>`;
      outputs.breakEven.innerHTML = `<div class="big">${formatNumber(breakEven)} RN</div><p>Break-even room nights per property per year</p>`;
      outputs.monthly.innerHTML = `<div class="big">${formatCurrency(costMonthly)}</div><p>Per property per month</p>`;
    };

    calculatorForm.addEventListener('input', calculate);
    calculate();
  }
});
