from pydantic import BaseModel

class PlaceTag(BaseModel):
    id: int | None = None
    name: str