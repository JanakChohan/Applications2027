// -----------------------------------------------------------------------------
// items.js — turn a dataset into individual True/False/Cannot Say statements.
//
// Contract for every generator:
//   • Build a STRUCTURED claim (see claim.js) over dataset cells.
//   • Render English text FROM that claim (never the other way round).
//   • Compute the label with evalClaim against the VISIBLE resolver — i.e. the
//     exact same view the candidate has. The label is COMPUTED, never asserted,
//     so a mis-aimed "False" that lands True is still correctly labelled.
//   • Emit worked-solution material: which tab each figure is on, the arithmetic,
//     and (for Cannot Say) the name of the missing datum.
//
// "Cannot Say" is only ever produced by referencing a LATENT cell — a period,
// entity, or metric that exists in the world but appears on no tab — so the
// label is provably correct, not a matter of vagueness (research/SPEC.md §7).
//
// The session assembler (session.js) still runs every finished item through the
// INDEPENDENT verifier and drops any whose verifier-label disagrees. This file
// aims to be correct; the verifier guarantees it.
// -----------------------------------------------------------------------------

import {
  cell, num, sub, div, sum, pctChange, pctPoints, shareOf, evalClaim, LABEL,
} from './claim.js';
import { money, count as fmtCount, percent as fmtPct, group, formatValue } from './format.js';

// ---- small helpers ----------------------------------------------------------

const TITLES_LOWER = (dataset, role) => dataset.theme.titles[role].toLowerCase();

function tabFor(dataset, metric) {
  return dataset.tabs.find((t) => t.metric === metric) || null;
}

/** Human description of a cell ref for worked solutions. */
function refInfo(dataset, ref) {
  const tab = tabFor(dataset, ref.m);
  const base = dataset.resolveWorld(ref);
  const visible = dataset.isVisible(ref);
  const roleTitle = tab ? tab.title
    : ref.m === 'revenueTotal' ? `Total ${dataset.theme.titles.revenue}`
    : ref.m === 'latent' ? dataset.meta.latentMetricLabel
    : ref.m;
  const entityText = ref.e === '__ALL__' ? '' : ref.e;
  return { tab, base, visible, roleTitle, entityText, period: ref.p, unit: dataset.units[ref.m] };
}

/** Walk a claim collecting every cell ref it depends on. */
function collectRefs(claim) {
  const out = [];
  const walkExpr = (e) => {
    if (!e || typeof e !== 'object') return;
    if ('cell' in e) out.push(e.cell);
    if ('bin' in e) { walkExpr(e.a); walkExpr(e.b); }
    if ('sum' in e) e.sum.forEach((r) => out.push(r.cell || r));
    if ('pctChange' in e) { walkExpr(e.pctChange.from); walkExpr(e.pctChange.to); }
    if ('pctPoints' in e) { walkExpr(e.pctPoints.a); walkExpr(e.pctPoints.b); }
    if ('shareOf' in e) { walkExpr(e.shareOf.part); walkExpr(e.shareOf.whole); }
  };
  if (claim.kind === 'cmp') { walkExpr(claim.lhs); walkExpr(claim.rhs); }
  if (claim.kind === 'trend') claim.cells.forEach((r) => out.push(r));
  if (claim.kind === 'rank') { claim.among.forEach((r) => out.push(r)); out.push(claim.target); }
  return out;
}

/** Round a base-unit value to a clean DISPLAY figure, return base units. */
function niceValue(base, unit) {
  const d = base / unit.scale;
  const mag = Math.pow(10, Math.floor(Math.log10(Math.abs(d) || 1)));
  const step = mag / (unit.kind === 'currency' && unit.scale >= 1e6 ? 10 : 2);
  return Math.round(d / step) * step * unit.scale;
}
function stepOf(base, unit) {
  const d = base / unit.scale;
  const mag = Math.pow(10, Math.floor(Math.log10(Math.abs(d) || 1)));
  return (mag / (unit.kind === 'currency' && unit.scale >= 1e6 ? 10 : 2)) * unit.scale;
}

// How far a threshold sits from the true value, by tier. Beginner thresholds are
// wide enough to eyeball; ADVANCED thresholds are deliberate near-misses (a few
// percent off) so estimation fails and you must actually compute — that is what
// the real advanced items feel like under the ~20s/item clock.
const MARGIN = {
  beginner: { above: [1.15, 1.25, 1.4], below: [0.6, 0.75, 0.85], pct: [0.5, 0.7, 1.4, 1.7] },
  intermediate: { above: [1.06, 1.12, 1.2], below: [0.8, 0.88, 0.94], pct: [0.6, 0.85, 1.15, 1.4] },
  advanced: { above: [1.025, 1.045, 1.08], below: [0.92, 0.955, 0.975], pct: [0.85, 0.93, 1.08, 1.15] },
};
const marginOf = (tier) => MARGIN[tier] || MARGIN.intermediate;

/** A threshold near `base` on a chosen side, as clean display units, never equal to the rounded actual. */
function threshold(rng, base, unit, wantAbove, tier = 'intermediate') {
  const m = marginOf(tier);
  const factor = wantAbove ? rng.pick(m.above) : rng.pick(m.below);
  let t = niceValue(base * factor, unit);
  // On tight margins rounding can land exactly on the actual value — nudge one
  // display step to the wanted side so "exceeded X" is never a coin-flip on ties.
  if (t === niceValue(base, unit)) t += (wantAbove ? 1 : -1) * stepOf(base, unit);
  return t;
}

