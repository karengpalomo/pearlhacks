from tkinter import Place
from sqlalchemy import ForeignKey, Integer, String, Time, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.entities.entity_base import EntityBase
from backend.entities.tag_entity import TagEntity
from backend.entities.place_tag_entity import PlaceTagEntity
from backend.models.place import Place
from datetime import time, datetime
from backend.entities.user_favorites_entity import user_favorites_table
from backend.entities.places_tags_entity import places_tags_entity


class PlaceEntity(EntityBase):
    __tablename__ = 'place'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(200))
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    address: Mapped[str] = mapped_column(String(64), nullable=False)
    rating: Mapped[int] = mapped_column(Integer)
    tags: Mapped[list['PlaceTagEntity']] = relationship(secondary=places_tags_entity, back_populates="places")
    users = relationship('UserEntity',
                         secondary=user_favorites_table,
                         back_populates='favorites')

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
            tags=[tag.to_model() for tag in self.tags]
        )
    