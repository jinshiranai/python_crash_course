# PCC Try It Yourself 6-9. Favorite Places.

favorite_places = {
    'rosemary': ['ilford', 'the wild wood', 'shokawan'],
    'emily warren': ['vochigolov'],
    'edward jenvier': ['avendale', 'ellington']
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")