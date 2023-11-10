# föreläsning_funktioner_och_variabler.py
# Jonatan Linn
# 4/9
# DD1310
print("Hej, Daniel")
ålder_daniel = 37
print(f"Du är {ålder_daniel} år gammal")

# heltalsoperationer
x = 5
y = x / 2 # blir flyttal
z = x // 2 # tar bort decimaldelen och blir heltal
x_square = x**2

# operationer med strängar
hej = "hej"
print(3*hej) # man kan multipricera en sträng med heltal

# testar funktion utan return
def returns_nothing(x):
    y = x + 2

# y = returns_nothing(2)
# z = returns_nothing(2)

print(f"y = {y}")
print(f"z = {z}")