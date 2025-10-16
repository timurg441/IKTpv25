#1. Päevade kontroll

paev=input("Sisesta päeva nimetus (nt esmaspäev): ")
#1. Kui on neljapäev, siis "Huraaa, Programmeerimine!
if paev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")

#2. Kui on neljapäev, siis "Huraaa, Programmeerimine, kui on reede, siis "Igatsen, programmeerimida tahaks!".
if paev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmeerimida tahaks!")

#3. Tööpäevad ja nädalavahetus
if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus!")
else:
    print("Tööpäev, pean tööl käima!")
# 1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4-neljapäev, 5-reede, 6-laupäev, 7-pühapäev
paev_number=int(input("Sisesta päeva number (1-7): "))
if paev_number==1:
    print("Esmaspäev")
elif paev_number==2:
     print ("Teisipäev")
elif paev_number==3:
     print("Kolmapäev")
elif paev_number==4:
     print("Neljapäev")
elif paev_number==5:
     print("Reede")
elif paev_number==6:
     print("Laupäev")
elif paev_number==7:
     print("Pühapäev")
else:
     print ("Vale number, sisesta 1-7 vahemikus")

# 1. Juku

# a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
# b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)
# <6 aastad  - tasuta
# 6-14 - lastepilet
# 15-65 - täispilet
# >65 - sooduspilet
# <0 ja >100 viga andmetega
eesnimi=input("Sisesta eesnimi: ")
if eesnimi=="JUKU": 
   print("Lähme Jukuga kinno!")
   vanus=input("Sisesta Juku vanus: ")
   if vanus.isdigit():
         vanus=int(vanus)
         if vanus<0 or vanus>100:
              print("Viga andmetega")
         elif vanus<6:
              print("Pilet on tasuta")
         elif vanus<=14:
              print("Lastepilet")
         elif vanus<=65:
              print("Täispilet")
         else:
              print("Sooduspilet")
   else:
         print("Palun sisesta vanus täisarvuna!")

#2. Pinginaabrid

# Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, kas nad on täna pinginaabrid või ei mitte.
nimi1=input("Sisesta esimese inimese nimi: ").capitalize()
nimi2=input("Sisesta teise inimese nimi: ").capitalize()
if nimi1.isalpha() and nimi2.isalpha():
   if nimi1=="Timur" and nimi2=="Yaroslav" or nimi1=="Yaroslav" and nimi2=="Timur":
    print(f"{nimi1} ja {nimi2} on täna pinginaabrid!")
   else:
    print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid!")
else:
    print("Palun sisesta ainult tähti sisaldavad nimed!")

# 3 Remont

# Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. 
# Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
# Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.
pikkus=input("Sisesta toa pikkus meetrites: ")
laius=input("Sisesta toa laius meetrites: ")
if pikkus>0 and laius>0:
    pindala = pikkus*laius
    print(f"Toa pindala on {pindala} ruutmeetrit.")
    user =input("Kas soovid teha remonti? (jah/ei): ").capitalize()
    if user.isalpha () and user == "Jah":
        hind=float(input("Kui palju maksab ruutmeeter?: "))
        if hind>0: 
            remont=pindala*hind
            print(f"Põranda vahetamise hind on {remont} eurot.")
            kes = input("Kas teed remonti ise või töötajaga? (ise/töötaja): ").capitalize()
            if kes.isalpha() and kes == "Ise":
             print ("Siis summa on {remondi_hind} eurot.")
            else:
             print (f"Siis summa on {remont + 300} eurot.")
        else:
            print("Hind ei saa olla negatiivne!")
    else:
        print("Remonti ei tehta.")
else:
    print("Arvud peavad olema suuremad kui 0.")

# 4 Allahindus

# Leia 30% soodustusega hinna, kui alghind on suurem kui 700
from curses.ascii import isdigit
hind=input("Sisesta toote alghind: ")
if hind.isdigit():
   hind = float(hind)
   if hind > 700:
       hind = hind * 0.7
       print(f"Toote hind on soodustusega {hind} eurot.")
   else:
       print(f"Toote hind on {hind} eurot.")

# 5 Temperatuur

# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
try:
   temp=float(input("Sisesta temperatuur: "))
   if temp>18:
         print("Soovitatav toasoojus talvel.")
   else:
         print("Võib olla jahe.")
except:
         print("Palun sisesta temperatuur numbrina!")

# 6 Pikkus

# Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)
try:
   pikkus=float(input("Sisesta inimese pikkus cm: "))
   if pikkus<155:
         print("Lühike")
   elif pikkus<=180:
         print("Keskmine")
   else:
         print("Pikk")
except:
         print("Palun sisesta pikkus numbrina!")

#7 Pikkus ja sugu

#Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).
try:
    pikkus=float(input("Sisesta pikkus cm: "))
    sugu=input("Sisesta sugu (mees/naine): ").capitalize()
    if sugu=="mees":
            if pikkus<165:
                  print("Lühike mees")
            elif pikkus<=175:
                  print("Keskmine mees")
            else:
                  print("Pikk mees")
    elif sugu=="naine":
            if pikkus<155:
                  print("Lühike naine")
            elif pikkus<=170:
                  print("Keskmine naine")
            else:
                  print("Pikk naine")
    else:
            print("Palun sisesta sugu kas mees või naine!")
except:
            print("Palun sisesta pikkus numbrina!")

#8 Poes

# Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. 
# Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).
import random
piim_hind=random.randint(1,5)
saia_hind=random.randint(1,5)
leib_hind=random.randint(1,5)
muna_hind=random.randint(1,5)
juust_hind=random.randint(1,5)
kohv_hind=random.randint(1,5)
print(f"Piima hind on {piim_hind} eurot.")
print(f"Saia hind on {saia_hind} eurot.")
print(f"Leiva hind on {leib_hind} eurot.")
print(f"Muna hind on {muna_hind} eurot.")
print(f"Juustu hind on {juust_hind} eurot.")
print(f"Kohvi hind on {kohv_hind} eurot.")
tooted=input("Millist toodet soovid osta? (piim/saia/leib/muna/juust/kohv): ").capitalize()
kogus=input("Mitu tükki soovid osta?: ")
if kogus.isdigit():
    kogus=int(kogus)
    if kogus>0:
        if tooted=="Piim":
            summa=piim_hind*kogus
            print(f"Ostetud {kogus} piima(t) hinnaga {summa} eurot.")
        elif tooted=="Saia":
            summa=saia_hind*kogus
            print(f"Ostetud {kogus} saia(t) hinnaga {summa} eurot.")
        elif tooted=="Leib":
            summa=leib_hind*kogus
            print(f"Ostetud {kogus} leiba(t) hinnaga {summa} eurot.")
        elif tooted=="Muna":
            summa=muna_hind*kogus
            print(f"Ostetud {kogus} muna(t) hinnaga {summa} eurot.")
        elif tooted=="Juust":
            summa=juust_hind*kogus
            print(f"Ostetud {kogus} juustu(t) hinnaga {summa} eurot.")
        elif tooted=="Kohv":
            summa=kohv_hind*kogus
            print(f"Ostetud {kogus} kohvi(t) hinnaga {summa} eurot.")
        else:
            print("Meil seda toodet ei ole!")
    else:
        print("Kogus peab olema suurem kui 0!")
# 9 Ruut

# Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
# Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.


# 10 Matemaatika

# Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
# Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

