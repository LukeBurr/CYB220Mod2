def make_shirt(size="large", message="I love Python"):
    print(f"A {size}-sized shirt will be printed with the message: '{message}'")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="Keep Calm and Code On")
