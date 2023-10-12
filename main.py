
def läsa_blomfil():
    blomfil = open("infil.txt", "x", encoding="utf-8")
    blommor = []
    blomma = blomfil.readline().strip()
    while blomma != "":           #Så länge som raden inte är tom
        pris = blomfil.readline().strip()   #Här vill du läsa in nästa rad, den som innehåller priset och spars den i variabeln pris
        blommor.append([blomma,pris])
        blomma = blomfil.readline().strip()  #läser in nästa rad, namnet på nästa blomma
    blomfil.close()
    return blommor
 
def main():
    inlästa_blommor = läsa_blomfil()
    for blomma in inlästa_blommor:
        print(blomma[0] + " har priset " + blomma[1] + " kr.")
  
main()
"""
fil = open("infil.txt", "r", encoding="utf-8")
for rad in fil:
    print(rad)
"""
