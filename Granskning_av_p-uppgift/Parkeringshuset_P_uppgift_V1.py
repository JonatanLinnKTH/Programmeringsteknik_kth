import felhantering_P_huset as fh

class bil:
    def __init__(self, reg_nr, biltyp, namn):
        """Skapar ett objekt med attributen reg_nr, biltyp och namn"""
        self.reg_nr = reg_nr
        self.biltyp = biltyp
        self.namn = namn

    @property
    def __str__(self):
        """Returnerar bilen som en sträng"""
        return self.reg_nr + " " + str(self.biltyp) + " " + self.namn + "\n"


class Bilar:
    def __init__(self):
        """Läser av filen bilar och skapar en lista"""
        self.bilar = []
        with open("bilar.txt", 'r') as fil:
            self.fil = fil.readlines()

        for rad in self.fil:  # Loopar koden tills alla rader har lästs
            if rad == "":  # Om en rad är tom så avslutas loopen
                break
            reg_nr = rad[0:6]
            storlek = rad[7:8]
            namn = rad[9:]

            if fh.felInläsningBilar(rad):
                self.bilar.append(reg_nr + " " + storlek + " " + namn )
            else:
                print("Fel format i bilar filen på raden:")
                print(rad)

    def nyBil(self):
        """Skapar en ny bil m.h.a klassen bil och lägger till den i listan bilar"""
        reg_nr = fh.felReg_nr("Skriv in registeringsnummer: ")
        biltyp = fh.felBiltyp("Skriv in biltyp (1 liten, 2 mellan, 3 stor):  ")
        namn = input("Skriv in namn: ")
        bilen = bil(reg_nr, biltyp, namn)
        self.bilar.append(bilen.__str__)

    def finnsRegnr(self, regnr):
        """Kollar om indatan regnr finns i listan bilar"""
        if self.bilar.__str__().find(regnr) != -1 and len(regnr) == 6:
            return True
        else:
            return False

    def vilkenTimkostnad(self, regnr):
        """Kollar vilket timpris en bil har utifrån dess regnr"""
        pris = 0

        for rad in self.bilar:
            if rad.find(regnr) != -1:
                storlek = int(rad[7:8])

        if storlek == 1:
            pris += 20
        if storlek == 2:
            pris += 25
        if storlek == 3:
            pris += 30

        return pris

    def avsluta(self):
        """Sparar listan bilar till den specifika filen"""
        with open("bilar.txt", 'w') as fil:
            fil.writelines(self.bilar)

    def __str__(self):
        """Skriver ut bilarna"""
        bilarna = ""
        for rad in self.bilar:
            bilarna += rad
        return bilarna


