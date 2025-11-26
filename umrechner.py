kilometer = str(1000)

print("Hallo Benutzer, willkommen im Umrechner") #Begrüßung

print("Wollen sie Kilometer (km) oder Meter (m) umrechnen?")

eingabe_starteinheit = input("Ihre Wahl: ") #Auswahl von Benutzer von Ursprungseinheit

if eingabe_starteinheit != "m" and eingabe_starteinheit != "km":
    print("Ungültige Eingabe. Bitte wählen Sie 'm' für Meter oder 'km' für Kilometer.")

elif eingabe_starteinheit == "m": #Berechnung in Kilometern wenn Meter ausgewählt
    eingabe_startlänge = input("Geben sie die Startdistanz in Metern an: ")
    ergebnis_km = float(eingabe_startlänge) / float(kilometer)
    print(f"Die Distanz in Kilometern beträgt: {ergebnis_km} km")

elif eingabe_starteinheit == "km": #Berechnung in Kilometern wenn Meter ausgewählt
    eingabe_startlänge = input("Geben sie die Startdistanz in Kilometern an: ")
    ergebnis_m = float(eingabe_startlänge) * float(kilometer)
    print(f"Die Distanz in Metern beträgt: {ergebnis_m} m")
