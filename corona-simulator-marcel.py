import random, pygame
pygame.init()
verbose = False

# Voreinstellungen zur Simulation: ---------------------------------

bevoelkerungszahl = 1000000
inkubationszeit = 7            # in Tagen
krankheitsdauer = 28           # in Tagen
ansteckung_nach_inkubation = False
ansteckungsfaktor =  3
mortalitaetsfaktor = 1000      # "einer von 1000 stirbt..."
immunisierung = True
komplikationsquote = 100       # "einer von 100 hat einen schweren verlauf..."
simulationsdauer = 365
karte = pygame.image.load("karte.jpg")
# -----------------------------------------------------------------------

# Population vorbereiten:

status = [] # g / k / s / t - gesund / krank / schwerkrank / tot
krankentag = []
immunitaet = []

iniz_back = 0
infizierte = 0
schwerkranke = 0
tote = 0
geheilte = 0
anzeigen = []
neuer_kranker = False
for i in range (bevoelkerungszahl+1):
    status.append("g")
    krankentag.append(0)
    immunitaet.append(False)
kartesize = karte.get_size()
screen = pygame.display.set_mode(kartesize)
# Erste Infektion auslösen:

infizierte = 1
infizierte_history = 1
schwerkranke_history = 0
status[0] = "k"
krankentag[0] = 1


# Und los gehts... - Regeln anwenden:

for tag in range (simulationsdauer):
    screen.blit(karte, (0,0))
    pygame.display.flip()
    for i in range (bevoelkerungszahl):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if status[i] == "k" or status[i] == "s": # wenn man krank ist...
            # verbringt man Zeit:
            krankentag[i] = krankentag[i] + 1

            # steckt man Leute an:
            if (ansteckung_nach_inkubation == False and krankentag[i] < inkubationszeit) or (ansteckung_nach_inkubation == True):
                ansteckentscheidung = random.randint (0, int (inkubationszeit / ansteckungsfaktor )) # überhaupt anstecken?
                if ansteckentscheidung == 1:
                    ziel = random.randint (1, bevoelkerungszahl)
                    if status[ziel] == "k" or status[ziel] == "s" or status[ziel] == "t" or immunitaet[ziel] == True: # keine kranken oder immunen anstecken
                        if verbose: print ("Potentielle Ansteckung gescheitert, Patient: ", ziel)
                        pass
                    else:
                        if verbose: print ("Patient", i, "steckt jetzt Mensch", ziel, "an.")
                        status[ziel] = "k"
                        krankentag[ziel] = 1
                        infizierte = infizierte + 1
                        infizierte_history = infizierte_history + 1


            # wird schwerkrank:
            if status[i] == "k":
                komplikationsentscheidung = random.randint (0, komplikationsquote) # einer von hundert...
                if komplikationsentscheidung == 1:
                    status[i] = "s"
                    schwerkranke = schwerkranke + 1
                    schwerkranke_history = schwerkranke_history + 1
                    if verbose: print ("Patient", i, "hat einen schweren Verlauf.")

            # stirbt:
            sterbeentscheidung = random.randint (0, mortalitaetsfaktor ) # einer von tausend...
            if sterbeentscheidung == 1:
                status[i] == "t"
                tote = tote + 1
                if verbose: print ("Patient", i, "stirbt.")

            # oder wird gesund:
            if krankentag[i] > krankheitsdauer:
                if status[i] == "s":
                    schwerkranke = schwerkranke - 1
                status[i] = "g"
                krankentag[i] = "0"
                if immunisierung == True:
                    immunitaet[i] = True
                infizierte = infizierte - 1
                geheilte = geheilte + 1
                if verbose: print ("Patient", i, "ist wieder gesund.")
    for i in range(infizierte-iniz_back):
        while 1:
            anzeigen_snd = (random.randint(20, kartesize[0]-23), random.randint(20, kartesize[1]-23))
            pixelfabe = karte.get_at(anzeigen_snd)
            if pixelfabe[0] < 50 and pixelfabe[1] < 50 and pixelfabe[2] < 50:
                anzeigen.append([anzeigen_snd[0], anzeigen_snd[1], 0, 0, 255])
                break
    iniz_back = infizierte
    print(karte.get_size())
    for zeig in anzeigen:
        print(zeig)
        karte.set_at((zeig[0], zeig[1]), (zeig[2], zeig[3], zeig[4]))
    pygame.display.flip()
    print ("Tag", tag, ": - akut Inf.: ", infizierte, "Summe:", infizierte_history, " - akut Intensivpat.: ", schwerkranke, "Summe:", schwerkranke_history, " - Geheilte:", geheilte, " - Tote:", tote)
