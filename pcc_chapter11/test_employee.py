# Test case for Try It Yourself 11-3.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """A set of tests for the class Employee."""

    def setUp(self):
        """Create an employee for use in all test methods."""
        self.employee = Employee('Tsuyomi', 'Seiryu', 500000)

    def test_give_default_raise(self):
        """Test that giving a default raise works properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 505000)

    def test_give_custom_raise(self):
        """Test that giving a non-default value raise works properly."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 510000)


if __name__ == '__main__':
    unittest.main()