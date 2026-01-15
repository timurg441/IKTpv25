import analuusaator
import os

def näita_menüüd():
    print("\n" + "="*50)
    print("PROJEKTI ANALÜÜSJA")
    print("="*50)
    print("Praegune asukoht:", os.getcwd())
    print("="*50)
    print("1 - Otsi faile laiendi järgi")
    print("2 - Analüüsi faili sisu")
    print("3 - Loo raportikataloog")
    print("4 - Otsi faile algustähe järgi")
    print("5 - Loo raportifail")
    print("6 - Lõpeta ja salvesta")
    print("="*50)

def käivita_programm():
    print("Tere tulemud projekti analüüsijasse!")
    
    tegevuste_logi = []
    
    while True:
        näita_menüüd()
        valik = input("Vali tegevuse number (1-6): ").strip()
        
        if valik == "1":
            print("\nFailide otsimine")
            tulemus = analuusaator.leia_projektifailid()
            tegevuste_logi.append(("Failide otsimine", tulemus))
        
        elif valik == "2":
            print("\nFaili analüüs")
            tulemus = analuusaator.analyysi_faili_sisu()
            if tulemus:
                tegevuste_logi.append(("Faili analüüs", tulemus))
        
        elif valik == "3":
            print("\nKataloogi loomine")
            tulemus = analuusaator.loo_raporti_kataloog()
            tegevuste_logi.append(("Kataloogi loomine", tulemus))
        
        elif valik == "4":
            print("\nOtsing tähe järgi")
            tulemus = analuusaator.leia_failid_algustahega()
            tegevuste_logi.append(("Otsing tähe järgi", tulemus))
        
        elif valik == "5":
            print("\nFaili loomine")
            tulemus = analuusaator.loo_raporti_fail()
            tegevuste_logi.append(("Faili loomine", tulemus))
        
        elif valik == "6":
            print("\nProgramm lõpetab töö")
            
            if not os.path.exists("Analüüsi_Raportid"):
                print("Loon raportikataloogi...")
                os.mkdir("Analüüsi_Raportid")
            
            logi_fail = "Analüüsi_Raportid/programmi_logi.txt"
            
            with open(logi_fail, 'w', encoding='utf-8') as f:
                f.write("PROGRAMMI TEGEVUSTE LOOG\n")
                f.write("="*50 + "\n\n")
                
                for i, (tegevus, tulemus) in enumerate(tegevuste_logi, 1):
                    f.write(f"{i}. {tegevus}\n")
                    f.write(f"   Tulemus: {tulemus}\n")
                    f.write("-"*30 + "\n")
            
            print(f"Logi on salvestatud faili: {logi_fail}")
            print("Tänan programmi kasutamise eest! Head aega!")
            break
        
        else:
            print("Vigane valik! Palun vali number 1 kuni 6.")
        
        input("\nVajuta Enter, et jätkata...")

if __name__ == "__main__":
    käivita_programm()
