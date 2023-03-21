#Use to access and record the longitude and latitude of an android device

import android  #importing android library

droid = android.Android()

class MyLocationListener(object):
    def __init__(self):
        self.location = None

    def onLocationChanged(self, location):
        self.location = location

location_listener = MyLocationListener()

droid.startLocating()
droid.eventRegisterForBroadcast("android.location.PROVIDERS_CHANGED")
droid.eventRegisterForBroadcast("android.intent.action.AIRPLANE_MODE")

try:
    while True:
        if location_listener.location is not None:
            latitude = location_listener.location.getLatitude() #to get the Latitude
            longitude = location_listener.location.getLongitude()   #to get Longitude
            gps_file = open('GPS_Location.txt', 'a')    #creating a text file
            gps_list = []
            gps_list.append([latitude,longitude])   #entering the latitude and longitude
            break
        droid.eventWaitFor("location", 10000)   #will record the location for 10sec
except KeyboardInterrupt:
    pass
finally:
    droid.stopLocating()
    droid.eventUnregisterForBroadcast("android.location.PROVIDERS_CHANGED")
    droid.eventUnregisterForBroadcast("android.intent.action.AIRPLANE_MODE")
    gps_file.close()
