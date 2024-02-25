from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.entities.entity_base import EntityBase
from backend.entities.user_entity import UserEntity
from backend.models.tag import Tag
from backend.entities.group_member_entity import group_member_table
from typing import Self



class GroupEntity(EntityBase):
    __tablename__ = 'group'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    members = relationship('UserEntity',
                           secondary=group_member_table,
                           primaryjoin=id == group_member_table.c.group_id,
                           secondaryjoin=id == group_member_table.c.member_id,
                           backref='group_members')

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
    