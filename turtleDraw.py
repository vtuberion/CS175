# CS175L-50
# Vincent Tuberion
# turtleDraw.py
# Last Modified 2/14/2022 18:43 EST

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 6
NUM_SIDES = 8
LENGTH = 100
ANGLE = 360/NUM_SIDES
TEXT_X = -5
TEXT_Y = -10

# Size the window.
screen = turtle.getscreen()
screen.bgcolor("#FF0000")
#screen = turtle.getscreen()
#screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0)
#screen.bgcolor("black")
print("Hey look, the screen should work")
# turtle.screensize(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle.
t = turtle.Turtle()
t.speed(ANIMATION_SPEED)
t.pencolor("#FFFFFF")
t.pensize(2)
# Move the turtle to the starting point.
t.penup()
t.goto(-(diameter/2), 40)

# Draw the octagon.
t.left(90)
t.pendown()
for i in range(1, NUM_SIDES + 2):  # Number of sides + 2 steps for half a side
    if i == 1:
        t.forward(LENGTH/2)
    elif i == NUM_SIDES + 1:
        t.right(ANGLE)
        t.forward(LENGTH / 2)
    else:
        t.right(ANGLE)
        t.forward(LENGTH)
    print(i)
t.penup()
turtle.hideturtle()
# Display 'STOP'
turtle.color('#FFFFFF')
style = ('Segoe UI Semibold', 50, 'normal')
turtle.write('STOP', font=style, align='center')
turtle.hideturtle()
turtle.write("STOP", False, 'Center', style)
turtle.mainloop()
