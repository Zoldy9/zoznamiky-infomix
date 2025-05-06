from random import randrange as rr
with open("generuj_2.txt","w")as file:
    for i in range(1000):
        cislo=str(rr(10))
        for j in range(rr(60)):
            file.write(cislo)
        for j in range(rr(20)):
            file.write(str(rr(10)))
            
        
