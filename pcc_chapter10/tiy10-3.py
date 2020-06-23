# PCC Try It Yourself 10-3. Guest.

guest_name = input("Hey there. What's your name? ")

with open('guest.txt', 'w') as file_object:
    file_object.write(guest_name)