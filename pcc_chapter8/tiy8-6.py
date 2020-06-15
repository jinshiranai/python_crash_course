# PCC Try It Yourself 8-6. City Names.

def city_country(city_name, country_name):
    """Returns a neatly formatted city-country pair."""
    city_country_pair = f"{city_name.title()}, {country_name.title()}"
    return city_country_pair

capital = city_country('avignon', 'gratia')
print(capital)

capital = city_country('visaradaya', 'samsara')
print(capital)

capital = city_country('xingto', 'nanboshi')
print(capital)