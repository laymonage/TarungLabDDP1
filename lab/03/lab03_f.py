'''
Python program to do number representation conversion:
1. from decimal integer to hexadecimal string
2. from hexadecimal string to decimal integer
'''

print("""Lab 03
From decimal to hexadecimal
---------------------------""")

# Get the decimal value
# Initialize an empty string
# Make one temporary variable for decimal value

num = dec = int(input("Give a positive integer in decimal representation: "))
str_hex = ""

# While the temporary variable num is non-zero
# Calculate the remainder of decimal value divided by 16
# If it yields more than 9, we have to convert it into char using ascii table
# code for the char [a, b, c, d, e, f] which starts from 97 to 102
# else use plain str() and concatenate to str_hex
# Divide num by 16 using integer quotient for the next iteration

while num:
    digit = num % 16
    if digit > 9:
        str_hex = chr(digit + 87) + str_hex
    else:
        str_hex = str(digit) + str_hex
    num = num // 16

# str_hex will be a valid hex value by the end of iterations

print("The hexadecimal representation of {} is 0x{}".format(dec, str_hex))

print("""
From decimal to hexadecimal
---------------------------""")

# Get the hexadecimal value
# Initialize new decimal and power variable

str_hex = input("Give a positive integer in hexadecimal representation: ")
str_hex = str_hex.lower().lstrip('0x')
dec = pwr = 0

# For each digit from last to first
# If it's an alphabet, use it's ascii table code subtracted by 87
# so it directly maps to it's hex value
# else turn it into plain int
# After that multiply it by power according to its position
# Add to decimal value

for char in str_hex[::-1]:
    if char >= 'a':
        dec += (ord(char) - 87) * 16 ** pwr
    else:
        dec += int(char) * 16 ** pwr
    pwr += 1

# The decimal value will be complete by the end of iterations

print("The decimal representation of 0x{} is {}".format(str_hex, dec))

print("Thanks for using this program.")
input("Press Enter to continue ...") # Hold the screen display
