import logging

from movie import Movie


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    
    def __init__(self, movie, days_rented): 
    	"""Initialize a new movie rental object for
    	   a movie with known rental period (daysRented).
    	"""
    	self.movie = movie
    	self.days_rented = days_rented

    def get_movie(self):
    	return self.movie

    def get_days_rented(self):
    	return self.days_rented

    def get_price(self,rental):
        try:
            return self.movie.get_price(rental.get_days_rented())
        except Exception:
            log = logging.getLogger()
            log.error(f"Movie {rental.get_movie()} has unrecognized priceCode {rental.get_movie().get_price_code()}")

    def get_rental_points(self, frequent_renter_points, rental):
        return frequent_renter_points + self.movie.get_rental_points(rental.get_days_rented())

