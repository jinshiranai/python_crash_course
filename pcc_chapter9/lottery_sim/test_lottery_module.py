# Test cases for the Lottery and AutoLottery classes.

import unittest
from lottery_module import Lottery

class TestLottery(unittest.TestCase):
    """Tests for the class Lottery."""
       
    def setUp(self):
        """
        Spawns an instance of Lottery and draws numbers for use
        in all test methods.
        """
        self.lottery = Lottery()
        self.lottery_draw = self.lottery.lottery_selection()

    def test_length_of_draw(self):
        """Checks that the lottery draws are in a list of length 5."""
        self.assertEqual(len(self.lottery_draw), 5)

    def test_no_values_less_than_one(self):
        """Checks that the lottery only pulls numbers >= 1."""
        for value in self.lottery_draw:
            self.assertTrue(value >= 1)

    def test_no_values_greater_than_forty_two(self):
        """Checks that the lottery only pulls numbers <= 42."""
        for value in self.lottery_draw:
            self.assertTrue(value <= 42)

    def test_no_repeat_values(self):
        """Checks that there are no repeat pulls in the lottery numbers."""
        for value in self.lottery_draw:
            self.assertTrue(self.lottery_draw.count(value) == 1)
    
    def test_validate_user_number(self):
        """Checks that this method only accepts and returns valid inputs."""
        self.assertEqual(self.lottery.validate_user_number('1'), 1)
        self.assertEqual(self.lottery.validate_user_number('0'), None)
        self.assertEqual(self.lottery.validate_user_number('43'), None)
        self.assertEqual(self.lottery.validate_user_number('twelve'), None)

if __name__ == '__main__':
    unittest.main()