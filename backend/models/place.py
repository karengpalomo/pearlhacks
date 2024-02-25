from pydantic import BaseModel


class Place(BaseModel):
    id: int | None = None
    name: str
    description: str
    longitude: float
    latitude: float
    address: str
    rating: int
    hours: ['WeekdayTime'] = []
    tags: ['Tag'] = []
