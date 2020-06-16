# Module for tiy8-12.

def make_sandwich(*items):
    """Displays a summary of an ordered sandwich."""
    item_s = 'items'
    if len(items) == 1:
        item_s = 'item'
    print(f"\nYou've ordered a sandwich with the following {item_s}:")
    for item in items:
        print(f" - {item}")