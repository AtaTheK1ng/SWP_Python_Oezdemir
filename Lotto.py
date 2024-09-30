import random
a = {
     0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16,
     17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27: 27, 28: 28, 29: 29, 30: 30,
     31: 31, 32: 32, 33: 33, 34: 34, 35: 35, 36: 36, 37: 37, 38: 38, 39: 39, 40: 40, 41: 41, 42: 42, 43: 43, 44: 44
}

gezogene_zahlen = []
i=0
while (i<6):
    random_number = random.randint(0, a.length)
    number_to_change = a[random_number]

    if (i == 0):
        last_number = a[a.length]
    else:
        last_number = a[random_number - 1]

    a[last_number] = number_to_change
    a[random_number] = last_number
    gezogene_zahlen.__add__(a[last_number])
    print(gezogene_zahlen)
    i = i + 1

