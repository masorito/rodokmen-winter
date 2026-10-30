import sys
S = {  # zdroje
 "S1": "SOA Litoměřice, Sbírka matrik, N Prunéřov 1852–1878, sign. L123/6, sn. 140",
 "S2": "SOA Litoměřice, Sbírka matrik, N O Z Prunéřov 1852–1881, sign. L123/8, sn. 39",
 "S3": "SOA Plzeň, Porta fontium, O Teplá-město 1873–1907 (tepla-mesto-34), sn. 163, fol. 160",
 "S4": "SOkA Děčín, NAD 804 Sčítání 1921, Podmokly čp. 301–370, sn. 140",
 "S5": "SOkA Děčín, NAD 962 OÚ Děčín, Rejstřík živností 1895–1924 (inv. č. 4), sn. 80, č. 92",
 "S6": "SOA Litoměřice, Sbírka matrik, Z Podmokly 1900–1938, sign. 133/132, sn. 218, pag. 427",
 "S7": "SOA Litoměřice, Sbírka matrik, O Podmokly 1926–1934, sign. 133/123, sn. 223, fol. 220, č. 21",
 "S8": "SOkA Děčín, NAD 962 OÚ Děčín, Rejstřík živností (inv. č. 15), sn. 29, č. 119",
}
I = {}  # id: (jméno, příjmení, pohlaví, [(tag, datum, místo, zdroj, pozn)], fams, famc)
def ind(i, given, sur, sex, ev, note=None): I[i] = dict(g=given, s=sur, sex=sex, ev=ev, note=note)
ind("I1","Hildegard","Winter","F",[("BIRT","14 JUN 1909","Bodenbach (Podmokly), Böhmen","S7",None),("OCCU",None,None,"S8","Konditorin (cukrářka), Gewerbe Podmokly čp. 332 1934–1942")],"Po 1941 úředně Elias. Úmrtí neznámé.")
ind("I2","Rudolf","Winter","M",[("BIRT","15 MAY 1874","Brunnersdorf (Prunéřov) čp. 119, Böhmen","S1",None),("OCCU",None,None,"S5","Konditor; živnost Bodenbach čp. 337 od 4. 3. 1903"),("DEAT","9 AUG 1926","Bodenbach čp. 332","S6","Herzklappenfehler"),("BURI","12 AUG 1926","Bodenbach","S6",None)])
ind("I3","Franziska (Fanni)","Schwarz","F",[("BIRT","ABT 1878","Prosauer Mühle čp. 13, Prosau (Mrázov), Bez. Tepl","S3","24 let 1903; sčítání 1921: 25. 4. 187?")],"Úmrtí po 1938 neznámé.")
ind("I4","Josef","Winter","M",[("BIRT","ABT 1836","Brunnersdorf","S2",None),("OCCU",None,None,"S2","Schuhmachermeister, Brunnersdorf čp. 119")])
ind("I5","Marie","Weitzdörfer","F",[("BIRT","ABT 1842","Brunnersdorf čp. 34","S2",None)])
ind("I6","Johann Nepomuk","Schwarz","M",[("OCCU",None,None,"S3","Müllermeister, Prosauer Mühle čp. 13")])
ind("I7","Aloisia","Wollrab","F",[("RESI",None,"Tepl čp. 28","S3",None)])
ind("I8","Anton","Winter","M",[("OCCU",None,None,"S2","Schuhmachermeister, Brunnersdorf čp. 119"),("DEAT","BEF 13 NOV 1871",None,"S2",None)])
ind("I9","Johanna","Kunz","F",[("DEAT","BEF 13 NOV 1871",None,"S2","rodné příjmení nejisté (Kunz/Kurz)")])
ind("I10","Wenzel","Weitzdörfer","M",[("OCCU",None,None,"S2","Landwirt, Brunnersdorf čp. 34"),("DEAT","BEF 13 NOV 1871",None,"S2",None)])
ind("I11","Katharina","Gschale","F",[],"rodné příjmení nejisté (Gschale/Gschafe)")
ind("I12","Franz Robert Albin","Eliáš","M",[("BIRT","17 JUL 1909","Bodenbach","S7",None),("OCCU",None,None,"S7","Konditor")],"Od 1941 úředně Elias.")
ind("I13","Franz","Eliáš","M",[("OCCU",None,None,"S7","Fabriksdirektor, Bodenbach čp. 576")])
ind("I14","Anna Wilhelmine","Prantsch","F",[],"rodné příjmení čteno nejistě")
ind("I15","Gerda","Elias","F",[("BIRT","19 JAN 1942",None,"S7","přípis v oddacím zápisu rodičů")])
F = [("F1","I4","I5","13 NOV 1871","Brunnersdorf","S2",["I2"]),
     ("F2","I2","I3","8 JAN 1903","Tepl, Dekanalkirche St. Aegidius","S3",["I1"]),
     ("F3","I8","I9",None,None,None,["I4"]),("F4","I10","I11",None,None,None,["I5"]),
     ("F5","I6","I7",None,None,None,["I3"]),
     ("F6","I12","I1","19 MAY 1932","Bodenbach, Pfarrkirche","S7",["I15"]),
     ("F7","I13","I14",None,None,None,["I12"])]
o = ["0 HEAD","1 SOUR rodokmen-winter","1 GEDC","2 VERS 5.5.1","2 FORM LINEAGE-LINKED","1 CHAR UTF-8","1 NOTE Rodokmen Winterových – jen údaje doložené prameny (S1–S8)."]
fams = {}; famc = {}
for f,h,w,d,pl,src,ch in F:
    for x in (h,w): fams.setdefault(x,[]).append(f)
    for c in ch: famc[c]=f
for i,p in I.items():
    o += [f"0 @{i}@ INDI", f"1 NAME {p['g']} /{p['s']}/", f"1 SEX {p['sex']}"]
    for tag,d,pl,src,note in p["ev"]:
        if tag=="OCCU": o.append(f"1 OCCU {note}")
        else:
            o.append(f"1 {tag}")
            if d: o.append(f"2 DATE {d}")
            if pl: o.append(f"2 PLAC {pl}")
            if note: o.append(f"2 NOTE {note}")
        if src: o.append(f"2 SOUR @{src}@")
    if p["note"]: o.append(f"1 NOTE {p['note']}")
    for f in fams.get(i,[]): o.append(f"1 FAMS @{f}@")
    if i in famc: o.append(f"1 FAMC @{famc[i]}@")
for f,h,w,d,pl,src,ch in F:
    o += [f"0 @{f}@ FAM", f"1 HUSB @{h}@", f"1 WIFE @{w}@"]
    if d: o += ["1 MARR", f"2 DATE {d}", f"2 PLAC {pl}", f"2 SOUR @{src}@"]
    o += [f"1 CHIL @{c}@" for c in ch]
for k,v in S.items(): o += [f"0 @{k}@ SOUR", f"1 TITL {v}"]
o.append("0 TRLR")
open(sys.argv[1],"w",encoding="utf-8").write("\n".join(o)+"\n")
print(len(I),"osob,",len(F),"rodin")
