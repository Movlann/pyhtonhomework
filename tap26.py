age = int(input("Enter your age: "))
degree = input("Enter your degree: ")
experience = int(input("Enter your years of experience: "))

if age >= 22 and age <= 45:
    if degree == "CS" or experience >= 5:
        print("You are eligible for hiring.")
    else:
        print("Not eligible: Need CS degree or at least 5 years of experience.")
else:
    print("Not eligible: Age must be between 22 and 45.")