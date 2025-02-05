# select units
units = input("Select between Imperial or Metric Units (I/M): ")

# input values
if units == "M" or units == "m":
    height = float(input("Enter height in metres or centimeters: "))

    if height > 4:
        height = height / 100

    weight = float(input("Enter weight in kilograms: "))

    bmi = weight / (height * height)

    print("Your BMI is:", bmi)

    if bmi < 18.5:
        bmiclass = "Underweight"
        bmirisk = "Increased"
    elif 18.5 <= bmi < 24.9:
        bmiclass = "Normal"
        bmirisk = "Least"
    elif 25 <= bmi < 29.9:
        bmiclass = "Overweight"
        bmirisk = "Increased"
    elif 30 <= bmi < 34.9:
        bmiclass = "Obese Class I"
        bmirisk = "High"
    elif 35 <= bmi < 39.9:
        bmiclass = "Obese Class II"
        bmirisk = "Very High"
    else:
        bmiclass = "Obese Class III"
        bmirisk = "Extremely High"

    print(f"Your BMI is classified as {bmiclass} and your risk of developing health problems is {bmirisk}")

elif units == "I" or units == "i":
    height1 = float(input("Enter height in feet: "))
    height2 = float(input("Enter height in inches: "))

    height = (((height1 * 12) + height2) * 0.0254)

    weight = int(input("Enter weight in pounds: "))

    weight = (weight * 0.453592)

    bmi = weight / (height * height)

    print("Your BMI is:", bmi)

    if bmi < 18.5:
        bmiclass = "Underweight"
        bmirisk = "Increased"
    elif 18.5 <= bmi < 24.9:
        bmiclass = "Normal"
        bmirisk = "Least"
    elif 25 <= bmi < 29.9:
        bmiclass = "Overweight"
        bmirisk = "Increased"
    elif 30 <= bmi < 34.9:
        bmiclass = "Obese Class I"
        bmirisk = "High"
    elif 35 <= bmi < 39.9:
        bmiclass = "Obese Class II"
        bmirisk = "Very High"
    else:
        bmiclass = "Obese Class III"
        bmirisk = "Extremely High"

    print(f"Your BMI is classified as {bmiclass} and your risk of developing health problems is {bmirisk}")



else:
    print("Please enter a valid unit")