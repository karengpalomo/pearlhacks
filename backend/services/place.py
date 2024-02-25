from typing import Tuple
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User, Tag, Place
from ..entities import UserEntity, TagEntity, PlaceEntity

class PlaceService:
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session
        
    def add_place(self, place: Place):
        place_entity = PlaceEntity.from_model(place)
        self._session.commit()