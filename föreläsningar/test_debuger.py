def klicka_step_into():
    a = 10
    b = 5
    return a + b

def klicka_step_over():
    c = 20
    d = 30
    return c + d

def klicka_step_into_step_out():
    e = 1  # klicka nu STEP OUT
    f = 2
    return e + f


print("Sätt din break point på denna rad")
# använda STEP OVER för att gå till nästa rad

ålder = 21
# se hur ålder visas i variables-fönstret!

# gör som funktionsnamnen beskriver
into_retur = klicka_step_into()
print(into_retur)

over_retur = klicka_step_over()
print(over_retur)

into_out_retur = klicka_step_into_step_out()
print((into_out_retur))