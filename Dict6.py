# South Carolina counties dictionary
sc_counties_dict = {
    'Abbeville': 'Abbeville',
    'Charleston': 'Charleston',
    'Greenville': 'Greenville',
    'Lexington': 'Lexington',
    'Richland': 'Columbia',
    'Spartanburg': 'Spartanburg'
}

# List of 10 South Carolina counties
sc_counties_list = ['Abbeville', 'Charleston', 'Greenville', 'Lexington', 'Richland', 'Spartanburg', 'Anderson', 'York', 'Beaufort', 'Dorchester']

# Looping through each county in the list
for county in sc_counties_list:
    if county in sc_counties_dict:
        print(f"{county} is in our dictionary, and the capital/seat is {sc_counties_dict[county]}.")
    else:
        print(f"{county} is not in our dictionary. We will add this county shortly. Thanks!")
