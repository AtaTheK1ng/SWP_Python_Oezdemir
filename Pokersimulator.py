from random import random

# wahrscheinlichkeit: paar 42,26%
# wahrscheinlichkeit: zwei paar 4,75%
# wahrscheinlichkeit: drillings 2,11%
# wahrscheinlichkeit: straße 0,392%
# wahrscheinlichkeit: flush 0,197%
# wahrscheinlichkeit: full house 0,144%
# wahrscheinlichkeit: straight flush 0,00139%
# wahrscheinlichkeit: royal flush 0,000154%

zahlen = [i for i in range(0, 52)]

def getRandomKarte():
    return zahlen[random.randint(0, len(zahlen) - 1) % 13]

# two pair, 3 pair, straigth, flush, full house, 4 of a kind, straight flush, royal flush, texas holdem
def pokerTable():
    for _ in range(5):
        print(getRandomKarte())
