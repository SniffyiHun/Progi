print("Adja meg a kezdő számot")
szam = float(input())
print("Adjon meg 5 számot:")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
if a + b + c + d + e > szam:
    print("Az 5 szám, átlaga:", (a + b + c + d + e) / 5)

else:
    print("Az 5 szám összegénke négyzete:", (a + b + c + d + e)**2)
