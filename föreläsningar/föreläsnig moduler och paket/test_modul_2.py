#bla bla bla
def matar_du_in_ett_heltal():
    """bla bla bla"""
    while True:
        try:
            inmatning = int(input("Mata in ett heltal! "))
            break

        except ValueError:
            print("Ge mig ett heltal! ")


matar_du_in_ett_heltal()