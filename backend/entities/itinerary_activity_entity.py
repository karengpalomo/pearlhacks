from sqlalchemy import Table, Column, ForeignKey
from backend.entities.entity_base import EntityBase

itinerary_activity_table = Table(
    "itinerary_activity_table",
    EntityBase.metadata,
    Column('itinerary_id', ForeignKey('itinerary.id'), primary_key=True),
    Column('activity_id', ForeignKey('activity.id'), primary_key=True)
 )


    