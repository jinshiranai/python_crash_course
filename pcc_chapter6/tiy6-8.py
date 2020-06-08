# PCC Try It Yourself 6-8. Pets.

pet_0 = {'name': 'snuffles', 'type': 'dog', 'owner': 'jeff'}
pet_1 = {'name': 'precious', 'type': 'shetland pony', 'owner': 'sandra'}
pet_2 = {'name': 'banana smoothie', 'type': 'ball python', 'owner': 'alexis'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\nPet name: {pet['name'].title()}")
    print(f"\tType: {pet['type']}")
    print(f"\tOwner: {pet['owner'].title()}")