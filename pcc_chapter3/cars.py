#PCC example code
#Organizing lists

#sort() permanently sorts the list alphabetically and cannot be reverted
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sort(reverse=True) sorts in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorted() lets you display your list in a particular order but doesn't affect the actual order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
#sorted()can also accept a reverse=True argument ex. print(sorted(cars, reverse=True))

#reverse() reverses the original order of the list. It does not sort backwards alphabetically
#It is permanent but can be reapplied to revert the list
print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#len() tells you the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars) #outputs 4 when working within python
#useful for determining things like how many enemies left to defeat in a game, number of registered users, etc
