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


# Creating an instance of User
user = User("Luke", "Burroughs", 20, "Male", "luke.burroughs@example.com")

# Incrementing login_attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Printing the value of login_attempts
print("Login Attempts:", user.login_attempts)

# Resetting login_attempts
user.reset_login_attempts()

# Printing the value of login_attempts after reset
print("Login Attempts after reset:", user.login_attempts)
