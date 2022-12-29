# 1. Move the turtle with keypress

from turtle import Turtle

# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280

class Player(Turtle) :
    def __init__(self,position) :
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.color("black")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.move_speed = 0.1
        self.goto(position)


    def move(self) :
        new_y = self.ycor() + 10
        self.goto(0,new_y)
    
