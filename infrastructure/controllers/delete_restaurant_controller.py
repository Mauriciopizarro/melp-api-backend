from fastapi import APIRouter, HTTPException
from application.services.delete_restaurant_service import DeleteRestaurantService

router = APIRouter()
delete_restaurant_service = DeleteRestaurantService()


@router.delete("/restaurants/delete/{restaurant_id}")
async def delete_restaurant(restaurant_id: str):
    try:
        delete_restaurant_service.delete_restaurant(restaurant_id)
        return "Restaurant deleted"
    except Exception:
        raise HTTPException(
            status_code=404, detail='Error deleting a restaurant',
        )