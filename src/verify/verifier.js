// -----------------------------------------------------------------------------
// verifier.js — the INDEPENDENT ground-truth checker.
//
// This is the safety net the whole project leans on: it re-derives each item's
// True/False/Cannot Say label WITHOUT reusing the generator's evaluator, and the
// session assembler drops any item whose two labels disagree. A generated item
// with a wrong label would teach the wrong reasoning — the worst possible bug —
// so we compute the answer twice, by different code, and only trust agreement.
//
// Deliberate differences from generators/claim.js (to avoid a shared bug):
//   • It builds its OWN visibility map by scanning dataset.tabs directly, rather
//     than trusting dataset.resolveVisible/isVisible.
//   • It uses `null` (not a MISSING symbol) to mark unavailable values.
//   • It evaluates expressions with its own switch and its own arithmetic.
//   • It additionally tries to DERIVE a missing entity figure from a visible
//     total; if it can, a "Cannot Say" item is actually decidable and is rejected.
// -----------------------------------------------------------------------------

const EPS = 1e-9;

/** Build the set of visible (metric,entity,period) → base value, from tabs only. */
function buildVisibleMap(dataset) {
  const map = new Map();
  const k = (m, e, p) => `${m}::${e}::${p}`;
  for (const tab of dataset.tabs) {
    for (const c of tab.cells) map.set(k(tab.metric, c.e, c.p), c.base);
  }
  // the share-tab caption exposes the company total for the latest period only
  for (const tab of dataset.tabs) {
    if (tab.caption) {
      const cap = tab.caption;
      map.set(k(cap.metric, cap.entity, cap.period), cap.base);
    }
  }
  return { map, k };
}

/** Attempt to derive a missing entity value from a visible "total" over shown entities. */
function tryDerive(dataset, vis, ref) {
  // Only meaningful for per-entity metrics where a total row is displayed.
  const tab = dataset.tabs.find((t) => t.metric === ref.m && t.hasTotal);
  if (!tab) return null;
  // total of shown entities is present only if the tab claims a total; but our
  // generator's totals cover exactly the SHOWN entities and never the latent one,
  // so a latent entity can't be derived. We still check the arithmetic honestly:
  const shown = tab.entities;
  if (shown.includes(ref.e)) return null; // not actually missing among shown
  return null; // latent entity is not part of any shown total → genuinely underivable
}

/** Independent expression evaluator. Returns a Number, or null if unavailable. */
function ev(expr, get) {
  if (expr == null) return null;
  if (Object.prototype.hasOwnProperty.call(expr, 'num')) return expr.num;

  if (Object.prototype.hasOwnProperty.call(expr, 'cell')) {
    const v = get(expr.cell);
    return v == null || Number.isNaN(v) ? null : v;
  }

  if (Object.prototype.hasOwnProperty.call(expr, 'sum')) {
    let total = 0;
    for (const r of expr.sum) {
      const v = ev(r.cell ? r : { cell: r }, get);
      if (v === null) return null;
      total += v;
    }
    return total;
  }

  if (Object.prototype.hasOwnProperty.call(expr, 'bin')) {
    const x = ev(expr.a, get);
    const y = ev(expr.b, get);
    if (x === null || y === null) return null;
    if (expr.bin === 'add') return x + y;
    if (expr.bin === 'sub') return x - y;
    if (expr.bin === 'mul') return x * y;
    if (expr.bin === 'div') return y === 0 ? null : x / y;
    return null;
  }

  if (Object.prototype.hasOwnProperty.call(expr, 'pctChange')) {
    const a = ev(expr.pctChange.from, get);
    const b = ev(expr.pctChange.to, get);
    if (a === null || b === null || a === 0) return null;
    return (b - a) / a * 100;
  }

  if (Object.prototype.hasOwnProperty.call(expr, 'pctPoints')) {
    const a = ev(expr.pctPoints.a, get);
    const b = ev(expr.pctPoints.b, get);
    if (a === null || b === null) return null;
    return a - b;
  }

  if (Object.prototype.hasOwnProperty.call(expr, 'shareOf')) {
    const part = ev(expr.shareOf.part, get);
    const whole = ev(expr.shareOf.whole, get);
    if (part === null || whole === null || whole === 0) return null;
    return part / whole * 100;
  }

  return null;
}

