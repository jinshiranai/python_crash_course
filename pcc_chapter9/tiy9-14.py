# PCC Try It Yourself 9-14. Lottery.

from random import choice

lottery = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

lottery_choice = []

while len(lottery_choice) < 5:
    lottery_choice.append(choice(lottery))

print("\nToday's winning numbers are:")
print(f"{lottery_choice[0]}, {lottery_choice[1]}, {lottery_choice[2]},",
        f"{lottery_choice[3]}, {lottery_choice[4]}")

print("\nIf these are your numbers, you win a prize!")

# 9-15. Lottery Analysis.
# Approach 1: Matching the ticket to the lottery.
my_ticket = []
tickets = 0

while my_ticket != lottery_choice:
    my_ticket = []
    tickets += 1

    while len(my_ticket) < 5:
        my_ticket.append(choice(lottery))

print(f"\nIt took {tickets} tickets for mine to match the lottery.")

# Approach 2: Matching the lottery to the ticket.
my_ticket = []
while len(my_ticket) < 5:
    my_ticket.append(choice(lottery))

lottery_count = 0

while lottery_choice != my_ticket:
    lottery_choice = []
    lottery_count += 1

    while len(lottery_choice) < 5:
        lottery_choice.append(choice(lottery))

print(f"It took {lottery_count} lotteries to match my ticket.")

# Approach 3: Random tickets AND lotteries.
my_ticket = []
lottery_choice = ['a']
lottery_count = 0

while lottery_choice != my_ticket:
    lottery_choice = []
    my_ticket = []
    lottery_count += 1

    while len(lottery_choice) < 5:
        lottery_choice.append(choice(lottery))
        my_ticket.append(choice(lottery))

print(f"It took {lottery_count} lotteries for my random tickets to win.")