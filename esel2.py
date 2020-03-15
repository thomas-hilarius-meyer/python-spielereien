# Taschrenchner - Programm - Version 1.0.0

print ("Willkommen zum Taschenrechner!")

zahl1 = input ("Erste Zahl:")
zahl2 = input ("Zweite Zahl:")
rechenart = input ("Was soll ich rechnen (a/s/m/d):")

zahl1 = float (zahl1)
zahl2 = float (zahl2)

if rechenart == "a":
    print ("Aha, sie wollen addieren. Ergebnis:")
    print (zahl1 + zahl2)
if rechenart == "s":
    print ("Aha, sie wollen subtrahieren. Ergebnis:")
    print (zahl1 - zahl2)
if rechenart == "m":
    print ("Aha, sie wollen multiplizieren. Ergebnis:")
    print (zahl1 * zahl2)
if rechenart == "d":
    if zahl2 == 0:
        print ("In Mathe nicht aufgepasst, oder was?")
    else:
        print ("Aha, sie wollen dividieren. Ergebnis:")
        print (zahl1 / zahl2)
    
print ("Auf Wiedersehen!")




