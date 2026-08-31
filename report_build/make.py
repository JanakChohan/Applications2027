import sys, os, glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import render
from render import *
from reportlab.platypus.doctemplate import NextPageTemplate

files=sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),"content","c*.txt")),
             key=lambda p:int(os.path.basename(p)[1:-4]))
text="\n".join(open(f).read() for f in files)

def run(toc_entries,outfile):
    doc=Doc(outfile,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=20*mm,bottomMargin=22*mm,
        title="PIMCO - Business Model and London Summer Internship Roles",
        author="Deep research report",subject="PIMCO deep dive")
    doc.offset=OFFSET
    story=title_page()+[PageBreak(),NextPageTemplate('front')]
    story+=toc_flowables(toc_entries)
    story+=[PageBreak(),NextPageTemplate('body')]
    story+=parse(text)
    doc.multiBuild(story)
    return doc.toc

# pass 1: guess offset (title page + toc pages). Assume 2 front pages initially.
OFFSET=2
toc=run(None,"/tmp/pass1.pdf")
# how many pages did the TOC take? rebuild with real entries to find out
OFFSET=2
toc2=run(toc,"/tmp/pass2.pdf")
# determine actual front matter length from pass2 by counting: title(1) + toc pages
from pypdf import PdfReader
# recompute offset: find page where body starts = 1 + tocpages
# estimate toc pages from entry count
n=len(toc2)
tocpages=1 if n<=40 else 2
OFFSET=1+tocpages
toc3=run(toc2,"/tmp/pass3.pdf")
OFFSET=1+tocpages
final=run(toc3,"/home/user/Applications2027/output/PIMCO_deep_dive.pdf")
print("headings:",len(final))
print("offset used:",OFFSET,"toc pages assumed:",tocpages)
for lvl,t,p in final[:8]: print("  ",lvl,t,p)
