# Initialize an empty list to store names
guest_names = []

# Prompt the user for their name
print("Welcome to the guest book. Enter 'quit' when you're done.")
while True:
    name = input("Please enter your name: ")

    # Check if the user wants to quit
    if name.lower() == 'quit':
        break

    # Add the name to the list
    guest_names.append(name)

# Write the names to a file called guest_book.txt
with open("guest_book.txt", "w") as file:
    for name in guest_names:
        file.write(name + "\n")

print("Names have been written to guest_book.txt.")
