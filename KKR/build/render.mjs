// Usage: node render.mjs <input.html> <output.pdf> <headerTitle> [cover]
// cover mode: zero margins, no header/footer.
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import path from 'node:path';

const [, , input, output, title = '', mode = ''] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);

const hdr = `<div style="width:100%;font-family:Inter,Arial;font-size:7px;color:#7A8294;padding:0 15mm;display:flex;justify-content:space-between;">
  <span>${title}</span><span>Built from public sources · not affiliated with KKR</span></div>`;
const ftr = `<div style="width:100%;font-family:Inter,Arial;font-size:7.5px;color:#7A8294;padding:0 15mm;display:flex;justify-content:space-between;">
  <span>Prepared October 2026 · verify figures before quoting</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`;

if (mode === 'cover') {
  await page.pdf({ path: output, format: 'A4', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
} else {
  await page.pdf({
    path: output, format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: hdr, footerTemplate: ftr,
    margin: { top: '18mm', bottom: '18mm', left: '15mm', right: '15mm' },
  });
}
await browser.close();
