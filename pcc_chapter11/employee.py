# PCC Try It Yourself 11-3. Employee.

class Employee:
    """Models a humble employee."""

    def __init__(self, first, last, salary):
        """Initialize the basic attributes of the employee."""
        self.first_name = first
        self.last_name = last
        self.salary = int(salary)

    def give_raise(self, payraise=5000):
        """Gives the hardworking employee a raise."""
        self.salary += payraise