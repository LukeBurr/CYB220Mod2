# Creating a dictionary for shorter definitions
definitions = {
    'python': 'High-level programming language.',
    'variable': 'Storage location with a symbolic name.',
    'list': 'Ordered, mutable collection of elements.',
    'method': 'Function associated with an object.',
    'if statement': 'Control flow statement based on a condition.',
    'dictionary': 'Collection of key-value pairs for efficient data manipulation.',
    'function': 'Reusable block of code for a specific task.'
}

# Printing each word and its meaning using a loop
for word, meaning in definitions.items():
    print(f"{word}:\n{meaning}\n")
