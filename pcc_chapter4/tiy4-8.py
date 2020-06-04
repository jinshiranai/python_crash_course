#PCC Try It Yourself 4-8

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

#4-9 list comprehension style!
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)