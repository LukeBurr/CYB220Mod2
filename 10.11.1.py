import json

# Prompt the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Store the favorite number in a file using JSON
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print("Your favorite number has been stored in", filename)
