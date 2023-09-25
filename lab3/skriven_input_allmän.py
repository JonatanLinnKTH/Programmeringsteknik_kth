"""
Detta program hjälper dig att se till att all input som kommer in är av rett datatyp
Skriven av Jonatan Linn
Kurskod: DD1310
"""

def input_float(input_text, variabelnamn = "Den här variabeln"):
    """Tar in textten som man vill ha tillsammans med inputen
    och skickar tillbaka inputen om ett flyttal har angets"""
    fel_inmatning = True
    while fel_inmatning:
        try:
            inputen = float(input(input_text))
            fel_inmatning = False
            return inputen
        except ValueError:
            print(variabelnamn, "måste vara ett flyttal, försök igen\n")

'''
def input_int(input_text, variabelnamn = "Den här variabeln"):
    """Tar in textten som man vill ha tillsammans med inputen 
    och skickar tillbaka inputen om ett heltal har angets"""
    fel_inmatning = True
    while fel_inmatning:
        try:
            inputen = int(input(input_text))
            fel_inmatning = False
            return inputen
        except ValueError:
            print(variabelnamn, "måste vara ett heltal, försök igen\n")
'''
def input_nat(input_text, variabelnamn = "Den här variabeln"):
    """Tar in textten som man vill ha tillsammans med inputen 
    och skickar tillbaka inputen om ett naturligt tal har angets"""
    fel_inmatning = True
    while fel_inmatning:
        try:
            feltext = "måste vara ett heltal större än noll, försök igen\n"
            inputen = int(input(input_text))
            if inputen <= 0:
                print(variabelnamn, feltext)
            else:
                fel_inmatning = False
                return inputen
        except ValueError:
            print(variabelnamn, feltext)

def input_int(input_text, variabelnamn = "Den här variabeln ", jämförelse = "!", jämförelsesifra = " "):
    """Tar in texten som man vill ha tillsammans med inputen, variabelnamnet, samt vilket krav man 
    har på inmatningen (alltså på vilket sätt man ska jämföra det och med vad"""
    fel_inmatning = True
    while fel_inmatning:
        try:
            inputen = int(input(input_text))
            feltext = variabelnamn + "måste vara ett heltal " + jämförelse + " " + str(jämförelsesifra)
            inputen_kollad = kravställd_jämförelse(inputen, feltext, jämförelse, jämförelsesifra)
            return inputen_kollad

        except ValueError:
            print(feltext)
                    
"""Kommer inte fungera, behöver mer arbete!!!!"""

def kravställd_jämförelse(tal, feltext, jämförelse = "!!", kravsifra = " "):
    if jämförelse == "större än":
        if tal <= jämrörelsesifra:
            print(feltext)
        else:
            fel_inmatning = False
            return inputen
    elif jämförelse == "mindre än":
        if tal >= jämrörelsesifra:
            print(feltext)
        else:
            fel_inmatning = False
            return inputen
    elif tal == "inte lika med":
        if inputen == jämförelse:
            print(feltext)
        else:
            fel_inmatning = False
            return inputen
    else:
        fel_inmatning = False
        return inputen


def huvudprogram():
    """Körs när filen kör filen direkt"""
    # testvärde_float = input_float("Vad är flyttalet? ","Flytalet")
    testvärde_int = input_int("Vad är heltalet? ","Heltalet")
    # testvärde_nat = input_nat("Vad är det naturliga talet? ","Det natruliga talet")
    # testvärde_kravställd_int = input_krävställd_int("Vad är heltalet? ", jämförelse = "mindre än", jämrörelsesifra = 0)
    # testvärde_kravställd_int = input_krävställd_int("Vad är heltalet? ")
    # print(f"Värdet du matade in för flyttal var {testvärde_float}")
    print(f"Värdet du matade in för heltal var {testvärde_int}")
    # print(f"Värdet du matade in för det naturliga talet var {testvärde_nat}")
    # print(f"Värdet du matade in för heltal var {testvärde_kravställd_int}")



if __name__ == "__main__":
    huvudprogram()
