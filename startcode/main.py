import turtle
from boom import Boom

pen = turtle.Turtle()
pen.speed(0)
pen.setheading(90)
pen.width(3)

boom = Boom(pen)
boom.teken()

pen.hideturtle()
turtle.done()