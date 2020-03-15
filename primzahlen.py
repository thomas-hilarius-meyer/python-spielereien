obergrenze = int (input ("Wieweit listen?"))

for zahl in range (1, obergrenze):
    rest = 0
    primzahl = "ja"
    for i in range (2, zahl): # bei 2 beginnen!!!! jede geht durch 1!!!!
        rest = zahl % i
        if rest == 0:
            primzahl = "nein"
    if primzahl == "ja":
        print (zahl) 
        
