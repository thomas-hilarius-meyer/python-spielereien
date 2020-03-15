# Taschenrechner-Programm

print ("Geben Sie zwei Zahlen ein und wählen Sie eine Rechenart!")
x = input ("Erste Zahl: ")
y = input ("Zweite Zahl: ")
z = input ("Was tun? (a/s/m/d)")
x = float(x)
y = float(y)

if z == "a":
    print ("aha, Addieren. Das Ergebnis ist:")
    print (x+y)

if z == "s":
    print ("aha, Subtrahieren. Das Ergebnis ist:")
    print (x-y)

if z == "m":
    print ("aha, Multiplizieren. Das Ergebnis ist:")
    print (x*y)

if z == "d":
    if y == 0:
        print ("Das geht doch nidd, Du Dirmel, Du Schereschleifer!!!")
    else:
        print ("aha, Dividieren. Das Ergebnis ist:")
        print (x/y)
