from typing import List, Optional
from pydantic import BaseModel

class EditProfileRequest(BaseModel):
    bio: Optional[str] = None
    location: Optional[str] = None
    tags_to_add: Optional[List[str]] = []
    tags_to_remove: Optional[List[str]] = []
