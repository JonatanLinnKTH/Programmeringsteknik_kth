# Ett program som fungerar som ett lexikon där det svenska ordet är nyckel
# och värdet är en lista med översättningar på engelska, tyska och italienska.

lexikon = {} # En tom uppslagslista, som vi sedan kommer fylla på med våra ord och deras översättningar
nycklar = ["glass", "hej", "måndag"]
värden = [] # En tom lista med värden, som vi sedan kommer fylla på
glass_översättning = ["ice cream", "Eis", "gelato"]
värden.append(glass_översättning)
hej_översättning = ["hi", "hallo", "ciao"]
värden.append(hej_översättning)
måndag_översättning = ["Monday", "Montag", "lundi"]
värden.append(måndag_översättning)
# Nu ser listan ut så här: [['ice cream', 'Eis', 'gelato'], ['hi', 'hallo', 'ciao'], ['Monday', 'Montag', 'lundi']]

for i in range(len(nycklar)):
 # Här lägger vi till ett element i vår uppslagslista, första gången
 # for-slingan körs kommer i vara 0 och vi kommer lägga till
 # lexikon["glass"]=['ice cream', 'Eis', 'gelato']
   lexikon[nycklar[i]] = värden[i]

print("Hej och välkommen till lexikonet! Följande ord finns det översättningar på: ")
for nyckel in lexikon.keys():
   print(nyckel)
print("språken du kan välja att översätta till är engelska, tyska och italienska")

val = 0
while val != 3:
    print("\n1. Översätt ett ord \n2. Lägg till ett ord \n3. Avsluta")
    val = int(input("Välj en siffra 1-3: \n"))
    if val == 1: # Översätt ett ord
        svenskt_ord = input("Vilket ord vill du översätta? ")
        språk = input("Vilket språk vill du översätta till? ")
        if svenskt_ord in lexikon.keys():
          # Om första bosktaven på språk är e är vi ute efter det engelska ordet
           if språk[0] == "e": 
               # Här tar vi fram det ord som finns på index 0, i listan med värdet, med den givna nyckeln
               översättning = lexikon[svenskt_ord][0]
               print(svenskt_ord, "översätts till", översättning)
           elif språk[0] == "t":
               översättning = lexikon[svenskt_ord][1]
               print(svenskt_ord, "översätts till", översättning)
           elif språk[0] == "i":
               översättning = lexikon[svenskt_ord][2]
               print(svenskt_ord, "översätts till", översättning)
           else:
               print("Det språket har vi ingen översättning till.")
        else:
            print("Det ordet finns inte lexikonet")
            
    elif val == 2: # Lägg till ett ord
        svenskt_ord = input("Vilket ord vill du lägga till? ")
        # Tom lista där vi sedan fyller på med varje värde.
        översättningar = []
        engelskt_ord = input("Vad heter det på engelska? ")
        översättningar.append(engelskt_ord)
        tyskt_ord = input("Vad heter det på tyska? ")
        översättningar.append(tyskt_ord)
        italienskt_ord = input("Vad heter det på italienska? ")
        översättningar.append(italienskt_ord)
        # Här lägger vi till ordet i vårt lexikon
        lexikon[svenskt_ord] = översättningar
        print("Det svenska ordet", svenskt_ord, "har lagts till med översättningarna: ")
        for i in range(3):
           print(lexikon[svenskt_ord][i], end=" ")
        print() # Skriver bara ut en blankrad

    elif val == 3: # Avsluta
        print("Välkommen åter!")

    else:
       print("Tyvärr så skrev du något fel. Försök igen!")