
with open("generuj_2.txt") as file:
    subor=file.read().strip()

maximum=1
teraz=1
for i in range(1, len(subor)):
    if subor[i] == subor[i-1]:
        teraz += 1
        if teraz > maximum:
            maximum = teraz
    else:
        teraz = 1

print(maximum)
