# Pictet - A Ground-Up Business Guide

`Pictet_Business_Guide.pdf` - a 40-page, 21-figure guide to the Pictet Group,
written for a reader with no prior knowledge of asset management.

**Contents**

| Part | Covers |
|---|---|
| 1 | Asset management explained from zero: money flow, fees, the value chain, vocabulary |
| 2 | Pictet at a glance: the 2025 numbers and the margins calculated from them |
| 3 | 220 years of history as two illustrated timelines |
| 4 | The partnership: ownership rules, governance, why the structure is the strategy |
| 5 | The four business lines and how they reinforce each other |
| 6 | The 2025 income statement taken apart |
| 7 | The investment engine: thematics, emerging markets, the house view, sustainability |
| 8 | Three competitive arenas, peer numbers, and the definitional trap in league tables |
| 9 | What genuinely differentiates Pictet - and the honest weaknesses |
| 10 | The 2025-26 strategic moves decoded |
| 11 | Interview toolkit |
| Appendix | Data notes, caveats and full source list |

Figures are Pictet's audited 2025 results (published 10 February 2026); news is
current to July 2026.

**Rebuilding**

`build_guide.py` generates `pictet_guide.html` (all charts and diagrams are
generated inline SVG - no external assets, fonts are embedded). Render with:

```
python3 build_guide.py
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=Pictet_Business_Guide.pdf file://$PWD/pictet_guide.html
```

`build_guide.py` expects `fonts_embedded.css` alongside it (Inter and Source
Serif 4, base64-embedded); regenerate it from Google Fonts if missing.
