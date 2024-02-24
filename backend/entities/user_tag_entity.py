from sqlalchemy import Integer, Table, Column, ForeignKey
from backend.entities.entity_base import EntityBase

user_tag_table = Table(
    "user_tag_table",
    EntityBase.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True)
 )


    