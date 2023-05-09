"""Weather routes module"""
from fastapi import APIRouter

weather_router = APIRouter(prefix="/api/users", tags=["Users"])


@weather_router.post("/city",
                     summary="City input")
def get_city_data_differences():
    print("Here")
    return {"message": "success"}
