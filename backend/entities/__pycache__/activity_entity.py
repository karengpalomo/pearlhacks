from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.models.activity import Activity
import datetime


class ActivityEntity(EntityBase):
    __tablename__ = 'itinerary'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    date: Mapped[datetime.date] = mapped_column(datetime.date, nullbale=False)
    start_time: Mapped[datetime.time] = mapped_column(datetime.time, nullable=False)
    end_time: Mapped[datetime.time] = mapped_column(datetime.time, nullable=False)
    store: Mapped[StoreEntity] = mapped_column(StoreEntity, nullable=False)

    @classmethod
    def from_model(cls, model: Activity) -> Self:
        return cls(
            id=model.id,
            date=model.date,
            start_time=model.start_time,
            end_time=model.end_time,
            store=model.store
        )

    def to_model(self) -> Activity:
        return Activity(
            id=self.id,
            date=self.date,
            start_time=self.start_time,
            end_time=self.end_time,
            store=self.store
        )
