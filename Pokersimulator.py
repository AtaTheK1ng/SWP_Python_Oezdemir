from random import random

# wahrscheinlichkeit: paar 42,26%
# wahrscheinlichkeit: zwei paar 4,75%
# wahrscheinlichkeit: drillings 2,11%
# wahrscheinlichkeit: straße 0,392%
# wahrscheinlichkeit: flush 0,197%
# wahrscheinlichkeit: full house 0,144%
# wahrscheinlichkeit: straight flush 0,00139%
# wahrscheinlichkeit: royal flush 0,000154%

karten = 52
spiele_anzahl = 100000

zahlen = [i for i in range(0, karten)]
gezogene_zahlen = []
import random

wahrscheinlichkeiten_statistik = {
    "Paar": 0,
    "Zwei Paar": 0,
    "Drilling": 0,
    "Straße": 0,
    "Flush": 0,
    "Full House": 0,
    "Straight Flush": 0,
    "Royal Flush": 0
}

def ziehe_fuenf_karten():
    gezogene_zahlen = []
    for i in range(5):
        random_index = random.randint(0, len(zahlen) - 1 - i)
        gezogene_zahl = zahlen[random_index] % 13
        gezogene_zahlen.append(gezogene_zahl)

        zahlen[random_index], zahlen[len(zahlen) - 1 - i] = zahlen[len(zahlen) - 1 - i], zahlen[random_index]

    return gezogene_zahlen

def erkenne_kombinationen(hand):

    paar = 2 in hand
    drilling = 3 in hand
    zwei_paar = hand.count(2) == 2

    werte_sortiert = sorted(hand)
    strasse = all([werte_sortiert[i] - werte_sortiert[i - 1] == 1 for i in range(1, 5)])
    full_house = drilling and paar
    flush = 5 in hand
    straight_flush = strasse and flush
    royal_flush = straight_flush and []

    if full_house:
        return "Full House"
    elif flush:
        return "Flush"
    elif strasse:
        return "Straße"
    elif royal_flush:
        return "Royal Flush"
    elif straight_flush:
        return "Straight Flush"
    elif drilling:
        return "Drilling"
    elif zwei_paar:
        return "Zwei Paar"
    elif paar:
        return "Paar"
    else:
        return None

def spiele_poker_simulation(spiele_anzahl):
    for _ in range(spiele_anzahl):
        hand = ziehe_fuenf_karten()
        kombination = erkenne_kombinationen(hand)
        if kombination is not None:
            wahrscheinlichkeiten_statistik[kombination] += 1


spiele_poker_simulation(spiele_anzahl)

print(f"Ergebnisse nach {spiele_anzahl} Spielen:")
for kombination, anzahl in wahrscheinlichkeiten_statistik.items():
    prozent = (anzahl / spiele_anzahl) * 100
    print(f"{kombination}: {anzahl} Mal ({prozent:.4f}%)")
