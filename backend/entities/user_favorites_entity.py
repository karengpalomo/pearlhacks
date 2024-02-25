from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.entities.entity_base import EntityBase

user_favorites_table = Table('user_favorites', EntityBase.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('place_id', Integer, ForeignKey('place.id'), primary_key=True)
)
