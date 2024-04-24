from domain.models.Restaurant import Restaurant
from infrastructure.repository.RestaurantSqlRepository import RestaurantRepo


class UpdateRestaurantService:

    restaurant_repo = RestaurantRepo()

    def update_restaurant(self, update_restaurant_data, restaurant_id):
        restaurant = Restaurant(**update_restaurant_data)
        return self.restaurant_repo.update(restaurant, restaurant_id)