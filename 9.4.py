class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


# Creating an instance of Restaurant
restaurant = Restaurant("Luke's", "American")

# Printing the initial number of customers served
print("Number of customers served:", restaurant.number_served)

# Changing the number of customers served and printing again
restaurant.number_served = 53
print("Number of customers served:", restaurant.number_served)

# Using set_number_served() method
restaurant.set_number_served(78)
print("Number of customers served:", restaurant.number_served)

# Using increment_number_served() method
restaurant.increment_number_served(20)
print("Number of customers served:", restaurant.number_served)
