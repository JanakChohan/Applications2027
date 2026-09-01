// Tests for the scoring model (negative marking, wrong-tab, blank=0) and the
// wrong-reason diagnosis — the coaching layer's correctness matters as much as
// the generator's, since it's what the user learns from.
import { describe, it, expect } from 'vitest';
import { scoreSession, requiredTabs } from '../src/coaching/scoring.js';
import { diagnose } from '../src/coaching/diagnosis.js';
import { percentileToStanine, rateToPercentile } from '../src/coaching/norms.js';

// A minimal tab-based module stub for the generic scorer (mirrors numerical).
const MOD = {
  usesTabs: true,
  answerOf: (it) => it.label,
  requiredTabsOf: (it) => [...requiredTabs(it)],
  diagnose,
};

// Build a fake session of simple items with known labels + required tabs.
function fakeSession(labels) {
  return {
    dataset: { tabs: [] },
    items: labels.map((label, i) => ({
      id: `x${i}`, index: i, type: 'lookup', tier: 'medium', label, traps: [],
      requiredCells: label === 'CANNOT_SAY' ? [] : [{ m: 'revenue', e: 'A', p: 'P1', tab: 'revenue' }],
      solution: { steps: [], rationale: '' },
    })),
  };
}

describe('scoreSession negative marking', () => {
  it('correct +1, wrong -1, blank 0', () => {
    const session = fakeSession(['TRUE', 'FALSE', 'TRUE', 'CANNOT_SAY']);
    const answers = [
      { given: 'TRUE', submittedTab: 'revenue', timeMs: 10000 }, // correct
      { given: 'TRUE', submittedTab: 'revenue', timeMs: 10000 }, // wrong
      { given: null, timeMs: 0 },                                // blank
      { given: 'CANNOT_SAY', timeMs: 8000 },                     // correct
    ];
    const s = scoreSession(session, answers, { wrongTabPenalty: true }, MOD);
    expect(s.correct).toBe(2);
    expect(s.wrong).toBe(1);
    expect(s.blank).toBe(1);
    expect(s.rawScore).toBe(1);       // 2 - 1
    expect(s.naiveScore).toBe(2);     // count-correct only
    expect(s.adjustedScore).toBe(1);  // no wrong-tab events here
  });

  it('applies the wrong-tab penalty when answering on a non-required tab', () => {
    const session = fakeSession(['TRUE']);
    const s = scoreSession(session, [{ given: 'TRUE', submittedTab: 'costs', timeMs: 5000 }], { wrongTabPenalty: true }, MOD);
    expect(s.correct).toBe(1);
    expect(s.wrongTabEvents).toBe(1);
    expect(s.adjustedScore).toBe(0); // +1 correct − 1 wrong-tab
  });

  it('can disable the wrong-tab penalty', () => {
    const session = fakeSession(['TRUE']);
    const s = scoreSession(session, [{ given: 'TRUE', submittedTab: 'costs' }], { wrongTabPenalty: false }, MOD);
    expect(s.adjustedScore).toBe(1);
  });
});

describe('diagnosis categories', () => {
  const item = (label, traps = [], type = 'lookup') => ({ label, traps, type });
  it('flags missed Cannot Say (over-inference)', () => {
    expect(diagnose(item('CANNOT_SAY'), { given: 'TRUE', timeMs: 15000 }).category).toBe('missed_cannot_say');
  });
  it('flags over-caution (said Cannot Say when answerable)', () => {
    expect(diagnose(item('TRUE'), { given: 'CANNOT_SAY', timeMs: 15000 }).category).toBe('over_cautious');
  });
  it('flags a fast wrong guess', () => {
    expect(diagnose(item('TRUE'), { given: 'FALSE', timeMs: 3000 }).category).toBe('panicked_guess');
  });
  it('flags percent-vs-points confusion via trap tag', () => {
    expect(diagnose(item('TRUE', ['pct_vs_pp']), { given: 'FALSE', timeMs: 20000 }).category).toBe('pct_vs_pp_confusion');
  });
  it('flags slow-but-correct', () => {
    expect(diagnose(item('TRUE'), { given: 'TRUE', timeMs: 60000 }).category).toBe('slow_but_correct');
  });
  it('flags wrong-tab', () => {
    expect(diagnose(item('TRUE'), { given: 'FALSE', wrongTab: true, timeMs: 20000 }).category).toBe('wrong_tab');
  });
  it('distinguishes timeout blank from deliberate skip', () => {
    expect(diagnose(item('TRUE'), { given: null, ranOutOfTime: true }).category).toBe('ran_out_of_time');
    expect(diagnose(item('TRUE'), { given: null, ranOutOfTime: false }).category).toBe('skipped_blank');
  });
});

describe('norms', () => {
  it('maps score-rate monotonically to percentile', () => {
    expect(rateToPercentile(-0.5)).toBeLessThan(rateToPercentile(0.5));
  });
  it('percentile → stanine boundaries', () => {
    expect(percentileToStanine(50)).toBe(5);
    expect(percentileToStanine(2)).toBe(1);
    expect(percentileToStanine(99)).toBe(9);
  });
});
