from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional
from .user import User


class Group(BaseModel):
    id: int | None = None
    name: str = ''
    members: List[User] = [] 
