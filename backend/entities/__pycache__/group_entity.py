from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.models.group import Group


class GroupEntity(EntityBase):
    __tablename__ = 'group'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(64), nullable=False, default='')
    members: Mapped[list['UserEntity']] = relationship(secondary=user_group_table, back_populates="groups")


    @classmethod
    def from_model(cls, model: Group) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            members=[UserEntity.from_model(member) for member in model.members]
        )

    def to_model(self) -> Group:
        return Group(
            id=self.id,
            name=self.name,
            members = [member.to_model() for member in self.members]
        )
    
    def add_member(self, user: UserEntity) -> None:
        self.members.append(user)
