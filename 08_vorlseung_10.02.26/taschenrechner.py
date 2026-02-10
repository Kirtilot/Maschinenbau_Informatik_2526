print("Der Tolle Taschenrechner!")
print("Lass uns zwei Zahlen Addieren")

print("Operatoren:")
print("- addition/a")
print("- subtraktion/s")
print("- multiplikation/m")
print("- division/d")
print("- exit/e")

operatior = ""

while True:

    operatior = input("Gib deine Rechenoperation an: ")
    if operatior != "exit" and operatior != "e":
        zahl1 = float(input("Gib die erste Zahl ein: "))
        zahl2 = float(input("Gib die zweite Zahl ein: "))

        if operatior == "addition" or operatior == "a":
            ergebnis = zahl1 + zahl2

        elif operatior == "subtraktion" or operatior == "s":
            ergebnis = zahl1 - zahl2

        elif operatior == "multiplikation" or operatior == "m":
            ergebnis = zahl1 * zahl2

        elif operatior == "division" or operatior == "d":
            ergebnis = zahl1 / zahl2

        else:
            print("Die Eingabe ist nicht gültig!")

        print(f"Das Ergebnos der Berechnung ist: {ergebnis}")
        print()
