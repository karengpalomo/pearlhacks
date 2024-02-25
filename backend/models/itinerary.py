"""User model serves as the data object for representing registered users across application layers."""

from pydantic import BaseModel
from group import Group


class Itinerary(BaseModel):
    id: int | None = None
    name: str = ''
    group: Group | None = None
    activities: ['Activity'] = []