function pickVisibleEntity(rng, dataset) { return rng.pick(dataset.entitiesVisible); }
function latestPeriod(dataset) { return dataset.periodsVisible[dataset.periodsVisible.length - 1]; }

/** Phrase a value for the rhs of a comparison, in the metric's unit. */
function phraseValue(dataset, metric, base, opts = {}) {
  const unit = dataset.units[metric];
  if (unit.kind === 'currency') {
    // optionally use a DIFFERENT unit word than the tab → unit-conversion trap
    const word = opts.forceWord || unit.word;
    return money(base, word, unit.symbol);
  }
  if (unit.kind === 'percent') return fmtPct(base, 1);
  if (unit.kind === 'index') return `${group(base, 0)} points`;
  return fmtCount(base, unit.label);
}

function verb(op) {
  return op === '>' ? 'exceeded' : op === '<' ? 'was less than'
    : op === '>=' ? 'was at least' : op === '<=' ? 'was at most' : 'was';
}
function verbAlt(rng, op) {
  if (op === '>') return rng.pick(['exceeded', 'was greater than', 'was above', 'was more than']);
  if (op === '<') return rng.pick(['was less than', 'was below', 'did not reach', 'stayed under']);
  return verb(op);
}

/** Pick one phrasing template — same claim, varied English, so items never read canned. */
function phrase(rng, variants) { return rng.pick(variants); }

// Assemble a finished item from parts (computes the label independently-of-intent).
function finalize(dataset, { type, traps, claim, text, tier, narrative }) {
  const label = evalClaim(claim, dataset.resolveVisible);
  const refs = collectRefs(claim).map((r) => ({ ...r, info: refInfo(dataset, r) }));
  return {
    type, traps: traps || [], tier, claim, text, label,
    requiredCells: refs.map((r) => ({
      m: r.m, e: r.e, p: r.p,
      tab: r.info.tab ? r.info.tab.id : null,
      title: r.info.roleTitle, visible: r.info.visible,
      display: r.info.base != null ? formatValue(r.info.unit, r.info.base) : null,
    })),
    solution: buildSolution(dataset, { type, claim, label, narrative, refs }),
  };
}

// -----------------------------------------------------------------------------
// worked-solution builder
// -----------------------------------------------------------------------------
function buildSolution(dataset, { claim, label, narrative, refs }) {
  const steps = [];
  const visibleRefs = refs.filter((r) => r.info.visible);
  const missingRefs = refs.filter((r) => !r.info.visible);

  for (const r of visibleRefs) {
    const i = r.info;
    steps.push(
      `Open the “${i.roleTitle}” tab. Read ${i.entityText ? i.entityText + ', ' : ''}${i.period}: ` +
      `${formatValue(i.unit, i.base)}.`
    );
  }
  if (narrative) narrative.forEach((s) => steps.push(s));

  let rationale;
  if (label === LABEL.CANNOT_SAY) {
    const m = missingRefs[0]?.info;
    const why = m
      ? whyMissing(dataset, missingRefs[0])
      : 'a figure the statement needs is not shown on any tab';
    rationale =
      `The statement requires ${describeMissing(dataset, missingRefs[0])}, but ${why}. ` +
      `Because a required figure is not available from the six data displays, the answer is ` +
      `Cannot Say — it is neither confirmed nor contradicted.`;
  } else {
    rationale =
      label === LABEL.TRUE
        ? 'Every figure the statement needs is shown, and the data confirms it — so True.'
        : 'Every figure the statement needs is shown, and the data contradicts it — so False.';
  }
  return { steps, rationale, answer: label };
}

function describeMissing(dataset, ref) {
  if (!ref) return 'a figure that is not displayed';
  const i = ref.info;
  return `${i.roleTitle}${i.entityText ? ' for ' + i.entityText : ''} in ${i.period}`;
}
function whyMissing(dataset, ref) {
  const i = ref.info;
  if (ref.m === 'latent') {
    return `no tab shows ${dataset.meta.latentMetricLabel} — the displays only give ` +
      `${dataset.tabs.map((t) => t.title.toLowerCase()).join(', ')}`;
  }
  if (ref.e === dataset.entityLatent) {
    return `${dataset.entityLatent} does not appear on any tab (only ` +
      `${dataset.entitiesVisible.join(', ')} are shown)`;
  }
  if (dataset.periodLatentBefore.includes(ref.p) || dataset.periodLatentAfter.includes(ref.p)) {
    return `${ref.p} is outside the range shown (only ${dataset.periodsVisible.join(', ')} are given)`;
  }
  if (ref.m === 'revenueTotal') {
    return `a company-wide total is only given for ${latestPeriod(dataset)}, not ${ref.p}`;
  }
  return 'that figure is not shown on any tab';
}

// -----------------------------------------------------------------------------
// the nine item-type generators
// -----------------------------------------------------------------------------

