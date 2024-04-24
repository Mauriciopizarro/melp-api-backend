from domain.models.Restaurant import Restaurant
from domain.interface.restaurant_repository import RestaurantRepository
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector


class UpdateRestaurantService:

    @inject
    def __init__(self, restaurant_repo: RestaurantRepository = Provide[Injector.restaurant_repo]):
        self.restaurant_repo = restaurant_repo

    def update_restaurant(self, update_restaurant_data, restaurant_id):
        restaurant = Restaurant(**update_restaurant_data)
        return self.restaurant_repo.update(restaurant, restaurant_id)