// node preview_one.js parts/00_how_to_use.html out.pdf
const fs=require('fs');const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
const h=`<!doctype html><html><head><meta charset="utf-8"><style>${fs.readFileSync(__dirname+'/fonts/fonts_embed.css')}\n${fs.readFileSync(__dirname+'/style.css')}</style></head><body>${process.argv.slice(2,-1).map(f=>fs.readFileSync(f,'utf8')).join('\n')}</body></html>`;
await p.setContent(h);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:process.argv[process.argv.length-1],format:'A4',printBackground:true,margin:{top:'18mm',bottom:'18mm',left:'16mm',right:'16mm'}});await b.close();})();
