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
        inpassage = self.starttid.strftime('%H:%M')
        utpassage = self.sluttid.strftime('%H:%M')
        return "Inpassage: " + str(inpassage) + ", Utpassage: " + str(utpassage)

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
        inpassage_int = [int(i) for i in inpassage]
        utpassage_int = [int(i) for i in utpassage]
        parkering = Parkering(time(inpassage_int[0],inpassage_int[1]),time(utpassage_int[0],utpassage_int[1]))
        self.parkeringslogg.append(parkering)

    def ta_fram_parkeringshistorik(self):
        """Retunerar en lista med alla loggade klockslag för inpassage och utpassage"""
        parkeringslista = "\n"
        for parkering in self.parkeringslogg:
            parkeringslista += str(parkering) + "\n"
        return "Registrerade parkeringar: " + parkeringslista

class Parkeringshus:
    """Bestkriver ett parkeringshus registrerad i systemet"""
    def __init__(self):
        """Skapar ett tomt bibkiotek där bilar kan läggas in"""
        self.bilar = {}
    
    def finns_bilen(self, registreringsnummer):
        """Kontrollerar om bilen finns i biblioteket bilar"""
    
    def registrera_ny_bil(self):
        """Skapar en ny bil och sparar den i biblioteket bilar"""
        print("\nRegistrering av ny bil")
        registreringsnummer = input("Vad är bilens registreringsnummer? ")
        ägare = input("Vad är namnet på bilens ägare? ")
        biltyp = input("Kategoriserars bilensom listen, mellan eller stor? ")
        self.bilar[registreringsnummer] = Bil(registreringsnummer, ägare, biltyp)
        print("\nBilen registrerad!")

    def registrera_parkering(self):
        """Hanterar registrering av inpassage och utpassae, genom att bl.a. använda metoderna
        self.finns_bilen och Bil()"""
        print("\nRegistering av inpassage och utpassage")
        registreringsnummer = input("Ange registeringsnummer")
        starttid = felhantering_input.rätt_tid("Ange tide för inpassage: ")
        sluttid = felhantering_input.rätt_tid("Ange tiden för utpassage: ")
        self.bilar[registreringsnummer].ny_parkering(starttid,sluttid)
        print("\nParkering registerad!")

    def läs_in_registreringshistorik(self):
        """Läser in en fil med redan registreade bilar, genom att bl.a. använda 
        bil.nu_parkering()"""
        print("\nLäser in pareringshistorik")
        filnamn = "registrerade_bilar.txt"
        with open(filnamn,"r", encoding = "utf-8") as registrerade_bilar:
            rad = registrerade_bilar.readline().strip()
            while rad != "":
                rad_uppdelad = rad.split(",")
                self.bilar[rad_uppdelad[0]] = Bil(rad_uppdelad[0],rad_uppdelad[1],rad_uppdelad[2])
                rad = registrerade_bilar.readline().strip()
        print("\nParkeringshistrorik registrerad")

    def räkna_ut_parkeringskostnad(self):
        """Räknar ut kundens skuld för en viss bil m.h.a. bilens storlek och att avrunda
        parkeringstiden till närmaste halvtimme samt genom att använda metoden
        bil.ta_fram_parkeringshistorik()"""
    
    def läs_in_parkeringshistorik(self):
        """Läser in en fil med redan registrerade in och utpassager, genom att bl.a. använda 
        metoderna self.finns_bilen och bil.ny_parkering()"""
        filnamn = felhantering_input.finns_filen("Vad heter filen? ")
        with open(filnamn, "r", encoding = "utf-8") as historik:
            reggistreringsnummer = historik.readline().strip()
            while reggistreringsnummer != "":
                parkeringar = historik.readline().strip()
                parkeringar_uppdelad = parkeringar.split(";")
                for parkering in parkeringar_uppdelad:
                    [starttid, sluttid] = parkering.split(",")
                    starttid_uppdelad = starttid.split(":")
                    sluttid_uppdelad = sluttid.split(":")
                    self.bilar[reggistreringsnummer].ny_parkering(starttid_uppdelad,sluttid_uppdelad)
                reggistreringsnummer = historik.readline().strip()

    def visa_parkeringshistorik(self):
        """Hanterar utskriften av information om när bilen kom till och lämnade parkeringshuset
        genom att använd medoden bil.ta_fram_parkeringshistorik"""
        bil = input("\nVilken bil vill du kolla upp?")
        print(self.bilar[bil].ta_fram_parkeringshistorik())

    def spara_parkeringhistorik(self):
        """Sparar alla bilars inpassager och utpassager på fil"""

    def spara_bilinformation(self):
        """Sparar all information om själa bilen: registreringsnummer, ägare och biltyp, på fil"""

def meny():
    """"Tar in användarens inmatning och returnerar menyvalet. Presenterar menyalternativen: 
            I Registrara parking 
            F Läs in fil med historik 
            N Lägg till ny bil 
            P Räkna ut parkeringskostnad för en bil 
            V Visa parkeringshistorik för en bil 
            S Avsluta."""
    print("""
            -------Meny------
            I Registrara parking 
            F Läs in fil med historik 
            N Lägg till ny bil 
            P Räkna ut parkeringskostnad för en bil 
            V Visa parkeringshistorik för en bil 
            S Avsluta.""")
    menyval = felhantering_input.rätt_menyval("Välj ett av åvanstående alternativ: ", ["I","F","N","P","V","S"])
    return menyval

def huvudprogram():
    """Presenterar användaren för programmet, startar menyfunktionen samt anropar funktioner 
    som motsvarar menyvalet"""
    parkeringshus = Parkeringshus()
    print("Välkommen till kundsystemet för parkeringshuset!")
    parkeringshus.läs_in_registreringshistorik()
    menyval = "Start"
    while menyval != "S":
        menyval = meny()
        tillbakatext = "Går tillbaka till menyn"
        if menyval == "I":
            parkeringshus.registrera_parkering()
            print(tillbakatext)
        elif menyval == "F":
            parkeringshus.läs_in_parkeringshistorik()
            print(tillbakatext)
        elif menyval == "N":
            parkeringshus.registrera_ny_bil()
            print(tillbakatext)
        elif menyval == "P":
            parkeringshus.räkna_ut_parkeringskostnad()
            print(tillbakatext)
        elif menyval == "V":
            parkeringshus.visa_parkeringshistorik()
            print(tillbakatext)
        else:
            print("\nSparar all registrerad information om bilar och parkeringar och")
            print("avslutar programmet\n")


def testprogram_parkering():
    parkering_1 = Parkering(time(12, 30), time(14, 40))
    print(parkering_1)

def testprogram_Bil():
    bil_1 = Bil("QPR556", "Carl von Testperson", "liten")
    print("Registrering av ny parkering")
    starttid = felhantering_input.rätt_tid("Starttid för parkering")
    sluttid = felhantering_input.rätt_tid("Sluttid för parkering")
    bil_1.ny_parkering(starttid, sluttid)
    print(bil_1)

huvudprogram()

#testprogram_Bil()

