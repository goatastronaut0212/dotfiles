import random
from enum import Enum

class Theme(Enum):
    PURPLE = 1
    PINK = 2

def random_theme():
    return random.randint(1,2)

def choose_border(number: int):
    match number:
        case Theme.PURPLE.value:
            return "#784ce1"
        case Theme.PINK.value:
            return "#ed87cc"

def choose_wallpaper(number: int):
    match number:
        case Theme.PURPLE.value:
            return "~/.config/qtile/wallpaper/dots_light_background_2560x1600.jpg"
        case Theme.PINK.value:
            return "~/.config/qtile/wallpaper/pexels-ithalu.jpg"

