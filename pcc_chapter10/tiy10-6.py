# Try It Yourself 10-6. Addition.
# And 10-7. Addition Calculator.

print("Gimme two numbers. I gotta add sumthin.")
print("Enter 'q' if yer a quitter.")

while True:
    first_number = input("\nGimme that first number: ")
    if first_number == 'q':
        print("Bye Felicia.")
        break
    second_number = input("Now the second: ")
    if second_number == 'q':
        print("Bye Felicia.")
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Get outta here with them letters! Gimme a number!")
    else:
        print(f"Answer's {answer}. What else ya got?")