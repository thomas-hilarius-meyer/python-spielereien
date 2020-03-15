gesamtanzahl = 0
feldwert = 1

for feld in range(1, 65):
    print ("Feld", feld, "kostet", feldwert)
    gesamtanzahl = gesamtanzahl + feldwert

    # nächstes Feld
    feldwert = 2 * feldwert

    
print("Kosten für die Erfindung des Schachspiels", gesamtanzahl, "Reiskörner")


# 30mg wiegt ein Reiskorn
gramm = (gesamtanzahl / 1000) * 30
kilogramm = gramm / 1000
tonnen = kilogramm / 1000
print ("Das entspricht", kilogramm, "Kilogramm oder", tonnen, "Tonnen.")

lkws = tonnen / 27
print ("Das entspricht", lkws, "Ladungen 40-Tonnen-LKW's.")

# 400.000 tonnen auf dem größten Massengutfrachter
frachter = tonnen / 400000
print ("Das entspricht", frachter, "Ladungen der größten Massengutfrachter-Klasse.")



