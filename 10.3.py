from pathlib import Path

# Define the path to the file
path = Path('9.1.py')

# Read the contents of the file, split into lines, and print each line
for line in path.read_text().splitlines():
    print(line)
