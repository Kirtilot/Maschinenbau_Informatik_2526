# eingabe = input("Eingabe Zahl: ")

# zahl = int(eingabe)

try:
    ergebnis = 10/0
except:
    print("Du darfst nicht durch Null teilen!")
finally:
    print("Wird immer ausgegeben")