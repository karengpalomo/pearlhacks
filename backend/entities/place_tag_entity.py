from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.entities.entity_base import EntityBase
from backend.models.place_tag import PlaceTag
from typing import Self
from backend.entities.places_tags_entity import places_tags_entity

class PlaceTagEntity(EntityBase):
    __tablename__ = 'place_tag'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    places = relationship('PlaceEntity',
                          secondary=places_tags_entity,
                          back_populates='tags')

    @classmethod
    def from_model(cls, model: PlaceTag) -> Self:
        return cls(
            id=model.id,
            name=model.name
        )

    def to_model(self) -> PlaceTag:
        return PlaceTag(
            id=self.id,
            name=self.name
        )
    