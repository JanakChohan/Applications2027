// -----------------------------------------------------------------------------
// audit-modules.js — self-audit for the verbal + logical/inductive modules.
// For each module it generates >=150 shipped items across tiers and checks:
//   • every item passes its own independent verifier (ship condition), AND
//   • an INDEPENDENT oracle here (a third computation) agrees with the answer.
// A single disagreement is a hard failure — a mislabelled item teaches the wrong
// reasoning. Also reports answer distribution and duplication.
// -----------------------------------------------------------------------------

import verbal from '../src/modules/verbal/index.js';
import ix from '../src/modules/ix/index.js';
import lst from '../src/modules/lst/index.js';
import cls from '../src/modules/cls/index.js';
import { verifyItem as vVerify } from '../src/modules/verbal/verify.js';
import { labelOf as vLabelOf } from '../src/modules/verbal/generate.js';
import { verifyItem as ixVerify } from '../src/modules/ix/verify.js';
import { verifyItem as lstVerify } from '../src/modules/lst/verify.js';
import { verifyItem as clsVerify } from '../src/modules/cls/verify.js';

const TIERS = ['beginner', 'intermediate', 'advanced'];
let hardFail = 0;

// ---- independent oracles (deliberately re-implemented) ----------------------
const sides = (s) => ({ circle: 0, triangle: 3, square: 4, pentagon: 5, hexagon: 6, heptagon: 7, octagon: 8, diamond: 4, star: 5 }[s] ?? 4);
function ixOracle(item) {
  const sat = (o) => {
    const r = item.rule;
    if (r.kind === 'sameShape') return o.shape === r.value;
    if (r.kind === 'filled') return o.filled === r.value;
    if (r.kind === 'sameRotation') return o.rotation === r.value;
    if (r.kind === 'hasInner') return (o.inner != null) === r.value;
    if (r.kind === 'evenSides') return sides(o.shape) % 2 === 0;
    return true;
  };
  const v = [];
  item.objects.forEach((o, k) => { if (!sat(o)) v.push(k); });
  return v.length === 1 && v[0] === Number(item.answer);
}
function lstOracle(item) {
  const { solution, shown, shapes, N, ask, answer } = item;
  for (let r = 0; r < N; r++) if (new Set(solution[r]).size !== N) return false;
  for (let c = 0; c < N; c++) if (new Set(solution.map((row) => row[c])).size !== N) return false;
  const used = new Set();
  for (let k = 0; k < N; k++) { if (shown[ask.r][k]) used.add(shown[ask.r][k]); if (shown[k][ask.c]) used.add(shown[k][ask.c]); }
  const cand = shapes.filter((s) => !used.has(s));
  return cand.length === 1 && cand[0] === answer && solution[ask.r][ask.c] === answer;
}
function clsOracle(item) {
  const isDigit = (c) => c >= '0' && c <= '9';
  const grp = (g) => {
    const r = item.rule;
    if (r.kind === 'centerDigit') return isDigit(g[4]) ? 'A' : 'B';
    if (r.kind === 'moreLetters') return g.filter((c) => !isDigit(c)).length > 4 ? 'A' : 'B';
    if (r.kind === 'containsChar') return g.includes(r.char) ? 'A' : 'B';
    if (r.kind === 'countChar2') return g.filter((c) => c === r.char).length >= 2 ? 'A' : 'B';
    if (r.kind === 'countChar3') return g.filter((c) => c === r.char).length >= 3 ? 'A' : 'B';
    if (r.kind === 'distinctEven') return new Set(g).size % 2 === 0 ? 'A' : 'B';
    return 'B';
  };
  if (item.examples.some((e) => grp(e.grid) !== e.group)) return false;
  return grp(item.target) === item.answer;
}

function auditModule(mod, verify, oracle, opts = {}) {
  const items = [];
  const worlds = [];
  let s = 0;
  while (items.length < 150 && s < 400) {
    const tier = TIERS[s % 3];
    const session = mod.generate({ seed: `am-${mod.id}-${s}`, tier, count: 16 });
    session.items.forEach((it) => { items.push(it); worlds.push(session.world || null); });
    s++;
  }
  let verifyFail = 0, oracleFail = 0;
  const dist = {}; const sigs = {};
  items.forEach((it, i) => {
    const v = verify(opts.needsWorld ? worlds[i] : it, opts.needsWorld ? it : undefined);
    if (!v.ok) { verifyFail++; if (verifyFail <= 3) console.error(`  verify fail [${mod.id}] ${v.reason}`); }
    const ok = opts.needsWorld ? oracle(it, worlds[i]) : oracle(it);
    if (!ok) { oracleFail++; if (oracleFail <= 3) console.error(`  ORACLE MISMATCH [${mod.id}] "${(it.prompt || '').slice(0, 60)}" answer=${it.answer}`); }
    const tok = opts.answerOf ? opts.answerOf(it) : it.answer;
    dist[tok] = (dist[tok] || 0) + 1;
    const sig = opts.sig(it);
    sigs[sig] = (sigs[sig] || 0) + 1;
  });
  const dups = Object.values(sigs).filter((n) => n > 1).length;
  const uniq = (Object.keys(sigs).length / items.length * 100).toFixed(1);
  console.log(`\n[${mod.id}] ${items.length} items · answers ${JSON.stringify(dist)} · unique ${uniq}% · repeated-shapes ${dups}`);
  console.log(`     verifier failures: ${verifyFail} · independent-oracle failures: ${oracleFail}`);
  if (verifyFail || oracleFail) hardFail += verifyFail + oracleFail;
}

console.log('=== verbal + logical module audit ===');
// verbal oracle uses the GENERATOR's labelOf (reads world.facts) — an independent
// path from the verifier's deriveLabel (which reads the rendered tabs).
auditModule(verbal, (world, it) => vVerify(world, it), (it, world) => vLabelOf(world, it.claim) === it.label, { needsWorld: true, answerOf: (it) => it.label, sig: (it) => `${it.claim.subject}|${it.claim.attribute}|${it.claim.asserted}` });
auditModule(ix, (it) => ixVerify(it), ixOracle, { sig: (it) => it.rule.kind + it.objects.map((o) => `${o.shape}${o.rotation}${o.filled}${o.inner}`).join() });
auditModule(lst, (it) => lstVerify(it), lstOracle, { sig: (it) => it.shown.map((r) => r.map((x) => x || '?').join()).join('|') + it.ask.r + it.ask.c });
auditModule(cls, (it) => clsVerify(it), clsOracle, { sig: (it) => it.rule.kind + (it.rule.char || '') + it.target.join() });

if (hardFail) { console.error(`\n❌ AUDIT FAILED — ${hardFail} correctness problems.`); process.exit(1); }
console.log('\n✅ MODULE AUDIT PASSED — every item independently confirmed.');
