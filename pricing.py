from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days):
        # Straight $3 per day charge
        return 3*days


class RegularPrice(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for rented."""
        if days > 0:
            return 1
        return 0

    def get_price(self, days):
        # Two days for $2, additional days 1.50 per day.
        if days <=2:
            return 2
        return 2 + (days-2)*1.5


class ChildrenPrice(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for rented."""
        if days > 0:
            return 1
        return 0

    def get_price(self, days):
        # Three days for $1.50, additional days 1.50 per day.
        if days <= 3:
            return 1.5
        return 1.5 + (days - 3) * 1.5


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrenPrice()
