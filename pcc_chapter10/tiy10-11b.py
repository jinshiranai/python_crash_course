# Try It Yourself 10-11. Favorite Number B.

import json

filename = 'favorite_number.json'
with open(filename) as f:
    fav_number = json.load(f)

print(f"I know your favorite number! It's {fav_number}!")