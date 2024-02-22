#Anthony Mendes
#stop sign

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
# Move the turtle to the starting point.
turtle.penup()
x,y = -50,-100
turtle.goto(x,y)
turtle.pendown()

x,y = -100, 20


# Draw the octagon.
turtle.pencolor('red')
turtle.fillcolor('red')

turtle.begin_fill()

for i in range(NUM_SIDES):

    x,y = x + turtle.xcor()/2, (y) + turtle.ycor()/2

    turtle.forward(LENGTH)
    turtle.left(ANGLE)

turtle.end_fill()
# Draw outside the octagon.
turtle.penup()
x,y = -55,-120
turtle.pensize(8)
turtle.goto(x,y)
turtle.pendown()

for i in range(NUM_SIDES):

    x,y = x + turtle.xcor()/1.8, (y) + turtle.ycor()/1.8

    turtle.forward(LENGTH + 15)
    turtle.left(ANGLE)

# Display 'STOP'
turtle.penup()

turtle.penup()
x,y = -60, 0
turtle.goto(x,y)
turtle.pendown()

turtle.pencolor('white')

# write text
# styling font

turtle.write("STOP", font=("Arial",
                                    35, "bold"))

turtle.ht()
turtle. mainloop()