# PCC Try It Yourself 9-13. Dice.

from random import randint

class Die:
    """A simple attempt to model a die."""
    def __init__(self, sides=6):
        """Initialize the side of the die."""
        self.sides = sides

    def roll_die(self):
        """Rolls the die with the determined number of sides."""
        print(f"You rolled a {randint(1, self.sides)}.")


d6 = Die()

roll_count = 0
while roll_count < 10:
    d6.roll_die()
    roll_count += 1

d10 = Die(10)

roll_count = 0
while roll_count < 10:
    d10.roll_die()
    roll_count += 1

d20 = Die(20)

roll_count = 0
while roll_count < 10:
    d20.roll_die()
    roll_count += 1