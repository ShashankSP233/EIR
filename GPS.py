#Use to access and record the longitude and latitude of an android device
from geopy.geocoders import Nominatim   #importing geopy modules

geolocator = Nominatim(user_agent='myapplication')

# Get location using IP address
location = geolocator.geocode('')

with open('GPS_Location.txt','w') as f:
    data = [location.latitude, location.longitude]
    f.write(data)