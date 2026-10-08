const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage();
 await p.goto('file://'+process.argv[2]); await p.evaluate(()=>document.fonts.ready);
 const res=await p.evaluate(()=>{
  const out=[];
  document.querySelectorAll('figure').forEach(f=>{
   const svg=f.querySelector('svg'); if(!svg) return;
   const vb=svg.viewBox.baseVal;
   svg.querySelectorAll('text').forEach(t=>{const bb=t.getBBox(); if(bb.x<vb.x-1||bb.y<vb.y-1||bb.x+bb.width>vb.x+vb.width+1||bb.y+bb.height>vb.y+vb.height+1) out.push(f.id+' VIEWBOX: '+t.textContent.slice(0,50));});
   svg.querySelectorAll('g.bx').forEach(g=>{const r=g.querySelector('rect').getBBox(); g.querySelectorAll('text').forEach(t=>{const bb=t.getBBox(); if(bb.x<r.x-1||bb.x+bb.width>r.x+r.width+1||bb.y<r.y-1||bb.y+bb.height>r.y+r.height+1) out.push(f.id+' BOX: '+t.textContent.slice(0,60)+` (${Math.round(bb.width)}>${Math.round(r.width)} / ${Math.round(bb.y+bb.height-r.y-r.height)})`);});});
  });
  return out;});
 console.log(res.join('\n')); console.log('issues',res.length); await b.close();})();
