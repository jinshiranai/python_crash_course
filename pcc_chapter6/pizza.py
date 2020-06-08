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

# Come back to this one later to make it so it accepts input and properly
# executes with said input instead of hard-coded values.