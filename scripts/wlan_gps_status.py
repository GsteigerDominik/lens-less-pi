from sense_hat import SenseHat
import socket
import time
from gps import *

# Initialize the Sense HAT
sense = SenseHat()
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

def has_internet():
    try:
        # Try connecting to a known external IP (8.8.8.8) to check internet connectivity
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False

def has_gps():
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        if latitude != "Unknown" and longitude != "Unknown":
            return True

    return False

def display_status():
    if has_internet():
        # Display WLAN icon on the Sense HAT
        sense.set_pixel(0, 0, red)

    if has_gps():
        sense.set_pixel(0, 1, blue)

def clear_status():
    sense.set_pixel(0, 0, black)
    sense.set_pixel(0, 1, black)

# Run the main loop to continuously check and display internet status
while True:
    display_status()
    time.sleep(1)
    clear_status()
    time.sleep(1)
