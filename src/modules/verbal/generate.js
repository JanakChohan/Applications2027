// -----------------------------------------------------------------------------
// verbal/generate.js — scales verbal (True / False / Cannot Say over text).
//
// Approach (research/SPEC.md §11): build a STRUCTURED fact world about one
// fictional company, render each fact into short passages across ~6 tabs, then
// derive statements whose label is COMPUTED from the facts, never asserted:
//   TRUE  — the relevant tab entails the statement (exact, or a genuine synonym).
//   FALSE — the statement swaps a stated value for a wrong one (any contradicted
//           element ⇒ False, per Aon's own Ex4).
//   CANNOT SAY — the statement is about an attribute deliberately WITHHELD from
//           every passage (or an over-reaching "all/always/only" claim the text
//           doesn't support). Withholding is the only honest Cannot Say.
//
// Each rendered tab carries the exact facts it states, so the independent
// verifier (verify.js) can rebuild "what's shown" from the tabs alone and re-derive
// every label without trusting this file.
// -----------------------------------------------------------------------------

import { makeRng } from '../../generators/rng.js';

// Sector flavours. finance/industry read as "complex" per the research; the app
// leans finance-heavy per the user's target, but rotates all four.
const SECTORS = {
  finance: {
    weight: 3,
    names: ['Meridian Capital', 'Halstead & Roe', 'Northbank Partners', 'Ardent Financial', 'Calderwood Group'],
    productNoun: 'service', products: ['wealth management', 'corporate lending', 'asset advisory', 'treasury services', 'private banking'],
    cities: ['Frankfurt', 'Zurich', 'Luxembourg', 'Singapore', 'Toronto', 'Dublin'],
    principles: [
      { value: 'prudent risk management', syn: ['managing risk carefully', 'a cautious approach to risk'] },
      { value: 'long-term client relationships', syn: ['lasting partnerships with clients', 'enduring client trust'] },
    ],
    growth: [
      { value: 'expand its private-banking arm', syn: ['grow its private-banking division', 'build out private banking'] },
      { value: 'enter the Asian market', syn: ['establish a presence in Asia', 'move into Asian markets'] },
    ],
    channel: [{ value: 'through regional advisory offices', syn: ['via its network of advisory offices'] }],
  },
  industry: {
    weight: 3,
    names: ['Brunel Manufacturing', 'Kessler Industrial', 'Orlov Steelworks', 'Petra Components', 'Vantar Engineering'],
    productNoun: 'product line', products: ['precision bearings', 'hydraulic pumps', 'industrial valves', 'drive systems', 'casting moulds'],
    cities: ['Stuttgart', 'Turin', 'Gothenburg', 'Osaka', 'Cleveland', 'Lyon'],
    principles: [
      { value: 'operational safety', syn: ['a strong safety culture', 'protecting worker safety'] },
      { value: 'continuous improvement', syn: ['ongoing process improvement', 'steadily refining its processes'] },
    ],
    growth: [
      { value: 'automate its assembly lines', syn: ['increase factory automation', 'invest in automated production'] },
      { value: 'reduce energy consumption', syn: ['cut its energy use', 'lower its energy footprint'] },
    ],
    channel: [{ value: 'through industrial distributors', syn: ['via distribution partners'] }],
  },
  consumer: {
    weight: 2,
    names: ['Verano Retail', 'Bloomfield & Co', 'Marlow Brands', 'Casa Nuova', 'Tindal Stores'],
    productNoun: 'range', products: ['home furnishings', 'outdoor apparel', 'kitchenware', 'personal care', 'footwear'],
    cities: ['Milan', 'Manchester', 'Barcelona', 'Melbourne', 'Austin', 'Rotterdam'],
    principles: [
      { value: 'customer satisfaction', syn: ['keeping customers happy', 'a customer-first outlook'] },
      { value: 'sustainable sourcing', syn: ['responsibly sourced materials', 'ethical sourcing'] },
    ],
    growth: [
      { value: 'open new flagship stores', syn: ['launch further flagship locations', 'expand its store estate'] },
      { value: 'grow its online sales', syn: ['build up e-commerce', 'increase digital sales'] },
    ],
    channel: [{ value: 'through its own retail stores', syn: ['via company-owned shops'] }],
  },
  admin: {
    weight: 2,
    names: ['Corvus Services', 'Ledger & Vale', 'Ashby Group', 'Pinehill Solutions', 'Delmore Associates'],
    productNoun: 'service', products: ['payroll processing', 'records management', 'facilities support', 'document handling', 'compliance support'],
    cities: ['London', 'Warsaw', 'Chicago', 'Madrid', 'Brussels', 'Auckland'],
    principles: [
      { value: 'accuracy and reliability', syn: ['dependable, accurate work', 'getting the details right'] },
      { value: 'clear communication', syn: ['communicating openly', 'transparent communication'] },
    ],
    growth: [
      { value: 'digitise its records', syn: ['move records online', 'digitalise document storage'] },
      { value: 'expand its client base', syn: ['win more clients', 'grow the number of clients'] },
    ],
    channel: [{ value: 'through long-term service contracts', syn: ['via ongoing contracts'] }],
  },
};

