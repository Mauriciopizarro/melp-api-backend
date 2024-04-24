from abc import ABC, abstractmethod
from domain.models import Restaurant


class RestaurantRepository(ABC):

    @abstractmethod
    def save(self, restaurant: Restaurant):
        pass

    @abstractmethod
    def get(self, restaurant_id: int) -> Restaurant:
        pass
