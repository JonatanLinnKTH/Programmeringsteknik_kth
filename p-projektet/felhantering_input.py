"""
Detta program hjälper dig att se till att all input som kommer in är av rett datatyp
Skriven av Jonatan Linn
Kurskod: DD1310
"""
def input_tid(inputtext):
    """Tar in texten som ska vara tillsammmans med inputen och retunerar lista med 
    timmar sedan minuter om det är angivet på formen HH:MM, annars skrivet ett felmedelande"""
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
        elif not bara_siffror:
            print("Skriv endast in tiden på formen HH:MM, ingen extra text")
        else:
            fel_inmatning = False
            utdata = [int(i) for i in inputen_uppdelad]
            return utdata
       