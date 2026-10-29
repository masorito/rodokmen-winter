# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Hildegard Winterová", y="* 1909", st="doc", sex="F", r=["podmokly_scitani_1921_cp332_winter"],
            f=["* 14. 6. 1909 Bodenbach (Podmokly)", "× před 1934 ? Elias (křestní jméno neznámé)",
               "cukrářka, podnikatelka", "1934 povolení k cukrářskému provozu v čp. 332/333 a koncese k podávání nápojů v čp. 332 (jako Hildegard Elias)",
               "1921 bydliště Bodenbach, Bahnhofstraße čp. 332"],
            note="Výchozí osoba stromu (aby šly sledovat obě linie – Winterovi i Schwarzovi). Varianty: Hilda, Hildegarda Eliasová. Údaje ze sčítání 1921 (přepis) a od archivního historika – zatím neověřeno v matrice. Datum a místo úmrtí neznámé."),
    2: dict(n="Rudolf Winter", y="1874–1926", st="doc", r=["prunerov_krest_rudolf_winter_1874", "podmokly_scitani_1921_cp332_winter"],
            f=["* 15. 5. 1874 Prunéřov (Brunnersdorf) čp. 119, pokřtěn 16. 5. 1874", "učení 15. 3. 1889 – 15. 3. 1892 v Kadani (Kaaden)",
               "cukrář, pekař, majitel kavárny", "1903 zakládá cukrářskou a pekařskou živnost v Bodenbachu, čp. 337",
               "1912 majitel čp. 332, žádost o koncesi kavárny", "1921 majitel domu čp. 333 (pekárna)",
               "× Franziska (Fanni) Schwarzová", "† 9. 8. 1926"],
            note="Narození doloženo matrikou (SOA Litoměřice, L123/6, snímek 140). Kmotrem byl jmenovec Rudolf Winter, cukrář v Bodenbachu (1874). Sčítání 1921: v Bodenbachu od 12. 1. 1903, domovská příslušnost Bodenbach, národnost německá, ř.-kat. Ostatní údaje od archivního historika. Příčina smrti (srdeční vada) podle historika – ověřit v matrice zemřelých. Na dopisním papíře 1923 „Gegründet 1865“ – nevysvětleno (předchůdce podniku?)."),
    3: dict(n="Franziska Schwarzová", y="1870–?", st="doc", r=["podmokly_scitani_1921_cp332_winter"],
            f=["* 25. 4. 1870, okres Teplá (obec nejistá: Prosau/Mrázov nebo Royau/Rájov)",
               "× Rudolf Winter", "1921 Bodenbach, Bahnhofstraße čp. 332", "po smrti manžela vedla podnik"],
            # sčítání 1921 (snímek od uživatele): v Bodenbachu od 12. 1. 1903 jako Rudolf; rodiště psané kurentem, čtení zatím nejisté
            note="Varianty: Fanni, Franziska Winter. Originál sčítání 1921 (SOkA Děčín): * 25. 4. 1870, rodiště v okrese Teplá psané kurentem – čtu „Prosau“ (Mrázov) nebo „Royau“ (Rájov); „Parchau“ z přepisu je zřejmě chybné čtení. V matrice narozených Prosau (Porta fontium, svaty-vojtech-06, sn. 14) mezi 8/1869 a 10/1870 nenalezena. Rodné příjmení Schwarz zatím jen z podkladů. Datum úmrtí neznámé."),
    4: dict(n="Josef Winter", y="* asi 1836", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["* asi 1836 Prunéřov (35 let při sňatku)", "obuvnický mistr (Schuhmachermeister) v Prunéřově čp. 119 (1871, 1874)", "× 13. 11. 1871 Prunéřov Marie Weigdörferová"],
            note="Otec Rudolfa. Křest (asi 1836) a úmrtí zatím nehledány."),
    5: dict(n="Marie Weigdörferová", y="* asi 1842", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["* asi 1842 Prunéřov čp. 34 (29 let při sňatku)", "× 13. 11. 1871 Prunéřov Josef Winter"],
            note="Příjmení v kurentu „Weigdörfer / Weikdörfer“; stejně psaný bratr (?) Wenzl Weigdörfer, syn Wenzla z čp. 34 a Kateřiny z čp. 71, se ženil v Prunéřově 1862/63 (L123/8, sn. 23) – to podporuje čtení Weigdörfer."),
    8: dict(n="Anton Winter", y="† před 1871", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["obuvnický mistr v Prunéřově čp. 119", "† před 13. 11. 1871"]),
    9: dict(n="Johanna Kunzová (?)", y="† před 1871", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["z Prunéřova čp. 130", "† před 13. 11. 1871"], note="Rodné příjmení čteno nejistě: 1874 spíš „Kurz“, 1871 spíš „Kunz“ – ověřit v křtu Josefa (asi 1836)."),
    10: dict(n="Václav Weigdörfer", y="† před 1871", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
             f=["rolník (Landwirth) v Prunéřově čp. 34", "† před 13. 11. 1871"]),
    11: dict(n="Kateřina Gschaleová (?)", y="", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
             f=["z Prunéřova čp. 71"], note="Rodné příjmení čteno nejistě („Gschafe“ 1874, „Gschale“ 1871)."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=2, n="Rudolf Winter (cukrář v Bodenbachu 1874)", t="Kmotr (v zastoupení) Rudolfa Wintera 1874, uveden jako „Zuckerbäcker in Bodenbach“. Jmenovec, nejspíš příbuzný (strýc?) – vztah zatím neprokázán. Možné vysvětlení nápisu „Gegründet 1865“.", r=["prunerov_krest_rudolf_winter_1874"]),
    dict(k=1, n="? Elias – manžel Hildegardy", t="Podle archivního historika českého původu; křestní jméno, narození a sňatek zatím neznámé. Sňatek pravděpodobně před 1. 7. 1934."),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kde leží „Parchau, Tepl“, rodiště Fanni Schwarzové?", "Otevřené: přepis sčítání 1921; v soupisech obcí okresu Teplá zatím nenalezeno – ověřit originální arch sčítání."),
    ("Jak se jmenoval manžel Hildegardy Winterové (Elias)?", "Otevřené: hledat oddací matriku Podmokel cca 1926–1934."),
    ("Proč stojí na dopisním papíře z roku 1923 „Gegründet 1865“?", "Hypotéza: při křtu 1874 byl kmotrem Rudolfův jmenovec Rudolf Winter, už tehdy cukrář v Bodenbachu – podnik mohl založit on (1865) a mladší Rudolf ho převzít. Ověřit."),
    ("Co se stalo s Fanni a Hildegardou po roce 1945?", "Otevřené: odsun, nebo zůstaly? Hledat v evidenci obyvatel a fondech národních výborů v SOkA Děčín."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
