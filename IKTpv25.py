# 1.
# Kirjuta enda esimene programm, mis v�ljastab k�sureale teksti: �Tere, maailm!�. 
# K�si kasutaja nimi ja muuda tekst, et ta n�eks v�lja nii: �Tere, maailm! Tervitan sind Mati�, kui kasutaja nimi on Mati.
# K�si kasutajalt sisend tema vanuse kohta ning v�ljasta see ekraanile:
# �Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.�

print("Tere maailm!")
nimi=input("Sisesta oma nimi: ").capitalize()#sisend ja ootab enterit
print(f"Tere maailm! Tervitan sind {nimi}")
vanus=int(input("Sisesta oma vanus: "))#int teisendab stringi t�isarvuks
print(f"Tere maailm! Tervitan sind {nimi.upper()}. Sa oled {vanus} aastat vana!")#upper teeb suurt�hed
print(f"Tere maailm! Tervitan sind {nimi.lower()}. Sa oled {vanus} aastat vana!")#lower teeb v�iket�hed

# 2.
# Mis t��pi on j�rgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 1.65
# d) kas_k�ib_koolis = True
# Mis v�imalus veel peale True oleks viimast muutujat v��rtustada? Kuidas v�iks nende muutujate v��rtusi koodis kontrollida?
# Kirjuta kood t��pide kontrollimiseks.
vanus = 18             #int
eesnimi = "Jaak"       #str
pikkus = 1.65          #float
kas_k�ib_koolis = True #bool
print("vanus {vanus} on: {type(vanus)}")
print("eesnimi {eesnimi} on: {type(eesnimi)}")
print("pikkus {pikkus} on: {type(pikkus)}")
print("kas_k�ib_koolis {kas_k�ib_koolis} on: {type(kas_k�ib_koolis)}")