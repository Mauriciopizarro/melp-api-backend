from infrastructure.repository.RestaurantSqlRepository import RestaurantRepo


class DeleteRestaurantService:
    restaurant_repo = RestaurantRepo()

    def delete_restaurant(self, restaurant_id):
        self.restaurant_repo.delete(restaurant_id)

