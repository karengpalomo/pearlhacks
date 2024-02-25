from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
from .tag import Tag
from .place import Place

class User(BaseModel):
        
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    occupation: str = ""
    location: str = ""
    age: Optional[int] = None
    bio: str = ""
    tags: List[Tag] = []  # Use List[Type] for a list of custom types
    friends: List[User] = []  # List of User instances, note the forward declaration
    favorites: List[Place] = []  # List of Place instances
    class Config:
        arbitrary_types_allowed = True
        
User.model_rebuild()