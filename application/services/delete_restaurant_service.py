from dependency_injector.wiring import Provide, inject
from domain.interface.restaurant_repository import RestaurantRepository
from infrastructure.injector import Injector

class DeleteRestaurantService:
    @inject
    def __init__(self, restaurant_repo: RestaurantRepository = Provide[Injector.restaurant_repo]):
        self.restaurant_repo = restaurant_repo

    def delete_restaurant(self, restaurant_id):
        self.restaurant_repo.delete(restaurant_id)

