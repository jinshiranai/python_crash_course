# Code to demonstrate using the int() function to turn strings into numbers.

height = input("How tall are you, in centimeters? ")
height = int(height)

if height >= 220:
    print("Okay, Shaq. You get your own car I guess.")
elif height >= 120:
    print("\nGreat! You can ride!")
else:
    print("\nSorry, come back when your bones are longer.")