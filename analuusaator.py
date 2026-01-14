import glob
import os

def leia_projektifailid():
    laiend = input("Sisesta faililaiend (nt: txt, py, java): ")
    
    if not laiend.startswith("."):
        laiend = "." + laiend
    
    kõik_failid = os.listdir(".")
    leitud_failid = []
    
    for fail in kõik_failid:
        if os.path.isfile(fail) and fail.endswith(laiend):
            leitud_failid.append(fail)
    
    if leitud_failid:
        print(f"Leitud {len(leitud_failid)} fail(i) laiendiga {laiend}:")
        for f in leitud_failid:
            print(f"  - {f}")
    else:
        print(f"Ei leitud faile laiendiga {laiend}")
    
    return leitud_failid

def analyysi_faili_sisu():
    failinimi = input("Sisesta faili nimi: ")
    
    if not os.path.exists(failinimi):
        print("Sellist faili ei leitud!")
        return "Faili ei leitud"
    
    try:
        with open(failinimi, 'r', encoding='utf-8') as f:
            read = f.readlines()
        
        ridu_kokku = len(read)
        tyhjad_read = 0
        todo_count = 0
        fixme_count = 0
        
        for rida in read:
            puhas_rida = rida.strip()
            
            if puhas_rida == "":
                tyhjad_read += 1
            
            if "TODO" in rida.upper():
                todo_count += 1
            if "FIXME" in rida.upper():
                fixme_count += 1
        
        print(f"\nFaili {failinimi} analüüs:")
        print(f"  Ridu kokku: {ridu_kokku}")
        print(f"  Tühjad read: {tyhjad_read}")
        print(f"  TODO sõnu: {todo_count}")
        print(f"  FIXME sõnu: {fixme_count}")
        
        return {
            "fail": failinimi,
            "ridu": ridu_kokku,
            "tyhjad": tyhjad_read,
            "TODO": todo_count,
            "FIXME": fixme_count
        }
        
    except:
        print("Viga faili lugemisel!")
        return "Viga faili lugemisel"

def loo_raporti_kataloog():
    kataloogi_nimi = "Analüüsi_Raportid"
    
    if os.path.exists(kataloogi_nimi):
        print(f"Kataloog '{kataloogi_nimi}' on juba olemas!")
        return f"Kataloog {kataloogi_nimi} juba eksisteerib"
    
    os.mkdir(kataloogi_nimi)
    print(f"Loodud kataloog: {kataloogi_nimi}")
    
    return f"Loodud kataloog: {kataloogi_nimi}"

def leia_failid_algustahega():
    taht = input("Sisesta täht: ")
    
    if len(taht) != 1 or not taht.isalpha():
        print("Palun sisesta üks täht!")
        return "Vigane sisend"
    
    kõik_failid = os.listdir(".")
    leitud_failid = []
    
    for fail in kõik_failid:
        if os.path.isfile(fail) and fail.startswith(taht):
            leitud_failid.append(fail)
    
    if leitud_failid:
        print(f"Leitud {len(leitud_failid)} fail(i) tähega '{taht}':")
        for f in leitud_failid:
            print(f"  - {f}")
    else:
        print(f"Ei leitud faile tähega '{taht}'")
    
    return leitud_failid
