import json

# Read the stored favorite number from the file
filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
        print("I know your favorite number! It's", favorite_number)
except FileNotFoundError:
    print("There is no favorite number stored yet.")
