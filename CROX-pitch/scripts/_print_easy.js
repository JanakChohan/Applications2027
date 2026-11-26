
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => [...document.querySelectorAll('.pg')].map((s, i) => { const f = s.querySelector('.foot'); let bottom = 0; for (const c of s.children) { if (c !== f) bottom = Math.max(bottom, c.getBoundingClientRect().bottom); } return [i + 1, Math.round(bottom - f.getBoundingClientRect().top)]; }).filter(x => x[1] > -4));
  console.log('fonts:', await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').length), 'pages overflowing (page, px past footer):', JSON.stringify(over));
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, margin: { top: '0', bottom: '0', left: '0', right: '0' } });
  await b.close();
})();
