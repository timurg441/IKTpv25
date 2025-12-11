import random

def registreerimine(k, s):
    """Lisa uus kasutaja"""
    nimi = input("Uus nimi: ")
    
    if nimi in k:
        print("Nimi on juba olemas!")
        return
    
    print("1 - Automaatne parool")
    print("2 - Sisesta ise")
    valik = input("Valik: ")
    
    if valik == "1":
        parool = str(random.randint(1000, 9999))
        print(f"Parool: {parool}")
    elif valik == "2":
        parool = input("Sisesta parool: ")
    else:
        print("Vale!")
        return
    
    k.append(nimi)
    s.append(parool)
    print("OK!")

def autoriseerimine(k, s):
    """Logi sisse"""
    nimi = input("Nimi: ")
    
    if nimi not in k:
        print("Pole olemas!")
        return
    
    i = k.index(nimi)
    parool = input("Parool: ")
    
    if parool == s[i]:
        print("Õige!")
    else:
        print("Vale!")

def paroolivahetus(k, s):
    """Muuda parooli"""
    nimi = input("Nimi: ")
    
    if nimi not in k:
        print("Pole olemas!")
        return
    
    i = k.index(nimi)
    uus = input("Uus parool: ")
    s[i] = uus
    print("Muudetud!")

def paroolitaastamine(k, s):
    """Unustatud parool"""
    nimi = input("Nimi: ")
    
    if nimi not in k:
        print("Pole olemas!")
        return
    
    i = k.index(nimi)
    uus = str(random.randint(1000, 9999))
    s[i] = uus
    print(f"Uus parool: {uus}")