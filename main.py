from datetime import date



treninzi = [

]



while True:
    trening = {
        "naziv_tr": "",
        "datum_tr": ""
    }
    print("--Fitnes tracker--")
    print("\n1. Dodaj trening \n2. Prikaži treninge \n3. Izlaz \n")
    opcija = input("Odaberi opciju: ")
    
    

    if opcija == "1":
        print("Odabrano: Dodaj trening")
        naziv_unos = input("Unesi naziv treninga: ")
        datum = date.today()
        trening["naziv_tr"] = naziv_unos
        trening["datum_tr"] = datum
        print(f"naziv: {trening['naziv_tr']}")
        print(f"datum: {trening['datum_tr']}")
        treninzi.append(trening)

    elif opcija == "2":
        print("Odabrano: Prikaži treninge")
        for trening in treninzi:
            for ime, podatak in trening:
                print(ime, podatak)
            #print(trening)

    elif opcija == "3":
        print("Izašli ste iz aplikacije!")
        break

    else:
        print("Neispravan odabir!")