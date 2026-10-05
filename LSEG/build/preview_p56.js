// Quick preview of Parts 5 and 6 only. Usage: node preview_p56.js
const fs = require('fs');
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const body = ['05_industry.html', '06_role_industry.html'].map(f => fs.readFileSync(path.join(ROOT, 'parts', f), 'utf8')).join('\n');
const html = `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync('/tmp/claude-0', { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: '/tmp/claude-0/p56.pdf', format: 'A4', printBackground: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await browser.close();
  console.log('ok');
})();
