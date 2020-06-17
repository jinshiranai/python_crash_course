# PCC Try It Yourself 9-1. Restaurant.

class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to ddescribe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Displays a summary of the restaurant."""
        print(f"\nThis restaurant's name is {self.restaurant_name}.")
        print(f"{self.restaurant_name} specializes in {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Simulates opening the restaurant."""
        print(f"\n{self.restaurant_name} is now open!")


restaurant = Restaurant("Azaziel's Pizza", 'pizza')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants.
restaurant_0 = Restaurant("Knockin' on Heaven's Door", 'manna')
restaurant_0.describe_restaurant()

restaurant_1 = Restaurant("The Last Tankard", 'spirits and tavern food')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Gilded Pagoda', 'Nanboshian dishes')
restaurant_2.describe_restaurant()