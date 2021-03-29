import turtle
import time


def draw_shape(turtle, radius, sides):
    turtle.penup()
    turtle.sety(-radius)
    turtle.pendown()
    turtle.circle(radius, steps=sides)

shapes = [(20, 3), (40, 4), (60, 5),(80, 6), (100, 7), (120, 8),(140, 9), (160, 10), (180,11),(200,12)]

for shape in shapes:
    draw_shape(turtle, *shape)
time.sleep(5)
    
