'''
Using Turtle Graphics to draw a blue polygon with customizable number and
length of sides according to user's input.
'''

import turtle

sides = int(input("Number of sides:  "))
distance = int(input("Side's length: "))

turtle.color('blue')    # Set the pen's color to blue
turtle.pendown()        # Start drawing

deg = 360 / sides               # Calculate the turn
for i in range(sides):
    turtle.forward(distance)    # By using loop, turn and
    turtle.left(deg)            # move the turtle forward

turtle.hideturtle()     # Hide the turtle/arrow
turtle.exitonclick()    # Close the window on click event
