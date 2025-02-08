#Istifadeciden 2 reqem sorushsun, 3-cude operasiyani sorushsun eger 
# `topla` dirsa toplasin, `cix` dirsa cixsin, `bolme` dirsa bolsun, `vurma` bu isharedirse 
# reqemleri bir birine vursun. neticeni sonda ekrana cap elesin.

num1 = float(input("Birinci regemi daxil edin!: "))
num2 = float(input("Ikinci regemi daxil edin!: "))
emeliyyat = input("emeliyyati daxil et: ")

if emeliyyat == "topla":
    netice = num1 + num2
elif emeliyyat == "cix":
    netice = num1 - num2
elif emeliyyat == "vurma":
    netice = num1 * num2
elif emeliyyat == "bolme":
    if num2 !=0:
        netice = num1 / num2
    else:
        netice = "Sifira bolmek mumkun deil!"
else:
    "Yanlis emeliyyat!"

print("netice:" ,netice)

