#PCC Try It Yourself 5-1 Conditional Tests

bike = 'cervelo'
print("Is bike == 'cervelo'? I predict True.")
print(bike == 'cervelo')

print("\nIs bike == 'canyon'? I predict False.")
print(bike == 'canyon')

print("\nIs bike == 'Cervelo'? I predict False.")
print(bike == 'Cervelo')

bike = 'Cervelo'
print("\nIs bike == 'cervelo'? I predict False.")
print(bike == 'cervelo')

print("\nIs bike.lower() == 'cervelo'? I predict True.")
print(bike.lower() == 'cervelo')

print("\nIs bike == 'Cervelo'? I predict True.")
print(bike == 'Cervelo')

car = 'toyota'
print("\nIs car == 'cervelo'? I predict False")
print(car == 'cervelo')

print("\nIs car == bike? I predict False.")
print(car == bike)

print("\nIs car == 'toyota'? I predict True.")
print(car == 'toyota')

print("\nIs car.lower() == 'toyota'? I predict True.")
print(car.lower() == 'toyota')

#5-2 More Conditional Tests
print("\n'magic' == 'science'?")
print('magic' == 'science')

print("\n'magic' != 'science'?")
print('magic' != 'science')

print("\nIs 9 >= 3**3?")
print(9 >= 3**3)

print("\nIs 9 > 3**3?")
print(9 > 3**3)

number = 27
squares = [value**2 for value in range(1,101)]
cubes = [value**3 for value in range(1, 101)]

print(f"\nIs {number} a square or a cube?")
if number in squares or number in cubes:
    print("Yes")
else:
    print("No")

print(f"\nIs {number} not a square?")
if number not in squares:
    print("Yes")

print(f"\nSo {number} is a cube?")
if number in cubes:
    print("Yes")

print("\nI see. Thank you.")
print("You're welcome, meatbag.")