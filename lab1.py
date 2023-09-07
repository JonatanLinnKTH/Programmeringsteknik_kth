"""
Detta program räknar ut summan för en aritmetisk och geometrisk talföljd
Skriven av Jonatan Linn
Kurskod: DD1310
"""

print("Halloj! Här räknas summan för en aritmetisk och geometrisk talföljd ut!")

första_elementet = 1
antal_tal = 3
differensen = 2
kvoten = 3

print("I detta fall räknar vi ut den aritmetiska och geometriska summan för följade uppställning:")
print(f"Första elemetet i talföljden är: {första_elementet}")
print(f"Antal element är: {antal_tal}")
print(f"Differensen är: {differensen}")
print(f"och kvoten är: {kvoten}")

def beräkna_aritmetisk_summa (första_elementet, differensen, antal_tal):
    """Räknar ut summan av den aritmetiska talföljden givet värdet på första 
    elementet, differensen mellan elementen och antalet tal i talföljden"""
    sista_elementet = första_elementet + differensen * (antal_tal - 1)
    return antal_tal * (första_elementet + sista_elementet) / 2

def beräkna_geometrisk_summa (första_elementet, kvoten, antal_tal):
    """Räknar ut summan av den geometriska talföljden givet värdet på första 
    elementet, kvoten mellan elementen och antalet tal i talföljden"""
    return första_elementet * (kvoten**antal_tal - 1) / (kvoten - 1)



aritmetisk_summa = beräkna_aritmetisk_summa(första_elementet, differensen, antal_tal)
geometrisk_summa = beräkna_geometrisk_summa(första_elementet, kvoten, antal_tal)

print(f"Den aritmetiska summan är: {int(aritmetisk_summa)}")
print(f"Den geometriska summan är: {int(geometrisk_summa)}")
