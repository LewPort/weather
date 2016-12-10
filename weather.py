#!/usr/bin/env python3

import time
import json
from urllib.request import urlopen
key = '3c06c2fea3463226'

def displayweather(loc):
    url = urlopen('http://api.wunderground.com/api/' + key + '/conditions/q/' + loc + '.json').read().decode('utf8')
    api = json.loads(url)    

    city = api['current_observation']['display_location']['full']
    station = api['current_observation']['observation_location']['city']
    lat = api['current_observation']['observation_location']['latitude']
    long = api['current_observation']['observation_location']['longitude']
    elev = api['current_observation']['observation_location']['elevation']

    lastupdate = api['current_observation']['observation_time']
    ctemp = api['current_observation']['temp_c']
    feelslike = api['current_observation']['feelslike_c']
    humidity = api['current_observation']['relative_humidity']
    desc = api['current_observation']['weather']
    windspeed = api['current_observation']['wind_kph']
    winddir = api['current_observation']['wind_degrees']
    gusts = api['current_observation']['wind_gust_kph']
    pressure = api['current_observation']['pressure_mb']
    visibility = api['current_observation']['visibility_km']

    #Locale
    print('\n%s - %s' % (station, city))
    print('Elevation: %s (Lat: %s Long: %s)' % (elev, lat, long))
    print(lastupdate)

    print('\nDescription: %s' % desc)
    print('Visibility %skm' % visibility)
    
    #Temp
    print('\nTemp: %s°c (Feels like: %s)' % (ctemp, feelslike))
    print('Humidity: ' + humidity)

    #Wind
    print('\nWind is %dkph from %d°' % (windspeed, winddir))
    print('Gusts of %s kph' % gusts)
    print('Pressure: %smb' % pressure)

while True:
    print('Stand By...')
    displayweather('burtonport_donegal')
    print('\nReport Generated: %s' % time.ctime())
    print('Next update in 5 minutes')
    time.sleep(60 * 5)

    




