def make_shirt(size, message):
    print(f"A {size}-sized shirt will be printed with the message: '{message}'")

# Call the function using positional arguments
make_shirt("medium", "This shirt is sized Medium!")

# Call the function using keyword arguments
make_shirt(size="large", message="This shirt is a Large!")
