# 1️ Sõna või lause analüüs
# Sisesta sõna või lause.
# Loenda:
# mitu täishäälikut 
# mitu kaashäälikut 
# kui sisestati lause – loenda ka tühikud ja kirjavahemärgid
import string
t=['a','e','i','o','u','õ','ä','ö','ü']
k=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y']
m=string.punctuation + string.whitespace
sõna_lause=input("Sisesta sõna või lause: ").lower()
täishäälikud=0
kaashäälikud=0
märgid=0
for täht in sõna_lause:
    if täht in t:
        täishäälikud+=1
    elif täht in k:
        kaashäälikud+=1
    elif täht in m:
        märgid+=1
print(f"Sõnas või lauses on {täishäälikud} täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} tühikut või kirjavahemärki.")

# 2.1 Nimed
# Küsi kasutajalt viis nime.
#Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.
# Kuva viimane lisatud nimi.
# Lisa võimalus nimekirjas olevaid nimesid muuta
nimed = []
for i in range(5):
    nimi = input(f"Sisesta {i+1}. nimi: ")
    nimed.append(nimi)

nimed.sort()
print("Nimed tähestikulises järjekorras:")
for n in nimed:
    print(n)

print(f"Viimane lisatud nimi on: {nimed[-1]}")

while True:
    muuda = input("Kas soovid mõnda nime muuta? (jah/ei): ").lower()
    
    if muuda == "jah":
        vana_nimi = input("Sisesta vana nimi: ")
        if vana_nimi in nimed:
            uus_nimi = input("Sisesta uus nimi: ")
            indeks = nimed.index(vana_nimi)
            nimed[indeks] = uus_nimi
            
            nimed.sort()
            print("Uuendatud nimed tähestikulises järjekorras:")
            for n in nimed:
                print(n)
            print(f"Viimane lisatud nimi on: {nimed[-1]}")
        else:
            print("Nime ei leitud nimekirjast.")
    
    elif muuda == "ei":
        print("Nime muutmine lõpetatud.")
        break
    
    else:
        print("Palun sisesta 'jah' või 'ei'")

# 2.2 Kordustega nimed
# Antud on loend kordustega.
# Koosta programm, mis väljastab nimed ilma kordusteta.
nimed = ["Mari", "Jüri", "Anna", "Mari", "Peeter", "Kati", "Jüri", "Anna", "Mari"]

unikaalsed_nimed = list(set(nimed))

print("Algne loend:", nimed)
print("Nimed ilma kordusteta:", sorted(unikaalsed_nimed))
print("Korduste arv:")
for nimi in sorted(unikaalsed_nimed):
    kordusi = nimed.count(nimi)
    print(f"{nimi}: {kordusi} korda")

# 2.3 Vanused
# Koosta vanuste loend ja leia:
# suurim
# väikseim
# kogusumma
# keskmine
# Vanuste loend
vanused = [25, 18, 42, 33, 21, 67, 19, 29, 55, 38]

suurim = max(vanused)
väikseim = min(vanused)
kogusumma = sum(vanused)
keskmine = sum(vanused) / len(vanused)

