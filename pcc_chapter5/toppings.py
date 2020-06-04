requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!\n")

# Testing multiple conditions.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")

# Checking for special items.
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!\n")

# Checking that a list is not empty. +Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                    'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = []
taking_order = True

while taking_order == True:
    topping = input("What would you like on your pizza?: ")
    requested_toppings.append(topping)
    checking_answer = True
    
    while checking_answer == True:
        answer = input("Is that all?: ")
        if answer.lower() == 'yes':
            taking_order = False
            checking_answer = False
        elif answer.lower() == 'no':
            taking_order = True
            checking_answer = False
        else:
            print("I'm sorry, I don't understand. Please type yes or no.")

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
    print("\nFinished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?")

# Currently, the code I added renders the final else unreachable.
# If the user enters nothing, the program returns "Adding ." instead of
# reaching the final else.