"""Testprogramm klasser och objekt"""

"""Classer använs för att skapa nya datortyper som inte är de fördefinierade av phytorn"""

class Bil:
    def __init__(self, märke, modell):
        """ konstruktor som initierar en Bil av märket märke och modellen modell """
        self.märke = märke
        self.modell = modell

    def __str__(self):
        return "Märke " + self.märke + " modell " + self.modell


minBil = Bil("volvo", "XE60")
# print(minBil)

bilar = [Bil("Smart", "?"), Bil("Lambo", "coutch")]
bilar.append(minBil)

for bil in bilar:
    print(bil)