# Code to demonstrate putting lists in dictionaries.
# Store informations about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# PCC Try It Yourself 6-12. Extensions.

pizza = {'toppings': []}

print("\nWelcome to Azaziel's Pizza! Let's get you started."
        "\nFirst, let's choose a crust.")

# Choosing the pizza's crust.
choosing_crust = True
while choosing_crust == True:
    crusts = ['regular', 'thin', 'deep dish']
    crust = input("\nWhat crust would you like? Regular, thin, or deep dish?: ")
    crust = crust.lower()

    if crust in crusts:
        crust_confirm = input(f"\nYou've chosen {crust} crust, is this correct?(y/n)")
        crust_confirm = crust_confirm.lower()
        if crust_confirm == 'y':
            print("Great!")
            pizza['crust'] = crust
            choosing_crust = False
        else:
            print("I'm sorry, let's try again.")
    else:
        print("I'm sorry, what was that? Please choose an available crust.")

# Choosing the pizza's sauce.
sauces = ['tomato', 'marinara', 'pesto', 'white', 'bbq']
print("\nNow for the sauce! Today's sauces are:")
for sauce in sauces:
    print(f"\t{sauce}")

choosing_sauce = True
while choosing_sauce == True:
    sauce = input("\nWhat sauce would you like?: ")
    sauce = sauce.lower()

    if sauce in sauces:
        sauce_confirm = input(f"\nYou've chosen {sauce} sauce, is this correct?(y/n)")
        sauce_confirm = sauce_confirm.lower()
        if sauce_confirm == 'y':
            print("Great!")
            pizza['sauce'] = sauce
            choosing_sauce = False
        else:
            print("I'm sorry, let's try again.")
    else:
        print("I'm sorry, what was that? Please choose an available sauce.")

# Choosing the pizza's toppings.
toppings = ['pepperoni', 'sausage', 'ham', 'green peppers', 'pineapple',
            'onions', 'mushrooms', 'bacon', 'jalapenos', 'spinach',
            'sun-dried tomato', 'extra cheese']
print("\nAnd finally, the toppings! Today's toppings are:")
for topping in toppings:
    print(f"\t{topping}")

choosing_topping = True
while choosing_topping == True:
    topping = input("\nWhat topping would you like?: ")
    topping = topping.lower()

    if topping in toppings:
        topping_confirm = input(f"\nYou've chosen {topping}, is this correct?(y/n)")
        topping_confirm = topping_confirm.lower()
        if topping_confirm == 'y':
            print("Great!")
            pizza['toppings'].append(topping)
            another_topping = input("Would you like to add another topping?(y/n): ")
            another_topping = another_topping.lower()
            if another_topping == 'n':
                choosing_topping = False
        else:
            print("I'm sorry, let's try again.")
    else:
        print("I'm sorry, what was that? Please choose an available topping.")

# Making the pizza.
print(f"\n Alright, so you've ordered a {pizza['crust']}-crust, "
    f"{pizza['sauce']} sauce pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

pizza_confirm = input("Is this correct? (y/n): ")
pizza_confirm = pizza_confirm.lower()
if pizza_confirm == 'y':
    print("Fantastic! We'll assemble this pie, bake it, and have it "
        "at your door in no time!")
elif pizza_confirm == 'n':
    print(" That's no bueno, my dude. Let's take it from the top to get you "
        "that delicious pie you deserve.")
else:
    print("... do you even want a pizza?")