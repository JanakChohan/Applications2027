// -----------------------------------------------------------------------------
// norms.js — a SYNTHETIC, transparent norm curve.
//
// The real Aon test is norm-referenced: your raw score is compared against a
// comparison group and reported as a percentile + Stanine (1–9). Aon's actual
// norm tables are confidential (see research/FINDINGS.md §2), so we CANNOT show
// a real percentile. Instead we map your penalised score-rate through a plain
// logistic curve tuned to feel roughly like a graduate norm, and we label it
// "illustrative" everywhere it appears. It is a training signal, not an official
// Aon result.
// -----------------------------------------------------------------------------

// Standard-normal CDF (Abramowitz–Stegun approximation) for the logistic map.
function phi(z) {
  const t = 1 / (1 + 0.2316419 * Math.abs(z));
  const d = 0.3989423 * Math.exp(-z * z / 2);
  let p = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
  return z > 0 ? 1 - p : p;
}

/**
 * Map a penalised score-RATE (adjustedScore / itemCount, roughly in [-1, 1]) to
 * an illustrative percentile (1–99). Centre and spread chosen so that:
 *   • answering ~55% correct with few penalties ≈ ~55th–65th percentile,
 *   • heavy guessing (many wrong) drags you well below average.
 */
export function rateToPercentile(rate) {
  const mu = 0.34;      // an "average" candidate nets ~34% after penalties
  const sigma = 0.24;
  const pct = Math.round(phi((rate - mu) / sigma) * 100);
  return Math.min(99, Math.max(1, pct));
}

// Standard Stanine boundaries by percentile.
export function percentileToStanine(pct) {
  if (pct <= 4) return 1;
  if (pct <= 11) return 2;
  if (pct <= 23) return 3;
  if (pct <= 40) return 4;
  if (pct <= 60) return 5;
  if (pct <= 77) return 6;
  if (pct <= 89) return 7;
  if (pct <= 96) return 8;
  return 9;
}

export const STANINE_LABEL = {
  1: 'well below average', 2: 'below average', 3: 'below average',
  4: 'lower average', 5: 'average', 6: 'upper average',
  7: 'above average', 8: 'well above average', 9: 'top band',
};
