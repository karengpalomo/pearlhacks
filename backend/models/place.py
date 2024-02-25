from pydantic import BaseModel
from ..models.place_tag import PlaceTag



class Place(BaseModel):
    id: int | None = None
    name: str
    longitude: float
    latitude: float
    address: str
    rating: int
    tags: ['PlaceTag'] = []
    photo_url: str 
