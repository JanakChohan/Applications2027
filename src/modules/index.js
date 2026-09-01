// modules/index.js — the module registry. Each module is self-contained and
// implements the shared interface the shell + coaching rely on:
//   { id, label, blurb, tiers[], usesTabs, answerKind, modes[],
//     generate(opts) -> { module, context?, items[] },
//     answerOf, tokenLabel, requiredTabsOf, renderReview, diagnose,
//     renderDisplay?/renderControls?/wireQuestion?  (for custom answer UIs),
//     adaptive?(storeData) -> partial generate opts }
import numerical from './numerical/index.js';
import verbal from './verbal/index.js';
import tabhunt from './tabhunt/index.js';
import ix from './ix/index.js';
import lst from './lst/index.js';
import cls from './cls/index.js';

export const MODULES = [numerical, tabhunt, verbal, ix, lst, cls];
export const moduleById = Object.fromEntries(MODULES.map((m) => [m.id, m]));
