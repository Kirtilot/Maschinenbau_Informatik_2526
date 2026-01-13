print("Willkommen beim Kühlmittelmonitor")

kuelmitteltemperatur = float(input("Bitte geben sie die Kühlmitteltemperatur in °C an: "))

if kuelmitteltemperatur < 15:
    print("Die Kühlmitteltemperatur ist zu gering! Es besteht die gefahr für Kondensation!")

if kuelmitteltemperatur > 15 and kuelmitteltemperatur < 20:
    print("Die Kühlmitteltemperatur ist Suboptimal-Kalt. Funktionisfähig aber nicht optimal.")

if kuelmitteltemperatur > 20 and kuelmitteltemperatur < 28:
    if kuelmitteltemperatur > 22 and kuelmitteltemperatur < 26:
        print("Die Temperatur ist im Absoluten Idealbereich!")

    else:
        print("Die Temperatur ist im Optimalbereich.")

if kuelmitteltemperatur > 28 and kuelmitteltemperatur < 35:
    print("Die Kühlmitteltemperatur ist Suboptimal-Warm. Erhöhter Verschleiß!")

if kuelmitteltemperatur > 35:
    print("Die Kühlmitteltemperatur ist zu heiß! Maschine sofort stoppen!")