// Preview Parts 3 and 4 only: node build/preview_p34.js -> /tmp/claude-0/p34.pdf
const fs = require('fs');
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const body = ['03_why_built.html', '04_stand_out.html'].map(f => fs.readFileSync(path.join(ROOT, 'parts', f), 'utf8')).join('\n');
const html = `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${body}</body></html>`;
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  fs.mkdirSync('/tmp/claude-0', { recursive: true });
  await page.pdf({ path: '/tmp/claude-0/p34.pdf', format: 'A4', printBackground: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  // report which page each part starts on
  await browser.close();
  console.log('wrote /tmp/claude-0/p34.pdf');
})();