print("Vanuste loend:", vanused)
print(f"Suurim vanus: {suurim}")
print(f"Väikseim vanus: {väikseim}")
print(f"Vanuste kogusumma: {kogusumma}")
print(f"Keskmine vanus: {keskmine:.2f}

# 3️ Tärnide lintdiagramm
# Kasuta loendis olevaid arve ja joonista tärnidega diagramm.
# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************
arvud = [18, 19, 32, 41, 52, 14]

print("=" * 50)

for arv in arvud:
    print('*' * arv)

# 4️ Postiindeks 
# Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:
# 1 – Tallinn 
# 2 – Narva, Narva-Jõesuu 
# 3 – Kohtla-Järve 
# 4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa 
# 5 – Tartu linn 
# 6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa 
# 7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa 
# 8 – Pärnumaa 
# 9 – Läänemaa, Hiiumaa, Saaremaa
# Kontrolli kasutaja sisestatud postiindeksit.
# Näita, millisesse maakonda see kuulub.
# Erireegel:
# Tallinn, Narva, Kohtla-Järve → „Mine merre!”
# Teised → „Mine metsa!”
indexid=["Tallinn","Narva","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        index=int(input("Sisesta oma postiindeks (5-kohaline arv): "))
        if 10000<=index<=99999: #len(str(index))==5)
            break
        else:
            print("Postiindeks peab olema 5-kohaline arv.")
    except:
        print("vigane andmetüüp")
index_list=list(str(index)) # index=37521 -> list("37521") -> ["3","7","5","2","1"]
n1=int(index_list[0]) #esimene number -> "3" -> int("3")=3
print(f"Sinu postiindeksiga {index} kuulud piirkonda: {indexid[n1-1]}")
if n1 in [1,2,3]:
    print("Mine merre!")
else:
    print("Mine metsa!")

# 5️ Vahetus
# Vaheta loendis esimene ja viimane element, teine ja eelviimane jne.
# Küsi kasutajalt, mitu paari vahetada. loendis on min 2 elem.
import random


loend_arvud=[]
loend_tähed= []
mitu=random.randint(2,20)
for i in range(mitu):
    elem=random.randint(1,100)
    loend_arvud.append(elem)
    täht=chr(random.randint(65,90))
print(loend_arvud)
while 1:
    try:
        user = int(input(f"Sisesta mitu paari soovid vahetada (max {mitu//2}): "))
        if 1 <= user <= mitu//2:
            break
        else:
            print(f"Vale sisestus.(max {mitu//2} )")

    except:
        print("Vale andmetüüp, proovi uuesti.")
        continue


for i in range(user):
    loend_arvud[i], loend_arvud[-(i+1)] = loend_arvud[-(i+1)], loend_arvud[i]
print("Vahetatud loend: ", loend_arvud)

# 6️ „Arvud“
# Leia loendi suurim arv, jaga see loendi pikkusega ja asenda see tulemusena.
loend_arvud=[]
mitu=randint(2,90) # loendi pikkus
for i in range(mitu):
    elem=random.randint(1,100) # juhuslik arv 0-100
    loend_arvud.append(elem)
print(f"Alguses loend: {loend_arvud}")
suurim=max(loend_arvud)
kus_asub=loend_arvud.index(suurim) # leiame suurima arvu indeksi
kogus=len(loend_arvud) # loendi pikkus
suurim_muudatud=suurim/mitu 
loend_arvud[kus_asub]=round(suurim_muudatud,2) # muudame suurima väärtuse ja ümardame 2 kohta pärast koma
print(f"Muutmise järel: {loend_arvud}")

#7 Sorteerimine 
# Sorteeri nimekiri numbreid absoluutväärtuse järgi
# kasvavalt
# või kahanevalt
loend = [15, -8, 23, -45, 12, 67, -34, 89, -5, 28]

print("Algne loend:", loend)

valik = input("Kas soovid sorteerida kasvavalt (k) või kahanevalt (v)? ")

if valik == "k":
    uus_loend = sorted(loend, key=abs)
    print("Kasvavalt:", uus_loend)
elif valik == "v":
    uus_loend = sorted(loend, key=abs, reverse=True)
    print("Kahanevalt:", uus_loend)
else:
    print("Vale valik! Sisesta 'k' või 'v'")

# 8️⃣ Võrdse pikkusega sõned 🧱

loend1 = ['tamm', 'taevas', 'elevant']
print("Algne 1:", loend1)

pikim1 = max(len(s) for s in loend1)

uus1 = []
for s in loend1:
    uus1.append(s + '_' * (pikim1 - len(s)))

print("Tulemus 1:", uus1)
print()

loend2 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
print("Algne 2:", loend2)

pikim2 = max(len(s) for s in loend2)
uus2 = []
for s in loend2:
    uus2.append(s + '_' * (pikim2 - len(s)))

print("Tulemus 2:", uus2)
print()

# Kolmas loend
loend3 = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
print("Algne 3:", loend3)

pikim3 = max(len(s) for s in loend3)
uus3 = []
for s in loend3:
    uus3.append(s + '_' * (pikim3 - len(s)))

print("Tulemus 3:", uus3)

# 9 Nime kontroll

n = input("Nimi: ")

if n.isalpha():
    print("Nimi OK")
    print("Tere, " + n.capitalize() + "!")
    print("Tähti:", len(n))
    
    t = "aeiouõäöü"
    taishaalikuid = sum(1 for c in n.lower() if c in t)
    print("Täishäälikuid:", taishaalikuid)
    print("Kaashäälikuid:", len(n) - taishaalikuid)
    
    tahed = sorted(set(n.lower()))
    print("Tähed a-z:", ''.join(tahed))
    
else:
    print("Vigane nimi!")

# 10 Töötajate andmed

t = [("Mari",25,1800), ("Jüri",32,2200), ("Anna",28,1950), 
     ("Peeter",45,3500), ("Kati",22,1700), ("Tanel",38,2800),
     ("Liisa",29,2000), ("Mart",41,3200)]

suurim = max(t, key=lambda x: x[2])
print("Suurim palk:", suurim[0], suurim[2], "€")

kesk_palk = sum(p[2] for p in t) / len(t)
print("Keskmine palk:", round(kesk_palk, 1), "€")

yle = sum(1 for p in t if p[2] > kesk_palk)
print("Üle keskmise:", yle)

kesk_vanus = sum(p[1] for p in t) / len(t)

noored = [p[1] for p in t if p[1] <= kesk_vanus]
kesk_noored = sum(noored) / len(noored)

# Grupp 2: vanemad
vanemad = [p[1] for p in t if p[1] > kesk_vanus]
kesk_vanemad = sum(vanemad) / len(vanemad)

print("Keskmine vanus:", round(kesk_vanus, 1))
print("Vanus ≤ keskmine:", len(noored), "inimest, keskmine", round(kesk_noored, 1))
print("Vanus > keskmine:", len(vanemad), "inimest, keskmine", round(kesk_vanemad, 1))

# 11 Inglise tähestik
import string
tahed = list(string.ascii_lowercase)
print("Tähed:", tahed)

uus = []
for i in range(26):
    uus.append(chr(97 + i) * (i + 1))
    
print("Korrutised:", uus[:10])
print("... ja nii edasi")

# 1️2 Min ja max vahetamine 
import random

arvud = [random.randint(1, 100) for _ in range(10)]
print("Algne:", arvud)

mini = arvud.index(min(arvud))
maxi = arvud.index(max(arvud))

arvud[mini], arvud[maxi] = arvud[maxi], arvud[mini]

print("Pärast:", arvud)
