from domain.models.Restaurant import Restaurant
from infrastructure.repository.RestaurantSqlRepository import RestaurantRepo


class SaveRestaurantService:

    restaurant_repo = RestaurantRepo()

    def save_restaurant(self, restaurant_data):
        restaurant = Restaurant(**restaurant_data)
        return self.restaurant_repo.save(restaurant)
