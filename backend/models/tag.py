"""Club model serves as the data object for representing a specific club."""

from pydantic import BaseModel

class Tag(BaseModel):
    id: int | None = None
    name: str