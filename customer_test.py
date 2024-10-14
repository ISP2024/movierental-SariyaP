import re
import unittest 
from customer import Customer
from price_strategy import *
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 1,NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", 2, REGULAR)
        self.childrens_movie = Movie("Frozen", 3, CHILDREN)

    def test_total_price(self):
        c1 = Customer("Bill")
        c1.add_rental(Rental(self.new_movie, 1))
        c1.add_rental(Rental(self.childrens_movie, 3))
        self.assertEqual(4.5, c1.get_total_charge())
        c2 = Customer("Billy")
        c2.add_rental(Rental(self.regular_movie, 2))
        c2.add_rental(Rental(self.childrens_movie, 1))
        self.assertEqual(3.5, c2.get_total_charge())

    def test_total_point(self):
        c1 = Customer("Bill")
        c1.add_rental(Rental(self.new_movie, 1))
        c1.add_rental(Rental(self.childrens_movie, 1))
        self.assertEqual(2, c1.get_total_rental_points())
        c2 = Customer("Billy")
        c2.add_rental(Rental(self.new_movie, 2))
        c2.add_rental(Rental(self.childrens_movie, 1))
        self.assertEqual(3, c2.get_total_rental_points())

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
