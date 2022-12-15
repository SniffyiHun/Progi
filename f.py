homerseklet = float(input("Add meg az alap hőfokot "))
print("Add meg a mértékegységet. C = Celsius,F = Fahrenheit, K = Kelvin")
mertekegyseg = input()
print("Add meg az átváltó értéket (C, F, K):")
atvalt = input()

if mertekegyseg == "C":
    if atvalt == "F":
        F = homerseklet * 1.8 + 32
        print("A hőmérséklet", F, "Fahrenheitben")
    elif atvalt == "K":
        K = homerseklet + 273.15
        print("A hőmérséklet", K, "Kelvinben")

elif mertekegyseg == "F":
    if atvalt == "C":
        C = (homerseklet-32) / 1.8
        print("A hőmérséklet", C, "Celsiusban")
    elif atvalt == "K":
        K = (homerseklet - 32) / 1.8 + 273.15
        print("A hőmérséklet", K, "Kelvinben")

elif mertekegyseg == "K":
    if atvalt == "C":
        C = homerseklet - 273.15
        print("A hőmérséklet", C, "Celsiusban")
    elif atvalt == "F":
        F = (homerseklet - 273.15) * 1.8 + 32
        print("A hőmérséklet", F, "Fahrenheitben")
else:
    print("Hibás Adat")
