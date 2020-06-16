# PCC Try It Yourself 8-14. Cars.

def car_profile(manufacturer, model, **car_info):
    """Build a dictionary containing a car's information."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = car_profile('toyota', 'aqua', color='dark blue', hybrid=True)
print(car)