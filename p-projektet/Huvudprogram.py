"""
Programmet ska hantera parkeringar för återkommande kunder till ett parkeringshus.
Det ska kunna registrera nya parkeringar, lägga in nya bilar i systemet och räkna 
ut kostnaden för den totala parkerade tiden för en viss bil med en viss storlek.
Programmet ska även kunna ta in parkeringshistorik från en tidigare sparad fil samt 
visa den parkeringshistorik som just då finns lagrad i programmet. Mellan
programkörningarna ska den inmatade informationen lagras på fil.
Skriven av Jonatan Linn
Kurskod: DD1310
"""

from datetime import time
import felhantering_input

class Parkering:
    """Beskriver ett parkeringstillfälle"""
    def __init__(self, starttid, sluttid):
        """Skapar ett nytt objekt Parkering. Parametrar: 
            starttid (time)
            sluttid (time)"""
        self.starttid = starttid
        self.sluttid = sluttid

    def __str__(self):
        """Returnerar en sträng som beskriver objektet"""
        return "Inpassage: " + str(self.starttid) + ", Utpassage: " + str(self.sluttid)

class Bil:
    """Beskriver en bil registrerad i systemet"""
    def __init__(self, registreringsnummer, ägare, biltyp):
        """Skapar ett nytt objekt Bil. Parametrar: 
            registreringsnummer (str) 
            ägare (str), 
            biltyp (str)"""
        self.registreringsnummer = registreringsnummer
        self.ägare = ägare
        self.biltyp = biltyp
        self.parkeringslogg = []
    
    def __str__(self):
        """Returnerar en sträng som beskriver objektet"""
        return ("Registreringsnummer: " + self.registreringsnummer + "\nÄgare: " + self.ägare
     + "\nBiltyp: " + self.biltyp)
    
    def ny_parkering(self, inpassage, utpassage):
        """Sparar ett nytt parkeringstillfälle till parkeringslogg"""
        parkering = Parkering(time(inpassage[0],inpassage[1]),time(utpassage[0],utpassage[1]))
        self.parkeringslogg.append(parkering)

    def ta_fram_parkeringshistorik(self):
        """Retunerar en lista med alla loggade klockslag för inpassage och utpassage"""
        parkeringslista = "\n"
        for parkering in self.parkeringslogg:
            parkeringslista += str(parkering) + "\n"
        return "Registrerade parkeringar: " + parkeringslista

def testprogram_parkering():
    parkering_1 = Parkering(time(12, 30), time(14, 40))
    print(parkering_1)

def testprogram_Bil():
    bil_1 = Bil("QPR556", "Carl von Testperson", "liten")
    print("Registrering av ny parkering")
    starttid = felhantering_input.input_tid("Starttid för parkering")
    sluttid = felhantering_input.input_tid("Sluttid för parkering")
    bil_1.ny_parkering(starttid, sluttid)
    print(bil_1)

testprogram_Bil()

