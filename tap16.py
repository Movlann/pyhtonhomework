a = int(input("Birinci ededi daxil edin: "))
b = int(input("Ikinci ededi daxil edin: "))
c = int(input("Ucuncu ededi daxil edin: "))
if a > b:
    if a > c:
        print("En boyuk eded: ", a)
    else:
        print("En boyuk eded: ", c)
elif b > c:
    print("En boyuk eded: ", b)
else:
    print("En boyuk eded: ", c)