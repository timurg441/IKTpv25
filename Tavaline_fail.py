from Mooduli_fail import *
#square() funktsiooni kasutamine
print("Arvutame ruudu pindala ja ümbermõõdu!")
#Kui tahad mitu korda arvutada, siis pane tsükkel
külg=float_kontroll(input("Sisesta ruudu külje pikkus: "))
ümbermõõt, pindala, diagonaal=square(külg)
print(f"Ruudu külg: {külg}")
print(f"Ruudu ümbermõõt: {ümbermõõt}")
print(f"Ruudu pindala: {pindala}")
print(f"Ruudu diagonaal: {diagonaal}")




#is_year_leap() funktstiooni kasutamine
for i in range(3):
    aasta=int_kontroll(input("Sisesta aasta: "))
    if is_year_leap(aasta):
        print(f"{aasta} on liigasta")
    else:
        print(f"{aasta} on tavaline aasta")




#arithmetic() funktsiooni kasutamine
print("Lahendame/testime 5 arvutehet!")
for i in range(5):

    arv1=float_kontroll(input("Sisesta esimene arv: "))
    arv2=float_kontroll(input("Sisesta teine arv:"))
    
    t=input("Sisesta tehe (+,-,*,/): ")
    tulemus=arithmetic(arv1, arv2, t)
    print(f"{arv1} {t} {arv2} = {tulemus}")