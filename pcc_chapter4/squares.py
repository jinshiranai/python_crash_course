#code to introduce making a list using  for loop

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#or you can omit the square variable for more concise code
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#now let's try it with a list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)