import time
from turtle import Turtle
from ball import Ball


class Paddle:
    def __init__(self, side, canvas_width, canvas_height):
        self.left_right = side
        self.x_size = canvas_width
        self.y_size = canvas_height

        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=6,stretch_len=1)
        self.paddle.pen(fillcolor="white", pencolor="white")
        self.paddle.penup()

        """Debug Drawing"""
        self.debug_drawing = Turtle()
        self.debug_drawing.penup()
        self.debug_drawing.goto(x=-self.x_size, y=self.paddle.ycor())
        self.debug_drawing.pendown()
        self.debug_drawing.goto(x=self.x_size, y=self.paddle.ycor())
        """ """

        #Left or right paddle?
        if self.left_right == "left":
            self.paddle.goto((-canvas_width/2)+10,0)
        if self.left_right == "right":
            self.paddle.goto((canvas_width/2)-20,0)

    def move_up(self):
        new_pos = self.paddle.ycor() + 15
        self.paddle.teleport(self.paddle.xcor(), new_pos)

    def move_down(self):
        y = self.paddle.pos()
        y = (tuple(y)[1])
        self.paddle.sety(y - 20)

