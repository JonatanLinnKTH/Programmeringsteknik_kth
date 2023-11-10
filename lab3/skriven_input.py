"""
Detta program hjälper dig att se till att all input som kommer in är av rett datatyp
Skriven av Jonatan Linn
Kurskod: DD1310
"""

def input_float(input_text, variabelnamn = "Den här variabeln", kan_inte_va_ett = False):
    """Tar in textten som man vill ha tillsammans med inputen och namnet på variabeln.
    Funktionen skickar sen tillbaka inputen om ett flyttal har angets. Det finns även möjligheter 
    att begrensa inputen till att inte kunna ha värdet ett"""
    fel_inmatning = True
    while fel_inmatning:
        try:
            inputen = float(input(input_text))
            if kan_inte_va_ett:
                if inputen == 1:
                    print(variabelnamn, "kan inte vara lika med ett, försök igen")
                else:
                    fel_inmatning = False
                    return inputen
            else:
                fel_inmatning = False
                return inputen
        except ValueError:
            print(variabelnamn, "måste vara ett flyttal, försök igen\n")

def input_int(input_text, variabelnamn = "Den här variabeln"):
    """Tar in textten som man vill ha tillsammans med inputen och namnet på variabeln.
    Funktionen skickar sen tillbaka inputen om ett heltal har angets."""
    fel_inmatning = True
    while fel_inmatning:
        try:
            inputen = int(input(input_text))
            fel_inmatning = False
            return inputen
        except ValueError:
            print(variabelnamn, "måste vara ett heltal, försök igen\n")

def input_nat(input_text, variabelnamn = "Den här variabeln"):
    """Tar in textten som man vill ha tillsammans med inputen och namnet på variabeln.
    Funktionen skickar sen tillbaka inputen om ett naturligt tal har angets."""
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

def huvudprogram():
    """Körs när man kör filen direkt, för att testa alla funktioner"""
    testvärde_float = input_float("Vad är flyttalet? ","Flytalet",False)
    testvärde_int = input_int("Vad är heltalet? ","Heltalet")
    testvärde_nat = input_nat("Vad är det naturliga talet? ","Det natruliga talet")
    print(f"Värdet du matade in för flyttal var {testvärde_float}")
    print(f"Värdet du matade in för heltal var {testvärde_int}")
    print(f"Värdet du matade in för det naturliga talet var {testvärde_nat}")

if __name__ == "__main__":
    huvudprogram()

