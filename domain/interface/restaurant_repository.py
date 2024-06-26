from abc import ABC, abstractmethod
from domain.models import Restaurant


class RestaurantRepository(ABC):

    @abstractmethod
    def save(self, restaurant: Restaurant) -> str:
        pass

    @abstractmethod
    def get(self, restaurant_id: str) -> Restaurant:
        pass

    @abstractmethod
    def update(self, restaurant_id: str, restaurant: Restaurant) -> Restaurant:
        pass

    @abstractmethod
    def delete(self, restaurant_id: str):
        pass

    @abstractmethod
    def get_rest_by_lat_long_and_radius(self, latitude, longitude, radius):
        pass