// 1. DIRECT LOOKUP — read one figure, compare to a threshold.
function genLookup(dataset, rng, tier, aim) {
  const metric = rng.pick(['revenue', 'costs', 'headcount', 'margin']);
  const e = pickVisibleEntity(rng, dataset);
  let p = latestOrLatent(dataset, rng, aim);
  const ref = { m: metric, e, p };
  const unit = dataset.units[metric];
  const actual = dataset.resolveWorld(ref);

  // Unit trap on harder tiers: phrase a currency threshold in the other word.
  const traps = [];
  let forceWord;
  if (tier !== 'beginner' && unit.kind === 'currency' && rng.chance(0.5)) {
    forceWord = unit.word === 'million' ? 'thousand' : 'million';
    traps.push('unit');
  }

  // Occasionally an exact-equality "close but not exact" item.
  if (aim !== LABEL.CANNOT_SAY && unit.kind === 'currency' && rng.chance(0.25)) {
    const wrong = rng.chance(0.5);
    const nudge = tier === 'advanced' ? rng.pick([1.015, 0.985]) : rng.pick([1.03, 0.97]);
    const tgt = wrong ? niceValue(actual * nudge, unit) : actual;
    traps.push('exactness');
    const claim = { kind: 'cmp', lhs: cell(metric, e, p), op: '==', rhs: num(tgt) };
    return finalize(dataset, {
      type: 'lookup', traps, tier, claim,
      text: `${dataset.theme.titles[metricRole(metric)]} for ${e} in ${p} was exactly ` +
        `${phraseValue(dataset, metric, tgt, { forceWord })}.`,
    });
  }

  const op = rng.pick(['>', '<']);
  const wantAbove = op === '<'; // threshold above actual makes "<" true, ">" false, etc.
  const tgt = threshold(rng, actual, unit, wantAbove, tier);
  const claim = { kind: 'cmp', lhs: cell(metric, e, p), op, rhs: num(tgt) };
  const title = dataset.theme.titles[metricRole(metric)];
  const val = phraseValue(dataset, metric, tgt, { forceWord });
  return finalize(dataset, {
    type: 'lookup', traps, tier, claim,
    text: phrase(rng, [
      `${title} for ${e} in ${p} ${verbAlt(rng, op)} ${val}.`,
      `In ${p}, ${title.toLowerCase()} recorded for ${e} ${verbAlt(rng, op)} ${val}.`,
      `${e} reported ${title.toLowerCase()} ${op === '>' ? 'of more than' : 'of less than'} ${val} in ${p}.`,
    ]),
  });
}

// 2. SINGLE-STEP ARITHMETIC — difference between two periods (or entities).
function genArithmetic(dataset, rng, tier, aim) {
  const metric = rng.pick(['revenue', 'costs', 'headcount']);
  const unit = dataset.units[metric];
  const e = pickVisibleEntity(rng, dataset);
  const [p1, p2] = orderedPeriods(dataset, rng, aim);
  const v1 = dataset.resolveWorld({ m: metric, e, p: p1 });
  const v2 = dataset.resolveWorld({ m: metric, e, p: p2 });
  const diff = Math.abs(v2 - v1);
  const rising = v2 >= v1;
  const tgt = threshold(rng, diff || unit.scale, unit, rng.chance(), tier);
  const lhs = rising ? sub(cell(metric, e, p2), cell(metric, e, p1))
    : sub(cell(metric, e, p1), cell(metric, e, p2));
  const claim = { kind: 'cmp', lhs, op: '>', rhs: num(tgt) };
  const dir = rising ? 'increased' : 'decreased';
  const title = dataset.theme.titles[metricRole(metric)];
  return finalize(dataset, {
    type: 'arithmetic', traps: [], tier, claim,
    text: phrase(rng, [
      `${title} for ${e} ${dir} by more than ${phraseValue(dataset, metric, tgt)} between ${p1} and ${p2}.`,
      `Between ${p1} and ${p2}, ${e}'s ${title.toLowerCase()} ${rising ? 'rose' : 'fell'} by more than ${phraseValue(dataset, metric, tgt)}.`,
      `The ${rising ? 'increase' : 'decrease'} in ${title.toLowerCase()} for ${e} from ${p1} to ${p2} was greater than ${phraseValue(dataset, metric, tgt)}.`,
    ]),
    narrative: [
      `Compute the change: |${p2} − ${p1}| = ${formatValue(unit, diff)}.`,
      `Compare with the stated ${formatValue(unit, tgt)}.`,
    ],
  });
}

