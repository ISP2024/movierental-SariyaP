from dataclasses import dataclass

from pricing import *


class Movie:
    """
    A movie available for rent.
    """

    @dataclass(frozen=True)
    def __init__(self, title: str, year: int, genre: list):
        # Initialize a new movie. 
        self.__title = title
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def is_genre(self, genre):
        return True if genre in self.__genre else False

    def __str__(self):
        return f"{self.__title} ({self.__year})"
