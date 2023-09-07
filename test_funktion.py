# test_funktion
# Jonatan Linn
# 2/9-2023
# DD1310 
#(bra att alltid ha med)

# grundläggande funktionsdefintition
def greeting():
   print("Hej!")

# grudläggande funktionsanrop
greeting()

# funktion med parameter
def skrik(meddelande):
   print(meddelande + "!!!")

# funktionsanrop med parameter
skrik("shhhh")
skrik("tyst i klassen")
skrik("M")

# default parametrar
def välkommen1(namn, hemvist="Lönneberga"):
   '''Skriver ut välkomstfras; namn och hemvist är strängar, hemvist blir 'Lönneberga' om inget annat anges'''
   print(f"Välkommen, {namn} från {hemvist}!")

# anrop som använder default parametrar
välkommen1("Emil")
välkommen1("Ida")
välkommen1("Alfred")
# anrop som skriver över default parametrar
välkommen1("Madicken", "Junibacken")

# test default parametrar
def beräkna_styckpris(antal=50, bakgrundsfärg="blå", form="fyrkantig"):
 if form != "fyrkantig":
    styckpris = 60
 else:
    styckpris = 40
 
 if bakgrundsfärg != "vit":
    styckpris += 3
 
 if antal >= 100:
    styckpris = styckpris * 0.80

 return styckpris

pris = beräkna_styckpris(form="rund")
print(pris)