from datetime import time, datetime
 
# calling the constructor

my_time = time(12, 14)
 
print("Entered time", my_time)

my_time = time(minute = 12)
string = my_time.strftime('%H:%M')

print("\nTime with one argument " + string)
print(my_time.minute)

tid_1 = time(12,30)
tid_2 = time(13,32)
datumobjekt = datetime(1,1,1)
t1 = datumobjekt.combine(datumobjekt, tid_1)
t2 = datumobjekt.combine(datumobjekt, tid_2)

diff = t2-t1
#df["Time Taken"] = (pd.to  _datetime(df['end_time'])- pd.to_datetime(df['start_time']))
timmar, resten = divmod(diff.seconds, 3600)
minuter, sekunder = divmod(resten, 60)
print(timmar, minuter)

#start = datetime.strptime("12:30","%H:%M")
#slut = datetime.strptime("13:32", "%H:%M")
start = datetime(1,1,1,12,15)
slut = datetime(1,1,1,13,29)
diff = slut - start
print(diff.total_seconds())
timmar, resten = divmod(diff.total_seconds(), 3600)
minuter, sekunder = divmod(resten, 60)

if minuter >= 45:
    timmar += 1
elif minuter >= 15:
    timmar += 0.5

print(diff)
print(timmar)
fem = 5
print(f"hej hej {fem}")

bilar = {}


"""
inpassage = input("Startid för parkering: ").split(":",1)
print(inpassage)
"""

rad = "QPR556,Carl von Testperson,liten"
rad_uppdelad = rad.split(",")
bokstäver = rad[0:3]
print(rad[0:3].isalpha())

"""
filnamn = "registrerade_bilar.txt"
with open(filnamn,"r", encoding = "utf-8") as registrerade_bilar:
    rad = registrerade_bilar.readline().strip()
    [regnummer, ägare, biltyp] = rad.split(",")
print(regnummer)
"""
