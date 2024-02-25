from sqlalchemy import ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.models.weekday_time import WeekDayTime
from backend.entities.entity_base import EntityBase
from datetime import time, datetime


class WeekdayTimeEntity(EntityBase):
    __tablename__ = 'week_day_time'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    day: Mapped[str] = mapped_column(String(100), nullable=False, default='')
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)


    @classmethod
    def from_model(cls, model: WeekDayTime) -> Self:
        return cls(
            id=model.id,
            day=model.day,
            start_time=datetime.strptime(model.start_time, '%H:%M').time(),
            end_time=datetime.strptime(model.end_time, '%H:%M').time()
        )
    
    def to_model(self) -> WeekDayTime:
        return WeekDayTime(
            id=self.id,
            day=self.day,
            start_time=self.start_time.strftime("%H:%M"),
            end_time=self.end_time.strftime("%H:%M")
        )
    