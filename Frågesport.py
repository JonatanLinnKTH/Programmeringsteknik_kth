"""
Övningsuppgift frågesport 12/9
Skriven av Jonatan Linn
Kurskod: DD1310
"""

"""
Exempelprogram för tidsmätning

Vi sparar klockslaget vid start och klockslaget vid slut, sedan tar vi 
skillnaden.
"""

import datetime as dt

start_time = dt.datetime.now()

def strafrunda(n):
    print("""Du svarade fel!
          Nu får du en straffrunda!""")
    
    straf_svar = input("Vad är meningen med livet? ")

    if straf_svar == "42":
        return

svar = input("Vad är svaret på frågan? ")

end_time = dt.datetime.now()

print(f"Tidsåtgång: {end_time-start_time}")