# Vokabeln definieren

vokabel = ["le chien", "le chat"]
bedeutung = ["der Hund", "die Katze"]


# Vokabeln abfragen

print ("Was heißt", vokabel[0], "?")

antwort = input ("Antwort >")

if antwort == bedeutung[0]:
    print ("Sehr gut gelernt! Weiter so!")
else:
    print ("Sehr gut. Fast richtig. Ganz richtig wäre", bedeutung)

