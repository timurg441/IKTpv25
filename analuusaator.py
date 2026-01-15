import os
import glob
import datetime

def leia_projektifailid():
    laiend = input("Sisesta faililaiend (näiteks: txt, py): ")
    
    if not laiend.startswith('.'):
        laiend = '.' + laiend
    
    failid = glob.glob(f'*{laiend}')
    
    if failid:
        print(f"Leitud {len(failid)} fail(i):")
        for fail in failid:
            print(f"  - {fail}")
    else:
        print(f"Ei leitud ühtegi faili laiendiga {laiend}")
    
    return failid

def analyysi_faili_sisu():
    while True:
        faili_tee = input("Sisesta faili nimi või tee: ")
        
        if not os.path.isfile(faili_tee):
            print("Sellist faili pole olemas! Proovi uuesti.")
            continue
        
        try:
            with open(faili_tee, 'r', encoding='utf-8') as f:
                sisu = f.read()
            
            read = sisu.split('\n')
            ridu_kokku = len(read)
            
            tyhjad_read = sum(1 for rida in read if rida.strip() == '')
            
            todo_count = sisu.upper().count('TODO')
            fixme_count = sisu.upper().count('FIXME')
            
            print("\nANALÜÜSI TULEMUSED:")
            print(f"Fail: {faili_tee}")
            print(f"Ridu kokku: {ridu_kokku}")
            print(f"Tühjad read: {tyhjad_read}")
            print(f"TODO märksõnu: {todo_count}")
            print(f"FIXME märksõnu: {fixme_count}")
            
            tulem = {
                'fail': faili_tee,
                'ridu': ridu_kokku,
                'tyhjad': tyhjad_read,
                'TODO': todo_count,
                'FIXME': fixme_count
            }
            return tulem
            
        except Exception as e:
            print(f"Tekkis viga: {e}")
            return None

def loo_raporti_kataloog():
    kataloogi_nimi = "Analüüsi_Raportid"
    
    if os.path.exists(kataloogi_nimi):
        print(f"Kataloog '{kataloogi_nimi}' on juba olemas.")
        valik = input("Kas soovid seda kasutada? (jah/ei): ").lower()
        if valik == 'jah':
            return f"Kasutatakse olemasolevat kataloogi: {kataloogi_nimi}"
    
    try:
        os.mkdir(kataloogi_nimi)
        print(f"Loodud uus kataloog: {kataloogi_nimi}")
        return f"Loodud kataloog: {kataloogi_nimi}"
    except Exception as e:
        print(f"Ei saanud kataloogi luua: {e}")
        return f"Viga: {e}"

def leia_failid_algustahega():
    while True:
        taht = input("Sisesta täht, millega failinimi algab: ").strip()
        
        if len(taht) == 1 and taht.isalpha():
            break
        print("Palun sisesta täpselt üks täht!")
    
    failid = []
    kõik_failid = os.listdir('.')
    
    for fail in kõik_failid:
        if os.path.isfile(fail) and fail.startswith(taht):
            failid.append(fail)
    
    if not failid:
        for fail in kõik_failid:
            if os.path.isfile(fail) and fail.startswith(taht.upper()):
                failid.append(fail)
    
    if failid:
        print(f"Leitud {len(failid)} fail(i) tähega '{taht}':")
        for fail in failid:
            print(f"  - {fail}")
    else:
        print(f"Ei leitud ühtegi faili tähega '{taht}'")
    
    return failid

def loo_raporti_fail():
    faili_nimi = input("Sisesta uue raportifaili nimi: ").strip()
    
    if not faili_nimi:
        print("Faili nimi ei saa olla tühi!")
        return "Viga: faili nimi puudub"
    
    if not faili_nimi.endswith('.txt'):
        faili_nimi += '.txt'
    
    try:
        with open(faili_nimi, 'w', encoding='utf-8') as f:
            f.write("=" * 40 + "\n")
            f.write("PROJEKTI ANALÜÜSI RAPORT\n")
            f.write("=" * 40 + "\n\n")
            f.write("Raport loodud: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M") + "\n")
            f.write("Automaatne analüüs\n\n")
        
        print(f"Raportifail '{faili_nimi}' on loodud!")
        
        vastus = input("Kas soovid faili midagi lisada? (jah/ei): ").lower()
        if vastus == 'jah':
            tekst = input("Kirjuta tekst, mida soovid lisada:\n")
            with open(faili_nimi, 'a', encoding='utf-8') as f:
                f.write(tekst + "\n")
            print("Tekst on lisatud!")
        
        return f"Loodud fail: {faili_nimi}"
        
    except Exception as e:
        print(f"Ei saanud faili luua: {e}")
        return f"Viga: {e}"
