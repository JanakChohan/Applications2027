// -----------------------------------------------------------------------------
// adaptive.js — build "serve me more of my weakest category" hints from the store.
//
// • Numerical: returns typeWeights that over-serve weak item types (its generator
//   accepts typeWeights directly).
// • Other modules: returns a `focus` list of weak skill keys (rule kinds / trap
//   classes) that each module's generator can bias toward.
// New/under-sampled skills get a mild boost so you still see everything.
// -----------------------------------------------------------------------------

import { skillAccuracy } from './store.js';
import { ITEM_TYPES } from '../generators/items.js';
import { DEFAULT_TYPE_WEIGHTS } from '../generators/session.js';

const MIN_ATTEMPTS = 4;

/** Numerical type weights (weak types get more airtime). */
export function adaptiveWeights(data, strength = 2) {
  const acc = skillAccuracy('numerical', data);
  const weights = {};
  for (const type of ITEM_TYPES) {
    const base = DEFAULT_TYPE_WEIGHTS[type] || 1;
    const s = acc[type];
    const factor = !s || s.seen < MIN_ATTEMPTS ? 1.3 : 1 + (1 - s.accuracy) * strength;
    weights[type] = +(base * factor).toFixed(2);
  }
  return weights;
}

/** The N weakest skills for a module (enough attempts to trust), worst first. */
export function weakestSkills(moduleId, data, n = 2) {
  const acc = skillAccuracy(moduleId, data);
  return Object.entries(acc)
    .filter(([, s]) => s.seen >= MIN_ATTEMPTS)
    .sort((a, b) => a[1].accuracy - b[1].accuracy)
    .slice(0, n)
    .map(([skill]) => skill);
}

/** For the progress screen: weakest skills with their numbers, for any module. */
export function weakestWithStats(moduleId, data, n = 3) {
  const acc = skillAccuracy(moduleId, data);
  return Object.entries(acc)
    .filter(([, s]) => s.seen >= MIN_ATTEMPTS)
    .sort((a, b) => a[1].accuracy - b[1].accuracy)
    .slice(0, n)
    .map(([skill, s]) => ({ skill, accuracy: s.accuracy, seen: s.seen }));
}
