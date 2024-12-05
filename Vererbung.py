class Schule:
    def __init__(self, name):
        self.name = name

    def beschreiben(self):
        print(f"Dies ist die {self.name} Schule.")

    def __str__(self):
        return f"Schule: {self.name}"


class Lehrer(Schule):
    def __init__(self, schulname, lehrername, fach):
        super().__init__(schulname)
        self.fach = fach
        self.lehrername = lehrername

    def unterrichten(self):
        print(f"Der Lehrer {self.lehrername} unterrichtet {self.fach}.")

    def __str__(self):
        return f"Lehrer {self.lehrername} in der {self.name} unterrichtet {self.fach}"


class Schueler(Lehrer):
    def __init__(self, schulname, klasse, lehrername, fach):
        Lehrer.__init__(self, schulname, lehrername, fach)
        self.klasse = klasse

    def lernen(self):
        return super().beschreiben()

    def __str__(self):
        return (f"Schueler besucht die Schule {self.name}, Klasse {self.klasse}, "
                f"mit dem Fach {self.fach} bei dem Lehrer {self.lehrername}.")


def main():
    schule = Schule("Gymnasium")
    lehrer = Lehrer(schule.name, "Herr Müller", "Mathematik")
    schueler = Schueler(schule.name, "5a", lehrer.lehrername, lehrer.fach)

    print(schule)
    print(lehrer)
    print(schueler)

    schueler.lernen()


if __name__ == "__main__":
    main()
