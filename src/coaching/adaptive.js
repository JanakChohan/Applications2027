// -----------------------------------------------------------------------------
// adaptive.js — build type weights that serve more of whatever you're weakest at.
//
// Weakness = low accuracy on a type you've attempted enough times to trust. New
// types (few attempts) get a mild boost too, so you still see everything.
// The result plugs straight into generateSession({ typeWeights }).
// -----------------------------------------------------------------------------

import { typeAccuracy } from './store.js';
import { ITEM_TYPES } from '../generators/items.js';
import { DEFAULT_TYPE_WEIGHTS } from '../generators/session.js';

const MIN_ATTEMPTS = 4; // below this we don't trust the accuracy estimate yet

/**
 * @param {object} data  optional store snapshot (defaults to load())
 * @param {number} strength  how aggressively to over-serve weak types (0..~3)
 * @returns {object} typeWeights for generateSession
 */
export function adaptiveWeights(data, strength = 2) {
  const acc = typeAccuracy(data);
  const weights = {};
  for (const type of ITEM_TYPES) {
    const base = DEFAULT_TYPE_WEIGHTS[type] || 1;
    const stat = acc[type];
    let factor = 1;
    if (!stat || stat.seen < MIN_ATTEMPTS) {
      factor = 1.3;                       // explore under-sampled types
    } else {
      // Lower accuracy → higher weight. Accuracy 1.0 → factor 1; 0.0 → 1+strength.
      factor = 1 + (1 - stat.accuracy) * strength;
    }
    weights[type] = +(base * factor).toFixed(2);
  }
  return weights;
}

/** A short, human explanation of what adaptive mode will focus on. */
export function weakestTypes(data, n = 3) {
  const acc = typeAccuracy(data);
  return Object.entries(acc)
    .filter(([, s]) => s.seen >= MIN_ATTEMPTS)
    .sort((a, b) => a[1].accuracy - b[1].accuracy)
    .slice(0, n)
    .map(([type, s]) => ({ type, accuracy: s.accuracy, seen: s.seen }));
}
