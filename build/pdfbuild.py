# -*- coding: utf-8 -*-
"""PDF builder for the JPMorgan deep-dive report."""
import os, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, Image, PageBreak, KeepTogether, NextPageTemplate, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

NAVY   = colors.HexColor('#0b2545')
BLUE   = colors.HexColor('#1d5b9e')
TEAL   = colors.HexColor('#2a9d8f')
AMBER  = colors.HexColor('#d4901a')
RED    = colors.HexColor('#b8392b')
GREY   = colors.HexColor('#5a6b82')
RULE   = colors.HexColor('#c3cede')
LIGHT  = colors.HexColor('#eef3f9')
LIGHT2 = colors.HexColor('#f7fafc')
WARN   = colors.HexColor('#fdf6e7')

# Fonts: DejaVu supports the dashes/arrows/pound signs we use.
import matplotlib as _mpl
DJ = os.path.join(os.path.dirname(_mpl.__file__),'mpl-data','fonts','ttf')
if not os.path.exists(os.path.join(DJ,'DejaVuSans-Oblique.ttf')): DJ='/usr/share/fonts/truetype/dejavu/'
for nm, fn in [('DJ','DejaVuSans.ttf'),('DJ-B','DejaVuSans-Bold.ttf'),('DJ-I','DejaVuSans-Oblique.ttf'),('DJ-BI','DejaVuSans-BoldOblique.ttf')]:
    p = os.path.join(DJ, fn)
    if not os.path.exists(p): raise SystemExit('MISSING FONT '+p)
    pdfmetrics.registerFont(TTFont(nm, p))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('DJ', normal='DJ', bold='DJ-B', italic='DJ-I', boldItalic='DJ-BI')
F, FB, FI = 'DJ', 'DJ-B', 'DJ-I'

S = {}
S['body']   = ParagraphStyle('body', fontName=F, fontSize=9.3, leading=14.2, alignment=TA_JUSTIFY,
                             textColor=colors.HexColor('#16283f'), spaceAfter=6.5)
S['lead']   = ParagraphStyle('lead', parent=S['body'], fontSize=10.4, leading=16, textColor=NAVY, spaceAfter=9)
S['h1']     = ParagraphStyle('h1', fontName=FB, fontSize=19, leading=23, textColor=NAVY, spaceBefore=2, spaceAfter=3)
S['h1sub']  = ParagraphStyle('h1sub', fontName=FI, fontSize=10, leading=14, textColor=GREY, spaceAfter=14)
S['h2']     = ParagraphStyle('h2', fontName=FB, fontSize=13, leading=17, textColor=NAVY, spaceBefore=15, spaceAfter=6)
S['h3']     = ParagraphStyle('h3', fontName=FB, fontSize=10.4, leading=14, textColor=BLUE, spaceBefore=10, spaceAfter=4)
S['h4']     = ParagraphStyle('h4', fontName='DJ-BI', fontSize=9.5, leading=13, textColor=colors.HexColor('#2c3e52'), spaceBefore=8, spaceAfter=3)
S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=11, bulletIndent=2, spaceAfter=3.6, alignment=TA_LEFT)
S['cap']    = ParagraphStyle('cap', fontName=FI, fontSize=7.8, leading=10.6, textColor=GREY, alignment=TA_LEFT, spaceBefore=3, spaceAfter=11)
S['tcap']   = ParagraphStyle('tcap', fontName=FB, fontSize=8.8, leading=12, textColor=NAVY, spaceBefore=9, spaceAfter=4)
S['th']     = ParagraphStyle('th', fontName=FB, fontSize=7.7, leading=9.8, textColor=colors.white)
S['td']     = ParagraphStyle('td', fontName=F, fontSize=7.7, leading=9.8, textColor=colors.HexColor('#16283f'))
S['tdb']    = ParagraphStyle('tdb', fontName=FB, fontSize=7.7, leading=9.8, textColor=NAVY)
S['callh']  = ParagraphStyle('callh', fontName=FB, fontSize=9.2, leading=12.4, textColor=NAVY, spaceAfter=3)
S['callb']  = ParagraphStyle('callb', fontName=F, fontSize=8.7, leading=12.6, textColor=colors.HexColor('#22364e'), alignment=TA_LEFT)
S['toc1']   = ParagraphStyle('toc1', fontName=FB, fontSize=10, leading=17, textColor=NAVY)
S['toc2']   = ParagraphStyle('toc2', fontName=F, fontSize=9, leading=14, textColor=colors.HexColor('#22364e'), leftIndent=13)
S['ttl']    = ParagraphStyle('ttl', fontName=FB, fontSize=31, leading=36, textColor=NAVY, alignment=TA_LEFT)
S['sub']    = ParagraphStyle('sub', fontName=F, fontSize=13.5, leading=19, textColor=BLUE, alignment=TA_LEFT)
S['meta']   = ParagraphStyle('meta', fontName=F, fontSize=9.2, leading=15, textColor=GREY, alignment=TA_LEFT)
S['src']    = ParagraphStyle('src', fontName=F, fontSize=7.9, leading=11.4, textColor=colors.HexColor('#22364e'), spaceAfter=4.5, leftIndent=13, firstLineIndent=-13)

