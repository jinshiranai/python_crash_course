# Try It Yourself 10-11. Favorite Numbers A.
# Plus 10-12. Favorite Number Remembered.

import json

def get_stored_number():
    """Get stored favorite number, if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number

def get_favorite_number():
    """Prompts for the user's favorite number."""
    fav_number = input("What's your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
    print("Okay, I'll rememebr that.")

def favorite_number():
    """Remembers the user's favorite number, or requests if it there is none."""
    fav_number = get_stored_number()
    if fav_number:
        print(f"I know your favorite number! It's {fav_number}!")
    else:
        get_favorite_number()

favorite_number()