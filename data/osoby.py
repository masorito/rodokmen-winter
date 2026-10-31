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
    1: dict(n="Hildegard Winterová", y="* 1909", st="doc", sex="F", r=["podmokly_scitani_1921_cp332_winter", "podmokly_snatek_franz_elias_hildegard_winter_1932", "podmokly_zivnost_hildegard_eliasova_1934"],
            f=["* 14. 6. 1909 Bodenbach (Podmokly); křest v matrice Altstadt-Weiher sv. V, fol. 209", "× 19. 5. 1932 Podmokly Franz Robert Albin Eliáš, cukrář", "1941 úřední změna příjmení Eliáš → Elias",
               "cukrářka, podnikatelka", "1934 povolení k cukrářskému provozu v čp. 332/333 a koncese k podávání nápojů v čp. 332 (jako Hildegard Elias)",
               "11. 7. 1934 živnostenský list – živnost cukrářská, Podmokly čp. 332 (jako Hildegard Eliasová)", "20. 11. 1942 cukrářská živnost odhlášena",
               "1921 bydliště Bodenbach, Bahnhofstraße čp. 332"],
            note="Výchozí osoba stromu (aby šly sledovat obě linie – Winterovi i Schwarzovi). Varianty: Hilda, Hildegarda Eliášová / Eliasová, Hildegard Elias. Narození a rodiče doloženy sčítáním 1921 a oddacím zápisem 1932 (odkaz na křest: Altstadt Weiher V/209 – svazek zatím nenalezen). Povolení a koncese 1934 (1. 7. a 19. 11.) od archivního historika; živnostenský list 11. 7. 1934 doložen rejstříkem. Datum a místo úmrtí neznámé."),
    2: dict(n="Rudolf Winter", y="1874–1926", st="doc", r=["prunerov_krest_rudolf_winter_1874", "podmokly_scitani_1921_cp332_winter", "podmokly_zivnost_rudolf_winter_1903", "podmokly_umrti_rudolf_winter_1926", "tepla_snatek_rudolf_winter_franziska_schwarz_1903"],
            f=["* 15. 5. 1874 Prunéřov (Brunnersdorf) čp. 119, pokřtěn 16. 5. 1874", "učení 15. 3. 1889 – 15. 3. 1892 v Kadani (Kaaden)",
               "cukrář, pekař, majitel kavárny", "4. 3. 1903 ohlášena cukrářská živnost (Conditorgewerbe) v Bodenbachu čp. 337",
               "dům čp. 332 koupil mezi 8/1910 a 1/1912 (předtím Sonntagovi)", "1912 přestavba přízemí na kavárnu, 22. 8. 1912 žádost o koncesi kavárny", "1921 majitel domu čp. 333 (pekárna)",
               "× 8. 1. 1903 Teplá (kostel sv. Jiljí) Franziska (Fanni) Schwarzová", "1902 cukrář v Prunéřově", "† 9. 8. 1926 Podmokly čp. 332, vada srdeční chlopně, pohřben 12. 8. 1926"],
            note="Narození doloženo matrikou (SOA Litoměřice, L123/6, snímek 140). Kmotrem byl jmenovec Rudolf Winter, cukrář v Bodenbachu (1874). Sčítání 1921: v Bodenbachu od 12. 1. 1903, domovská příslušnost Bodenbach, národnost německá, ř.-kat. Ostatní údaje od archivního historika. Úmrtí a příčina (Herzklappenfehler) doloženy matrikou zemřelých Podmokly 133/132, sn. 218; tamtéž údaj o sňatku 8. 1. 1903 v Teplé. Na dopisním papíře 1923 „Gegründet 1865“ – nevysvětleno (předchůdce podniku?)."),
    3: dict(n="Franziska Schwarzová", y="* asi 1878", st="doc", r=["tepla_snatek_rudolf_winter_franziska_schwarz_1903", "podmokly_scitani_1921_cp332_winter", "podmokly_umrti_rudolf_winter_1926", "podmokly_snatek_franz_elias_hildegard_winter_1932"],
            f=["* 25. 4. asi 1878 Mrázov (Prosau) u Teplé, Mrázovský mlýn čp. 13 (24 let při sňatku 1903; sčítání 1921 „25. 4. 187?“)",
               "× 8. 1. 1903 Teplá (kostel sv. Jiljí) Rudolf Winter", "1921 Bodenbach, Bahnhofstraße čp. 332", "po smrti manžela vedla podnik", "1934 v adresáři: Winter Fanny, Konditorei, Bahnhofstraße 332", "24. 11. 1938 a 2/1939 majitelka domu čp. 332 (stavební spis)"],
            note="Varianty: Fanni, Franziska Winter. Originál sčítání 1921 (SOkA Děčín): * 25. 4. 1870, rodiště v okrese Teplá psané kurentem = „Prosau“ (Mrázov); potvrzeno oddacím zápisem dcery 1932: „Franziska geb. Schwarz aus Prosauer Mühle 13“. „Parchau“ z přepisu je chybné čtení. Rodné příjmení Schwarz doloženo oddacím zápisem 1932. V matrice narozených Prosau 8/1869–10/1870 není – odpovídá to sňatku 1903 (24 let → narozena asi 1878). Rodiče podle sňatku 1903: Johann Nepomuk Schwarz, měšťan a mlynářský mistr v Mrázovském mlýně čp. 13, a Aloisie roz. Wollrabová z Teplé čp. 28. Křest odkazem „Taufbuch Tom. XXII fol. 176“. Datum úmrtí neznámé."),
    4: dict(n="Josef Winter", y="* asi 1836", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["* asi 1836 Prunéřov (35 let při sňatku)", "obuvnický mistr (Schuhmachermeister) v Prunéřově čp. 119 (1871, 1874)", "× 13. 11. 1871 Prunéřov Marie Weitzdörferová"],
            note="Otec Rudolfa. Křest (asi 1836) a úmrtí zatím nehledány."),
    5: dict(n="Marie Weitzdörferová", y="* asi 1842", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["* asi 1842 Prunéřov čp. 34 (29 let při sňatku)", "× 13. 11. 1871 Prunéřov Josef Winter"],
            note="Příjmení: v oddacím zápisu syna 1903 čitelně „Weizdörfer“, svědek Isidor „Weitzdörfer“ z Prunéřova – přijato Weitzdörfer (v kurentu 1871/1874 čteno Weigdörfer/Weikdörfer); stejně psaný bratr (?) Wenzl Weigdörfer, syn Wenzla z čp. 34 a Kateřiny z čp. 71, se ženil v Prunéřově 1862/63 (L123/8, sn. 23) – to podporuje čtení Weigdörfer."),
    8: dict(n="Anton Winter", y="† před 1871", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["obuvnický mistr v Prunéřově čp. 119", "† před 13. 11. 1871"]),
    9: dict(n="Johanna Kunzová (?)", y="† před 1871", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
            f=["z Prunéřova čp. 130", "† před 13. 11. 1871"], note="Rodné příjmení čteno nejistě: 1874 spíš „Kurz“, 1871 spíš „Kunz“ – ověřit v křtu Josefa (asi 1836)."),
    10: dict(n="Václav Weitzdörfer", y="† před 1871", st="doc", r=["prunerov_krest_rudolf_winter_1874", "prunerov_snatek_josef_winter_marie_weigdorfer_1871"],
             f=["rolník (Landwirth) v Prunéřově čp. 34", "† před 13. 11. 1871"]),
    6: dict(n="Johann Nepomuk Schwarz", y="", st="doc", r=["tepla_snatek_rudolf_winter_franziska_schwarz_1903"],
            f=["měšťan, mlynářský mistr (bürgerl. Müllermeister) v Mrázovském mlýně (Prosauer Mühle) čp. 13 (1903)", "× Aloisie Wollrabová"],
            note="Z oddacího zápisu dcery 1903; žil ještě v lednu 1903 (není uveden jako zemřelý)."),
    7: dict(n="Aloisie Wollrabová", y="", st="doc", r=["tepla_snatek_rudolf_winter_franziska_schwarz_1903"],
            f=["z Teplé čp. 28"], note="Z oddacího zápisu dcery 1903. Svědek Johann Wollrab, měšťan v Teplé čp. 278, nejspíš příbuzný."),
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
    dict(k=2, n="Rudolf Winter (cukrář v Bodenbachu 1874)", t="Kmotr (v zastoupení) Rudolfa Wintera 1874, uveden jako „Zuckerbäcker in Bodenbach“. V Podmoklech se v letech 1860–1874 neženil a v letech 1862–1900 tam nekřtil děti (rejstříky) – žil tedy nejspíš svobodný nebo jinde (Děčín-město?). Jmenovec, nejspíš příbuzný (strýc?) – vztah zatím neprokázán. Možné vysvětlení nápisu „Gegründet 1865“.", r=["prunerov_krest_rudolf_winter_1874"]),
    dict(k=2, n="Leo Winter, cukrář v Podmoklech (1934)", t="Adresář 1934: „Winter Leo, Konditor, Theod.-Körner-Str. 740“. Další cukrář Winter v Podmoklech – vztah k rodině neznámý (potomek staršího Rudolfa, cukráře 1874?)."),
    dict(k=2, n="Florian Winter, kaplan v Teplé (1903)", t="Kaplan, který 8. 1. 1903 v Teplé oddával Rudolfa a Fanni. Shoda příjmení naznačuje příbuznost (bratr? bratranec?) – neprokázáno.", r=["tepla_snatek_rudolf_winter_franziska_schwarz_1903"]),
    dict(k=2, n="Isidor Weitzdörfer, hospodář v Prunéřově (1903)", t="Svědek na svatbě Rudolfa 1903; nejspíš příbuzný Rudolfovy matky Marie Weitzdörferové – vztah neprokázán.", r=["tepla_snatek_rudolf_winter_franziska_schwarz_1903"]),
    dict(k=1, n="Franz Robert Albin Eliáš (Elias) (* 1909)", t="Manžel Hildegardy, × 19. 5. 1932 Podmokly. Cukrář (Konditor), * 17. 7. 1909, příslušný do Podmokel, bytem Podmokly čp. 576 (1932); adresář 1934: „Elias Franz, Konditor, Bahnhofstraße 332“ – žil s Hildegard v domě cukrárny. Křest v matrice Altstadt sv. VII, fol. 145. Syn Franze Eliáše, ředitele továrny (Fabriksdirektor; adresář 1934 „Geschäftsführer, Schlachthofstraße 576“), a Anny Wilhelminy roz. Prantschové (?). Od 1941 úředně „Elias“.", r=["podmokly_snatek_franz_elias_hildegard_winter_1932"]),
    dict(k=1, n="Gerda Elias (* 1942)", t="Dcera Franze a Hildegardy (přípis v oddacím zápisu rodičů), označena jako „2.“ – zřejmě druhé dítě. Může žít – údaje jen základní.", r=["podmokly_snatek_franz_elias_hildegard_winter_1932"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kde leží „Parchau, Tepl“, rodiště Fanni Schwarzové?", "Vyřešeno: Prosau = Mrázov u Teplé, mlýn čp. 13 (sčítání 1921 a oddací zápis dcery 1932). Křest 25. 4. 1870 v matrice Prosau zatím nenalezen."),
    ("Jak se jmenoval manžel Hildegardy Winterové (Elias)?", "Vyřešeno: Franz Robert Albin Eliáš, cukrář, * 17. 7. 1909, sňatek 19. 5. 1932 v Podmoklech."),
    ("Kolik dětí měli Franz a Hildegard Eliášovi?", "Otevřené: přípis zmiňuje „2. Gerda Elias, * 19. 1. 1942“ – první dítě zatím neznámé."),
    ("Proč stojí na dopisním papíře z roku 1923 „Gegründet 1865“?", "Hypotéza: dům čp. 332 cukrárnou před 1910 nebyl (stavební spis), rok 1865 tedy patří firmě, ne domu. Při křtu 1874 byl kmotrem jmenovec Rudolf Winter, už tehdy cukrář v Bodenbachu – firmu mohl založit on a mladší Rudolf ji převzít. Ověřit v živnostenském rejstříku."),
    ("Co se stalo s Fanni a Hildegardou po roce 1945?", "Otevřené: online nic; Hildegardina živnost odhlášena 20. 11. 1942, příjmení poněmčeno 1941 (Eliáš → Elias). Nutný dotaz SOkA Děčín (MNV/ONV, národní správa, odsun) a v Německu (Heimatkartei)."),
    ("Kdy zemřela Franziska Winterová roz. Schwarzová?", "Otevřené: v únoru 1939 ještě žila a vlastnila dům čp. 332 (stavební spis); v Podmoklech do konce 1938 nezemřela."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
