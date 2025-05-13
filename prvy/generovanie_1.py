from random import randrange as  rr
from random import choice as ch
with open("generuj_1.txt","w") as file:
    indexy=[]
    while len(indexy)!=10:
        pomoc=rr(35)
        if pomoc not in indexy:
            indexy.append(pomoc) 
    for i in range(800):
        riadok=[]
        for j in range(50):
            riadok.append(rr(100))
        maximum=max(riadok)
        cislo= riadok.count(maximum)
        for i in range(cislo):
            riadok.remove(maximum)
        index=ch(indexy)
        riadok[index]=maximum
        for prvok in riadok:
            file.write(f"{str(prvok)} ")
        file.write("\n")
        
        
        
            
        
            
            


        
        
    
