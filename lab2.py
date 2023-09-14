"""
Detta program räknar ut summan för en aritmetisk och geometrisk talföljd. 
Det hanterar även om man skriver in fel data till programmet
Skriven av Jonatan Linn
Kurskod: DD1310
"""
def beräkna_aritmetisk_summa (första_elementet, differensen, antal_tal):
    """Räknar ut summan av den aritmetiska talföljden givet värdet på första 
    elementet, differensen mellan elementen och antalet tal i talföljden"""

    sista_elementet = första_elementet + differensen * (antal_tal - 1)
    return antal_tal * (första_elementet + sista_elementet) / 2

def beräkna_geometrisk_summa (första_elementet, kvoten, antal_tal):
    """Räknar ut summan av den geometriska talföljden givet värdet på första 
    elementet, kvoten mellan elementen och antalet tal i talföljden"""

    return första_elementet * (kvoten**antal_tal - 1) / (kvoten - 1)

def vilken_summa_är_störst (aritmetisk, geometrisk):
    """Räknar ut vilken summa som är störst och skriver ut medelanden som svar"""

    if aritmetisk > geometrisk:
        print("Den aritmetiska summan är störst")
    elif aritmetisk < geometrisk:
        print("Den geometriska summan är störst")
    else:
        print("Summorna är lika")

print("""
Halloj och välkommen! Med det här programmet kan du räkna vilken summa av de aritmetiska eller 
geometriska talföljderna som är störst
      """)


"""Fel att hålla reda på:
* Matar in en string i första fyra inmatningarna 
* Matar in string eller float i antal tal
* Matar in en inkompatibel kvot
"""

inte_rätt = True
while inte_rätt:
    try:
        print("Data för den aritmetiska summan:")
        första_elementet_aritmetisk = float(input("Vad ska det första elementet i serien ha för värde? "))
        differensen =  float(input("Vad ska det vara för differens i talföljden? "))

        print("\nData för den geometriska summan:")
        första_elementet_geometrisk = float(input("Vad ska det första elementet i serien ha för värde? "))
        kvoten = float(input("Vad ska det vara för kvot i talföljden? "))
        if kvoten == 1:
            print("\nKvoten kan inte vara lika med 1\n")
        else:
            inte_rätt = False

    except ValueError:
        print("\nDet där var inte ett flyttal, försök igen.\n")

inte_rätt = True
while inte_rätt:
    try:
        antal_tal = int(input("\nVad är antalet termer i summorna? "))
        inte_rätt = False

    except ValueError:
        print("\nDet där var inte ett heltal, försök igen.")

aritmetisk_summa = beräkna_aritmetisk_summa(första_elementet_aritmetisk, differensen, antal_tal)
geometrisk_summa = beräkna_geometrisk_summa(första_elementet_geometrisk, kvoten, antal_tal)

print(f"\nDen aritmetiska summan är: {int(aritmetisk_summa)}") # ta bort detta
print(f"Den geometriska summan är: {int(geometrisk_summa)}\n") # ta bort detta

vilken_summa_är_störst(aritmetisk_summa, geometrisk_summa)
