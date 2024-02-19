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
    else:
        username = input("What is your name? ")
        age = input("How old are you? ")
        favorite_color = input("What is your favorite color? ")

        user_info = {
            'username': username,
            'age': age,
            'favorite_color': favorite_color
        }

        with open(path, 'w') as file:
            json.dump(user_info, file)
            print("We'll remember you when you come back, {}!".format(username))

greet_user()
