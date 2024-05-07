from sense_hat import SenseHat
import requests
from gps import *
sense = SenseHat()

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

def clicked():
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
        url = 'https://lens-less.azurewebsites.net/data'
        temperature = sense.get_temperature() -15
        myobj = {"latitude": latitude, "longitude":longitude,"temperature":temperature}
        x = requests.post(url, json = myobj)
        if x.status_code == 200:
            response_data = x.json()
            picture_id = response_data.get('pictureId', 'Unknown')
            sense.show_message(str(picture_id))

sense.stick.direction_middle = clicked

while True:
    pass  # This keeps the program running to receive joystick events