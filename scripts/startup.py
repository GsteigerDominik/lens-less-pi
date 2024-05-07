import os
import socket
import time

from sense_hat import SenseHat

sense = SenseHat()
red = (255, 0, 0)


def has_internet():
    try:
        # Try connecting to a known external IP (8.8.8.8) to check internet connectivity
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False


while True:
    if has_internet():
        os.system('rm -rf repository-name')
        os.system('git clone https://github.com/username/repository-name')
    else:
        sense.clear()
        time.sleep(1)
        sense.set_pixel(0, 0, red)
        time.sleep(1)
