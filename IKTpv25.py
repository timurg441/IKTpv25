# 1.
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

from PIL import Image
import matplotlib.pyplot as plt

# Открываем изображение из файла (например, 'photo.jpg' в той же папке, где этот скрипт)


import time
import tkinter as tk
from PIL import Image, ImageTk
import random

def open_image_window(image_path, screen_width, screen_height):
    window = tk.Toplevel()
    window.title("Photo")

    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()

    # Получаем размеры изображения
    img_width, img_height = img.size

    # Выбираем случайную позицию, чтобы окно целиком помещалось на экран
    x = random.randint(0, max(0, screen_width - img_width))
    y = random.randint(0, max(0, screen_height - img_height))

    # Задаём позицию окна
    window.geometry(f"{img_width}x{img_height}+{x}+{y}")

root = tk.Tk()
root.withdraw()

image_path = "images.jpg"

# Получаем размер экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

while True:
    open_image_window(image_path, screen_width, screen_height)
    root.update()
    



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

# 3.
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.

from random import *
laua_peal=randint(10,50) #juhuslik arv 10-50
print(f"Laual on {laua_peal} kommi")
võtab=int(input("Mitu kommi soovid võtta?")) #sisend võtab teisendab stringi täisarvuks
laua_peal-=võtab #laua_peak=laua_peal-võtab, võtab komnmid laualt maha
print(f"Laual on nüüd {laua_peal} kommi")

# 4.
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

from math import *
ümbermõõt=int(input("Sisesta puu ümbermõtt meetrites: ")) #int teisendab stringi täisarvuks

läbimõõt=ümbermõõt/3.14 #läbimõõt=ümbermõõt/pi
print(f"Puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

läbimõõt=ümbermõõt/pi #võib kasutada ka math raamatukogu
print(f"Puu läbimõõt on {läbimõõt:.2f} meetrit") #.2f tähendab 2 kohta pärast koma

# 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja sdf küsi kasutajalt.

# ТВОЙ ГИТХАБ БЫЛ ВЗЛОМАН, ОН ПЕРЕХОДИТ ПОД ВЛАДЕНИЕ ДЖОРДЖА ДРОИДА
