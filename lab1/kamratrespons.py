# Anonym 1
"""Här är ett pogram räknar utt den aretmatiska och geometriska summan av de
värdena som anges.
kod skriven av: David Bollö
Datum: 2023-09-07
Uppgift i programeringskurt Lab 1
Labgrupp 69
"""
def aretmetisk_summa(start_världe, diferans, antal_värden):
    """Räknar utt den aresmetiska talsumman givet världen: startvärlde, diferans
    mellan varjer steg och antal steg"""
   
    slut_värde = start_världe + diferans * (antal_värden - 1) #räknar utt slutvärdet.
    aretmetisk_summa = antal_värden * ((start_världe + slut_värde) /2) #räknar utt dne aretmetiska summan med angivna värden.
    return aretmetisk_summa

def geometrisk_summa(start_värde, kvot, antal_termer):
    """Räknar utt den geometriska talsumman givet världen: startvärde, kvot och
    antal termer"""

    if kvot == 1: #om kvoten är 1 pogramet att försöka dela med 0 på rad 23 vilket inte går. alltså är ett värde på 1 i kvor odefinerat
        return "odefinerat"
    else:
        geometrisk_summa = start_värde*(((kvot**antal_termer) - 1)/(kvot - 1))
        #räkanr utt den geometriska summan med angivna värden.
        return geometrisk_summa

""" här frågar pogramet om värdena för att räkna utt suman av den aretmetiska
talföljden"""

print("Nu kommer du att frågas att matta in värden för att räkna utt summan av en aretmetisk talföljd.")

start_världe = float(input("Skriv in startvärdet: "))
diferans = float(input("Skriv in differensen: "))
antal_värden = int(input("Skriv in antal element i följden: "))

aretmetisk_summa = aretmetisk_summa(start_världe, diferans, antal_värden)

print("Den aretmetiska summan är:", aretmetisk_summa) #Matar utt vad den aretmetiska summan är till användaren.

""" här frågar pogramet om värdena för att räkna utt summan av den geometriska
talföljden"""

print("Nu kommer du att frågas att matta in värden för att räkna utt summan av en aretmetisk talföljd.")

start_världe = float(input("Skriv in startvärdet: "))
kvot = float(input("Skriv in kvot: "))
antal_termer = int(input("Skriv in antal element i följden: "))

geometrisk_summa = geometrisk_summa(start_världe, kvot, antal_termer) #räknar utt talfölsden med angivna världen.
print("Den geometriska summan är:", geometrisk_summa) #Skriver utt den geometriska talföljden.
