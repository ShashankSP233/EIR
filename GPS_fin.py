import requests

url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY'
headers = {'content-type': 'application/json'}
data = {'considerIp': 'true'}

response = requests.post(url, json=data, headers=headers)
location = response.json()['location']
lat, lng = location['lat'], location['lng']

f= open("GPS_Location.txt","w")
data = [lat,lng]
f.write(data)