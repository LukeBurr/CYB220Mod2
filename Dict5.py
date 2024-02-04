# Creating a dictionary for South Carolina counties and their capitals/seats
sc_counties = {
    'Abbeville': 'Abbeville',
    'Charleston': 'Charleston',
    'Greenville': 'Greenville',
    'Lexington': 'Lexington',
    'Richland': 'Columbia',
    'Spartanburg': 'Spartanburg'
}

# Printing the dictionary
print("South Carolina Counties and County Capitals/Seats:")
for county, capital in sc_counties.items():
    print(f"{county} County: {capital}")
