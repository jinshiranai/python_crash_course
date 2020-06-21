# PCC Try It Yourself 9-1. Restaurant.

class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to ddescribe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Displays a summary of the restaurant."""
        print(f"\nThis restaurant's name is {self.restaurant_name}.")
        print(f"{self.restaurant_name} specializes in {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Simulates opening the restaurant."""
        print(f"\n{self.restaurant_name} is now open!")

    def set_number_served(self, customers_served):
        """Sets the number of customers served."""
        self.number_served = customers_served

    def increment_number_served(self, party_size):
        """Increments the number of customers served."""
        self.number_served += party_size


# 9-6. Ice Cream Stand.
class IceCreamStand(Restaurant):
    """A simple attempt to represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'fudge ripple',
                        'peanut butter', 'rasberry creme', 'rocky road',
                        'cheesecake', 'birthday cake', 'brownie supreme']

    def get_flavors(self):
        """Prints a list of the available flavors."""
        print("\nToday's available flavors are:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")


restaurant = Restaurant("Azaziel's Pizza", 'pizza')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants.
restaurant_0 = Restaurant("Knockin' on Heaven's Door", 'manna')
restaurant_1 = Restaurant("The Last Tankard", 'spirits and tavern food')
restaurant_2 = Restaurant('Gilded Pagoda', 'Nanboshian dishes')

eateries = [restaurant_0, restaurant_1, restaurant_2]

for eatery in eateries:
    eatery.describe_restaurant()

# 9-4. Number Served.
restaurant.set_number_served(54_234)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)

# 9-6 continued.
ice_cream_stand_0 = IceCreamStand("Azaziel's Frozen Treats",
                                    'frozen confections')
ice_cream_stand_0.open_restaurant()
ice_cream_stand_0.get_flavors()