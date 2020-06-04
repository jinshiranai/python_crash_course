#Python Crash Course Try It Yourself 3-4,5,6,7,9
#Making a guest list and altering it

#3-9 is the len()s sprinkled throughout

#3-4
guests = ['brian adams', 'miranda willan', 'saho fujikake']
print(f"Dear {guests[0].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[1].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[2].title()}, I humbly request your presence for a fancy-schmancy dinner.")
invited = len(guests)
print(f"There are currently {invited} guests invited to dinner.")

#3-5
print(f"\nAh, it appears {guests[0].title()} is unable to attend.")
absent = [guests.pop(0)]
guests.insert(0, 'emmanuel chambliss')
print(f"Dear {guests[0].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[1].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[2].title()}, I humbly request your presence for a fancy-schmancy dinner.")
invited = len(guests)
print(f"There are currently {invited} guests invited to dinner.")

#3-6
print("\nJubilations! It would appear a larger table has been procured for the event.")
guests.insert(0, 'scott overman')
guests.insert(2, 'zoey bishop')
guests.append('tripp roybal')
print(f"Dear {guests[0].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[1].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[2].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[3].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[4].title()}, I humbly request your presence for a fancy-schmancy dinner.")
print(f"Dear {guests[5].title()}, I humbly request your presence for a fancy-schmancy dinner.")
invited = len(guests)
print(f"There are currently {invited} guests invited to dinner.")

#3-7
print('\nTragedy! It is most unfortunate but the table will not arrive in time for the dinner party. Only two guests may attend.')
uninvited = guests.pop(0)
print(f'Apologies, {uninvited.title()}, but unfortunately you have been uninvited from the soiree. Another time, my friend.')
uninvited = guests.pop(0)
print(f'Apologies, {uninvited.title()}, but unfortunately you have been uninvited from the soiree. Another time, my friend.')
uninvited = guests.pop(1)
print(f'Apologies, {uninvited.title()}, but unfortunately you have been uninvited from the soiree. Another time, my friend.')
uninvited = guests.pop()
print(f'Apologies, {uninvited.title()}, but unfortunately you have been uninvited from the soiree. Another time, my friend.')
print(f'{guests[0].title()}, your attendance is still requested. I look forward to your warm presence.')
print(f'{guests[1].title()}, your attendance is still requested. I look forward to your warm presence.')
invited = len(guests)
print(f"There are currently {invited} guests invited to dinner.")
del guests[0]
del guests[0]
print(guests)