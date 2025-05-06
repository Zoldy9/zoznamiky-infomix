from random import randrange as rr
with open("generuj_4.txt","w") as file:
    for i in range(500):
        for j in range(39):
            file.write(f"{rr(100)}?")
        file.write(f"{rr(100)}")  
        file.write("\n")

