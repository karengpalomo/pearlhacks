from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base

user_favorites_table = Table('user_favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('place_id', Integer, ForeignKey('place.id'), primary_key=True)
)
