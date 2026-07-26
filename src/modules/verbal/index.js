// verbal/index.js — module definition for scales verbal.
import { makeRng } from '../../generators/rng.js';
import { buildWorld, generateItem, labelOf, norm } from './generate.js';
import { verifyItem, relevantTab } from './verify.js';
import { passageHtml, tokenLabel, renderReview, diagnose } from './view.js';
import { weakestSkills } from '../../coaching/adaptive.js';

const TARGET = { TRUE: 0.4, FALSE: 0.35, CANNOT_SAY: 0.25 };
const SKILL_LABEL = { cannot_say: 'CANNOT_SAY', quantifier: 'CANNOT_SAY', outside_knowledge: 'CANNOT_SAY', contradiction: 'FALSE', synonym: 'TRUE', literal: 'TRUE' };

/** Fine-grained skill bucket for progress + adaptive focus. */
function skillFrom(it) {
  if (it.label === 'CANNOT_SAY') return it.traps.includes('quantifier') ? 'quantifier' : it.traps.includes('outside_knowledge') ? 'outside_knowledge' : 'cannot_say';
  if (it.label === 'FALSE') return 'contradiction';
  return it.traps.includes('synonym') ? 'synonym' : 'literal';
}

function neediest(counts, total) {
  if (!total) return null;
  let best = null, gap = -Infinity;
  for (const [l, t] of Object.entries(TARGET)) { const g = t - counts[l] / total; if (g > gap) { gap = g; best = l; } }
  return best;
}
const sigOf = (it) => `${it.claim.subject}|${it.claim.attribute}|${norm(it.claim.asserted)}`;

function assemble(world, seed, tier, count, focus) {
  const items = [];
  const seen = new Set();
  const counts = { TRUE: 0, FALSE: 0, CANNOT_SAY: 0 };
  for (let i = 0; i < count; i++) {
    let aim = neediest(counts, items.length);
    if (focus && focus.length) {
      const r = makeRng(`vaim:${seed}:${tier}:${i}`);
      if (r.chance(0.6)) aim = SKILL_LABEL[r.pick(focus)] || aim;
    }
    let accepted = null, fallback = null;
    for (let a = 0; a < 40 && !accepted; a++) {
      const rng = makeRng(`vitem:${seed}:${tier}:${i}:${a}`);
      const it = generateItem(world, rng, tier, aim);
      it.label = labelOf(world, it.claim);
      it.prompt = it.statement;
      const v = verifyItem(world, it);
      if (!v.ok) continue;
      const sig = sigOf(it);
      if (seen.has(sig)) continue;
      it.requiredTabs = it.label === 'CANNOT_SAY' ? [] : [relevantTab(world, it.claim)].filter(Boolean);
      it.verify = v;
      if (aim == null || it.label === aim) { seen.add(sig); accepted = it; }
      else if (!fallback) fallback = { it, sig };
    }
    if (!accepted && fallback) { seen.add(fallback.sig); accepted = fallback.it; }
    if (!accepted) continue;
    accepted.id = `${seed}-v${i}`;
    accepted.index = items.length;
    accepted.skill = skillFrom(accepted);
    counts[accepted.label]++;
    items.push(accepted);
  }
  return items;
}

export default {
  id: 'verbal',
  label: 'scales verbal',
  blurb: 'Read short company passages across tabs; judge each statement True / False / Cannot Say. No maths.',
  tiers: ['beginner', 'intermediate', 'advanced'],
  usesTabs: true,
  answerKind: 'tfc',
  modes: [
    { key: 'full', label: 'Full mock', count: 30, time: 450, timed: true, allowBack: true, desc: '30 statements · 7:30 · real pace (~15s/item)' },
    { key: 'short', label: 'Short mock', count: 15, time: 225, timed: true, allowBack: true, desc: '15 statements · 3:45' },
    { key: 'untimed', label: 'Untimed drill', count: 12, time: 0, timed: false, allowBack: true, desc: 'No clock · learn the decision rule' },
    { key: 'adaptive', label: 'Adaptive drill', count: 15, time: 0, timed: false, allowBack: true, adaptive: true, desc: 'No clock · more of your weakest patterns' },
  ],

  generate({ seed, tier = 'intermediate', count = 15, sectorBias = null, focus = null }) {
    const world = buildWorld(seed, tier, sectorBias);
    const items = assemble(world, seed, tier, count, focus);
    const context = { tabs: world.tabs.map((t) => ({ id: t.id, title: t.title, html: passageHtml(t) })) };
    return { module: 'verbal', seed, tier, world, context, items };
  },
  adaptive: (data) => ({ focus: weakestSkills('verbal', data, 2) }),

  answerOf: (item) => item.label,
  tokenLabel,
  requiredTabsOf: (item) => item.requiredTabs || [],
  renderReview,
  diagnose,
};
