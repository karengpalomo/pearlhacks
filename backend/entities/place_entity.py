from tkinter import Place
from sqlalchemy import ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.entities.entity_base import EntityBase
from backend.entities.tag_entity import TagEntity
from backend.entities.weekday_time_entity import WeekdayTimeEntity
from backend.models.place import Place
from datetime import time, datetime

from backend.models.weekday_time import WeekdayTime


class PlaceEntity(EntityBase):
    __tablename__ = 'place'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(200))
    longitude: Mapped[float] = mapped_column(float, nullable=False)
    latitude: Mapped[float] = mapped_column(float, nullable=False)
    address: Mapped[str] = mapped_column(String(64), nullable=False)
    rating: Mapped[int] = mapped_column(Integer)
    hours: Mapped[list['WeekdayTimeEntity']] = relationship(back_populates="place", cascade="all, delete-orphan")
    tags: Mapped[list['TagEntity']] = relationship(back_populates="place", cascade="all, delete-orphan")


    @classmethod
    def from_model(cls, model: Place) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            longitude=model.longitude,
            latitude=model.latitude,
            address=model.address,
            rating=model.rating,
            hours=[WeekdayTimeEntity.from_model(hour) for hour in model.hours],
            tags=[TagEntity.from_model(tag) for tag in model.tags]
        )
    
    def to_model(self) -> Place:
        return Place(
            id=self.id,
            name=self.name,
            description=self.description,
            longitude=self.longitude,
            latitude=self.latitude,
            address=self.address,
            rating=self.rating,
            hours=[hour.to_model() for hour in self.hours],
            tags=[tag.to_model() for tag in self.tags]
        )
    