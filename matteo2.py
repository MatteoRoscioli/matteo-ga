# Four-Function Calculator Assignment

# Instructions:
# 1. Fill in the missing code sections indicated by comments.
# 2. Implement the four basic arithmetic operations: addition, subtraction, multiplication, and division.
# 3. Test your program with different input values to ensure correctness.


# Section 1: Define a function called 'addition' that takes two parameters: 'num1' and 'num2'.
# This function should return the sum of 'num1' and 'num2'.
def addition(num1, num2):
    sum = num1 + num2
    return sum


# Section 2: Define a function called 'subtraction' that takes two parameters: 'num1' and 'num2'.
# This function should return the result of subtracting 'num2' from 'num1'.
def subtraction(num1, num2):
    difference = num1 - num2
    return difference


# Section 3: Define a function called 'multiplication' that takes two parameters: 'num1' and 'num2'.
# This function should return the product of 'num1' and 'num2'.
def multiplication(num1, num2):
    product = num1 * num2
    return product


# Section 4: Define a function called 'division' that takes two parameters: 'num1' (dividend) and 'num2' (divisor).
# This function should return the result of dividing 'num1' by 'num2'.
# Handle the case where 'num2' is zero and return "Error: Division by zero" in this case.
def division(num1, num2):
    quotient = num1 / num2
    return quotient


# Section 5: Define a function called 'main' which will be the entry point of your program.
# Inside this function, prompt the user to enter two numbers and an arithmetic operation choice (addition, subtraction, multiplication, or division).
# Then call the appropriate function based on the user's choice and print the result.
def main():
    # Prompt the user to enter two numbers and an arithmetic operation choice
5    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input(
        "Enter the operation (addition/subtraction/multiplication/division): "
    )

    # Call the appropriate function based on the user's choice and print the result
    if operation == "addition":
        result = addition(num1, num2)
        print("Result:", result)
    elif operation == "subtraction":
        result = subtraction(num1, num2)
        print("Result:", result)
    elif operation == "multiplication":
        result = multiplication(num1, num2)
        print("Result:", result)
    elif operation == "division":
        result = division(num1, num2)
        print("Result:", result)
    else:
        print("Invalid operation!")


# Call the main function to run the program
if __name__ == "__main__":
    main()
