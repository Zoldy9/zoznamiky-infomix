from random import choice as ch
with open("generuj_3.txt","w") as file:
    cisla=[]
    for i in range(10):
        cisla.append(str(i))
    for i in range(500):
        for j in range(80):
            file.write(f"{ch(cisla)} ")
        file.write("\n")


        
