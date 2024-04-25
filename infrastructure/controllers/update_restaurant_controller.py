from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, EmailStr
from application.services.update_restaurant_service import UpdateRestaurantService
from domain.exceptions import RestaurantNotFoundException

router = APIRouter()
update_restaurant_service = UpdateRestaurantService()


class UpdateRestaurantRequestDataModel(BaseModel):
    rating: int = Field(ge=0, le=4)
    email: EmailStr
    name: str
    site: str
    phone: str
    street: str
    city: str
    state: str
    latitude: float
    longitude: float

@router.put("/restaurants/update/{restaurant_id}")
async def update_restaurant(request: UpdateRestaurantRequestDataModel, restaurant_id):
    try:
        restaurant_json = {
            'rating': request.rating,
            'email': request.email,
            'name': request.name,
            'site': request.site,
            'phone': request.phone,
            'street': request.street,
            'city': request.city,
            'state': request.state,
            'latitude': request.latitude,
            'longitude': request.longitude
        }
        restaurant = update_restaurant_service.update_restaurant(restaurant_json, restaurant_id)
        response = {
            'message': 'Restaurant successfully updated',
            'restaurant_data': restaurant.dict()
        }
        return response
    except RestaurantNotFoundException:
        raise HTTPException(
            status_code=404, detail='Restaurant not found',
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail='Error updating a new restaurant',
        )