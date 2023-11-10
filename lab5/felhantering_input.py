"""
Detta program hjälper dig att se till att all input som kommer in är av rett datatyp
Skriven av Jonatan Linn
Kurskod: DD1310
"""

def input_fullständigt_namn(inputtext):
    """Tar in texten som ska vara tillsammmans med inputen och
    retunerar lista med förnamnet sedan efternamner om de är 
    angivna på rätt sett. Alltså att det finns ett mellanslag 
    mellan namnen och det inte innehåller några andra tecken en bokstäver"""
    fel_inmatning = True
    while fel_inmatning:
        inputen = input(inputtext)
        inputen_uppdelad = inputen.split(" ")

        bara_bokstäver = True
        for namn in inputen_uppdelad:
            if not namn.isalpha():
                bara_bokstäver = False

        if inputen.count(" ") == 0: 
            print("Namnet måste skrivas in som 'förnamn' sen 'effternamn' med ett mellanslag mellan namnen")
        elif not bara_bokstäver:
            print("Namnet kan inte innehålla något annat än bokstäver")
        else:
            fel_inmatning = False
            return inputen.split(" ",1)

def input_siffervärden(input_text, antal_siffror = "ingen begränsning", variabelnamet = "Värdet"):
    """Tar in textten som man vill ha tillsammans med inputen och namnet på variabeln.
    Funktionen skickar sen tillbaka inputen om endast siffror av rett antal har matats in."""
    fel_inmatning = True
    while fel_inmatning:
        inputen = input(input_text)
        if not inputen.isnumeric():
            print(variabelnamet.capitalize(), "får bara innehålla siffror, försök igen!")
        elif antal_siffror != "ingen begränsning" and len(inputen) != antal_siffror:
            print(f"Mata in det {antal_siffror}-siffriga", variabelnamet)
        else:
            fel_inmatning = False
            return inputen
        