import random
upper_bound = 45
draws = 1000

numbers = list(range(upper_bound))
number = [i*i for i in range(upper_bound)]
statistics = {zahl: 0 for zahl in range(upper_bound + 1)}
set_numbers = set(numbers)

numbers[0] = 1000
b = number[0]

# for _ in range(draws):
#     winner_numbers = []
#     i = 0
#     while i < 6:
#         random_number = random.randint(0, len(numbers) - 1)
#         drawn_number = numbers[random_number]
#         drawn_number += 1
#
#         if drawn_number not in winner_numbers:
#             winner_numbers.append(drawn_number)
#             statistics[drawn_number] += 1
#             i += 1

# for number, amount in statistics.items():
    #print(f"{number} wurde {amount} mal gezogen.")

print(statistics)
print(numbers)
print(number)
print(set_numbers)

print(numbers[0])
print(b)














# while i < 6:
#         random_number = random.randint(0, len(zahlen) - 1)
#         number_to_change = zahlen[random_number]
#
#         if i == 0:
#             last_number = zahlen[len(zahlen) - 1]
#         else:
#             last_number = zahlen[len(zahlen) - 1 - i]
#
#         zahlen[last_number] = number_to_change + 1
#         zahlen[random_number] = last_number
#
#         gezogene_zahlen.append(zahlen[last_number])
#
#         if zahlen[last_number] in gezogene_zahlen:
#             statistik[zahlen[last_number]] += 1
#         i = i + 1