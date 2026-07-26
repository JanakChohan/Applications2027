// -----------------------------------------------------------------------------
// lst/generate.js — scales lst / gapChallenge ("shape sudoku", a Latin square).
//
// Build a VALID Latin square over N shapes (each shape once per row and column),
// blank one cell as "?", and optionally blank a few off-row/off-column cells as
// pre-fillable scratch space (like the real test). The "?" answer is forced by
// its own fully-shown row (and confirmed by its column), so the ground truth is
// exact and — crucially — actually deducible from what's shown. verify.js checks
// both the Latin-square property and that exactly one shape fits the "?".
// -----------------------------------------------------------------------------

import { makeRng } from '../../generators/rng.js';
import { SHAPE_NAMES } from '../../ui/shapes.js';

const TIER = {
  beginner: { N: 4, scratch: 0 },
  intermediate: { N: 4, scratch: 2 },
  advanced: { N: 5, scratch: 3 },
};

export function generateItem(seed, tier, i, attempt = 0) {
  const rng = makeRng(`lst:${seed}:${tier}:${i}:${attempt}`);
  const cfg = TIER[tier] || TIER.intermediate;
  const N = cfg.N;

  const shapes = rng.sample(SHAPE_NAMES, N);
  const permRows = rng.shuffle([...Array(N).keys()]);
  const permCols = rng.shuffle([...Array(N).keys()]);
  // Valid Latin square: value index (permRows[r] + permCols[c]) % N → a shape.
  const solution = Array.from({ length: N }, (_, r) =>
    Array.from({ length: N }, (_, c) => shapes[(permRows[r] + permCols[c]) % N]));

  const askR = rng.int(0, N - 1), askC = rng.int(0, N - 1);
  const answer = solution[askR][askC];

  // scratch blanks: cells NOT in the asked row or column (so the "?" stays forced)
  const candidates = [];
  for (let r = 0; r < N; r++) for (let c = 0; c < N; c++) {
    if (r !== askR && c !== askC) candidates.push([r, c]);
  }
  const scratch = rng.sample(candidates, Math.min(cfg.scratch, candidates.length));

  // shown grid: null at asked + scratch
  const shown = solution.map((row) => row.slice());
  shown[askR][askC] = null;
  for (const [r, c] of scratch) shown[r][c] = null;

  return {
    module: 'lst', type: 'sudoku', tier,
    N, shapes, solution, shown,
    ask: { r: askR, c: askC }, scratch,
    answer,
    choices: shapes.slice(),
    prompt: 'Each shape appears once in every row and every column. Which shape belongs in the “?” cell?',
    traps: [],
  };
}
