from random import randrange as rr
with open("generuj_5.txt","w")as file:
    for i in range(1000):
        cislo=str(rr(10))
        for j in range(rr(15)):
            file.write(cislo)
        cislo=str(rr(10))
        file.write(f"{str(rr(10))}")
        for j in range(rr(15)):
            file.write(cislo)
        
