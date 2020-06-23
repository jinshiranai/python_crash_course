# PCC Try It Yourself 10-4. Guest Book.

filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        guest_name = input("\nMay we have your name please? ")
        if guest_name == 'q':
            break
        else:
            print(f"Welcome, {guest_name}. Enjoy your stay.")
            file_object.write(f"{guest_name}\n")         