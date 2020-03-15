# Stufe 6: Vokabelliste aus Datei lesen

import random


# Vokabeln einlesen ---------------------------------------

vokabel = []
bedeutung = []

file = open("wortliste.txt", encoding="utf8").readlines()

anzahl = len(file)

x=0
while x < anzahl:
    vokabel.append(file[x].strip())
    bedeutung.append(file[x+1].strip())
    x=x+2

laenge = len(vokabel)


# Vokabeln / Bedeutung abfragen ------------------------------

while 1 == 1:
    welche = random.randint (0,laenge-1)
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
