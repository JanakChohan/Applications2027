# -*- coding: utf-8 -*-
import os, re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, Image, PageBreak, KeepTogether, CondPageBreak, Flowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

NAVY=colors.HexColor("#12305c"); TEAL=colors.HexColor("#1f7a8c"); GOLD=colors.HexColor("#c8992e")
RED=colors.HexColor("#a6383a"); GREY=colors.HexColor("#5b6472"); LGREY=colors.HexColor("#d8dce3")
PAPER=colors.HexColor("#ffffff"); INK=colors.HexColor("#1c2430")
BOXBG=colors.HexColor("#f4f6f9"); INFBG=colors.HexColor("#f2f7f8"); WARNBG=colors.HexColor("#fdf4f4")
KEYBG=colors.HexColor("#fbf6ea")

# fonts
LS="/usr/share/fonts/truetype/liberation/"
DV="/usr/share/fonts/truetype/dejavu/"
FB,FBd,FI="Helvetica","Helvetica-Bold","Helvetica-Oblique"
SANS,SANSB="Helvetica","Helvetica-Bold"
try:
    pdfmetrics.registerFont(TTFont("Ser",LS+"LiberationSerif-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Ser-B",LS+"LiberationSerif-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Ser-I",LS+"LiberationSerif-Italic.ttf"))
    pdfmetrics.registerFont(TTFont("Ser-BI",LS+"LiberationSerif-BoldItalic.ttf"))
    pdfmetrics.registerFontFamily("Ser",normal="Ser",bold="Ser-B",italic="Ser-I",boldItalic="Ser-BI")
    FB,FBd,FI="Ser","Ser-B","Ser-I"
