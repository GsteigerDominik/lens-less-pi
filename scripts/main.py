r = (255, 0, 0)
g = (0, 255, 0)
e = (0, 0, 0)

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


from sense_hat import SenseHat
sense = SenseHat()
sense.set_pixels(logo)