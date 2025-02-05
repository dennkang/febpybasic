marks = float(input("Enter the marks: "))
if marks >= 80:
    grade = "A"

elif marks >= 65:
    grade = "B"

elif marks >= 50:
    grade = "C"

elif marks >= 35:
    grade = "D"

else:
    grade = "F"

print("your grade is " + grade)