class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, pagesize=A4, **kw)
        fw, fh = A4[0]-2*20*mm, A4[1]-2*20*mm
        frame = Frame(20*mm, 18*mm, fw, fh-6*mm, id='n')
        self.addPageTemplates([
            PageTemplate(id='title', frames=[Frame(20*mm,18*mm,fw,fh-6*mm,id='t')], onPage=self._blank),
            PageTemplate(id='main',  frames=[frame], onPage=self._deco)])
        self.seen = set()
    def _blank(self, c, d): pass
    def _deco(self, c, d):
        c.saveState()
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.line(20*mm, A4[1]-16*mm, A4[0]-20*mm, A4[1]-16*mm)
        c.setFont(F, 7.4); c.setFillColor(GREY)
        c.drawString(20*mm, A4[1]-13.4*mm, 'JPMorganChase — business model and London summer analyst programmes')
        c.drawRightString(A4[0]-20*mm, A4[1]-13.4*mm, 'Research conducted 31 August 2026')
        c.line(20*mm, 14.5*mm, A4[0]-20*mm, 14.5*mm)
        c.setFont(FB, 8.4); c.setFillColor(NAVY)
        c.drawRightString(A4[0]-20*mm, 10*mm, str(d.page))
        c.setFont(FI, 7.2); c.setFillColor(GREY)
        c.drawString(20*mm, 10*mm, 'Figures dated. Inference marked. Sources listed in section 6.5.')
        c.restoreState()
    def afterFlowable(self, f):
        if hasattr(f, 'toclevel') and getattr(f, '_tocText', None):
            self.notify('TOCEntry', (f.toclevel, f._tocText, self.page))

_AMP = re.compile(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)')
def esc(t):
    return _AMP.sub('&amp;', t)
def P(t, st='body'): return Paragraph(esc(t), S[st])

def heading(txt, lvl):
    st = {0:'h1',1:'h2',2:'h3'}[lvl]
    p = Paragraph(esc(txt), S[st]); p.toclevel = lvl; p._tocText = esc(txt)
    return p

def make_table(headers, rows, widths=None, align=None, total_w=170*mm, small=False):
    fs = 7.0 if small else 7.7
    hs = ParagraphStyle('h_', parent=S['th'], fontSize=fs, leading=fs+2.1)
    ds = ParagraphStyle('d_', parent=S['td'], fontSize=fs, leading=fs+2.1)
    bs = ParagraphStyle('b_', parent=S['tdb'], fontSize=fs, leading=fs+2.1)
    data = [[Paragraph(esc(h), hs) for h in headers]]
    for r in rows:
        rr = []
        for i, c in enumerate(r):
            c = '' if c is None else str(c)
            rr.append(Paragraph(esc(c), bs if i == 0 else ds))
        data.append(rr)
    if widths is None:
        widths = [total_w/len(headers)]*len(headers)
    else:
        s = sum(widths); widths = [w/s*total_w for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    st = [('BACKGROUND',(0,0),(-1,0),NAVY),
          ('VALIGN',(0,0),(-1,-1),'TOP'),
          ('TOPPADDING',(0,0),(-1,-1),3.6),('BOTTOMPADDING',(0,0),(-1,-1),3.6),
          ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
          ('LINEBELOW',(0,0),(-1,-1),0.4,RULE),
          ('BOX',(0,0),(-1,-1),0.7,RULE)]
    for i in range(1, len(data)):
        if i % 2 == 0: st.append(('BACKGROUND',(0,i),(-1,i),LIGHT2))
    if align:
        for col, a in align.items(): st.append(('ALIGN',(col,1),(col,-1),a))
    t.setStyle(TableStyle(st))
    return t

def callout(title, body, kind='info'):
    bg = {'info':LIGHT,'warn':WARN,'key':colors.HexColor('#eaf4f1')}[kind]
    bar = {'info':BLUE,'warn':AMBER,'key':TEAL}[kind]
    inner = [Paragraph(esc(title), S['callh'])] if title else []
    inner.append(Paragraph(esc(body), S['callb']))
    t = Table([[inner]], colWidths=[170*mm], hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),
        ('LINEBEFORE',(0,0),(0,-1),2.6,bar),('BOX',(0,0),(-1,-1),0.5,RULE),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9)]))
    return t

FIGDIR = '/home/user/Applications2027/output/figs'
def figure(name, caption, width=170*mm):
    from PIL import Image as PILImage
    p = f'{FIGDIR}/{name}.png'
    iw, ih = PILImage.open(p).size
    w = width; h = w*ih/iw
    maxh = 205*mm
    if h > maxh: h = maxh; w = h*iw/ih
    img = Image(p, width=w, height=h)
    img.hAlign = 'CENTER'
    return KeepTogether([img, Paragraph(esc(caption), S['cap'])])

def kv_table(rows, widths=(0.85,4.0), total_w=170*mm, small=True):
    fs = 7.3 if small else 8.0
    ls = ParagraphStyle('kl', fontName=FB, fontSize=fs, leading=fs+2.4, textColor=NAVY)
    vs = ParagraphStyle('kv', fontName=F, fontSize=fs, leading=fs+2.6, textColor=colors.HexColor('#16283f'))
    data = [[Paragraph(esc(a), ls), Paragraph(esc(b), vs)] for a, b in rows]
    s = sum(widths); w = [x/s*total_w for x in widths]
    t = Table(data, colWidths=w, hAlign='LEFT')
    st = [('VALIGN',(0,0),(-1,-1),'TOP'),
          ('TOPPADDING',(0,0),(-1,-1),3.4),('BOTTOMPADDING',(0,0),(-1,-1),3.4),
          ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
          ('LINEBELOW',(0,0),(-1,-2),0.35,RULE),
          ('LINEABOVE',(0,0),(-1,0),0.9,NAVY),('LINEBELOW',(0,-1),(-1,-1),0.9,NAVY),
          ('BACKGROUND',(0,0),(0,-1),LIGHT2)]
    t.setStyle(TableStyle(st))
    return t
