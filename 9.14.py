import random

# Define the list containing numbers and letters
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 elements from the list
winning_tickets = random.sample(data, 4)

# Print the winning tickets
print("The winning tickets are:", winning_tickets)
