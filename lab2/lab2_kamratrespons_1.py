"""Nellie Rosén, Elina Ek, Helena Salwén
2023-09-13
DD1310: Labb2"""

import sys

print("Välkommen till vårt program")

def inmatning_av_flyttal(inmatning):
    """ Felhantering av inmatningen av flyttal"""
    try:
        inmatning = float(input(inmatning))
        return inmatning
    except ValueError:
        print("Det där var inget flyttal. Starta om programmet och försök igen.")
        sys.exit()
        
def inmatning_av_heltal(inmatning):
    """Felhantering av inmatningen av heltal"""
    try:
        inmatning = int(input(inmatning))
        return inmatning
    except ValueError:
        print("Det där var inget heltal. Starta om programmet och försök igen.")
        sys.exit()

print("Data för den aritmetriska summan:")
första_element_a1 = inmatning_av_flyttal("Skriv in startvärdet: ")
differens_d = inmatning_av_flyttal("skriv in differensen: ")

print("Data för den geometriska summan:")
första_element_g1 = inmatning_av_flyttal("Skriv in startvärdet: ")
kvot_q = inmatning_av_flyttal("skriv in kvoten: ")

print("Antal termer i summorna:")
antal_element_n = inmatning_av_heltal("skriv in antal element i följden: ")

def beräkna_aritmetrisk_summa(första_element, antal_element, differens):
    """Beräknar den aritmetriska summan av två tal"""
    aritmetrisk_summa = antal_element * ((första_element + (första_element + differens * (antal_element - 1))) / 2)
    return aritmetrisk_summa

def beräkna_geometrisk_summa(första_element, antal_element, kvot):
    """Beräknar den geometriska summan av två tal med en viss kvot"""
    try:
        geometrisk_summa = första_element*(((kvot**antal_element) - 1)/(kvot - 1))
        return geometrisk_summa
    except ZeroDivisionError:
        print("Nämnaren i geometriska summan är odefinierad då kvoten = 1. Jämförelse kan inte göras. Försök igen!")
        sys.exit()

def jämföra_summorna():
    aritmetrisk_summa = beräkna_aritmetrisk_summa(första_element_a1, antal_element_n, differens_d)
    geometrisk_summa = beräkna_geometrisk_summa(första_element_g1, antal_element_n, kvot_q)
    if aritmetrisk_summa < geometrisk_summa:
        print("Den geometriska summan är störst.")
    elif geometrisk_summa < aritmetrisk_summa:
        print("Den aritmetriska summan är störst.")
    else:
        print("De två summorna är lika stora.")

jämföra_summorna()
