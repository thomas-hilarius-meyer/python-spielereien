import random

# Vokabeln definieren

vokabel = ["scissor-grinder", "horse", "angel", "miller", "wall-builder", "painter", "long-well", "wolve", "present by God"]

bedeutung = ["Scherenschleifer", "Pferd", "engel", "Müller", "Maurer", "Dincher", "Langguth", "Wolf", "Dieudonne"]
laenge = len(vokabel)
welche = random.randint (0,laenge)

# Vokabeln / Bedeutung abfragen
entscheider = random.randint (0,1)

if entscheider == 0:
    print ("Was heißt", vokabel[welche], "?")

    antwort = input ("Antwort >")

    if antwort == bedeutung[welche]:
        print ("Sehr gut gelernt! Weiter so!")
    else:
        print ("Sehr gut. Fast richtig. Ganz richtig wäre", bedeutung[welche])
else:
    print ("Was heißt", bedeutung[welche], "?")

    antwort = input ("Antwort >")

    if antwort == vokabel[welche]:
        print ("Sehr gut gelernt! Weiter so!")
    else:
        print ("Sehr gut. Fast richtig. Ganz richtig wäre", vokabel[welche])
