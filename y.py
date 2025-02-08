
yas = int(input("Yasinizi daxil edin: "))

if 0 <= yas <= 12:
    mesaj = "Usaqsan"
elif 13 <= yas <= 19:
    mesaj = "gencsen"
elif 20 <= yas <= 64:
    mesaj = "Boyuksen"
elif yas >= 65:
    mesaj = "Yaslisan"
else:
    mesaj = "Yanlis yas daxil etdiniz"

print(mesaj)
