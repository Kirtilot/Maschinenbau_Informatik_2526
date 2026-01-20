aufgebrauchte_kraft = float(input("Bitte geben sie die aufgebrachte Kraft in N an: "))
querschnittsflaeche = float(input("Bitte geben sie die Querschnittsfläche in mm² an: "))

mechanische_spannung = aufgebrauchte_kraft / querschnittsflaeche

if mechanische_spannung < 100:
    print(f"Die mechanische Belastung beträgt {mechanische_spannung:.2f} N/mm² oder {mechanische_spannung:.2f} MPa. Das entspricht einer Niedrigspannung und ist weit unter der Streckgrenze.")

elif mechanische_spannung >= 100 and mechanische_spannung < 235:
    print(f"Die mechanische Belastung beträgt {mechanische_spannung:.2f} N/mm² oder {mechanische_spannung:.2f} MPa. Das entspricht der Betriebsspannung und ist normal und somit im zulässigen bereich.")

elif mechanische_spannung >= 235 and mechanische_spannung < 360:
    print(f"Die mechanische Belastung beträgt {mechanische_spannung:.2f} N/mm² oder {mechanische_spannung:.2f} MPa. Das entspricht der Grenzspannung. Achtung! Nahe/über Streckgrenze.")

else:
    print(f"Die mechanische Belastung beträgt {mechanische_spannung:.2f} N/mm² oder {mechanische_spannung:.2f} MPa. Gefahr! Material versagt! Bruchspannung!")