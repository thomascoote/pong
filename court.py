from turtle import Turtle, Screen


class Court:
    def __init__(self, canvas_width, canvas_height):
        self.x_size = canvas_width
        self.y_size = canvas_height
        self.left_scoreboard = Turtle()
        self.right_scoreboard = Turtle()
        self.line = Turtle()
        self.left_score = 0
        self.right_score = 0
        self.scoreboard()


    def screen_setup(self):

        #Draw center court line
        self.line.speed(10)
        self.line.penup()
        self.line.pen(fillcolor="white", pencolor="white", pensize=5)
        self.line.shape("square")
        self.line.hideturtle()
        self.line.goto(0, self.y_size / 2)
        self.line.setheading(-90)
        #Dotted line
        still_drawing = True
        while still_drawing:
            self.line.pendown()
            self.line.forward(20)
            self.line.penup()
            self.line.forward(20)
            if self.line.ycor() <= -self.y_size:
                still_drawing = False

    def scoreboard(self):
        self.left_scoreboard.pen(fillcolor="white",pencolor="white")
        self.left_scoreboard.hideturtle()
        self.left_scoreboard.penup()
        self.left_scoreboard.goto(-60,(self.y_size/2-80))
        self.left_scoreboard.write(self.left_score, font= ("arial", 40, "normal"), align= "center")

        self.right_scoreboard.pen(fillcolor="white",pencolor="white")
        self.right_scoreboard.hideturtle()
        self.right_scoreboard.penup()
        self.right_scoreboard.goto(60,(self.y_size/2-80))
        self.right_scoreboard.write(self.right_score,  font= ("arial", 40, "normal"), align= "center")

    def increase_left_score(self):
        self.left_score += 1
        self.left_scoreboard.clear()
        self.scoreboard()
    def increase_right_score(self):
        self.right_score += 1
        self.right_scoreboard.clear()
        self.scoreboard()