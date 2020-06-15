# PCC Try It Yourself 8-3. T-Shirt.

def make_shirt(size, text):
    """Describes an ordered shirt."""
    print(f"You've ordered a {size}-sized shirt with the text:")
    print(f'\t"{text}"')

make_shirt('medium', 'No Bike No Life')
make_shirt(size='small', text='Bikes = n+1')

# 8-4. Large Shirts.
def make_shirt(size='large', text='I Love Python'):
    """Describes an ordered shirt."""
    print(f"You've ordered a {size}-sized shirt with the text:")
    print(f'\t"{text}"')

make_shirt()
make_shirt('medium')
make_shirt(size='small', text='With Legs Like These...')