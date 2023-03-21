# from urllib.request import urlopen
# import json



# # open following url to get ipaddress
# urlopen("http://ipinfo.io/json")

# # load data into array
# data = json.load(urlopen("http://ipinfo.io/json"))

# # extract lattitude
# lat = data['loc'].split(',')[0]

# # extract longitude
# lon = data['loc'].split(',')[1]
# city= data['city']

# print(lat, lon,city)
import gpsd

# Connect to the local GPS daemon
gpsd.connect()

# Get the current location
packet = gpsd.get_current()
lat, lng = packet.position()

print(f"Latitude: {lat}, Longitude: {lng}")