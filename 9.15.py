import random

# Define the list containing numbers and letters
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [1, 'A', 5, 'C']

# Counter to keep track of the number of iterations
num_iterations = 0

# Loop to pull numbers until your ticket wins
while True:
    # Randomly select 4 elements from the list
    winning_tickets = random.sample(data, 4)

    # Increment the iteration counter
    num_iterations += 1

    # Check if the winning ticket matches your ticket
    if winning_tickets == my_ticket:
        break

# Print the number of times the loop had to run to give you a winning ticket
print(f"It took {num_iterations} iterations to win the lottery with ticket {my_ticket}.")
