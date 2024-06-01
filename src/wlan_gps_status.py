import socket
import time

from gps import *
from sense_hat import SenseHat

sense = SenseHat()
gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


def has_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False


def has_gps():
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        if latitude != "Unknown" and longitude != "Unknown":
            return True

    return False


def display_status():
    if has_internet():
        sense.set_pixel(0, 0, red)

    if has_gps():
        sense.set_pixel(0, 1, blue)


def clear_status():
    sense.set_pixel(0, 0, black)
    sense.set_pixel(0, 1, black)


while True:
    display_status()
    time.sleep(1)
    clear_status()
    time.sleep(1)
