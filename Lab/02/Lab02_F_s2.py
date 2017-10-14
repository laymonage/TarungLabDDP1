'''
Using simultaneous assignments to sort data.
'''

# Five variables with given values

number1 = 23
number2 = 7
number3 = 3
number4 = -6
number5 = 19

print("Initial data: ")
print(number1, number2, number3, number4, number5)
# The output expected: 23 7 3 -6 19

# Simultaneous assignment to swap the values
# of the variables; two variables at a time
number1, number4 = number4, number1
number2, number3 = number3, number2
number4, number5 = number5, number4

# Display the sorted values
print("Sorted data, from smallest to largest: ")
print(number1, number2, number3, number4, number5)
# The output expected: -6 3 7 19 23
