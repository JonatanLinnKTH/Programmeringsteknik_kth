"""
Detta program räknar ut summan för en aritmetisk och geometrisk talföljd. 
Det hanterar även om man skriver in fel data till programmet
Skriven av Jonatan Linn
Kurskod: DD1310
"""

import skriven_input

def beräkna_aritmetisk_summa (första_elementet, differens, antal_tal):
    """Räknar ut summan av den aritmetiska talföljden givet värdet på första 
    elementet, differensen mellan elementen och antalet tal i talföljden"""

    sista_elementet = första_elementet + differens * (antal_tal - 1)
    return antal_tal * (första_elementet + sista_elementet) / 2

def beräkna_geometrisk_summa (första_elementet, kvot, antal_tal):
    """Räknar ut summan av den geometriska talföljden givet värdet på första 
    elementet, kvoten mellan elementen och antalet tal i talföljden"""

    return första_elementet * (kvot**antal_tal - 1) / (kvot - 1)

def vilken_summa_är_störst (aritmetisk, geometrisk):
    """Räknar ut vilken summa som är störst och skriver ut medelanden som svar"""

    if aritmetisk > geometrisk:
        print("Den aritmetiska summan är störst\n")
    elif aritmetisk < geometrisk:
        print("Den geometriska summan är störst\n")
    else:
        print("Summorna är lika\n")

def huvudprogram():
    """Hälsar välkommen till programmet och ställer ställer frågorna"""
    print("""Halloj och välkommen!
Med det här programmet kan du räkna vilken summa av de aritmetiska eller geometriska 
talföljderna som är störst""")

    print("\nData för den aritmetiska summan:")
    första_elementet_aritmetisk = skriven_input.input_float("Vad ska det första elementet i serien ha för värde? ", "Fösta elementet")
    differansen = skriven_input.input_float("Vad ska det vara för differens i talföljden? ","Differansen")

    print("\nData för den geometriska summan:")
    första_elementet_geometrisk = skriven_input.input_float("Var ska det första elemetet i serien ha för värde? ","Första elementet")
    kvoten = skriven_input.input_float("Vad är kvoten för talföljden? " ,"Kvoten", kan_inte_va_ett=True)

    antalet_tal = skriven_input.input_nat("\nVad är antalet termer i talföljderna? ","Antalet tal")

    aritmetisk_summa = beräkna_aritmetisk_summa(första_elementet_aritmetisk, differansen, antalet_tal)
    geometrisk_summa = beräkna_geometrisk_summa(första_elementet_geometrisk, kvoten, antalet_tal)
    vilken_summa_är_störst(aritmetisk_summa, geometrisk_summa)

if __name__ == "__main__":
    huvudprogram()
