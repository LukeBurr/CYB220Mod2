# Creating dictionaries for 5 South Carolina counties with cities and populations
county1 = {'Anderson': 50000, 'Greenville': 70000, 'Clemson': 20000, 'Belton': 8000, 'Pendleton': 5000}
county2 = {'Charleston': 140000, 'North Charleston': 120000, 'Mount Pleasant': 90000, 'Summerville': 50000, 'Goose Creek': 40000}
county3 = {'Columbia': 130000, 'Lexington': 50000, 'Irmo': 15000, 'Cayce': 12000, 'Forest Acres': 10000}
county4 = {'Rock Hill': 75000, 'Fort Mill': 35000, 'York': 15000, 'Tega Cay': 10000, 'Clover': 8000}
county5 = {'Greer': 30000, 'Spartanburg': 40000, 'Duncan': 8000, 'Inman': 5000, 'Woodruff': 6000}

# Creating a list of South Carolina county dictionaries
sc_counties_list = [county1, county2, county3, county4, county5]

# Looping through each county dictionary in the list
for county in sc_counties_list:
    for city, population in county.items():
        print(f"In {city.title()}, the current population is {population}.")
    print()  # Adding a newline between counties for better readability
