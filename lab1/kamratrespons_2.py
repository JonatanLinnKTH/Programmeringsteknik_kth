# Anonym 2
"""
Labortaion 1
Ludvig Romare
1.0.0
"""
def aritmetisk_summa(forsta_talet, differens, antalet_tal): #Funktion för beräkning av aritmetisk summa
    
    summa = antalet_tal * ((forsta_talet + (forsta_talet + differens * (antalet_tal - 1)))/2)
    return int(summa)

def geometrisk_summa(forsta_talet, kvoten, antalet_tal): #Funktion för beräkning av geometrisk summa
    
    summa = forsta_talet * (((kvoten ** antalet_tal) - 1) / (kvoten - 1))
    return int(summa)

def val_av_program(): #Användarens val mellan beräkning av aritmetisk summa eller geometrisk summa
    funktion = input("Vill du beräkna en Aritmetisk summa eller Geometrisk summa? Skriv 'quit' för att avsluta [A/G]\n")
    if funktion == "a" or funktion == "g" or funktion == "quit":
        if funktion == "a":

            forsta_talet = int(input("Vad är första talet? (a1)\n")) #variabel för första talet i talföljden
            differens = int(input("Vad är differensen? (d)\n")) #variabel för differensen mellan två tal i talföljden
            antalet_tal = int(input("Hur många tal? (n)\n")) #variabel för antalet tal i talföljden
            print("Den aritmetiska summan är: ", aritmetisk_summa(forsta_talet, differens, antalet_tal))
            val_av_program()

        elif funktion == "g":

            forsta_talet = int(input("Vad är första talet? (g1)\n")) #variabel för första talet i talföljden
            kvoten = int(input("Vad är kvoten? (q)\n")) #variabel för kvoten i talföljden
            antalet_tal = int(input("Hur många tal? (n)\n")) #variabel för antalet tal i talföljden
            print("Den geometriska summan är: ", geometrisk_summa(forsta_talet, kvoten, antalet_tal))
            val_av_program()

        else:

            quit

    else:

        val_av_program()
        

val_av_program()
