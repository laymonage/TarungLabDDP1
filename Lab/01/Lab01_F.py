# import turtle module to add turtle's method
import turtle

sides = int(input("Number of sides:  "))
distance = int(input("Side's length: "))

turtle.color('blue')    # set the pen's color to blue
turtle.pendown()        # start drawing

deg = 360 / sides               # calculate the turn
for i in range(sides):
    turtle.forward(distance)    # by using loop, turn and
    turtle.left(deg)            # move the turtle forward

turtle.hideturtle()     # hide the turtle/arrow
turtle.exitonclick()    # close the window on click event
