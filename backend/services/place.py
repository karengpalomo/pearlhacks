from typing import Tuple
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Place, PlaceTag
from ..entities import PlaceEntity

class PlaceService:
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session
        
    def add_place(self, place: Place):
        place_entity = PlaceEntity.from_model(place)
        self._session.add(place_entity)
        self._session.commit()
        
    @classmethod
    def to_place_tag_model(tags: list[str]) -> list[PlaceTag]:
        place_tags = [PlaceTag(name=tag) for tag in tags]
        return place_tags

    @classmethod
    def to_place_model(self, businesses) -> list[Place]:
        places = []
        for business in businesses:
            name = business["name"]
            longitude = business["coordinates"]["longitude"]
            latitude = business["coordinates"]["latitude"]
            address = business["location"]["address1"]
            rating = business["rating"]
            categories = business["categories"]
            place_tags_str = [category["alias"] for category in categories]
            place_tags = self.to_place_tag_model(place_tags_str)
            photo_url = business["image_url"]
            place = Place(name=name, longitude=longitude, latitude=latitude, address=address, rating=rating, tags=place_tags, photo_url=photo_url)
            places.append(place)
        return places