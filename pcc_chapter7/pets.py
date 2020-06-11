# Code demonstrating using while loops to remove specific values from lists.

pets = ['dog', 'cat', 'hamster', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)