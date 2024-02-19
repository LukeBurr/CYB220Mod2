import json

def store_favorite_number():
    # Prompt the user for their favorite number
    favorite_number = input("What is your favorite number? ")

    # Store the favorite number in a file using JSON
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    print("Your favorite number has been stored in", filename)

def print_favorite_number():
    # Read the stored favorite number from the file
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
            print("I know your favorite number! It's", favorite_number)
    except FileNotFoundError:
        print("There is no favorite number stored yet.")

def main():
    try:
        # Attempt to read the stored favorite number
        print_favorite_number()
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON. File may be corrupted.")

    # If the favorite number is not stored, prompt for it and store it
    if not favorite_number:
        store_favorite_number()

if __name__ == "__main__":
    main()
