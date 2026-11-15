"""Paint a cream background across every whole page of the PDF, margins included.

Chromium only paints backgrounds inside the page margins, which leaves a white frame round a
cream text block. This adds one small shared drawing instruction (a cream rectangle) in front
of each page's existing content. The original page content is not rewritten, so links, the
contents page, page numbers and file size are unaffected.

Usage: python3 build/page_background.py <file.pdf>
"""
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DecodedStreamObject, NameObject

CREAM = (253 / 255, 247 / 255, 231 / 255)   # matches #fdf7e7 in build/app/print.css


def main(path):
    reader = PdfReader(path)
    writer = PdfWriter(clone_from=reader)
    first = writer.pages[0]
    w, h = float(first.mediabox.width), float(first.mediabox.height)
    stream = DecodedStreamObject()
    stream.set_data(f"q {CREAM[0]:.3f} {CREAM[1]:.3f} {CREAM[2]:.3f} rg 0 0 {w:.2f} {h:.2f} re f Q\n".encode())
    ref = writer._add_object(stream)
    for page in writer.pages:
        existing = page.raw_get("/Contents") if "/Contents" in page else None
        if existing is None:
            page[NameObject("/Contents")] = ref
            continue
        resolved = existing.get_object()
        if isinstance(resolved, ArrayObject):
            page[NameObject("/Contents")] = ArrayObject([ref] + list(resolved))
        else:
            page[NameObject("/Contents")] = ArrayObject([ref, existing])
    with open(path, "wb") as f:
        writer.write(f)
    print(f"cream page background added to {len(writer.pages)} pages")


if __name__ == "__main__":
    main(sys.argv[1])
