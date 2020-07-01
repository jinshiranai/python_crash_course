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

    def validate_user_number(self, chosen_number):
        """Checks that the user-selected number is valid before appending."""
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
                    return chosen_number
    
    def user_chosen_ticket(self):
        """Prompts the user to select numbers for their ticket."""
        user_ticket = []
        while len(user_ticket) < 5:
            valid_number = ''
            chosen_number = input("\nPlease enter your number (1-42): ")
            valid_number = self.validate_user_number(chosen_number)
            if valid_number:
                if valid_number not in user_ticket:
                    user_ticket.append(valid_number)
                else:
                    print("You've already chosen that number!")
                        
        return sorted(user_ticket)

    
    def user_quit(self):
        """Measures taken to ensure the user actually wants to quit."""
        quit_check = input("Are you sure you want to quit?(y/n) ")
        if quit_check == 'y':
            print("\nSee You Space Cowboy.")
            raise SystemExit
        else:
            print("Returning to the main menu...")
            self.lottery_style_select_menu()

    def replay_loop(self):
        """Loops back to the menu if the user wants to try again."""
        play_again = input("\nWould you like to run another simulation?(y/n): ")
        if play_again == 'y':
            self.lottery_style_select_menu()
        else:
            self.user_quit()

    def lottery_style_select_menu(self):
        """Presents the user with options for how to run the lottery."""

        style_select_loop = True
        while style_select_loop:
            style_selection = input("\n\nSo what will it be? Make your choice "
                "by entering 1, 2, 3, or 4: ")
            
            if style_selection == '1':
                style_select_loop = False
                self.single_ticket_lottery()
            elif style_selection == '2':
                style_select_loop = False
                self.random_ticket_lottery()
            elif style_selection == '3':
                style_select_loop = False
                self.lucky_numbers_ticket_lottery()
            elif style_selection == '4':
                style_select_loop = False
                self.every_ticket_user_ticket()
            else:
                print("\nI'm sorry, please enter a number from "
                    "1 to 4")
    
    def single_ticket_lottery(self):
        """Simulates playing the lottery with a set ticket."""
        ticket_numbers = self.lottery_selection()
        winning_numbers = ''
        draw_count = 0

        print(f"\nYour numbers are: {ticket_numbers}")
        print("Running simulation...")

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()

        print(f"\nIt took {draw_count} draws to win the lottery.")

        self.replay_loop()

    def random_ticket_lottery(self):
        """Simulates playing the lottery with a random ticket every draw."""
        ticket_numbers = ' '
        winning_numbers = ''
        draw_count = 0

        print("\nRunning simulation...")

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()
            ticket_numbers = self.lottery_selection()

        print(f"\nIt took {draw_count} draws to win the lottery.")
        print(f"The winning ticket was: {winning_numbers}")

        self.replay_loop()

    def lucky_numbers_ticket_lottery(self):
        """
        Simulates playing the lottery with a single ticket of
        user-chosen 'lucky numbers'.
        """

        ticket_numbers = self.user_chosen_ticket()
        winning_numbers = ''
        draw_count = 0

        print(f"\nYour numbers are: {ticket_numbers}")
        print("Running simulation...")

        while winning_numbers != ticket_numbers:
            draw_count += 1
            winning_numbers = self.lottery_selection()
            
        print(f"\nIt took {draw_count} draws to win the lottery.")

        self.replay_loop()

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