from turtle import *

bgcolor("black")
speed(0)
hideturtle()

for i in range(250):
    color("red")
    circle(i)
    color("yellow")
    circle(i * 0.5)
    right(3)
    forward(3)
done()
