def make_car(manufacturer, model, **kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
    return car_info

# Call the function with required information and additional name-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to verify all information was stored correctly
print(car)
