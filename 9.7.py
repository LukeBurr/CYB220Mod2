class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempts = 0  # Default value

    def describe_user(self):
        print(f"User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, email):
        super().__init__(first_name, last_name, age, gender, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator's Privileges:")
        for privilege in self.privileges:
            print(privilege)


# Creating an instance of Admin
admin = Admin("Admin", "User", 00, "Male", "admin@example.com")

# Calling the show_privileges method
admin.show_privileges()
