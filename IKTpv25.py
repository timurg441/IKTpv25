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