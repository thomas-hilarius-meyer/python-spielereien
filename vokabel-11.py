# Stufe 11: Anfänge einer Steuerung

import random

# Vokabel vordefinieren:
laenge = 0
vokabel = []
bedeutung = []

# Vokabeln einlesen
def laden():
    file = open("wortliste.txt", encoding="utf8").readlines()

    anzahl = len(file)

    x=0
    while x < anzahl:
        vokabel.append(file[x].strip())
        bedeutung.append(file[x+1].strip())
        x=x+2

    print (vokabel)
    print (bedeutung)
    global laenge
    laenge = len(vokabel)


# Vokabeln / Bedeutung abfragen
def abfragen():
    print (vokabel)

    richtige = 0
    falsche = 0

    vokabel_gekannt = []
    bedeutung_gekannt = []
    for i in range (0, laenge):
        vokabel_gekannt.append("nein")
        bedeutung_gekannt.append("nein")


    antwort = ""
    while antwort != "X":
        print(laenge)
        welche = random.randint (0,laenge-1)
        entscheider = random.randint (0,1)

        noch_nicht_gekonnt = vokabel_gekannt.count("nein") + bedeutung_gekannt.count("nein")
        if noch_nicht_gekonnt == 0:
            break

        if entscheider == 0:
            if vokabel_gekannt[welche] == "ja":
                continue
            print ("Was heißt", vokabel[welche], "?")
            antwort = input ("Antwort >")
            if antwort == "X":
                break
            elif antwort == bedeutung[welche]:
                print ("Sehr gut gelernt! Weiter so!")
                richtige = richtige + 1
                vokabel_gekannt[welche] = "ja"
            else:
                print ("Sehr gut. Fast richtig. Ganz richtig wäre", bedeutung[welche])
                falsche = falsche + 1
        else:
            if bedeutung_gekannt[welche] == "ja":
                continue
            print ("Was heißt", bedeutung[welche], "?")
            antwort = input ("Antwort >")
            if antwort == "X":
                break
            elif antwort == vokabel[welche]:
                print ("Sehr gut gelernt! Weiter so!")
                richtige = richtige + 1
                bedeutung_gekannt[welche] = "ja"
            else:
                print ("Sehr gut. Fast richtig. Ganz richtig wäre", vokabel[welche])
                falsche = falsche + 1

    #Schlussmeldung
    print ("--------------------------------------------------------------------")
    print ("Auf Wiedersehen!")
    print ("Du bist insgesamt", richtige+falsche, "Vokabeln abgefragt worden,")
    print ("davon waren", richtige, "richtig und", falsche, "falsch beantwortet.")
    print ("Die Lektion umfasst", len(vokabel), "Wörter.")
    print ("--------------------------------------------------------------------")


# Auswahlmenü:

def auswahl():
    print ("Willkommen zum Vokabeltrainer")
    print ("Was wollen Sie tun?")
    print ("L - Vokabelliste laden")
    print ("A - Vokabelliste anzeigen")
    print ("T - Test machen")
    print ("X - Verlassen")
    print ("--------------------------------")
    wille = input ("Auswahl >")

    if wille == "l":
        laden()
    elif wille == "t":
        abfragen()
    elif wille == "X":
        print ("Auf Wiedersehen")
        exit()
    else:
        print ("Ich weiß nicht was Du willst...")
    auswahl()

# jetzt gehts los:
auswahl()

