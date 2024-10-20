import csv
from dataclasses import dataclass
from typing import Collection

from pricing import *


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def get_title(self):
        return self.title

    def is_genre(self, genre):
        return genre in self.genre

    def __str__(self):
        return f"{self.title} ({self.year})"

    def get_year(self):
        return self.year

    def get_price_for_movie(self):
        if self.year == 2024:
            return NEW_RELEASE
        elif "children" in self.genre:
            return CHILDREN
        else:
            return REGULAR

class MovieCatalog(ABC):
    def __init__(self):
        self.__movies = []
        with open('movies.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if len(row) != len(header):
                    continue
                try:
                    int(row[2])
                except ValueError:
                    continue
                movie = Movie(row[1], int(row[2]), row[3:])
                self.__movies.append(movie)

    def get_movie(self, title, year=None):
        for movie in self.__movies:
            if movie.get_title() == title:
                if year is None or movie.get_year() == year:
                    return movie
        return None
