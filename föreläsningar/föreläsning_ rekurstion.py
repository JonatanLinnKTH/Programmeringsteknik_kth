"""
Föreläsning rekursion, for, while 18/9
Skriven av Jonatan Linn
Kurskod: DD1310
"""

"""
namelist = 3*[None]
agelist = 3*[None]
for i in range(3):
    namelist[i] = input("Name of person number " + str(i+1) + ": ")
    agelist[i] = input("Age of person number " + str(i+1) + ": ")

for i in range(3):
    print(namelist[i],agelist[i])

print(namelist)
print(agelist)
"""
"""
tal = 100
while True:
    if tal > 50:
        tal -= 10
        print(tal)
        continue
    print("Tal är nu", tal, ".")
    svar = input("Vil du fortsätta? (j/n)")
 
    if svar == "n":
        break
    else:
        tal = 100
 
print("Tack och hej!")
"""
"""
while True: 
     stoppa = input("Vill du stoppa? Skriv ja: ") 
     if stoppa == "ja": 
         break
"""
"""
N = 4
i = 0
while i >= N:
    print("Halloj!")
    i += 1

m = 3
while m < 8:
    print("d", end = " ")
    if m > 5:
        print("e", end = " ")
    m += 1

k = 3
while k < 8:
    print("h", end = " ")
    if k > 5:
        print("d", end = " ")
    k += 1
"""
"""
for i in range(5):
    print("hej")
"""

def räknar_siffersumma(tal):
    """Räknar ut siffersumman för talet som stoppas in"""
    if tal < 10:
        return tal

    return räknar_siffersumma(tal // 10) + tal % 10

def räkna_siffersumma_while(tal):
    """Räknar ut siffersumman för talet som stoppas in"""
    summa = 0
    while tal > 0:
        summa += tal % 10
        tal //= 10 # Värt att veta "//="

    return summa

'''
talet = int(input("Positivt heltal: "))
print(f"Siffersumman för {talet} är {räkna_siffersumma_while(talet)}")
'''
