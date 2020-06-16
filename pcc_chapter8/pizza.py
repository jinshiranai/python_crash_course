# Module for making pizzas.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    topping_s = 'toppings'
    if len(toppings) == 1:
        topping_s = 'topping'
    print(f"\nMaking a {size}-inch pizza with the following {topping_s}:")
    for topping in toppings:
        print(f" - {topping}")
