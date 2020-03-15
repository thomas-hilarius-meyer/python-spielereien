print (" Willkommen zum ultimativen Lego-Treppen-Kalkulator!!!")
print ("                   #                                  ")
print ("                  # #                                 ")
print ("                 # # #                                ")
print ("                # # # #                               ")
print ("                                 in memoriam GRAF ZAHL")

reihen = int ( input ("Wieviele Reihen baust Du?") )
kloetze = 0

for reihen in range (1, reihen + 1):
    kloetze = kloetze + reihen

print ( "Du brauchst ", kloetze, " Klötzchen, um die Treppe zu bauen.")

