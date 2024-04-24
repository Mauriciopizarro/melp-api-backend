from fastapi import APIRouter, HTTPException
from application.services.save_restaurant_service import SaveRestaurantService
from pydantic import BaseModel, Field, EmailStr

router = APIRouter()
save_restaurant_service = SaveRestaurantService()


class SaveRestaurantRequestDataModel(BaseModel):
    rating: int = Field(ge=1, le=4)
    email: EmailStr
    name: str
    site: str
    phone: str
    street: str
    city: str
    state: str
    latitude: float
    longitude: float

@router.post("/restaurants/save")
async def save_restaurant(request: SaveRestaurantRequestDataModel):
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
        save_restaurant_service.save_restaurant(restaurant_json)
        return 'Restaurant created successfully'
    except Exception:
        raise HTTPException(
            status_code=404, detail='Error saving a new restaurant',
        )