länge = 150
dehnung = 0.25

dehnung_in_pro = float(dehnung) / int(länge) * 100 #
gerundet = round(dehnung_in_pro, 2)
echt_prozent = gerundet * 100

print(f"{gerundet}, das entspricht {echt_prozent}%")