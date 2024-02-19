try:
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Add the numbers together
    result = num1 + num2

    # Print the result
    print("The sum of", num1, "and", num2, "is", result)

except ValueError:
    # Print a friendly error message if the input is not a number
    print("Please enter valid numbers.")
