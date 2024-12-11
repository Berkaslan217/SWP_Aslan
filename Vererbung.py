class Gaming:
    def __init__(self, genre):
        self.genre = genre

    def beschreibung(self):
        return f"Dies ist ein allgemeines Gaming-Genre: {self.genre}."

class Shooter(Gaming):
    def __init__(self, genre, waffenart):
        super().__init__(genre)
        self.waffenart = waffenart

    def beschreibung(self):
        return f"Genre: {self.genre}, spezialisiert auf Shooter mit Waffenart: {self.waffenart}."

class RPG(Gaming):
    def __init__(self, genre, setting):
        super().__init__(genre)
        self.setting = setting

    def beschreibung(self):
        return f"Genre: {self.genre}, Rollenspiel mit Setting: {self.setting}."

class Sportspiel(Gaming):
    def __init__(self, genre, sportart):
        super().__init__(genre)
        self.sportart = sportart

    def beschreibung(self):
        return f"Genre: {self.genre}, spezialisiert auf Sportspiele in der Sportart: {self.sportart}."

class Strategie(Gaming):
    def __init__(self, genre, komplexität):
        super().__init__(genre)
        self.komplexität = komplexität

    def beschreibung(self):
        return f"Genre: {self.genre}, Strategiespiel mit Komplexität: {self.komplexität}."

shooter = Shooter("Shooter", "Projektilwaffen")
rpg = RPG("RPG", "Fantasy-Welt")
sportspiel = Sportspiel("Sportspiel", "Fußball")
strategie = Strategie("Strategie", "Hoch")

spiele = [shooter, rpg, sportspiel, strategie]
for spiel in spiele:
    print(spiel.beschreibung())
