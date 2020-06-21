"""A module of a class modeling users."""

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
        self.login_attempts = 0

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

    def increment_login_attemtps(self):
        """Increment login attempts by one for each attempt."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts."""
        self.login_attempts = 0