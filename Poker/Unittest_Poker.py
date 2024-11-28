import Pokersimulator

def test_erkenne_kombinationen():
    test_cases = [
        ([0, 1, 2, 2, 3], "Paar"),                # Ein Paar
        ([0, 0, 2, 2, 3], "Zwei Paar"),           # Zwei Paare
        ([0, 0, 0, 2, 3], "Drilling"),            # Drilling
        ([0, 1, 2, 3, 4], "Straße"),              # Straße
        ([5, 6, 7, 8, 9], "Flush"),               # Flush
        ([8, 9, 10, 11, 12], "Royal Flush"),      # Royal Flush
        ([0, 1, 3, 5, 7], None)                   # Keine Kombination
    ]

    passed = 0
    for hand, expected in test_cases:
        result = Pokersimulator.erkenne_kombinationen(hand)
        assert result == expected, f"Test fehlgeschlagen für Hand {hand}: erwartet {expected}, erhalten {result}"
        passed += 1

    print(f"Alle {passed} Tests erfolgreich bestanden!")


def main():
    test_erkenne_kombinationen()

if __name__ == "__main__":
    main()

