# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- SOA Litoměřice v cloudu (bez Claude in Chrome): digi.soalitomerice.cz jde ovládat headless Playwrightem přes proxy (`chromium.launch({proxy:{server:HTTPS_PROXY}})`, `ignoreHTTPSErrors`). Ověření projde samo (~15 s), cookies uložit do storageState. Hledání svazků: pole „Místo / Lokalita“ (#geoAccessPointText) + datum od–do; ID snímků jsou v `select` na detailu svazku (`N%20uuid`), cesta k obrázku z `showZoomify/<entita>/<uuid>`. Stálo by za to udělat z toho nástroj `soal.py` (hledat / snimek).
