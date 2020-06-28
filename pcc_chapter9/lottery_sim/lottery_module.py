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

    def user_chosen_ticket(self):
        """Prompts the user to select numbers for their ticket."""
        user_ticket = []
        while len(user_ticket) < 5:
            chosen_number = input("\nPlease enter your number (1-42): ")
            if chosen_number == 'q':
                raise SystemExit
            else:
                try:
                    chosen_number = int(chosen_number)
                except ValueError:
                    print("Only numbers, please.")
                else:
                    if chosen_number > 42 or chosen_number < 1:
                        print("Please choose a number between 1 and 42 inclusive.")
                    else:
                        user_ticket.append(chosen_number)
                        
        return sorted(user_ticket)

    def user_quit(self):
        """Measures taken to ensure the user actually wants to quit."""
        quit_check = input("Are you sure you want to quit?(y/n) ")
        if quit_check == 'q':
            quit


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

        ticket_numbers = self.user_chosen_ticket()
        winning_numbers = ''
        draw_count = 0

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()
            
        print(f"It took {draw_count} draws to win the lottery.")

    def every_ticket_user_ticket(self):
        """Every ticket is chosen by the user until jackpot or they quit."""
        print("\nThis will continue until you hit the jackpot or quit.")
        print("Remember, you can quit at any time by entering 'q'.")

        winning_numbers = ' '
        ticket_numbers = ''
        draw_count = 0

        while winning_numbers != ticket_numbers:
            draw_count += 1
            ticket_numbers = self.user_chosen_ticket()
            winning_numbers = self.lottery_selection()
                        
            if winning_numbers == ticket_numbers:
                print("\nWow, you actually won the lottery! Congratulations!")
                print(f"It only took {draw_count} attempts!")
            else:
                input(f"\nYour numbers: {ticket_numbers}")
                input(f"Winning numbers: {winning_numbers}")
                print("\nLooks like you didn't win this time.")
                input(f"Maybe ticket number {draw_count + 1} will be the one!")