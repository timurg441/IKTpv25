# Töö 5.1
#Andmete kontrollimine
#float konverteerimine try except plokis
def float_kontroll(sisend:str)->float:
    """Kontrollib, kas sisestatud andmed on teisendatavad float arvuks
    :param str sisend: kasutaja sisestatud andmed
    :return/type: teisendtautd float arv
    """
    while True:
        try:
             arv=float(sisend)
             return arv
        except ValueError:
             sisend=input("Palun sisesta arv: ")
def int_kontroll(sisend:str)->int:
    """Kontrollib, kas sisestatud andmed on tesendatavad täisarvuks
    :param str sisend: kasutaja sisestatud andmed
    :return/rtype: teisendatud int arv
    """





# 1 Lihtsad aritmeetilised tehteid

def arithmetic(a:float,b:float,tehe:str)->any:
    """Lihtne kalkulaator:
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Muul juhul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float b: teine arv
    :param str tehe: tehe, mis tuleb teha
    :retur/rtype: tehte tulemus float või str
    """
    if tehe in ["+","-","*","/"]:
       if tehe=="/" and b==0:
          vastus= "Nulliga jagamine pole lubatud"
       else:
          vastus=eval(f"{a} {tehe} {b}") #tehe toostamine eval funktsiooniga
    else:
          vastus="Tundmatu tehe"
    return vastus

from Mooduli_fail import *

while True:
    try:
        arv1=float(input("Sisesta esimene arv: "))
        break
    except ValueError:
        print("Palun sisesta")
while True:
    try:
        arv2=float(input("Sisesta esimene arv: "))
        break
    except ValueError:
        print("Palun sisesta arv!")
t=input("Sisesta tehe (+,-,*,/): ")
tulemus=arithmetic(arv1,arv2,t)
print(f"{arv1} {t} {arv2} = {tulemus}")


# 2 Liigaasta
def is_year_leap(aasta:int)->bool:
    """Kontrollib, kas aasta on liigasta
    :param int aasta: aasta arvuna
    :return/type: True kui liigasta, False kui tavaline aasta
    """
    if (aasta % 4 == 0 and aasta % 100 != 0):
        return True
    else:
        return False

# 3 Ruut 
def square(külg:float)->any:
    """Arvutab ruudu ümbermõõdu




    ümbermõõt=4*külg
    pindala=külg**2 #või külg*külg
    diagonaal=külg**0.5*2
    """

# 4 Aastaajad
def season(kuu:int)->str:
    """Tagastab aastaaja kuu numbri põhjal
    :param int kuu: kuu number (1-12)
    :return/rtype: hooaja nimetus str
    """

    if kuu in [12,1,2]:
       return "talv"
    elif kuu in [3,4,5]:
       return "kevad"
    elif kuu in [6,7,8]:
       return "suvi"
    elif kuu in [9,10,11]:
       return "sügis"
    else:
       return "Vigane kuu number"

# 5 Pangahoiuss
def bank(a:float,years:int)->float:
     """Arvutab lõppsumma koos intressiga
     :param float a: algsumma
     :param int years: aastate arvs
     :return/rtype: lõppsumma float
     """
     intress==0.1 #10% intress
     for i in range(years):
         a+=a*intress
     return a

# 6