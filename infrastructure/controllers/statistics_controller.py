from fastapi import APIRouter, HTTPException
from application.services.restaurants_statistics_service import StatisticsRestaurantsService

router = APIRouter()
statistics_service = StatisticsRestaurantsService()

@router.get("/restaurants/statistics/")
async def get_restaurants(latitude, longitude, radius):
    try:
        return statistics_service.get_restaurants_by_latitude_longitude_and_radius(float(latitude), float(longitude), float(radius))
    except Exception:
        raise HTTPException(
            status_code=404, detail='Error in statistics',
        )
