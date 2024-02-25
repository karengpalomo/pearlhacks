from typing import Tuple
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User, Tag, Place
from ..entities import UserEntity
from ..tag_data import getYelpTags
from .user_helper import *
from ..api.yelp import *


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
        
        