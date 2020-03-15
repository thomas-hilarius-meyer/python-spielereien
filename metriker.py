# METRIKER.PY - atomatisches Metrisieren von Gedichtzeilen - thm 26.2.2020:

verbose = False
#verbose = True        # bei verbose empfihelt sich ausgabeumleitung!!!

import re

# Gedicht aus Datei einlesen

#filename = input ("Gib Dateiname >")
filename = "gryphius.txt"
file = open(filename, encoding="utf8").readlines()

verszahl = len(file)
x=0
gedicht = []
silben = []

while x < verszahl:
    gedicht.append(file[x].strip())
    x=x+1

vokal = []

print ("--------------------------------------------")
print ("   x = unbetonte Silbe")
print ("   # = betonte Silbe")
print ("--------------------------------------------")
print ()

metrisierung_vorgaenger = "   "
versnummer = 0
reimvokale = []

for vers in gedicht:
    versnummer = versnummer + 1
    print (vers)
    rest = []
    vokal = []
    # Großbuchstaben in Kleinbuchstaben umwandeln
    rest = vers.lower()

    # nicht alle Silben sind im Original durch Konsonanten getrennt
    rest = re.sub("aue", "auxe", rest)
    rest = re.sub("äol", "äxol", rest)
    rest = re.sub("eie", "eixe", rest)
    rest = re.sub("eue", "euxe", rest)
    rest = re.sub("tue", "tuxe", rest)
    rest = re.sub("ruhe", "ruxe", rest)
    rest = re.sub("rohe", "roxe", rest)
    rest = re.sub("zuha", "zuxa", rest)
    rest = re.sub("zuhe", "zuxe", rest)

    # Sonderverwendungen des h behandeln:
    #rest = re.sub("ch", "CH", rest) # warum???
    rest = re.sub("heit", "xeit", rest)
    rest = re.sub(" die ", " de ", rest) # Artikel
    rest = re.sub("^die ", " de ", rest) # Artikel
    rest = re.sub(" das ", " des ", rest)
    rest = re.sub("^das ", " des ", rest)
    rest = re.sub("ah", "aa", rest)
    rest = re.sub("ie", "ii", rest) 
    rest = re.sub("eh", "ee", rest)
    rest = re.sub("ih", "ii", rest)
    rest = re.sub("oh", "oo", rest)
    rest = re.sub("uh", "uu", rest)
    rest = re.sub("ß",  "SZsz", rest)
    rest = re.sub("ss", "SSss", rest)  # Schärfung

    # Wortgrenzen codieren:
    rest = "WG" + rest
    rest = re.sub(" ", " WG ", rest)
    
    if verbose: print (rest)

    rest = rest + " "
    rest = re.split ('b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z| |\,|\;|\:|\.|\?|\!|\'|\n|\r', rest)
    if verbose: print ("Nach Transformation: ", rest)

    vokal_mit_trenner = []
    vokal_und_trenner = []
    for x in range (0, len(rest)):
        if rest[x] == '':
            next
        elif rest[x] == 'WG':
            vokal_und_trenner.append(rest[x])
        else:
            vokal.append(rest[x])
            vokal_und_trenner.append(rest[x])

    flag = False
    for x in range (0, len(vokal_und_trenner)):
        if vokal_und_trenner[x] == "WG":
            vokal_mit_trenner.append("WG" + vokal_und_trenner[x+1])
            flag = True
        else:
            try:
                if flag:
                    flag = False
                    next
                else:
                    vokal_mit_trenner.append(vokal_und_trenner[x])
                    flag = False
            except:
                pass
        
      #vokalstring = rest[x]
      #if vokalstring.count("WG") == 1:
      #    rest[x+1] = "WG" + rest[x+1]
      #if vokalstring != "" and vokalstring.count("WG") == 0:
      #  vokal.append (vokalstring)

    silbenzahl = len (vokal)

    #vokal_mit_trenner = vokal
    if verbose: print ("Silbenvokale mit Wortgrenzen: ", vokal_mit_trenner)
    
    #for x in range (silbenzahl):
    #    vokal[x] = re.sub("WG", '', vokal_mit_trenner[x])

    if verbose: print ("Silbenvokale:                 ", vokal)
    
    if verbose: print ("Silbenzahl: ", silbenzahl)
  
    punktzahl = []
    metrisierungsstring = []
    for metrisierung in range (0, 2**silbenzahl):
        punktzahl.append (0)
        string = str(bin(metrisierung))
        string = string[2::]

        for i in range (silbenzahl - len(string)):
            string = "0" + string
        metrisierungsstring.append (string)
        if verbose: print ("Prüfe Metrisierungsvorschlag: ", string)

