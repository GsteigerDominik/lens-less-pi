from sense_hat import SenseHat
import socket
import time

# Initialize the Sense HAT
sense = SenseHat()

# Define WLAN icon (7x7 pixel array)
#wlan_icon = [
#(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(255,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(255,0,0),(255,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(255,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(255,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
#(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)
#]
red = (255, 0, 0)
blue = (0, 0, 255)



def has_internet():
    try:
        # Try connecting to a known external IP (8.8.8.8) to check internet connectivity
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False

def has_gps():
    return True

def display_status():
    if has_internet():
        # Display WLAN icon on the Sense HAT
        sense.set_pixel(0, 0, red)

    if has_gps():
        sense.set_pixel(0, 1, blue)


# Run the main loop to continuously check and display internet status
while True:
    display_status()
    time.sleep(1)
    sense.clear()
    time.sleep(1)
