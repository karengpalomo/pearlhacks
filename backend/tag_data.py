# Key: our name , value: yelps name
from .models import Tag

tagmap = {
    "Active" : "active", 
    "Artsy" : "arts",
    "Beauty" : "beautysvc", 
    "Quick Snacks" : "food",
    "Restaurants" : "restaurants",
    "Shopping" : "shopping",
    "Nightlife" : "nightlife"
}

def getYelpTags(tags : list[str]):
    yelptags = []

    for tag in tags:
        yelptags.append(tagmap[tag])

    return yelptags