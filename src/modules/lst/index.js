// lst/index.js — module definition for scales lst (shape sudoku).
import { generateItem } from './generate.js';
import { verifyItem, deduction } from './verify.js';
import { shapeSvg } from '../../ui/shapes.js';
import { REASONS } from '../../coaching/diagnosis.js';

const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);

function assemble(seed, tier, count) {
  const items = [];
  const seen = new Set();
  for (let i = 0; i < count; i++) {
    for (let a = 0; a < 30; a++) {
      const it = generateItem(seed, tier, i, a);
      if (!verifyItem(it).ok) continue;
      // de-dup by the shown puzzle signature
      const sig = it.shown.map((r) => r.map((x) => x || '?').join()).join('|') + '@' + it.ask.r + it.ask.c;
      if (seen.has(sig)) continue;
      seen.add(sig);
      it.id = `${seed}-l${i}`; it.index = items.length; it.skill = `${it.N}x${it.N}`;
      items.push(it);
      break;
    }
  }
  return items;
}

function gridHtml(item) {
  const pf = item.__prefill || {};
  const rows = item.shown.map((row, r) => `<tr>${row.map((cell, c) => {
    const isAsk = r === item.ask.r && c === item.ask.c;
    if (isAsk) return `<td class="sud-cell ask">?</td>`;
    if (cell == null) {
      const v = pf[`${r},${c}`];
      return `<td class="sud-cell scratch" data-prefill="${r},${c}" title="scratch — click to try a shape">${v ? shapeSvg({ shape: v, filled: false }, 40) : '<span class="scratch-hint">＋</span>'}</td>`;
    }
    return `<td class="sud-cell">${shapeSvg({ shape: cell }, 40)}</td>`;
  }).join('')}</tr>`).join('');
  return `<table class="sudoku">${rows}</table>`;
}

export default {
  id: 'lst',
  label: 'scales lst',
  blurb: 'Shape sudoku: each shape appears once per row and column. Pick the shape for the “?” cell.',
  tiers: ['beginner', 'intermediate', 'advanced'],
  usesTabs: false,
  answerKind: 'custom',
  modes: [
    { key: 'timed', label: 'Timed set', count: 12, time: 360, timed: true, allowBack: true, desc: '12 grids · 6:00' },
    { key: 'untimed', label: 'Untimed drill', count: 10, time: 0, timed: false, allowBack: true, desc: 'No clock · pre-fill cells to reason' },
    { key: 'adaptive', label: 'Adaptive drill', count: 10, time: 0, timed: false, allowBack: true, adaptive: true, desc: 'No clock · harder as you improve' },
  ],

  generate({ seed, tier = 'intermediate', count = 10 }) {
    return { module: 'lst', seed, tier, context: null, items: assemble(seed, tier, count) };
  },

  answerOf: (item) => item.answer,
  tokenLabel: (t) => cap(t),
  requiredTabsOf: () => [],

  renderDisplay: (item) => `<div class="shape-stage">${gridHtml(item)}</div>`,
  renderControls: (item) => `<div class="options">${item.choices.map((s) =>
    `<button class="opt" data-ans="${s}" title="${s}">${shapeSvg({ shape: s }, 40)}</button>`).join('')}</div>`,

  wireQuestion(root, item, session, api) {
    root.querySelectorAll('[data-prefill]').forEach((el) => {
      el.onclick = () => {
        item.__prefill = item.__prefill || {};
        const k = el.dataset.prefill;
        const order = [null, ...item.choices];
        const cur = item.__prefill[k] || null;
        const next = order[(order.indexOf(cur) + 1) % order.length];
        if (next) item.__prefill[k] = next; else delete item.__prefill[k];
        api.rerender();
      };
    });
  },

  renderReview(item, res) {
    const d = deduction(item);
    const chain = `Look at the “?” cell’s row: it already contains ${d.rowShapes.map(cap).join(', ') || '—'}. ` +
      `The full set is ${item.shapes.map(cap).join(', ')}, so the only shape missing from that row is ` +
      `<strong>${cap(item.answer)}</strong>. The column confirms it.`;
    const diag = res.diagnosis && res.diagnosis.category !== 'correct_fast'
      ? `<div class="diag"><strong>${res.diagnosis.label}.</strong> ${res.diagnosis.advice}</div>` : '';
    return `<p>${chain}</p>${diag}`;
  },

  diagnose(item, ans) {
    const R = (c) => ({ category: c, ...REASONS[c] });
    if (ans.given == null) return R(ans.ranOutOfTime ? 'ran_out_of_time' : 'skipped_blank');
    if (ans.given === item.answer) return ans.timeMs > 40000 ? R('slow_but_correct') : R('correct_fast');
    if (ans.timeMs != null && ans.timeMs < 5000) return R('panic_guess');
    return R('wrong_row_or_column');
  },
};
