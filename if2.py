age = int(input("Enter your age: "))
if age >= 18:
    print("You are can vote!")

elif age == 17:
    print("Please try again next year!")

else:
    print(f"Please try again in {18 - age} years!")