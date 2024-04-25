from domain.interface.restaurant_repository import RestaurantRepository
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
import statistics

class StatisticsRestaurantsService:

    @inject
    def __init__(self, restaurant_repo: RestaurantRepository = Provide[Injector.restaurant_repo]):
        self.restaurant_repo = restaurant_repo

    def get_restaurants_by_latitude_longitude_and_radius(self, latitude, longitude, radius):
        data = self.restaurant_repo.get_rest_by_lat_long_and_radius(latitude, longitude, radius)
        ratings = [restaurant.rating for restaurant in data]
        count = len(data)
        avg = sum(ratings) / len(ratings)
        if count < 2:
            stv = 'Unable to calculate the standard deviation because there were not enough points (less than 2) found to compute it.'
        else:
            stv = statistics.stdev(ratings)
        response = {
            "count": count,
            "avg": avg,
            "stv": stv
        }
        return response