2020-07-01:
Wrote a test case for the Lottery module.
Refactored the user input method to make it more testable.
The child class was causing more problems than it helped, so it got refactored back into the parent.
Moved the option explanations out of the module and into the main program (having it repeat every loop gets annoying).

TODO:
 - Implement the ability to save during Every Ticket User Ticket.
 - Write tests for saving/loading.

2020-06-29:
Finished TODO work from the previous update.
Added a loop back to the main menu so the user can continue simulating if desired.

TODO:
 - Implement the ability to save during Every Ticket User Ticket.
 - Write tests for the number drawings.(DONE)

2020-06-28:
Renamed the lottery module from lottery.py to lottery_module.py.
Finished the skeleton of lottery_module.py.
Recreated lottery.py as the main lottery program.

TODO:
 - Finish the exit method so it confirms before quitting.(DONE)
 - Add intro text to the main program.(DONE)
 - Add lottery simulation style selection to the main program.(DONE)
  


The goal of this project is to use everything that I've learned until now
to craft a lottery simulation that accepts user input and runs until they
hit the jackpot under user-decided conditions.

After winning the lottery, the program will print a summary of the simulation,
including values such as money spent, net jackpot gain/loss, and time spent
broken down into weeks and years.
