from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Alexnake Game")
segments = []
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]

for position in starting_positions :
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

is_game_on = True

while is_game_on :
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(len(segments)-1, 0, -1) :
        x = segments[seg_num-1].xcor()
        y = segments[seg_num-1].ycor()
        segments[seg_num].goto(x,y)
    
    segments[0].forward(20)
    segments[0].right(70)

screen = Screen()
screen.exitonclick()