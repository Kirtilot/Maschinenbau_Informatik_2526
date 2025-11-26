print("Willkommen beim Binärrechner!")  # Begrüßung

print("Sie können hier zwei Dezimalzahlen zu einer Binärzahl addieren.") # Erklärung des Programms

while True:
    while True: 
        dezimalzahl1 = int(input("Geben sie die erste Dezimalzahl ein: "))  # Erste Zahl eingeben
        if dezimalzahl1 < 0 or dezimalzahl1 != int(dezimalzahl1): # Prüfung ob Zahl eingegeben wurde und nicht Buchstabe
            print("Ungültige Eingabe. Bitte geben Sie eine nicht-negative ganze Zahl ein.")
            continue
        else:
            print(f"Dezimalzahl eins wurde als {dezimalzahl1} gespeichert. Binär sieht sie so aus:{bin(dezimalzahl1)}") # Darstellung von Dezimal sowie Binär Zahl von Zahleneingabe 1
            break

    while True:
        dezimalzahl2 = int(input("Geben sie die zweite Dezimalzahl ein: "))  # Erste Zahl eingeben
        if dezimalzahl2 < 0 or dezimalzahl2 != int(dezimalzahl2): # Prüfung ob Zahl eingegeben wurde und nicht Buchstabe
            print("Ungültige Eingabe. Bitte geben Sie eine nicht-negative ganze Zahl ein.")
            continue
        else:
            print(f"Dezimalzahl eins wurde als {dezimalzahl2} gespeichert. Binär sieht sie so aus:{bin(dezimalzahl2)}") # Darstellung von Dezimal sowie Binär Zahl von Zahleneingabe 2
            break
    
    ergebnis = dezimalzahl1 + dezimalzahl2 # Berechnung vom Ergebnis
    print(f"Das Ergebniss der Rechnung {ergebnis}. Binär sieht das Ergebnis so aus: {bin(ergebnis)}") # Ausgabe vom Ergebnis in Dezimal und Binär

    nochmal = input("Möchten Sie eine weitere Berechnung durchführen? (Ja (j)/Nein (n)): ") # Frage ob weitere Rechnung ansteht
    if nochmal.lower() != "j":
        print("Danke fürs Benutzen des Binärrechners. Auf Wiedersehen!") # Verabschiedung
        quit()