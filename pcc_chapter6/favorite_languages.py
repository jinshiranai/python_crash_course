# A Dictionary of Similar Ojects.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# Looping through a dictionary.
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through just the keys.
for name in favorite_languages.keys(): # Code works the same without keys()
    print(f"{name.title()}")

# Accessing keys within the loop.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Looking for specific keys.
if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll! Or else! :D\n")

# Looping through keys in a particular order.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll.")

# Looping through values.
print(f"\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# set() collects the unique items and discards repeats.
print(f"\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# PCC Try It Yourself 6-6. Polling

pollsters = ['jen', 'jin', 'sarah', 'saho', 'edward', 'bella','phil']

for pollster in pollsters:
    if pollster in favorite_languages.keys():
        print(f"Thank you for taking our poll, {pollster.title()}.")
    else:
        print(f"Time is running out, {pollster.title()}. You know what to do. Take the poll.")