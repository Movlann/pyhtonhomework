temp = int(input("Enter the temperature: "))
if temp > 30:
    print("Turn on the AC")
elif temp >= 20:
    if temp <= 30:
        print("Comfortable")
else:
    print("Turn on the heater")