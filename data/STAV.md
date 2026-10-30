# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba stromu: Hildegard Winterová (* 1909 Podmokly), dcera Rudolfa Wintera (* 1874 Prunéřov) a Fanni Schwarzové (* 1870). Výzkum vede rodina Rudolfa Wintera, cukráře v Podmoklech.
- Uživatel: Jan; chce důsledné rozlišení primárních a sekundárních pramenů, zvláštní důraz na osudy rodiny 1938–1945 a po 1945.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Hotovo (30. 10. 2026): křest Rudolfa 1874; sňatek rodičů 1871 (Prunéřov); sňatek Rudolf × Fanni 8. 1. 1903 Teplá (rodiče Fanni: J. N. Schwarz, mlynář Prosauer Mühle 13, a Aloisie Wollrab); živnost 1903 (čp. 337); sčítání 1921; úmrtí Rudolfa 9. 8. 1926 (Herzklappenfehler); sňatek Hildegardy s Franzem Robertem Albinem Eliášem 19. 5. 1932 (Podmokly 133/123 fol. 220); dítě Gerda * 19. 1. 1942; živnost Hildegardy 11. 7. 1934 – odhlášena 20. 11. 1942.
- Nenalezeno online: křest Fanni (Taufbuch Tom. XXII fol. 176 – kniha online není), křest Hildegardy (Altstadt-Weiher V/209) a Franze Eliáše (Altstadt VII/145), úmrtí Fanni (po 1938), osudy po 1945 → archivni_dotazy.md.
- Další možné kroky online: Josef Winter * asi 1836 a sourozenci (starší Rudolf Winter, cukrář v Bodenbachu 1874) v L123/5 (sn. ~165–176); Johann Nep. Schwarz – sňatek s Aloisií Wollrab (Teplá, asi 1865–1878); rodiče Franze Eliáše; kavárenská koncese 1912. GEDCOM: vystupy/rodokmen_winter.ged (generuje tools/gedcom_winter.py).
