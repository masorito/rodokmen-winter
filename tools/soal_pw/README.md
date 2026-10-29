# Badatelna SOA Litoměřice přes headless prohlížeč (Playwright)

Spouštět ze složky, kde se smí ukládat `state.json` a `opts_*.json` (např. scratchpad), s `NODE_PATH=$(npm root -g)`.
- `node geo.js "<Obec>" <rok_od> <rok_do> [text]` – seznam svazků podle místa (nová relace, ~20 s ověření).
- `PAT="<text>" node vol2.js "<Obec>" <rok> "<text ve výsledku, např. sign. 133/131>" <pref> [snímky…]` – otevře svazek, uloží `opts_<pref>.json` a `ent_<pref>.txt`.
- `./get.sh <pref> <0|1|2> n1 n2 …` – stáhne snímky do `pracovni/<pref>/` (0 = plné rozlišení). Cesta v get.sh je absolutní – upravit.
Pozor: detail svazku (`vysledekDetail/…?page=N`) se řídí pořadím ve výsledcích hledání, ne ID – proto vol2.js hledá svazek podle textu.
Trvalý odkaz na snímek: `showZoomifySeparate?imageNumberSeparate=N&myEntityUuid=<entita>&myImageUuid=<uuid>`.
