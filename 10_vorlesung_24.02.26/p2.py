

datei = open("/workspaces/Maschinenbau_Informatik_2526/10_vorlesung_24.02.26/maschine_01.log")

zeilen = datei.readlines()

print(f"Anzahl Zeilen: {len(zeilen)}")

anzahlAlarm = 0
anzahlError = 0

for zeile in zeilen:
    datum = zeile.split("|")[0]
    print(datum)
    anzahlAlarm += zeile.count("ALARM")
    anzahlError += zeile.count("ERROR")

print(f"Anzahl Alarm: {anzahlAlarm}")
print(f"Anzahl Error: {anzahlError}")
