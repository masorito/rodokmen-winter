# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Prostředí (cloud, claude.ai)
- Linux, ImageMagick 6 (`convert`, nástroje ho použijí samy), Python 3.13, Node 22.
- Kontejner je dočasný: po každém větším kroku `git commit` a `git push` do https://github.com/masorito/rodokmen-winter (větev main). `pracovni/` se neukládá (stažené snímky – lze znovu stáhnout).
- Síť: SOA Litoměřice (digi.soalitomerice.cz) a Porta fontium fungují. Badatelnu Litoměřice ovládat headless Playwrightem (viz poznamky_pro_skill.md); WebFetch je blokovaný, curl funguje.
