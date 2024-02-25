# Hard code our version of the yelp category here (similar to image)
from ..models import tag

# Active Life (active, All), Arts & Entertainment (arts, All), Beauty & Spas (beautysvc, All), Food (food, All)
# Hotels & Travel (hotelstravel, All), Restaurants (restaurants, All), Shopping (shopping, All), 
# Nightlife (nightlife, All)

tag1 = tag(id=1, name="Active")
tag2 = tag(id=2, name="Artsy")
tag3 = tag(id=3, name="Beauty & Relaxation")
tag4 = tag(id=4, name="Quick Snacks")
tag5 = tag(id=5, name="Nightlife")
tag6 = tag(id=6, name="Restaurants")
tag7 = tag(id=7, name="Shopping")