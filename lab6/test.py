"""Test av filfunktionalitet"""


def läsa_studentfil():
    # studentfil = open("students.txt", "r", encoding='utf-8')
    
    with open("students.txt", "r", encoding = "utf-8") as studentfil:
        studenter = []
        personnummer = studentfil.readline().strip()
        while personnummer != "":           #Så länge som raden inte är tom
            församn = studentfil.readline().strip()   #Här vill du läsa in nästa rad, den som innehåller priset och spars den i variabeln pris
            efternamn = studentfil.readline().strip()
            studenter.append([församn,efternamn,personnummer])
            personnummer = studentfil.readline().strip()  #läser in nästa rad, namnet på nästa blomma
    return studenter
 
def main():
    #with open("students.txt", "r", encoding='utf-8') as file:
     #   for rad in file:
      #      print(rad)
    inlästa_studenter = läsa_studentfil()
    for student in inlästa_studenter:
        print(student[0] + student[1] + student[2])
  
main()