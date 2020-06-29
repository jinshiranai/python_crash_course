import lottery_module

# Greet the user.
print("\nHello and welcome to the [REDACTED] lottery simulator!")
input("\nPress 'enter' to continue...")

# Begin the simulation.
lottery = lottery_module.AutoLottery()
lottery.lottery_style_select_menu()