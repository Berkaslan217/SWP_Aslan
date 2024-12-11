class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []  # Liste von Abteilungen

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def count_mitarbeiter(self):
        return sum(len(abt.mitarbeiter) for abt in self.abteilungen)

    def count_abteilungsleiter(self):
        return len([abt.abteilungsleiter for abt in self.abteilungen if abt.abteilungsleiter is not None])

    def count_abteilungen(self):
        return len(self.abteilungen)

    def abteilung_mit_meisten_mitarbeitern(self):
        if not self.abteilungen:
            return None
        return max(self.abteilungen, key=lambda abt: len(abt.mitarbeiter))

    def geschlechterverteilung(self):
        gesamt = []
        for abt in self.abteilungen:
            gesamt.extend(abt.mitarbeiter)
        gesamt.extend([abt.abteilungsleiter for abt in self.abteilungen if abt.abteilungsleiter is not None])

        frauen = sum(1 for person in gesamt if person.geschlecht.lower() == "weiblich")
        maenner = sum(1 for person in gesamt if person.geschlecht.lower() == "männlich")
        gesamt_anzahl = frauen + maenner

        if gesamt_anzahl == 0:
            return {"Frauen": 0, "Männer": 0}

        return {
            "Frauen": frauen / gesamt_anzahl * 100,
            "Männer": maenner / gesamt_anzahl * 100
        }


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []  # Liste von Mitarbeitern
        self.abteilungsleiter = None

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_abteilungsleiter(self, abteilungsleiter):
        self.abteilungsleiter = abteilungsleiter


class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)


# Beispiel zur Instanziierung aller Objekte
firma = Firma("Tech Solutions")

# Abteilungen erstellen
it_abteilung = Abteilung("IT")
hr_abteilung = Abteilung("HR")

firma.add_abteilung(it_abteilung)
firma.add_abteilung(hr_abteilung)

# Abteilungsleiter erstellen
it_leiter = Abteilungsleiter("Anna Müller", "weiblich", it_abteilung)
it_abteilung.set_abteilungsleiter(it_leiter)

# Mitarbeiter erstellen
mitarbeiter1 = Mitarbeiter("Max Mustermann", "männlich", it_abteilung)
mitarbeiter2 = Mitarbeiter("Lisa Schmidt", "weiblich", it_abteilung)
mitarbeiter3 = Mitarbeiter("John Doe", "männlich", hr_abteilung)

it_abteilung.add_mitarbeiter(mitarbeiter1)
it_abteilung.add_mitarbeiter(mitarbeiter2)
hr_abteilung.add_mitarbeiter(mitarbeiter3)

# Anzahl der Mitarbeiter und Abteilungsleiter in der Firma
print("Anzahl der Mitarbeiter:", firma.count_mitarbeiter())
print("Anzahl der Abteilungsleiter:", firma.count_abteilungsleiter())

# Anzahl der Abteilungen
print("Anzahl der Abteilungen:", firma.count_abteilungen())

# Abteilung mit den meisten Mitarbeitern
abteilung_groesste = firma.abteilung_mit_meisten_mitarbeitern()
if abteilung_groesste:
    print("Abteilung mit den meisten Mitarbeitern:", abteilung_groesste.name)

# Geschlechterverteilung
verteilung = firma.geschlechterverteilung()
print("Geschlechterverteilung:")
print("Frauen: {:.2f}%".format(verteilung["Frauen"]))
print("Männer: {:.2f}%".format(verteilung["Männer"]))
