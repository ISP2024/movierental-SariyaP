import csv
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
        return genre in self.__genre

    def __str__(self):
        return f"{self.__title} ({self.__year})"

    def get_year(self):
        return self.__year

class MovieCatalog(ABC):
    def __init__(self):
        self.__movies = []
        with open('movies.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                movie_id, title, year, genres_str = row
                genres = genres_str.split('|')
                movie = Movie(title, int(year), genres)
                self.__movies.append(movie)

    def get_movie(self, title, year=None):
        for movie in self.__movies:
            if movie.get_title() == title:
                if year is None or movie.get_year() == year:
                    return movie
        return None

