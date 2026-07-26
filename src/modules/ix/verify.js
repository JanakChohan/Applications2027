// ix/verify.js — INDEPENDENT verifier for odd-one-out.
// Re-implements the rule predicate (separate from generate.js) and confirms that
// EXACTLY ONE object violates the rule and that it is the stored breaker index.
// If zero or more than one object violates, the item is ambiguous and rejected.

function sides(shape) {
  return { circle: 0, triangle: 3, square: 4, pentagon: 5, hexagon: 6, heptagon: 7, octagon: 8, diamond: 4, star: 5 }[shape] ?? 4;
}

function satisfies(rule, o) {
  switch (rule.kind) {
    case 'sameShape': return o.shape === rule.value;
    case 'filled': return o.filled === rule.value;
    case 'sameRotation': return o.rotation === rule.value;
    case 'hasInner': return (o.inner != null) === rule.value;
    case 'evenSides': return sides(o.shape) % 2 === 0;
    default: return true;
  }
}

export function verifyItem(item) {
  const problems = [];
  const violators = [];
  item.objects.forEach((o, k) => { if (!satisfies(item.rule, o)) violators.push(k); });

  if (violators.length === 0) problems.push('no object breaks the rule');
  else if (violators.length > 1) problems.push(`ambiguous: ${violators.length} objects break the rule`);
  else if (violators[0] !== item.breakerIndex) problems.push(`breaker mismatch: found ${violators[0]} stored ${item.breakerIndex}`);

  return {
    ok: problems.length === 0,
    derivedLabel: violators.length === 1 ? String(violators[0]) : null,
    generatorLabel: item.answer,
    reason: problems.join('; ') || 'ok',
  };
}
