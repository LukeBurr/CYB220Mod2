while True:
    # Asking the user for an integer or the exit command
    user_input = input("Enter an integer or type 'exit' to end the program: ")

    # Checking if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    try:
        # Converting user input to an integer
        user_number = int(user_input)

        # Checking if the number is even or odd
        if user_number % 2 == 0:
            print(f"{user_number} is an even number.")
        else:
            print(f"{user_number} is an odd number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer or type 'exit' to end the program.")
