#Funktion för att räkna ut den artimetiska talföljden
def artimetisk_summa (a1, d, n):
    Sn=(n*(a1+(a1+d*(n-1))))/2
    return Sn

#Funktion för att räkna ut den geometriska talföljden
def geometrisk_summa (g1, q, n):
    Sn=g1*((q**n-1)/(q-1))
    return Sn

try: #Frågar användaren om värden
    a1=float(input("Ange ett värde på a1: "))
    d=float(input("Ange differensen på talföljden: "))
    g1=float(input("Ange ett värde på g1: "))
    q=float(input("Ange en kvot som inte är 1: "))
    n=int(input("Ange antal termer i talföljden: "))
    artimetisk_resultat=artimetisk_summa(a1,d, n)
    geomtrisk_resultat=geometrisk_summa(g1, q, n)

#Om den artimetiska resultatet är större än det geometriska resultatet
    if (artimetisk_resultat>geomtrisk_resultat):
        print("Den aritmetiska summan är störst")

#Om den geomtriska resultatet är större än det artimetiska resultatet
    elif (artimetisk_resultat<geomtrisk_resultat):
        print("Den geometriska summan är störst")
    else:
        print("Summorna är lika")

#Felhantering
except ValueError:
    print("Det där var felinmatning. Starta om programmmet och försök igen.")
