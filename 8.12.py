def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)

# Call the function three times with different numbers of arguments
make_sandwich("ham", "cheese", "lettuce")
print("\n")
make_sandwich("turkey", "bacon")
print("\n")
make_sandwich("peanut butter", "jelly")
