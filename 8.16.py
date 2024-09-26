# Importing the module using different approaches
import printing_functions
from printing_functions import make_car
from printing_functions import make_car as make
import printing_functions as pf
from printing_functions import *

# Call the function using each approach
car1 = printing_functions.make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('subaru', 'outback', color='blue', tow_package=True)
car3 = make('subaru', 'outback', color='blue', tow_package=True)
car4 = pf.make_car('subaru', 'outback', color='blue', tow_package=True)
car5 = make_car('subaru', 'outback', color='blue', tow_package=True)  # If using '*' import, no need to use the module name

# Print the dictionary to verify all information was stored correctly
print("Car 1:", car1)
print("Car 2:", car2)
print("Car 3:", car3)
print("Car 4:", car4)
print("Car 5:", car5)
