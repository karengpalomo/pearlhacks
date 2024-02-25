from pydantic import BaseModel
import datetime


class WeekdayTime(BaseModel):
    id: int | None = None
    day: str = ''
    start_time: datetime.time
    end_time = datetime.time