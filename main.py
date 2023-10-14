from turtle import Turtle, exitonclick, Screen
from random import randint, choice

pen = Turtle()


def move_forward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def move_ccw():
    pen.setheading(pen.heading() + 10)

def move_cw():
    pen.setheading(pen.heading() - 10)

def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen = Screen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_ccw, "a")
screen.onkey(move_cw, "d")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
