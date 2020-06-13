Chapter 5 introduces if, elif, else, and checking lists for specific values.

This is where I started getting annoyed with hardcoding variables to test my code.
This is also where I started getting comfortable enough with my ability to screw around.
tiy5-6.py is evidence of both those things.

For tiy5-6.py, I taught myself input() ahead of the book's schedule for the sake of testing
    my code in real time. It didn't feel right to directly alter variables in the code and then
    run the altered code to test outputs, because that's not how a user interacts with a program.
    So I taught myself input() and immediately ran into a problem.
Apparently, numbers entered with input() are stored as strings, not integers.
So then I had to teach myself how to fix that, and came across int() as well.
After that, I was able to test my tiy5-6.py with live input instead of directly altering
    the age variable for the desired outputs.
  
toppings.py also saw me teach myself the while loop early for similar reasons.
Lines 50 to 58 were the original sample code, but I wanted the user to be able to enter toppings
    themself and decide for themself when they were finished. Unfortunately, the code I added broke
    the original functionality of the demo code and rendered line 58 unreachable. I'd like to fix
    that at some point, but I feel like adding everything I did at that point in my development
    as a programmer renders that moot.

![toppings.py in action](https://raw.githubusercontent.com/jinshiranai/python_crash_course/master/pcc_chapter5/toppingsdotpy.png)
