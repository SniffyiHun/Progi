pozitiv_szam = int(input())
while pozitiv_szam < 0:
    pozitiv_szam = int(input())

for i in range(pozitiv_szam+1):
    if i % 2 == 0:
        print(i)
    elif i % 3 == 0 and i % 5:
        print(i*2)
    else:
        print("NO")