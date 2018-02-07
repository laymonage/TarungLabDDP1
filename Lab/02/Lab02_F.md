# Soal Tutorial

## Bagian A

You will use Turtle graphics like in Lab 01.
1. Use a `for` statement to draw a regular polygon given the number of sides
   provided by the user.
2. Add the capability to your program to fill polygons with a color indicated
   by a combination of the colors `red`, `green`, and `blue` provided by the
   user.

Your program will work as follows:
1. Prompt the user for the number of sides of a regular polygon.
2. Prompt the user for the color components: R(red component), G(green
   component), B(blue component). Make a color from these three components.
3. Draw the polygon using a `for` statement, without filling it with given
   color.
4. Move to a new position and draw again the polygon using a `for` statement
   and fill it with the given color.

### First, try it!
The first thing you should do is try out some of the turtle commands by just
typing them in the IDLE window. You can get a much better feel for how the
whole thing works by just trying it.

### Regular Polygon

The formula for the *total degrees* of all angles on the inside of a regular
polygon with *n* sides is `180*(n - 2)` so each *interior angle* is
`180*(n - 2) / n`.
From that you can calculate how much to turn (*exterior angle*):
`180 - 180*(n - 2) / n` = *???*
Use a `for` statement to draw the regular polygon with n sides.
The length of a side gets shorter as n gets larger. When n = 4, the length of
a side is 100.

### Loops

`for` is useful when you know how many times you want repeatedly do something,
e.g. you know how many sides of a polygon you want to draw.

### Mixing Colors

Your program will read in color values from the user and then use the methods
in the turtle module to draw the polygons filled with the color indicated.
There are many ways to create a color but a common one used in computer
graphics is the process of additive color (see
http://en.wikipedia.org/wiki/Additive_color). Combining different amounts of
`red`, `green` and `blue` can create most colors.

For example, here is how to draw a yellow circle: 1 red + 1 green + 0 blue.
Type the following stateents one by one in the IDLE shell and see what
happens. What color do you get from 0.3 red + 0.7 green + 0.6 blue?

```python
>>> import turtle
>>> turtle.color(1, 1, 0)
>>> turtle.begin_fill()
>>> turtle.circle(80)
>>> turtle.end_fill()
>>> turtle.hideturtle()
>>> turtle.bye()
```

Ikuti kerangka program di bawah ini, dengan mengisi bagian-bagian yang masih
kosong menurut komentar ybs.

```python
## Author: ...................
## File name: lab02a.py
## using turtle to draw regular polygons
## prompt user for the number of sides and the color component (r, g, b)
import turtle

turtle.shape('turtle')
turtle.title('Lab 02 -- 2017')

# get the number of sides from user
n = int(turtle.textinput("Lab 02", "The number of sides: "))

# draw the n-side polygon using a for loop
# the length of a side is getting shorter as n getting larger
# When n = 4, the length of a side is 100.
...................
...................
...................

# get the value of red color from user

r = float(...................)

# get the value of green color from user

g = ...................

# get the value of blue color from user

b = ...................

# create the color from rgb values given by user
...................

# move the turtle to a new location below
...................
...................
...................
...................

# draw a regular polygon with n sides and color(r,g,b)
# use a for loop
...................
...................
...................
...................
...................

# make the turtle invisible
turtle.hideturtle()

# message for user
print("Please click on the graphics window to exit ...")

# wait for user to click on the screen to exit
turtle...................

# the end
```

## Part B

In order to complete the following program, you should write a sequence of
*simultaneous assignment* statements of the form `x, y = y, x` to sort
(mengurutkan) the values referenced by the variables **number1, number2,
number3, number4, number5** so that when printed their values are in sorted
order from the smallest to the largest. Three (3) simultaneous assignments
will be enough.

```python
## Author: ...................
## File name: lab02b.py
## using simultaneous assignment to sort data

# five variables with given values
number1 = 23
number2 = 7
number3 = 3
number4 = -6
number5 = 19
print("Initial data: ")
print(number1, number2, number3, number4, number5)
# the output expected: 23 7 3 -6 19

# simultaneous assignment to swap the values
# of the variables; two variables at a time
    .
    .
    .
    .

# Display the sorted values
print("Sorted data, from smallest to largest: ")
print(number1, number2, number3, number4, number5)
# the output expected: -6 3 7 19 23
```

Happy programming! 'Met ngoding!

L. Y. Stefanus

---

Taken from `lab02_ddp1_2017.pdf` (Tutorial Lab 2 DDP1 F -- 06 September 2017)
