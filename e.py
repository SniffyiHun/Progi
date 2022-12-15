# F to C = (F - 32) / 1.8
# C to F = C * 1,8 + 32
# K to C = K - 273.15
# C to K = C + 273.15
# K to F = (K - 273.15) * 1.8 + 32
# F to K = (F - 32)/1.8 + 273.15


homerseklet = float(input("Add meg az alap hőfokot "))
print("Add meg a mértékegységet. C = Celsius,F = Fahrenheit, K = Kelvin")
mertekegyseg = input()

if mertekegyseg == "C":
    F = homerseklet * 1.8 + 32
    K = homerseklet + 273.15
    print("A hőmérséklet Celsiusban: ", homerseklet)
    print("A hőmérséklet Fahrenheitben: ", F)
    print("A hőmérséklet Kelviben: ", K)
elif mertekegyseg == "F":
    C = (homerseklet-32) / 1.8
    K = (homerseklet - 32) / 1.8 + 273.15
    print("A hőmérséklet Fahrenheitben: ", homerseklet)
    print("A hőmérséklet Celsiusban: ", C)
    print("A hőmérséklet Kelvinben: ", K)
elif mertekegyseg == "K":
    C = homerseklet - 273.15
    F = (homerseklet - 273.15) * 1.8 + 32
    print("A Hőmérséklet Kelvinben", homerseklet)
    print("A hőmérséklet Fahrenheitben: ", F)
    print("A hőmérséklet Celsiusban: ", C)
else:
    print("Hibás Adat")