except Exception as e: print("serif fail",e)
try:
    pdfmetrics.registerFont(TTFont("Sn",DV+"DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("Sn-B",DV+"DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFontFamily("Sn",normal="Sn",bold="Sn-B",italic="Sn",boldItalic="Sn-B")
    SANS,SANSB="Sn","Sn-B"
except Exception as e: print("sans fail",e)

S={}
S['body']=ParagraphStyle('body',fontName=FB,fontSize=9.6,leading=14.4,alignment=TA_JUSTIFY,
    textColor=INK,spaceAfter=6.5)
S['first']=ParagraphStyle('first',parent=S['body'],spaceAfter=6.5)
S['h1']=ParagraphStyle('h1',fontName=SANSB,fontSize=17,leading=21,textColor=NAVY,spaceBefore=0,spaceAfter=3)
S['h1sub']=ParagraphStyle('h1sub',fontName=SANS,fontSize=9.2,leading=13,textColor=GREY,spaceAfter=11)
S['h2']=ParagraphStyle('h2',fontName=SANSB,fontSize=12.2,leading=15.5,textColor=NAVY,spaceBefore=13,spaceAfter=5)
S['h3']=ParagraphStyle('h3',fontName=SANSB,fontSize=10.2,leading=13.4,textColor=TEAL,spaceBefore=9,spaceAfter=3.5)
S['h4']=ParagraphStyle('h4',fontName=FBd,fontSize=9.8,leading=13,textColor=INK,spaceBefore=7,spaceAfter=2.5)
S['bullet']=ParagraphStyle('bullet',parent=S['body'],leftIndent=13,bulletIndent=3,spaceAfter=3.2,alignment=TA_LEFT)
S['cap']=ParagraphStyle('cap',fontName=SANS,fontSize=7.8,leading=10.6,textColor=GREY,spaceBefore=3,spaceAfter=11,alignment=TA_LEFT)
S['tcap']=ParagraphStyle('tcap',fontName=SANSB,fontSize=8.6,leading=11.6,textColor=NAVY,spaceBefore=7,spaceAfter=4)
S['th']=ParagraphStyle('th',fontName=SANSB,fontSize=7.9,leading=10.2,textColor=colors.white)
S['td']=ParagraphStyle('td',fontName=SANS,fontSize=7.9,leading=10.2,textColor=INK)
S['tdb']=ParagraphStyle('tdb',fontName=SANSB,fontSize=7.9,leading=10.2,textColor=INK)
S['box']=ParagraphStyle('box',fontName=FB,fontSize=9.1,leading=13.4,textColor=INK,alignment=TA_LEFT)
S['boxh']=ParagraphStyle('boxh',fontName=SANSB,fontSize=8.4,leading=11,textColor=NAVY,spaceAfter=3)
S['src']=ParagraphStyle('src',fontName=SANS,fontSize=7.9,leading=11.2,textColor=INK,spaceAfter=4.5,leftIndent=12,firstLineIndent=-12)
S['gl']=ParagraphStyle('gl',parent=S['body'],fontSize=9.2,leading=13,spaceAfter=4.5,leftIndent=11,firstLineIndent=-11)
S['tocL1']=ParagraphStyle('tocL1',fontName=SANSB,fontSize=9.6,leading=15.5,textColor=NAVY,spaceBefore=6)
S['tocL2']=ParagraphStyle('tocL2',fontName=SANS,fontSize=9,leading=13.6,textColor=INK,leftIndent=13)

def esc(t):
    t=t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    t=t.replace("&lt;b&gt;","<b>").replace("&lt;/b&gt;","</b>")
    t=t.replace("&lt;i&gt;","<i>").replace("&lt;/i&gt;","</i>")
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'(?<![A-Za-z0-9])_(.+?)_(?![A-Za-z0-9])',r'<i>\1</i>',t)
    return t

class HR(Flowable):
    def __init__(self,w,c=LGREY,t=0.6): Flowable.__init__(self); self.w=w; self.c=c; self.t=t
    def wrap(self,aw,ah): self.w=aw; return (aw,self.t+4)
    def draw(self):
        self.canv.setStrokeColor(self.c); self.canv.setLineWidth(self.t)
        self.canv.line(0,2,self.w,2)

class Doc(BaseDocTemplate):
    def __init__(self,fn,**kw):
        BaseDocTemplate.__init__(self,fn,**kw)
        self.toc=[]; self.secmap={}
        fw=A4[0]-2*20*mm
        self.addPageTemplates([
          PageTemplate(id='title',frames=[Frame(20*mm,20*mm,fw,A4[1]-40*mm,id='t')],onPage=self._blank),
          PageTemplate(id='front',frames=[Frame(20*mm,22*mm,fw,A4[1]-42*mm,id='f')],onPage=self._front),
          PageTemplate(id='body',frames=[Frame(20*mm,22*mm,fw,A4[1]-42*mm,id='b')],onPage=self._body),
        ])
    def _blank(self,c,d): pass
    def _front(self,c,d):
        c.saveState(); c.setFont(SANS,8); c.setFillColor(GREY)
        c.drawCentredString(A4[0]/2,13*mm,{1:'i',2:'ii',3:'iii',4:'iv'}.get(d.page-1,str(d.page-1)))
        c.restoreState()
    def _body(self,c,d):
        c.saveState()
        c.setStrokeColor(LGREY); c.setLineWidth(.5)
        c.line(20*mm,A4[1]-17*mm,A4[0]-20*mm,A4[1]-17*mm)
        c.setFont(SANS,7.4); c.setFillColor(GREY)
        c.drawString(20*mm,A4[1]-14.6*mm,"PIMCO — Business Model and London Summer Internship Roles")
        c.drawRightString(A4[0]-20*mm,A4[1]-14.6*mm,"Research conducted 31 August 2026")
        c.line(20*mm,15.5*mm,A4[0]-20*mm,15.5*mm)
        c.setFont(SANSB,8.4); c.setFillColor(NAVY)
        c.drawCentredString(A4[0]/2,10.6*mm,str(self.pageno))
        c.restoreState()
    @property
    def pageno(self): return self.page - self.offset if hasattr(self,'offset') else self.page
    def afterFlowable(self,f):
        if hasattr(f,'_tocentry'):
            lvl,txt=f._tocentry
            self.toc.append((lvl,txt,self.pageno))

def H(text,lvl,doc_toc=True,style=None,sub=None):
    st=S['h1'] if lvl==0 else S['h2']
    p=Paragraph(esc(text),style or st)
    if doc_toc: p._tocentry=(lvl,text)
    return p

def build(content_blocks, outfile, toc_entries=None, pass2=False):
    doc=Doc(outfile,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=20*mm,bottomMargin=22*mm,
            title="PIMCO — Business Model and London Summer Internship Roles",
            author="Deep research report", subject="PIMCO deep dive")
    doc.offset=0
    story=[]
    story+=title_page()
    story.append(PageBreak())
    story.append(_setnext('front'))
    story+=toc_flowables(toc_entries)
    story.append(PageBreak())
    story.append(_setnext('body'))
    story+=content_blocks
    doc.offset=None
    # compute offset: pages before body start
    class D2(Doc):
        pass
    doc.multiBuild(story)
    return doc.toc

def _setnext(tid):
    from reportlab.platypus.doctemplate import NextPageTemplate
    return NextPageTemplate(tid)

def title_page():
    W=A4[0]-40*mm
    out=[Spacer(1,26*mm)]
    out.append(HR(W,NAVY,2.2)); out.append(Spacer(1,7*mm))
    out.append(Paragraph("PIMCO",ParagraphStyle('t1',fontName=SANSB,fontSize=44,leading=48,textColor=NAVY)))
    out.append(Spacer(1,3*mm))
    out.append(Paragraph("How the firm makes money,<br/>and which London summer internship to apply for",
        ParagraphStyle('t2',fontName=SANS,fontSize=16.5,leading=22,textColor=TEAL)))
    out.append(Spacer(1,6*mm)); out.append(HR(W,LGREY,1)); out.append(Spacer(1,6*mm))
    out.append(Paragraph("A deep-dive research report written for a reader with no prior background in asset management. "
        "Every technical term is defined in plain English at first use. Facts are separated from inference throughout, "
        "and every assumption is registered in Section 15.",
        ParagraphStyle('t3',fontName=FB,fontSize=10.6,leading=16,textColor=INK)))
    out.append(Spacer(1,14*mm))
    rows=[["Research conducted","31 August 2026"],
          ["Most recent PIMCO firm data","30 June 2026 (PIMCO at a Glance)"],
          ["Most recent Allianz segment data","H1 2026, released 7 August 2026"],
          ["Careers data","PIMCO Workday requisitions, read 31 August 2026"],
          ["London roles found open","4 (all posted 31 August 2026)"],
          ["Primary sources used","PIMCO factsheets and website, PIMCO Form ADV Part 2A,<br/>Allianz earnings releases, UK Companies House, PIMCO's<br/>Workday careers API, SEC filings"]]
    t=Table([[Paragraph(f"<b>{a}</b>",ParagraphStyle('k',fontName=SANSB,fontSize=8.6,leading=11.6,textColor=NAVY)),
              Paragraph(b,ParagraphStyle('v',fontName=SANS,fontSize=8.6,leading=11.6,textColor=INK))] for a,b in rows],
             colWidths=[54*mm,W-54*mm])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),3.4),
        ('BOTTOMPADDING',(0,0),(-1,-1),3.4),('LEFTPADDING',(0,0),(-1,-1),0),
        ('LINEBELOW',(0,0),(-1,-2),0.4,LGREY)]))
    out.append(t)
    out.append(Spacer(1,16*mm))
    out.append(HR(W,LGREY,1)); out.append(Spacer(1,3*mm))
    out.append(Paragraph("A note on honesty. Where a figure could not be found, this report says <b>“not found”</b> and tells you where to look. "
        "Where sources conflict, both numbers are shown with a judgement on which to trust. Nothing here — no job title, no deadline, "
        "no fee rate, no name — has been invented to fill a gap.",
        ParagraphStyle('t4',fontName=FI,fontSize=9,leading=13.4,textColor=GREY)))
    return out

