yas = int(input("Yasinizi daxil edin: "))
if yas >= 18:
    print("Bilet qiymeti: $15")
if yas >= 13 and yas <= 17:
    print("Biletin qiymeti: $10")
if yas < 13:
    print("Biletin qiymeti: $7")