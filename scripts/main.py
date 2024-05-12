r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
e = (0, 0, 0)
y = (255,255,0)

logo = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    r, g, g, g, g, r, e, e,
    r, e, e, e, e, r, e, e,
    r, e, g, g, e, r, e, e,
    r, e, e, e, e, r, e, e,
    r, r, r, g, g, r, r, r,
    e, e, e, e, e, e, e, e
]
camera = [
    e, e, e, e, e, e, e, e,
    e, b, b, b, b, b, b, e,
    e, b, e, e, e, g, b, e,
    r, b, e, b, b, e, b, r,
    r, b, e, b, b, e, b, r,
    e, b, e, e, e, e, b, e,
    e, b, b, b, b, b, b, e,
    e, e, e, e, e, e, e, e
]

brightness = [
    e, e, e, e, e, e, e, e,
    e, e, e, y, y, e, e, e,
    e, e, e, g, g, e, e, e,
    r, e, e, g, g, e, e, r,
    r, e, e, g, g, e, e, r,
    b, b, b, b, b, b, b, b,
    b, y, y, e, e, e, e, b,
    b, b, b, b, b, b, b, b
]




from sense_hat import SenseHat
import time



sense = SenseHat()
sense.set_pixels(logo)
time.sleep(3)
sense.set_pixels(camera)

def right():
    sense.set_pixels(brightness)

sense.stick.direction_right = right


while True:
    pass  # This keeps the program running to receive joystick events