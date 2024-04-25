import json
import os
import sys

class PasswordManager:
    def __init__(self):
        self.data = {}
        self.master_password = None
        self.reveal_password = None

    def factory_reset(self):
        # This will delete the configuration file
        if os.path.exists("config.json"):
            os.remove("config.json")

        # This will delete the passwords file
        if os.path.exists("passwords.txt"):
            os.remove("passwords.txt")

        # Restart the script after reset/quit
        os.execv(sys.executable, [sys.executable] + sys.argv)

    def set_master_password(self, master_password):
        self.master_password = master_password

    def set_reveal_password(self, reveal_password):
        self.reveal_password = reveal_password

    def add_password(self, website, username, password):
        self.data[website] = {'username': username, 'password': password}
        self.save_data()
        print(f"Password for {website} added successfully.")

    def remove_password(self, website):
        if website in self.data:
            del self.data[website]
            self.save_data()
            print(f"Password for {website} removed successfully.")
        else:
            print(f"No password found for {website}.")

    def get_password(self, website, input_password):
        if input_password != self.master_password and input_password != self.reveal_password:
            print("Incorrect password. Access denied.")
            return None

        if website not in self.data:
            print("Website not found.")
            return None

        username = self.data[website]['username']
        password = self.data[website]['password']
        hidden_password = password[:-2] + '**'  # Hide the last two characters
        return f"Website: {website}\nUsername: {username}\nPassword: {hidden_password}"

    def list_passwords(self, input_password):
        if input_password != self.master_password:
            print("Incorrect password. Access denied.")
            return

        if not self.data:
            print("No passwords stored.")
            return

        print("Stored Passwords:")
        for website, info in self.data.items():
            print(f"Website: {website}, Username: {info['username']}")

    def save_data(self):
        with open("passwords.txt", "w") as file:
            for website, info in self.data.items():
                file.write(f"{website},{info['username']},{info['password']}\n")

    def load_data(self):
        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    website, username, password = line.strip().split(',')
                    self.data[website] = {'username': username, 'password': password}
        except FileNotFoundError:
            # If the file doesn't exist, create an empty one
            open("passwords.txt", "w").close()

    def save_configuration(self):
        config = {'master_password': self.master_password, 'reveal_password': self.reveal_password}
        with open("config.json", "w") as file:
            json.dump(config, file)

    def load_configuration(self):
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
                self.master_password = config.get('master_password')
                self.reveal_password = config.get('reveal_password')
        except FileNotFoundError:
            # If the file doesn't exist, create an empty one
            open("config.json", "w").close()

    def factory_reset(self):
        self.data = {}
        self.master_password = None
        self.reveal_password = None
        os.remove("passwords.txt")
        os.remove("config.json")
        print("Factory reset completed.")

# Example usage:
if __name__ == "__main__":
    password_manager = PasswordManager()

    # Load configuration (if exists)
    password_manager.load_configuration()

    # If master password is not set, prompt to set it
    if not password_manager.master_password:
        master_password = input("Set master password: ")
        password_manager.set_master_password(master_password)
        password_manager.save_configuration()

    # If reveal password is not set, prompt to set it
    if not password_manager.reveal_password:
        reveal_password = input("Set reveal password: ")
        password_manager.set_reveal_password(reveal_password)
        password_manager.save_configuration()

    # Load existing data
    password_manager.load_data()

    while True:
        print("\n1. Add Password\n2. Remove Password\n3. List Passwords\n4. Show Password\n5. Factory Reset\n6. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_manager.add_password(website, username, password)
        elif choice == '2':
            website = input("Enter website to remove: ")
            password_manager.remove_password(website)
        elif choice == '3':
            input_password = input("Enter master password to list passwords: ")
            password_manager.list_passwords(input_password)
        elif choice == '4':
            input_password = input("Enter reveal password to show password: ")
            website = input("Enter website: ")
            print(password_manager.get_password(website, input_password))
        elif choice == '5':
            confirm = input("Are you sure you want to perform a factory reset? (yes/no): ")
            if confirm.lower() == 'yes':
                password_manager.factory_reset()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
