# Multiplication Table Generator Assignment

# Instructions:
# 1. Fill in the missing code sections indicated by comments.
# 2. Implement a program that generates a multiplication table for two given numbers.
# 3. Test your program with different input values to ensure correctness.

# Section 1: Define a function called 'generate_multiplication_table' that takes two parameters: 'num1' and 'num2'.
# This function should generate and print the multiplication table for both 'num1' and 'num2' up to 10, including tabulation.
def generate_multiplication_table(num1, num2):
    # Fill in the missing code here
    for row in range (num1):
        for col in range (num2):
            print((row+1) * (col+1), end =" ")
        print()

# Section 2: Define a function called 'main' which will be the entry point of your program.
# Inside this function, prompt the user to enter two numbers for which the multiplication table needs to be generated.
# Then call the 'generate_multiplication_table' function with the provided numbers.
def main():
    # Prompt the user to enter two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Call the 'generate_multiplication_table' function with the provided numbers
    generate_multiplication_table(num1, num2)


# Call the main function to run the program
if __name__ == "__main__":
    main()
