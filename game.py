import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_EXIT  # Keybinds
import random
import time


class snake:
    def __init__(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass


class food:
    def __init__(self, max_x=25, max_y=60, char="█", coordinates=[20, 20]):
        """ """
        self.char = char
        self.coordinates = coordinates

    def regenerate():
        """Regenerates the food coordinates"""
        self.coordinates = [random.randint(0,self.max_x),random.randint(0,self.maxy)]


def game_loop():
    # Window initialization
    main = curses.initscr()
    height, width = main.getmaxyx()  # Gets the max window size
    window = curses.newwin(height, width, 0, 0)  # Creates a mew window drawn max x and y size from the top left
    curses.noecho()  # Turns off key echoing
    curses.curs_set(0)  # Hides Cursor
    main.border(0)  # Adds a boarder to window
    main.nodelay(1)

    a = food()

    # Actual Game Loop
    while(True):  # TODO: Make game run while not esc pressed or game over
        main.refresh()
        window.addch(a.coordinates[0], a.coordinates[1], a.char) 
        a.regenerate()
        time.sleep(1)

if __name__ == "__main__":
    game_loop()
