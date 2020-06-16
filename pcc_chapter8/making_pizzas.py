# Code demonstrating importing modules.
#import pizza

#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing specific functions.
#from pizza import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Giving a function an alias with as.
#from pizza import make_pizza as mp

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Giving a module an alias with as.
#import pizza as p

#p.make_pizza(16, 'pepperoni')
#p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing ALL THE FUNCTIONS in a module.
from pizza import*
# This is usually not a good idea unless it's your own module.

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')