class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 300  # Arbitrary value for battery size 75

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery size to 65 if it isn't already."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Creating an instance of Battery for ElectricCar


# Creating an instance of ElectricCar with default battery size
my_leaf = ElectricCar('Nissan', 'Leaf', 2024)

# Calling get_range() before upgrading the battery
print("Before upgrading the battery:")
my_leaf.battery.get_range()

# Upgrading the battery
my_leaf.battery.upgrade_battery()

# Calling get_range() after upgrading the battery
print("\nAfter upgrading the battery:")
my_leaf.battery.get_range()
