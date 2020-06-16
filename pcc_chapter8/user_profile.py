# Code demonstrating using arbitrary keyword arguments.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)

# PCC Try It Yourself 8-13. User Profile.
user_profile = build_profile('jin', 'shiranai', team='blau blitzen',
                            height='182', weight='80')

print(user_profile)