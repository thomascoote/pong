from turtle import Turtle
import time
class Ball:
    def __init__(self, canvas_width, canvas_height):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.pen(fillcolor="white",pencolor="white",pensize=10)
        self.ball.penup()
        self.x_size = canvas_width
        self.y_size = canvas_height
        self.ball.goto(0,0)
        self.x_move = 5
        self.y_move = 5
        self.ball.setheading(45)

    def move_ball(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def ball_bounce(self):
        if self.ball.ycor() >= (self.y_size /2)-20 and self.ball.ycor() > 0:
            self.y_move *= -1
            self.ball.forward(self.y_move)

        if self.ball.ycor() <= (-self.y_size /2)+20 and self.ball.ycor() < 0:
            self.y_move *= -1
            self.ball.forward(self.y_move)

    def ball_hit(self):
        self.x_move *= -1
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)