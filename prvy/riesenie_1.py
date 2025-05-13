indexy=[]
with open("generuj_1.txt") as file:
    for line in file:
        line1=[]
        line=line.strip().split()
        for cislo in line:
            line1.append(int(cislo))
        maximum=max(line1)
        if line1.index(maximum) not in indexy:
            indexy.append(line1.index(maximum))
vysledok=""
for prvok in indexy:
    vysledok+=f"{prvok}-"
print(vysledok[:-1])
