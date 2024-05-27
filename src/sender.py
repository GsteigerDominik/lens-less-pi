import requests
from gps import *

gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)


def send_request(temperature, brightness, population, colorscheme,style):
    nx={}
    for i in range(0,10):
        nx = gpsd.next()
        if nx['class'] == 'TPV':
            break
    latitude = getattr(nx, 'lat', "Unknown")
    longitude = getattr(nx, 'lon', "Unknown")
    print("current position",latitude,longitude)
    url = 'https://lens-less.azurewebsites.net/data'
    temperature = temperature - 15
    myobj = {
            "latitude": latitude,
            "longitude": longitude,
            "temperature": temperature,
            "brightness": brightness,
            "population": population,
            "colorscheme": colorscheme,
            "style":style
        }
    x = requests.post(url, json=myobj)
    if x.status_code == 200:
        response_data = x.json()
        picture_id = response_data.get('pictureId', 'Unknown')
        return picture_id
