import random

def registreerimine(k, s):
    """Registreerib uue kasutaja"""
    print("\n--- REGISTREERIMINE ---")
    
    nimi = input("Sisesta uus kasutajanimi: ")
    
    if nimi in k:
        print("Viga: See kasutajanimi on juba olemas!")
        return
    
    print("\nVali parooli meetod:")
    print("1 - Automaatne parool")
    print("2 - Sisesta ise")
    
    valik = input("Tee valik (1 või 2): ")
    
    if valik == "1":
        tahed = "abcdefghijklmnopqrstuvwxyz"
        suured = tahed.upper()
        numbrid = "0123456789"
        kogu = tahed + suured + numbrid + "!@#$%"
        
        parool = ""
        for i in range(8):
            parool += random.choice(kogu)
        
        print(f"Sinu parool: {parool}")
    
    elif valik == "2":
        while True:
            parool = input("Sisesta parool: ")
            
            if len(parool) < 4:
                print("Parool peab olema vähemalt 4 tähemärki!")
                continue
                
            break
    
    else:
        print("Vale valik!")
        return
    
    k.append(nimi)
    s.append(parool)
    print(f"Kasutaja {nimi} on edukalt registreeritud!")

def autoriseerimine(k, s):
    """Logib kasutaja sisse"""
    print("\n--- AUTORISEERIMINE ---")
    
    nimi = input("Kasutajanimi: ")
    
    if nimi not in k:
        print("Viga: Sellist kasutajat ei ole!")
        return
    
    indeks = k.index(nimi)
    
    parool = input("Parool: ")
    
    if parool == s[indeks]:
        print(f"Tere tulemast, {nimi}!")
    else:
        print("Vale parool!")

def paroolivahetus(k, s):
    """Muudab kasutaja parooli"""
    print("\n--- PAROOLI VAHETUS ---")
    
    nimi = input("Sisesta kasutajanimi: ")
    
    if nimi not in k:
        print("Viga: Sellist kasutajat ei ole!")
        return
    
    indeks = k.index(nimi)
    
    vana = input("Sisesta vana parool: ")
    
    if vana != s[indeks]:
        print("Vale vana parool!")
        return
    
    uus = input("Sisesta uus parool: ")
    
    if len(uus) < 4:
        print("Uus parool peab olema vähemalt 4 tähemärki!")
        return
    
    s[indeks] = uus
    print("Parool on edukalt muudetud!")

def paroolitaastamine(k, s):
    """Taastab unustatud parooli"""
    print("\n--- PAROOLI TAASTAMINE ---")
    
    nimi = input("Sisesta kasutajanimi: ")
    
    if nimi not in k:
        print("Viga: Sellist kasutajat ei ole!")
        return
    
    indeks = k.index(nimi)
    
    uus_parool = str(random.randint(1000, 9999))
    
    s[indeks] = uus_parool
    
    print(f"Sinu uus parool on: {uus_parool}")
    print("Ära unusta seda salvestada!")