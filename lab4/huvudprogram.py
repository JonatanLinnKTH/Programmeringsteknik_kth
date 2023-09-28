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

    def skriv_info(self): # Onödig, ta bort
        print("Förnamn:", self.förnamn)
        print("Efternamn:", self.efternamn)
        print("Personnummer:", str(self.personnummer))

def testprogram():
    """Program för att testa så att klassen Student samt dess metoder fungerar som de ska"""
    print("")
    student_1 = Student("Bengt", "Johansson Svenssson", 9804103493)
    student_1.skriv_info()
    print("")
    print(student_1)

def huvudprogram():
    """Hälsar välkommen till programmet, ställer frågorna och retunerar svaret"""
    print("\nHalloj och välkommen!")
    print("Här är ett programm där du kan mata in information om studenter som sedan matas ut i en prydlig lista!\n")
    
    antal_studenter = felhantering_input.input_siffror("Hur många studenter ska matas in?: ", variabelnamet= "antal studenter")
    studentlista = []
    for i in range(antal_studenter):
        print(f"Stutent {i+1}:")
        hela_namnet = felhantering_input.input_fullständigt_namn("Vad heter studenten?: ")
        personnummret = felhantering_input.input_siffror("Vad är studentens 10 siffriga personnummer?: ", 10, "personnummret")
        studentlista.append(Student(hela_namnet[0], hela_namnet[1], personnummret))
        print("Objektet sparat!\n")

    print("\nHär är alla sparade objekt:")
    for i in range(antal_studenter):
        print(studentlista[i])

huvudprogram()
#testprogram()  