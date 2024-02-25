from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.entities.entity_base import EntityBase
from backend.models.itinerary import Itinerary
from backend.entities.group_member_entity import group_member_table
from backend.models.group import Group
from backend.entities.activity_entity import ActivityEntity
from backend.entities.itinerary_activity_entity import itinerary_activity_table
from typing import Self



class Itinerary(EntityBase):
    __tablename__ = 'itinerary_table'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    group: Mapped[Group] = mapped_column(Group)
    activities = relationship('ActivityEntity',
                           secondary=itinerary_activity_table,
                           primaryjoin=id == group_member_table.c.group_id,
                           secondaryjoin=id == group_member_table.c.user_id,
                           backref='group_members')

    @classmethod
    def from_model(cls, model: Itinerary) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            group=model.group,
            activities=[ActivityEntity.from_model(activity) for activity in model.activities]
        )

    def to_model(self) -> Itinerary:
        return Itinerary(
            id=self.id,
            name=self.name,
            group=self.group,
            activities=[activity.to_model() for activity in self.activities]
        )
    