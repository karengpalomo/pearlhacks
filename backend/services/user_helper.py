from ..models.place import Place
from ..models.place_tag import PlaceTag
import math
from datetime import datetime

DATE_FORMAT = "%B %d, %Y"

def get_business_ids(yelp_places) -> list[str]:
    businesses = yelp_places["businesses"]
    ids = [business["id"] for business in businesses]
    return ids
    

def to_meters(miles: int) -> int:
    return math.floor(miles * 1609.34)

def get_yelp_prices(prices: list[str]) -> list[int]:
    price_levels = []
    for price in prices:
        if price == "$":
            price_levels += 1
        elif price == "$$":
            price_levels += 2
        elif price == "$$$":
            price_levels += 3
        elif price == "$$$$":
            price_levels += 4
            
def date_to_weekday(date: str) -> str:
    date_object = datetime.strptime(date, DATE_FORMAT)
    weekday = date_object.strftime("%A")
    return weekday
            
def to_yelp_weekday(date: str) -> int:
    weekday = date_to_weekday(date)
    if weekday == "Sunday":
        return 0
    elif weekday == "Monday":
        return 1
    elif weekday == "Tuesday":
        return 2
    elif weekday == "Wednesday":
        return 3
    elif weekday == "Thursday":
        return 4
    elif weekday == "Friday":
        return 5
    elif weekday == "Saturday":
        return 6

    
        
        
        
        
        

    