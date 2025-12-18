from MinuOmaMoodul import *
k=['Mari', 'Juku', 'Kati']
s=['1234', '5678', 'abcd']

while True:
    print("Vali tegevus:")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Paroolitaastamine")
    print("5 - Välju")
    valik = input("Sisesta valik (1-5): ")
    if valik == '1':
        registreerimine(k, s)
    elif valik == '2':
        autoriseerimine(k, s)
    elif valik == '3':
        muutmine(k, s)
    elif valik == '4':
        paroolitaastamine(k, s)
    elif valik == '5':
        print("Väljun programmist.")
        break
    else:
        print("Vigane valik, proovi uuesti.")
