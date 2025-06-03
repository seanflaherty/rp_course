# `@timer` which times and displays how long each frame takes
# `@frame_rate(25)` which ensures that no frame lasts less than the required time
# Apply both of these to whatever function

import random
import turtle
import time

WIDTH, HEIGHT = 600, 600
screen = turtle.Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")

def draw_frame(all_turtles, speed):
    for a_turtle in all_turtles:
        a_turtle.forward(speed)
        a_turtle.left(random.uniform(-10, 10))
    screen.update()

    