// 3. PERCENTAGE CHANGE — divide the change by the ORIGINAL value.
function genPctChange(dataset, rng, tier, aim) {
  const metric = rng.pick(['revenue', 'costs']);
  const e = pickVisibleEntity(rng, dataset);
  const [p1, p2] = orderedPeriods(dataset, rng, aim);
  const v1 = dataset.resolveWorld({ m: metric, e, p: p1 });
  const v2 = dataset.resolveWorld({ m: metric, e, p: p2 });
  const pc = ((v2 - v1) / v1) * 100;
  const tgtPct = Math.max(1, Math.round(Math.abs(pc) * rng.pick(marginOf(tier).pct)));
  const op = rng.pick(['>', '<']);
  // Keep the rhs sign consistent with the direction the wording describes.
  const rhsPct = op === '>' ? tgtPct : -tgtPct;
  const claim = { kind: 'cmp', lhs: pctChange(cell(metric, e, p1), cell(metric, e, p2)), op, rhs: num(rhsPct) };
  const title = dataset.theme.titles[metricRole(metric)];
  return finalize(dataset, {
    type: 'pct_change', traps: ['pct_change'], tier, claim,
    text: phrase(rng, [
      `${title} for ${e} ${op === '>' ? 'rose by more than' : 'fell by more than'} ${tgtPct}% between ${p1} and ${p2}.`,
      `Between ${p1} and ${p2}, ${e}'s ${title.toLowerCase()} ${op === '>' ? 'grew by over' : 'declined by over'} ${tgtPct}%.`,
    ]),
    narrative: [
      `Percentage change = (new − old) ÷ old × 100 = ` +
      `(${formatValue(dataset.units[metric], v2)} − ${formatValue(dataset.units[metric], v1)}) ÷ ` +
      `${formatValue(dataset.units[metric], v1)} × 100 = ${pc.toFixed(1)}%.`,
      `Note: divide by the ORIGINAL (${p1}) value, not the new one.`,
    ],
  });
}

// 4. PERCENTAGE POINTS vs PERCENT — the classic pp/% confusion (uses a % metric).
function genPctPoints(dataset, rng, tier, aim) {
  const metric = 'margin';
  const e = pickVisibleEntity(rng, dataset);
  const [p1, p2] = orderedPeriods(dataset, rng, aim);
  const m1 = dataset.resolveWorld({ m: metric, e, p: p1 });
  const m2 = dataset.resolveWorld({ m: metric, e, p: p2 });
  const pointsChange = m2 - m1;
  const asPoints = rng.chance(0.5); // half phrased as points, half as relative %
  const title = dataset.theme.titles.margin;
  const ppMul = tier === 'advanced' ? [0.8, 1.2] : [0.6, 1.3];
  if (asPoints) {
    const tgt = Math.max(1, Math.round(Math.abs(pointsChange) * rng.pick(ppMul)));
    const claim = {
      kind: 'cmp',
      lhs: pointsChange >= 0 ? pctPoints(cell(metric, e, p2), cell(metric, e, p1))
        : pctPoints(cell(metric, e, p1), cell(metric, e, p2)),
      op: '>', rhs: num(tgt),
    };
    return finalize(dataset, {
      type: 'pct_points', traps: ['pct_vs_pp'], tier, claim,
      text: `${title} for ${e} ${pointsChange >= 0 ? 'increased' : 'decreased'} by more than ` +
        `${tgt} percentage points between ${p1} and ${p2}.`,
      narrative: [
        `“Percentage points” means subtract the two rates: ` +
        `${fmtPct(m2, 1)} − ${fmtPct(m1, 1)} = ${pointsChange.toFixed(1)} points.`,
        `Do NOT divide — that would give a relative % change, a different quantity.`,
      ],
    });
  }
  // relative-% wording about a percent metric — tests pp/% confusion
  const rel = ((m2 - m1) / m1) * 100;
  const tgt = Math.max(1, Math.round(Math.abs(rel) * rng.pick(ppMul)));
  const claim = {
    kind: 'cmp', lhs: pctChange(cell(metric, e, p1), cell(metric, e, p2)),
    op: '>', rhs: num(rel >= 0 ? tgt : -tgt),
  };
  return finalize(dataset, {
    type: 'pct_points', traps: ['pct_vs_pp'], tier, claim,
    text: `${title} for ${e} ${rel >= 0 ? 'rose' : 'fell'} by more than ${tgt}% ` +
      `(in relative terms) between ${p1} and ${p2}.`,
    narrative: [
      `A relative % change of a rate = (new − old) ÷ old × 100 = ` +
      `(${fmtPct(m2, 1)} − ${fmtPct(m1, 1)}) ÷ ${fmtPct(m1, 1)} × 100 = ${rel.toFixed(1)}%.`,
      `This is NOT the same as the change in percentage points (${(m2 - m1).toFixed(1)} pts).`,
    ],
  });
}

// 5. RATIO / SHARE — share of company total (combines revenue tab + total caption).
function genShare(dataset, rng, tier, aim) {
  const e = pickVisibleEntity(rng, dataset);
  // Cannot-Say variant: ask about share in a NON-latest period (total not shown).
  const p = aim === LABEL.CANNOT_SAY
    ? rng.pick(dataset.periodsVisible.slice(0, -1).concat(dataset.periodLatentBefore))
    : latestPeriod(dataset);
  const rev = dataset.resolveWorld({ m: 'revenue', e, p });
  const tot = dataset.resolveWorld({ m: 'revenueTotal', e: '__ALL__', p });
  const sh = (rev / tot) * 100;
  const shMul = tier === 'advanced' ? [0.88, 0.94, 1.07, 1.13] : [0.7, 1.3];
  const tgt = Math.max(1, Math.round(sh * rng.pick(shMul)));
  const op = rng.pick(['>', '<']);
  const claim = {
    kind: 'cmp',
    lhs: shareOf(cell('revenue', e, p), cell('revenueTotal', '__ALL__', p)),
    op, rhs: num(tgt),
  };
  return finalize(dataset, {
    type: 'share', traps: ['share', 'multi_tab'], tier, claim,
    text: phrase(rng, [
      `${e} accounted for ${op === '>' ? 'more than' : 'less than'} ${tgt}% of total ${TITLES_LOWER(dataset, 'revenue')} in ${p}.`,
      `In ${p}, ${op === '>' ? 'over' : 'under'} ${tgt}% of the company's total ${TITLES_LOWER(dataset, 'revenue')} came from ${e}.`,
    ]),
    narrative: [
      `Share = ${e}'s ${TITLES_LOWER(dataset, 'revenue')} ÷ company total × 100.`,
    ],
  });
}

