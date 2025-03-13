import random
import time
from collections import Counter

def zeitmesser(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} dauerte {end_time - start_time:.6f} Sekunden")
        return result
    return wrapper

farben = ['Pik', 'Herz', 'Karo', 'Kreuz']
symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

deck = [(farbe, symbol) for farbe in farben for symbol in symbole]

@zeitmesser
def ziehe_fuenf_karten(deck):
    random.shuffle(deck)
    return random.sample(deck, 5)

def ist_paar(hand):
    symbole = [symbol for _, symbol in hand]
    symbol_zaehler = Counter(symbole)
    return 2 in symbol_zaehler.values()

def ist_drilling(hand):
    symbole = [symbol for _, symbol in hand]
    symbol_zaehler = Counter(symbole)
    return 3 in symbol_zaehler.values()

def ist_vierling(hand):
    symbole = [symbol for _, symbol in hand]
    symbol_zaehler = Counter(symbole)
    return 4 in symbol_zaehler.values()

def ist_strasse(hand):
    werte_ordnung = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    symbole = [symbol for _, symbol in hand]
    symbol_indexe = sorted([werte_ordnung.index(symbol) for symbol in symbole])
    return all(symbol_indexe[i + 1] - symbol_indexe[i] == 1 for i in range(4))

def ist_flush(hand):
    farben = [farbe for farbe, _ in hand]
    return len(set(farben)) == 1

def ist_full_house(hand):
    symbole = [symbol for _, symbol in hand]
    symbol_zaehler = Counter(symbole)
    return 3 in symbol_zaehler.values() and 2 in symbol_zaehler.values()

def ist_royal_flush(hand):
    werte_ordnung = {'10', 'Bube', 'Dame', 'König', 'Ass'}
    symbole = {symbol for _, symbol in hand}
    return ist_flush(hand) and symbole == werte_ordnung

def erkenne_kombination(hand):
    if ist_royal_flush(hand):
        return "Royal Flush"
    elif ist_flush(hand):
        return "Flush"
    elif ist_strasse(hand):
        return "Straße"
    elif ist_vierling(hand):
        return "Vierling"
    elif ist_drilling(hand):
        return "Drilling"
    elif ist_paar(hand):
        return "Paar"
    elif ist_full_house(hand):
        return "Full House"
    else:
        return "High Card"

@zeitmesser
def simuliere_pokerhaende(anzahl_spiele):
    haeufigkeiten = {
        "Paar": 0,
        "Drilling": 0,
        "Vierling": 0,
        "Straße": 0,
        "Flush": 0,
        "Full House": 0,
        "Royal Flush": 0,
        "High Card": 0
    }

    for _ in range(anzahl_spiele):
        hand = ziehe_fuenf_karten(deck)
        kombination = erkenne_kombination(hand)
        haeufigkeiten[kombination] += 1

    return haeufigkeiten

anzahl_spiele = 100000
ergebnisse = simuliere_pokerhaende(anzahl_spiele)

for kombination, anzahl in ergebnisse.items():
    prozent = (anzahl / anzahl_spiele) * 100
    print(f"{kombination}: {anzahl} ({prozent:.2f}%)")