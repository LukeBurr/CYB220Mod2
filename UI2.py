# Asking the user for the amount of money they have
user_money = float(input("How much money do you have? $"))

# Realistic monetary values for processors
i3_price = 150.00
i5_price = 250.00
i7_price = 350.00
i9_price = 500.00

# Determining which processor the user can afford
if user_money >= i9_price:
    print("You can afford an Intel Core i9 processor!")
elif user_money >= i7_price:
    print("You can afford an Intel Core i7 processor!")
elif user_money >= i5_price:
    print("You can afford an Intel Core i5 processor!")
elif user_money >= i3_price:
    print("You can afford an Intel Core i3 processor!")
else:
    print("You may need to save more to afford an Intel Core i3 processor.")
