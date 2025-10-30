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
           for i in range(n):
               print("  ^  ")
               print(" / / ")
               print(" \\ \\ ")
               print("  / / ")
               print("  __  ")
               if i < n - 1:
                   print()
           break
       else:
           print("Palun sisesta arv vahemikus 1–9.")
   except:
       print("See ei ole korrektne arv. Proovi uuesti.")


# 2️. T sõpra tulid restorani. Sissepääsu juures on robotvalvur, kes laseb sisse ainult üle 16-aastased.
# Selgita, mitu sõpra pääseb õhtusöögile.
while True:
   try:
       T = int(input("Sisesta sõprade arv: "))
       if T > 0:
           count = 0
           for i in range(T):
               age = int(input(f"Sisesta sõbra {i+1} vanus: "))
               if age > 16:
                   count += 1
           print(f"{count} sõpra pääseb õhtusöögile.")
           break
       else:
           print("Palun sisesta positiivne arv.")
   except:
       print("See ei ole korrektne arv. Proovi uuesti.")

# 3️. Loenda eraldi tüdrukute ja poiste arv, et paigutada sportlased hotellitubadesse.
# Võistlusele saabus X-liikmeline võistkond.
# Määra, mitu neist on poisid ja mitu tüdrukud.
# Otsusta, mitu inimest elab ühes toas ja mitu tuba tuleb broneerida.
while true:
    try:
        x = int(input("sisesta võistkonna liikmete arv: "))
        if x > 0:
            poisid = 0
            tüdrukud = 0
            for i in range(x):
                while true:
                    sugu = input(f"sisesta liikme {i+1} sugu (p = poiss, t = tüdruk): ")
                    if sugu in ("p", "poiss"):
                        poisid += 1
                        break
                    elif sugu in ("t", "tüdruk"):
                        tüdrukud += 1
                        break
                    else:
                        print("viga: vali 'p' või 't'. proovi uuesti.")

# 4️. Küsitle O kasutajat, selgita välja nende kaal, pikkus ja vanus.
# Arvuta kehamassiindeks (BMI) ja teavita kasutajat tema tulemuse tähendusest.
while True:
    try:
        O = int(input("Mitu inimest küsitleda? "))
        if O <= 0:
            print("Palun sisesta positiivne arv.")
            continue

        for i in range(O):
            while True:
                try:
                    kaal = float(input(f"Sisesta inimese {i+1} kaal (kg): "))
                    if kaal > 0:
                        break
                    print("Palun sisesta positiivne kaal.")
                except:
                    print("See ei ole korrektne arv. Proovi uuesti.")

            while True:
                try:
                    pikkus = float(input(f"Sisesta inimese {i+1} pikkus (m): "))
                    if pikkus > 0:
                        break
                    print("Palun sisesta positiivne pikkus.")
                except:
                    print("See ei ole korrektne arv. Proovi uuesti.")

            while True:
                try:
                    vanus = int(input(f"Sisesta inimese {i+1} vanus (aastad): "))
                    if vanus > 0:
                        break
                    print("Palun sisesta positiivne vanus.")
                except:
                    print("See ei ole korrektne arv. Proovi uuesti.")

            bmi = kaal / (pikkus ** 2)
            print(f"Inimese {i+1} BMI on: {bmi:.2f}")

            if bmi < 18.5:
                print("Alakaal")
            elif bmi < 25:
                print("Normaalkaal")
            elif bmi < 30:
                print("Ülekaal")
        break
    except:
        print("See ei ole korrektne arv. Proovi uuesti.")

# 5️. Kontrolli N inimese isikukoodi (11 sümbolit).
# Määra isiku sugu.
# Kuva, mitu meest ja mitu naist sisestatud N inimese seas on.
while True:
    try:
        N = int(input("Sisesta inimeste arv: "))
        if N <= 0:
            print("Palun sisesta positiivne arv.")
            continue
        break
    except:
        print("Palun sisesta korrektne arv.")

mehed = 0
naised = 0

for i in range(N):
    while True:
        isikukood = input(f"Sisesta inimese {i+1} isikukood (11 sümbolit): ")
        if len(isikukood) == 11 and isikukood.isdigit():
            sugu_esimene_number = int(isikukood[0])
            if sugu_esimene_number % 2 == 1:
                mehed += 1
            else:
                naised += 1
            break
        else:
            print("Viga: Isikukood peab olema 11-kohaline number. Proovi uuesti.")
            print(f"Kokku mehi: {mehed}")
            print(f"Kokku naisi: {naised}")
