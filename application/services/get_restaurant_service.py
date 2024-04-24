from infrastructure.repository.RestaurantSqlRepository import RestaurantRepo


class GetRestaurantService:

    restaurant_repo = RestaurantRepo()

    def get_restaurant(self, restaurant_id):
        return self.restaurant_repo.get(restaurant_id)
