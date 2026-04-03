year = int(input("Enter the year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("It's leap year")
    else:
        print("It's not leap year")
elif year % 4 == 0:
    print("It's leap year")
else:
    print("It's not leap year")