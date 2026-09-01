// -----------------------------------------------------------------------------
// store.js — persistent progress across ALL modules (localStorage in the browser,
// in-memory fallback under Node). Tracks accuracy by module, by fine-grained skill
// (`module:skill`), by difficulty, by wrong-reason, and a dated history so the
// progress screen can show whether you're improving on each test type.
// -----------------------------------------------------------------------------

const KEY = 'aon-scales-trainer:v2';

const backend = (() => {
  try { if (typeof localStorage !== 'undefined') return localStorage; } catch { /* sandboxed */ }
  const mem = new Map();
  return { getItem: (k) => (mem.has(k) ? mem.get(k) : null), setItem: (k, v) => mem.set(k, v), removeItem: (k) => mem.delete(k) };
})();

function blank() {
  return { version: 2, sessions: [], byModule: {}, bySkill: {}, byTier: {}, byReason: {}, history: [] };
}

export function load() {
  try {
    const raw = backend.getItem(KEY);
    if (!raw) return blank();
    return { ...blank(), ...JSON.parse(raw) };
  } catch { return blank(); }
}
export function save(data) { backend.setItem(KEY, JSON.stringify(data)); return data; }
export function reset() { backend.removeItem(KEY); return blank(); }

/** The fine-grained skill bucket for an item (falls back to its type). */
export function skillOf(item) { return item.skill || item.type || 'general'; }

export function recordSession(score, meta) {
  const data = load();
  const bump = (bucket, key, outcome, timeMs = 0) => {
    const b = (bucket[key] ??= { seen: 0, correct: 0, wrong: 0, blank: 0, timeMs: 0 });
    b.seen++; b[outcome]++; b.timeMs += timeMs || 0;
  };
  for (const p of score.perItem) {
    const outcome = p.isBlank ? 'blank' : p.isCorrect ? 'correct' : 'wrong';
    bump(data.byModule, meta.module, outcome, p.timeMs || 0);
    bump(data.bySkill, `${meta.module}:${skillOf(p.item)}`, outcome, p.timeMs || 0);
    bump(data.byTier, `${meta.module}:${p.item.tier || meta.tier}`, outcome, p.timeMs || 0);
    data.byReason[p.diagnosis.category] = (data.byReason[p.diagnosis.category] || 0) + 1;
  }
  data.sessions.push({
    date: meta.dateISO, module: meta.module, mode: meta.mode, tier: meta.tier, count: score.count,
    correct: score.correct, wrong: score.wrong, blank: score.blank,
    adjustedScore: score.adjustedScore, stanine: score.stanine, percentile: score.percentile,
    accuracyAttempted: score.accuracyAttempted, coverage: score.coverage,
  });
  data.history.push({ date: meta.dateISO, module: meta.module, accuracy: score.accuracyAttempted, stanine: score.stanine, count: score.count });
  return save(data);
}

/** Accuracy per fine-grained skill within a module. */
export function skillAccuracy(moduleId, data = load()) {
  const out = {};
  for (const [key, b] of Object.entries(data.bySkill)) {
    if (!key.startsWith(`${moduleId}:`)) continue;
    out[key.slice(moduleId.length + 1)] = { seen: b.seen, accuracy: b.seen ? b.correct / b.seen : 0, avgTimeMs: b.seen ? b.timeMs / b.seen : 0 };
  }
  return out;
}
