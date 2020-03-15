import random

# Vokabeln definieren

vokabel = ["le chien", "le chat"]
bedeutung = ["der Hund", "die Katze"]

# Vokabeln / Bedeutung abfragen
entscheider = random.randint (0,1)

if entscheider == 0:
    print ("Was heißt", vokabel[0], "?")

    antwort = input ("Antwort >")

    if antwort == bedeutung[0]:
        print ("Sehr gut gelernt! Weiter so!")
    else:
        print ("Sehr gut. Fast richtig. Ganz richtig wäre", bedeutung[0])
else:
    print ("Was heißt", bedeutung[0], "?")

    antwort = input ("Antwort >")

    if antwort == vokabel[0]:
        print ("Sehr gut gelernt! Weiter so!")
    else:
        print ("Sehr gut. Fast richtig. Ganz richtig wäre", vokabel[0])
