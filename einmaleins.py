# Einmaleins-Trainer

import random
richtig = 0
falsch  = 0

print ("Hallo zum coolen 1x1-Programm")

obergrenze = input ("Wie weit kannst Du schon?")
obergrenze = int(obergrenze)

print ("Ich werde Dich also bis ", obergrenze, " abfragen. Ok.")
weitermachen = "ja"

while weitermachen == "ja":
    a = random.randint (1, obergrenze)
    b = random.randint (1, obergrenze)

    print ("Was ist", str(a) , " x ", str(b), "?")

    ergebnis = a * b
    antwort  = input ("Deine Antwort")
    antwort  = int (antwort)

    if antwort == ergebnis:
        print ("Richtig!")
        richtig = richtig + 1
    else:
        print ("Leider falsch!")
        print ("Das richtige Ergebnis ist", str(ergebnis))
        falsch = falsch + 1
    nochmal = input ("Noch eine Aufgabe? (j/n)")
    if nochmal != "j":
        weitermachen = "nein"

print ("Du hast", richtig + falsch, "Aufgaben gerechnet. Davon waren", richtig, "richtig und", falsch, "falsch.")
