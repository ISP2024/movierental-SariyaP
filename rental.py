import logging

from movie import Movie
from pricing import PriceStrategy


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    
    def __init__(self, price_code, strategy: PriceStrategy, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.strategy = strategy
        self.price_code = price_code
        self.days_rented = days_rented

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_movie(self):
        return self.strategy

    def get_days_rented(self):
        return self.days_rented

    def get_price(self, rental):
        return self.strategy.get_price(rental.get_days_rented())

    def get_rental_points(self, frequent_renter_points, rental):
        return frequent_renter_points + self.strategy.get_rental_points(rental.get_days_rented())

