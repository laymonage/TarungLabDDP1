'''
A program for adding line number to each line of an existing text-file and
write the result to a new text file.
'''

def main():
    '''
    Main program
    '''
    input_file = input("Enter your input text file: ")
    output_file = input("Enter your output text file: ")
    text = open(input_file)                 # Open file for read-only
    new_text = open(output_file, "w")       # Open file for writing
    lines = text.readlines()                # Read text per lines
    line_number = 1                         # New var to track line number
    for line in lines:
        numbered_line = put_number(line_number, line)
        print(numbered_line, file=new_text, end='')
        line_number += 1
        # Put the line number to line
        # Print without additional newline
        # Increment line number for next iteration
    print()
    text.close()
    new_text.close()

def put_number(line_number, line):
    """
    Return a string. The `line_number` is formatted as 3 digits
    number with a dot and a space preceding the `line`. The empty
    space before line number will be replaced by '0's.

    Example:
    >>> put_number(1, "Hello World!")
    '001. Hello World'
    """
    return "{:03d}. {}".format(line_number, line)

main()
