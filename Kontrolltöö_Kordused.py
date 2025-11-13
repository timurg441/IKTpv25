# 7. variant
# 1️. Kirjuta programm, mis antud arvu n (1–9) põhjal kuvab ekraanile n kujundit.
# Kahe kujundi vahel on tühikurida.
#  ^
# / /
# \ \
#  / /
#  __
while True:
    try:
        n = int(input("Sisesta arv 1–9: "))
        if 1 <= n <= 9:
            break
        else:
            print("Palun sisesta arv vahemikus 1–9")
    except:
        print("See ei ole korrektne arv. Proovi uuesti")

for i in range(n):
    print("  ^  ")
    print(" / / ")
    print(" \\ \\ ")
    print("  / / ")
    print("  __  ")
    if i < n - 1:
        print()


# 2️. T sõpra tulid restorani. Sissepääsu juures on robotvalvur, kes laseb sisse ainult üle 16-aastased.
# Selgita, mitu sõpra pääseb õhtusöögile.
sopru = input("Mitu sõpra tuli? ")

while not sopru.isdigit():
    sopru = input("Palun sisesta ainult number: ")

sopru = int(sopru)
passeb = 0
i = 0

while i < sopru:
    vanus = input(f"Sõbra {i+1} vanus: ")
    
    while not vanus.isdigit():
        vanus = input("Palun sisesta vanus numbrina: ")
    
    vanus = int(vanus)
    
    if vanus > 16:
        passeb = passeb + 1
    
    i = i + 1

print(f"Restorani pääseb {passeb} sõpra")


# 3️. Loenda eraldi tüdrukute ja poiste arv, et paigutada sportlased hotellitubadesse.
# Võistlusele saabus X-liikmeline võistkond.
# Määra, mitu neist on poisid ja mitu tüdrukud.
# Otsusta, mitu inimest elab ühes toas ja mitu tuba tuleb broneerida.
voistkonna_suurus = int(input("Võistkonna suurus:"))
poiste_arv = int(input("Mitu poissi?"))
tudrukute_arv = voistkonna_suurus - poiste_arv

inimesi_toas = int(input("Mitu inimest ühes toas?"))

tuba_poistele = (poiste_arv + inimesi_toas - 1) // inimesi_toas
tuba_tudrukutele = (tudrukute_arv + inimesi_toas - 1) // inimesi_toas
kokku_tube = tuba_poistele + tuba_tudrukutele

print(f"Poisse: {poiste_arv}")
print(f"Tüdrukuid: {tudrukute_arv}")
print(f"Tubasi broneerida: {kokku_tube}")
print(f"{tuba_poistele} tuba poistele")
print(f"{tuba_tudrukutele} tuba tüdrukutele")

# 4️. Küsitle O kasutajat, selgita välja nende kaal, pikkus ja vanus.
# Arvuta kehamassiindeks (BMI) ja teavita kasutajat tema tulemuse tähendusest.
kaal = float(input("Sisesta oma kaal (kg): "))
pikkus = float(input("Sisesta oma pikkus (m): "))
vanus = int(input("Sisesta oma vanus: "))

bmi = kaal / (pikkus * pikkus)

if bmi < 18.5:
    print("Alakaaluline")
elif bmi < 25:
    print("Normaalkaal")
elif bmi < 30:
    print("Ülekaaluline")
else:
    print("Rasvumine")


# 5️. Kontrolli N inimese isikukoodi (11 sümbolit).
# Määra isiku sugu.
# Kuva, mitu meest ja mitu naist sisestatud N inimese seas on.
mehi = 0
naisi = 0

N = int(input("Mitu isikukoodi sisestad? "))

for i in range(N):
    kood = input("Sisesta isikukood: ")

    if len(kood) != 11:
        print("Vigane isikukood!")
    else:
        if kood[0] == '1' or kood[0] == '3' or kood[0] == '5':
            print("Mees")
            mehi += 1
        elif kood[0] == '2' or kood[0] == '4' or kood[0] == '6':
            print("Naine")
            naisi += 1
        else:
            print("Vigane esimene number!")

print("Mehi kokku:", mehi)
print("Naisi kokku:", naisi)
