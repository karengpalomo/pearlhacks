from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from backend.entities.entity_base import EntityBase
from backend.models.tag import PlaceTag
from typing import Self

class PlaceTagEntity(EntityBase):
    __tablename__ = 'place_tag'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)

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
    