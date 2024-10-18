from pricing import *


class Movie:
    """
    A movie available for rent.
    """
    
    def __init__(self, title, strategy: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.strategy = strategy

    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
