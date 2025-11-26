kilometer = str(1000)

print("Hallo Benutzer, willkommen im Umrechner") #Begrüßung

print("Wollen sie Kilometer (km) oder Meter (m) umrechnen?")

while True:
    eingabe_starteinheit = input("Bitte wählen Sie 'm' für Meter oder 'km' für Kilometer: ") #Auswahl von Benutzer von Ursprungseinheit

    if eingabe_starteinheit != "m" and eingabe_starteinheit != "km":
        print("Ungültige Eingabe. Bitte wählen Sie 'm' für Meter oder 'km' für Kilometer.")
        continue

    while eingabe_starteinheit == "m": #Berechnung in Kilometern wenn Meter ausgewählt
        eingabe_startlänge = input("Geben sie die Startdistanz in Metern an: ")
        if isinstance(eingabe_startlänge, str):
            try:
                float(eingabe_startlänge)
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                continue
        ergebnis_km = float(eingabe_startlänge) / float(kilometer)
        print(f"Die Distanz in Kilometern beträgt: {ergebnis_km} km")
        break

    while eingabe_starteinheit == "km": #Berechnung in Metern wenn Kilometer ausgewählt
        eingabe_startlänge = input("Geben sie die Startdistanz in Kilometern an: ")
        if isinstance(eingabe_startlänge, str):
            try:
                float(eingabe_startlänge)
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                continue
        ergebnis_m = float(eingabe_startlänge) * float(kilometer)
        print(f"Die Distanz in Metern beträgt: {ergebnis_m} m")
        break
    
    nochmal = input("Möchten Sie eine weitere Umrechnung durchführen? (Ja (j)/Nein (n)): ")
    if nochmal.lower() != "j":
        print("Danke fürs Benutzen des Umrechners. Auf Wiedersehen!")
        quit()