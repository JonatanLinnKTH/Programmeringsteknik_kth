from datetime import time
class Parkering:
    def __init__(self, starttid, sluttid):
        """Skapar ett nytt objekt Parkering. Parametrar: 
        starttid (time)
        sluttid (time)"""
        self.starttid = starttid
        self.sluttid = sluttid

    def __str__(self):
        """Returnerar en sträng som beskriver objektet"""
        return "Inpassage: " + self.starttid + ", Utpassage: " + self.sluttid

def testprogram():
    parkering_1 = Parkering(time(12, 30), time(14, 40))
    print(parkering_1)

testprogram()