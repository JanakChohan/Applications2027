// ix/index.js — module definition for scales ix (odd-one-out).
import { generateItem, ruleText } from './generate.js';
import { verifyItem } from './verify.js';
import { objectSvg } from '../../ui/shapes.js';
import { REASONS } from '../../coaching/diagnosis.js';
import { weakestSkills } from '../../coaching/adaptive.js';

function assemble(seed, tier, count, focus) {
  const items = [];
  const seen = new Set();
  for (let i = 0; i < count; i++) {
    for (let a = 0; a < 30; a++) {
      const it = generateItem(seed, tier, i, a, focus);
      if (!verifyItem(it).ok) continue;
      const sig = it.rule.kind + '|' + it.objects.map((o) => `${o.shape}${o.filled ? 1 : 0}${o.rotation}${o.inner || '-'}`).join(',');
      if (seen.has(sig)) continue;
      seen.add(sig);
      it.id = `${seed}-x${i}`; it.index = items.length; it.skill = it.rule.kind;
      items.push(it);
      break;
    }
  }
  return items;
}

export default {
  id: 'ix',
  label: 'scales ix',
  blurb: 'Nine objects; eight share a hidden rule. Click the one that breaks it.',
  tiers: ['beginner', 'intermediate', 'advanced'],
  usesTabs: false,
  answerKind: 'custom',
  modes: [
    { key: 'timed', label: 'Timed set', count: 15, time: 300, timed: true, allowBack: true, desc: '15 series · 5:00 (~20s each)' },
    { key: 'untimed', label: 'Untimed drill', count: 12, time: 0, timed: false, allowBack: true, desc: 'No clock · learn to scan every attribute' },
    { key: 'adaptive', label: 'Adaptive drill', count: 12, time: 0, timed: false, allowBack: true, adaptive: true, desc: 'No clock · more of your weakest rule types' },
  ],

  generate({ seed, tier = 'intermediate', count = 12, focus = null }) {
    return { module: 'ix', seed, tier, context: null, items: assemble(seed, tier, count, focus) };
  },
  adaptive: (data) => ({ focus: weakestSkills('ix', data, 2) }),

  answerOf: (item) => item.answer,
  tokenLabel: (t) => `object ${Number(t) + 1}`,
  requiredTabsOf: () => [],

  // The nine objects ARE the answer controls (each is clickable via data-ans).
  renderDisplay(item, session, state) {
    const given = state && state.given;
    const cells = item.objects.map((o, k) =>
      `<button class="ix-obj${given === String(k) ? ' sel' : ''}" data-ans="${k}">${objectSvg(o)}</button>`).join('');
    return `<div class="ix-grid">${cells}</div>`;
  },
  renderControls: () => '',

  renderReview(item, res) {
    const rt = ruleText[item.rule.kind](item.rule);
    const diag = res.diagnosis && res.diagnosis.category !== 'correct_fast'
      ? `<div class="diag"><strong>${res.diagnosis.label}.</strong> ${res.diagnosis.advice}</div>` : '';
    return `<p>The rule is: <strong>${rt}</strong>. Object <strong>${item.breakerIndex + 1}</strong> is the only one that breaks it, so it is the odd one out.</p>${diag}`;
  },

  diagnose(item, ans) {
    const R = (c) => ({ category: c, ...REASONS[c] });
    if (ans.given == null) return R(ans.ranOutOfTime ? 'ran_out_of_time' : 'skipped_blank');
    if (ans.given === item.answer) return ans.timeMs > 35000 ? R('slow_but_correct') : R('correct_fast');
    if (ans.timeMs != null && ans.timeMs < 4000) return R('panic_guess');
    return R('checked_one_property');
  },
};
