from fastapi import APIRouter, HTTPException
from application.services.get_restaurant_service import GetRestaurantService

router = APIRouter()
restaurant_service = GetRestaurantService()


@router.get("/restaurants/get/{restaurant_id}")
async def get_restaurants(restaurant_id: str):
    try:
        return restaurant_service.get_restaurant(restaurant_id)
    except Exception:
        raise HTTPException(
            status_code=404, detail='Error getting a restaurant',
        )
