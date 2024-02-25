from tkinter import Place
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.entities.entity_base import EntityBase
from backend.entities.user_entity import UserEntity
from backend.models.tag import Tag
from backend.entities.group_member_entity import group_member_table
from typing import Self
import datetime



class ActivityEntity(EntityBase):
    __tablename__ = 'activity_table'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(datetime.time)
    start_time: Mapped[datetime.time] = mapped_column(datetime.time)
    end_time: Mapped[datetime.time] = mapped_column(datetime.time)
    place: Mapped[Place] = mapped_column(Place)

    @classmethod
    def from_model(cls, model: Tag) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            members=[UserEntity.from_model(member) for member in model.members]
        )

    def to_model(self) -> Tag:
        return Tag(
            id=self.id,
            name=self.name,
            members=[member.to_model() for member in self.members]
        )
    