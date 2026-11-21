import sys
from pypdf import PdfReader, PdfWriter
src=PdfReader(sys.argv[1]); w=PdfWriter()
for pg in src.pages:
    bg=PdfReader('bg.pdf').pages[0]
    bg.merge_page(pg)
    w.add_page(bg)
w.add_metadata({'/Title':sys.argv[3] if len(sys.argv)>3 else 'TP ICAP'})
w.write(sys.argv[2])
