"""User model serves as the data object for representing registered users across application layers."""

from pydantic import BaseModel
from .group import Group
from typing import List, Optional
from .activity import Activity


class Itinerary(BaseModel):
    id: int | None = None
    name: str = ''
    group: Group | None = None
    activities: List['Activity'] = []