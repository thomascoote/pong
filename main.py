from tabnanny import check
from turtle import Screen, Turtle
import tkinter as tk
import paddle
from court import Court
from ball import Ball
import time


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
paddle_size = (5,1)
#Left
left_paddle = Turtle()
left_paddle.penup()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(paddle_size[0],paddle_size[1])
left_paddle.goto(-950,0)

#Right
right_paddle = Turtle()
right_paddle.penup()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(paddle_size[0],paddle_size[1])
right_paddle.goto(950,0)

def left_paddle_up():
    left_paddle.goto(left_paddle.xcor(), left_paddle.ycor() + 20)
def left_paddle_down():
    left_paddle.goto(left_paddle.xcor(), left_paddle.ycor() - 20)

def right_paddle_up():
    right_paddle.goto(right_paddle.xcor(), right_paddle.ycor() + 20)
def right_paddle_down():
    right_paddle.goto(right_paddle.xcor(), right_paddle.ycor() - 20)

def hit_right_paddle():
    if ball.ball.distance(right_paddle) < 50 and ball.ball.xcor() > 940:
        ball.ball_hit()
    else:
        pass

def hit_left_paddle():
    if ball.ball.distance(left_paddle) < 30 and ball.ball.xcor() < 960:
        ball.ball_hit()
    else:
        pass

def check_score():
    #If ball passes RIGHT
    if ball.ball.xcor() > 1000:
        court.increase_left_score()
        ball.ball.goto(0,0)

    #If ball passes LEFT
    if ball.ball.xcor() < -1000:
        court.increase_right_score()
        ball.ball.goto(0,0)

def main_loop_ball():
    ball.move_ball()
    ball.ball_bounce()
    hit_right_paddle()
    hit_left_paddle()
    check_score()


"""Ball setup"""
ball = Ball(canvas_width=screen_x, canvas_height=screen_y)

screen.listen()
screen.onkeypress(fun=left_paddle_up, key="w")
screen.onkeypress(fun=left_paddle_down, key="s")
screen.onkeypress(fun=right_paddle_up, key="Up")
screen.onkeypress(fun=right_paddle_down, key="Down")

a = True
while a:
    update = screen.update()
    main_loop_ball()
    screen.ontimer(fun=update,t=5)

"""Click to exit"""
screen.exitonclick()