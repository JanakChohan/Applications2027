// cls/verify.js — INDEPENDENT verifier for grid categorisation.
// Re-implements the rule → group function (separate from generate.js) and checks
// that every shown example is coloured correctly AND that the target's stored
// answer matches the rule's verdict. Catches a mis-coloured example or wrong key.

const isDigit = (c) => c >= '0' && c <= '9';
const numLetters = (g) => g.filter((c) => !isDigit(c)).length;
const countOf = (g, ch) => g.filter((c) => c === ch).length;
const distinct = (g) => new Set(g).size;

function group(rule, g) {
  switch (rule.kind) {
    case 'centerDigit': return isDigit(g[4]) ? 'A' : 'B';
    case 'moreLetters': return numLetters(g) > 4 ? 'A' : 'B';
    case 'containsChar': return g.includes(rule.char) ? 'A' : 'B';
    case 'countChar2': return countOf(g, rule.char) >= 2 ? 'A' : 'B';
    case 'countChar3': return countOf(g, rule.char) >= 3 ? 'A' : 'B';
    case 'distinctEven': return distinct(g) % 2 === 0 ? 'A' : 'B';
    default: return 'B';
  }
}

export function verifyItem(item) {
  const problems = [];
  // examples must be coloured to match the rule, and both groups must be present
  const groups = new Set();
  for (const ex of item.examples) {
    const g = group(item.rule, ex.grid);
    if (g !== ex.group) problems.push('an example is coloured against the rule');
    groups.add(ex.group);
  }
  if (groups.size < 2) problems.push('examples do not show both groups');
  // target answer must match the rule's verdict
  const derived = group(item.rule, item.target);
  if (derived !== item.answer) problems.push(`target mismatch: rule=${derived} stored=${item.answer}`);

  return { ok: problems.length === 0, derivedLabel: derived, generatorLabel: item.answer, reason: problems.join('; ') || 'ok' };
}