const FIRST = ['Anders', 'Bianca', 'Cheng', 'Dana', 'Elif', 'Farid', 'Greta', 'Hugo', 'Ingrid', 'Javier', 'Keiko', 'Lars'];
const LAST = ['Novak', 'Reyes', 'Okafor', 'Lindqvist', 'Marchetti', 'Haddad', 'Bauer', 'Costa', 'Yamamoto', 'Petrov'];

const TIER = {
  beginner: { synonymTrue: false, quantifierTrap: false, tabs: 5 },
  intermediate: { synonymTrue: true, quantifierTrap: false, tabs: 6 },
  advanced: { synonymTrue: true, quantifierTrap: true, tabs: 6 },
};

/** Build a company fact world + tabs. Facts are attached to the tab that states them. */
export function buildWorld(seed, tier = 'intermediate', sectorBias = null) {
  const rng = makeRng(`verbal:${seed}:${tier}`);
  const cfg = TIER[tier] || TIER.intermediate;
  const sectorKey = sectorBias || rng.weighted(Object.entries(SECTORS).map(([k, v]) => ({ value: k, weight: v.weight })));
  const S = SECTORS[sectorKey];

  const name = rng.pick(S.names);
  const hq = rng.pick(S.cities);
  const otherCities = S.cities.filter((c) => c !== hq);
  const founded = rng.int(1958, 2012);
  const employees = rng.int(3, 90) * 100;
  const ceo = `${rng.pick(FIRST)} ${rng.pick(LAST)}`;
  const director = `${rng.pick(FIRST)} ${rng.pick(LAST)}`;
  const [prodA, prodB] = rng.sample(S.products, 2);
  const principle = rng.pick(S.principles);
  const principle2 = rng.pick(S.principles.filter((p) => p !== principle)) || principle;
  const growth = rng.pick(S.growth);
  const channel = rng.pick(S.channel);
  const retail = rng.int(8, 60);
  const warehouses = rng.int(2, 9);
  const region = sectorKey === 'consumer' ? 'across Europe' : 'in several international markets';

  // Facts, grouped by the tab that will state them. Each: {subject, attribute, value, synonyms}.
  const F = (subject, attribute, value, synonyms = []) => ({ subject, attribute, value: String(value), synonyms });

  const tabs = [
    {
      id: 'about', title: 'About the Company',
      facts: [
        F('company', 'name', name),
        F('company', 'sector', sectorLabel(sectorKey)),
        F('company', 'founded', founded),
        F('company', 'headquarters', hq),
        F('company', 'employees', `${employees.toLocaleString('en-US')} people`, [`around ${employees.toLocaleString('en-US')} staff`]),
      ],
    },
    {
      id: 'values', title: 'Values',
      facts: [
        F('company', 'core value', principle.value, principle.syn),
        F('company', 'second value', principle2.value, principle2.syn),
      ],
    },
    {
      id: 'strategy', title: 'Corporate Strategy',
      facts: [
        F('company', 'strategic priority', growth.value, growth.syn),
        F('company', 'market focus', region, [region.replace('in ', 'across ')]),
      ],
    },
    {
      id: 'locations', title: 'Locations',
      facts: [
        F('company', 'retail sites', `${retail}`, [`${retail} outlets`]),
        F('company', 'warehouses', `${warehouses}`),
        F('company', 'sales channel', channel.value, channel.syn),
      ],
    },
    {
      id: 'products', title: 'Products & Services',
      facts: [
        F('products', 'main line', prodA),
        F('products', 'second line', prodB),
      ],
    },
    {
      id: 'people', title: 'Executive Board',
      facts: [
        F('people', 'chief executive', ceo),
        F('people', 'operations director', director),
      ],
    },
  ].slice(0, cfg.tabs);

  // Render prose for each tab from its facts (deterministic templates).
  for (const t of tabs) t.passage = renderPassage(t, { name, sectorKey, region });

  // Build the "present" index the generator uses (verifier rebuilds its own).
  const facts = new Map();
  for (const t of tabs) for (const f of t.facts) facts.set(key(f.subject, f.attribute), { ...f, tab: t.id });

  // Attributes that are deliberately ABSENT (askable but never stated) → Cannot Say.
  const absent = [
    { subject: 'company', attribute: 'annual revenue', phrase: (v) => `had an annual revenue of ${v}`, val: () => `$${rng.int(2, 900)} million` },
    { subject: 'company', attribute: 'net profit', phrase: (v) => `reported a net profit of ${v}`, val: () => `$${rng.int(1, 90)} million` },
    { subject: 'company', attribute: 'stock listing', phrase: () => `is listed on a stock exchange`, val: () => '' },
    { subject: 'people', attribute: 'previous employer of the chief executive', phrase: () => `previously worked at a competitor`, val: () => '' },
    { subject: 'products', attribute: 'product pricing', phrase: () => `sells its ${prodA} at a premium price`, val: () => '' },
    { subject: 'company', attribute: 'number of countries', phrase: () => `operates in every European country`, val: () => '', quantifier: true },
    { subject: 'company', attribute: 'founding location', phrase: (v) => `was founded in ${v}`, val: () => rng.pick(otherCities) },
  ];

  return {
    seed, tier, sectorKey, cfg, rng,
    company: { name, hq, founded, employees, ceo, director, prodA, prodB, retail, warehouses, region, otherCities },
    tabs, facts, absent,
    sectorPool: S,
  };
}

export function sectorLabel(k) {
  return { finance: 'a financial services firm', industry: 'an industrial manufacturer', consumer: 'a consumer retail business', admin: 'a business services provider' }[k];
}
export function key(subject, attribute) { return `${subject}||${attribute}`; }
export const norm = (s) => String(s).toLowerCase().replace(/\s+/g, ' ').trim();

/**
 * The GENERATOR's own label function (reads world.facts). The independent
 * verifier in verify.js recomputes this from the rendered tabs by separate code;
 * the session/audit drops any item where the two disagree.
 */
export function labelOf(world, claim) {
  const f = world.facts.get(key(claim.subject, claim.attribute));
  if (!f) return 'CANNOT_SAY';
  if (norm(claim.asserted) === norm(f.value)) return 'TRUE';
  if (f.synonyms.some((s) => norm(s) === norm(claim.asserted))) return 'TRUE';
  return 'FALSE';
}

// ---- passage rendering ------------------------------------------------------
function get(tab, attr) { return tab.facts.find((f) => f.attribute === attr); }
function renderPassage(tab, ctx) {
  const v = (a) => (get(tab, a) ? get(tab, a).value : '');
  switch (tab.id) {
    case 'about':
      return `${v('name')} is ${v('sector')} founded in ${v('founded')}. ` +
        `Its headquarters are in ${v('headquarters')}. The company employs ${v('employees')}.`;
    case 'values':
      return `The company sees ${v('core value')} as central to how it works. ` +
        `It also emphasises ${v('second value')}.`;
    case 'strategy':
      return `Its current strategic priority is to ${v('strategic priority')}. ` +
        `The business operates ${v('market focus')}.`;
    case 'locations':
      return `The company runs ${v('retail sites')} retail sites and ${v('warehouses')} warehouses. ` +
        `Sales are made ${v('sales channel')}.`;
    case 'products':
      return `Its main ${ctx.sectorKey === 'industry' ? 'product line' : ctx.sectorKey === 'finance' || ctx.sectorKey === 'admin' ? 'service' : 'range'} is ${v('main line')}. ` +
        `It also offers ${v('second line')}.`;
    case 'people':
      return `The chief executive is ${v('chief executive')}. ` +
        `The operations director is ${v('operations director')}.`;
    default:
      return tab.facts.map((f) => `${f.attribute}: ${f.value}.`).join(' ');
  }
}

// ---- item generation --------------------------------------------------------

/**
 * Generate one verbal statement. `aim` biases the label; the final label is
 * recomputed from the facts in view.js/verify, so it is always correct.
 */
export function generateItem(world, rng, tier, aim = null) {
  const cfg = world.cfg;
  const pickTarget = () => aim || rng.weighted([{ value: 'TRUE', weight: 4 }, { value: 'FALSE', weight: 3.5 }, { value: 'CANNOT_SAY', weight: 3 }]);
  const target = pickTarget();

  if (target === 'CANNOT_SAY') return csItem(world, rng, cfg);
  const present = [...world.facts.values()].filter((f) => f.attribute !== 'name'); // avoid trivial "is called X"
  const f = rng.pick(present);

  if (target === 'FALSE') {
    const wrong = wrongValue(world, rng, f);
    if (wrong == null) return csItem(world, rng, cfg); // fall back if no clean contradiction
    return build(world, f, wrong, ['contradiction'], statementFor(f, wrong));
  }
  // TRUE — exact, or a synonym at higher tiers
  const asserted = cfg.synonymTrue && f.synonyms.length && rng.chance(0.6) ? rng.pick(f.synonyms) : f.value;
  const traps = asserted !== f.value ? ['synonym'] : [];
  return build(world, f, asserted, traps, statementFor(f, asserted));
}

function csItem(world, rng, cfg) {
  const a = rng.pick(world.absent);
  const asserted = a.val();
  const claim = { subject: a.subject, attribute: a.attribute, asserted, tabHint: null };
  const text = `${world.company.name} ${a.phrase(asserted)}.`;
  const traps = a.quantifier ? ['quantifier', 'absent'] : ['absent', 'outside_knowledge'];
  return { module: 'verbal', type: 'verbal', tier: world.tier, claim, statement: capitalize(text), traps };
}

function build(world, fact, asserted, traps, statement) {
  return {
    module: 'verbal', type: 'verbal', tier: world.tier,
    claim: { subject: fact.subject, attribute: fact.attribute, asserted, tabHint: fact.tab },
    statement, traps,
  };
}

/** A contradicting value of the same attribute (a wrong-but-plausible swap). */
function wrongValue(world, rng, f) {
  const c = world.company;
  switch (f.attribute) {
    case 'headquarters': return rng.pick(c.otherCities);
    case 'founded': return String(f.value === String(c.founded) ? c.founded + rng.pick([-7, -4, 5, 9]) : c.founded);
    case 'employees': return `${(c.employees + rng.pick([-1500, 1200, 2000])).toLocaleString('en-US')} people`;
    case 'retail sites': return String(Math.max(1, c.retail + rng.pick([-9, 7, 12])));
    case 'warehouses': return String(Math.max(1, c.warehouses + rng.pick([-1, 2, 3])));
    case 'chief executive': return `${rng.pick(['Anders', 'Bianca', 'Cheng', 'Dana'])} ${rng.pick(['Vance', 'Ortiz', 'Kane'])}`;
    case 'operations director': return `${rng.pick(['Elif', 'Farid', 'Greta'])} ${rng.pick(['Voss', 'Reed', 'Salo'])}`;
    case 'sector': return rng.pick(Object.keys(SECTORS).filter((k) => sectorLabel(k) !== f.value).map(sectorLabel));
    case 'main line': case 'second line': {
      const alt = world.sectorPool.products.filter((p) => p !== c.prodA && p !== c.prodB);
      return alt.length ? rng.pick(alt) : null;
    }
    case 'core value': case 'second value': {
      const alt = world.sectorPool.principles.map((p) => p.value).filter((v) => v !== f.value);
      return alt.length ? rng.pick(alt) : null;
    }
    case 'strategic priority': {
      const alt = world.sectorPool.growth.map((g) => g.value).filter((v) => v !== f.value);
      return alt.length ? rng.pick(alt) : null;
    }
    default: return null;
  }
}

/** Render the statement sentence for a (fact, asserted-value). */
function statementFor(f, asserted) {
  const co = 'The company';
  switch (f.attribute) {
    case 'headquarters': return `${co}'s headquarters are in ${asserted}.`;
    case 'founded': return `${co} was founded in ${asserted}.`;
    case 'employees': return `${co} employs ${asserted}.`;
    case 'sector': return `${co} is ${asserted}.`;
    case 'core value': return `${co} regards ${asserted} as central to how it works.`;
    case 'second value': return `${co} emphasises ${asserted}.`;
    case 'strategic priority': return `${co}'s strategic priority is to ${asserted}.`;
    case 'market focus': return `${co} operates ${asserted}.`;
    case 'retail sites': return `${co} runs ${asserted} retail sites.`;
    case 'warehouses': return `${co} operates ${asserted} warehouses.`;
    case 'sales channel': return `${co} makes its sales ${asserted}.`;
    case 'main line': return `${co}'s main offering is ${asserted}.`;
    case 'second line': return `${co} offers ${asserted}.`;
    case 'chief executive': return `The chief executive is ${asserted}.`;
    case 'operations director': return `The operations director is ${asserted}.`;
    default: return `${co} reports that ${f.attribute} is ${asserted}.`;
  }
}

function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
