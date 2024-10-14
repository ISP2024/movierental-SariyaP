# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from price_strategy import *

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 0, NEW_RELEASE),
        Movie("Oppenheimer", 1, REGULAR),
        Movie("Frozen", 2, CHILDREN),
        Movie("Bitconned", 1, NEW_RELEASE),
        Movie("Particle Fever", 2, REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
