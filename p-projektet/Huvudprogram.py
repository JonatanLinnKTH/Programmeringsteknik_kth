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

from datetime import datetime
import felhantering_input

class Parkering:
    """Beskriver ett parkeringstillfälle"""
    def __init__(self, starttid, sluttid):
        """Skapar ett nytt objekt Parkering. Parametrar: 
            starttid (datetime)
            sluttid (datetime)"""
        self.starttid = starttid
        self.sluttid = sluttid

    def __str__(self):
        """Returnerar en sträng med värdena för objeket"""
        inpassage = self.starttid.strftime('%H:%M')
        utpassage = self.sluttid.strftime('%H:%M')
        return inpassage + "," + utpassage
    
    def visa_parkering(self):
        """Returnerar en sträng som beskriver objektet tydligt"""
        inpassage = self.starttid.strftime('%H:%M')
        utpassage = self.sluttid.strftime('%H:%M')
        return "Inpassage: " + inpassage + ", Utpassage: " + utpassage

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
        starttid = datetime.strptime(inpassage, "%H:%M")
        sluttid = datetime.strptime(utpassage, "%H:%M")
        parkering = Parkering(starttid,sluttid)
        self.parkeringslogg.append(parkering)

class Parkeringshus:
    """Bestkriver ett parkeringshus registrerad i systemet"""
    def __init__(self):
        """Skapar ett tomt bibkiotek där bilar kan läggas in"""
        self.bilar = {}
    
    def registrera_ny_bil(self):
        """Skapar en ny bil och sparar den i biblioteket bilar"""
        registreringsnummer = felhantering_input.är_ett_registreringsnummer("Vad är bilens registreringsnummer? ")
        ägare = input("Vad är namnet på bilens ägare? ")
        biltyp = input("Kategoriserars bilensom listen, mellan eller stor? ")
        self.bilar[registreringsnummer] = Bil(registreringsnummer, ägare, biltyp)

    def registrera_parkering(self):
        #Saknade felhantering av startiden är innan sluttiden
        """Hanterar registrering av inpassage och utpassage, genom att felhantera inputen och
        klassen Bil()"""
        frågetext = "Vad är registreringsnummret för bilen som har parkerat? "
        registreringsnummer = felhantering_input.finns_bilen(frågetext, self.bilar.keys())
        starttid = felhantering_input.rätt_tid("Ange tiden för inpassage: ")
        sluttid = felhantering_input.rätt_tid("Ange tiden för utpassage: ")
        self.bilar[registreringsnummer].ny_parkering(starttid,sluttid)

    def läs_in_registreringshistorik(self):
        """Läser in en fil med redan registreade bilar, genom att bl.a. använda 
        bil.nu_parkering()"""
        filnamn = "registrerade_bilar.txt"
        with open(filnamn,"r", encoding = "utf-8") as registrerade_bilar:
            rad = registrerade_bilar.readline().strip()
            while rad != "":
                rad_uppdelad = rad.split(",")
                self.bilar[rad_uppdelad[0]] = Bil(rad_uppdelad[0],rad_uppdelad[1],rad_uppdelad[2])
                rad = registrerade_bilar.readline().strip()

    def läs_in_parkeringshistorik(self):
        """Läser in en fil med redan registrerade in och utpassager, genom att bl.a. använda
        funketionen felhantering.finns_bilen() och bil.ny_parkering()"""
        filnamn = felhantering_input.finns_filen("Vad heter filen? ")
        with open(filnamn, "r", encoding = "utf-8") as historik:
            registreringsnummer = historik.readline().strip()
            while registreringsnummer != "":
                parkeringar = historik.readline().strip()[:-1] #[:-1] tar bort det sissta semikolonet
                parkeringar_uppdelad = parkeringar.split(";")
                for parkering in parkeringar_uppdelad:
                    [starttid, sluttid] = parkering.split(",")
                    self.bilar[registreringsnummer].ny_parkering(starttid,sluttid)
                registreringsnummer = historik.readline().strip()

    def visa_parkeringshistorik(self):
        """Hämtar information om när bilen kom till och lämnade parkeringshuset, retunerar 
        parkeringshistoriken som en sträng"""
        frågetext = "Vad är registreringsnummret för bilen som ska visas? "
        bil = felhantering_input.finns_bilen(frågetext, self.bilar.keys())
        bil_information = str(self.bilar[bil])
        parkeringslista = "\n"
        for parkering in self.bilar[bil].parkeringslogg:
            parkeringslista += parkering.visa_parkering() + "\n"
        return "\n" + bil_information + "\n" "Registrerade parkeringar: " + parkeringslista

    def räkna_ut_parkeringskostnad(self):
        """Räknar ut kundens skuld för en viss bil m.h.a. bilens storlek och att avrunda
        parkeringstiden till närmaste halvtimme, i detta fall är prissättningen följande stor bil 
        30 kr/h, mellanbil 25 kr/h, liten bil 20 kr/h"""
        kostnad_stor_bil = 30
        kostnad_mellan_bil = 25
        kostand_liten_bil = 20
        frågetext = "Vad är registreringsnummret för bilen som ska undersökas? "
        bil = felhantering_input.finns_bilen(frågetext, self.bilar.keys())
        total_parkerad_tid = 0
        for parkering in self.bilar[bil].parkeringslogg:
            parkeringstid = parkering.sluttid - parkering.starttid
            timmar, resten = divmod(parkeringstid.total_seconds(), 3600)
            minuter = resten / 60
            if minuter >= 45:
                timmar += 1
            elif minuter >= 15:
                timmar += 0.5
            total_parkerad_tid += timmar
        storlek = self.bilar[bil].biltyp
        if storlek == "stor":
            skuld = total_parkerad_tid * kostnad_stor_bil
        elif storlek == "mellan":
            skuld = total_parkerad_tid * kostnad_mellan_bil
        elif storlek == "liten":
            skuld = total_parkerad_tid * kostand_liten_bil
        else:
            print("Något är fel i registreringen av bilen i systemt, kontrollera att bilen")
            print("är regisrerad som anringen stor, mellan eller liten")
        return total_parkerad_tid, skuld

    def spara_parkeringhistorik(self):
        """Sparar alla bilars inpassager och utpassager på fil"""
        filnamn = "parkeringshistorik.txt"
        with open(filnamn, "w", encoding = "utf-8") as fil:
            for bil in self.bilar.values():
                fil.write(bil.registreringsnummer + "\n")
                for parkering in bil.parkeringslogg:
                    fil.write(str(parkering) + ";")
                fil.write("\n")

    def spara_bilinformation(self):
        """Sparar all information om själa bilen: registreringsnummer, ägare och biltyp, på fil"""
        filnamn = "registrerade_bilar.txt"
        with open(filnamn, "w", encoding="utf-8") as fil:
            for bil in self.bilar.values():
                fil.write(bil.registreringsnummer + ",")
                fil.write(bil.ägare + ",")
                fil.write(bil.biltyp + "\n")

