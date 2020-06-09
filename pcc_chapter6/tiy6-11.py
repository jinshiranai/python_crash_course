# PCC Try It Yourself 6-11. Cities.

cities = {
    'new york': {
        'country': 'america',
        'population': 8_399_000,
        'area': 784,
        },
    'tokyo': {
        'country': 'japan',
        'population': 13_929_280,
        'area': 2194,
        },
    'london': {
        'country': 'united kingdom',
        'population': 8_908_081,
        'area': 1572,
        },
    }

for city, city_info in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tArea: {city_info['area']}km\u00b2")