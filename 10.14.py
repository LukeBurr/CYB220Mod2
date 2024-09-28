from pathlib import Path
import json

def greet_user():
    """Greet the user by name and collect additional information."""
    path = Path('user_info.json')
    if path.exists():
        with open(path, 'r') as file:
            user_info = json.load(file)
            print("Welcome back, {}!".format(user_info['username']))
            print("Your age is {}.".format(user_info['age']))
            print("Your favorite color is {}.".format(user_info['favorite_color']))

            # Ask if the displayed username is correct
            correct_username = input("Is this the correct username? (yes/no): ").lower()
            if correct_username != 'yes':
                get_new_username(user_info)
            else:
                print("Welcome back, {}!".format(user_info['username']))
    else:
        get_new_username()

def get_new_username(prev_user_info=None):
    """Get the correct username from the user."""
    if prev_user_info:
        username = input("What is your correct username? (prev: {}): ".format(prev_user_info['username']))
    else:
        username = input("What is your correct username? ")

    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")

    user_info = {
        'username': username,
        'age': age,
        'favorite_color': favorite_color
    }

    path = Path('user_info.json')
    with open(path, 'w') as file:
        json.dump(user_info, file)
        print("Welcome, {}!".format(username))

greet_user()
