import random

current_theme = random.randint(1,3)

def chooseBorder(themeNumber: int):
    match themeNumber:
        case Theme.PURPLE:
            return "#784ce1"
       case Theme.PINK:
           return "#ed87cc"
       case _:
           return "oi ban oi"