#       Gleichheit mit Vorgänger: Bonus
        if (string == metrisierung_vorgaenger):
            punktzahl[metrisierung] = punktzahl[metrisierung] + 15
#       wenigstens gleicher Beginn:
        if (string[0] == metrisierung_vorgaenger[0] and string[1] == metrisierung_vorgaenger[1]):
            punktzahl[metrisierung] = punktzahl[metrisierung] + 10

        for i in range (silbenzahl):
            if verbose: print ("Prüfe das ", vokal[i], " auf Eigenschaft ", string[i])
            # bei mehrsilbigen Wörtern ist der Wortton bei der ersten Silbe:
            try:
                if vokal_mit_trenner[i].count("WG") == 1 and vokal_mit_trenner[i+1].count("WG") == 0 and string[i] == "1":
                    punktzahl[metrisierung] = punktzahl[metrisierung] + 10
                    # print ("bingo:" + str(i)+ " " + vokal[i] + vokal[i+1] + " " + string[i])
            except:
                pass
#           jedes betonte e vor oder nach buntem Vokal ergibt einen  Malus 
            try:
                if vokal[i].count("e") == 1 and string [i] == "1" and vokal[i+1].count == 0:
                    punktzahl[metrisierung] = punktzahl[metrisierung] - 5
                if vokal[i].count("e") == 1 and string [i] == "1" and vokal[i-1].count == 0:
                    punktzahl[metrisierung] = punktzahl[metrisierung] - 5
            except:
                pass
#           jeder betonte bunte Vokal (aiou Dipthonge) ergibt einen größeren Bonus (+2)
            if vokal[i] in ["a", "i", "o", "u"] and string [i] == "1":
                punktzahl[metrisierung] = punktzahl[metrisierung] + 5
            # Umlaute sind i.d.R. betont:
            if vokal[i] in ["ä", "ö", "ü"] and string [i] == "1":
                punktzahl[metrisierung] = punktzahl[metrisierung] + 15
            if vokal[i] in ["ä", "ö", "ü"] and string [i] == "0":
                punktzahl[metrisierung] = punktzahl[metrisierung] - 5
#           jeder unbetonte Diphtong -> deutlicher Malus (-2)
            if vokal[i] in ["au", "ei", "eu", "äu", "ou"] and string [i] == "0":
                punktzahl[metrisierung] = punktzahl[metrisierung] - 5
#           jeder betonte Diphtong -> deutlicher Bonus (+2)
            if vokal[i] in ["au", "ei", "eu", "äu", "ou"] and string [i] == "1":
                punktzahl[metrisierung] = punktzahl[metrisierung] + 5
#           betonter Doppelvokal / gedehnter Vokal -> Bonus (+2)
            if vokal[i] in ["aa", "ee", "ii", "oo", "uu"] and string [i] == "1":
                punktzahl[metrisierung] = punktzahl[metrisierung] + 5
#           unbetonter Doppelvokal / gedehnter Vokal -> Malus (-2)
            if vokal[i] in ["aa", "ee", "ii", "oo", "uu"] and string [i] == "0":
                punktzahl[metrisierung] = punktzahl[metrisierung] - 5
#           betonter Vokal vor ß - >Bonus
            if vokal[i].count("SZ") == 1 and string [i] == "1":
                punktzahl[metrisierung] = punktzahl[metrisierung] + 7                  
#           Schärfung:
            if vokal[i].count("SS") == 1 and string [i] == "1":
                punktzahl[metrisierung] = punktzahl[metrisierung] + 7
#           doppelter Hebungsprall bringt mittleren Malus (-2)
            try: # falls index out of range einfach ignorieren
                if string[i] == "1" and string[i+1] == "1":
                    punktzahl[metrisierung] = punktzahl[metrisierung] - 25
#           dreifacher Hebungsprall bringt gigantischen Malus (-3)
                if string[i] == "1" and string[i+1] == "1" and string[i+2] == "1":
                    punktzahl[metrisierung] = punktzahl[metrisierung] - 50
#           dreifacher Senkungsprall bringt riesigen Malus    (-2)
                if string[i] == "0" and string[i+1] == "0" and string[i+2] == "0":
                    punktzahl[metrisierung] = punktzahl[metrisierung] - 4
                if string[i] == "0" and string[i+1] == "0":
                    punktzahl[metrisierung] = punktzahl[metrisierung] - 2
            except:
                pass
