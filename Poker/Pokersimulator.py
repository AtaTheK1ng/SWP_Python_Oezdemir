import random
import Unittest_Poker


def ziehe_fuenf_karten(karten):
    gezogene_zahlen = []
    aktuelle_karten = karten.copy()
    for i in range(5):
        random_index = random.randint(0, len(aktuelle_karten) - 1 - i)
        gezogene_zahl = aktuelle_karten[random_index]
        gezogene_zahlen.append(gezogene_zahl)

        aktuelle_karten[random_index], aktuelle_karten[len(aktuelle_karten) - 1 - i] = aktuelle_karten[
            len(aktuelle_karten) - 1 - i], aktuelle_karten[random_index]

    return gezogene_zahlen


def erkenne_kombinationen(hand, modulo_basis=13):
    werte = [karte % modulo_basis for karte in hand]

    werte_counter = {}
    for wert in werte:
        if wert in werte_counter:
            werte_counter[wert] += 1
        else:
            werte_counter[wert] = 1

    paar = any(count == 2 for count in werte_counter.values())
    zwei_paar = sum(1 for count in werte_counter.values() if count == 2) == 2
    drilling = any(count == 3 for count in werte_counter.values())

    werte_sortiert = sorted(set(werte))
    strasse = len(werte_sortiert) == 5 and (werte_sortiert[-1] - werte_sortiert[0] == 4)
    flush = sorted(werte) == list(range(min(werte), min(werte) + 5))

    straight_flush = strasse and flush
    royal_flush = straight_flush and min(werte_sortiert) == 8
    full_house = drilling and paar

    if royal_flush:
        return "Royal Flush"
    elif straight_flush:
        return "Straight Flush"
    elif full_house:
        return "Full House"
    elif flush:
        return "Flush"
    elif strasse:
        return "Straße"
    elif drilling:
        return "Drilling"
    elif zwei_paar:
        return "Zwei Paar"
    elif paar:
        return "Paar"
    else:
        return None

def spiele_poker_simulation(spiele_anzahl, kartenzahl=52, modulo_basis=13):
    zahlen = list(range(kartenzahl))
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

    for _ in range(spiele_anzahl):
        hand = ziehe_fuenf_karten(zahlen)
        kombination = erkenne_kombinationen(hand, modulo_basis)
        if kombination is not None:
            wahrscheinlichkeiten_statistik[kombination] += 1

    return wahrscheinlichkeiten_statistik


def main():
    spiele_anzahl = int(input("Geben Sie die Anzahl der Spiele ein: "))
    kartenzahl = 52
    modulo_basis = 13

    wahrscheinlichkeiten_statistik = spiele_poker_simulation(spiele_anzahl, kartenzahl, modulo_basis)

    print(f"Ergebnisse nach {spiele_anzahl} Spielen:")
    for kombination, anzahl in wahrscheinlichkeiten_statistik.items():
        prozent = (anzahl / spiele_anzahl) * 100
        print(f"{kombination}: {anzahl} Mal ({prozent:.2f}%)")

if __name__ == "__main__":
    main()
    # Unittest_Poker.main()