def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Building a profile of yourself
my_profile = build_profile('Luke', 'Burroughs',
                           location='South Carolina',
                           occupation='Full time student',
                           hobbies=['Video Games', 'Cars', 'Basketball'])

print(my_profile)
