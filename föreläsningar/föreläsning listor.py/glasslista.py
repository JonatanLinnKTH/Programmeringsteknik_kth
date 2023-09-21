glasslista = ["chokladglass"]
  
def ny_smak():
    glasslista.append("hallonglass")
    glasslista.append("blåbärsglass")
  
def sortera_lista():
    glasslista.sort() 

ny_smak()

def ny_lista():
    global glasslista
    glasslista = ["vaniljglass", "jordgubbsglass", "chokladglass"]
  
def ta_bort():
    glasslista.remove("hallonglass")
