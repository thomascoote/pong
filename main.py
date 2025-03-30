from logging.config import listen
from turtle import Turtle, Screen
from court import Court
from paddle import Paddle
import time

import keyboard


#TODO Scoreboard

#TODO Paddles - movement locked to max size Y size of screen, slight offset from back

#TODO Ball

"""Screen setup"""

screen = Screen()
screen_x = 2000
screen_y = (screen_x / 16) * 9
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(width=screen_x, height=screen_y)

"""Court line"""
court = Court(canvas_width=screen_x,canvas_height=screen_y)
court.screen_setup()

"""Paddle setup"""
left_paddle = Paddle(side= "left", canvas_width=screen_x, canvas_height=screen_y)
right_paddle = Paddle(side= "right", canvas_width=screen_x, canvas_height=screen_y)

"""Define hotkeys"""

# keyboard.add_hotkey("w", lambda: left_paddle.move_up())
# keyboard.add_hotkey("s", lambda: left_paddle.move_down())

screen.tracer(1)
playing = True
while playing:
    time.sleep(0.1)
    if keyboard.is_pressed("w"):
        left_paddle.move_up()
    if keyboard.is_pressed("s"):
        left_paddle.move_down()


"""Click to exit"""
screen.exitonclick()