# Importing the necessary function from the printing_functions module
from printing_functions import make_car

# Call the function with required information and additional name-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to verify all information was stored correctly
print(car)
