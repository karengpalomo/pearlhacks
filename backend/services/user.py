from typing import Tuple
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User, Tag, Place
from ..entities import UserEntity, TagEntity, PlaceEntity
from ..tag_data import getYelpTags
from .user_helper import *
from ..api.yelp import *
from place import PlaceService


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
    
    def filter_by_availability(self, business_ids, yelp_day: int, time_of_day: str) -> list[Place]:
        # Define the time ranges for each part of the day
        filtered_businesses = []
        time_ranges = {
            "Morning": ("0600", "1200"),
            "Afternoon": ("1200", "1700"),
            "Evening": ("1700", "2100"),
            "Night": ("2100", "0600"),
        }
        
        businesses = business_details_search(ids=business_ids)
        for business in businesses:
            open_hours_on_yelp_day = business["hours"]["open"][yelp_day]
            start, end = open_hours_on_yelp_day["start"], open_hours_on_yelp_day["end"]
            start_time, end_time = time_ranges[time_of_day]
            if start_time < end and end_time > start:
                    filtered_businesses.append(business)
        return to_place_model(filtered_businesses)
            
            
    def filter(self, tags, distance, prices, availability) -> list[Place]:
        params = {}
        yelp_categories = getYelpTags(tags=tags)
        params["categories"] = yelp_categories
        if distance:
            distance_meters = to_meters(distance)
            params["radius"] = distance_meters
        if prices:
            yelp_prices = get_yelp_prices(prices)
            params["price"] = yelp_prices
        businesses = business_search(params=params)
        if availability:
            business_ids = get_business_ids(businesses=businesses)
            date, time_of_day = availability
            weekday = to_yelp_weekday(date=date)
            return self.filter_by_availability(business_ids=business_ids, yelp_day=weekday, time_of_day=time_of_day)
        else:
            return to_place_model(businesses["businesses"])
    
    def add_friend(self, user_id: int, friend_id: int):
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        friend = self._session.query(UserEntity).filter(UserEntity.id == friend_id).first()
        if not user or not friend:
            return None  # Either user or friend doesn't exist
        if friend not in user.friends:
            user.friends.append(friend)
            self._session.commit()
        return user
    
    def remove_friend(self, user_id: int, friend_id: int):
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        friend = self._session.query(UserEntity).filter(UserEntity.id == friend_id).first()
        if not user or not friend:
            return None  # Either user or friend doesn't exist
        if friend in user.friends:
            user.friends.remove(friend)
            self._session.commit()
        return user
    
    def get_friends(self, user_id: int):
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        if not user:
            return None  # User doesn't exist
        return user.friends
    
    def edit_profile(self, user_id: int, bio: str = None, tags: list = None, location: str = None):
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        if not user:
            return None  # User doesn't exist
        if bio is not None:
            user.bio = bio
        if location is not None:
            user.location = location
        if tags is not None:
            all_tags = {tag.name: tag for tag in self._session.query(TagEntity).all()}
            tags_to_add = [all_tags[tag_name] for tag_name in tags if tag_name in all_tags]
            user.tags = tags_to_add
        self._session.commit()
        return user
    
    def get_friends(self, user_id) -> list[User]:
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        if not user:
            return None  # User doesn't exist
        return user.friends

    def get_user_by_username(self, username: str):
        return self._session.query(UserEntity).filter(UserEntity.username == username).first()

    def add_favorite(self, user_id: int, place: Place):
        place_entity = self._service.query(PlaceEntity).filter(PlaceEntity.name == place.name, PlaceEntity.location == place.location).first()
        if not place_entity:
            place_svc = PlaceService()
            place_svc.add_place(place)
            
        user = self._session.query(UserEntity).filter(UserEntity.id == user_id).first()
        if not user:
            raise Exception("User not found")
        
        if place not in user.favorites:
            user.favorites.append(place)
            self._session.commit()
