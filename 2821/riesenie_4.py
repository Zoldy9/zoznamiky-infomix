vysledok=0
with open("generuj_4.txt") as file:
    for line in file:
        line1=[]
        line=line.strip().split("?")
        for cislo in line:
            line1.append(int(cislo))
        for i in range(2):
            pocet=line1.count(max(line1))
            for i in range(pocet):
                indexik=line1.index(max(line1))
                line1[indexik]=0
        vysledok+=max(line1)

print(vysledok)
                
                
        
