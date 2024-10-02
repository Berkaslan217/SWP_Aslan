import random


def zufallszahlen():
    return random.sample(range(46), 6)

def statistik_akt(statistik_dict, gezogene_zahlen):
    for zahl in gezogene_zahlen:
        statistik_dict[zahl] += 1

def lottoziehung():
    statistik = {zahl: 0 for zahl in range(46)}

    for i in range(1000):
        gezogene_zahlen = zufallszahlen()
        statistik_akt(statistik, gezogene_zahlen)

    for zahl, anzahl in statistik.items():
        print(f"{zahl} wurde {anzahl} mal gezogen")

lottoziehung()
