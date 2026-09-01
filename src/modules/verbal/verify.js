// -----------------------------------------------------------------------------
// verbal/verify.js — the INDEPENDENT verifier for the verbal module.
//
// It rebuilds "what the passages actually state" from world.tabs (NOT from the
// generator's world.facts map), then re-derives each statement's label by its own
// code path. The session/audit drops any item whose verifier label disagrees with
// the generator's. This catches both logic bugs and "claimed a fact that was never
// rendered into a tab" bugs — the verbal analogue of the numerical verifier.
// -----------------------------------------------------------------------------

import { key, norm } from './generate.js';

/** Rebuild the shown-facts index straight from the rendered tabs. */
function shownFacts(world) {
  const map = new Map();
  for (const tab of world.tabs) {
    for (const f of tab.facts) {
      map.set(key(f.subject, f.attribute), { value: f.value, synonyms: f.synonyms || [], tab: tab.id });
    }
  }
  return map;
}

/** Independently derive TRUE / FALSE / CANNOT_SAY for a claim. */
export function deriveLabel(world, claim) {
  const shown = shownFacts(world);
  const f = shown.get(key(claim.subject, claim.attribute));
  if (!f) return 'CANNOT_SAY';                              // attribute not stated anywhere
  const a = norm(claim.asserted);
  if (a === norm(f.value)) return 'TRUE';                   // exact match
  if (f.synonyms.some((s) => norm(s) === a)) return 'TRUE'; // genuine synonym
  return 'FALSE';                                           // the tab states a different value
}

/** Which tab is relevant to a decidable claim (for wrong-tab + worked solution). */
export function relevantTab(world, claim) {
  const shown = shownFacts(world);
  const f = shown.get(key(claim.subject, claim.attribute));
  return f ? f.tab : null;
}

export function verifyItem(world, item) {
  const problems = [];
  if (!item.statement) problems.push('missing statement');
  if (!item.claim) problems.push('missing claim');
  if (!['TRUE', 'FALSE', 'CANNOT_SAY'].includes(item.label)) problems.push('bad label');

  let derived = null;
  if (item.claim) {
    derived = deriveLabel(world, item.claim);
    if (derived !== item.label) problems.push(`label mismatch: gen=${item.label} verifier=${derived}`);
  }
  // Cannot Say honesty: the attribute must genuinely be absent from every tab.
  if (item.label === 'CANNOT_SAY') {
    const shown = shownFacts(world);
    if (shown.has(key(item.claim.subject, item.claim.attribute))) problems.push('Cannot Say about a stated attribute');
  }
  return { ok: problems.length === 0, derivedLabel: derived, generatorLabel: item.label, reason: problems.join('; ') || 'ok' };
}
