from datetime import time
 
# calling the constructor
my_time = time(12, 14)
 
print("Entered time", my_time)

my_time = time(minute = 12)
print("\nTime with one argument", my_time)

inpassage = input("Startid för parkering: ").split(":",1)
print(inpassage)
