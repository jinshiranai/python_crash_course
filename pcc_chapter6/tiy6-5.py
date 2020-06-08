#PCC Try It Yourself 6-5. Rivers

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'america',
    }

for river, country in rivers.items():
    print(f"The {river.title()} is the longest river in {country.title()}.")

print("\nThese are the rivers:")
for river in rivers.keys():
    print(river.title())

print("\nAnd these are the countries:")
for countries in rivers.values():
    print(countries.title())