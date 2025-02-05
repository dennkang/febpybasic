# prompt for two number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# ask for operator
operator = input("Enter operator(+,-,*,/): ")

# calculate
if operator == "+":
    result = (num1 + num2)

elif operator == "-":
    result = (num1 - num2)

elif operator == "*":
    result = (num1 * num2)

elif operator == "/":
    if num2 == 0:
        result = ("Error cannot divide by zero")
    else:
        result = (num1 / num2)

else:
        result = ("Operator not recognized")

if result == "Error cannot divide by zero" or result == "Operator not recognized":
    print(result)
else:
    print(f"The result of {num1} {operator} {num2} is {result}")