def meny():
    """"Tar in användarens inmatning och returnerar menyvalet. Presenterar menyalternativen: 
            I Registrera parkering 
            F Läs in fil med parkeringshistorik 
            N Lägg till ny bil 
            P Räkna ut parkeringskostnad för en bil 
            V Visa parkeringshistorik för en bil 
            S Avsluta."""
    print("""
            -------Meny------
            I Registrera parkering 
            F Läs in fil med parkeringshistorik 
            N Lägg till ny bil 
            P Räkna ut parkeringskostnad för en bil 
            V Visa parkeringshistorik för en bil 
            S Avsluta.""")
    tillåtna_menyval = ["I","F","N","P","V","S"]
    menyval = felhantering_input.rätt_menyval("Välj ett av åvanstående alternativ: ", tillåtna_menyval)
    return menyval

def huvudprogram():
    """Presenterar användaren för programmet, laddar in de registrerade bilarna genom funktionen
    parkeringshus.läs_in_registreringshistorik(), startar menyfunktionen samt anropar funktioner 
    som motsvarar menyvalet"""
    parkeringshus = Parkeringshus()
    print("Välkommen till kundsystemet för parkeringshuset!")
    parkeringshus.läs_in_registreringshistorik()
    menyval = ""
    while menyval != "S":
        menyval = meny()
        if menyval == "I":
            print("\nRegistering av inpassage och utpassage")
            parkeringshus.registrera_parkering()
            print("\nParkering registerad!")
        elif menyval == "F":
            print("\nLäser in parkeringshistorik")
            parkeringshus.läs_in_parkeringshistorik()
            print("Inläsning färdig")
        elif menyval == "N":
            print("\nRegistrering av ny bil")
            parkeringshus.registrera_ny_bil()
            print("\nBilen registrerad!")
        elif menyval == "P":
            tid_parkerad,skuld = parkeringshus.räkna_ut_parkeringskostnad()
            print(f"Kunden har totalt parkerat {tid_parkerad} timmar i parkeringhuset")
            print(f"Kundens skulld är därför {skuld} kr")
        elif menyval == "V":
            print("\nTa fram parkeringshistoriken för en bil")
            historik = parkeringshus.visa_parkeringshistorik()
            print(historik)

        if menyval == "S":
            print("\nSparar all registrerad information om bilar")
            parkeringshus.spara_bilinformation()
            print("och parkeringar och avslutar programmet\n")
            parkeringshus.spara_parkeringhistorik()
        else:
            print()
            input("För att gå tillbaka till huvudmenyn klicka enter: ")

huvudprogram()
