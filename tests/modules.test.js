// Tests for the verbal + logical/inductive modules. The core guarantee mirrors
// the numerical module: every generated item passes its INDEPENDENT verifier, and
// deliberately corrupting an item's answer makes the verifier reject it (so a
// mislabelled item can never ship).
import { describe, it, expect } from 'vitest';
import verbal from '../src/modules/verbal/index.js';
import ix from '../src/modules/ix/index.js';
import lst from '../src/modules/lst/index.js';
import cls from '../src/modules/cls/index.js';
import { verifyItem as vVerify } from '../src/modules/verbal/verify.js';
import { verifyItem as ixVerify } from '../src/modules/ix/verify.js';
import { verifyItem as lstVerify } from '../src/modules/lst/verify.js';
import { verifyItem as clsVerify } from '../src/modules/cls/verify.js';

const TIERS = ['beginner', 'intermediate', 'advanced'];

describe('verbal: every item verifies; Cannot Say is honest', () => {
  it('pipeline invariant', () => {
    let n = 0;
    for (let s = 0; s < 12; s++) {
      const session = verbal.generate({ seed: `vt-${s}`, tier: TIERS[s % 3], count: 15 });
      for (const item of session.items) {
        expect(vVerify(session.world, item).ok, item.statement).toBe(true);
        if (item.label === 'CANNOT_SAY') {
          // the asked attribute must not be stated on any tab
          const shown = new Set();
          session.world.tabs.forEach((t) => t.facts.forEach((f) => shown.add(`${f.subject}||${f.attribute}`)));
          expect(shown.has(`${item.claim.subject}||${item.claim.attribute}`)).toBe(false);
        }
        n++;
      }
    }
    expect(n).toBeGreaterThan(120);
  });
  it('rejects a flipped label', () => {
    const session = verbal.generate({ seed: 'vflip', tier: 'intermediate', count: 6 });
    const item = session.items[0];
    const bad = { ...item, label: item.label === 'TRUE' ? 'FALSE' : 'TRUE' };
    expect(vVerify(session.world, bad).ok).toBe(false);
  });
});

describe('ix: exactly one rule-breaker, at the stored index', () => {
  it('pipeline invariant', () => {
    for (let s = 0; s < 12; s++) {
      const session = ix.generate({ seed: `xt-${s}`, tier: TIERS[s % 3], count: 12 });
      for (const item of session.items) expect(ixVerify(item).ok).toBe(true);
    }
  });
  it('rejects a wrong breaker index', () => {
    const item = ix.generate({ seed: 'xflip', tier: 'beginner', count: 3 }).items[0];
    const bad = { ...item, breakerIndex: (item.breakerIndex + 1) % 9 };
    expect(ixVerify(bad).ok).toBe(false);
  });
});

describe('lst: valid Latin square, "?" uniquely forced', () => {
  it('pipeline invariant', () => {
    for (let s = 0; s < 12; s++) {
      const session = lst.generate({ seed: `lt-${s}`, tier: TIERS[s % 3], count: 10 });
      for (const item of session.items) expect(lstVerify(item).ok).toBe(true);
    }
  });
  it('rejects a wrong answer shape', () => {
    const item = lst.generate({ seed: 'lflip', tier: 'beginner', count: 3 }).items[0];
    const other = item.choices.find((s) => s !== item.answer);
    expect(lstVerify({ ...item, answer: other }).ok).toBe(false);
  });
});

describe('cls: examples coloured by the rule, target correct', () => {
  it('pipeline invariant', () => {
    for (let s = 0; s < 12; s++) {
      const session = cls.generate({ seed: `ct-${s}`, tier: TIERS[s % 3], count: 10 });
      for (const item of session.items) expect(clsVerify(item).ok).toBe(true);
    }
  });
  it('rejects a flipped target group', () => {
    const item = cls.generate({ seed: 'cflip', tier: 'intermediate', count: 3 }).items[0];
    expect(clsVerify({ ...item, answer: item.answer === 'A' ? 'B' : 'A' }).ok).toBe(false);
  });
});
