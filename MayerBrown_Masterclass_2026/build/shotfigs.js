const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1.6});
 await p.goto('file://'+process.argv[2]); await p.evaluate(()=>document.fonts.ready);
 const ids=process.argv.slice(4);
 for(const id of ids){ const el=await p.$('#fig-'+id); if(el) await el.screenshot({path:process.argv[3]+'/'+id+'.png'}); }
 await b.close();})();
