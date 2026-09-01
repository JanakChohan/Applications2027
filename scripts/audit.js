// -----------------------------------------------------------------------------
// audit.js — generate a large batch of items across every type and tier, then
// self-audit them for CORRECTNESS and DUPLICATION. Run with `npm run audit`.
//
// "Correct" here means: the independent verifier agrees with the generator's
// label for every single item. A single disagreement is a hard failure (exit 1)
// because a wrong-label item teaches the wrong reasoning.
// -----------------------------------------------------------------------------

import { generateSession } from '../src/generators/session.js';
import { verifyItem, deriveLabel } from '../src/verify/verifier.js';

const TIERS = ['beginner', 'intermediate', 'advanced'];
const TARGET = 200;

function run() {
  const items = [];
  const perDataset = [];
  let s = 0;
  // Collect >= TARGET items, spread across tiers and many datasets.
  while (items.length < TARGET) {
    const tier = TIERS[s % TIERS.length];
    const session = generateSession({ seed: `audit-${s}`, tier, count: 18 });
    for (const it of session.items) items.push({ ...it, _tier: tier, _dataset: session.dataset });
    perDataset.push(session);
    s++;
    if (s > 400) break; // safety
  }

  let failures = 0;
  const byType = {};
  const byLabel = { TRUE: 0, FALSE: 0, CANNOT_SAY: 0 };
  const byTier = {};
  const trapCounts = {};
  const sigCounts = {};
  const textCounts = {};

  for (const it of items) {
    byType[it.type] = (byType[it.type] || 0) + 1;
    byLabel[it.label] = (byLabel[it.label] || 0) + 1;
    byTier[it._tier] = (byTier[it._tier] || 0) + 1;
    (it.traps || []).forEach((t) => (trapCounts[t] = (trapCounts[t] || 0) + 1));

    // Re-verify independently (belt and braces).
    const v = verifyItem(it._dataset, it);
    const d = deriveLabel(it._dataset, it.claim);
    if (!v.ok || d !== it.label) {
      failures++;
      console.error(`✗ FAIL [${it.type}] "${it.text}"`);
      console.error(`   generator=${it.label} verifier=${d} reason=${v.reason}`);
    }

    const sig = signatureOf(it);
    sigCounts[sig] = (sigCounts[sig] || 0) + 1;
    textCounts[it.text] = (textCounts[it.text] || 0) + 1;
  }

  const dupSig = Object.entries(sigCounts).filter(([, n]) => n > 1);
  const dupText = Object.entries(textCounts).filter(([, n]) => n > 1);

  console.log('\n=== Aon scales trainer — item self-audit ===');
  console.log(`Items audited:        ${items.length} (from ${perDataset.length} datasets)`);
  console.log(`Label distribution:   ${fmtDist(byLabel, items.length)}`);
  console.log(`Tier distribution:    ${fmtDist(byTier, items.length)}`);
  console.log('\nBy item type:');
  for (const t of Object.keys(byType).sort()) {
    console.log(`   ${t.padEnd(14)} ${byType[t]}`);
  }
  console.log('\nTrap tags seen:');
  for (const t of Object.keys(trapCounts).sort()) {
    console.log(`   ${t.padEnd(20)} ${trapCounts[t]}`);
  }
  console.log('\nDuplication:');
  console.log(`   exact-text duplicates:      ${dupText.length} shapes`);
  console.log(`   same-question signatures:   ${dupSig.length} shapes repeated`);
  console.log(`   unique-text ratio:          ${(Object.keys(textCounts).length / items.length * 100).toFixed(1)}%`);

  console.log(`\nLabel-correctness failures: ${failures}`);
  if (failures > 0) {
    console.error('\n❌ AUDIT FAILED — mislabelled items exist. Do not ship.');
    process.exit(1);
  }
  console.log('✅ AUDIT PASSED — every item’s label was independently confirmed.\n');
}

function signatureOf(item) {
  const refs = (item.requiredCells || []).map((c) => `${c.m}:${c.e}:${c.p}`).sort().join(',');
  const op = item.claim.op || item.claim.dir || item.claim.sel || '';
  return `${item.type}|${item.claim.kind}|${op}|${refs}`;
}
function fmtDist(obj, total) {
  return Object.entries(obj)
    .map(([k, v]) => `${k}=${v} (${(v / total * 100).toFixed(0)}%)`)
    .join('  ');
}

run();
