class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht

    def __str__(self):
        return f"{self.name} ({self.geschlecht})"

class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)

class Abteilung():
    def __init__(self, name, abteilungsleiter, mitarbeiter):
        self.name = name
        self.abteilungsleiter = abteilungsleiter
        self.mitarbeiter = []

    def mitarbeiter_anzahl(self):
        return len(self.mitarbeiter)

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

class Firma:
    def __init__(self, abteilungen):
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def mitarbeiter_anzahl(self):
        anzahl = 0
        for abteilung in self.abteilungen:
            anzahl += abteilung.mitarbeiter_anzahl()
        return anzahl

    # def abteilungsleiter_anzahl(self):
    #     anzahl = 0
    #     for abteilung in self.abteilungen:
    #         if abteilung.abteilungsleiter:
    #             anzahl += 1
    #     return anzahl

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_Abteilung(self):
        groesste_abteilung = None
        anzahl = 0
        for abteilung in self.abteilungen:
            if abteilung.mitarbeiter_anzahl() > anzahl:
                groesste_abteilung = abteilung
                anzahl = abteilung.mitarbeiter_anzahl()
        return groesste_abteilung

    def prozent_frauen(self):
        anzahl_frauen = 0
        anzahl_mitarbeiter = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht == "w":
                    anzahl_frauen += 1
                anzahl_mitarbeiter += 1
        return anzahl_frauen / anzahl_mitarbeiter * 100


def main():
    # Firma erstellen
    firma = Firma()

    # Abteilungen erstellen
    it = Abteilung("IT")
    hr = Abteilung("HR")

    # Abteilungsleiter erstellen
    leiter_it = Abteilungsleiter("Herr Schmidt", "m", it)
    leiter_hr = Abteilungsleiter("Frau Müller", "w", hr)
    it.leiter = leiter_it
    hr.leiter = leiter_hr

    # Mitarbeiter erstellen und Abteilungen hinzufügen
    mitarbeiter1 = Mitarbeiter("Max Mustermann", "m", it)
    mitarbeiter2 = Mitarbeiter("Anna Schmidt", "w", it)
    mitarbeiter3 = Mitarbeiter("Peter Müller", "m", hr)

    it.add_mitarbeiter(mitarbeiter1)
    it.add_mitarbeiter(mitarbeiter2)
    hr.add_mitarbeiter(mitarbeiter3)

    # Abteilungen zur Firma hinzufügen
    firma.add_abteilung(it)
    firma.add_abteilung(hr)

    # Methoden testen
    print(f"Anzahl der Mitarbeiter in der Firma: {firma.mitarbeiter_anzahl()}")
    print(f"Anzahl der Abteilungsleiter in der Firma: {firma.abteilungsleiter_anzahl()}")
    print(f"Anzahl der Abteilungen in der Firma: {firma.abteilungen_anzahl()}")

    groesste_abt = firma.groesste_abteilung()
    print(
        f"Die größte Abteilung ist: {groesste_abt.name} mit {groesste_abt.mitarbeiter_anzahl()} Mitarbeitern."
    )

    frauen_prozent, maenner_prozent = firma.geschlechter_prozent()
    print(f"Frauen: {frauen_prozent:.2f}%, Männer: {maenner_prozent:.2f}%")

if __name__ == "__main__":
    main()