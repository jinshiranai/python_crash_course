# PCC Try It Yourself 10-5. Programming Poll.

filename = 'programming_poll.txt'

print("\nWelcome to the programming poll!")
print("(enter 'q' at any time to quit)")

with open(filename, 'a') as file_object:
    while True:
        name = input("\nFirst, let's start with your name: ")
        if name == 'q':
            break
        print(f"Okay, {name}, why do you like programming?")
        reason = input()
        if reason == 'q':
            break
        
        file_object.write(f"{name}: {reason}\n")

        print(f"\nThank you for your input, {name}. Have a nice day!\n")

