from playwright.sync_api import sync_playwright
import sys, pathlib
src = pathlib.Path(sys.argv[1]).resolve()
out = sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                          args=["--no-sandbox"])
    pg = b.new_page()
    pg.goto(src.as_uri(), wait_until="networkidle")
    pg.pdf(path=out, format="A4", print_background=True,
           display_header_footer=True,
           header_template='<div style="font-size:6.5pt;color:#9aa3b0;width:100%;padding:0 15mm;font-family:Verdana,sans-serif;display:flex;justify-content:space-between;"><span>SEO London &mdash; Deep-Dive Intelligence Report</span><span>August 2026</span></div>',
           footer_template='<div style="font-size:6.5pt;color:#9aa3b0;width:100%;padding:0 15mm;font-family:Verdana,sans-serif;text-align:right;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
           margin={"top":"20mm","bottom":"16mm","left":"15mm","right":"15mm"})
    b.close()
print("written", out)
