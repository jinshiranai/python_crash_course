import lottery_module

# Greet the user.
print("\nHello and welcome to the [REDACTED] lottery simulator!")
input("\nPress 'enter' to continue...")

# Present the user with their options.
input("\n\nHere are your simulation options:")
print("\n- 1 - Computer-generated Lucky Numbers:")
input("\tThe computer chooses a single ticket for you "
            "and runs the lottery until you win.")

print("\n- 2 - Computer-generated Quick Picks:")
input("\tThe computer generates a new ticket for every draw of the lottery.")

print("\n- 3 - User-generated Lucky Numbers:")
input("\tEnter your own lucky numbers and see just how lucky they are!")

print("\n- 4 - Every Ticket User Ticket:")
print("\tBe the master of your own fate and choose your own "
            "numbers for every draw of the lottery!")
input("\t<This mode allows you to save your progress.>")

# Begin the simulation.
if __name__ == '__main__':
    lottery = lottery_module.Lottery()
    lottery.lottery_style_select_menu()