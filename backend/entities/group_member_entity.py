from sqlalchemy import Integer, Table, Column, ForeignKey
from backend.entities.entity_base import EntityBase

group_member_table = Table(
    "group_member_table",
    EntityBase.metadata,
    Column('group_id', ForeignKey('group.id'), primary_key=True),
    Column('member_id', ForeignKey('user.id'), primary_key=True)
 )


    