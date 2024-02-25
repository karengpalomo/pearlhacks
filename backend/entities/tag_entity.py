from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.entities.entity_base import EntityBase
from backend.models.tag import Tag
from typing import Self


class TagEntity(EntityBase):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)

    @classmethod
    def from_model(cls, model: Tag) -> Self:
        return cls(
            id=model.id,
            name=model.name
        )

    def to_model(self) -> Tag:
        return Tag(
            id=self.id,
            name=self.name
        )
    