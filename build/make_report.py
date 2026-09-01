# -*- coding: utf-8 -*-
import sys, importlib
sys.path.insert(0, '/home/user/Applications2027/build')
from pdfbuild import *

PARTS = sys.argv[1].split(',') if len(sys.argv) > 1 else ['c_part1','c_part2']
OUTPATH = sys.argv[2] if len(sys.argv) > 2 else '/home/user/Applications2027/output/JPMorgan_deep_dive.pdf'

def title_page():
    F=[]; A=F.append
    A(Spacer(1, 30*mm))
    t=Table([['']], colWidths=[64*mm], rowHeights=[3.2*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),AMBER)])); t.hAlign='LEFT'
    A(t); A(Spacer(1, 11*mm))
    A(Paragraph('JPMorganChase', S['ttl']))
    A(Paragraph('How the firm makes money, and which London<br/>summer analyst programme to apply to', S['sub']))
    A(Spacer(1, 13*mm))
    A(Paragraph('A research report written for a reader with no prior knowledge of banking. '
                'Every piece of jargon is defined in plain English where it first appears. Figures are dated. '
                'Sourced fact and author inference are labelled separately throughout.', S['meta']))
    A(Spacer(1, 16*mm))
    rows=[['Research conducted','31 August 2026 — all web sources accessed on this date'],
          ['Most recent full-year data','FY2025 (Form 10-K filed 13 February 2026)'],
          ['Most recent quarterly data','Q2 2026 (reported July 2026)'],
          ['Recruitment data','JPMorgan live requisition records, read 31 August 2026'],
          ['Application cycle covered','Summer 2027 London programmes — opened 31 August 2026'],
          ['Stated application deadline','1 November 2026, 23:55'],
          ['Prepared for','A student or early-career candidate applying to JPMorgan in London']]
    tt=Table([[Paragraph(f'<b>{a}</b>',S['td']), Paragraph(b,S['td'])] for a,b in rows], colWidths=[46*mm,124*mm])
    tt.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),4.4),('BOTTOMPADDING',(0,0),(-1,-1),4.4),
        ('LINEBELOW',(0,0),(-1,-2),0.4,RULE),('LINEABOVE',(0,0),(-1,0),0.9,NAVY),
        ('LINEBELOW',(0,-1),(-1,-1),0.9,NAVY),('LEFTPADDING',(0,0),(-1,-1),0)]))
    tt.hAlign='LEFT'; A(tt)
    A(Spacer(1, 14*mm))
    A(callout('A warning about this document, before you rely on any of it',
        'Recruitment deadlines, leadership names and financial figures all change. Every material claim below carries a date and a '
        'source. Where a source could not be found, the report says "not found" and tells you where to look instead — it does not '
        'guess. Where a conclusion is the author\'s reasoning rather than a published figure, it is marked as inference. '
        'Verify the application deadlines yourself before you rely on them: they are the fastest-moving facts here.', 'warn'))
    A(PageBreak())
    return F

def toc_page():
    toc = TableOfContents()
    toc.levelStyles = [S['toc1'], S['toc2'], ParagraphStyle('toc3', parent=S['toc2'], leftIndent=26,
                        fontSize=8.4, leading=12.6, textColor=colors.HexColor('#40536b'))]
    return [Paragraph('Contents', S['h1']),
            Paragraph('Page numbers refer to the printed page numbers in the footer.', S['h1sub']),
            toc, PageBreak()]

story = []
story += [NextPageTemplate('main')] + title_page()
story += toc_page()
for m in PARTS:
    story += importlib.import_module(m).build()

doc = Doc(OUTPATH, title='JPMorganChase — business model and London summer analyst programmes',
          author='Research report', subject='JPMorganChase deep dive')
doc.multiBuild(story)
print('BUILT', OUTPATH)
import os; print('size', os.path.getsize(OUTPATH))
