# Creating a dictionary for South Carolina counties with the three largest cities
sc_counties = {
    'Anderson': ['Anderson City', 'Greenville', 'Clemson'],
    'Charleston': ['Charleston', 'North Charleston', 'Mount Pleasant'],
    'Richland': ['Columbia', 'Lexington', 'Irmo'],
    'York': ['Rock Hill', 'Fort Mill', 'Clover'],
    'Spartanburg': ['Greer', 'Spartanburg', 'Duncan']
}

# Looping through the dictionary
for county, cities in sc_counties.items():
    print(f"In {county} County, the largest cities are {cities[0]}, {cities[1]}, and {cities[2]}.")
