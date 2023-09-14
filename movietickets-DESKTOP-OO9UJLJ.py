barn_pris = 10
vuxen_pris = 20
print("Hej och välkommen till biljettcentret!")

antal_biljetter = int(input("Hur många biljetter vill du köpa? "))

antal_vuxen = int(input("Hur många av de biljetterna är för en vuxen? "))

antal_barn = antal_biljetter - antal_vuxen

total_pris = antal_barn*barn_pris + antal_vuxen*vuxen_pris

print(f"Du ska betala: {total_pris} kr")
