// -----------------------------------------------------------------------------
// rng.js — a small, SEEDABLE pseudo-random generator.
//
// Why seedable? Two reasons that matter for this project:
//   1. Tests must be deterministic. A generator bug that only shows up on 1 seed
//      in 10,000 is exactly the "wrong label" bug we most fear, so every test
//      pins a seed and asserts an exact outcome.
//   2. Sessions are reproducible. A session is identified by its seed, so the
//      coaching layer can regenerate the exact same dataset+items for review.
//
// Algorithm: mulberry32 — tiny, fast, good enough statistical quality for a
// practice app. Not cryptographic; never use for anything security-sensitive.
// -----------------------------------------------------------------------------

/** Hash an arbitrary string/number into a 32-bit seed integer. */
export function hashSeed(input) {
  const str = String(input);
  let h = 2166136261 >>> 0; // FNV-1a
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/**
 * Create a RNG object seeded by `seed` (string or number).
 * Returns a bag of helpers so call sites read clearly (rng.int(1,6), rng.pick(...)).
 */
export function makeRng(seed) {
  let a = hashSeed(seed);

  // Core mulberry32 step → float in [0, 1).
  function next() {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }

  const rng = {
    /** raw float in [0,1) */
    float: next,
    /** float in [min, max) */
    range(min, max) {
      return min + next() * (max - min);
    },
    /** integer in [min, max] inclusive */
    int(min, max) {
      return Math.floor(min + next() * (max - min + 1));
    },
    /** true with probability p (default 0.5) */
    chance(p = 0.5) {
      return next() < p;
    },
    /** random element of an array */
    pick(arr) {
      return arr[Math.floor(next() * arr.length)];
    },
    /** in-place Fisher–Yates shuffle (returns the same array) */
    shuffle(arr) {
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(next() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      return arr;
    },
    /** k distinct elements sampled without replacement */
    sample(arr, k) {
      return rng.shuffle(arr.slice()).slice(0, k);
    },
    /** weighted pick: items = [{value, weight}, ...] */
    weighted(items) {
      const total = items.reduce((s, it) => s + it.weight, 0);
      let r = next() * total;
      for (const it of items) {
        r -= it.weight;
        if (r < 0) return it.value;
      }
      return items[items.length - 1].value;
    },
    /** a "nice" round-ish number near `base`, jittered by ±jitterPct */
    around(base, jitterPct = 0.15) {
      const f = 1 + rng.range(-jitterPct, jitterPct);
      return base * f;
    },
  };
  return rng;
}
