// lst/verify.js — INDEPENDENT verifier for shape-sudoku.
// Rebuilds the answer from the SHOWN puzzle (not the stored answer) and checks:
//   1. the full solution is a genuine Latin square (each row & column a permutation);
//   2. exactly ONE shape is consistent with the "?" cell's row AND column givens;
//   3. that unique shape equals the stored answer.
// Different code path from generate.js → catches a wrong-labelled "?".

function isPermutation(arr, shapes) {
  if (arr.length !== shapes.length) return false;
  const set = new Set(arr);
  return set.size === shapes.length && shapes.every((s) => set.has(s));
}

/** Shapes still allowed in (r,c) given the shown grid's row + column. */
function candidates(shown, shapes, r, c) {
  const used = new Set();
  for (let k = 0; k < shown.length; k++) {
    if (shown[r][k]) used.add(shown[r][k]);
    if (shown[k][c]) used.add(shown[k][c]);
  }
  return shapes.filter((s) => !used.has(s));
}

export function verifyItem(item) {
  const problems = [];
  const { solution, shown, shapes, N, ask, answer } = item;

  // 1. Latin square check on the full solution
  for (let r = 0; r < N; r++) if (!isPermutation(solution[r], shapes)) problems.push(`row ${r} not a permutation`);
  for (let c = 0; c < N; c++) {
    const col = solution.map((row) => row[c]);
    if (!isPermutation(col, shapes)) problems.push(`col ${c} not a permutation`);
  }

  // 2 & 3. the "?" must be uniquely forced and equal to the stored answer
  const cand = candidates(shown, shapes, ask.r, ask.c);
  if (cand.length !== 1) problems.push(`"?" not uniquely determined (${cand.length} candidates)`);
  else if (cand[0] !== answer) problems.push(`answer mismatch: forced=${cand[0]} stored=${answer}`);
  if (solution[ask.r][ask.c] !== answer) problems.push('stored answer disagrees with solution grid');

  return { ok: problems.length === 0, derivedLabel: cand.length === 1 ? cand[0] : null, generatorLabel: answer, reason: problems.join('; ') || 'ok' };
}

/** The deduction chain for coaching (which givens force the answer). */
export function deduction(item) {
  const { shown, shapes, ask } = item;
  const rowShapes = shown[ask.r].filter(Boolean);
  const colShapes = shown.map((row) => row[ask.c]).filter(Boolean);
  const missingFromRow = shapes.filter((s) => !rowShapes.includes(s));
  return { rowShapes, colShapes, missingFromRow };
}
