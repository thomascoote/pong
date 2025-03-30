from turtle import Turtle, Screen
from court import Court
import keyboard

#TODO Screen object 16:9

#TODO Dashed line down middle of screen

#TODO Scoreboard

#TODO Paddles - movement locked to max size Y size of screen, slight offset from back

#TODO Ball

"""Screen setup"""

# screen = Screen()
# screen_x = 2000
# screen_y = (screen_x / 16) * 9
# screen.bgcolor("black")
# screen.title("Pong")
# screen.setup(width=screen_x, height=screen_y)
"""Court line"""

court = Court()

court.screen_setup()

court.screen.exitonclick()