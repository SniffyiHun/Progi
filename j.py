nev = ["Martin", "Géza", "Niki", "Csilla", "Illango"]

szul_ev = [2000, 1998, 2005, 526, 2005]

kor = []

for i, j in zip(nev, szul_ev):
    print(i, " ", j)
    print(i, " ", 2022-j)
    kor.append(2022-j)

legoregebb = kor[0]
for i in kor:
    if i < legoregebb:
        legoregebb = i

legfiatalabb = kor[0]
for i in kor:
    if i > legfiatalabb:
        legfiatalabb = i
