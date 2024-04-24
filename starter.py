import time
time.sleep(10)
from fastapi import FastAPI
from infrastructure.controllers import get_restaurant_controller, save_restaurant_controller

app = FastAPI()
app.include_router(get_restaurant_controller.router)
app.include_router(save_restaurant_controller.router)