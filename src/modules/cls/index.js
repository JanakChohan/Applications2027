// cls/index.js — module definition for scales cls (grid categorisation).
import { generateItem, ruleText } from './generate.js';
import { verifyItem } from './verify.js';
import { REASONS } from '../../coaching/diagnosis.js';
import { weakestSkills } from '../../coaching/adaptive.js';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));

function gridHtml(grid, cls = '') {
  return `<table class="cls-grid ${cls}">${[0, 3, 6].map((r) =>
    `<tr>${[0, 1, 2].map((c) => `<td>${esc(grid[r + c])}</td>`).join('')}</tr>`).join('')}</table>`;
}

function assemble(seed, tier, count, focus) {
  const items = [];
  for (let i = 0; i < count; i++) {
    const wantGroup = i % 2 === 0 ? 'A' : 'B'; // balance answers so guessing one group fails
    for (let a = 0; a < 40; a++) {
      const it = generateItem(seed, tier, i, a, focus, wantGroup);
      if (!it || !verifyItem(it).ok) continue;
      it.id = `${seed}-c${i}`; it.index = items.length; it.skill = it.rule.kind;
      items.push(it);
      break;
    }
  }
  return items;
}

export default {
  id: 'cls',
  label: 'scales cls',
  blurb: 'Six grids are colour-sorted by a hidden rule. Work out the rule and classify the new grid.',
  tiers: ['beginner', 'intermediate', 'advanced'],
  usesTabs: false,
  answerKind: 'custom',
  modes: [
    { key: 'timed', label: 'Timed set', count: 12, time: 480, timed: true, allowBack: true, desc: '12 grids · 8:00' },
    { key: 'untimed', label: 'Untimed drill', count: 10, time: 0, timed: false, allowBack: true, desc: 'No clock · learn to spot the rule' },
    { key: 'adaptive', label: 'Adaptive drill', count: 10, time: 0, timed: false, allowBack: true, adaptive: true, desc: 'No clock · more of your weakest rule types' },
  ],

  generate({ seed, tier = 'intermediate', count = 10, focus = null }) {
    return { module: 'cls', seed, tier, context: null, items: assemble(seed, tier, count, focus) };
  },
  adaptive: (data) => ({ focus: weakestSkills('cls', data, 2) }),

  answerOf: (item) => item.answer,
  tokenLabel: (t) => `Group ${t}`,
  requiredTabsOf: () => [],

  renderDisplay(item) {
    const groupBlock = (g) => `<div class="cls-group cls-${g}"><div class="cls-glabel">Group ${g}</div>` +
      item.examples.filter((e) => e.group === g).map((e) => gridHtml(e.grid, `cls-${g}`)).join('') + '</div>';
    return `<div class="cls-examples">${groupBlock('A')}${groupBlock('B')}</div>
      <div class="cls-target"><div class="cls-tlabel">Classify this grid:</div>${gridHtml(item.target, 'target')}</div>`;
  },
  renderControls: (item) => `<div class="answers">${item.choices.map((g) =>
    `<div class="ans" data-ans="${g}">Group ${g}</div>`).join('')}</div>`,

  renderReview(item, res) {
    const diag = res.diagnosis && res.diagnosis.category !== 'correct_fast'
      ? `<div class="diag"><strong>${res.diagnosis.label}.</strong> ${res.diagnosis.advice}</div>` : '';
    return `<p>The hidden rule: <strong>Group A = ${esc(ruleText(item.rule))}</strong>. ` +
      `The target grid ${item.answer === 'A' ? 'satisfies' : 'does not satisfy'} it, so it belongs to ` +
      `<strong>Group ${item.answer}</strong>.</p>${diag}`;
  },

  diagnose(item, ans) {
    const R = (c) => ({ category: c, ...REASONS[c] });
    if (ans.given == null) return R(ans.ranOutOfTime ? 'ran_out_of_time' : 'skipped_blank');
    if (ans.given === item.answer) return ans.timeMs > 45000 ? R('slow_but_correct') : R('correct_fast');
    if (ans.timeMs != null && ans.timeMs < 5000) return R('panic_guess');
    return R('wrong_group');
  },
};
