with open("generuj_5.txt") as file:
    subor = file.read().strip()

maximum = 0
for i in range(1, len(subor) - 1):
    if subor[i - 1] == subor[i + 1]:
        cifra = subor[i - 1]
        lava = 0
        j = i - 1
        while j >= 0 and subor[j] == cifra:
            lava += 1
            j -= 1
        prava = 0
        j = i + 1
        while j < len(subor) and subor[j] == cifra:
            prava += 1
            j += 1
        sucet = (lava + prava) * int(cifra)
        if sucet > maximum:
            maximum = sucet

print(maximum)
