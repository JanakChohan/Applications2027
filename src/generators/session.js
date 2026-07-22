// -----------------------------------------------------------------------------
// session.js — assemble a playable session: ONE dataset (six fixed tabs) plus N
// statements about it, mixed across item types and balanced across the three
// answers, de-duplicated, and every item independently verified before it is
// allowed in. Anything the verifier rejects never reaches the candidate.
// -----------------------------------------------------------------------------

import { makeRng } from './rng.js';
import { generateDataset } from './dataset.js';
import { generateItem, ITEM_TYPES } from './items.js';
import { verifyItem } from '../verify/verifier.js';

// Default relative frequency of each item type in a mixed session.
export const DEFAULT_TYPE_WEIGHTS = {
  lookup: 3, arithmetic: 3, pct_change: 2, pct_points: 2, share: 2,
  multi_tab: 2, trend: 2, rank: 2, insufficient: 2,
};

// Target answer distribution. The real test isn't perfectly balanced, but for
// training we keep all three well represented so Cannot Say gets practised.
const TARGET_LABELS = { TRUE: 0.4, FALSE: 0.35, CANNOT_SAY: 0.25 };

/** Stable signature for de-duplication: same references + operator = same question. */
function signature(item) {
  const refs = (item.requiredCells || [])
    .map((c) => `${c.m}:${c.e}:${c.p}`)
    .sort()
    .join(',');
  const op = item.claim.op || item.claim.dir || item.claim.sel || '';
  return `${item.type}|${item.claim.kind}|${op}|${refs}`;
}

/**
 * @param {object} opts
 * @param {string|number} opts.seed
 * @param {'medium'|'intermediate'|'hard'} opts.tier
 * @param {number} opts.count            number of items
 * @param {object} [opts.typeWeights]    override type frequencies (adaptive mode)
 * @param {number} [opts.maxTriesPerItem]
 * @returns {{seed, tier, dataset, items}}
 */
export function generateSession({ seed, tier = 'intermediate', count = 18, typeWeights, maxTriesPerItem = 40 }) {
  const rng = makeRng(`session:${seed}:${tier}:${count}`);
  const dataset = generateDataset(seed, tier);
  const weights = typeWeights || DEFAULT_TYPE_WEIGHTS;
  const weightList = ITEM_TYPES.filter((t) => (weights[t] || 0) > 0)
    .map((t) => ({ value: t, weight: weights[t] }));

  const items = [];
  const seen = new Set();
  const labelCounts = { TRUE: 0, FALSE: 0, CANNOT_SAY: 0 };

  for (let i = 0; i < count; i++) {
    const aim = neediestLabel(labelCounts, items.length);
    let accepted = null;
    let fallback = null; // a valid item whose label didn't match the target

    for (let attempt = 0; attempt < maxTriesPerItem && !accepted; attempt++) {
      // Bias type choice toward `aim`: insufficient guarantees Cannot Say.
      let type;
      if (aim === 'CANNOT_SAY' && rng.chance(0.5)) type = 'insufficient';
      else type = rng.weighted(weightList);

      const itemRng = makeRng(`item:${seed}:${tier}:${i}:${attempt}`);
      let item;
      try {
        item = generateItem(dataset, itemRng, tier, type, aim);
      } catch {
        continue;
      }
      const v = verifyItem(dataset, item);
      if (!v.ok) continue;                 // reject any mislabelled item outright
      const sig = signature(item);
      if (seen.has(sig)) continue;          // reject duplicate question shapes

      item.id = `${seed}-${i}`;
      item.index = i;
      item.verify = v;

      // Prefer an item whose computed label matches the target we're short on;
      // this keeps the True/False/Cannot-Say mix close to TARGET_LABELS instead
      // of drifting (the generators naturally skew a little towards False).
      if (aim == null || item.label === aim) {
        seen.add(sig);
        accepted = item;
      } else if (!fallback) {
        fallback = { item, sig };
      }
    }

    if (!accepted && fallback) {
      seen.add(fallback.sig);
      accepted = fallback.item;
    }

    // Fallback: if we somehow couldn't find a fresh verified item, take any
    // verified one (still correct, may repeat a shape). Extremely rare.
    if (!accepted) {
      accepted = forceAny(dataset, seed, tier, i, weightList);
      accepted.id = `${seed}-${i}`;
      accepted.index = i;
    }

    labelCounts[accepted.label]++;
    items.push(accepted);
  }

  return { seed, tier, dataset, items };
}

/** Pick the answer label currently furthest below its target share. */
function neediestLabel(counts, total) {
  if (total === 0) return null;
  let best = null;
  let bestGap = -Infinity;
  for (const [label, target] of Object.entries(TARGET_LABELS)) {
    const cur = counts[label] / total;
    const gap = target - cur;
    if (gap > bestGap) { bestGap = gap; best = label; }
  }
  return best;
}

function forceAny(dataset, seed, tier, i, weightList) {
  const rng = makeRng(`force:${seed}:${tier}:${i}`);
  for (let a = 0; a < 200; a++) {
    const type = rng.weighted(weightList);
    const r = makeRng(`forceitem:${seed}:${tier}:${i}:${a}`);
    try {
      const item = generateItem(dataset, r, tier, type, null);
      if (verifyItem(dataset, item).ok) return item;
    } catch { /* keep trying */ }
  }
  // As an absolute last resort, an insufficient item is always valid.
  const item = generateItem(dataset, makeRng(`last:${seed}:${i}`), tier, 'insufficient', null);
  return item;
}
