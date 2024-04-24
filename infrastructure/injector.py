from dependency_injector import containers, providers
from infrastructure.repository.RestaurantSqlRepository import RestaurantRepo


class Injector(containers.DeclarativeContainer):

    restaurant_repo = providers.Singleton(RestaurantRepo)


injector = Injector()
injector.wire(modules=[
    "application.services.get_restaurant_service",
    "application.services.delete_restaurant_service",
    "application.services.save_restaurant_service",
    "application.services.update_restaurant_service"
])