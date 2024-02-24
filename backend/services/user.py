from typing import Tuple
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User
from ..entities import UserEntity


class UserService:
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def create_user(self, username: str, email: str, password: str, first_name: str, last_name: str) -> None:
        new_user = User(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        new_user_entity = UserEntity.from_model(new_user)
        self._session.add(new_user_entity)
        self._session.commit()
    
    def login(self, username: str, password: str) -> User:
        query = select(UserEntity).where(UserEntity.username == username)
        user = self._session.scalar(query)
        if not user:
            raise Exception("Username does not exists.")
        if user.password != password:
           raise Exception("Password is incorrect.") 
        return user
    