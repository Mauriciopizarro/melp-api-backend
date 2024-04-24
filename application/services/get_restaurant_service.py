from domain.interface.restaurant_repository import RestaurantRepository
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector

class GetRestaurantService:

    @inject
    def __init__(self, restaurant_repo: RestaurantRepository = Provide[Injector.restaurant_repo]):
        self.restaurant_repo = restaurant_repo

    def get_restaurant(self, restaurant_id):
        return self.restaurant_repo.get(restaurant_id)
