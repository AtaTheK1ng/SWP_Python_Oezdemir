import random
zahlen = list(range(0, 45))
statistik = {zahl: 0 for zahl in range(45)}

for a in range(1000):
    gezogene_zahlen = []
    i = 0
    while i < 6:
        random_number = random.randint(0, len(zahlen) - 1)
        gezogene_zahl = zahlen[random_number]

        if gezogene_zahl not in gezogene_zahlen:
            gezogene_zahlen.append(gezogene_zahl)
            statistik[gezogene_zahl] += 1
            i += 1

for numbers, amount in statistik.items():
    print(f"{numbers} wurde {amount} mal gezogen.")



