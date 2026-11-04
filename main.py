while True:
    print("--Fitnes tracker--")
    print("\n1. Dodaj trening \n2. Prikaži treninge \n3. Izlaz \n")
    opcija = input("Odaberi opciju: ")

    if opcija == "1":
        print("Odabrano: Dodaj trening")
    elif opcija == "2":
        print("Odabrano: Prikaži treninge")
    elif opcija == "3":
        print("Izašli ste iz aplikacije!")
        break
    else:
        print("Neispravan odabir!")