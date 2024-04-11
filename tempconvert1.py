# Temperature Converter Assignment

# Instructions:
# 1. Fill in the missing code sections indicated by comments.
# 2. Implement a program that converts temperatures between Celsius and Fahrenheit scales.
# 3. Test your program with different input values to ensure correctness.


# Section 1: Define a function called 'celsius_to_fahrenheit' that takes a single parameter: 'celsius'.
# This function should convert 'celsius' temperature to Fahrenheit and return the result.
def celsius_to_fahrenheit(celsius):
    # Fill in the missing code here
    pass


# Section 2: Define a function called 'fahrenheit_to_celsius' that takes a single parameter: 'fahrenheit'.
# This function should convert 'fahrenheit' temperature to Celsius and return the result.
def fahrenheit_to_celsius(fahrenheit):
    # Fill in the missing code here
    pass


# Section 3: Define a function called 'main' which will be the entry point of your program.
# Inside this function, prompt the user to choose the conversion direction (Celsius to Fahrenheit or Fahrenheit to Celsius).
# Then prompt the user to enter the temperature value to convert.
# Finally, call the appropriate conversion function based on the user's choice and print the result.
def main():
    # Prompt the user to choose the conversion direction
    print("Choose the conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1 or 2): "))

    # Prompt the user to enter the temperature value
    temperature = float(input("Enter the temperature value: "))

    # Call the appropriate conversion function based on the user's choice and print the result
    if choice == 1:
        result = celsius_to_fahrenheit(temperature)
        print("Temperature in Fahrenheit:", result)
    elif choice == 2:
        result = fahrenheit_to_celsius(temperature)
        print("Temperature in Celsius:", result)
    else:
        print("Invalid choice!")


# Call the main function to run the program
if __name__ == "__main__":
    main()
