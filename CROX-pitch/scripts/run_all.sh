#!/usr/bin/env bash
# Re-run the whole pipeline. Steps 01, 03, 04, 07 need network access (SEC EDGAR, Nasdaq API, StockAnalysis) and re-use files already in data/.
# Usage: bash scripts/run_all.sh [--offline]   (offline skips the download steps)
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ "${1:-}" != "--offline" ]]; then
  python3 scripts/01_fetch_sec.py; python3 scripts/03_fetch_market.py; python3 scripts/04_fetch_stockanalysis.py
fi
python3 scripts/02_html_to_text.py 2>/dev/null
python3 scripts/05_parse_releases.py > /dev/null
python3 scripts/06_build_dataset.py > /dev/null
if [[ "${1:-}" != "--offline" ]]; then python3 scripts/07_form4.py > /dev/null; fi
python3 scripts/08_market_analytics.py > /dev/null 2>&1
python3 scripts/09_peers.py > /dev/null
python3 scripts/10_revenue_at_risk.py > /dev/null
python3 scripts/11_build_model.py
python3 scripts/12_recalc_model.py > /dev/null
python3 scripts/14_facts.py > /dev/null      # facts first: charts and documents read model outputs
python3 scripts/13_charts.py > /dev/null
python3 scripts/14_facts.py > /dev/null
python3 scripts/15_sources.py
python3 scripts/16_write_markdown.py
python3 scripts/17_build_memo.py
python3 scripts/18_build_deck.py
python3 scripts/19_verify.py
