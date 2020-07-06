2020-07-06:
It's finished! Until I learn data analysis, anyway.

This project is meant as a showcase of everything I learned in the first part (chapters 1-11) of Python Crash Course.
This lottery simulates an actual lottery from a particular state in the US that I'm intimately familiar with.

[lottery sim screenshot](readme_pictures/lottery_sim.png)

On running, the user is presented with four options on how to run the simulation.

[lottery sim option 1](readme_pictures/lottery_sim_option1.png)

The first option has the computer pick a set of numbers and run until those numbers hit the jackpot.
It also promps the user as to whether they would like to run another simulation after completion.

[lottery sim option 2](readme_pictures/lottery_sim_option2.png)

The second option picks random numbers for every draw of the lottery.

[lottery sim option 3](readme_pictures/lottery_sim_option3.png)

The third option allows the user to input their own numbers for a single ticket. They lottery is drawn until that ticket wins.

[lottery sim option 4.1](readme_pictures/lottery_sim_option4_1.png)

Option four is where the bulk of the work comes in. Not only is the user allowed to chose their own numbers, but they do so for every draw of the lottery.
It continues until the user either hits the jackpot or quits.

[lottery sim option 4.2](readme_pictures/lottery_sim_option4_2.png)

Since that could possibly take forever, I added the ability for the user to save their progress on quit. The file is saved in JSON format.

[lottery sim option 4.3](readme_pictures/lottery_sim_option4_3.png)

Of course, the user can choose to load their progress on return, or start again from zero if they so choose.

And that's all for now! Once I've learned a bit more, I'll return to this project to maybe do data analysis things like approximating a truer random, seeing if any numbers appear to win more than others, breaking down the lottery draws down into the days/weeks/months/years/centuries/millenia it takes to hit the jackpot, and so on. Thank you for viewing my project!


2020-07-01:
Wrote a test case for the Lottery module.
Refactored the user input method to make it more testable.
The child class was causing more problems than it helped, so it got refactored back into the parent.
Moved the option explanations out of the module and into the main program (having it repeat every loop gets annoying).

TODO:
 - Implement the ability to save during Every Ticket User Ticket.(DONE)
 - Write tests for saving/loading.(ABANDONED)

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
