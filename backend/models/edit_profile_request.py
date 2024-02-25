from typing import List, Optional
from pydantic import BaseModel

class EditProfileRequest(BaseModel):
    bio: Optional[str] = None
    location: Optional[str] = None
    tags: Optional[List[str]]
