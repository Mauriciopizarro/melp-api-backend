from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Restaurant(BaseModel):

    id: Optional[str]
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
