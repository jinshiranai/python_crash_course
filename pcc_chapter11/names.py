# Importing the name function to make sure it works.

from name_function import get_formatted_name

print("Enter 'q' to quit at any time.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Neatly printed name: {formatted_name}.")