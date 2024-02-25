from typing import Tuple
from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Place, PlaceTag
from ..entities.group_entity import GroupEntity
from ..entities.user_entity import UserEntity
from ..entities.group_member_entity import group_member_table

class GroupService:
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session
    
    def view_members(self, group_id: int):
        # Using the relationship to directly access members
        group = self._session.query(GroupEntity).filter(GroupEntity.id == group_id).first()
        if not group:
            return None  # Or raise an exception as per your error handling strategy
        return group.members  # This will give you the list of UserEntity instances

    def create_group(self, group_name: str):
        new_group = GroupEntity(name=group_name)
        self._session.add(new_group)
        self._session.commit()
        return new_group

    def add_member(self, group_id: int, user_id: int):
        # Directly insert into the association table
        stmt = insert(group_member_table).values(group_id=group_id, user_id=user_id)
        self._session.execute(stmt)
        self._session.commit()

    def view_user_groups(self, user_id: int):
        # Utilize the backref from UserEntity to find all groups a user belongs to
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        if not user:
            return None  # Or raise an exception as per your error handling strategy
        return user.group_members  # Assuming 'group_members' is the backref in UserEntity