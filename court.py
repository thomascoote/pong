from turtle import Turtle, Screen


class Court:
    def __init__(self):
        self.screen = Screen()
        self.line = Turtle()
        self.screen_x = 0
        self.screen_y = 0


    def screen_setup(self):
        # Set screen resolution
        self.screen_x = 2000
        self.screen_y = (self.screen_x / 16) * 9

        #Set screen BG Colour
        self.screen.bgcolor("black")

        #Set Screen Title
        self.screen.title("Pong")

        #Initialise the screen
        self.screen.setup(width=self.screen_x, height=self.screen_y)

        #Draw center court line
        self.line.penup()
        self.line.pen(fillcolor="white", pencolor="white", pensize=5)
        self.line.shape("square")
        self.line.goto(0, self.screen_y / 2)
        self.line.setheading(-90)
        #Dotted line
        still_drawing = True
        while still_drawing:
            self.line.pendown()
            self.line.forward(20)
            self.line.penup()
            self.line.forward(20)
            if self.line.ycor() == self.screen_y/2:
                still_drawing = False


