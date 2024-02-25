from typing import Optional, List
from pydantic import BaseModel, Annotated, Field

class SearchParams(BaseModel):
    tags: Optional[List[str]] = None
    availability: Optional[tuple[str, str]] = None
    radius: Optional[Annotated[int, Field(strict=True, le=40000)]]
    prices: Optional[List[str]] = None
    longitude: float
    latitude: float