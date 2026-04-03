height = int(input("Enter the height: "))
age = int(input("Enter the age: "))
if height >= 120:
    if age >= 18:
        print("You can enter the theme park")
    else:
        print("You must have parent")
else:
    print("You can't enter the theme park")