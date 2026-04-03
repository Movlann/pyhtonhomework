income = int(input("Gelir daxil edin: "))
credit = int(input("Kredit daxil edin: "))
if income > 50000:
    if credit > 700:
        print("approved")
    else:
        print("denied")
else:
    print("denied")