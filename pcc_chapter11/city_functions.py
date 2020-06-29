# Try It Yourself 11-1. City, Country.

def city_country(city, country, population=''):
    """Returns a neatly formatted city-country pair with optional population."""

    formatted_city_country = f"{city}, {country}"

    if population:
        return f"{formatted_city_country.title()} - population {population}"
    else:
        return formatted_city_country.title()