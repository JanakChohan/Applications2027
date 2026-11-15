(function(){
'use strict';
document.documentElement.classList.add('js');
var DATA=JSON.parse(document.getElementById('data').textContent);
var $=function(s,r){return (r||document).querySelector(s)};
var $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var VIEWS=['home','role','relationships','sales','teams','facts','practise','library','search'];
var reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function toast(msg){var t=document.createElement('div');t.className='toast';t.setAttribute('role','status');t.textContent=msg;document.body.appendChild(t);setTimeout(function(){t.remove()},2400)}

/* ---------- fee model (mirror of build/calc.py) ---------- */
var CDEF={currency:'£',size:500000000,funded_pct_initial:100,remaining_funded_month:null,annual_return_pct:0,flow_amount:0,flow_month:null,monthly_flow:0,monthly_flow_start:null,fee_mode:'flat',fee_bps:20,tiers:[],fee_change_month:null,new_fee_bps:null,months:12,fee_base:'market_value'};
function annualFee(base,p,month){
  if(p.fee_mode==='tiered'&&p.tiers&&p.tiers.length){var fee=0,lower=0;for(var i=0;i<p.tiers.length;i++){var t=p.tiers[i];var upper=(t.upto==null)?Infinity:t.upto;var slice=Math.max(0,Math.min(base,upper)-lower);fee+=slice*t.bps/10000;lower=upper;if(base<=upper)break}return fee}
  var bps=p.fee_bps;if(p.fee_change_month&&p.new_fee_bps!=null&&month>=p.fee_change_month)bps=p.new_fee_bps;return base*bps/10000}
function feeModel(params){
  var p={},k;for(k in CDEF)p[k]=CDEF[k];for(k in params)if(k in CDEF)p[k]=params[k];
  var months=Math.max(1,Math.floor(p.months)),rm=Math.pow(1+p.annual_return_pct/100,1/12)-1,bal=0,rows=[];
  for(var m=1;m<=months;m++){var flow=0;
    if(m===1)flow+=p.size*p.funded_pct_initial/100;
    if(p.remaining_funded_month&&m===p.remaining_funded_month)flow+=p.size*(100-p.funded_pct_initial)/100;
    if(p.flow_month&&m===p.flow_month)flow+=p.flow_amount;
    if(p.monthly_flow&&p.monthly_flow_start&&m>=p.monthly_flow_start)flow+=p.monthly_flow;
    bal=Math.max(0,bal+flow);var base=p.fee_base==='committed'?p.size:bal;var fee=annualFee(base,p,m)/12;
    var row={month:m,flow:flow,start_balance:bal,fee_base:base,fee:fee};bal=bal*(1+rm);row.end_balance=bal;rows.push(row)}
  var years=[],total=0;
  for(var y=0;y<Math.ceil(months/12);y++){var ch=rows.slice(y*12,(y+1)*12),avg=0,fees=0;ch.forEach(function(r){avg+=r.fee_base;fees+=r.fee});avg/=ch.length;
    years.push({year:y+1,months:ch.length,avg_fee_base:avg,fees:fees,effective_bps_annualised:avg?fees/avg*10000*12/ch.length:null,end_balance:ch[ch.length-1].end_balance})}
  rows.forEach(function(r){total+=r.fee});
  return {params:p,rows:rows,years:years,total_fees:total}}
function trimNum(x,d){return x.toLocaleString('en-GB',{minimumFractionDigits:0,maximumFractionDigits:d})}
function money(x,cur){if(x==null)return 'n/a';cur=cur||'£';var neg=x<0;x=Math.abs(x);var s;
  if(x>=1e9)s=trimNum(x/1e9,3)+'bn';else if(x>=1e6)s=trimNum(x/1e6,3)+'m';else if(x>=1e3)s=trimNum(x/1e3,1)+'k';else s=trimNum(x,0);return (neg?'-':'')+cur+s}
window.__feeModel=feeModel;window.__cases=DATA.cases;

/* ---------- views, tabs, chapters ---------- */
var chapters=$$('#chapters .chapter'),curCh=0,glossDone={};
function showView(name){
  VIEWS.forEach(function(v){var el=$('#view-'+v);if(el)el.hidden=(v!==name)});
  $$('nav.main a').forEach(function(a){if(a.getAttribute('href')==='#/'+name)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  var g=$('#view-'+name+' .guide-page');if(g)linkGlossary(g)}
function showPane(tab,pane){var found=false;
  $$('[data-tab="'+tab+'"]').forEach(function(b){var on=b.dataset.pane===pane;if(on)found=true;b.setAttribute('aria-pressed',on?'true':'false');var p=$('#'+tab+'-'+b.dataset.pane);if(p)p.hidden=!on});
  if(!found){var first=$('[data-tab="'+tab+'"]');if(first)showPane(tab,first.dataset.pane)}}
function showChapter(id,sec){
  var idx=0;chapters.forEach(function(c,i){if(c.dataset.chapter===id)idx=i});curCh=idx;
  chapters.forEach(function(c,i){c.hidden=(i!==idx)});
  $$('#chapterNav > li').forEach(function(li,i){li.classList.toggle('current',i===idx)});
  $('#prevCh').disabled=idx===0;$('#nextCh').disabled=idx===chapters.length-1;
  linkGlossary(chapters[idx]);
  var t=sec?document.getElementById(sec):null;if(t)t.scrollIntoView({block:'start'});else window.scrollTo(0,0)}
/* make any element visible: its page, its tab, its chapter, its filter state; then scroll to it */
function reveal(el){
  var v=el.closest('.view');if(!v)return false;showView(v.id.replace('view-',''));
  var p=el.closest('.pane');if(p){var bits=p.id.split('-');showPane(bits[0],bits.slice(1).join('-'))}
  var ch=el.closest('#chapters .chapter');if(ch)showChapter(ch.dataset.chapter);
  var tc=el.closest('.team-card');if(tc)selectTeam('');
  var holder=el.closest('[data-filtered]');if(holder)holder.removeAttribute('data-filtered');
  for(var d=el;d;d=d.parentElement){if(d.tagName==='DETAILS')d.open=true}
  el.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});
  if(el.matches('.card,tr,details')){el.setAttribute('tabindex','-1');el.focus({preventScroll:true})}
  return true}
var firstRoute=true;
function route(){
  var initial=firstRoute;firstRoute=false;
  var h=location.hash||'#/';
  if(h.indexOf('#/')!==0){var el=document.getElementById(decodeURIComponent(h.slice(1)));if(el)reveal(el);return}
  var parts=h.slice(2).split('/').map(decodeURIComponent),name=parts[0]||'home';if(VIEWS.indexOf(name)<0)name='home';
  showView(name);
  if(name==='search'){runSearch(parts.slice(1).join('/'));return}
  if(name==='teams'){selectTeam(parts[1]||'');if(!parts[1])window.scrollTo(0,0);return}
  if(name==='facts'||name==='practise'||name==='library'){
    showPane(name,parts[1]||'');
    if(name==='library'&&(parts[1]||'chapters')==='chapters'){showChapter(parts[2]||(chapters[0]&&chapters[0].dataset.chapter),parts[3]);return}
    if(parts[2]){var t=document.getElementById(parts[2]);if(t){reveal(t);return}}}
  window.scrollTo(0,0);
  if(!initial)$('#main').focus({preventScroll:true})}
window.addEventListener('hashchange',route);
$$('[data-tab]').forEach(function(b){b.addEventListener('click',function(){location.hash='#/'+b.dataset.tab+'/'+b.dataset.pane})});
$('#prevCh').addEventListener('click',function(){if(curCh>0)location.hash='#/library/chapters/'+chapters[curCh-1].dataset.chapter});
$('#nextCh').addEventListener('click',function(){if(curCh<chapters.length-1)location.hash='#/library/chapters/'+chapters[curCh+1].dataset.chapter});
$$('#chapterNav a').forEach(function(a){var m=a.getAttribute('href').match(/^#\/read\/(.*)$/);if(m)a.setAttribute('href','#/library/chapters/'+m[1])});
$$('[data-level]').forEach(function(b){b.addEventListener('click',function(){document.body.classList.remove('view-l1','view-l2','view-both');document.body.classList.add('view-'+b.dataset.level);
  $$('[data-level]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')})})});

/* ---------- glossary: quiet dotted terms with a definition on click ---------- */
var G=DATA.glossary.filter(function(g){return g.term&&g.term.length>1}),gByKey={};
G.forEach(function(g){gByKey[g.term.toLowerCase()]=g});
var gRe=null;
function buildGRe(){var terms=G.map(function(g){return g.term}).sort(function(a,b){return b.length-a.length}).map(function(t){return t.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&')});
  if(!terms.length)return null;return new RegExp('(^|[^A-Za-z0-9])('+terms.join('|')+')(?![A-Za-z0-9])','g')}
function linkGlossary(ch){if(!ch||glossDone[ch.id]||!G.length)return;glossDone[ch.id]=true;if(!gRe)gRe=buildGRe();if(!gRe)return;
  var secs=$$('.sec',ch);if(!secs.length)secs=[ch];
  secs.forEach(function(sec){var seen={},w=document.createTreeWalker(sec,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentElement;
      if(!p||p.closest('h1,h2,h3,h4,a,button,code,pre,summary,svg,strong,.badge,.layer,.cite,.box-title,th,caption,figcaption'))return NodeFilter.FILTER_REJECT;return n.nodeValue.length>2?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT}}),nodes=[],n;
    while((n=w.nextNode()))nodes.push(n);
    nodes.forEach(function(node){var text=node.nodeValue,m,last=0,frag=null;gRe.lastIndex=0;
      while((m=gRe.exec(text))){var term=m[2],key=term.toLowerCase(),g=gByKey[key];
        if(!g||seen[key]||(g.term===g.term.toUpperCase()&&term!==g.term)){gRe.lastIndex=m.index+m[0].length;continue}
        seen[key]=1;frag=frag||document.createDocumentFragment();var start=m.index+m[1].length;
        frag.appendChild(document.createTextNode(text.slice(last,start)));
        var b=document.createElement('button');b.type='button';b.className='g';b.dataset.g=g.id;b.textContent=term;b.setAttribute('aria-label',term+': show definition');frag.appendChild(b);last=start+term.length}
      if(frag){frag.appendChild(document.createTextNode(text.slice(last)));node.parentNode.replaceChild(frag,node)}})})}
var pop=$('#pop'),popFrom=null;
function closePop(){if(!pop.hidden){pop.hidden=true;if(popFrom)popFrom.focus();popFrom=null}}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button.g');
  if(b){var g=G.filter(function(x){return x.id===b.dataset.g})[0];if(!g)return;popFrom=b;
    pop.innerHTML='<strong>'+esc(g.term)+'</strong>'+(g.expansion&&g.expansion!==g.term?' · '+esc(g.expansion):'')+'<p>'+esc(g.plain||'')+'</p><p><button type="button" id="popClose">Close</button></p>';
    pop.hidden=false;var r=b.getBoundingClientRect();pop.style.top=(window.scrollY+r.bottom+6)+'px';pop.style.left=Math.max(8,Math.min(window.scrollX+r.left,window.scrollX+document.documentElement.clientWidth-360))+'px';
    $('#popClose').focus();e.stopPropagation();return}
  if(e.target.id==='popClose'){closePop();return}
  if(!pop.hidden&&!pop.contains(e.target)){pop.hidden=true;popFrom=null}});
document.addEventListener('keydown',function(e){
  if(e.key==='Escape')closePop();
  if(e.key==='/'&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();$('#q').focus()}});
$('#gq').addEventListener('input',function(){var q=this.value.trim().toLowerCase(),n=0;$$('#glossList .gloss').forEach(function(c){var hit=!q||c.textContent.toLowerCase().indexOf(q)>=0;if(hit){c.removeAttribute('data-filtered');n++}else c.setAttribute('data-filtered','out')});
  $('#gCount').textContent=n+' terms'});
$('#gCount').textContent=$$('#glossList .gloss').length+' terms';

/* ---------- search ---------- */
var index=null;
var KIND={chapter:'Guide',glossary:'Glossary',source:'Source',claim:'Checked claim','claim-audit':'Former intern\'s account',interview:'Interview question','practice-case':'Case','fee-case':'Fee example',coverage:'Research coverage',intel:'Key finding',number:'Number',chart:'Chart',stage:'Step'};
function kindLabel(k){if(KIND[k])return KIND[k];if(/team/.test(k))return 'Team';if(/person/.test(k))return 'Person';if(/mandate/.test(k))return 'Mandate';if(/dev/.test(k))return 'Market change';if(/comp/.test(k))return 'Competitor';if(/role/.test(k))return 'Role';if(/gloss/.test(k))return 'Glossary';return 'Item'}
function buildIndex(){index=[];$$('[data-search]').forEach(function(el){if(!el.closest('.view'))return;
  var t=$('h2,h3,h4,.card-title,summary,.num-label',el),title=t?t.textContent.trim():(el.cells?el.cells[0].textContent.trim().slice(0,90):''),href='';
  if(el.dataset.kind==='chapter'){var ch=el.closest('.chapter');href='#'+el.dataset.sec;title=($('h1',ch)?$('h1',ch).textContent+' › ':'')+title}
  else if(el.id){href='#'+el.id;if(el.id.indexOf('src-')===0)title=el.cells[1].textContent.trim().slice(0,110)}
  else{var v=el.closest('.view').id.replace('view-',''),p=el.closest('.pane');href='#/'+v+(p?'/'+p.id.split('-').slice(1).join('-'):'')}
  var text=el.textContent.replace(/\s+/g,' ');index.push({kind:el.dataset.kind||'',title:title,text:text,low:text.toLowerCase(),tlow:title.toLowerCase(),href:href})})}
function runSearch(q){if(!index)buildIndex();q=(q||'').trim();if($('#q').value!==q)$('#q').value=q;var out=$('#searchResults');out.innerHTML='';
  var toks=q.toLowerCase().split(/\s+/).filter(Boolean);if(!toks.length){$('#searchSummary').textContent='Type in the search box.';return}
  var hits=[];index.forEach(function(it){var score=0;for(var i=0;i<toks.length;i++){var t=toks[i],c=it.low.split(t).length-1;if(!c)return;score+=Math.min(c,8)+(it.tlow.indexOf(t)>=0?12:0)}
    if(it.kind==='chapter')score+=4;if(it.kind==='glossary'&&it.tlow.indexOf(toks[0])===0)score+=20;hits.push({it:it,score:score})});
  hits.sort(function(a,b){return b.score-a.score});
  $('#searchSummary').textContent=hits.length+' result'+(hits.length===1?'':'s')+' for "'+q+'"'+(hits.length>60?' (showing the first 60)':'');
  hits.slice(0,60).forEach(function(h){var it=h.it,pos=it.low.indexOf(toks[0]),s=Math.max(0,pos-70),snip=esc(it.text.slice(s,s+220));
    toks.forEach(function(t){snip=snip.replace(new RegExp('('+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>')});
    var li=document.createElement('li');li.innerHTML='<a href="'+esc(it.href)+'"><strong>'+esc(it.title||'(untitled)')+'</strong></a> <span class="muted">· '+esc(kindLabel(it.kind))+'</span><div class="muted">'+(s>0?'… ':'')+snip+' …</div>';out.appendChild(li)})}
var qTimer;$('#q').addEventListener('input',function(){var v=this.value;clearTimeout(qTimer);qTimer=setTimeout(function(){if(v.trim().length>1){var nh='#/search/'+encodeURIComponent(v.trim());if(location.hash.indexOf('#/search')===0){history.replaceState(null,'',nh);route()}else location.hash=nh}},220)});
$('#q').addEventListener('keydown',function(e){if(e.key==='Enter'){clearTimeout(qTimer);location.hash='#/search/'+encodeURIComponent(this.value.trim())}});

/* ---------- filters built from the data ---------- */
$$('.filters[data-filter-for]').forEach(function(bar){var list=document.getElementById(bar.dataset.filterFor);if(!list)return;
  var rowsSel=bar.dataset.filterRows,items=rowsSel?$$(rowsSel,list):$$(':scope > .card',list),keys=bar.dataset.filterKeys.split(','),sels=[];
  var count=document.createElement('span');count.className='count';count.setAttribute('role','status');
  keys.forEach(function(k){var vals={};items.forEach(function(it){(it.getAttribute('data-'+k)||'').split('|').forEach(function(v){v=v.trim();if(v)vals[v]=(vals[v]||0)+1})});
    var names=Object.keys(vals).sort();if(names.length<2)return;var lab=document.createElement('label'),sel=document.createElement('select');
    lab.textContent=k.replace(/-/g,' ').replace(/^./,function(c){return c.toUpperCase()})+' ';sel.dataset.key=k;sel.innerHTML='<option value="">All</option>'+names.map(function(n){return '<option value="'+esc(n)+'">'+esc(n)+' ('+vals[n]+')</option>'}).join('');
    lab.appendChild(sel);bar.appendChild(lab);sels.push(sel);sel.addEventListener('change',apply)});
  var reset=document.createElement('button');reset.type='button';reset.textContent='Clear';reset.addEventListener('click',function(){sels.forEach(function(s){s.value=''});apply()});
  if(sels.length)bar.appendChild(reset);bar.appendChild(count);
  function apply(){var n=0;items.forEach(function(it){var ok=sels.every(function(s){if(!s.value)return true;return (it.getAttribute('data-'+s.dataset.key)||'').split('|').map(function(x){return x.trim()}).indexOf(s.value)>=0});
    if(ok){it.removeAttribute('data-filtered');n++}else it.setAttribute('data-filtered','out')});count.textContent=n+' of '+items.length}
  apply()});

/* ---------- teams ---------- */
var teamSel=$('#teamSel');DATA.teams.forEach(function(t){var o=document.createElement('option');o.value=t.id;o.textContent=t.name;teamSel.appendChild(o)});
function selectTeam(id){teamSel.value=id||'';var found=null;$$('#teamPanel .team-card').forEach(function(c){var show=!id||c.id===id;c.hidden=!show;if(show&&id)found=c});
  if(found){found.scrollIntoView({block:'start'});found.setAttribute('tabindex','-1');found.focus({preventScroll:true})}}
teamSel.addEventListener('change',function(){location.hash='#/teams'+(this.value?'/'+this.value:'')});
$$('a.teamlink').forEach(function(a){a.setAttribute('href','#/teams/'+a.dataset.team)});

/* ---------- numbers ---------- */
$('#testMe').addEventListener('click',function(){var on=$('#numWall').classList.toggle('testme');this.setAttribute('aria-pressed',on?'true':'false');this.textContent=on?'Show the values':'Hide the values and test me';if(on)$$('#numWall details').forEach(function(d){d.open=false})});

/* ---------- calculator ---------- */
var num=function(id){var v=$('#'+id).value;return v===''?null:Number(v)};
function readCalc(){var p={size:num('c_size')||0,funded_pct_initial:num('c_funded')==null?100:num('c_funded'),remaining_funded_month:num('c_remmonth'),annual_return_pct:num('c_ret')||0,months:Math.min(120,Math.max(1,num('c_months')||12)),
  flow_amount:num('c_flow')||0,flow_month:num('c_flowmonth'),monthly_flow:num('c_mflow')||0,monthly_flow_start:num('c_mflowstart'),fee_base:$('#c_base').value,fee_mode:$('#c_mode').value,fee_bps:num('c_bps')||0,fee_change_month:num('c_chgmonth'),new_fee_bps:num('c_newbps'),tiers:[]};
  if(p.fee_mode==='tiered'){[['t1u','t1b'],['t2u','t2b'],['t3u','t3b']].forEach(function(t){var b=num(t[1]);if(b!=null)p.tiers.push({upto:num(t[0]),bps:b})});
    for(var i=0;i<p.tiers.length;i++)if(p.tiers[i].upto==null){p.tiers=p.tiers.slice(0,i+1);break}}
  return p}
function writeCalc(p){var q={},k;for(k in CDEF)q[k]=CDEF[k];for(k in p)q[k]=p[k];var set=function(id,v){$('#'+id).value=(v==null?'':v)};
  set('c_size',q.size);set('c_funded',q.funded_pct_initial);set('c_remmonth',q.remaining_funded_month);set('c_ret',q.annual_return_pct);set('c_months',q.months);set('c_flow',q.flow_amount);set('c_flowmonth',q.flow_month);set('c_mflow',q.monthly_flow);set('c_mflowstart',q.monthly_flow_start);
  $('#c_base').value=q.fee_base;$('#c_mode').value=q.fee_mode;set('c_bps',q.fee_bps);set('c_chgmonth',q.fee_change_month);set('c_newbps',q.new_fee_bps);
  var t=q.tiers||[];[['t1u','t1b'],['t2u','t2b'],['t3u','t3b']].forEach(function(ids,i){set(ids[0],t[i]?t[i].upto:null);set(ids[1],t[i]?t[i].bps:null)})}
function runCalc(){var p=readCalc(),r=feeModel(p);$('#tierBox').hidden=p.fee_mode!=='tiered';$('#calcTotal').textContent=money(r.total_fees);
  var y1=r.years[0],f='';
  if(p.fee_mode==='flat'){f+='Fee for a month = fee base × rate ÷ 12\nRate = '+p.fee_bps+'bp = '+(p.fee_bps/100).toFixed(4).replace(/0+$/,'').replace(/\.$/,'')+'% a year'+(p.fee_change_month&&p.new_fee_bps!=null?' (then '+p.new_fee_bps+'bp from month '+p.fee_change_month+')':'')+'\n'}
  else{f+='Yearly fee = each slice of the fee base × its own rate\n'+p.tiers.map(function(t,i){return '  Tier '+(i+1)+': '+(t.upto==null?'everything above':'up to '+money(t.upto))+' at '+t.bps+'bp'}).join('\n')+'\n'}
  f+='Fee base = '+(p.fee_base==='committed'?'committed capital of '+money(p.size):'value of the assets each month')+'\n';
  f+='Year 1: average fee base '+money(y1.avg_fee_base)+' → fee '+money(y1.fees)+(y1.effective_bps_annualised==null?'':' ('+y1.effective_bps_annualised.toFixed(1)+'bp a year)');
  $('#calcFormula').textContent=f;
  $('#calcYears tbody').innerHTML=r.years.map(function(y){return '<tr><td>Year '+y.year+(y.months===12?'':' ('+y.months+' months)')+'</td><td>'+money(y.avg_fee_base)+'</td><td>'+money(y.fees)+'</td><td>'+(y.effective_bps_annualised==null?'n/a (no fee-bearing assets)':y.effective_bps_annualised.toFixed(1)+'bp')+'</td><td>'+money(y.end_balance)+'</td></tr>'}).join('');
  $('#calcMonths tbody').innerHTML=r.rows.map(function(m){return '<tr><td>'+m.month+'</td><td>'+(m.flow?money(m.flow):'none')+'</td><td>'+money(m.start_balance)+'</td><td>'+money(m.fee_base)+'</td><td>'+money(m.fee)+'</td><td>'+money(m.end_balance)+'</td></tr>'}).join('');
  return r}
var caseSel=$('#caseSel'),lastGroup='',og=null;DATA.cases.forEach(function(c){if(c.group!==lastGroup){og=document.createElement('optgroup');og.label=c.group;caseSel.appendChild(og);lastGroup=c.group}var o=document.createElement('option');o.value=c.id;o.textContent=c.title;og.appendChild(o)});
caseSel.addEventListener('change',function(){var c=DATA.cases.filter(function(x){return x.id===caseSel.value})[0];if(c){writeCalc(c.params);$('#caseTeach').textContent=c.teaches}else $('#caseTeach').textContent='';runCalc()});
$$('#calcForm input,#calcForm select').forEach(function(i){i.addEventListener('input',function(){if(caseSel.value){caseSel.value='';$('#caseTeach').textContent=''}runCalc()})});
runCalc();

/* ---------- timed practice (silent timer, nothing recorded, nothing saved) ---------- */
var QS=$$('#qList .iq').map(function(c){return {id:c.id,cat:c.dataset.category,q:$('.card-title',c).textContent,el:c}}),used=[],curQ=null,tStart=0,tInt=null,elapsed=0;
var CRIT=(DATA.criteria&&DATA.criteria.length)?DATA.criteria.map(function(c){return c.name}):['Accuracy','Specificity','Logic','Judgement','Clarity','Supported personal evidence'];
(function(){var cats={};QS.forEach(function(q){cats[q.cat]=1});Object.keys(cats).sort().forEach(function(c){var o=document.createElement('option');o.value=c;o.textContent=c;$('#pCat').appendChild(o)});
  $('#pScores').innerHTML=CRIT.map(function(c,i){return '<label>'+esc(c)+' <select data-crit="'+i+'" aria-label="'+esc(c)+' score"><option value="">–</option><option>0</option><option>1</option><option>2</option><option>3</option></select></label>'}).join('')})();
function fmt(s){return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2)}
function stopTimer(){if(tInt){clearInterval(tInt);tInt=null}}
$('#pNext').addEventListener('click',function(){var cat=$('#pCat').value,pool=QS.filter(function(q){return (!cat||q.cat===cat)&&used.indexOf(q.id)<0});
  if(!pool.length){used=[];pool=QS.filter(function(q){return !cat||q.cat===cat})}if(!pool.length){toast('No questions in this set.');return}
  curQ=pool[Math.floor(Math.random()*pool.length)];used.push(curQ.id);stopTimer();elapsed=0;$('#pTimer').textContent='0:00';$('#pTimeMsg').textContent='';
  $('#pCard').hidden=false;$('#pMeta').textContent=curQ.cat;$('#pQ').textContent=curQ.q;$('#pAnswer').hidden=true;$('#pAnswer').innerHTML='';$$('#pScores select').forEach(function(s){s.value=''});$('#pQ').focus()});
$('#pStart').addEventListener('click',function(){stopTimer();var target=Number($('#pLen').value);tStart=Date.now()-elapsed*1000;$('#pTimeMsg').textContent='Target '+fmt(target);
  tInt=setInterval(function(){elapsed=Math.floor((Date.now()-tStart)/1000);$('#pTimer').textContent=fmt(elapsed);if(elapsed===target)$('#pTimeMsg').textContent='Time. Finish your sentence.';if(elapsed>=target+60){stopTimer();$('#pTimeMsg').textContent='Stopped.'}},250)});
$('#pStop').addEventListener('click',function(){stopTimer();$('#pTimeMsg').textContent='Stopped at '+fmt(elapsed)});
$('#pReveal').addEventListener('click',function(){if(!curQ)return;var box=$('#pAnswer');box.innerHTML='';$$(':scope > details',curQ.el).forEach(function(d){var c=d.cloneNode(true);c.open=true;box.appendChild(c)});box.hidden=false});

/* ---------- quick quiz ---------- */
function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function srcLinks(ids){return (ids||[]).filter(function(i){return DATA.sources[i]}).map(function(i){return '<a class="cite" href="#src-'+esc(i)+'">'+esc(i)+'</a>'}).join(' ')}
var TOPIC={foundations:'Foundations',role:'The role',teams:'Teams',ocio:'OCIO',tpw:'Third Party Wealth',liquidity:'Liquidity',insurance:'Insurance',economics:'Fees and economics','sales-rm':'Sales and RM',relationship:'Relationships',awareness:'Market changes',competitors:'Competitors','people-process':'People and process',glossary:'Glossary'};
(function(){var t={};DATA.quiz.forEach(function(q){t[q.topic]=(t[q.topic]||0)+1});Object.keys(t).sort().forEach(function(k){var o=document.createElement('option');o.value=k;o.textContent=(TOPIC[k]||k)+' ('+t[k]+')';$('#zTopic').appendChild(o)})})();
var zSet=[],zI=0,zScore=0,zMiss={};
$('#zStart').addEventListener('click',function(){var tp=$('#zTopic').value,pool=DATA.quiz.filter(function(q){return !tp||q.topic===tp});
  if(!pool.length){toast('No questions match.');return}zSet=shuffle(pool).slice(0,Number($('#zLen').value));zI=0;zScore=0;zMiss={};$('#zEnd').hidden=true;$('#zPlay').hidden=false;zShow()});
function zShow(){var q=zSet[zI];$('#zProg').textContent='Question '+(zI+1)+' of '+zSet.length+' · '+(TOPIC[q.topic]||q.topic);$('#zScore').textContent=zScore;
  $('#zQ').textContent=q.q;$('#zFb').hidden=true;$('#zNext').hidden=true;var box=$('#zOpts');box.innerHTML='';
  q.options.forEach(function(o,i){var b=document.createElement('button');b.type='button';b.textContent=String.fromCharCode(65+i)+'. '+o;b.addEventListener('click',function(){zAnswer(i)});box.appendChild(b)});$('#zQ').focus()}
function zAnswer(i){var q=zSet[zI],ok=i===q.answer;$$('#zOpts button').forEach(function(b,k){b.disabled=true;if(k===q.answer){b.classList.add('right');b.textContent='✔ '+b.textContent}else if(k===i){b.classList.add('wrong');b.textContent='✘ '+b.textContent}});
  if(ok)zScore++;else zMiss[q.topic]=(zMiss[q.topic]||0)+1;$('#zScore').textContent=zScore;
  $('#zFb').innerHTML='<strong>'+(ok?'Correct.':'Not quite. The answer is '+String.fromCharCode(65+q.answer)+'.')+'</strong> '+esc(q.explain||'')+' '+srcLinks(q.sources);$('#zFb').hidden=false;
  var n=$('#zNext');n.hidden=false;n.textContent=zI===zSet.length-1?'See the result':'Next';n.focus()}
$('#zNext').addEventListener('click',function(){zI++;if(zI<zSet.length){zShow();return}
  $('#zPlay').hidden=true;var weak=Object.keys(zMiss).sort(function(a,b){return zMiss[b]-zMiss[a]}).slice(0,3);
  $('#zEnd').innerHTML='<p class="bignum">'+zScore+' / '+zSet.length+'</p>'+(weak.length?'<p>Worth another look: '+weak.map(function(w){return esc(TOPIC[w]||w)}).join(', ')+'.</p>':'<p>All correct.</p>')+'<p><button type="button" class="primary" id="zAgain">Again</button></p>';
  $('#zEnd').hidden=false;$('#zAgain').addEventListener('click',function(){$('#zStart').click()})});

route();
})();
