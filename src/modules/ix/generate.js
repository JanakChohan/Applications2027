// -----------------------------------------------------------------------------
// ix/generate.js — scales ix ("discovering rules" / inductive odd-one-out).
//
// A series of 9 shape-objects share a hidden RULE; exactly one breaks it. We pick
// an explicit rule, build 8 objects that satisfy it and 1 that violates it, and
// hold every OTHER attribute constant so the violator is the UNIQUE odd one (no
// second property accidentally singles out a different object). The breaker index
// is the verified answer; verify.js re-checks that exactly one object violates the
// rule and that it sits at that index.
// -----------------------------------------------------------------------------

import { makeRng } from '../../generators/rng.js';
import { SHAPE_COLORS } from '../../ui/shapes.js';

const EVEN = ['square', 'hexagon', 'octagon'];
const ODD = ['triangle', 'pentagon', 'heptagon'];
const ALL_SHAPES = ['triangle', 'square', 'pentagon', 'hexagon', 'octagon'];
const ROT = [0, 45, 90, 135, 180, 225, 270, 315];

const TIER = {
  beginner: ['sameShape', 'filled', 'sameRotation'],
  intermediate: ['hasInner', 'sameRotation', 'filled'],
  advanced: ['evenSides', 'hasInner', 'sameShape'],
};

export function sideCount(shape) {
  return { circle: 0, triangle: 3, square: 4, pentagon: 5, hexagon: 6, heptagon: 7, octagon: 8, diamond: 4, star: 5 }[shape] ?? 4;
}

/** Does an object satisfy the rule? (Re-implemented independently in verify.js.) */
export function satisfies(rule, o) {
  switch (rule.kind) {
    case 'sameShape': return o.shape === rule.value;
    case 'filled': return o.filled === rule.value;
    case 'sameRotation': return o.rotation === rule.value;
    case 'hasInner': return (o.inner != null) === rule.value;
    case 'evenSides': return sideCount(o.shape) % 2 === 0;
    default: return true;
  }
}

export const ruleText = {
  sameShape: (r) => `every object is a ${r.value}`,
  filled: (r) => `every object is ${r.value ? 'solid (filled)' : 'an outline'}`,
  sameRotation: (r) => `every object has the same orientation`,
  hasInner: (r) => `every object ${r.value ? 'contains a smaller inner shape' : 'has no inner shape'}`,
  evenSides: () => `every shape has an even number of sides`,
};

export function generateItem(seed, tier, i, attempt = 0, focus = null) {
  const rng = makeRng(`ix:${seed}:${tier}:${i}:${attempt}`);
  const pool = TIER[tier] || TIER.intermediate;
  // Adaptive focus: over-serve weak rule kinds that exist in this tier.
  const inFocus = focus ? focus.filter((f) => pool.includes(f)) : [];
  const kind = inFocus.length && rng.chance(0.7) ? rng.pick(inFocus) : rng.pick(pool);
  const color = SHAPE_COLORS[0];

  // constant "background" attributes shared by all 9 (except the rule attribute)
  const constShape = rng.pick(ALL_SHAPES);
  const constRot = rng.pick(ROT);
  const constFilled = rng.chance(0.6);
  const constInner = rng.pick(['triangle', 'square', 'circle']);

  let base, rule, breaker;
  const mk = (o) => ({ shape: constShape, filled: constFilled, rotation: constRot, inner: null, color, ...o });

  switch (kind) {
    case 'sameShape': {
      rule = { kind, value: constShape };
      base = mk({});
      breaker = mk({ shape: rng.pick(ALL_SHAPES.filter((s) => s !== constShape)) });
      break;
    }
    case 'filled': {
      rule = { kind, value: constFilled };
      base = mk({ filled: constFilled });
      breaker = mk({ filled: !constFilled });
      break;
    }
    case 'sameRotation': {
      // give the shape rotational asymmetry so orientation is visible
      const shp = rng.pick(['triangle', 'pentagon', 'heptagon']);
      rule = { kind, value: constRot };
      base = mk({ shape: shp, rotation: constRot });
      breaker = mk({ shape: shp, rotation: rng.pick(ROT.filter((r) => Math.abs(r - constRot) >= 90 && Math.abs(r - constRot) <= 270)) });
      break;
    }
    case 'hasInner': {
      const present = rng.chance(0.5);
      rule = { kind, value: present };
      base = mk({ inner: present ? constInner : null });
      breaker = mk({ inner: present ? null : constInner });
      break;
    }
    case 'evenSides':
    default: {
      rule = { kind: 'evenSides' };
      // conformers vary across the EVEN set (richer), breaker is odd-sided
      base = null; // handled below
      breaker = mk({ shape: rng.pick(ODD) });
      break;
    }
  }

  const breakerIndex = rng.int(0, 8);
  const objects = [];
  for (let k = 0; k < 9; k++) {
    if (k === breakerIndex) { objects.push(breaker); continue; }
    if (kind === 'evenSides') objects.push(mk({ shape: rng.pick(EVEN) }));
    else objects.push({ ...base });
  }

  return {
    module: 'ix', type: 'oddoneout', tier,
    objects, rule, breakerIndex,
    answer: String(breakerIndex),
    choices: objects.map((_, k) => String(k)),
    prompt: 'Eight of these nine objects follow one rule. Click the ONE object that breaks it.',
    traps: [kind],
  };
}