def toc_flowables(entries):
    W=A4[0]-40*mm
    out=[Paragraph("Contents",S['h1']),HR(W,NAVY,1.4),Spacer(1,5*mm)]
    if not entries: 
        out.append(Paragraph("(generating…)",S['body'])); return out
    data=[]
    for lvl,txt,pg in entries:
        st=S['tocL1'] if lvl==0 else S['tocL2']
        data.append([Paragraph(esc(txt),st),
                     Paragraph(f"<font size=8.6>{pg}</font>",ParagraphStyle('pg',fontName=SANSB if lvl==0 else SANS,
                        fontSize=9,leading=15.5 if lvl==0 else 13.6,textColor=NAVY if lvl==0 else INK,alignment=2))])
    t=Table(data,colWidths=[W-16*mm,16*mm])
    st=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]
    for i,(lvl,_,_) in enumerate(entries):
        if lvl==0: st.append(('LINEBELOW',(0,i),(-1,i),0.35,LGREY))
    t.setStyle(TableStyle(st))
    out.append(t)
    return out

FIGDIR="figs/"
CW=A4[0]-40*mm

def _tbl(caption,widths,rows,fontsize=7.9):
    ws=[float(x) for x in widths.split(",")]
    tot=sum(ws); cols=[CW*w/tot for w in ws]
    data=[]
    for ri,r in enumerate(rows):
        cells=r.split(";;")
        line=[]
        for c in cells:
            c=c.strip()
            if ri==0: line.append(Paragraph(esc(c),S['th']))
            else:
                stl=S['tdb'] if c.startswith("**") and c.endswith("**") else S['td']
                line.append(Paragraph(esc(c),stl))
        while len(line)<len(cols): line.append(Paragraph("",S['td']))
        data.append(line[:len(cols)])
    t=Table(data,colWidths=cols,repeatRows=1)
    st=[('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),3.6),('BOTTOMPADDING',(0,0),(-1,-1),3.6),
        ('LEFTPADDING',(0,0),(-1,-1),4.6),('RIGHTPADDING',(0,0),(-1,-1),4.6),
        ('LINEBELOW',(0,0),(-1,-1),0.35,LGREY),
        ('BOX',(0,0),(-1,-1),0.6,colors.HexColor("#b9c0ca")),
        ('LINEAFTER',(0,0),(-2,-1),0.3,LGREY)]
    for i in range(1,len(data)):
        if i%2==0: st.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor("#f6f8fa")))
    t.setStyle(TableStyle(st))
    out=[]
    if caption.strip(): out.append(Paragraph(esc(caption),S['tcap']))
    out.append(t); out.append(Spacer(1,9))
    return out

