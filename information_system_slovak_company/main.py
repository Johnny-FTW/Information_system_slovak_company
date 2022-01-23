
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Manager(Person):
    def __init__(self, name, surname):
        super().__init__(name,surname)

    def __str__(self):
        return f"Manager, name:{self.name} surname:{self.surname}"

class Technik(Person):
    def __init__(self, name, surname):
        super().__init__(name,surname)

    def __str__(self):
        return f"Technik, name:{self.name} surname:{self.surname}"

class Obchodak(Person):
    def __init__(self, name, surname, pocet_zakaziek, technik = None):
        super().__init__(name,surname)
        self.pocet_zakaziek = pocet_zakaziek
        self.technik = technik

    def __str__(self):
        return f"Obchoďák, name:{self.name} surname:{self.surname} počet zákaziek:{self.pocet_zakaziek} technik:{self.technik}"

class Produkt:
    def __init__(self, produkt, manager, technici = None):
        self.produkt = produkt
        self.manager = manager
        self.technici = technici or []

    def add_technik(self, technik):
        self.technici.append(technik)

    def __str__(self):
        dalimiter= "\n\t"
        return f"Produkt:{self.produkt}\n\t{self.manager}\n\t{dalimiter.join([technik.__str__() for technik in self.technici])}"


class Information_system:
    def __init__(self, managers = None, technici = None, obchodaci = None, produkty = None):
        self.managers = managers or []
        self.technici = technici or []
        self.obchodaci = obchodaci or []
        self.produkty = produkty or []

    def add_technik(self):
        print("Technik:")
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")
                print("Vyber produkt: ")
                for counter, produkt in enumerate(self.produkty):
                    print(f"{counter}, {produkt}")
                produkt_id = int(input("Produkt_id: "))
                if produkt_id < 0 or produkt_id > len(self.produkty):
                    raise Exception("Error - wrong input")
            except Exception as e:
                print(e)
                print("Error - wrong input")
                continue
            break
        technik = Technik(name, surname)
        self.produkty[produkt_id].add_technik(technik)
        self.technici.append(technik)

    def add_manager(self):
        print("Manager:")
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")

            except Exception as e:
                print(e)
                print("Error - wrong input")
                continue
            break
        manager = Manager(name, surname)
        self.managers.append(manager)

    def add_obchodak(self):
        print("Obchodak:")
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")
                pocet_zakaziek = input("Pocet zakaziek: ")
                print("Vyber prisluchajuceho technika: ")
                for counter, technik in enumerate(self.technici):
                    print(f"{counter}, {technik}")
                technik_id = int(input("Technik_id: "))
                if technik_id < 0 or technik_id > len(self.technici):
                    raise Exception("Error - wrong input")

            except Exception as e:
                print(e)
                print("Error - wrong input")
                continue
            break
        obchodak = Obchodak(name, surname, pocet_zakaziek, technik.surname)
        self.obchodaci.append(obchodak)


    def add_produkt(self):
        print("Produkt:")
        while True:
            try:
                name = input("Name: ")
                counter = 0
                print("Chose your manager:")
                for manager in self.managers:
                    print(f"{counter}, {manager}")
                    counter +=1
                manager_id = int(input("Manager id:"))
                if manager_id < 0 or manager_id > len(self.managers):
                    raise Exception("Error - wrong input")
            except Exception as e:
                print(e)
                print("Error - wrong input")
                continue
            break
        produkt = Produkt(name, self.managers[manager_id])
        self.produkty.append(produkt)

def print_menu():
    print("--------------------------------------------")
    print("Vitajte v systeme")
    print("Stlačte prosím:")
    print("\t[0] Pre pridanie manazera")
    print("\t[1] Pre pridanie produktu")
    print("\t[2] Pre pridanie technika")
    print("\t[3] Pre pridanie obchodaka")
    print("\t[4] Pre ukončenie práce so systémom")
    print("\t[5] Pre zoznam produktov")
    print("\t[6] Pre zoznam technikov")
    print("\t[7] Pre zoznam managerov")
    print("\t[8] Pre zoznam obchodakov")

inf_syst = Information_system()

while True:
    print_menu()
    try:
        menu_choice = int(input("Menu choice: "))
        if menu_choice <0 or menu_choice > 8:
            raise Exception("Wrong menu choice")
    except Exception as e:
        print(e)
        print("Error - wrong input")
        continue
    if menu_choice == 4:
        print("Good bye")
        break
    elif menu_choice == 0:
        inf_syst.add_manager()
    elif menu_choice == 1:
        if len(inf_syst.managers) == 0:
            print("Najskor pridaj manazera")
        else:
            inf_syst.add_produkt()
    elif menu_choice == 2:
        if len(inf_syst.produkty) == 0:
            print("Najskor pridaj produkt")
        else:
            inf_syst.add_technik()
    elif menu_choice == 3:
        if len(inf_syst.technici) == 0:
            print("Najskor pridaj technika")
        else:
            inf_syst.add_obchodak()
    elif menu_choice == 5:
        if len(inf_syst.produkty) == 0:
            print("V systeme nie su produkty")
        else:
            print("Produkty: ")
            for produkt in inf_syst.produkty:
                print(produkt)
    elif menu_choice == 6:
        if len(inf_syst.technici) == 0:
            print("V systeme nie su technici")
        else:
            print("Technici: ")
            for technik in inf_syst.technici:
                print(technik)
    elif menu_choice == 7:
        if len(inf_syst.managers) == 0:
            print("V systeme nie su manazeri")
        else:
            print("Manazeri: ")
            for manager in inf_syst.managers:
                print(manager)
    elif menu_choice == 8:
        if len(inf_syst.obchodaci) == 0:
            print("V systeme nie su obchodaci")
        else:
            print("Obchodaci: ")
            for obchodak in inf_syst.obchodaci:
                print(obchodak)


