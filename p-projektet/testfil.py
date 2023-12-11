from datetime import time
 
# calling the constructor

my_time = time(12, 14)
 
print("Entered time", my_time)

my_time = time(minute = 12)
string = my_time.strftime('%H:%M')
intedger = my_time.hour

print("\nTime with one argument " + string)
print(intedger)

"""
inpassage = input("Startid för parkering: ").split(":",1)
print(inpassage)
"""
"""
rad = "QPR556,Carl von Testperson,liten"
rad_uppdelad = rad.split(",")
print(rad_uppdelad)
"""
"""
filnamn = "registrerade_bilar.txt"
with open(filnamn,"r", encoding = "utf-8") as registrerade_bilar:
    rad = registrerade_bilar.readline().strip()
    [regnummer, ägare, biltyp] = rad.split(",")
print(regnummer)
"""
