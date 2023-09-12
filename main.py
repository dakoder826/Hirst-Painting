from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
screen.colormode(255)
dot_distance = 67
turn = 0
timmy.penup()

color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148,
93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93)]


def go_to_position():
    timmy.penup()
    timmy.setpos(-300, -220)

def go_left():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(65)

def go_right():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(360)
    timmy.forward(65)

go_to_position()


for i in range(100):
    random_color = random.choice(color_list)
    timmy.dot(20, random_color)
    timmy.forward(65)
    i += 1

    if i % 20 == 0:
        go_right()
    elif i % 10 == 0:
        go_left()


screen.exitonclick()



