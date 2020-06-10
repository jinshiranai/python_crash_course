# PCC Try It Yourself 7-2. Restaurant Seating.

party_name = input("Welcome to Azaziel's Kebabs! May we have your party name? ")

seating_prompt = f"\nHow many people are in the {party_name.title()} party?"
seating_prompt += "\nPlease enter a number: "

party_size = input(seating_prompt)
party_size = int(party_size)

if party_size < 9:
    print(f"\n{party_name.title()}, party of {party_size}, right this way "
        "please. Your table is ready.")
elif party_size < 13:
    print(f"\nApologies, but you'll have to wait for a table.")
elif party_size >= 13:
    print(f"\nUnfortunately, a party of your size must call and make a "
        "reservation in advance. Sorry for the inconvenience.")
