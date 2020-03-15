name = input("Wie heissen Sie? ")


geschlecht = input ("Sind Sie ein Männlein (m) oder eine Frau (f)?")

if geschlecht == "m":
    print ("Guten Tag, lieber ")
else:
    print ("Guten Tag, liebe ")

print (name)

if name == "Kevin" and geschlecht == "m" :
    print ("Hallo, Dich kenne ich ja schon...")
else:
    print ("Ei wer bist denn Du???")
    ergehen = input ("Wie geht es Dir?")
    if ergehen == "gut":
        print ("Na immerhin geht es Dir gut, Unbekannter!")
    else:
        print ("oje...")
        
wastun = input ("Was 
