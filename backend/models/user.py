"""User model serves as the data object for representing registered users across application layers."""

from pydantic import BaseModel
from .tag import Tag



class User(BaseModel):
    id: int | None = None
    username: str = ""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    occupation: str = ""
    location: str = ""
    age: int | None = None
    bio: str = ""
    tags: list['Tag'] = []
    friends: list['User'] = []