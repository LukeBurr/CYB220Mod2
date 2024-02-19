import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Roll the die and print the result."""
        result = random.randint(1, self.sides)
        print(f"The die rolled a {result}.")


# Creating a 6-sided die and rolling it 10 times
print("Rolling a 6-sided die 10 times:")
six_sided_die = Die()
for _ in range(10):
    six_sided_die.roll_die()

# Creating a 10-sided die and rolling it 10 times
print("\nRolling a 10-sided die 10 times:")
ten_sided_die = Die(sides=10)
for _ in range(10):
    ten_sided_die.roll_die()

# Creating a 20-sided die and rolling it 10 times
print("\nRolling a 20-sided die 10 times:")
twenty_sided_die = Die(sides=20)
for _ in range(10):
    twenty_sided_die.roll_die()
