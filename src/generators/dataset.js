// -----------------------------------------------------------------------------
// dataset.js — procedurally generate ONE test's worth of data.
//
// Authentic-format fact (see research/SPEC.md §1): in the real scales numerical
// test the ~6 data displays are FIXED for the whole test — every statement in a
// session refers to the same six tabs. So a session = one dataset (6 tabs) + N
// statements about it. We therefore generate a random "world" of numbers and
// project a fixed roster of six role-tagged tabs from it.
//
// The world contains MORE than the six tabs show:
//   • periods before/after the visible window,
//   • one entity excluded from every tab,
//   • extra metrics that appear on no tab (e.g. units sold when only revenue
//     is displayed — the classic data-type-mismatch trap).
// Anything in the world but not on a tab is "latent" and is the ONLY honest
// basis for a provably-correct "Cannot Say" item: a statement that needs a
// latent figure cannot be decided from what the candidate can see.
//
// Roles let the item generators (items.js) stay generic and let you add tabs
// later without rewriting them. The six roles are:
//   revenue  (currency, per-entity, per-period)   — trends, ranking, %-change
//   costs    (currency, different scale)           — profit combos (rev - cost)
//   share    (percent share of company revenue)    — %-vs-pp traps, share×total
//   headcount(count, per-entity, per-period)       — ratios (revenue per head)
//   margin   (percent rate, per-period)            — %-vs-pp traps
//   index    (base-100 index, per-period)          — index/absolute trap
// plus a visible aggregate "revenueTotal" per period, used by share×total combos.
// -----------------------------------------------------------------------------

import { makeRng } from './rng.js';

// --- domain themes: only labels/units/flavour change; structure is identical. -
const THEMES = [
  {
    key: 'retail',
    entityLabel: 'Region',
    entities: ['North', 'South', 'East', 'West', 'Central', 'Northeast', 'Southwest'],
    periodLabel: 'FY',
    currency: { symbol: '$', word: 'dollars' },
    titles: {
      revenue: 'Revenue', costs: 'Operating Costs', share: 'Revenue Share',
      headcount: 'Employees', margin: 'Net Margin', index: 'Customer Satisfaction',
    },
    latentMetricLabel: 'Units Sold', // exists in world, shown on no tab
  },
  {
    key: 'manufacturing',
    entityLabel: 'Plant',
    entities: ['Aveley', 'Bremen', 'Cortez', 'Delft', 'Esbjerg', 'Faro', 'Genoa'],
    periodLabel: 'Year',
    currency: { symbol: '€', word: 'euros' },
    titles: {
      revenue: 'Output Value', costs: 'Energy Costs', share: 'Output Share',
      headcount: 'Workforce', margin: 'Capacity Utilisation', index: 'Quality Index',
    },
    latentMetricLabel: 'Defect Rate',
  },
  {
    key: 'saas',
    entityLabel: 'Product',
    entities: ['Atlas', 'Beacon', 'Cobalt', 'Drift', 'Ember', 'Flux', 'Grove'],
    periodLabel: 'FY',
    currency: { symbol: '$', word: 'dollars' },
    titles: {
      revenue: 'Recurring Revenue', costs: 'Support Costs', share: 'Revenue Share',
      headcount: 'Team Size', margin: 'Gross Margin', index: 'NPS Index',
    },
    latentMetricLabel: 'Active Users',
  },
  {
    key: 'bank',
    entityLabel: 'Division',
    entities: ['Retail', 'Commercial', 'Markets', 'Wealth', 'Treasury', 'Digital', 'Cards'],
    periodLabel: 'FY',
    currency: { symbol: '£', word: 'pounds' },
    titles: {
      revenue: 'Income', costs: 'Operating Expenses', share: 'Income Share',
      headcount: 'Staff', margin: 'Cost-Income Ratio', index: 'Service Index',
    },
    latentMetricLabel: 'Complaints',
  },
];

// Currency scales we draw from, so different tabs use different units (the
// thousands-vs-millions trap). Revenue tends large, costs a notch smaller.
const CUR = (symbol, scale, word) => ({
  kind: 'currency', symbol, scale, decimals: scale >= 1e6 ? 2 : 0,
  label: `${symbol} ${word}`, word,
});
const PCT = (label = '%') => ({ kind: 'percent', symbol: '', scale: 1, decimals: 1, label });
const CNT = (label = '') => ({ kind: 'count', symbol: '', scale: 1, decimals: 0, label });
const IDX = (label = 'index (base 100)') => ({ kind: 'index', symbol: '', scale: 1, decimals: 0, label });

