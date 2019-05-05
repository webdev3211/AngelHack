from googleplaces import GooglePlaces, types, lang
import requests
import json

# send_url = 'http://freegeoip.net/json'
# r = requests.get(send_url)
# j = json.loads(r.text)
# lat = j['latitude']
# lon = j['longitude']
API_KEY = 'AIzaSyArWLYsjxyxIDjybWoWJ-ZGcDQPulG3aRU'

google_places = GooglePlaces(API_KEY)

# query_result = google_places.nearby_search(
#     location='London', keyword='Restaurants',
#     radius=1000, types=[types.TYPE_RESTAURANT])

query_result = google_places.nearby_search(
        #lat_lng={'lat': 46.1667, 'lng': -1.15},
        lat_lng={'lat': 28.4089, 'lng': 77.3178},
        radius=5000,
        types=[types.TYPE_HOSPITAL] or [types.TYPE_CAFE] or [type.TYPE_BAR] or [type.TYPE_CASINO])

if query_result.has_attributions:
    print (query_result.html_attributions)


for place in query_result.places:
    #place.get_details()
    print (place) 