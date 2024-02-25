'''User accounts for all registered users in the application.'''

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from backend.models.user import User
from backend.entities.entity_base import EntityBase
from backend.entities.user_tag_entity import user_tag_table
from backend.entities.user_friend_entity import user_friend_table
from backend.entities.user_favorites_entity import user_favorites_table


class UserEntity(EntityBase):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(32), unique=True, index=True, nullable=False, default=''
    )
    first_name: Mapped[str] = mapped_column(
        String(64), nullable=False, default='')
    last_name: Mapped[str] = mapped_column(
        String(64), nullable=False, default='')
    password: Mapped[str] = mapped_column(
        String(64), nullable=False, default='')
    occupation: Mapped[str] = mapped_column(
        String(64), nullable=True)
    location: Mapped[str] = mapped_column(
        String(64), nullable=True)
    age: Mapped[int] = mapped_column(
        Integer(), nullable=True)
    bio: Mapped[str] = mapped_column(String(256), nullable=True)
    tags: Mapped[list['TagEntity']] = relationship(secondary=user_tag_table)
    friends = relationship('UserEntity',
                           secondary=user_friend_table,
                           primaryjoin=id == user_friend_table.c.user_id,
                           secondaryjoin=id == user_friend_table.c.friend_id,
                           backref='user_friends')
    favorites = relationship('PlaceEntity',
                             secondary=user_favorites_table,
                             back_populates='users')
    

    @classmethod
    def from_model(cls, model: User) -> Self:
        return cls(
            id=model.id,
            username=model.username,
            email=model.email,
            password=model.password,
            first_name=model.first_name,
            last_name=model.last_name,
            occupation=model.occupation,
            location=model.location,
            age=model.age,
            bio=model.bio,
            tags=[UserEntity.from_model(tag) for tag in model.tags],
            friends=[UserEntity.from_model(friend) for friend in model.friends],
            favorites = [PlaceEntity.from_model(place) for place in model.favorites]
        )

    def to_model(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            occupation=self.occupation,
            location=self.location,
            age=self.age,
            bio=self.bio,
            tags=[tag.to_model() for tag in self.tags],
            friends=[friend.to_model() for friend in self.friends],
            favorites = [place.to_model() for place in self.favorites]
        )


#import entities
from backend.entities.tag_entity import TagEntity
from backend.entities.place_entity import PlaceEntity