// Chart type per metric, matched to Aon's real scales numerical displays (see
// the chart-types research). Tables are the most common form; market share is a
// doughnut with a total caption; headcount is a stacked column; a metric across
// future periods is a grouped HORIZONTAL bar (Aon's FORECAST form); trends are
// line charts. Weighting via repetition (e.g. table twice for costs).
const CHART_OPTIONS = {
  revenue: ['groupedBarH', 'line', 'table'],
  costs: ['table', 'table', 'stackedBar'],
  share: ['doughnut', 'doughnut', 'pie'],
  headcount: ['stackedBar', 'table'],
  margin: ['line', 'table'],
  index: ['line'],
};

// Tier tuning: harder tiers use bigger unit gaps and more entities/periods to
// juggle. Difficulty of the *reasoning* is applied in items.js.
const TIER = {
  beginner: { entities: 3, periods: 3, latentBefore: 2, latentAfter: 0 },
  intermediate: { entities: 4, periods: 4, latentBefore: 3, latentAfter: 1 },
  advanced: { entities: 5, periods: 5, latentBefore: 3, latentAfter: 1 },
};

/**
 * Generate a full dataset for one session.
 * @param {string|number} seed
 * @param {'medium'|'intermediate'|'hard'} tier
 */
export function generateDataset(seed, tier = 'intermediate') {
  const rng = makeRng(`ds:${seed}:${tier}`);
  const cfg = TIER[tier] || TIER.intermediate;
  const theme = rng.pick(THEMES);

  // -- entities: choose the visible set + one globally-latent entity ----------
  const pool = rng.shuffle(theme.entities.slice());
  const entitiesVisible = pool.slice(0, cfg.entities);
  const entityLatent = pool[cfg.entities]; // present in world, on no tab

  // -- periods: a world timeline; only a contiguous window is visible ---------
  const startYear = rng.int(1, 4); // FY index start
  const totalPeriods = cfg.latentBefore + cfg.periods + cfg.latentAfter;
  const worldPeriodIdx = Array.from({ length: totalPeriods }, (_, i) => startYear + i);
  const worldPeriods = worldPeriodIdx.map((i) => `${theme.periodLabel}${i}`);
  const visStart = cfg.latentBefore;
  const periodsVisible = worldPeriods.slice(visStart, visStart + cfg.periods);
  const periodLatentBefore = worldPeriods.slice(0, cfg.latentBefore);
  const periodLatentAfter = worldPeriods.slice(visStart + cfg.periods);

  // -- units: randomise scales so tabs mix thousands/millions -----------------
  const bigScale = rng.pick([1e6, 1e6, 1e3]);
  const costScale = bigScale === 1e6 ? rng.pick([1e3, 1e6]) : 1e3;
  const units = {
    revenue: CUR(theme.currency.symbol, bigScale, bigScale >= 1e6 ? 'million' : 'thousand'),
    costs: CUR(theme.currency.symbol, costScale, costScale >= 1e6 ? 'million' : 'thousand'),
    share: PCT('% of revenue'),
    headcount: CNT(theme.entityLabel === 'Plant' ? 'workers' : 'people'),
    margin: PCT('%'),
    index: IDX(),
    revenueTotal: CUR(theme.currency.symbol, bigScale, bigScale >= 1e6 ? 'million' : 'thousand'),
    latent: CNT('units'),
  };

  // -- generate base-unit values for the whole world --------------------------
  // values[metric][entity][period] = base-unit number. Aggregates use entity
  // key '__ALL__'. Every WORLD cell exists here; visibility is decided later.
  const values = {};
  const setV = (m, e, p, v) => {
    (values[m] ??= {});
    (values[m][e] ??= {});
    values[m][e][p] = v;
  };

  const allEntities = [...entitiesVisible, entityLatent];

  // Revenue: each entity has a level and a growth path across ALL world periods.
  for (const e of allEntities) {
    let level = rng.range(20, 90) * (bigScale >= 1e6 ? 1e6 : 1e5); // base money
    const growth = rng.range(-0.06, 0.14);
    for (const p of worldPeriods) {
      level = Math.max(1e5, level * (1 + growth + rng.range(-0.05, 0.05)));
      setV('revenue', e, p, roundMoney(level, units.revenue));
    }
  }
  // Revenue total per period (visible aggregate) = sum over VISIBLE entities.
  for (const p of worldPeriods) {
    let t = 0;
    for (const e of entitiesVisible) t += values.revenue[e][p];
    setV('revenueTotal', '__ALL__', p, t);
  }
  // Share of (visible) company revenue, per entity per period.
  for (const p of worldPeriods) {
    const total = values.revenueTotal['__ALL__'][p];
    for (const e of allEntities) {
      setV('share', e, p, +(100 * values.revenue[e][p] / total).toFixed(1));
    }
  }
  // Costs: correlated with revenue but noisier; different unit scale.
  for (const e of allEntities) {
    for (const p of worldPeriods) {
      const rev = values.revenue[e][p];
      const c = rev * rng.range(0.45, 0.85);
      setV('costs', e, p, roundMoney(c, units.costs));
    }
  }
  // Headcount: scales loosely with revenue.
  for (const e of allEntities) {
    const perHead = rng.range(120000, 320000); // revenue per head
    for (const p of worldPeriods) {
      setV('headcount', e, p, Math.max(20, Math.round(values.revenue[e][p] / perHead) * 5));
    }
  }
  // Margin (%): a per-period rate, per entity, plausible band.
  for (const e of allEntities) {
    let m = rng.range(6, 24);
    for (const p of worldPeriods) {
      m = clamp(m + rng.range(-2.5, 2.5), 1, 40);
      setV('margin', e, p, +m.toFixed(1));
    }
  }
  // Index (base 100 in first WORLD period): aggregate series.
  {
    let idx = 100;
    for (let i = 0; i < worldPeriods.length; i++) {
      if (i > 0) idx = Math.round(idx * (1 + rng.range(-0.04, 0.08)));
      setV('index', '__ALL__', worldPeriods[i], idx);
    }
  }
  // Latent metric (e.g. units sold): exists in world, shown on NO tab.
  for (const e of allEntities) {
    for (const p of worldPeriods) {
      setV('latent', e, p, Math.round(rng.range(50, 900)) * 1000);
    }
  }

  // -- build the six visible tabs --------------------------------------------
  const tabs = [];
  const mkTab = (id, role, metric, opts = {}) => {
    const chart = rng.pick(CHART_OPTIONS[role]);
    const entities = opts.aggregate ? ['__ALL__'] : entitiesVisible;
    const periods = opts.latestOnly ? [periodsVisible[periodsVisible.length - 1]] : periodsVisible;
    // Materialise the visible cell list for this tab.
    const cells = [];
    for (const e of entities) {
      for (const p of periods) {
        cells.push({ e, p, base: values[metric][e][p] });
      }
    }
    const hasTotal = role === 'revenue' || role === 'costs' || role === 'headcount'
      ? rng.chance(0.5) : false;
    tabs.push({
      id, role, metric, title: theme.titles[role], chart,
      unit: units[metric] || units[role], entities, periods, cells, hasTotal,
      aggregate: !!opts.aggregate, latestOnly: !!opts.latestOnly,
    });
  };

  mkTab('revenue', 'revenue', 'revenue');
  mkTab('costs', 'costs', 'costs');
  mkTab('share', 'share', 'share', { latestOnly: true });
  mkTab('headcount', 'headcount', 'headcount');
  mkTab('margin', 'margin', 'margin');
  mkTab('index', 'index', 'index', { aggregate: true });

  // A hidden 7th "revenueTotal" is exposed as a small caption on the share tab
  // (a visible aggregate the share×total combo relies on).
  const shareTab = tabs.find((t) => t.role === 'share');
  const latestP = periodsVisible[periodsVisible.length - 1];
  shareTab.caption = {
    metric: 'revenueTotal', entity: '__ALL__', period: latestP,
    base: values.revenueTotal['__ALL__'][latestP], unit: units.revenueTotal,
    text: `Total ${theme.titles.revenue.toLowerCase()} (${latestP})`,
  };

  // -- build the visible index for O(1) resolution ----------------------------
  // A cell is VISIBLE iff it appears on some tab (or as the share-tab caption).
  const visible = new Map();
  const keyOf = (m, e, p) => `${m}|${e}|${p}`;
  for (const t of tabs) {
    for (const c of t.cells) visible.set(keyOf(t.metric, c.e, c.p), c.base);
  }
  visible.set(keyOf('revenueTotal', '__ALL__', latestP), shareTab.caption.base);

  const resolveVisible = (ref) => visible.get(keyOf(ref.m, ref.e, ref.p));
  const resolveWorld = (ref) => values[ref.m]?.[ref.e]?.[ref.p];

  return {
    seed, tier, theme, meta: {
      domain: theme.key, entityLabel: theme.entityLabel, periodLabel: theme.periodLabel,
      currency: theme.currency, latentMetricLabel: theme.latentMetricLabel,
    },
    entitiesVisible, entityLatent, allEntities,
    periodsVisible, periodLatentBefore, periodLatentAfter, worldPeriods,
    units, tabs, values,
    resolveVisible, resolveWorld,
    // convenience for item generators / verifier
    isVisible: (ref) => visible.has(keyOf(ref.m, ref.e, ref.p)),
    visibleKeys: () => Array.from(visible.keys()),
    displayValue: (metric, base) => base / (units[metric]?.scale || 1),
  };
}

function roundMoney(v, unit) {
  // Round to a tidy number of display units so charts read cleanly.
  const step = unit.scale >= 1e6 ? unit.scale / 100 : unit.scale / 10;
  return Math.max(step, Math.round(v / step) * step);
}
function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }
