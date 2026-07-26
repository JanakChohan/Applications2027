// Tests for the INDEPENDENT verifier against hand-built datasets, plus the
// whole-pipeline invariant: across many seeds/tiers, every generated item must
// pass verification, no decidable item may reference a hidden cell, and every
// Cannot Say must reference a genuinely missing cell.
import { describe, it, expect } from 'vitest';
import { deriveLabel, verifyItem } from '../src/verify/verifier.js';
import { cell, num, pctChange } from '../src/generators/claim.js';
import { generateSession } from '../src/generators/session.js';
import { generateDataset } from '../src/generators/dataset.js';

// Minimal dataset shaped like the real one, but with values we control.
function fakeDataset() {
  return {
    tabs: [
      {
        metric: 'revenue', entities: ['A', 'B'], periods: ['P1', 'P2'], hasTotal: false,
        cells: [
          { e: 'A', p: 'P1', base: 100 }, { e: 'A', p: 'P2', base: 130 },
          { e: 'B', p: 'P1', base: 200 }, { e: 'B', p: 'P2', base: 150 },
        ],
      },
    ],
  };
}

describe('deriveLabel on a controlled dataset', () => {
  const ds = fakeDataset();
  it('TRUE: A rose 30% > 25%', () =>
    expect(deriveLabel(ds, {
      kind: 'cmp', lhs: pctChange(cell('revenue', 'A', 'P1'), cell('revenue', 'A', 'P2')),
      op: '>', rhs: num(25),
    })).toBe('TRUE'));
  it('FALSE: A rose 30%, not > 40%', () =>
    expect(deriveLabel(ds, {
      kind: 'cmp', lhs: pctChange(cell('revenue', 'A', 'P1'), cell('revenue', 'A', 'P2')),
      op: '>', rhs: num(40),
    })).toBe('FALSE'));
  it('CANNOT_SAY: references a hidden period', () =>
    expect(deriveLabel(ds, {
      kind: 'cmp', lhs: cell('revenue', 'A', 'P9'), op: '>', rhs: num(1),
    })).toBe('CANNOT_SAY'));
  it('CANNOT_SAY: references a hidden metric', () =>
    expect(deriveLabel(ds, {
      kind: 'cmp', lhs: cell('units', 'A', 'P1'), op: '>', rhs: num(1),
    })).toBe('CANNOT_SAY'));
});

describe('verifyItem rejects a deliberately mislabelled item', () => {
  it('flags a label that disagrees with the data', () => {
    const ds = fakeDataset();
    const bad = {
      text: 'x', label: 'TRUE', // WRONG on purpose (A P2 = 130, not > 200)
      claim: { kind: 'cmp', lhs: cell('revenue', 'A', 'P2'), op: '>', rhs: num(200) },
      requiredCells: [{ m: 'revenue', e: 'A', p: 'P2' }],
    };
    const v = verifyItem(ds, bad);
    expect(v.ok).toBe(false);
    expect(v.derivedLabel).toBe('FALSE');
  });
});

describe('PIPELINE INVARIANT: every generated item verifies', () => {
  const tiers = ['beginner', 'intermediate', 'advanced'];
  it('no mislabelled items across many seeds', () => {
    let n = 0;
    for (let s = 0; s < 30; s++) {
      const tier = tiers[s % 3];
      const session = generateSession({ seed: `t-${s}`, tier, count: 18 });
      for (const item of session.items) {
        const v = verifyItem(session.dataset, item);
        expect(v.ok, `item "${item.text}" → ${v.reason}`).toBe(true);
        expect(deriveLabel(session.dataset, item.claim)).toBe(item.label);
        n++;
      }
    }
    expect(n).toBeGreaterThanOrEqual(500);
  });

  it('decidable items never depend on a hidden cell; Cannot Say always does', () => {
    for (let s = 0; s < 20; s++) {
      const session = generateSession({ seed: `inv-${s}`, tier: 'advanced', count: 18 });
      const ds = session.dataset;
      const key = (c) => `${c.m}::${c.e}::${c.p}`;
      const visible = new Set();
      for (const t of ds.tabs) for (const c of t.cells) visible.add(key({ m: t.metric, e: c.e, p: c.p }));
      for (const t of ds.tabs) if (t.caption) visible.add(key({ m: t.caption.metric, e: t.caption.entity, p: t.caption.period }));

      for (const item of session.items) {
        const missing = item.requiredCells.filter((c) => !visible.has(key(c)));
        if (item.label === 'CANNOT_SAY') expect(missing.length).toBeGreaterThan(0);
        else expect(missing.length).toBe(0);
      }
    }
  });
});

describe('dataset shape', () => {
  it('always produces six tabs with a latent entity, metric, and periods', () => {
    for (let s = 0; s < 10; s++) {
      const ds = generateDataset(`d-${s}`, 'intermediate');
      expect(ds.tabs.length).toBe(6);
      expect(ds.entityLatent).toBeTruthy();
      expect(ds.periodLatentBefore.length).toBeGreaterThan(0);
      expect(ds.values.latent).toBeTruthy();
    }
  });
});
