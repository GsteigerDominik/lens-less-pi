import time
from enum import Enum

from assets import MAIN, led_brightness, led_population, led_colorscheme, ERROR, LOADING, led_style
from sender import send_request

colorschema_map = {1: "Normal", 2: "BlackAndWhite"}
style_map = {1: "realistic", 2: "futuristic", 3: "vintage", 4: "drawing"}


class State(Enum):
    MAIN = 0  # MAIN PAGE
    BRIGHTNESS = 1  # 0-5
    POPULATION = 2  # 0-5
    COLORSCHEME = 3  # 1=Normal, 2=BlackAndWhite
    STYLE = 4  # 1=realistic,2=futuristic,3=vintage,4=drawing
    RESULT = 5

    def get_right(self):
        member_list = list(self.__class__)
        current_index = member_list.index(self)
        next_index = (current_index + 1) % len(member_list)
        return member_list[next_index]

    def get_left(self):
        member_list = list(self.__class__)
        current_index = member_list.index(self)
        previous_index = (current_index - 1) % len(member_list)
        return member_list[previous_index]


STATE_TO_LED = {State.MAIN: MAIN,
                State.BRIGHTNESS: led_brightness,
                State.POPULATION: led_population,
                State.COLORSCHEME: led_colorscheme,
                State.STYLE: led_style
                }

STATE_TO_VALUE = {State.BRIGHTNESS: 2,
                  State.POPULATION: 2,
                  State.COLORSCHEME: 1,
                  State.STYLE: 1,
                  State.RESULT: 0
                  }
from sense_hat import SenseHat


class Menu:
    def __init__(self):
        self.sense = SenseHat()
        self.current_state = State.MAIN
        self.update_led()
        self.sense.stick.direction_right = self.right
        self.sense.stick.direction_left = self.left
        self.sense.stick.direction_up = self.up
        self.sense.stick.direction_down = self.down
        self.sense.stick.direction_middle = self.middle

    def right(self, event):
        if event.action == 'pressed':
            self.current_state = self.current_state.get_right()
            self.update_led()

    def left(self, event):
        if event.action == 'pressed':
            self.current_state = self.current_state.get_left()
            self.update_led()

    def up(self, event):
        if event.action == 'pressed':
            if self.current_state in [State.POPULATION, State.BRIGHTNESS]:
                STATE_TO_VALUE[self.current_state] = min(STATE_TO_VALUE[self.current_state] + 1, 6)
            elif self.current_state in [State.COLORSCHEME]:
                STATE_TO_VALUE[self.current_state] = min(STATE_TO_VALUE[self.current_state] + 1, 2)
            elif self.current_state in [State.STYLE]:
                STATE_TO_VALUE[self.current_state] = min(STATE_TO_VALUE[self.current_state] + 1, 4)
            else:
                self.show_error()
            self.update_led()

    def down(self, event):
        if event.action == 'pressed':
            if self.current_state in [State.POPULATION, State.BRIGHTNESS]:
                STATE_TO_VALUE[self.current_state] = max(STATE_TO_VALUE[self.current_state] - 1, 0)
            elif self.current_state in [State.COLORSCHEME]:
                STATE_TO_VALUE[self.current_state] = max(STATE_TO_VALUE[self.current_state] - 1, 1)
            elif self.current_state in [State.STYLE]:
                STATE_TO_VALUE[self.current_state] = max(STATE_TO_VALUE[self.current_state] - 1, 1)
            else:
                self.show_error()
            self.update_led()

    def middle(self, event):
        if event.action == 'pressed':
            if self.current_state == State.MAIN:
                self.sense.set_pixels(LOADING)
                picture_id = send_request(self.sense.get_temperature(),
                                          STATE_TO_VALUE[State.BRIGHTNESS],
                                          STATE_TO_VALUE[State.POPULATION],
                                          colorschema_map[STATE_TO_VALUE[State.COLORSCHEME]],
                                          style_map[STATE_TO_VALUE[State.STYLE]]
                                          )
                STATE_TO_VALUE[State.RESULT] = picture_id
            else:
                self.show_error()
            self.current_state = State.RESULT
            self.update_led()

    def update_led(self):
        if self.current_state == State.RESULT:
            self.sense.show_message(str(STATE_TO_VALUE[State.RESULT]))
        elif callable(STATE_TO_LED[self.current_state]):
            self.sense.set_pixels(STATE_TO_LED[self.current_state](STATE_TO_VALUE[self.current_state]))
        else:
            self.sense.set_pixels(STATE_TO_LED[self.current_state])

    def show_error(self):
        self.sense.set_pixels(ERROR)
        time.sleep(1)


menu = Menu()
while True:
    pass  # This keeps the program running to receive joystick events
