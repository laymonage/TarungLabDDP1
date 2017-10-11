# Soal Tutorial

## First, let's experiment!

The first thing you should do is try out some of the turtle commands by just
typing them in the IDLE window. You can get a much better feel for how the
whole thing works by just trying it.

1. Type the following program using the IDLE editor and save it in a file:
   `turtleSample01.py`
[**WARNING: Do not save it in a file named turtle.py**]

```python
## turtleSample01.py
## using turtle to draw a triangle
import turtle

# let's start up a Turtle Graphics window with a red turtle
turtle.color('red')

# put it down so all movement will show as a red line
turtle.pendown()

# move forward by 100 in current direction
turtle.forward(100)

# rotate direction of turtle by 120 degrees
turtle.right(120)

# move forward by 100 in current direction
turtle.forward(100)

# rotate direction of turtle by 120 degrees
turtle.right(120)

# move forward by 100 in current direction
turtle.forward(100)

# make the turtle invisible
turtle.hideturtle()

# wait for user to click on the screen to exit
turtle.exitonclick()
```

2. Run the program to see what it does.

3. Modify the program to draw a **green hexagon** (regular polygon with 6
   sides). You have to calculate first the suitable turning angle, using the
   formula discussed below.

   Here is some useful information about regular polygon.

   **Regular Polygon**

   The formula for **total degress** of all angles on the inside of a regular
   polygon with n sides is `180*(n-2)` so each interior angle is `180*(n-2)/n`.
   From that you can calculate how much to turn (exterior angle):
   `180-180*(n-2)/n` = `360/n`

4. Modify the previos program to draw a blue regular polygon according to
   user's input:

   1. Prompt the user to input the number of sides and store the string in a
      variable. Then convert the string to an integer and store it in a new
      variable.
   2. Prompt the user to input the length of each side and store the string in
      a variable. Then convert the string to an integer and store it in a new
      variable.
   3. Using for loop, draw a blue regular polygon of given number of sides.
      Each side of the polygon has a length as determined by the user's input.
   4. Save your work (source code) to a file:
      `<your_name>_<NPM>_lab01.py`, such as
      `taylor_swift_1706837915_lab01.py`.
      Submit your source code file using the submit link at SCeLE.

That's all for today. Happy programming! `Met ngoding!

L. Y. Stefanus

P.S. : Taken from lab01_ddp2017.pdf (Tutorial Lab 1 DDP1 -- 30 August 2017)