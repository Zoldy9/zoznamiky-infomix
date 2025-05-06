vysledok=0
with open("generuj_3.txt") as file:
    for line in file:
        cisla=[]
        for i in range(10):
            cisla.append(0)
        riadok=line.strip().split()
        for prvok in riadok:
            cisla[int(prvok)]+=1
        pocet=cisla.count(max(cisla))
        for i in range(pocet):
            vysledok+=cisla.index(max(cisla))
            cisla[cisla.index(max(cisla))]=0
print(vysledok)
            


