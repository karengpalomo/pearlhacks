from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.entities.entity_base import EntityBase

places_tags_entity = Table('places_tags_entity', EntityBase.metadata,
    Column('place_id', Integer, ForeignKey('place.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('place_tag.id'), primary_key=True)
)