// 6. MULTI-TAB COMBINATION — profit (revenue − costs) or revenue per head.
function genMultiTab(dataset, rng, tier, aim) {
  const e = pickVisibleEntity(rng, dataset);
  const p = latestOrLatent(dataset, rng, aim);
  if (rng.chance(0.5)) {
    // profit = revenue − costs
    const rev = dataset.resolveWorld({ m: 'revenue', e, p });
    const cost = dataset.resolveWorld({ m: 'costs', e, p });
    const profit = rev - cost;
    const unit = dataset.units.revenue;
    const pMul = tier === 'advanced' ? [0.93, 0.96, 1.05, 1.08] : [0.7, 1.25];
    const tgt = niceValue(Math.abs(profit) * rng.pick(pMul), unit);
    const diffName = dataset.meta.diffLabel; // operating profit / gross profit / net assets / free cash flow
    const claim = { kind: 'cmp', lhs: sub(cell('revenue', e, p), cell('costs', e, p)), op: '>', rhs: num(tgt) };
    return finalize(dataset, {
      type: 'multi_tab', traps: ['multi_tab'], tier, claim,
      text: `${e}'s ${diffName} (${TITLES_LOWER(dataset, 'revenue')} minus ` +
        `${TITLES_LOWER(dataset, 'costs')}) in ${p} exceeded ${money(tgt, unit.word, unit.symbol)}.`,
      narrative: [
        `${diffName.charAt(0).toUpperCase() + diffName.slice(1)} = ${TITLES_LOWER(dataset, 'revenue')} − ${TITLES_LOWER(dataset, 'costs')} ` +
        `= ${formatValue(unit, rev)} − ${formatValue(dataset.units.costs, cost)} = ${formatValue(unit, profit)}.`,
        `The two figures live on DIFFERENT tabs — note the units may differ.`,
      ],
    });
  }
  // revenue per head = revenue ÷ headcount
  const rev = dataset.resolveWorld({ m: 'revenue', e, p });
  const heads = dataset.resolveWorld({ m: 'headcount', e, p });
  const rph = rev / heads;
  const unit = { kind: 'currency', symbol: dataset.units.revenue.symbol, scale: 1e3, decimals: 0, word: 'thousand', label: 'per head' };
  const rphMul = tier === 'advanced' ? [0.92, 0.96, 1.05, 1.09] : [0.75, 1.25];
  const tgt = niceValue(rph * rng.pick(rphMul), unit);
  const claim = { kind: 'cmp', lhs: div(cell('revenue', e, p), cell('headcount', e, p)), op: '>', rhs: num(tgt) };
  return finalize(dataset, {
    type: 'multi_tab', traps: ['multi_tab', 'ratio'], tier, claim,
    text: `${TITLES_LOWER(dataset, 'revenue')} per ${dataset.units.headcount.label.replace(/s$/, '')} ` +
      `for ${e} in ${p} exceeded ${money(tgt, 'thousand', unit.symbol)}.`,
    narrative: [
      `Revenue per head = ${TITLES_LOWER(dataset, 'revenue')} ÷ ${TITLES_LOWER(dataset, 'headcount')} ` +
      `= ${formatValue(dataset.units.revenue, rev)} ÷ ${group(heads)} = ${money(rph, 'thousand', unit.symbol)} per head.`,
    ],
  });
}

// 7. TREND / DIRECTION — monotonic movement over the visible periods.
function genTrend(dataset, rng, tier, aim) {
  const metric = rng.pick(['revenue', 'costs', 'headcount', 'margin']);
  const e = pickVisibleEntity(rng, dataset);
  // Cannot-Say: extend the span into a latent period.
  const span = aim === LABEL.CANNOT_SAY && dataset.periodLatentBefore.length
    ? [dataset.periodLatentBefore[dataset.periodLatentBefore.length - 1], ...dataset.periodsVisible]
    : dataset.periodsVisible;
  const dir = rng.pick(['increasing', 'decreasing']);
  const claim = { kind: 'trend', cells: span.map((p) => ({ m: metric, e, p })), dir };
  const word = dir === 'increasing' ? 'rose every period' : 'fell every period';
  return finalize(dataset, {
    type: 'trend', traps: ['trend'], tier, claim,
    text: `${dataset.theme.titles[metricRole(metric)]} for ${e} ${word} from ` +
      `${span[0]} to ${span[span.length - 1]}.`,
    narrative: [`Check each step in turn — a single exception makes a “every period” claim False.`],
  });
}

