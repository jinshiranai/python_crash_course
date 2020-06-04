#code to introduce tuples

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#tuples can't be modified so this returns an error
#dimensions[0] = 250

#tuples can be looped through like lists
for dimension in dimensions:
    print(dimension)

#tuples can't be modified, but their variable can be overwritten entirely
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)