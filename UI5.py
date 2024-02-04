# Valid Ubuntu flavors
valid_flavors = ['Ubuntu', 'Kubuntu', 'Xubuntu', 'Lubuntu', 'Ubuntu Budgie', 'Ubuntu Kylin', 'Ubuntu MATE']

# Dictionary to store user polls
user_polls = {}

while True:
    # Asking the user for their username and favorite Ubuntu flavor
    username = input("Enter your username (or type 'quit' to exit): ")

    # Checking if the user wants to quit
    if username.lower() == 'quit':
        break

    flavor = input(f"Hello, {username}! What is your favorite Ubuntu flavor? ")

    # Checking if the entered flavor is legitimate
    if flavor.capitalize() in valid_flavors:
        # Adding the user's poll to the dictionary
        user_polls[username] = flavor.capitalize()
        print(f"Thank you, {username}! Your vote for {flavor.capitalize()} has been recorded.")
    else:
        # Handling non-legitimate flavor input
        print(f"Sorry, '{flavor}' is not a legitimate Ubuntu flavor.")
        print("Valid options are:", ', '.join(valid_flavors))

# Printing the final poll results
print("\nPoll Results:")
for user, fav_flavor in user_polls.items():
    print(f"{user}'s favorite Ubuntu flavor is {fav_flavor}.")
