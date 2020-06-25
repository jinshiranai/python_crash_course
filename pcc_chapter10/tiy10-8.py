# Try It Yourself 10-8. Cats and Dogs.
# Plus 10-9. Silent Cats and Dogs.

filenames = ['cats.txt','snakes.txt', 'dogs.txt','ferrets.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            pet_names = f.readlines()
            for pet_name in pet_names:
                print(pet_name.rstrip())
    except FileNotFoundError:
        pass