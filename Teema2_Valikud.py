paev=input("Sisesta päeva nimetus (nt esmaspäev): ")
#1. Kui on neljapäev, siis "Huraaa, Programmeerimine!
if päev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")

#2. Kui on neljapäev, siis "Huraaa, Programmeerimine, kui on reede, siis "Igatsen, programmeerimida tahaks!".
if päev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmeerimida tahaks!")

#3. Tööpäevad ja nädalavahetus
if päev.lower()=="laupäev" or päev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus!")
else:
    print("Tööpäev, pean tööl käima!")