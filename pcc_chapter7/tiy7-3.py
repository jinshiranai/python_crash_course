# PCC Try It Yourself 7-3. Multiples of Ten.

while True:
    number = input("\nC'mon, gimme that sweet sweet number...: ")
    number = int(number)

    if number % 10 == 0:
        print("\nAhhh yeah multiple of 10 that's the stuff...")
        break
    else:
        print("\nThat ain't what I need, gimme that number!")