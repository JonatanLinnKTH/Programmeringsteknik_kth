"""
Detta program sparar information om studenter och skriver sedan ut den sparade informationen
Skriven av Jonatan Linn
Kurskod: DD1310
"""
import felhantering_input

class Student:
    """Beskriver en student. Har attributen: förnamn (str), efternamn (str), personnummer (int)"""
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn #string
        self.efternamn = efternamn #string
        self.personnummer = personnummer # int

    def __str__(self):
        return "Namn: " + self.förnamn + " " + self.efternamn + ", Personnummer: " + str(self.personnummer)

class Skola:
    """Sparar informationen om studenter"""
    def __init__(self):
        self.studenter = {}

    def ny_student(self, listnummer):
        """Skapar en ny student och lägger in informationen i objektet studenter"""
        print(f"Stutent {listnummer}:")
        hela_namnet = felhantering_input.input_fullständigt_namn("Vad heter studenten?: ")
        personnummret = felhantering_input.input_siffervärden("Vad är studentens 10 siffriga personnummer?: ", 10, "personnummret")
        self.studenter[f"Student {listnummer}:"] = (Student(hela_namnet[0], hela_namnet[1], personnummret))
        print("Objektet sparat!\n")

    def läs_in_studentlista(self, filnamn):
        """Läser in informationen om de studenter som redand är sparade"""
        with open(filnamn,"r", encoding = "utf-8") as studentfil:
            listnummer = 1
            personnummer = studentfil.readline().strip()
            while personnummer != "":
                efternamn = studentfil.readline().strip()
                förnamn = studentfil.readline().strip()
                self.studenter[f"Student {listnummer}:"] = (Student(förnamn, efternamn, personnummer))
                personnummer = studentfil.readline().strip()
                listnummer += 1
        return listnummer

    def skriv_ut_alla_studenter(self):
        """Skriver ut informationen om alla studenter"""
        print("\nHär är alla sparade objekt:")
        for listnamn,information in self.studenter.items():
            print(listnamn,information)

def huvudprogram():
    """Hälsar välkommen till programmet, ställer frågorna och retunerar svaret"""
    print("\nHalloj och välkommen!")
    print("Här är ett programm där du kan hämta information samt mata in information om nya studenter!\n")
    skola = Skola()
    studentfilnamn = felhantering_input.input_finns_filen("Vad heter filen där informationen ligger?: ")
    antal_registrerade_studenter = skola.läs_in_studentlista(studentfilnamn)

    antal_nya_studenter = felhantering_input.input_siffervärden("Hur många nya studenter ska matas in?: ", variabelnamet= "antal studenter")

    for i in range(antal_registrerade_studenter, antal_registrerade_studenter + int(antal_nya_studenter)):
        skola.ny_student(i)

    skola.skriv_ut_alla_studenter()

huvudprogram()
