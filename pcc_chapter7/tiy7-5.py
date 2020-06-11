# PCC Try It Yourself 7-5. Movie Tickets.

moviegoers = input("How many moviegoers are you? ")
moviegoers = int(moviegoers)

counter = 1
total = 0

while counter <= moviegoers:
    age = input(f"\nHow old is moviegoer {counter}? ")
    age = int(age)

    if age < 3:
        print("\nChildren under the age of 3 are free!")
        counter += 1
    elif age < 13:
        print("Children from 3 to 12 are $10.")
        total += 10
        counter += 1
    elif age >= 13:
        print("Ages 13 and up are $15.")
        total += 15
        counter += 1

print(f"\n\nYour total is ${total}. Enjoy your movie!")
