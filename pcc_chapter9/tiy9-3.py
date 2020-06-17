# PCC Try It Yourself 9-3. Users.

class User:
    """A simple attempt to represent a user."""

    def __init__(self, first_name, last_name, username, email, location, age):
        """Initialize attributes of a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name.title()} {last_name.title()}"
        self.username = username
        self.email = email
        self.location = location
        self.age = age

    def describe_user(self):
        """Displays all current information of a user."""
        print(f"\nUsername: {self.username}")
        print(f"Name: {self.full_name}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"\n{self.username} has logged in.")
        print(f"Welcome back, {self.first_name.title()}!")


user_0 = User('jin', 'shiranai', '1337hax0rz6969', 'hackermann12@geemail.net',
            'Japan', 77)
user_1 = User('bob', 'douglas', 'bobdouglas1975', 'bobdouglas1975@aol.org',
            'America', 45)
user_2 = User('jillian', 'montgomery', 'jillymont421', 'p39nw4hjk2@notabot.biz',
            'Russia', 18)
user_3 = User('rosemary', 'warren', 'rosesformary',
            'rosewaterlikewater@kingdom.gra', 'Gratia', 537)

user_list = [user_0, user_1, user_2, user_3]

for user in user_list:
    user.describe_user()
    user.greet_user()