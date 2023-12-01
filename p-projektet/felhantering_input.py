"""
Detta program hjälper dig att se till att all input som kommer in är av rett datatyp
Skriven av Jonatan Linn
Kurskod: DD1310
"""
def tid(inputtext):
    """Tar in texten som ska vara tillsammmans med inputen och retunerar lista med 
    timmar sedan minuter om det är angivet på formen HH:MM, annars skriver ett felmedelande"""
    fel_inmatning = True
    while fel_inmatning:
        inputen = input(inputtext)
        inputen_uppdelad = inputen.split(":")

        bara_siffror = True
        for tal in inputen_uppdelad:
            if not tal.isdigit:
                bara_siffror = False

        if inputen.count(":") != 1:
            print("Skriv in tiden med ett kolon ':' på formen HH:MM")
        elif len(inputen) != 5:
            print("Fel antal tecken. Skriv endast in tiden på formen HH:MM, ingen extra text")
        elif not bara_siffror:
            print("Fel typ av tecken. Skriv endast in tiden på formen HH:MM, ingen extra text")
        else:
            fel_inmatning = False
            utdata = [int(i) for i in inputen_uppdelad]
            return utdata

def menyval(inputtext, meny_alternativ):
    """Tar in texten som ska vara tillsammans med inputen och retunerar menyvalet som ett string om
    den är angiven på rett sett, annars slrover ett felmedelande"""
    fel_inmatning = True
    while fel_inmatning:
        inputen = input(inputtext)
        inputen = inputen.capitalize()

        alternativ_finns = False
        for alternativ in meny_alternativ:
            if alternativ == inputen:
                alternativ_finns = True
        
        if len(inputen) != 1:
            print("Skriv endast menyvalet som en bokstav")
        elif not alternativ_finns:
            print("Det där är inte ett möjligt mynyval")
        else:
            fel_inmatning = False
            return inputen
        