// 8. RANK / COMPARISON — highest/lowest across entities (level or growth).
function genRank(dataset, rng, tier, aim) {
  // Cannot-Say via a latent period, or via naming the latent entity as target.
  const p = aim === LABEL.CANNOT_SAY && rng.chance(0.5)
    ? rng.pick(dataset.periodLatentBefore.concat(dataset.periodLatentAfter).concat([latestPeriod(dataset)]))
    : latestPeriod(dataset);
  const metric = rng.pick(['revenue', 'revenue', 'costs', 'headcount', 'margin']);
  const target = aim === LABEL.CANNOT_SAY && rng.chance(0.5) ? dataset.entityLatent : pickVisibleEntity(rng, dataset);
  const sel = rng.pick(['max', 'min']);
  const among = dataset.entitiesVisible.map((e) => ({ m: metric, e, p }));
  const claim = { kind: 'rank', among, target: { m: metric, e: target, p }, sel };
  const titleLower = dataset.theme.titles[metricRole(metric)].toLowerCase();
  return finalize(dataset, {
    type: 'rank', traps: ['rank'], tier, claim,
    text: phrase(rng, [
      `${target} had the ${sel === 'max' ? 'highest' : 'lowest'} ${titleLower} of all ${dataset.meta.entityLabel.toLowerCase()}s in ${p}.`,
      `Of all the ${dataset.meta.entityLabel.toLowerCase()}s, ${target} recorded the ${sel === 'max' ? 'greatest' : 'smallest'} ${titleLower} in ${p}.`,
    ]),
    narrative: [`Compare all ${dataset.meta.entityLabel.toLowerCase()}s for ${p} and find the ${sel === 'max' ? 'largest' : 'smallest'}.`],
  });
}

// 9. INSUFFICIENT DATA — always Cannot Say, using the most instructive omissions.
function genInsufficient(dataset, rng, tier) {
  const kind = rng.pick(['metric', 'entity', 'period', 'index']);
  const e = pickVisibleEntity(rng, dataset);
  const p = latestPeriod(dataset);
  if (kind === 'metric') {
    // data-type mismatch: ask about a latent metric (e.g. units sold)
    const tgt = rng.int(200, 800) * 1000;
    const claim = { kind: 'cmp', lhs: cell('latent', e, p), op: '>', rhs: num(tgt) };
    return finalize(dataset, {
      type: 'insufficient', traps: ['insufficient', 'data_type_mismatch'], tier, claim,
      text: `${dataset.meta.latentMetricLabel} for ${e} in ${p} exceeded ${group(tgt)}.`,
    });
  }
  if (kind === 'entity') {
    const tgt = niceValue(dataset.resolveWorld({ m: 'revenue', e: dataset.entityLatent, p }), dataset.units.revenue);
    const claim = { kind: 'cmp', lhs: cell('revenue', dataset.entityLatent, p), op: '>', rhs: num(tgt) };
    return finalize(dataset, {
      type: 'insufficient', traps: ['insufficient'], tier, claim,
      text: `${dataset.theme.titles.revenue} for ${dataset.entityLatent} in ${p} exceeded ` +
        `${money(tgt, dataset.units.revenue.word, dataset.units.revenue.symbol)}.`,
    });
  }
  if (kind === 'period') {
    const pl = rng.pick(dataset.periodLatentBefore.concat(dataset.periodLatentAfter));
    const tgt = niceValue(dataset.resolveWorld({ m: 'revenue', e, p: pl }), dataset.units.revenue);
    const claim = { kind: 'cmp', lhs: cell('revenue', e, pl), op: '>', rhs: num(tgt) };
    return finalize(dataset, {
      type: 'insufficient', traps: ['insufficient'], tier, claim,
      text: `${dataset.theme.titles.revenue} for ${e} in ${pl} exceeded ` +
        `${money(tgt, dataset.units.revenue.word, dataset.units.revenue.symbol)}.`,
    });
  }
  // index → absolute conversion not possible
  const tgt = rng.int(5, 40) * 1000;
  const claim = { kind: 'cmp', lhs: cell('latent', e, p), op: '>', rhs: num(tgt) };
  return finalize(dataset, {
    type: 'insufficient', traps: ['insufficient', 'index_trap'], tier, claim,
    text: `The ${dataset.theme.titles.index} shows that more than ${group(tgt)} ${dataset.meta.latentMetricLabel.toLowerCase()} ` +
      `were recorded for ${e} in ${p}.`,
  });
}

// -----------------------------------------------------------------------------
// harder multi-step types (weighted towards intermediate/advanced sessions)
// -----------------------------------------------------------------------------

