# Prompt the user for their name
name = input("Please enter your name: ")

# Write the user's name to a file called guest.txt
with open("guest.txt", "w") as file:
    file.write(name)

print("Your name has been written to guest.txt.")
