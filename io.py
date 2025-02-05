num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

print(f"The sum of {num1} and  {num2} is {num1+num2}")
print(f"The product of {num1} and {num2} is {num1*num2}")
print(f"The difference between {num1} and {num2} is {num1-num2}")
print(f"The quotient of {num1} and {num2} is {num1/num2}")
print(f"The remainder of dividing {num1} and {num2} is {num1%num2}")
print(f"The exponential of {num1} and {num2} is {num1**num2}")
print(f"The floor division of {num1} and {num2} is {num1//num2}")
print("")


# conditional operators
print(f"is {num1} equal to {num2} ? {num1==num2}")
print(f"Is {num1} different from {num2} ? {num1!=num2}")
print(f"Is {num1} greater than {num2} ? {num1>num2}")
print(f"Is {num1} greater than or equal to {num2} ? {num1>=num2}")
print(f"Is {num1} less than {num2} ? {num1<num2}")
print(f"Is {num1} less than  or equal to {num2} ? {num1<=num2}")
print("")

# logical operators
print(f"Are both {num1} and {num2} greater than or equal to 30?", num1>=30 and num2>=30)
print(f"Is {num1} or {num2} greater than or equal to 30?", num1>=30 or num2>=30)
