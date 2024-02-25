import datetime
from datetime import time
from pydantic import BaseModel
from backend.models.place import Place
from typing import ClassVar



class Activity(BaseModel):
    id: int | None = None
    date: datetime.date
    start_time: ClassVar[time]
    end_time: ClassVar[time]
    place: Place

