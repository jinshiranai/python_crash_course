# PCC Try It Yourself 6-2. Favorite Numbers

favorite_numbers = {
    'emmanuel': [69, 420],
    'brian': [2, 88, 222],
    'saho': [32],
    'tripp': [1337, 360],
    'trump': [1940],
    }

print(f"Emmanuel's favorite number is {favorite_numbers['emmanuel']}.")
print(f"Brian's favorite number is {favorite_numbers['brian']}.")
print(f"Saho's favorite number is {favorite_numbers['saho']}.")
print(f"Tripp's favorite number is {favorite_numbers['tripp']}.")
print(f"Trump's favorite number is {favorite_numbers['trump']} because that's the decade he wishes it was.")

# 6-10. Favorite Numbers the 2nd.

for name, numbers in favorite_numbers.items():
    verb = 'is'
    number_singular = 'number'
    if len(numbers) > 1:
        verb = 'are'
        number_singular = 'numbers'
    
    print(f"\n{name.title()}'s favorite {number_singular} {verb}:")
    for number in numbers:
        print(f"\t{number}")