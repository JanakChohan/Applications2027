// -----------------------------------------------------------------------------
// calculator.js — a small on-screen calculator, because scales numerical PROVIDES
// one (research/FINDINGS.md §4). Plain four-function + percent, keyboard-enabled.
// Returns a detachable element you can show/hide next to the question.
// -----------------------------------------------------------------------------

export function createCalculator() {
  const el = document.createElement('div');
  el.className = 'calc';
  el.innerHTML = `
    <div class="calc-display" data-role="display">0</div>
    <div class="calc-keys">
      ${['C', '±', '%', '÷', '7', '8', '9', '×', '4', '5', '6', '−', '1', '2', '3', '+', '0', '.', '=']
      .map((k) => `<button class="calc-key${k === '=' ? ' eq' : ''}" data-k="${k}">${k}</button>`).join('')}
    </div>`;

  const display = el.querySelector('[data-role="display"]');
  let acc = null, op = null, cur = '0', fresh = true;

  const show = () => { display.textContent = cur.length > 12 ? Number(cur).toPrecision(10) : cur; };
  const apply = (a, b, o) => o === '+' ? a + b : o === '−' ? a - b : o === '×' ? a * b : b === 0 ? NaN : a / b;

  function press(k) {
    if (/[0-9]/.test(k)) { cur = fresh ? k : (cur === '0' ? k : cur + k); fresh = false; }
    else if (k === '.') { if (!cur.includes('.')) { cur = fresh ? '0.' : cur + '.'; fresh = false; } }
    else if (k === 'C') { acc = null; op = null; cur = '0'; fresh = true; }
    else if (k === '±') { cur = String(-parseFloat(cur)); }
    else if (k === '%') { cur = String(parseFloat(cur) / 100); }
    else if (k === '=') {
      if (op != null && acc != null) { cur = String(round(apply(acc, parseFloat(cur), op))); acc = null; op = null; fresh = true; }
    } else { // an operator
      if (op != null && acc != null && !fresh) { acc = apply(acc, parseFloat(cur), op); cur = String(round(acc)); }
      else { acc = parseFloat(cur); }
      op = k; fresh = true;
    }
    show();
  }
  const round = (n) => Math.round((n + Number.EPSILON) * 1e6) / 1e6;

  el.addEventListener('click', (e) => {
    const k = e.target.closest('[data-k]');
    if (k) press(k.dataset.k);
  });

  // keyboard support while the calculator is on screen
  const onKey = (e) => {
    const map = { '/': '÷', '*': '×', '-': '−', '+': '+', '=': '=', 'Enter': '=', '%': '%', '.': '.', 'c': 'C', 'C': 'C' };
    if (/[0-9]/.test(e.key)) press(e.key);
    else if (map[e.key]) { press(map[e.key]); if (e.key === 'Enter') e.preventDefault(); }
  };
  el.addEventListener('attach', () => document.addEventListener('keydown', onKey));
  el.addEventListener('detach', () => document.removeEventListener('keydown', onKey));
  el._onKey = onKey;
  return el;
}
