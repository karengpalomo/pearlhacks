from ..models.place import Place

def to_place_model(yelp_places) -> list[Place]:
    places = []
    businesses = yelp_places["businesses"]
    for business in businesses:
        name = business["name"]
        longitude = business["coordinates"]["longitude"]
        latitude = business["coordinates"]["latitude"]
        address = business["location"]["address1"]
        rating = business["rating"]
        categories = business["category"]
        tags = []
        for category in categories:
            tags.append(category["alias"])
        place = Place(name=name, longitude=longitude, latitude=latitude, address=address, rating=rating, tags=tags)
        places.append(place)
    return places
        
        
        

    