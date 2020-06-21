"""Module for modeling admin-type users."""

from user import User

class Privileges:
    """Class to house the privileges of an admin."""

    def __init__(self):
        """Initialize the privileges available to an admin."""
        self.privileges = ["can add post", "can delete post", "can ban user",
                            "can delete user", "can promote to admin"]
    
    def show_privileges(self):
        """Lists the privileges of an admin."""
        print("\nPrivileges available to admin:")
        for privilege in self.privileges:
            print(f" - {privilege.title()}")


class Admin(User):
    """A user with special administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location, age):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to admins.
        """
        super().__init__(first_name, last_name, username, email, location, age)
        self.privileges = Privileges()