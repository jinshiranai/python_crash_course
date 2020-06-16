# PCC Try It Yourself 8-12. Sandwiches.

#def make_sandwich(*items):
#    """Displays a summary of an ordered sandwich."""
#    item_s = 'items'
#    if len(items) == 1:
#        item_s = 'item'
#    print(f"\nYou've ordered a sandwich with the following {item_s}:")
#    for item in items:
#        print(f" - {item}")

# 8-16. Imports.
#import sandwich_function
#from sandwich_function import make_sandwich
#from sandwich_function import make_sandwich as ms
#import sandwich_function as sf
from sandwich_function import *

make_sandwich('ham')
make_sandwich('turkey', 'bacon', 'cheddar', 'onion', 'lettuce')
make_sandwich('tuna', 'mayo', 'corn')
make_sandwich('potato salad', 'pastrami')