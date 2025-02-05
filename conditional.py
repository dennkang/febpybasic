def condition():
    while True:
        try:
            num1 = int(input("Enter a number: "))
            return num1
        except ValueError:
            print("That's not a number")

n = condition()
print(n)