def _callout(kind,text):
    conf={'INF':("INFERENCE — not a sourced fact",INFBG,TEAL),
          'WARN':("UNCERTAINTY / STALENESS FLAG",WARNBG,RED),
          'KEY':("THE POINT",KEYBG,GOLD),
          'NF':("NOT FOUND",WARNBG,RED),
          'CONF':("SOURCES CONFLICT",WARNBG,RED)}
    lbl,bg,bar=conf[kind]
    inner=[Paragraph(lbl,ParagraphStyle('cl',fontName=SANSB,fontSize=7.2,leading=9.4,textColor=bar,spaceAfter=3.2)),
           Paragraph(esc(text),S['box'])]
    t=Table([[inner]],colWidths=[CW])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),6.5),('BOTTOMPADDING',(0,0),(-1,-1),6.5),
        ('LINEBEFORE',(0,0),(0,-1),2.6,bar),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return [Spacer(1,2.5),t,Spacer(1,8)]

def _fig(name,caption,scale=1.0):
    p=FIGDIR+name
    if not os.path.exists(p): return [Paragraph(f"[missing figure {name}]",S['cap'])]
    from reportlab.lib.utils import ImageReader
    iw,ih=ImageReader(p).getSize()
    w=CW*scale; h=w*ih/iw
    maxh=(A4[1]-52*mm)*0.86
    if h>maxh: h=maxh; w=h*iw/ih
    img=Image(p,width=w,height=h); img.hAlign='CENTER'
    out=[Spacer(1,4),img]
    if caption.strip(): out.append(Paragraph(esc(caption),S['cap']))
    else: out.append(Spacer(1,9))
    return out

def parse(text):
    fl=[]; i=0
    lines=text.split("\n")
    while i<len(lines):
        ln=lines[i]; i+=1
        if not ln.strip(): continue
        if "|" not in ln: 
            fl.append(Paragraph(esc(ln),S['body'])); continue
        tag,rest=ln.split("|",1)
        tag=tag.strip()
        if tag=="#":
            num,ttl,sub=(rest.split("|")+["",""])[:3]
            fl.append(CondPageBreak(70*mm))
            p=Paragraph(esc(f"{num}  {ttl}"),S['h1']); p._tocentry=(0,f"{num}  {ttl}")
            fl.append(p); fl.append(HR(CW,NAVY,1.3))
            if sub.strip(): fl.append(Spacer(1,3)); fl.append(Paragraph(esc(sub),S['h1sub']))
            else: fl.append(Spacer(1,7))
        elif tag=="##":
            num,ttl=(rest.split("|")+[""])[:2]
            fl.append(CondPageBreak(52*mm))
            p=Paragraph(esc(f"{num}  {ttl}"),S['h2']); p._tocentry=(1,f"{num}  {ttl}")
            fl.append(p)
        elif tag=="###": fl.append(CondPageBreak(34*mm)); fl.append(Paragraph(esc(rest),S['h3']))
        elif tag=="####": fl.append(Paragraph(esc(rest),S['h4']))
        elif tag=="P": fl.append(Paragraph(esc(rest),S['body']))
        elif tag=="B": fl.append(Paragraph(esc(rest),S['bullet'],bulletText="•"))
        elif tag=="N": 
            n,t2=rest.split("|",1); fl.append(Paragraph(esc(t2),S['bullet'],bulletText=n))
        elif tag in ("INF","WARN","KEY","NF","CONF"): fl+=_callout(tag,rest)
        elif tag=="FIG":
            parts=rest.split("|"); nm=parts[0]; cap=parts[1] if len(parts)>1 else ""
            sc=float(parts[2]) if len(parts)>2 else 1.0
            fl+=_fig(nm,cap,sc)
        elif tag=="TBL":
            cap,widths=rest.split("|",1)
            widths,first=widths.split("|",1)
            rows=[first]
            while i<len(lines) and lines[i].startswith("R|"):
                rows.append(lines[i][2:]); i+=1
            fl.append(CondPageBreak(30*mm))
            fl+=_tbl(cap,widths,rows)
        elif tag=="SRC": fl.append(Paragraph(esc(rest),S['src']))
        elif tag=="GL": fl.append(Paragraph(esc(rest),S['gl']))
        elif tag=="HR": fl.append(Spacer(1,3)); fl.append(HR(CW)); fl.append(Spacer(1,4))
        elif tag=="PB": fl.append(PageBreak())
        elif tag=="SP": fl.append(Spacer(1,float(rest)))
        else: fl.append(Paragraph(esc(ln),S['body']))
    return fl
