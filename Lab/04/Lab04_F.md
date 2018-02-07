# Soal Tutorial

## Part A: Writing a function definition

Write a function `put_number()` that takes a sentence (a string) and a number
(an int) as arguments and then returns the string obtained from concatenating
the number as a string in front of the sentence. Assume that the number, which
is ≤ 999, occupies 5 spaces, including a point. If the number consists of less
than three digits, add **zeros**. You have to use **format string**.

For examples:
```
>>> put_number(12, 'When we were younger and free')
'012. When we were younger and free'
>>> put_number(7, "They say that time's supposed to heal you")
"007. They say that time's supposed to heal you"
>>> st = put_number(890, "Python is an object-oriented programming language.")
>>> st
'890. Python is an object-oriented programming language.'
```

Test your function in IDLE. If you have already gotten it right, then go to
Part B where the function put_number() will be used.

## Part B: Processing a text file
Construct a program for adding a line number to each line of an existing
text-file and write the result to a new text file. You have to use the
function `put_number()` from Part A. Each line number occupies 5 spaces. Your
program prompts the user for an input file name and an output file name.

For example, if the input file contains:
```
"Hello"
-- Songwriters: ADELE ADKINS, GREGORY KURSTIN

Hello, it's me
I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya
But I ain't done much healing

Hello, can you hear me?
I'm in California dreaming about who we used to be
When we were younger and free
```
then the output file will contain:
```
001. "Hello"
002. -- Songwriters: ADELE ADKINS, GREGORY KURSTIN
003.
004. Hello, it's me
005. I was wondering if after all these years you'd like to meet
006. To go over everything
007. They say that time's supposed to heal ya
008. But I ain't done much healing
009.
010. Hello, can you hear me?
011. I'm in California dreaming about who we used to be
012. When we were younger and free
```

Happy programming! 'Met ngoding!

L. Y. Stefanus

--

Taken from `lab04_fprog2017.pdf` (Tutorial Lab 4 DDP1 F -- 27 September 2017)
