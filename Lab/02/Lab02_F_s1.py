'''
Using turtle to draw regular polygons
prompt user for the number of sides and the color components (r, g, b).
'''
import turtle

# Get the turtle ready in position
turtle.hideturtle()
turtle.up()
turtle.goto(-50, 5)
turtle.shape('turtle')
turtle.title('Labe 02 -- 2017')

# Ask the user for the number of poly's sides
sides = int(turtle.textinput("Lab 02", "The number of sides: "))

# User will input RGB values [0.0 - 1.0]
r = float(turtle.textinput("Lab 02", "Value of red [0.0 - 1.0]"))
g = float(turtle.textinput("Lab 02", "Value of green [0.0 - 1.0]"))
b = float(turtle.textinput("Lab 02", "Value of blue [0.0 - 1.0]"))

turtle.color(r, g, b)       # Assign the user specified color to turtle

deg = 360 / sides	        # Calculate the turn
length = 400 / sides
turtle.showturtle()
turtle.down()
for i in range(sides):
    turtle.forward(length)  # By using loop, turn and
    turtle.left(deg)        # Move the turtle forward
turtle.up()

# Get the turtle in position for another poly
turtle.goto(-50, -5)

turtle.down()
turtle.begin_fill()         # Call turtle.begin_fill() to start filling poly
for i in range(sides):
    turtle.forward(length)  # By using loop, turn and
    turtle.right(deg)       # move the turtle forward
turtle.end_fill()           # Call turtle.end_fill() to finish filling poly
turtle.up()

turtle.hideturtle()         # Hide the turtle/arrow

print("Please click on the graphics window to exit . . .")
turtle.exitonclick()        # Close the window on click event
