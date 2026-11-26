"""Recalculate model.xlsx with LibreOffice (headless), scan every cell for formula errors, and export key outputs
to data/derived/model_outputs.json so that the deck, memo and markdown files quote the model, not hand-typed numbers."""
import os, subprocess, shutil, json, tempfile
from openpyxl import load_workbook
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); D = os.path.join(ROOT, "data", "derived")
src = os.path.join(ROOT, "model.xlsx"); tmp = tempfile.mkdtemp()
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", tmp, src], check=True, capture_output=True, timeout=180)
shutil.copy(os.path.join(tmp, "model.xlsx"), src)          # keep formulas AND cached values in the delivered file
wbv = load_workbook(src, data_only=True); wbf = load_workbook(src)
errs = []; nform = 0
for ws in wbf.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and c.value.startswith("="):
                nform += 1; v = wbv[ws.title][c.coordinate].value
                if v is None or (isinstance(v, str) and v.startswith(("#", "Err:"))): errs.append((ws.title, c.coordinate, c.value[:80], v))
def val(ref):
    sh, cell = ref.split("!"); return wbv[sh][cell.replace("$", "")].value
def rng(ref):
    sh, r = ref.split("!"); return [[c.value for c in row] for row in wbv[sh][r]]
cm = json.load(open(os.path.join(D, "model_cellmap.json")))
out = {"n_formulas": nform, "errors": errs, "inputs": {k: val(v) for k, v in cm["inputs"].items()},
       "valuation": {k: [val(x) for x in v] for k, v in cm["valuation"].items()}, "key": {k: val(v) for k, v in cm["key"].items()},
       "rar": {k: val(v) for k, v in cm["rar"].items()}, "sens": {k: [val(v[0]), val(v[1])] for k, v in cm["sens"].items()},
       "reverse": {k: (rng(v) if ":" in v else val(v)) for k, v in cm["reverse"].items()}, "sens_dcf_grid": rng(cm["sens_dcf_grid"]), "sens_pt_grid": rng(cm["sens_pt_grid"]),
       "checks": rng(cm["checks"]), "peers_derived": rng(cm["peers_derived"]), "scen": {}}
cols = dict(zip(["FY2025A", "FY2026E", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"], "BCDEFGH"))
for sc, rows in cm["scen_rows"].items():
    out["scen"][sc] = {k: {y: wbv[sc][f"{c}{r}"].value for y, c in cols.items()} for k, r in rows.items() if not k.startswith("_")}
    out["scen"][sc]["dcf"] = {k: val(v) for k, v in cm["scen_dcf"][sc].items()}
json.dump(out, open(os.path.join(D, "model_outputs.json"), "w"), indent=1, default=str)
print("formulas:", nform, "errors:", len(errs)); [print(e) for e in errs[:30]]
print(json.dumps(out["valuation"], indent=0)); print(json.dumps(out["key"], indent=0)); print(json.dumps(out["rar"], indent=0)); print(json.dumps(out["sens"], indent=0))
print(out["reverse"]["implied_g"], out["reverse"]["implied_margin"], out["reverse"]["implied_cagr"]); [print(r) for r in out["reverse"]["grid"]]; [print(r) for r in out["checks"]]
b = out["scen"]["Base"]; 
for k in ("rev", "g", "margin", "ebit", "int", "ni", "sh_avg", "eps", "epsg", "fcf", "bb", "sh_end", "nd", "lev", "fcff"): print(k, [round(v, 3) if isinstance(v, (int, float)) else v for v in b[k].values()])
print(out["scen"]["Base"]["dcf"]); print(out["scen"]["Bear"]["dcf"]); print(out["scen"]["Bull"]["dcf"])
