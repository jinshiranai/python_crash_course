#PCC Try It Yourself 4-5

millions = [one for one in range(1,1000001)]
print(min(millions))
print(max(millions))
print(sum(millions))

#4-10 slices
print("\nThe first three items in this list are:")
print(millions[:3])

print("\nThree items from the middle are:")
print(millions[435623:435626])

print("\nThe last three items in the list are:")
print(millions[-3:])