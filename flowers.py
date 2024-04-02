import turtle
from colorsys import hsv_to_rgb

# Setup
turtle.speed(0)
turtle.pensize(3)
turtle.bgcolor("black")

# Variables
hue = 0.0

# Drawing loop
for i in range(200):
    # Convert HSV to RGB for the pen color
    col = hsv_to_rgb(hue, 1, 1)
    turtle.pencolor(col)

    # Update the hue value
    hue += 0.005

    # Draw the petals
    turtle.circle(5 - i, 100)
    turtle.lt(80)
    turtle.circle(5 - i, 100)
    turtle.rt(100)

# Close the turtle graphics window
turtle.done()