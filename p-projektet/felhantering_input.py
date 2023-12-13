"""
Detta program hjälper dig att se till att all input som kommer in är av rett datatyp
Skriven av Jonatan Linn
Kurskod: DD1310
"""
def rätt_tid(inputtext):
    """Tar in texten som ska vara tillsammmans med inputen och retunerar en sträng om det är
    angivet på formen HH:MM, annars skriver ett felmedelande"""
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
            return inputen

def rätt_menyval(inputtext, meny_alternativ):
    """Tar in texten som ska vara tillsammans med inputen och retunerar menyvalet som en 
    sträng om den är angiven på rett sett, annars skriver ett felmedelande"""
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
        
def finns_filen(inputtext):
    """Tar in texten som ska vara tillsammans med inputen och retunerar filnamnet som en sträng om
    filen ligger i samma mapp, annars skrivet ett felmedelande"""
    fel_inmatning = True
    while fel_inmatning:
        try:
            inputen = input(inputtext)
            with open(inputen, "r", encoding="utf-8"):
                pass
            fel_inmatning = False
            return inputen
        except FileNotFoundError:
            print("Filnamnet finns inte, försök igen")

def är_ett_registreringsnummer(inputtext):
    """Tar in texten som ska vara tillsammans med inputen och retunerar registreringsnummret som en string om
    det är angivet på rett sätt"""
    fel_inmatning = True
    while fel_inmatning:
        inputen = input(inputtext)
        
        if len(inputen) != 6:
            print("Fel antal tecken. Registreringsnummret ska var 6 tecken långt på formen 'NNN000', skriv inte heller någon extra text")
        elif not inputen[0:3].isalpha() or not inputen[3:6].isdigit():
            print("Fel typ av tecken. Skriv endast in registreringsnummret på formen 'NNN000', ingen extra text")
        elif not inputen[0:3].isupper():
            print("Det bör vara stora bokstäver i registreringsnummret")
        else:
            fel_inmatning = False
            return inputen
        
def finns_bilen(inputtext, bilar_i_systemet):
    """Tar in texten som ska vata tillsammans med inputen samt vilka bilar som är registrerade i
    systemet och retunerar registreringsnummret som en string om den finns i systemet"""
    fel_inmatning = True
    while fel_inmatning:
        inputen = input(inputtext)
        if not inputen in bilar_i_systemet:
            print("Det registeringsnummret finns inte i systemet. Testa ett annat.")
        else:
            fel_inmatning = False
            return inputen