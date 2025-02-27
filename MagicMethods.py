import sys


class Auto:
    def __init__(self, ps):
        if not isinstance(ps, int):
            raise ValueError("PS muss eine Ganzzahl sein.")
        self.ps = ps

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps + other.ps

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps - other.ps

    def __truediv__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps / other.ps

    def __mul__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps * other.ps

    def __eq__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            raise ValueError("Auto Objekt erwartet.")
        return self.ps > other.ps


def main():
    auto1 = Auto(100)
    auto2 = Auto(200)

    # __add__
    print(auto1 + auto2)
    # __sub__
    print(auto1 - auto2)
    # __truediv__
    print(auto1 / auto2)
    # __mul__
    print(auto1 * auto2)
    # __eq__
    print(auto1 == auto2)
    # __lt__
    print(auto1 > auto2)
    # __gt__
    print(auto1 < auto2)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
