"""Module for a collection of classes simulating a lottery."""

from random import choice

class Lottery:
    """A simple attempt at a lottery simulation."""

    def __init__(self):
        """Initializes the lottery simulation."""

    def lottery_selection(self):
        """Pulls the numbers for a lottery."""
        lottery_pool = [value for value in range(1, 43)]
        lottery_choice = []
        drawn_number = ''

        while len(lottery_choice) < 5:
            drawn_number = choice(lottery_pool)
            
            if drawn_number not in lottery_choice:
                lottery_choice.append(drawn_number)
        
        return sorted(lottery_choice)

lottery = Lottery()
print(lottery.lottery_selection())
