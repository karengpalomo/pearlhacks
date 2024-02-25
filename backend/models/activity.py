import datetime
from pydantic import BaseModel
from backend.models.place import Place


class Activity(BaseModel):
    id: int | None = None
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    place: Place

