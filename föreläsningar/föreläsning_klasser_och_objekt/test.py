class Djur:
    def __init__(self, namn, föda):
        self.namn = namn
        self.föda = föda

djur1 = Djur("Häst", "Hö")

print("En", djur1.namn, "äter", djur1.föda)

#print(djur1)

namn = "Örjan johansson"
felnamn = "johan4sson"

print(namn.count(" "))

print(namn.isalpha())

print(felnamn.isalpha())

namn_split = namn.split(" ")

print(namn_split[1].isalpha())

antal_studenter = 2
studentlista = []
for i in range(antal_studenter):
    print(i)

studentlista.append(3)
studentlista.append(4)

for student in studentlista:
    print(student)