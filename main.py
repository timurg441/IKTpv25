import os
import analuusaator

def kuva_menuu():
    print("\n" + "="*40)
    print("PROJEKTI ANALÜÜS")
    print("="*40)
    print("1 - Leia projektifailid")
    print("2 - Analüüsi faili sisu")
    print("3 - Loo raporti kataloog")
    print("4 - Leia failid algustähega")
    print("5 - Välju")
    print("="*40)

def main():
    print("Tere! See on projekti analüüsija.")
    print(f"Praegune kaust: {os.getcwd()}")
    
    tulemused = []
    
    while True:
        kuva_menuu()
        valik = input("Vali tegevus (1-5): ")
        
        if valik == "1":
            print("\nFailide otsing laiendi järgi")
            tulemus = analuusaator.leia_projektifailid()
            tulemused.append(("Failide otsing", tulemus))
            
        elif valik == "2":
            print("\nFaili analüüs")
            tulemus = analuusaator.analyysi_faili_sisu()
            tulemused.append(("Faili analüüs", tulemus))
            
        elif valik == "3":
            print("\nRaportikausta loomine")
            tulemus = analuusaator.loo_raporti_kataloog()
            tulemused.append(("Kataloogi loomine", tulemus))
            
        elif valik == "4":
            print("\nFailide otsing tähe järgi")
            tulemus = analuusaator.leia_failid_algustahega()
            tulemused.append(("Failide otsing tähe järgi", tulemus))
            
        elif valik == "5":
            print("Programm lõpetab töö...")
            break
            
        else:
            print("Vale valik! Palun vali 1-5.")
    
    print("\nStatistika salvestamine")
    
    if not os.path.exists("Analüüsi_Raportid"):
        os.mkdir("Analüüsi_Raportid")
    
    with open("Analüüsi_Raportid/statistika.txt", 'w', encoding='utf-8') as f:
        f.write("PROJEKTI ANALÜÜSI STATISTIKA\n")
        f.write("=" * 40 + "\n\n")
        
        for i, (tegevus, tulemus) in enumerate(tulemused, 1):
            f.write(f"{i}. {tegevus}:\n")
            f.write(f"   Tulemus: {tulemus}\n")
            f.write("-" * 40 + "\n")
    
    print("Statistika on salvestatud faili 'Analüüsi_Raportid/statistika.txt'")

if __name__ == "__main__":
    main()
