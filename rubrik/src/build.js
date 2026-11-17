// Renders guide.html to a dyslexic-friendly A4 PDF with a full-page cream background.
// Usage: node build.js   (needs playwright and python3 with pypdf)
const path = require('path');
const os = require('os');
const fs = require('fs');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

const BG = '#FBF4E4';

(async () => {
  const src = path.join(__dirname, 'guide.html');
  const out = path.join(__dirname, '..', 'Rubrik_Company_Guide.pdf');
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'guide-'));
  const body = path.join(tmp, 'body.pdf');
  const bg = path.join(tmp, 'bg.pdf');

  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src);
  await page.pdf({
    path: body,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate:
      '<div style="width:100%;font-family:DejaVu Sans,Verdana,Arial,sans-serif;font-size:8.5pt;color:#555;padding:0 17mm;display:flex;justify-content:space-between;">' +
      '<span>Rubrik: plain-English company guide</span>' +
      '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>',
  });
  // One blank cream page, laid underneath every page so the margins are cream too.
  await page.setContent(`<html><body style="margin:0;background:${BG}"><div style="height:296mm"></div></body></html>`);
  await page.pdf({ path: bg, format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
  await browser.close();

  execFileSync('python3', ['-c', `
import sys
from pypdf import PdfReader, PdfWriter
body, bg, out = sys.argv[1:4]
w = PdfWriter()
for pg in PdfReader(body).pages:
    base = w.add_page(PdfReader(bg).pages[0])
    base.merge_page(pg)
w.add_metadata({'/Title': 'Rubrik: a plain-English company guide'})
w.write(out)
`, body, bg, out], { stdio: 'inherit' });
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('Wrote ' + out);
})();
