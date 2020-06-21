"""A class tht can be used to represent a restaurant."""

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