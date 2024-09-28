class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email

    def describe_user(self):
        print(f"User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


# Creating instances of User
user1 = User("Luke", "Burroughs", 20, "Male", "luke.burroughs@example.com")
user2 = User("Chase", "Suchka", 20, "Male", "chase.suchka@example.com")
user3 = User("Evan", "Grey", 19, "Male", "evan.grey@example.com")

# Calling describe_user() and greet_user() for each user
user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()
