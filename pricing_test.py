import unittest
from movie import Movie
from pricing import *

class TestPrice(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("New Release Movie", 2024, [])
        self.children_movie = Movie("Children's Movie", 2023, ["children"])
        self.regular_movie = Movie("Regular Movie", 2023, [])

    def test_price_strategy(self):
        self.assertEqual(self.new_movie.get_price_for_movie(), NEW_RELEASE)
        self.assertEqual(self.regular_movie.get_price_for_movie(), REGULAR)
        self.assertEqual(self.children_movie.get_price_for_movie(), CHILDREN)