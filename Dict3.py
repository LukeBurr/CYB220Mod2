# Creating a dictionary for definitions
definitions = {
    'python': 'A high-level programming language',
    'variable': 'A storage location paired with an an identifier.',
    'list': 'An ordered, mutable collection of elements, often used for storing data types.',
    'method': 'A function associated with an object in object-oriented programming.',
    'if statement': 'A control flow statement that executes a block of code if a specified condition is true.',
    'dictionary': 'A collection of key-value pairs, allowing efficient lookup, insertion, and deletion of items.',
    'function': 'A reusable, self-contained block of code that performs a specific task.'
}

# Printing each word and its meaning
for word, meaning in definitions.items():
    print(f"{word}:\n{meaning}\n")
