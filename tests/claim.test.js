// Hand-computed tests for the claim evaluator. These pin EXACT expected values
// computed by hand, so a bug shared by both evaluators (the one case item-vs-
// verifier agreement can't catch) still fails a test.
import { describe, it, expect } from 'vitest';
import {
  evalExpr, evalClaim, compareNums, trendHolds, MISSING, LABEL,
  cell, num, sub, pctChange, pctPoints, shareOf,
} from '../src/generators/claim.js';

// A tiny fixed resolver: base-unit values keyed "m|e|p".
const DATA = {
  'rev|A|P1': 100, 'rev|A|P2': 130, 'rev|B|P1': 200, 'rev|B|P2': 150,
  'cost|A|P2': 40, 'mar|A|P1': 10, 'mar|A|P2': 15, 'tot|X|P2': 400,
};
const resolve = (r) => DATA[`${r.m}|${r.e}|${r.p}`];

describe('evalExpr arithmetic', () => {
  it('resolves a cell', () => expect(evalExpr(cell('rev', 'A', 'P1'), resolve)).toBe(100));
  it('returns MISSING for an absent cell', () =>
    expect(evalExpr(cell('rev', 'Z', 'P9'), resolve)).toBe(MISSING));
  it('subtracts', () =>
    expect(evalExpr(sub(cell('rev', 'A', 'P2'), cell('rev', 'A', 'P1')), resolve)).toBe(30));
  it('percentage change divides by the ORIGINAL', () =>
    expect(evalExpr(pctChange(cell('rev', 'A', 'P1'), cell('rev', 'A', 'P2')), resolve)).toBeCloseTo(30, 9));
  it('percentage change is negative when falling', () =>
    expect(evalExpr(pctChange(cell('rev', 'B', 'P1'), cell('rev', 'B', 'P2')), resolve)).toBeCloseTo(-25, 9));
  it('percentage POINTS subtracts the two rates', () =>
    expect(evalExpr(pctPoints(cell('mar', 'A', 'P2'), cell('mar', 'A', 'P1')), resolve)).toBeCloseTo(5, 9));
  it('shareOf = part / whole * 100', () =>
    expect(evalExpr(shareOf(cell('rev', 'A', 'P2'), cell('tot', 'X', 'P2')), resolve)).toBeCloseTo(32.5, 9));
});

describe('percentage-points vs percent are DIFFERENT numbers', () => {
  // margin 10% -> 15%: +5 points but +50% relative. This is the core trap.
  it('points = 5', () =>
    expect(evalExpr(pctPoints(cell('mar', 'A', 'P2'), cell('mar', 'A', 'P1')), resolve)).toBeCloseTo(5, 9));
  it('relative % = 50', () =>
    expect(evalExpr(pctChange(cell('mar', 'A', 'P1'), cell('mar', 'A', 'P2')), resolve)).toBeCloseTo(50, 9));
});

describe('compareNums (close-but-not-exact = FALSE)', () => {
  it('1,550,000 == 1,500,000 is false', () =>
    expect(compareNums(1550000, '==', 1500000)).toBe(false));
  it('exact equality holds under float noise', () =>
    expect(compareNums(0.1 + 0.2, '==', 0.3)).toBe(true));
  it('> is strict', () => expect(compareNums(5, '>', 5)).toBe(false));
  it('approx respects tolerance', () =>
    expect(compareNums(102, 'approx', 100, { frac: 0.05 })).toBe(true));
});

describe('trendHolds', () => {
  it('increasing', () => expect(trendHolds([1, 2, 3, 4], 'increasing')).toBe(true));
  it('breaks on a single dip', () => expect(trendHolds([1, 2, 2, 4], 'increasing')).toBe(false));
  it('decreasing', () => expect(trendHolds([9, 5, 2], 'decreasing')).toBe(true));
});

describe('evalClaim labels', () => {
  it('TRUE when data confirms', () =>
    expect(evalClaim({ kind: 'cmp', lhs: cell('rev', 'A', 'P2'), op: '>', rhs: num(120) }, resolve)).toBe(LABEL.TRUE));
  it('FALSE when data contradicts', () =>
    expect(evalClaim({ kind: 'cmp', lhs: cell('rev', 'A', 'P2'), op: '>', rhs: num(200) }, resolve)).toBe(LABEL.FALSE));
  it('CANNOT_SAY when a required cell is missing', () =>
    expect(evalClaim({ kind: 'cmp', lhs: cell('rev', 'Z', 'P2'), op: '>', rhs: num(1) }, resolve)).toBe(LABEL.CANNOT_SAY));
  it('rank max', () =>
    expect(evalClaim({
      kind: 'rank', among: [{ m: 'rev', e: 'A', p: 'P1' }, { m: 'rev', e: 'B', p: 'P1' }],
      target: { m: 'rev', e: 'B', p: 'P1' }, sel: 'max',
    }, resolve)).toBe(LABEL.TRUE));
});
