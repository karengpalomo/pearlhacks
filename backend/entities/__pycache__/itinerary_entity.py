from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.models.group import Group
from backend.models.itinerary import Itinerary


class ItineraryEntity(EntityBase):
    __tablename__ = 'itinerary'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(64), nullable=False, default='')
    group: Mapped[Group] = mapped_column(Group, nullable=False)
    activities: Mapped[list['ItineraryEntity']] = mapped_column(secondary=itinerary_activity_table, back_populates='itineraries')

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
            activities = [activity.to_model() for activity in self.activities]
        )
    
    def add_activity(self, activity: ActivityEntity) -> None:
        self.activities.append(activity)
