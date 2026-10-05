// Preview Parts 9 and 10 only: node preview_p910.js
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const ROOT = __dirname;
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const body = ['09_interview.html', '10_interviewers.html']
  .map(f => fs.readFileSync(path.join(ROOT, 'parts', f), 'utf8')).join('\n');
const html = `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${body}</body></html>`;
const OUT = '/tmp/claude-0/p910.pdf';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  // report pages where each part / figure starts is not available from Chromium; report figure boxes instead
  await page.pdf({ path: OUT, format: 'A4', printBackground: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await browser.close();
  execSync(`rm -f /tmp/claude-0/p910-*.png && pdftoppm -r 60 -png ${OUT} /tmp/claude-0/p910`);
  console.log(execSync(`pdfinfo ${OUT} | grep Pages`).toString());
})();
