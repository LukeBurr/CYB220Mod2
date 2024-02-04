# Generating a random number for the user to guess
import random
target_number = random.randint(1, 10)

# Setting up the loop control variable
active = True

while active:
    # Asking the user to guess the number or enter 'quit'
    user_input = input("Guess the number (between 1 and 10) or enter 'quit' to exit: ")

    # Checking if the user wants to quit
    if user_input.lower() == 'quit':
        print(f"The correct number was {target_number}. Goodbye!")
        break

    try:
        # Converting user input to an integer
        user_guess = int(user_input)

        # Checking if the guess is correct
        if user_guess == target_number:
            print(f"Congratulations! {user_guess} is the correct number.")
            active = False  # Setting the loop control variable to False to exit the loop
        else:
            print("Sorry, try again!")

    except ValueError:
        print("Invalid input. Please enter a valid number or 'quit' to exit.")
