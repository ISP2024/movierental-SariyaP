import unittest
from customer import Customer
from pricing import *
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 1, NEW_RELEASE)
        self.regular_movie = Movie("Air", 2, REGULAR)
        self.childrens_movie = Movie("Frozen", 3, CHILDREN)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air",1, REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(REGULAR, m.strategy)


    def test_rental_price(self):
        rental = Rental(NEW_RELEASE, 1)
        self.assertEqual(rental.get_price(rental), 3.0)
        rental = Rental(NEW_RELEASE, 5)
        self.assertEqual(rental.get_price(rental), 15.0)
        rental = Rental(REGULAR, 5)
        self.assertEqual(rental.get_price(rental), 6.5)
        rental = Rental(CHILDREN, 5)
        self.assertEqual(rental.get_price(rental), 4.5)

    def test_rental_points(self):
        rental = Rental(NEW_RELEASE, 1)
        self.assertEqual(rental.get_rental_points(0, rental), 1)
        rental = Rental(REGULAR, 5)
        self.assertEqual(rental.get_rental_points(0, rental), 1)
        rental = Rental(CHILDREN, 10)
        self.assertEqual(rental.get_rental_points(0, rental), 1)
