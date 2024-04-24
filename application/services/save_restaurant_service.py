from domain.models.Restaurant import Restaurant
from domain.interface.restaurant_repository import RestaurantRepository
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector


class SaveRestaurantService:

    @inject
    def __init__(self, restaurant_repo: RestaurantRepository = Provide[Injector.restaurant_repo]):
        self.restaurant_repo = restaurant_repo

    def save_restaurant(self, restaurant_data):
        restaurant = Restaurant(**restaurant_data)
        return self.restaurant_repo.save(restaurant)