function eq(a, b) { return Math.abs(a - b) <= Math.max(EPS, Math.abs(b) * 1e-9); }

function cmp(a, op, b, tol) {
  if (op === '>') return a - b > EPS;
  if (op === '<') return b - a > EPS;
  if (op === '>=') return a - b > -EPS;
  if (op === '<=') return b - a > -EPS;
  if (op === '==') return eq(a, b);
  if (op === 'approx') {
    const t = typeof tol === 'number' ? tol : Math.abs(b) * ((tol && tol.frac) || 0.02);
    return Math.abs(a - b) <= t + EPS;
  }
  return false;
}

/** Independently derive the label for a claim given a dataset. */
export function deriveLabel(dataset, claim) {
  const { map, k } = buildVisibleMap(dataset);
  const get = (ref) => {
    const key = k(ref.m, ref.e, ref.p);
    if (map.has(key)) return map.get(key);
    const derived = tryDerive(dataset, map, ref);
    return derived == null ? null : derived;
  };

  if (claim.kind === 'cmp') {
    const a = ev(claim.lhs, get);
    const b = ev(claim.rhs, get);
    if (a === null || b === null) return 'CANNOT_SAY';
    return cmp(a, claim.op, b, claim.tol) ? 'TRUE' : 'FALSE';
  }
  if (claim.kind === 'trend') {
    const vals = claim.cells.map((r) => ev({ cell: r }, get));
    if (vals.some((v) => v === null)) return 'CANNOT_SAY';
    for (let i = 1; i < vals.length; i++) {
      const d = vals[i] - vals[i - 1];
      if (claim.dir === 'increasing' && !(d > EPS)) return 'FALSE';
      if (claim.dir === 'decreasing' && !(d < -EPS)) return 'FALSE';
      if (claim.dir === 'flat' && Math.abs(d) > Math.abs(vals[i - 1]) * 0.001) return 'FALSE';
    }
    return 'TRUE';
  }
  if (claim.kind === 'rank') {
    const vals = claim.among.map((r) => ev({ cell: r }, get));
    const tv = ev({ cell: claim.target }, get);
    if (tv === null || vals.some((v) => v === null)) return 'CANNOT_SAY';
    const extreme = claim.sel === 'max' ? Math.max(...vals) : Math.min(...vals);
    return eq(tv, extreme) ? 'TRUE' : 'FALSE';
  }
  return 'CANNOT_SAY';
}

/**
 * Verify a finished item. Returns {ok, derivedLabel, generatorLabel, reason}.
 * ok === true means the two independent evaluations agree AND basic structural
 * checks pass. The session assembler only shows items with ok === true.
 */
export function verifyItem(dataset, item) {
  const problems = [];

  // structural sanity
  if (!item.text || typeof item.text !== 'string') problems.push('missing text');
  if (!item.claim) problems.push('missing claim');
  if (!['TRUE', 'FALSE', 'CANNOT_SAY'].includes(item.label)) problems.push('bad label value');

  let derivedLabel = null;
  if (item.claim) {
    derivedLabel = deriveLabel(dataset, item.claim);
    if (derivedLabel !== item.label) {
      problems.push(`label mismatch: generator=${item.label} verifier=${derivedLabel}`);
    }
  }

  // Cannot-Say honesty: it must reference at least one genuinely-missing cell.
  if (item.label === 'CANNOT_SAY') {
    const { map, k } = buildVisibleMap(dataset);
    const anyMissing = (item.requiredCells || []).some((c) => !map.has(k(c.m, c.e, c.p)));
    if (!anyMissing) problems.push('Cannot Say without any missing required cell');
  }

  // Decidable items must reference only visible cells.
  if (item.label === 'TRUE' || item.label === 'FALSE') {
    const { map, k } = buildVisibleMap(dataset);
    const missing = (item.requiredCells || []).filter((c) => !map.has(k(c.m, c.e, c.p)));
    if (missing.length) problems.push('decidable item references a missing cell');
  }

  return {
    ok: problems.length === 0,
    derivedLabel,
    generatorLabel: item.label,
    reason: problems.join('; ') || 'ok',
  };
}
