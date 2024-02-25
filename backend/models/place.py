from pydantic import BaseModel
from ..models.place_tag import PlaceTag



class Place(BaseModel):
    id: int | None = None
    name: str
    description: str
    longitude: float
    latitude: float
    address: str
    rating: int
    hours: ['WeekdayTime'] = []
    tags: ['PlaceTag'] = []
