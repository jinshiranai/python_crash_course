# PCC Try It Yourself 7-10. Dream Vacation.

polling = True
vacation_poll = {}
while polling:
    name = input("\nHello! May we have your name please? ")
    print(f"Thank you, {name}, and welcome to Azaziel's Getaways poll.")

    place = input("\nIf you could go anywhere, where would you want to go? ")
    print(f"Wow, {place} sounds like a great place. Thank you!")

    vacation_poll[name] = place

    poll_repeat = input("\n Would you like to allow another being to respond?"
        " (y/n) ")
    if poll_repeat == 'n':
        polling = False

# Poll results!
print("\n\n***Poll Results***")
for name, place in vacation_poll.items():
    print(f"{name} wants to go to {place}. Isn't that nice.")

print("\nThank you for your participation!")