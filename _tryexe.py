def calculate_bmi(weight, height, unit_system):
    if unit_system == "imperial":
        # Convert height from feet and inches to inches
        height_inches = height[0] * 12 + height[1]
        # BMI formula for imperial units
        bmi = (weight / (height_inches ** 2)) * 703
    elif unit_system == "metric":
        # Convert height from centimeters to meters if necessary
        if height > 3:  # Assuming height in meters is less than 3, otherwise it's in centimeters
            height_meters = height / 100
        else:
            height_meters = height
        # BMI formula for metric units
        bmi = weight / (height_meters ** 2)
    else:
        raise ValueError("Invalid unit system. Please choose 'imperial' or 'metric'.")

    return bmi



def get_imperial_input():
    feet = int(input("Enter your height in feet: "))
    inches = int(input("Enter your height in inches: "))
    pounds = float(input("Enter your weight in pounds: "))
    return pounds, (feet, inches)


def get_metric_input():
    height_input = input("Enter your height in meters or centimeters (e.g., 1.75m or 175cm): ")
    if height_input.endswith('m'):
        height = float(height_input[:-1])
    elif height_input.endswith('cm'):
        height = float(height_input[:-2]) / 100
    else:
        height = float(height_input) / 100  # Assume input is in centimeters if no unit is provided
    kilograms = float(input("Enter your weight in kilograms: "))
    return kilograms, height


def main():
    print("Welcome to the BMI Calculator!")
    unit_system = input("Choose your unit system (imperial/metric): ").lower()

    if unit_system == "imperial":
        weight, height = get_imperial_input()
    elif unit_system == "metric":
        weight, height = get_metric_input()
    else:
        print("Invalid choice. Please choose 'imperial' or 'metric'.")
        return

    bmi = calculate_bmi(weight, height, unit_system)
    print(f"Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You are normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")


if __name__ == "__main__":
    main()