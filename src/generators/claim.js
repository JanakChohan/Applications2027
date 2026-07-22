// -----------------------------------------------------------------------------
// claim.js — the STRUCTURED representation of a statement, plus the generator's
// evaluator.
//
// A statement shown to the user (e.g. "Research costs in FY8 exceeded $7m") is
// rendered from a `claim` object. The claim references dataset cells by meaning
// — {m: metric, e: entity, p: period} — never by pixel/tab position. That keeps
// the logic independent of how a tab happens to be drawn.
//
// IMPORTANT (design contract): this file is the GENERATOR's evaluator. The file
// verify/verifier.js contains a SEPARATE, independently-written evaluator. Both
// take the same claim + the same *visible* data and must agree on the label. If
// one has an arithmetic bug the other will disagree and the item is rejected
// before it is ever shown. A generated item with a wrong label is the worst bug
// in this whole app, so we pay for the redundancy on purpose.
//
// All arithmetic happens in BASE UNITS (actual dollars, actual headcount, raw
// percent points, raw index points). The dataset resolver is responsible for
// converting a tab's displayed value (e.g. "7,256" shown as "$ thousand") into
// base units (7,256,000) before it reaches this evaluator. That is what makes
// mixed-unit statements ("$7 million" vs a table in thousands) decidable.
// -----------------------------------------------------------------------------

/** Sentinel meaning "a required cell is not present in the visible data". */
export const MISSING = Symbol('MISSING');

export const LABEL = {
  TRUE: 'TRUE',
  FALSE: 'FALSE',
  CANNOT_SAY: 'CANNOT_SAY',
};

// ---- expression constructors (thin helpers so item code reads declaratively) -
export const cell = (m, e, p) => ({ cell: { m, e, p } });
export const num = (x) => ({ num: x });
export const add = (a, b) => ({ bin: 'add', a, b });
export const sub = (a, b) => ({ bin: 'sub', a, b });
export const mul = (a, b) => ({ bin: 'mul', a, b });
export const div = (a, b) => ({ bin: 'div', a, b });
export const sum = (refs) => ({ sum: refs });
export const pctChange = (from, to) => ({ pctChange: { from, to } });
export const pctPoints = (a, b) => ({ pctPoints: { a, b } });
export const shareOf = (part, whole) => ({ shareOf: { part, whole } });

/**
 * A resolver maps a cell ref -> a base-unit number, or undefined if the cell is
 * not available. The generator passes a resolver built from the VISIBLE dataset
 * (same view the candidate has), so "insufficient data" is detected honestly.
 */
export function evalExpr(expr, resolve) {
  if (expr == null) return MISSING;

  if ('num' in expr) return expr.num;

  if ('cell' in expr) {
    const v = resolve(expr.cell);
    return v === undefined || v === null || Number.isNaN(v) ? MISSING : v;
  }

  if ('sum' in expr) {
    let acc = 0;
    for (const r of expr.sum) {
      const v = evalExpr({ cell: r.cell ? r.cell : r }, resolve);
      if (v === MISSING) return MISSING;
      acc += v;
    }
    return acc;
  }

  if ('bin' in expr) {
    const a = evalExpr(expr.a, resolve);
    const b = evalExpr(expr.b, resolve);
    if (a === MISSING || b === MISSING) return MISSING;
    switch (expr.bin) {
      case 'add': return a + b;
      case 'sub': return a - b;
      case 'mul': return a * b;
      case 'div': return b === 0 ? MISSING : a / b;
      default: return MISSING;
    }
  }

  if ('pctChange' in expr) {
    const from = evalExpr(expr.pctChange.from, resolve);
    const to = evalExpr(expr.pctChange.to, resolve);
    if (from === MISSING || to === MISSING) return MISSING;
    if (from === 0) return MISSING;
    return ((to - from) / from) * 100;
  }

  if ('pctPoints' in expr) {
    const a = evalExpr(expr.pctPoints.a, resolve);
    const b = evalExpr(expr.pctPoints.b, resolve);
    if (a === MISSING || b === MISSING) return MISSING;
    return a - b; // both already in percent → difference is percentage POINTS
  }

  if ('shareOf' in expr) {
    const part = evalExpr(expr.shareOf.part, resolve);
    const whole = evalExpr(expr.shareOf.whole, resolve);
    if (part === MISSING || whole === MISSING) return MISSING;
    if (whole === 0) return MISSING;
    return (part / whole) * 100;
  }

  return MISSING;
}

/** Relative-epsilon equality, tolerant of floating-point noise only. */
function nearlyEqual(a, b, epsFrac = 1e-9) {
  const eps = Math.max(1e-9, Math.abs(b) * epsFrac);
  return Math.abs(a - b) <= eps;
}

/** Compare two numbers under an operator. `tol` used by 'approx'. */
export function compareNums(a, op, b, tol) {
  switch (op) {
    case '>': return a > b && !nearlyEqual(a, b);
    case '>=': return a > b || nearlyEqual(a, b);
    case '<': return a < b && !nearlyEqual(a, b);
    case '<=': return a < b || nearlyEqual(a, b);
    case '==': return nearlyEqual(a, b);
    case 'approx': {
      // tol may be absolute (number) or {frac} relative. Default 2% relative.
      const t = typeof tol === 'number' ? tol : Math.abs(b) * ((tol && tol.frac) || 0.02);
      return Math.abs(a - b) <= t;
    }
    default: return false;
  }
}

/**
 * Evaluate a whole claim against a resolver → 'TRUE' | 'FALSE' | 'CANNOT_SAY'.
 * This is the label the GENERATOR assigns. The verifier recomputes it separately.
 */
export function evalClaim(claim, resolve) {
  switch (claim.kind) {
    case 'cmp': {
      const a = evalExpr(claim.lhs, resolve);
      const b = evalExpr(claim.rhs, resolve);
      if (a === MISSING || b === MISSING) return LABEL.CANNOT_SAY;
      return compareNums(a, claim.op, b, claim.tol) ? LABEL.TRUE : LABEL.FALSE;
    }
    case 'trend': {
      const vals = claim.cells.map((r) => evalExpr({ cell: r }, resolve));
      if (vals.some((v) => v === MISSING)) return LABEL.CANNOT_SAY;
      return trendHolds(vals, claim.dir) ? LABEL.TRUE : LABEL.FALSE;
    }
    case 'rank': {
      const vals = claim.among.map((r) => evalExpr({ cell: r }, resolve));
      const tv = evalExpr({ cell: claim.target }, resolve);
      if (tv === MISSING || vals.some((v) => v === MISSING)) return LABEL.CANNOT_SAY;
      const extreme = claim.sel === 'max' ? Math.max(...vals) : Math.min(...vals);
      return nearlyEqual(tv, extreme) ? LABEL.TRUE : LABEL.FALSE;
    }
    default:
      return LABEL.CANNOT_SAY;
  }
}

/** Strict monotonic / flat check over an ordered value list. */
export function trendHolds(vals, dir) {
  for (let i = 1; i < vals.length; i++) {
    const d = vals[i] - vals[i - 1];
    if (dir === 'increasing' && !(d > 0)) return false;
    if (dir === 'decreasing' && !(d < 0)) return false;
    if (dir === 'flat' && Math.abs(d) > Math.abs(vals[i - 1]) * 0.001) return false;
  }
  return true;
}
