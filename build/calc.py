"""Illustrative management-fee model.

The same algorithm is implemented in JavaScript in build/app/app.js (function feeModel).
build/test_app.js checks that both give identical results for every preset case.

Model, month by month (m = 1 .. months):
  1. Flows land at the START of the month:
       - initial funding in month 1 (size x funded_pct_initial)
       - the unfunded remainder in `remaining_funded_month` (if set)
       - a one-off flow (`flow_amount`, negative = withdrawal) in `flow_month`
       - a recurring net flow (`monthly_flow`) from `monthly_flow_start` onwards
     A withdrawal can never take the balance below zero.
  2. The fee for the month = annual fee on the fee base / 12.
       - fee base 'market_value': the balance after step 1
       - fee base 'committed'   : the committed size, whatever has been drawn or its value
     Annual fee = flat rate, or the sum over tiers (breakpoints) of slice x tier rate.
     A fee change replaces the flat rate from `fee_change_month` onwards.
  3. The market return for the month is applied at the END of the month:
       monthly rate = (1 + annual_return) ** (1/12) - 1
  Fees are assumed to be invoiced separately (not deducted from the assets).

Everything this produces is an illustration of gross management fees before costs,
rebates, distribution payments, performance fees and any other adjustment. It is not
a statement of any firm's actual fees.
"""

DEFAULTS = {
    "currency": "£",
    "size": 500_000_000,
    "funded_pct_initial": 100,
    "remaining_funded_month": None,
    "annual_return_pct": 0.0,
    "flow_amount": 0,
    "flow_month": None,
    "monthly_flow": 0,
    "monthly_flow_start": None,
    "fee_mode": "flat",          # 'flat' | 'tiered'
    "fee_bps": 20.0,
    "tiers": [],                  # [{"upto": 250_000_000, "bps": 25}, {"upto": None, "bps": 15}]
    "fee_change_month": None,
    "new_fee_bps": None,
    "months": 12,
    "fee_base": "market_value",  # 'market_value' | 'committed'
}


def annual_fee(base, p, month):
    """Annual fee on `base` under the schedule that applies in `month`."""
    if p["fee_mode"] == "tiered" and p["tiers"]:
        fee, lower = 0.0, 0.0
        for t in p["tiers"]:
            upper = t["upto"] if t["upto"] is not None else float("inf")
            slice_ = max(0.0, min(base, upper) - lower)
            fee += slice_ * t["bps"] / 10_000
            lower = upper
            if base <= upper:
                break
        return fee
    bps = p["fee_bps"]
    if p["fee_change_month"] and p["new_fee_bps"] is not None and month >= p["fee_change_month"]:
        bps = p["new_fee_bps"]
    return base * bps / 10_000


def fee_model(params):
    p = dict(DEFAULTS)
    p.update({k: v for k, v in params.items() if k in DEFAULTS})
    months = int(p["months"])
    r_m = (1 + p["annual_return_pct"] / 100) ** (1 / 12) - 1
    bal = 0.0
    rows = []
    for m in range(1, months + 1):
        flow = 0.0
        if m == 1:
            flow += p["size"] * p["funded_pct_initial"] / 100
        if p["remaining_funded_month"] and m == p["remaining_funded_month"]:
            flow += p["size"] * (100 - p["funded_pct_initial"]) / 100
        if p["flow_month"] and m == p["flow_month"]:
            flow += p["flow_amount"]
        if p["monthly_flow"] and p["monthly_flow_start"] and m >= p["monthly_flow_start"]:
            flow += p["monthly_flow"]
        bal = max(0.0, bal + flow)
        base = p["size"] if p["fee_base"] == "committed" else bal
        fee = annual_fee(base, p, m) / 12
        rows.append({"month": m, "flow": flow, "start_balance": bal, "fee_base": base, "fee": fee})
        bal = bal * (1 + r_m)
        rows[-1]["end_balance"] = bal
    years = []
    for y in range(0, (months + 11) // 12):
        chunk = rows[y * 12:(y + 1) * 12]
        avg = sum(r["fee_base"] for r in chunk) / len(chunk)
        fees = sum(r["fee"] for r in chunk)
        years.append({
            "year": y + 1,
            "months": len(chunk),
            "avg_fee_base": avg,
            "fees": fees,
            "effective_bps_annualised": (fees / avg * 10_000 * 12 / len(chunk)) if avg else None,
            "end_balance": chunk[-1]["end_balance"],
        })
    total = sum(r["fee"] for r in rows)
    return {"params": p, "rows": rows, "years": years, "total_fees": total}


def money(x, cur="£"):
    if x is None:
        return "n/a"
    neg = x < 0
    x = abs(x)
    if x >= 1e9:
        s = f"{x / 1e9:,.3f}".rstrip("0").rstrip(".") + "bn"
    elif x >= 1e6:
        s = f"{x / 1e6:,.3f}".rstrip("0").rstrip(".") + "m"
    elif x >= 1e3:
        s = f"{x / 1e3:,.1f}".rstrip("0").rstrip(".") + "k"
    else:
        s = f"{x:,.0f}"
    return ("-" if neg else "") + cur + s


if __name__ == "__main__":
    out = fee_model({"size": 500_000_000, "fee_bps": 20, "months": 12})
    assert abs(out["total_fees"] - 1_000_000) < 1e-6, out["total_fees"]
    print("£500m at 20bp for 12 months ->", money(out["total_fees"]))
