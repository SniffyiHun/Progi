szam = int(input())

logika = True

# for i in range(2,szam,1):

#    if szam % i == 0:
#        logika = False
J = 2
while logika and J < szam:
    if szam % J == 0:
        logika = False
    else:
        J = J+1

if logika:
    print("Primszám")
else:
    print("Nem Primszám")
