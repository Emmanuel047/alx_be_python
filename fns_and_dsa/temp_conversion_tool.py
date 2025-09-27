FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    
def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

temp_input = input("Enter the temperature you want to convert: ")
if not temp_input:
    raise ValueError("Enter a numeric value.")
try:
    temp = float(temp_input)
except ValueError:
    raise ValueError("Enter a numeric value.")

choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if choice == "F":
    converted = convert_to_celsius(temp)
    print(f"{temp_input}°F is {converted}°C")
elif choice == "C":
    converted = convert_to_fahrenheit(temp)
    print(f"{temp_input}°C is {converted}°F")
else:
    print("Enter a valid choice C or F")