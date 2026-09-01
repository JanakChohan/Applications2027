// -----------------------------------------------------------------------------
// cls/generate.js — scales cls (inductive-logical grid categorisation).
//
// Pick a hidden binary RULE first, then build 3×3 grids of letters/digits whose
// group (A / B) is COMPUTED from the rule. Each item shows 6 correctly-coloured
// example grids (3 per group) plus one target grid to classify. Because the rule
// exists before the grids, every grid's true group is known and independently
// re-checkable (verify.js recomputes group() for the target and all examples).
// -----------------------------------------------------------------------------

import { makeRng } from '../../generators/rng.js';

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'K', 'M', 'P', 'R', 'S', 'T', 'X'];
const DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

const TIER = {
  beginner: ['centerDigit', 'moreLetters'],
  intermediate: ['containsChar', 'countChar2'],
  advanced: ['distinctEven', 'countChar3'],
};

const isDigit = (c) => c >= '0' && c <= '9';
const isLetter = (c) => !isDigit(c);
const countOf = (g, ch) => g.filter((c) => c === ch).length;
const distinct = (g) => new Set(g).size;
const numLetters = (g) => g.filter(isLetter).length;

/** The rule as a pure function grid → 'A' | 'B'. (Re-implemented in verify.js.) */
export function group(rule, g) {
  switch (rule.kind) {
    case 'centerDigit': return isDigit(g[4]) ? 'A' : 'B';
    case 'moreLetters': return numLetters(g) > 4 ? 'A' : 'B';
    case 'containsChar': return g.includes(rule.char) ? 'A' : 'B';
    case 'countChar2': return countOf(g, rule.char) >= 2 ? 'A' : 'B';
    case 'countChar3': return countOf(g, rule.char) >= 3 ? 'A' : 'B';
    case 'distinctEven': return distinct(g) % 2 === 0 ? 'A' : 'B';
    default: return 'B';
  }
}

export const ruleText = (rule) => ({
  centerDigit: 'the centre cell is a number (letters → the other group)',
  moreLetters: 'the grid contains more letters than digits',
  containsChar: `the grid contains the character “${rule.char}”`,
  countChar2: `the character “${rule.char}” appears at least twice`,
  countChar3: `the character “${rule.char}” appears at least three times`,
  distinctEven: 'the grid contains an even number of distinct characters',
}[rule.kind]);

function randCell(rng) { return rng.chance(0.5) ? rng.pick(LETTERS) : rng.pick(DIGITS); }

/** Construct a grid in the desired group (constructive → balanced, then verified). */
function makeGrid(rule, want, rng) {
  const g = Array.from({ length: 9 }, () => randCell(rng));
  const set = (i, v) => { g[i] = v; };
  switch (rule.kind) {
    case 'centerDigit': set(4, want === 'A' ? rng.pick(DIGITS) : rng.pick(LETTERS)); break;
    case 'moreLetters': {
      const nLet = want === 'A' ? rng.int(5, 8) : rng.int(1, 4);
      const idx = rng.shuffle([...Array(9).keys()]);
      idx.forEach((p, k) => set(p, k < nLet ? rng.pick(LETTERS) : rng.pick(DIGITS)));
      break;
    }
    case 'containsChar': {
      // remove any incidental occurrences first, then add if wanted
      for (let i = 0; i < 9; i++) if (g[i] === rule.char) g[i] = altOf(rule.char, rng);
      if (want === 'A') set(rng.int(0, 8), rule.char);
      break;
    }
    case 'countChar2':
    case 'countChar3': {
      const need = rule.kind === 'countChar2' ? 2 : 3;
      for (let i = 0; i < 9; i++) if (g[i] === rule.char) g[i] = altOf(rule.char, rng);
      const put = want === 'A' ? need + rng.int(0, 1) : rng.int(0, need - 1);
      const idx = rng.shuffle([...Array(9).keys()]);
      for (let k = 0; k < put; k++) set(idx[k], rule.char);
      break;
    }
    case 'distinctEven': {
      for (let tries = 0; tries < 40; tries++) {
        for (let i = 0; i < 9; i++) g[i] = randCell(rng);
        if ((distinct(g) % 2 === 0 ? 'A' : 'B') === want) break;
      }
      break;
    }
    default: break;
  }
  return g;
}
function altOf(ch, rng) { const alt = [...LETTERS, ...DIGITS].filter((c) => c !== ch); return rng.pick(alt); }

export function generateItem(seed, tier, i, attempt = 0, focus = null, wantGroup = null) {
  const rng = makeRng(`cls:${seed}:${tier}:${i}:${attempt}`);
  const pool = TIER[tier] || TIER.intermediate;
  const inFocus = focus ? focus.filter((f) => pool.includes(f)) : [];
  const kind = inFocus.length && rng.chance(0.7) ? rng.pick(inFocus) : rng.pick(pool);
  const rule = { kind };
  if (kind === 'containsChar' || kind === 'countChar2' || kind === 'countChar3') rule.char = rng.pick([...LETTERS.slice(0, 8), ...DIGITS.slice(0, 6)]);

  // build 3 A + 3 B examples and one target, each verified to fall in its group
  const grid = (want) => {
    for (let t = 0; t < 60; t++) { const g = makeGrid(rule, want, rng); if (group(rule, g) === want) return g; }
    return null;
  };
  const examples = [];
  for (const want of ['A', 'A', 'A', 'B', 'B', 'B']) {
    const g = grid(want); if (!g) return null;
    examples.push({ grid: g, group: want });
  }
  rng.shuffle(examples);
  const targetGroup = wantGroup || (rng.chance(0.5) ? 'A' : 'B');
  const target = grid(targetGroup);
  if (!target) return null;

  return {
    module: 'cls', type: 'categorise', tier,
    rule, examples, target, answer: targetGroup,
    choices: ['A', 'B'],
    prompt: 'The coloured grids are sorted into two groups by a hidden rule. Which group does the last grid belong to?',
    traps: [kind],
  };
}
