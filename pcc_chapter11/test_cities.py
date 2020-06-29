# Try It Yourself 11-1 test file.

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city-country pairs like 'Avignon, Gratia' work?"""

        formatted_city_country = city_country('avignon', 'gratia')
        self.assertEqual(formatted_city_country, 'Avignon, Gratia')

    def test_city_country_population(self):
        """
        Do city-country pairs with populations like
        'Avignon, Gratia - population 85000' work?
        """

        formatted_city_country = city_country('avignon', 'gratia', '85000')
        self.assertEqual(formatted_city_country,
            'Avignon, Gratia - population 85000')


if __name__ == '__main__':
    unittest.main()