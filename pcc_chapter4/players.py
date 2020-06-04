#code to introduce the slice to work with sections of a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#lets slice up the middle now
print(players[1:4])

#no first index starts from the beginning
print(players[:4])

#and no last index goes until the end
print(players[2:])

#negative indexing lets you slice from the end no matter how much the list changes
print(players[-3:])

#looping through a slice
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())