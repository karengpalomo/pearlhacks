from pydantic import BaseModel
from typing import List, Optional
from .place_tag import PlaceTag

class Place(BaseModel):
    id: Optional[int] = None
    name: str
    longitude: float
    latitude: float
    address: str
    rating: int
    tags: List[PlaceTag] = []
    photo_url: str

