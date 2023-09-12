barn_pris = 10
vuxen_pris = 20

antal_biljetter = input("Hur många biljetter vil du köpa? ") #felstavning
antalBiljetter = int(antal_biljetter) # kan skrivas på samma rad och följer inte namnstandard

antal_vuxen = input("Hur många av de biljetterna är för en vuxen? ")
antalVuxen = int(antal_vuxen) # kan skrivas på samma rad och följer inte namnstandard

antal_barn = antalBiljetter - antalVuxen

total_pris = antal_barn*barn_pris + antalVuxen*vuxen_pris

print("Du ska betala:")
print(total_pris) # kan skrivas på samma rad
