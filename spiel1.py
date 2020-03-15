# Zufallszahl festlegen (ZAHL)
import random
zahl = random.randint (1,1000)
anzahl = 0

while zahl > 0:
    # Nutzer eine Zahl raten lassen (EINGABE)
    eingabe = input ("Was rätst DU? ")
    eingabe = int (eingabe)
    anzahl = anzahl + 1
    
    # Wenn ZAHL == EINGABE:
    # -> gewonnen -> Schluss!
    if zahl == eingabe:
        print ("Toll, Du hast gewonnen.")
        break 

    # Wenn ZAHL > EINGABE:
    # -> ätsch, meine Zahl ist größer! -> nochmal!
    if zahl > eingabe:
        print ("FALSCH! Meine Zahl ist größer!")

    # Wenn ZAHL < EINGABE:
    # -> ätsch, meine Zahl ist kleiner! -> nochmal!
    if zahl < eingabe:
        print ("FALSCH! Meine Zahl ist kleiner!")

print ("Anzahl Versuche: ")
print (anzahl)