class Tider:
    def __init__(self):
        """Läser av filen med in och utdata och skapar en lista utifrån den"""
        #self.tider = []
        with open("inutpassage.txt", 'r') as filen:
            self.tider = filen.readlines()

        for rad in self.tider:  # Loopar koden tills alla rader har lästs
            if rad == "":  # Om en rad är tom så avslutas loopen
                break

            reg_nr = rad[0:6]
            starttid = rad[7:12]
            sluttid = rad[13:18]
            datum = rad[19:]
            
            """if fh.felInläsningBilar(rad):
                self.tider.append(reg_nr + " " + starttid + " " + sluttid + " " + datum)
            else:
                print("Fel format på raden:")
                print(rad)"""

            if fh.felInläsningInUtPassage(rad) == False:
                #self.tider.append(reg_nr + " " + starttid + " " + sluttid + " " + datum)
                self.tider.remove(rad)
                print("Fel format i inutpassagefilen på raden:")
                print(rad)
            
            
    def inutpassage(self):
        """Ber användaren om tider och lägger de i listan"""
        check = 0

        datum = fh.felDatum()

        while True:
            print("Ange registeringsnummer:")
            registeringsnummer = input(">>> ")
            if bilarA.finnsRegnr(registeringsnummer):
                check += 1

            if check == 1:
                print("Ange tid som hh:mm")
                starttid = fh.felTid("Ange starttid:")
                sluttid = fh.felTid("Ange sluttid:")

                self.tider.append(registeringsnummer + " " + starttid + " " + sluttid + " " + datum + "\n")


                print("OK!")
                break
            else:
                print("Hittar inte registeringsnummret")


    def parkeringshistorik(self):
        """Skriver ut parkeringshistoriken för ett visst regnr"""
        checkRegnr = 0

        while True:

            print("Ange registeringsnummer:")
            registeringsnummer = input(">>> ")
            if bilarA.finnsRegnr(registeringsnummer):
                checkRegnr += 1
            else:
                print("Hittar inte registeringsnummret")

            if checkRegnr == 1:
                print("Start Slut Datum")
                print("Tid   Tid")
                for rad in self.tider:
                    if rad.find(registeringsnummer) != -1:
                        print(rad[7:27])
                break

    def parkeringskostnad(self):
        """Beräknar parkeringskostnaden för ett visst regnr"""
        checkRegnr = 0

        kostnad = 0

        while True:

            print("Ange registeringsnummer:")
            registeringsnummer = input(">>> ")

            if bilarA.finnsRegnr(registeringsnummer):
                checkRegnr += 1

            if checkRegnr == 1:
                timpris =0
                for rad in self.tider:
                    if rad.find(registeringsnummer) != -1:
                        timpris = bilarA.vilkenTimkostnad(registeringsnummer)
                        timmar = int(rad[13:15]) - int(rad[7:9])
                        kostnad += timmar * timpris  # Vilken bilstorlek?
                        halvtimme = int(rad[16:18]) - int(rad[10:12])
                        if halvtimme > 15 & halvtimme < 30:
                            kostnad += timpris / 2
                        if halvtimme > 30:
                            kostnad += timpris

                print("Parkeringskostnaden för din bil är " + str(kostnad) + " kr (" + str(timpris) + " kr/h)")
                break

            else:
                print("Hittar inte registeringsnummret")

        return kostnad

    def läsFil(self):
        """Läser in en fil och lägger till informationen i programmets fil"""
        print("Hämta data från fil")
        print("Ange filnamn", end=" ")
        while True:  # Loopar koden till användaren matar in en fil som finns
            try:  # Försöker att öppna filen med det namn som användaren matar in
                filnamn = input()
                with open(filnamn, 'r') as filen:
                    fil = filen.readlines()
                break
            except:  # Om filen inte hittas skrivs detta ut
                print("Den filen fanns inte! Skriv in en ny fil", end=" ")

        for rad in fil:  # Loopar koden tills alla rader har lästs
            if rad == "":  # Om en rad är tom så avslutas loopen
                break
            reg_nr = rad[0:6]
            starttid = rad[7:12]
            sluttid = rad[13:18]
            datum = rad[19:]
            print(rad.strip())

            if fh.felInläsningBilar(rad):
                self.tider.append(reg_nr + " " + starttid + " " + sluttid + " " + datum)
            else:
                print("Fel format på raden:")
                print(rad)

    def betalaSkuld(self):
        """Funktionen förflyttar alla in och utpassager till filen betaldaskulder och ber användaren att betala skulden"""
        check=False
        kostnad = 0
        regnr = fh.felReg_nr("Skriv in regnr för att betala skuld ")

        for rad in self.tider:
            if rad.find(regnr) != -1:
                timpris = bilarA.vilkenTimkostnad(regnr)
                timmar = int(rad[13:15]) - int(rad[7:9])
                kostnad += timmar * timpris  # Vilken bilstorlek?
                halvtimme = int(rad[16:18]) - int(rad[10:12])
                if halvtimme > 15 & halvtimme < 30:
                    kostnad += timpris / 2
                if halvtimme > 30:
                    kostnad += timpris
                check = True

        if check == True:
            print("Parkeringskostnaden för din bil är " + str(kostnad) + " kr (" + str(timpris) + " kr/h)")
            print("Din skuld är nu betald")

            with open("betaldaSkulder.txt", 'a') as fil:
                fil.write("\n")
                for rad in self.tider [:]:
                    if rad.find(regnr) != -1:
                        fil.write(rad)
                        self.tider.remove(rad)

        else:
            print("Hittar inte bilen försök igen")

    def avsluta(self):
        """Sparar listan i filen"""
        with open("inutpassage.txt", 'w') as fil:
            fil.writelines(self.tider)

    def __str__(self):
        """Skriver ut alla tider"""
        tider = ""
        for rad in self.tider:
            tider += rad
        return tider

def meny():
    """Skriver ut menyn"""
    print("     I   Inpassage/Utpassage")
    print("     F   Läs in fil med historik")
    print("     N   Lägg till ny bil")
    print("     P   Beräkna parkeringskostnad")
    print("     V   Visa parkeringshistorik")
    print("     B   Betala skuld")
    print("     S   Avsluta")

def användarval():
    """Funktionen användarval skriver ut alla alternativ och låter användaren göra ett val"""
    print("Välkommen till parkeringshuset")
    while True:
        meny()
        val = (input(">>> ")).upper() # Gör användarens inmatning versal

        if val == "I":
            tiderA.inutpassage()
        elif val == "F":
            tiderA.läsFil()
        elif val == "N":
            bilarA.nyBil()
        elif val == "P":
            tiderA.parkeringskostnad()
        elif val == "V":
            tiderA.parkeringshistorik()
        elif val == "B":
            print("Betala skuld")
            tiderA.betalaSkuld()
        elif val == "S": #Avsluta funktionerna sparar listorna på varin fil och sen stängs programmet ned
            bilarA.avsluta()
            tiderA.avsluta()
            exit()
        else:
            print("Fel, försök igen")

bilarA = Bilar()
tiderA = Tider()
användarval()