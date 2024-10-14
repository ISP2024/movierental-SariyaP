from price_strategy import *


class Movie:
    """
    A movie available for rent.
    """
    
    def __init__(self, title, price_code, strategy: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code
        self.strategy = strategy

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_price(self, days):
        return self.strategy.get_price(days)

    def get_rental_points(self, days):
        return self.strategy.get_rental_points(days)
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
