def ist_binaerzahl(eingabe):                                                # Deffiniert was eine Binäre Zahl ist
    return all(ziffer in "01" for ziffer in eingabe) and len(eingabe) > 0 

print("Willkommen beim Binärrecher. Hier können sie zwei Binäre Zahlen in eine Binäre Zahl addieren oder subtrahieren und gleich als Dezimalzahl Ausgegeben bekommen") # Begrüßung

while True:    
    eingabe_rechenbefehl = input("Bitte geben sie an ob sie addieren (+) oder subtrahieren (-) wollen: ") # Anfrage welche Rechenart verwendet werden soll

    if eingabe_rechenbefehl != "+" and eingabe_rechenbefehl != "-": # Prüfen ob gültige Rechenart ausgewählt wurde
        print("Ungültige Eingabe. Bitte wählen Sie '+' für addition oder '-' für sutraktion.") # Falls nicht erneute Anfrage
        continue

    while eingabe_rechenbefehl == "+": # Rechenablauf bei addition
        while True:
            erste_binearzahl = input("Geben sie die erste Binärzahl an: ") # Anfrage nach erster Binärzahl
            if not ist_binaerzahl(erste_binearzahl): # Prüfung ob binäre Zahl eingegeben wurde
                print("Ungültige Eingabe. Bitte geben Sie eine binäre Zahl ein die nur aus 0 und 1 besteht.") # Erneute Anfrage bei Fehler
                continue
            else:
                dezimal = int(erste_binearzahl, 2) # Umrechnung erster Binärzahl in Dezimal
                print(f"Ihre erste Eingabe: {erste_binearzahl}. Dezimal entspricht das: {dezimal}") # Ausgabe erster Eingabe für Nutzer auch als Dezimal
                break
        while True:   
            zweite_binearzahl = input("Geben sie die zweite Binärzahl an: ") # Anfrage nach zweiter Binärzahl
            if not ist_binaerzahl(zweite_binearzahl): # Prüfung ob binäre Zahl eingegeben wurde
                print("Ungültige Eingabe. Bitte geben Sie eine binäre Zahl ein die nur aus 0 und 1 besteht.") # Erneute Anfrage bei Fehler
                continue
            else:
                dezimal = int(zweite_binearzahl, 2) # Umrechnung weiter Binärzahl in Dezimal
                print(f"Ihre erste Eingabe: {zweite_binearzahl}. Dezimal entspricht das: {dezimal}") # Ausgabe zweiter Eingabe für Nutzer auch als Dezimal
                break

        ergebnis_addition = int(erste_binearzahl, 2) + int(zweite_binearzahl, 2)
        print(f"Das Ergebniss der Addition ist: {bin(ergebnis_addition)[2:]}. Dezimal entspricht das {ergebnis_addition}")
        break

    while eingabe_rechenbefehl == "-":
        while True:
            erste_binearzahl = input("Geben sie die erste Binärzahl an: ")
            if not ist_binaerzahl(erste_binearzahl): # Prüfung ob binäre Zahl eingegeben wurde
                print("Ungültige Eingabe. Bitte geben Sie eine binäre Zahl ein die nur aus 0 und 1 besteht.")
                continue
            else:
                dezimal = int(erste_binearzahl, 2)
                print(f"Ihre erste Eingabe: {erste_binearzahl}. Dezimal entspricht das: {dezimal}")
                break
        while True:   
            zweite_binearzahl = input("Geben sie die zweite Binärzahl an: ")
            if not ist_binaerzahl(zweite_binearzahl): # Prüfung ob binäre Zahl eingegeben wurde
                print("Ungültige Eingabe. Bitte geben Sie eine binäre Zahl ein die nur aus 0 und 1 besteht.")
                continue
            else:
                dezimal = int(zweite_binearzahl, 2)
                print(f"Ihre erste Eingabe: {zweite_binearzahl}. Dezimal entspricht das: {dezimal}")
                break

        ergebnis_addition = int(erste_binearzahl, 2) - int(zweite_binearzahl, 2)
        print(f"Das Ergebniss der Addition ist: {bin(ergebnis_addition)[2:]}. Dezimal entspricht das {ergebnis_addition}")
        break

    nochmal = input("Möchten Sie eine weitere Berechnung durchführen? (Ja (j)/Nein (n)): ") # Frage ob weitere Rechnung ansteht
    if nochmal.lower() != "j":
        print("Danke fürs Benutzen des Binärrechners. Auf Wiedersehen!") # Verabschiedung
        quit()