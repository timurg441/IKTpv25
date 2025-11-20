import msvcrt
#Sisestamise ajal asendatakse kõik tähed '@'-ga
täht=""
while True:
    t=msvcrt.getwch()
    print(t.replace(t, "@"), end="", flush=True)
    täht+=t
    if t=='\r':  #Enter
        break
    print()  
    print(täht)




#List-loend
#Loome listi
l=[] #tühi list
print(f"Listi algseis: {l}")

while True:
    print("Tee valik:")
    print("1-Lisa elemente\n2-Lisa elemente pos-le\n3-Eemalda elemente pos järgi")
    print("4-Eemalda element nime järgi")
    while True:
        try:
            valik=int(input())
            break
        except :
            print("Arvud: 1...n")
    print("Töö listiga")
    if valik==1:
        while True:
            try:
                i=int(input("Mitu elementi soovid lisada? "))
                if i>0:
                    break
                else:
                    print("Arvud on vaja >0")
            except:
                print("Täisarvud on vaja kasutada")
        for element_id in range(i):
            element=input(f"{element_id}. element:")
            l.append(element)
        
    elif valik==2:
        while True:
            try:
                pos=int(input(f"Positsioon kuhu soovid lisada (0-{len(l)}): "))
                if 0<=pos<=len(l):
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
            except:
                print("Täisarv on vaja kasutada")
        element=input("Sisesta element mida soovid lisada: ")
        l.insert(pos,element) #lisab elemendi soovitud positsioonile
    
    elif valik==3:
        while True:
            try:
                pos=int(input(f"Positsioon kust soovid eemaldada (0-{len(l)-1}): "))
                if 0<=pos<=len(l)-1:
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)-1}")
            except:
                print("Täisarv on vaja kasutada")
        eem_element=l.pop(pos) #eemaldab elemendi soovitud positsioonilt
        print(f"Eemaldatud element on {eem_element}")
    elif valik==4:
        element=input("Sisesta element mida soovid eemaldada: ")
        mitu=l.count(element)
        if mitu==0:
            print("Elementi ei leitud")
        else:
            for e in range(mitu):
                print(f"Eemaldame element '{element}' {l.index(element)} poeitsioonilt")
                l.remove(element) #eemaldab esileiud elemendi
        print(f"Eemaldati {mitu} elementi")               

    elif valik == 5:
        element_list = list(input("Sisesta elemendid komadega: "))
        l.extend(element_list)
        print("List laiendatud")

    elif valik == 6:
        l.sort()
        print("List sorteeritud:")
    
    elif valik == 7:
        l.reverse()
        print("List pööratud ümber:")
    
    elif valik == 8:
        l.clear()
        print("List on nüüd tühi")
    
    elif valik == 9:
        print("Praegune list:")   
    else:
        print("Vale valik, vali uuesti")
   

print(f"Uuendatud list on {l}")


    #loend.extend()
    #loend.sort()
    #loend.reverse()
    #loend.clear()
    #loend.list()