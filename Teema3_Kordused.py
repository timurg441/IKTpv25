#Töö 3.1
#1. Sisestatakse 15 arvu.
# Määrata, mitu neist on täisarvud.
##k=0 # loendur
from math import e

k=0 # loendur
for i in range(15):
    while True:
     try:
       arv=float(input(f"Sisesta {i+1}. arv: "))
       break
     except:
         print("Vale andmetüüp!")

    if int(arv)==arv:
     print(f"{arv} on täisarv.")
     k+=1
print(f"Täisarve oli kokku {k} tk.")

#2. Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
while True:
    try:
        A=int(input("Sisesta A: "))
        break
    except:
        print("Vale andmetüüp!")
for i in range(1,A+1):
    s=s+i
print(f"Summa vahemikus 1 kuni {A} võrdub {s}.")

#3. Sisestatakse 8 arvu.
# Leida nende korrutis (ainult positiivsete arvude puhul).
korrut = 1
for i in range(8):
    while True:
     try:
       arv=float(input(f"Sisesta {i+1}. arv: "))
       if arv>0: break
     except:
         print("Vale andmetüüp!")
     korrutis*=arv
print(f"Korrutis võrdub {korrutis}.")

#4. Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
for i in range(10,21):
    print(f"Arv {i} ruut on {i**2}.")

#5. Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N väärtus sisestatakse klaviatuurilt.
while True:
    try:
        N=int(input("Sisesta N: "))
        break
    except:
        print("Vale andmetüüp!")

#6. Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis määrab sisestatud arvude seast: negatiivsete arvude arvu, positiivsete arvude arvu, nullide arvu.
# (N väärtus sisestatakse klaviatuurilt.)
neg=0
pos=0
nul=0
while True:
    try:
        N=int(input("Sisesta N: "))
        break
    except:
        print("Vale andmetüüp!")
        for i in range(N):
            while True:
                try:
                    arv=float(input(f"Sisesta {i+1}. arv: "))
                    break
                except:
                    print("Vale andmetüüp!")
            if arv<0:
                neg+=1
            elif arv>0:
                pos+=1
            else:
                nul+=1
                print(f"Negatiivseid arve oli {neg} tk, positiivseid arve oli {pos} tk ja nulle oli {nul} tk.")

#7. Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].
while True:
    try:
        A=int(input("Sisesta A: "))
        B=int(input("Sisesta B: "))
        K=int(input("Sisesta K: "))
        break
    except:
        print("Vale andmetüüp!")