// 10. GROWTH COMPARISON — which entity grew faster in % terms (two full
// percentage-change computations, then a comparison — a real advanced staple).
function genGrowthCompare(dataset, rng, tier, aim) {
  const metric = rng.pick(['revenue', 'costs']);
  const [eA, eB] = rng.sample(dataset.entitiesVisible, 2);
  const [p1, p2] = orderedPeriods(dataset, rng, aim);
  const unit = dataset.units[metric];
  const a1 = dataset.resolveWorld({ m: metric, e: eA, p: p1 });
  const a2 = dataset.resolveWorld({ m: metric, e: eA, p: p2 });
  const b1 = dataset.resolveWorld({ m: metric, e: eB, p: p1 });
  const b2 = dataset.resolveWorld({ m: metric, e: eB, p: p2 });
  const pcA = ((a2 - a1) / a1) * 100;
  const pcB = ((b2 - b1) / b1) * 100;
  const claim = {
    kind: 'cmp',
    lhs: pctChange(cell(metric, eA, p1), cell(metric, eA, p2)),
    op: '>',
    rhs: pctChange(cell(metric, eB, p1), cell(metric, eB, p2)),
  };
  const titleLower = dataset.theme.titles[metricRole(metric)].toLowerCase();
  const bothFell = pcA < 0 && pcB < 0;
  const text = bothFell
    ? `Between ${p1} and ${p2}, ${titleLower} fell by a smaller percentage at ${eA} than at ${eB}.`
    : phrase(rng, [
      `Between ${p1} and ${p2}, ${titleLower} grew by a greater percentage at ${eA} than at ${eB}.`,
      `${titleLower.charAt(0).toUpperCase() + titleLower.slice(1)} for ${eA} rose faster in percentage terms than for ${eB} between ${p1} and ${p2}.`,
    ]);
  return finalize(dataset, {
    type: 'growth_compare', traps: ['pct_change', 'multi_step'], tier, claim,
    text,
    narrative: [
      `${eA}: (${formatValue(unit, a2)} − ${formatValue(unit, a1)}) ÷ ${formatValue(unit, a1)} × 100 = ${pcA.toFixed(1)}%.`,
      `${eB}: (${formatValue(unit, b2)} − ${formatValue(unit, b1)}) ÷ ${formatValue(unit, b1)} × 100 = ${pcB.toFixed(1)}%.`,
      `Compare the two percentage changes — the larger absolute figures do NOT decide it.`,
    ],
  });
}

// 11. AVERAGE — mean over the shown periods vs a near-miss threshold.
function genAverage(dataset, rng, tier, aim) {
  const metric = rng.pick(['revenue', 'costs', 'headcount']);
  const e = pickVisibleEntity(rng, dataset);
  const unit = dataset.units[metric];
  const span = aim === LABEL.CANNOT_SAY && dataset.periodLatentBefore.length
    ? [dataset.periodLatentBefore[dataset.periodLatentBefore.length - 1], ...dataset.periodsVisible]
    : dataset.periodsVisible;
  const refs = span.map((p) => ({ m: metric, e, p }));
  const vals = refs.map((r) => dataset.resolveWorld(r));
  const avg = vals.reduce((s, v) => s + v, 0) / vals.length;
  const op = rng.pick(['>', '<']);
  const tgt = threshold(rng, avg, unit, op === '<', tier);
  const claim = { kind: 'cmp', lhs: div(sum(refs), num(refs.length)), op, rhs: num(tgt) };
  const titleLower = dataset.theme.titles[metricRole(metric)].toLowerCase();
  return finalize(dataset, {
    type: 'average', traps: ['multi_step'], tier, claim,
    text: phrase(rng, [
      `Average ${titleLower} for ${e} across ${span[0]} to ${span[span.length - 1]} ${verbAlt(rng, op)} ${phraseValue(dataset, metric, tgt)}.`,
      `Across ${span[0]}–${span[span.length - 1]}, ${e}'s ${titleLower} averaged ${op === '>' ? 'more' : 'less'} than ${phraseValue(dataset, metric, tgt)} per period.`,
    ]),
    narrative: [
      `Sum the ${span.length} periods, then divide by ${span.length}: average = ${formatValue(unit, avg)}.`,
      `A shortcut under time pressure: compare the threshold × ${span.length} against the running total.`,
    ],
  });
}

// 12. RATIO — one figure as a multiple or percentage of another (cross-tab).
function genRatio(dataset, rng, tier, aim) {
  const e = pickVisibleEntity(rng, dataset);
  const p = latestOrLatent(dataset, rng, aim);
  const rev = dataset.resolveWorld({ m: 'revenue', e, p });
  const cost = dataset.resolveWorld({ m: 'costs', e, p });
  const revLower = TITLES_LOWER(dataset, 'revenue');
  const costLower = TITLES_LOWER(dataset, 'costs');
  if (rng.chance(0.5)) {
    // costs as a % of revenue (cost-to-income style)
    const pctActual = (cost / rev) * 100;
    const mul = tier === 'advanced' ? [0.92, 0.96, 1.05, 1.09] : [0.75, 1.25];
    const tgt = Math.max(1, Math.round(pctActual * rng.pick(mul)));
    const op = rng.pick(['>', '<']);
    const claim = { kind: 'cmp', lhs: shareOf(cell('costs', e, p), cell('revenue', e, p)), op, rhs: num(tgt) };
    return finalize(dataset, {
      type: 'ratio', traps: ['ratio', 'multi_tab'], tier, claim,
      text: `In ${p}, ${costLower} for ${e} amounted to ${op === '>' ? 'more' : 'less'} than ${tgt}% of its ${revLower}.`,
      narrative: [
        `Ratio = ${costLower} ÷ ${revLower} × 100 = ${formatValue(dataset.units.costs, cost)} ÷ ${formatValue(dataset.units.revenue, rev)} × 100 = ${pctActual.toFixed(1)}%.`,
        `The two figures sit on DIFFERENT tabs and may use different units — convert before dividing.`,
      ],
    });
  }
  // revenue as a multiple of costs
  const ratio = rev / cost;
  const mul = tier === 'advanced' ? [0.93, 0.97, 1.04, 1.08] : [0.8, 1.2];
  const tgt = Math.max(0.1, +(ratio * rng.pick(mul)).toFixed(1));
  const op = rng.pick(['>', '<']);
  const claim = { kind: 'cmp', lhs: div(cell('revenue', e, p), cell('costs', e, p)), op, rhs: num(tgt) };
  return finalize(dataset, {
    type: 'ratio', traps: ['ratio', 'multi_tab'], tier, claim,
    text: `In ${p}, ${revLower} for ${e} was ${op === '>' ? 'more' : 'less'} than ${tgt} times its ${costLower}.`,
    narrative: [
      `Multiple = ${revLower} ÷ ${costLower} = ${formatValue(dataset.units.revenue, rev)} ÷ ${formatValue(dataset.units.costs, cost)} = ${ratio.toFixed(2)}×.`,
    ],
  });
}

// 13. COMBINED SHARE — two entities together vs the company total (three
// figures, two tabs, one near-miss threshold).
function genCombinedShare(dataset, rng, tier, aim) {
  const [eA, eB] = rng.sample(dataset.entitiesVisible, 2);
  const p = aim === LABEL.CANNOT_SAY
    ? rng.pick(dataset.periodsVisible.slice(0, -1).concat(dataset.periodLatentBefore))
    : latestPeriod(dataset);
  const revA = dataset.resolveWorld({ m: 'revenue', e: eA, p });
  const revB = dataset.resolveWorld({ m: 'revenue', e: eB, p });
  const tot = dataset.resolveWorld({ m: 'revenueTotal', e: '__ALL__', p });
  const sh = ((revA + revB) / tot) * 100;
  const mul = tier === 'advanced' ? [0.9, 0.95, 1.05, 1.1] : [0.75, 1.25];
  const tgt = Math.max(1, Math.min(99, Math.round(sh * rng.pick(mul))));
  const op = rng.pick(['>', '<']);
  const claim = {
    kind: 'cmp',
    lhs: shareOf(sum([{ m: 'revenue', e: eA, p }, { m: 'revenue', e: eB, p }]), cell('revenueTotal', '__ALL__', p)),
    op, rhs: num(tgt),
  };
  const revLower = TITLES_LOWER(dataset, 'revenue');
  return finalize(dataset, {
    type: 'combined_share', traps: ['share', 'multi_step'], tier, claim,
    text: phrase(rng, [
      `${eA} and ${eB} together accounted for ${op === '>' ? 'more' : 'less'} than ${tgt}% of total ${revLower} in ${p}.`,
      `In ${p}, ${op === '>' ? 'over' : 'under'} ${tgt}% of the company's total ${revLower} came from ${eA} and ${eB} combined.`,
    ]),
    narrative: [
      `Add the two: ${formatValue(dataset.units.revenue, revA)} + ${formatValue(dataset.units.revenue, revB)} = ${formatValue(dataset.units.revenue, revA + revB)}.`,
      `Divide by the company total (share-tab caption) and × 100 = ${sh.toFixed(1)}%.`,
    ],
  });
}

// ---- period helpers ---------------------------------------------------------

function latestOrLatent(dataset, rng, aim) {
  if (aim === LABEL.CANNOT_SAY) {
    const pool = dataset.periodLatentBefore.concat(dataset.periodLatentAfter);
    if (pool.length) return rng.pick(pool);
  }
  return latestPeriod(dataset);
}

function orderedPeriods(dataset, rng, aim) {
  if (aim === LABEL.CANNOT_SAY && dataset.periodLatentBefore.length) {
    // one endpoint latent → Cannot Say
    return [dataset.periodLatentBefore[dataset.periodLatentBefore.length - 1], latestPeriod(dataset)];
  }
  const vis = dataset.periodsVisible;
  const i = rng.int(0, vis.length - 2);
  return [vis[i], vis[i + 1 + rng.int(0, vis.length - 2 - i)]];
}

function metricRole(metric) {
  return { revenue: 'revenue', costs: 'costs', headcount: 'headcount', margin: 'margin', index: 'index', share: 'share' }[metric] || metric;
}

// -----------------------------------------------------------------------------
// registry + top-level generate
// -----------------------------------------------------------------------------
export const GENERATORS = {
  lookup: genLookup,
  arithmetic: genArithmetic,
  pct_change: genPctChange,
  pct_points: genPctPoints,
  share: genShare,
  multi_tab: genMultiTab,
  trend: genTrend,
  rank: genRank,
  insufficient: genInsufficient,
  growth_compare: genGrowthCompare,
  average: genAverage,
  ratio: genRatio,
  combined_share: genCombinedShare,
};

export const ITEM_TYPES = Object.keys(GENERATORS);

/**
 * Generate one item of `type`.
 * @param aim optional target label bias ('TRUE'|'FALSE'|'CANNOT_SAY') — advisory;
 *            the final label is always recomputed from the claim.
 */
export function generateItem(dataset, rng, tier, type, aim = null) {
  const gen = GENERATORS[type];
  if (!gen) throw new Error(`unknown item type: ${type}`);
  return type === 'insufficient' ? gen(dataset, rng, tier) : gen(dataset, rng, tier, aim);
}
