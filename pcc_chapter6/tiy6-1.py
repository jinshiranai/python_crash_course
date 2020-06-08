# PCC Try It Yourself 6-1. Person

person_0 = {
    'first': 'rosemary',
    'last': 'warren',
    'age': '129',
    'location': 'unknown',
    'threat level': 'moderate',
    }

print(f"First Name: {person_0['first'].title()}")
print(f"Last Name: {person_0['last'].title()}")
print(f"Age: {person_0['age']}")
print(f"Location: {person_0['location'].title()}")
print(f"Threat Level: {person_0['threat level'].upper()}")
print("\n")

#6-7. People.
person_1 = {
    'first': 'emily',
    'last': 'warren',
    'age': '85',
    'location': 'vochigolov',
    'threat level': 'mild',
    }

person_2 = {
    'first': 'mikhail',
    'last': 'warren',
    'age': '54',
    'location': 'vochigolov',
    'threat level': 'severe',
    }

people = [person_0, person_1, person_2]

for person in people:
    name = f"{person['first']} {person['last']}"

    print(f"\nName: {name.title()}")
    print(f"Age: {person['age']}")
    print(f"Location: {person['location'].title()}")
    print(f"Threat Level: {person['threat level'].upper()}")