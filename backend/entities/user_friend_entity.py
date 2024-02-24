from sqlalchemy import Integer, Table, Column, ForeignKey
from backend.entities.entity_base import EntityBase

user_friend_table = Table(
    "user_friend_table",
    EntityBase.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('friend_id', ForeignKey('user.id'), primary_key=True)
 )


    