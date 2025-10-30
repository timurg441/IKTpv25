# 7. variant
# 1️. Kirjuta programm, mis antud arvu n (1–9) põhjal kuvab ekraanile n kujundit.
# Kahe kujundi vahel on tühikurida.
#  ^
# / /
# \ \
#  / /
#  __

#while True:
#    try:
#        n = int(input("Sisesta arv 1–9: "))
#        if 1 <= n <= 9:
#            for i in range(n):
#                print("  ^  ")
#                print(" / / ")
#                print(" \\ \\ ")
#                print("  / / ")
#                print("  __  ")
#               if i < n - 1:
#                    print()
#            break
#        else:
#            print("Palun sisesta arv vahemikus 1–9.")
#    except:
#        print("See ei ole korrektne arv. Proovi uuesti.")


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
while True:
    try:
        X = int(input("Sisesta võistkonna liikmete arv: "))
        if X > 0: