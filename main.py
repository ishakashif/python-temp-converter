
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
if unit not in ["F", "C", "f", "c"]:
    print(f"'{unit}' is an invalid unit of measurement. Please try again")
elif unit == "C":
    temp = float(input("Enter the temperature: "))
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp} degrees")
elif unit == "F":
    temp = float(input("Enter the temperature: "))
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is {temp} degrees")
