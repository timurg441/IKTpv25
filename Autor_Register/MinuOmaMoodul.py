import random

def genereeri_parool():
    """Genereerib parooli"""
    erimargid = ".,:;!_*-+()/#¤%&"
    numbrid = '0123456789'
    vaikesed = 'qwertyuiopasdfghjklzxcvbnm'
    suured = vaikesed.upper()
    
    kogu = erimargid + numbrid + vaikesed + suured
    
    list_maargid = list(kogu)
    
    random.shuffle(list_maargid)
    
    parool = ""
    for i in range(12):
        parool += random.choice(list_maargid)
    
    return parool

def kontrolli_parool(parool):
    """Kontrollib kas parool on hea"""
    on_number = False
    for char in parool:
        if char.isdigit():
            on_number = True
            break
    
    on_vaike = False
    for char in parool:
        if char.islower():
            on_vaike = True
            break
    
    on_suur = False
    for char in parool:
        if char.isupper():
            on_suur = True
            break
    
    erimargid = ".,:;!_*-+()/#¤%&"
    on_erimark = False
    for char in parool:
        if char in erimargid:
            on_erimark = True
            break
    
    return on_number and on_vaike and on_suur and on_erimark

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
        parool = genereeri_parool()
        print(f"Parool: {parool}")
    elif valik == "2":
        while True:
            parool = input("Sisesta parool: ")
            if kontrolli_parool(parool):
                break
            print("Parool peab sisaldama:")
            print("- numbrit")
            print("- väikest tähte")
            print("- suurt tähte")
            print("- erimärki")
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

def muutmine(k, s):
    """Muuda nime või parooli"""
    nimi = input("Nimi: ")
    
    if nimi not in k:
        print("Pole olemas!")
        return
    
    i = k.index(nimi)
    
    print("1 - Muuda nime")
    print("2 - Muuda parooli")
    valik = input("Valik: ")
    
    if valik == "1":
        uus_nimi = input("Uus nimi: ")
        if uus_nimi in k:
            print("Nimi on juba olemas!")
            return
        k[i] = uus_nimi
        print("Nimi muudetud!")
    elif valik == "2":
        while True:
            uus_parool = input("Uus parool: ")
            if kontrolli_parool(uus_parool):
                s[i] = uus_parool
                print("Parool muudetud!")
                break
            print("Parool ei sobi!")
    else:
        print("Vale!")

def paroolitaastamine(k, s):
    """Unustatud parool"""
    nimi = input("Nimi: ")
    
    if nimi not in k:
        print("Pole olemas!")
        return
    
    i = k.index(nimi)
    uus_parool = genereeri_parool()
    s[i] = uus_parool
    print(f"Uus parool: {uus_parool}")
