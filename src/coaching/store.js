// -----------------------------------------------------------------------------
// store.js — persistent progress store (localStorage in the browser, in-memory
// fallback under Node so tests/audit can import this module).
//
// Tracks accuracy by item type, by difficulty, by wrong-reason, and a dated
// history so the progress screen can show whether you're actually improving.
// -----------------------------------------------------------------------------

const KEY = 'aon-scales-trainer:v1';

// In-browser we use window.localStorage; elsewhere a tiny memory shim.
const backend = (() => {
  try {
    if (typeof localStorage !== 'undefined') return localStorage;
  } catch { /* access can throw in some sandboxes */ }
  const mem = new Map();
  return {
    getItem: (k) => (mem.has(k) ? mem.get(k) : null),
    setItem: (k, v) => mem.set(k, v),
    removeItem: (k) => mem.delete(k),
  };
})();

function blank() {
  return {
    version: 1,
    sessions: [],                 // one summary per completed session
    byType: {},                   // type -> {seen, correct, wrong, blank, timeMs}
    byTier: {},                   // tier -> {seen, correct, wrong, blank}
    byReason: {},                 // diagnosis category -> count
    history: [],                  // [{date, accuracy, stanine, adjusted, count}]
  };
}

export function load() {
  try {
    const raw = backend.getItem(KEY);
    if (!raw) return blank();
    const data = JSON.parse(raw);
    return { ...blank(), ...data };
  } catch {
    return blank();
  }
}

export function save(data) {
  backend.setItem(KEY, JSON.stringify(data));
  return data;
}

export function reset() {
  backend.removeItem(KEY);
  return blank();
}

/**
 * Fold a scored session into the store.
 * @param {object} score  the result from scoreSession
 * @param {object} meta   { mode, tier, dateISO }
 */
export function recordSession(score, meta) {
  const data = load();
  const bump = (bucket, key, patch) => {
    const b = (bucket[key] ??= { seen: 0, correct: 0, wrong: 0, blank: 0, timeMs: 0 });
    for (const k in patch) b[k] = (b[k] || 0) + patch[k];
  };

  for (const p of score.perItem) {
    const outcome = p.isBlank ? 'blank' : p.isCorrect ? 'correct' : 'wrong';
    bump(data.byType, p.item.type, { seen: 1, [outcome]: 1, timeMs: p.timeMs || 0 });
    bump(data.byTier, p.item.tier || meta.tier || 'intermediate', { seen: 1, [outcome]: 1 });
    data.byReason[p.diagnosis.category] = (data.byReason[p.diagnosis.category] || 0) + 1;
  }

  data.sessions.push({
    date: meta.dateISO, mode: meta.mode, tier: meta.tier, count: score.count,
    correct: score.correct, wrong: score.wrong, blank: score.blank,
    adjustedScore: score.adjustedScore, stanine: score.stanine, percentile: score.percentile,
    accuracyAttempted: score.accuracyAttempted, coverage: score.coverage,
  });
  data.history.push({
    date: meta.dateISO, accuracy: score.accuracyAttempted,
    stanine: score.stanine, adjusted: score.adjustedScore, count: score.count,
  });

  return save(data);
}

/** Accuracy (correct / seen) per item type, with attempt counts. */
export function typeAccuracy(data = load()) {
  const out = {};
  for (const [type, b] of Object.entries(data.byType)) {
    out[type] = { seen: b.seen, accuracy: b.seen ? b.correct / b.seen : 0,
      avgTimeMs: b.seen ? b.timeMs / b.seen : 0 };
  }
  return out;
}
