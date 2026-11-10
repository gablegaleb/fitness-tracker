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
        treninzi.append(trening)

    elif opcija == "2":
        print("Odabrano: Prikaži treninge")
        for broj, trening in enumerate(treninzi, start=1):
            for stavka, podatak in trening.items():
                if stavka == "naziv_tr":
                    print(f"Trening {broj} {podatak}")
                elif stavka == "datum_tr":
                    print(f"Datum: {podatak}\n")
            #print(trening)

    elif opcija == "3":
        print("Izašli ste iz aplikacije!")
        break

    else:
        print("Neispravan odabir!")