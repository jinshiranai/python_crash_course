#PCC Try It Yourself 4-1

pizzas = ['meat', 'dessert', 'new york style']
for pizza in pizzas:
    print(f"I really like {pizza} pizza.")
print("\nI love pizza too much, which is bad for my cycling diet.")

#4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]

pizzas.append('pesto sauce')
friend_pizzas.append('chicago style')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)