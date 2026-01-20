druck = float(input("Bitte geben sie den Hydraulikdruck in bar an: "))
psi = druck * 14.5038

if druck < 50:
    print(f"❌ FEHLER: Druck zu niedrig ({druck} bar). Pumpe prüfen!")

else:
    print(f"✅ Druck OK ({druck} bar). System betriebsbereit.")
    print(f"In PSI beträgt der Druck {psi:.2f}")