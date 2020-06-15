# Code demonstrating returning a value from a function.
# Updated to add optional middle name.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a fullname, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)