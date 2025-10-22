
# 1.
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print("Tere maailm!")
nimi=input("Sisesta oma nimi: ").capitalize()#sisend ja ootab enterit
print(f"Tere maailm! Tervitan sind {nimi}")
vanus=int(input("Sisesta oma vanus: "))#int teisendab stringi täisarvuks
print(f"Tere maailm! Tervitan sind {nimi.upper()}. Sa oled {vanus} aastat vana!")#upper teeb suurtähed
print(f"Tere maailm! Tervitan sind {nimi.lower()}. Sa oled {vanus} aastat vana!")#lower teeb väiketähed

# 2.
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 1.65
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

vanus = 18             #int
eesnimi = "Jaak"       #str
pikkus = 1.65          #float
kas_käib_koolis = True #bool
print("vanus {vanus} on: {type(vanus)}")
print("eesnimi {eesnimi} on: {type(eesnimi)}")
print("pikkus {pikkus} on: {type(pikkus)}")
print("kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

# 3.
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.

from random import *
laua_peal=randint(10,50) #juhuslik arv 10-50
print(f"Laual on {laua_peal} kommi")
võtab=int(input("Mitu kommi soovid võtta?")) #sisend võtab teisendab stringi täisarvuks
laua_peal-=võtab #laua_peak=laua_peal-võtab, võtab komnmid laualt maha
print(f"Laual on nüüd {laua_peal} kommi")

# 4.
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

from math import *
ümbermõõt=int(input("Sisesta puu ümbermõtt meetrites: ")) #int teisendab stringi täisarvuks

läbimõõt=ümbermõõt/3.14 #läbimõõt=ümbermõõt/pi
print(f"Puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

läbimõõt=ümbermõõt/pi #võib kasutada ka math raamatukogu
print(f"Puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

# 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
<<<<<<< HEAD
import math

N = float(input("Sisesta ristküliku pikkus (N): "))
M = float(input("Sisesta ristküliku laius (M): "))

diagonaal = math.sqrt(N**2 + M**2)
print("Ristküliku diagonaal on:", diagonaal)

# 6.
# Leidke järgnevast näiteprogrammist loogiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# 7.
# Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
# Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.

# 8. 
# Joonista samasugune konn
#    @..@
#   (----)
#  ( \__/ )
#  ^^ "" ^^  
print("   @..@")
print("   (----)")
print("  ( \\__/ )")
print('^^ "" ^^')


# 9.
# Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
a = int(input("Sisesta külg a: "))
b = int(input("Sisesta külg b: "))
c = int(input("Sisesta külg c: "))

P = a + b + c
print("Kolmnurga ümbermõõt on:", P)

# 10.
# Pitsa
# Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
# Jätate teenindajale 10% jootraha.
# Koosta programm, mis arvutab, kui palju igaüks peab maksma.

hind = 12.90
inimesed = int(input("Mitu inimest jagab pitsa? "))
=======
from math import *
import math

N = float(input("Sisesta ristküliku pikkus (N): "))
M = float(input("Sisesta ristküliku laius (M): "))

diagonaal = math.sqrt(N**2 + M**2)
print("Ristküliku diagonaal on:", diagonaal)

# 6.
# Leidke järgnevast näiteprogrammist loogiline viga:
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# 7.
# Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
# Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.

# 8. 
# Joonista samasugune konn
#    @..@
#   (----)
#  ( \__/ )
#  ^^ "" ^^  
print("   @..@")
print("   (----)")
print("  ( \\__/ )")
print('^^ "" ^^')


# 9.
# Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
a = int(input("Sisesta külg a: "))
b = int(input("Sisesta külg b: "))
c = int(input("Sisesta külg c: "))

P = a + b + c
print("Kolmnurga ümbermõõt on:", P)

# 10.
# Pitsa
# Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
# Jätate teenindajale 10% jootraha.
# Koosta programm, mis arvutab, kui palju igaüks peab maksma.

hind = 12.90
inimesed = int(input("Mitu inimest jagab pitsa? "))