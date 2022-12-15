print("Adjon meg egy mértékegységet(cm, m, km):")
egyseg = input()
print("Adjon meg egy számot:")
szam = float(input())
while szam > 0:
    if szam > 0:
        print("Adja meg az átvltási mértékegységet")
        valt = input()
        eredmeny = -1

        if egyseg == "cm" and valt == "m":
            eredmeny = szam * 0.01
        elif egyseg == "cm" and valt == "km":
            eredmeny = szam * 0.00001
        elif egyseg == "cm" and valt == "cm":
            eredmeny = szam * 1

        elif egyseg == "m" and valt == "cm":
            eredmeny = szam * 100
        elif egyseg == "m" and valt == "km":
            eredmeny = szam * 0.001
        elif egyseg == "m" and valt == "m":
            eredmeny = szam * 1

        elif egyseg == "km" and valt == "m":
            eredmeny = szam * 1000
        elif egyseg == "km" and valt == "cm":
            eredmeny = szam * 100000
        elif egyseg == "km" and valt == "km":
            eredmeny = szam * 1
        else:
            print("Hibás Adat")

        print(eredmeny)
    else:
        print("Hibás szám")