#       reiner Versfuß im ganzen Vers bringt deutlichen Bonus (+3)
#          -> d.h. Vers restlos aufteilbar in ((evtl. Auftakt) + beliebig viele (Xx, xX, Xxx ODER xxX))
        punktzahl[metrisierung] = punktzahl[metrisierung] + 5 * string.count ("1010")
        punktzahl[metrisierung] = punktzahl[metrisierung] + 5 * string.count ("0101")
        punktzahl[metrisierung] = punktzahl[metrisierung] + 9 * string.count ("101010")
        punktzahl[metrisierung] = punktzahl[metrisierung] + 9 * string.count ("010101")
            
        punktzahl[metrisierung] = punktzahl[metrisierung] + 5 * string.count ("100100")
        punktzahl[metrisierung] = punktzahl[metrisierung] + 5 * string.count ("001001")

        if verbose:
            print ("Erreichte Punktzahl: ", punktzahl[metrisierung])
#        erste Silbe eines Wortes betont -> deutlicher Bonus (+2)

#   höchste Bewertungszahl feststellen
    hoechstwert = 0
    hoechstindex = 0
    for i in range (len(punktzahl)):
      if punktzahl[i] > hoechstwert:
        hoechstwert = punktzahl[i]
        hoechstindex = i

    if verbose: print ("Vokale: ", vokal, "Silben :", silbenzahl)
#   Metrisierung mit bester Punktzahl ausgeben
    binaer_string = metrisierungsstring[hoechstindex]
    huebscher_string = ""
    for i in range (len(binaer_string)):
        huebscher_string = huebscher_string + binaer_string[i]
        huebscher_string = huebscher_string + " "
        huebscher_string = re.sub("0", "x", huebscher_string)
        huebscher_string = re.sub("1", "#", huebscher_string)

    formatierblanks = ""
    for i in range (50 - len(huebscher_string)):
        formatierblanks = formatierblanks + " "

    diagnose = "unregelm."
    if binaer_string.count("10") * 2 == silbenzahl:
        diagnose = str(int(silbenzahl/2)) + "-hebiger Trochäus"
    if binaer_string.count("01") * 2 == silbenzahl:
        diagnose = str(int(silbenzahl/2)) + "-hebiger Jambus"
        
    hilfstring = binaer_string + "1"
    if hilfstring.count("01") * 2 == (silbenzahl + 1):
        diagnose = str(int(((silbenzahl-1)/2))) + "-hebiger Jambus, klingend!"
        
    hilfstring = binaer_string + "0"
    if hilfstring.count("10") * 2 == (silbenzahl + 1):
        diagnose = str(int(((silbenzahl-1)/2))) + "-hebiger Trochäus, unvollständig!"
        
    if binaer_string.count("100") * 2 == silbenzahl:
        diagnose = str(int(silbenzahl/2)) + "-hebiger Daktylus"
    if binaer_string.count("001") * 2 == silbenzahl:
        diagnose = str(int(silbenzahl/2)) + "-hebiger Anapäst"
    
    print (huebscher_string, formatierblanks, " --- ", silbenzahl, " S.", "---", diagnose)
    
    metrisierung_vorgaenger = metrisierungsstring[hoechstindex]
    if verbose: print ("(Bewertung:", hoechstwert, ")")

#   Reimvokale aufheben
    x = silbenzahl - 1
    if binaer_string[x] == "1":
        reimvokale.append(vokal[x])
    elif binaer_string[x-1] == "1":
        reimvokale.append(vokal [x-1] + " " + vokal[x])
    else:
        reimvokale.append(vokal [x-2] + " " + vokal [x-1] + " " + vokal[x])
        

# Teil II - Reimmaster

reimkennung = ["a", "b", "c", "d", "e", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
z = 0
reimkuerzel = []

for x in range(versnummer):
    gefunden = False
    for y in range(x):
        if reimvokale[x] == reimvokale[y]:
            reimkuerzel.append(reimkuerzel[y])
            gefunden = True
            #print ("gefunden - dasselbe wie in Vers " + str(y))
            break
    if gefunden == False:
        reimkuerzel.append(reimkennung[z])
        z = z + 1

    #print (reimvokale[x] + "------>" + reimkuerzel[x])
print (reimkuerzel)

    

