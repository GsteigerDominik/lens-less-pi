r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
e = (0, 0, 0)
y = (255, 255, 0)
w = (255, 255, 255)
br = (66, 40, 14)
gr = (102, 102, 102)
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
MAIN = [
    e, e, e, e, e, e, e, e,
    e, b, b, b, b, b, b, e,
    e, b, e, e, e, g, b, e,
    r, b, e, b, b, e, b, r,
    r, b, e, b, b, e, b, r,
    e, b, e, e, e, e, b, e,
    e, b, b, b, b, b, b, e,
    e, e, e, e, e, e, e, e
]

ERROR = [
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r
]

LOADING = [
    e, e, b, b, b, b, e, e,
    e, b, e, r, e, e, b, e,
    b, e, e, r, e, r, e, b,
    b, e, e, r, r, e, e, b,
    b, e, e, r, e, e, e, b,
    b, e, e, e, e, e, e, b,
    e, b, e, e, e, e, b, e,
    e, e, b, b, b, b, e, e
]


def x(idx, current_nr, color):
    if idx <= current_nr:
        return color
    return e


def led_brightness(i):
    return [
        e, e, e, e, e, e, e, e,
        e, e, e, y, y, e, e, e,
        e, e, e, g, g, e, e, e,
        r, e, e, g, g, e, e, r,
        r, e, e, g, g, e, e, r,
        b, b, b, b, b, b, b, b,
        b, x(1, i, y), x(2, i, y), x(3, i, y), x(4, i, y), x(5, i, y), x(6, i, y), b,
        b, b, b, b, b, b, b, b
    ]


def led_style(i):  # 1=realistic,2=futuristic,3=vintage,4=drawing
    if i == 1:
        return [
            e, e, e, e, e, e, e, e,
            e, e, b, b, b, b, e, e,
            e, e, b, e, e, b, e, e,
            r, e, b, b, b, b, e, r,
            r, e, b, b, e, e, e, r,
            e, e, b, e, b, e, e, e,
            e, e, b, e, e, b, e, e,
            e, e, e, e, e, e, e, e
        ]
    if i == 2:
        return [
            e, e, e, e, e, e, e, e,
            e, e, b, b, b, b, e, e,
            e, e, b, e, e, e, e, e,
            r, e, b, b, b, b, e, r,
            r, e, b, e, e, e, e, r,
            e, e, b, e, e, e, e, e,
            e, e, b, e, e, e, e, e,
            e, e, e, e, e, e, e, e
        ]
    if i == 3:
        return [
            e, e, e, e, e, e, e, e,
            e, b, e, e, e, e, b, e,
            e, b, e, e, e, e, b, e,
            r, e, b, e, e, b, e, r,
            r, e, b, e, e, b, e, r,
            e, e, e, b, b, e, e, e,
            e, e, e, b, b, e, e, e,
            e, e, e, e, e, e, e, e
        ]
    if i == 4:
        return [
            e, e, e, e, e, e, e, e,
            e, e, b, b, b, e, e, e,
            e, e, b, e, e, b, e, e,
            r, e, b, e, e, b, e, r,
            r, e, b, e, e, b, e, r,
            e, e, b, e, e, b, e, e,
            e, e, b, b, b, e, e, e,
            e, e, e, e, e, e, e, e
        ]


def led_population(i):
    return [
        e, e, e, e, e, e, e, e,
        e, e, e, e, y, e, e, e,
        e, e, e, g, g, g, e, e,
        r, e, e, e, w, e, e, r,
        r, e, e, w, e, w, e, r,
        b, b, b, b, b, b, b, b,
        b, x(1, i, y), x(2, i, y), x(3, i, y), x(4, i, y), x(5, i, y), x(6, i, y), b,
        b, b, b, b, b, b, b, b
    ]


def led_colorscheme(i):
    if i == 1:
        return [
            e, e, e, e, e, e, e, e,
            e, e, e, g, g, e, e, e,
            e, e, g, g, g, g, e, e,
            r, e, g, br, br, g, e, r,
            r, e, e, br, br, e, e, r,
            e, e, e, br, br, e, e, e,
            e, e, e, br, br, e, e, e,
            e, e, e, e, e, e, e, e
        ]
    elif i == 2:
        return [
            e, e, e, e, e, e, e, e,
            e, e, e, w, w, e, e, e,
            e, e, w, w, w, w, e, e,
            r, e, w, gr, gr, w, e, r,
            r, e, e, gr, gr, e, e, r,
            e, e, e, gr, gr, e, e, e,
            e, e, e, gr, gr, e, e, e,
            e, e, e, e, e, e, e, e
        ]
