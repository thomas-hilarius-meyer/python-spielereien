# Vokabeln definieren

vokabel = "le chien"
bedeutung = "der Hund"


# Vokabeln abfragen

print ("Was heißt", vokabel, "?")

antwort = input ("Antwort >")

if antwort == bedeutung:
    print ("Sehr gut gelernt! Weiter so!")
else:
    print ("Sehr gut. Fast richtig. Ganz richtig wäre", bedeutung)

