from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.models.store import Store


class StoreEntity(EntityBase):
    __tablename__ = 'store'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(64), nullable=False, default='')
    description: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(64))
    distance: Mapped[str] = mapped_column(String(64))
    rating: Mapped[int] = mapped_column(Integer)
    tags: Mapped[list['tag']] = mapped_column(secondary=store_tags_table)


    @classmethod
    def from_model(cls, model: Itinerary) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            address=model.address,
            distance=model.distance,
            rating=model.rating,
            tags=[TagEntity.from_model(tag) for tag in model.tags]
        )

    def to_model(self) -> Itinerary:
        return Store(
            id=self.id,
            name=self.name,
            description=self.description,
            address=self.address,
            distance=self.distance,
            rating=self.rating,
            tags=[tag.to_model() for tag in self.tags]
        )