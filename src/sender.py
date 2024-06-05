import requests
from gps import *

gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)


def send_request(temperature, brightness, population, colorscheme, style):
    nx = {}
    for i in range(0, 50):
        latitude = 0
        longitude = 0
        nx = gpsd.next()
        if nx['class'] == 'TPV':
            latitude = getattr(nx, 'lat', 0)
            longitude = getattr(nx, 'lon', 0)
            if latitude != 0 and longitude != 0:
                break
    url = 'https://lens-less.azurewebsites.net/data'
    temperature = temperature - 15
    myobj = {
        "latitude": latitude,
        "longitude": longitude,
        "temperature": temperature,
        "brightness": brightness,
        "population": population,
        "colorscheme": colorscheme,
        "style": style
    }
    x = requests.post(url, json=myobj)
    if x.status_code == 200:
        response_data = x.json()
        picture_id = response_data.get('pictureId', 'Unknown')
        return picture_id
