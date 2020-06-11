# PCC Try It Yourself 7-4. Pizza Toppings.

# Active variable exit.
adding_toppings = True
topping_prompt = "\nWhat topping would you like on your pizza?"
topping_prompt += "\n(Enter 'quit' to finish.) "

while adding_toppings:
    topping = input(topping_prompt)

    if topping == 'quit':
        adding_toppings = False
    else:
        print(f"\nAdding {topping} to your pizza.")

# 7-6. Three Exits.
# Break exit.
topping_prompt = "\nWhat topping would you like on your pizza?"
topping_prompt += "\n(Enter 'quit' to finish.) "

while True:
    topping = input(topping_prompt)

    if topping == 'quit':
        break
    else:
        print(f"\nAdding {topping} to your pizza.")

# Conditional test exit.
toppings = []
topping_prompt = "\nYour pizza must have three toppings. Go. "

while len(toppings) != 3:
    topping = input(topping_prompt)
    print(f"\nAdding {topping} to your pizza.")
    toppings.append(topping)