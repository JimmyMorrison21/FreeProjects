from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(200):
    t = i / 5 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)