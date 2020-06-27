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


class AutoLottery(Lottery):
    """Simulates a lottery until jackpot with various ticket conditions."""

    def __init__(self):
        """Initialize attributes of Lottery."""
        super().__init__()
    
    def single_ticket_lottery(self):
        """Simulates playing the lottery with a set ticket."""
        ticket_numbers = self.lottery_selection()
        winning_numbers = ''
        draw_count = 0

        print(f"\nYour numbers are: {ticket_numbers}")

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()

        print(f"It took {draw_count} draws to win the lottery.")
        print(f"The winning ticket was: {winning_numbers}")

    def random_ticket_lottery(self):
        """Simulates playing the lottery with a random ticket every draw."""
        ticket_numbers = ' '
        winning_numbers = ''
        draw_count = 0

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()
            ticket_numbers = self.lottery_selection()

        print(f"It took {draw_count} draws to win the lottery.")
        print(f"The winning ticket was: {winning_numbers}")

    def lucky_numbers_ticket_lottery(self):
        """
        Simulates playing the lottery with a single ticket of
        user-chosen 'lucky numbers'.
        """

        ticket_numbers = []
        winning_numbers = ''
        draw_count = 0

        while len(ticket_numbers) < 5:
            chosen_number = input("\nPlease enter your number: ")
            try:
                chosen_number = int(chosen_number)
            except ValueError:
                print("Only numbers, please.")
            else:
                ticket_numbers.append(chosen_number)
                ticket_numbers = sorted(ticket_numbers)

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()

        print(f"It took {draw_count} draws to win the lottery.")


lottery = AutoLottery()
lottery.lucky_numbers_ticket_lottery()