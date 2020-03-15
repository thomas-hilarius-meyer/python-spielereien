from time import sleep

import winsound
frequenz = 50  # Set Frequency To 2500 Hertz
dauer = 1000  # Set Duration To 1000 ms == 1 second

zeit = int ( input ("Wie lange willst Du schlafen?") )
i = zeit

while i > 0:
    sleep (1)
    print (i)
    i = i - 1
    
print ("Aufwachen!!!!!!!!!!!!!!!!")
winsound.Beep(frequenz, dauer)
