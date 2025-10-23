# Töö 2.3 Praktiline töö "Kehamassiindeksi (KMI) kalkulaator"
# Ülesanne: Kehamassiindeksi (KMI) kalkulaator
# Koosta programm, mis täidab järgmised tegevused:
# Kuvab ekraanile tervituse:
# "Tere! Olen sinu uus sõber - Python!"
#Palub kasutajal sisestada oma nime ja salvestab selle muutujasse nimi.
#Kuvab ekraanile sõnumi: nimi, oi kui ilus nimi!
#Küsib kasutajalt, kas ta soovib oma kehamassiindeksit (KMI) arvutada: nimi! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>
#Kui kasutaja vastab 1 (jah):
#Küsib kasutaja pikkust sentimeetrites ja salvestab selle täisarvuna muutujasse pikkus.
#Küsib kasutaja kehakaalu kilogrammides ja salvestab selle reaalarvuna muutujasse mass.
#Arvutab kehamassiindeksi (KMI) valemiga: 
#Kuvab kasutaja nime koos sõnumiga:
#"nimi! Sinu keha indeks on: indeks" (KMI kuvatakse ühe komakohaga).
#Kuvab KMI hinnangu vastavalt allolevale tabelile:
#Hinnang	KMI vahemik
#Tervisele ohtlik alakaal	< 16
#Alakaal	16 - 19
#Normaalkaal	20 - 25
#Ülekaal	26 - 30
#Rasvumine	31 - 35
#Tugev rasvumine	36 - 40
#Tervisele ohtlik rasvumine	> 40
#Kui kasutaja vastab 0 (ei):
#Kuvab ekraanile teate:
#"Kahju! See on väga kasulik info!"
#Kuvab tühja rea.
#Lõpetuseks kuvab hüvastijätu:
#"Kohtumiseni, nimi! Igavesti Sinu, Python!"
#Nõuded:
#✅ Programm peab kontrollima kasutaja sisestusi ja vältima vigaseid andmeid.
#✅ Veatöötluseks kasuta try-except plokki, et vältida vigade tekkimist valede sisendite puhul.

# Töö 2.3 Praktiline töö "Kehamassiindeksi (KMI) kalkulaator"
# Ülesanne: Kehamassiindeksi (KMI) kalkulaator

print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")

try:
    soov = input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah: ")

    if soov == "1":
        print("Indeksi leidmine")
        # Küsi pikkust kuni on õiges formaadis ja vahemikus 0-250
        while True:
            try:
                pikkus = int(input("Mis on sinu pikkus (cm)? "))
                if 0 < pikkus <= 250:
                    break
                else:
                    print("Pikkus peab olema vahemikus 0 kuni 250 cm!")
            except:
                print("Vale pikkuse formaat! Palun sisesta täisarv.")

        # Küsi massi kuni on õiges formaadis ja vahemikus 0-200
        while True:
            try:
                mass = float(input("Mis on sinu kaal (kg)? "))
                if 0 < mass <= 200:
                    break
                else:
                    print("Kaal peab olema vahemikus 0 kuni 200 kg!")
            except:
                print("Vale kaalu formaat! Palun sisesta reaalarv.")

        # Arvuta KMI
        indeks = round(mass / (0.01 * pikkus) ** 2, 2)
        print(f"{nimi}! Sinu kehamassiindeks on: {indeks}")
        # Hinda KMI. Tee seda ise

    elif soov == "0":
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vale valik! Palun sisesta 0 või 1.")

except:
    print("Tekkis viga sisendi töötlemisel!")

print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
