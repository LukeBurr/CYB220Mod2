# Creating a dictionary for a person
person_dict = {
    'f_name': 'Keeghan',
    'l_name': 'Brown',
    'age': 19,
    'hometown': 'Boiling Springs',
    'current_city': 'Greenville',
    'username': 'K_Brown1'
}

# Printing information using f-strings
print(f"This person's first name is {person_dict['f_name']}, last name is {person_dict['l_name']}, and their username is {person_dict['username']}.")
print(f"For security reasons, we might ask them for their hometown, which is {person_dict['hometown']}.")
