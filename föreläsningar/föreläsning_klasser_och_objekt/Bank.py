class Konto:
    """Beskriver ett konto, har attributen kontoinnehavare (str), kontonr (int), pin (int), saldo (float)"""

    def __init__(self, namn, nr, pin, saldo):
        """Konstruktorn som anropas när vi skapar ett nytt konto
        Parametrar: namn (str),nr (int), pin (int), saldo (float)
        """
        self.kontonr = nr # int
        self.saldo = saldo # float
        self.kontoinnehavare = namn # string
        self.pin = pin # int

    def __str__(self):
        """Returnerar: en sträng som beskriver objektet"""
        return self.kontoinnehavare + " har " + \
           str(self.saldo) + " på sitt konto " + str(self.kontonr)

    def ta_ut(self, belopp):
        """Tar ut pengar från kontot, ändrar saldo om det finns täckning på kontot.
        Parametrar: self och belopp (int)
        Returnerar: Inget
        """
        if self.saldo >= belopp:
            self.saldo = self.saldo - belopp
        else:
            print("Du har för lite pengar på kontot! Saldot är " + str(self.saldo))

    def __lt__(self, other):
        """För jämförelser mellan konton (används vid sortering). """
        if self.saldo < other.saldo:
            return True
        else:
            return False

    def satt_in(self, pengar):
        """Insättning på kontot
        Parametrar: self och pengar (int)
        Returnerar: inget
        """
        self.saldo += pengar


class Bank:

    def __init__(self):
        """ Skapar en tom lista där konton ska läggas in """
        self.konton = []

    def las_konton(self):
        """ Läser konton från filen konton.txt till attributet konton.
        Parametrar: self
        Returnerar: inget
        """
        fil = open("konton.txt", "r")
        namn = fil.readline().strip()
        while namn:
            nr = int(fil.readline().strip())
            pin = int(fil.readline().strip())
            saldo = float(fil.readline().strip())
            nytt = Konto(namn, nr, pin, saldo)
            self.konton.append(nytt)
            namn = fil.readline().strip()
        fil.close()

    def spara_konton(self):
        """Skriver ut (lagrar) alla konton på filen konton.txt
        Parametrar: self
        Returnerar: inget
        """
        fil = open("konton.txt", "w")
        self.konton.sort()
        for konto in self.konton:
            fil.write(konto.kontoinnehavare + "\n")
            fil.write(str(konto.kontonr) + "\n")
            fil.write(str(konto.pin) + "\n")
            fil.write(str(konto.saldo) + "\n")
        fil.close()

    def visa_alla(self):
        """Skriver ut information om alla konton i banken
        Parametrar: self
        Returnerar: inget
        """
        losen = input("Ge det hemliga lösenordet för personalen: ")
        if losen == "pengar":
           print("Dessa konton finns i banken, sorterade efter saldo:")
           self.konton.sort(reverse=True)
           for konto in self.konton:
               print(konto)
        else:
            print("Fel lösenord!")

    def nytt_konto(self):
        """ Ser till att nytt konto skapas och lägger till det i attributet konton
        Parametrar: self
        Returnerar: inget
        """
        namn = input("Namn:")
        pin = int(input("Pin:"))
        kontonr = self.konton[len(self.konton) - 1].kontonr + 1
        nytt = Konto(namn, kontonr, pin, 0)
        self.konton.append(nytt)
        print("Du har nu ett konto i Banken")
        print("Din PIN-kod är", nytt.pin)

    def insattning(self):
        """ Hanterar insättning
        Parametrar: self
        Returnerar: Inget
        """
        namn = input("Namn:")
        pengar = float(input("Hur mycket vill du sätta in? "))
        for konto in self.konton:
            if konto.kontoinnehavare == namn:
                konto.satt_in(pengar)

    def uttag(self):
        """ Hanterar uttag
        Parametrar: self
        Returnerar: Inget
        """
        namn = input("Namn: ")
        pengar = float(input("Hur mycket vill du ta ut? "))
        for konto in self.konton:
            if konto.kontoinnehavare == namn:
                pinkod = int(input("Ange din pinkod: "))
            if pinkod == konto.pin:
                konto.ta_ut(pengar)
            else:
                print("Du angav fel pinkod! Inget uttag beviljas!")
                
    def menyval():
        """Skriver ut menyn, läser in och returnerar användarens val
        Parametrar: inget
        Returnerar: val (str)
        """
        print("-------------------------------")
        print("N Skapa nytt konto")
        print("I Insättning")
        print("U Uttag")
        print("V Visa alla konton (endast bankpersonal)")
        print("A Avsluta")
        val = input("Vad vill du göra? ").upper()
        return val


def huvudprogram():
    """Huvudprogrammet, som skapar bank-objektet, läser in från fil
    anropar menyn och hanterar inmatningen som gjorts.
    Parametrar: inga
    Returnerar: inget
    """
    print("Välkommen till Banken!")
    print("---------------------------------")
    bank = Bank()
    bank.las_konton()
    val = Bank.menyval()
    while val != "A":
        if val == "N":
            bank.nytt_konto()
        elif val == "I":
            bank.insattning()
        elif val == "U":
            bank.uttag()
        elif val == "V":
            bank.visa_alla()
        val = menyval()
    bank.spara_konton()
    print("Tack för besöket, välkommen åter!")


if __name__ == "__main__":
    huvudprogram()